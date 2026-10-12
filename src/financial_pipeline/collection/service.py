"""Reusable collection service; no OCR, CLI, database or company PDF URLs here."""
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
import uuid
from .adapters import initial_catalog, parse_catalog
from .models import CollectionError, classify, select_candidate
from .transport import HttpClient, validate_url


@dataclass(frozen=True)
class CollectionResult:
    work_dir: Path
    source: dict
    observation_path: Path


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')
    temporary.replace(path)


def discover(target, source, client, progress=None):
    if not 1 <= source['max_pages'] <= 100:
        raise CollectionError('invalid_source_config', 'max_pages must be 1–100')
    first = initial_catalog(source, target)
    pending, visited, candidates, events, fingerprints = {1: first}, {}, {}, [], set()
    progress = progress if progress is not None else {}
    progress.update(complete=False, pages_visited=0, catalog_requests=events)
    duplicate_conflicts_outside_target = 0
    while pending:
        page_number = min(pending)
        url = pending.pop(page_number)
        if page_number in visited:
            continue
        if page_number > source['max_pages']:
            raise CollectionError('catalog_page_limit', 'Pagination exceeds the registered page limit', {'page': page_number})
        response = client.fetch(url, source['catalog_hosts'], 4*1024*1024)
        if response.event['content_type'] not in ['text/html', 'application/xhtml+xml']:
            raise CollectionError('not_catalog_html', 'Catalog response is not HTML')
        entries, links, coverage = parse_catalog(response.body, source, response.event['final_url'])
        if coverage['page'] != page_number:
            raise CollectionError('pagination_redirect_mismatch', 'Requested and returned catalog page differ')
        if coverage['page_count'] > source['max_pages']:
            raise CollectionError('catalog_page_limit', 'Declared catalog coverage exceeds the limit')
        if response.event['sha256'] in fingerprints:
            raise CollectionError('repeated_catalog_page', 'Different pages returned identical HTML; coverage is unverified')
        fingerprints.add(response.event['sha256'])
        visited[page_number] = coverage
        events.append({**response.event, **coverage, 'pdf_links': len(entries)})
        progress.update(pages_visited=len(visited), expected_pages=max(x['page_count'] for x in visited.values()))
        for candidate in entries:
            candidate['metadata'] = classify(candidate['title'], candidate['url'], target)
            if candidate['metadata']['eligible']:
                validate_url(candidate['url'], source['download_hosts'])
            # Duplicate anchors/pages with identical report metadata are one candidate.
            previous = candidates.get(candidate['url'])
            if previous and any(previous[k] != candidate[k] for k in ['published_at', 'metadata']):
                if not previous['metadata']['eligible'] and not candidate['metadata']['eligible']:
                    duplicate_conflicts_outside_target += 1
                    continue  # Do not let contradictory metadata for a rejected historical PDF choose/block the target.
                raise CollectionError('conflicting_duplicate_link', 'One PDF URL has conflicting target metadata across catalog pages', {'url': candidate['url']})
            candidates[candidate['url']] = candidate
        for link in links:
            parameter = coverage.get('pagination_parameter', 'page')
            start = coverage.get('pagination_start', 1)
            page = int(parse_qs(urlsplit(link).query).get(parameter, [str(start)])[0])-start+1
            if page not in visited:
                pending[page] = link
    maximum = max((x['page_count'] for x in visited.values()), default=1)
    if set(visited) != set(range(1, maximum+1)):
        raise CollectionError('incomplete_catalog', 'Not every declared catalog page was visited',
                              {'visited': sorted(visited), 'expected_pages': maximum})
    counts = Counter(c['metadata']['reason'] for c in candidates.values() if not c['metadata']['eligible'])
    summary = {'complete': True, 'scope': 'registered financial-report catalog; requested-year filter when supported',
               'pages_visited': len(visited), 'expected_pages': maximum, 'unique_pdf_links': len(candidates),
               'matching_candidates': sum(c['metadata']['eligible'] for c in candidates.values()),
               'rejected_counts': dict(counts), 'non_target_duplicate_conflicts': duplicate_conflicts_outside_target, 'catalog_requests': events}
    return list(candidates.values()), summary


