"""Transactional candidate persistence and exact database readback."""
from decimal import Decimal
import hashlib
import json
from sqlalchemy import select
from .models import Candidate, Document, DocumentVersion, ExtractionRun
from financial_pipeline.extraction.parser import RULES

def persist(source, rows, summary, sessions):
    if len(rows) != len(RULES) or {row['metric_code'] for row in rows} != set(RULES):
        raise ValueError('Persistence requires exactly one candidate for each core metric')
    # Collection timestamps/log IDs vary on each refresh; fact identity depends on
    # the selected PDF, target, rules and OCR content, not on when HTML was fetched.
    stable_fields = {'ticker', 'fiscal_year', 'sha256', 'scope', 'path', 'url', 'final_url',
                     'expected_legal_name', 'expected_scope', 'expected_period', 'expected_assurance', 'expected_language',
                     'context_status', 'acquisition_mode', 'published_at', 'catalog_url', 'catalog_anchor',
                     'catalog_candidate', 'catalog_context', 'selection_reason', 'collector_code_sha256', 'source_config_sha256'}
    canonical = {'source': {k:v for k,v in source.items() if k in stable_fields}, 'rows': rows,
                 'processing': {k:v for k,v in summary.items() if k not in {'checked_at', 'recognition_cache_entries', 'recognition_recomputed_entries'}}}
    digest = hashlib.sha256(json.dumps(canonical, sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()
    with sessions.begin() as db:
        doc = db.scalar(select(Document).where(Document.ticker == source['ticker'],
                                               Document.fiscal_year == source['fiscal_year'], Document.scope == 'consolidated'))
        if not doc:
            doc = Document(ticker=source['ticker'], fiscal_year=source['fiscal_year'], scope='consolidated')
            db.add(doc)
            db.flush()
        version = db.scalar(select(DocumentVersion).where(DocumentVersion.sha256 == source['sha256']))
        if not version:
            version = DocumentVersion(document_id=doc.id, sha256=source['sha256'], path=source['path'], source=source)
            db.add(version)
            db.flush()
        elif version.document_id != doc.id:
            raise ValueError('PDF version belongs to a different report target')
        run = db.scalar(select(ExtractionRun).where(ExtractionRun.input_sha256 == digest))
        if not run:
            run = ExtractionRun(document_version_id=version.id, input_sha256=digest,
                                pipeline='all_pages_paddle_detection_vietocr_content_parser_v1',
                                provenance={'source': source, 'processing': summary})
            db.add(run)
            db.flush()
            for row in rows:
                db.add(Candidate(extraction_run_id=run.id, metric_code=row['metric_code'],
                                 value=Decimal(row['value_vnd']) if row['value_vnd'] is not None else None,
                                 unit='VND', status=row['status'], evidence=row))
        run_id = run.id
    with sessions() as db:
        stored = db.scalars(select(Candidate).where(Candidate.extraction_run_id == run_id)).all()
        if len(stored) != len(RULES):
            raise ValueError('Readback target count mismatch')
        by_code = {c.metric_code: c for c in stored}
        output = []
        for row in rows:
            c = by_code[row['metric_code']]
            actual = None if c.value is None else format(c.value, 'f')
            if actual != row['value_vnd'] or c.evidence != row:
                raise ValueError('Database round-trip mismatch')
            evidence = c.evidence.get('evidence') or {}
            output.append({'ticker': source['ticker'], 'fiscal_year': source['fiscal_year'],
                           'metric_code': c.metric_code, 'value_vnd': actual, 'status': c.status,
                           'reason': row['reason'], 'pdf_page': None if evidence.get('pdf_page_index') is None else evidence['pdf_page_index']+1,
                           'raw_value': evidence.get('raw_value'), 'raw_unit': evidence.get('raw_unit'),
                           'extraction_run_id': run_id})
    return run_id, output