def collect_report(target, registry, workspace, client=None):
    workspace = Path(workspace).resolve()
    identifier = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'_'+uuid.uuid4().hex[:8]
    observation_path = workspace/'data/collections'/f'{target.ticker}-{target.year}'/(identifier+'.json')
    observation = {'target': asdict(target), 'status': 'started', 'started_at': datetime.now(timezone.utc).isoformat()}
    client = client or HttpClient()
    try:
        source_config = registry['sources'].get(target.ticker)
        if registry.get('schema_version') != 1 or not source_config:
            raise CollectionError('unregistered_company', 'Register the company catalog before collection')
        observation['discovery'] = {}
        candidates, summary = discover(target, source_config, client, observation['discovery'])
        observation['discovery'] = summary
        chosen, selection_reason = select_candidate(candidates)
        observation['selected'] = chosen
        response = client.fetch(chosen['url'], source_config['download_hosts'], 30*1024*1024)
        body = response.body
        if not body.startswith(b'%PDF-'):
            raise CollectionError('not_pdf', 'Selected URL returned non-PDF bytes')
        # Validate structure/encryption before OCR; PDF text is never used as OCR output.
        import pymupdf
        try:
            with pymupdf.open(stream=body, filetype='pdf') as pdf:
                if pdf.is_encrypted or pdf.page_count < 1:
                    raise CollectionError('unreadable_pdf', 'PDF is empty or encrypted')
                pdf_pages = pdf.page_count
        except CollectionError:
            raise
        except Exception as exc:
            raise CollectionError('unreadable_pdf', str(exc)) from exc
        sha = hashlib.sha256(body).hexdigest()
        raw = workspace/'data/raw'/(sha+'.pdf')
        raw.parent.mkdir(parents=True, exist_ok=True)
        if raw.exists():
            if hashlib.sha256(raw.read_bytes()).hexdigest() != sha:
                raise CollectionError('existing_pdf_corrupt', 'Existing PDF does not match its content hash')
        else:
            temporary = raw.with_suffix('.pdf.tmp')
            temporary.write_bytes(body)
            temporary.replace(raw)
        work = workspace/'runtime/processing'/f'{target.ticker}-{target.year}-{sha[:12]}'
        result_source = {'ticker': target.ticker, 'fiscal_year': target.year,
                         'expected_legal_name': source_config['legal_name'], 'expected_scope': target.scope,
                         'expected_period': target.period, 'expected_assurance': target.assurance, 'expected_language': target.language,
                         'url': chosen['url'], 'final_url': response.event['final_url'],
                         'retrieved_at': response.event['retrieved_at'], 'published_at': chosen['published_at'],
                         'sha256': sha, 'bytes': len(body), 'pdf_pages': pdf_pages, 'path': str(raw.relative_to(workspace)),
                         'acquisition_mode': 'automatic_official_catalog', 'context_status': 'pending_ocr_verification',
                         'catalog_url': initial_catalog(source_config, target), 'catalog_anchor': chosen.get('anchor_text', chosen['title']),
                         'catalog_candidate': chosen['metadata'], 'selection_reason': selection_reason,
                         'discovery': summary, 'download_request': response.event,
                         'collection_observation': str(observation_path.relative_to(workspace))}
        result_source['collector_code_sha256'] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in Path(__file__).parent.glob('*.py')}
        if 'context_text' in chosen:
            result_source['catalog_context'] = chosen['title']
        result_source['source_config_sha256'] = hashlib.sha256(json.dumps(source_config, sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()
        save_json(work/'source.json', result_source)
        observation.update(status='collected_pending_ocr_verification', pdf_sha256=sha,
                           pdf_pages=pdf_pages, selection_reason=selection_reason, source_path=str((work/'source.json').relative_to(workspace)))
        return CollectionResult(work, result_source, observation_path)
    except CollectionError as exc:
        observation.update(status=exc.code, error=str(exc), details=exc.details)
        raise
    except Exception as exc:
        observation.update(status='unexpected_error', error=f'{type(exc).__name__}: {exc}')
        raise
    finally:
        observation['finished_at'] = datetime.now(timezone.utc).isoformat()
        save_json(observation_path, observation)
