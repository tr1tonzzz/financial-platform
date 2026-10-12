"""Processing caches are reusable only for the same inputs, code and runtime."""
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path


@dataclass(frozen=True)
class CacheDecision:
    reusable: bool
    reason: str


def verified_file(workspace, work, relative, digest):
    path = (workspace/relative).resolve()
    return path.is_relative_to(work.resolve()) and path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == digest


def detection_cache(work, workspace, code_sha256, model_hashes, packages, dpi=180):
    work, workspace = Path(work), Path(workspace)
    try:
        source = json.loads((work/'source.json').read_text(encoding='utf-8'))
        run = json.loads((work/'detection/run.json').read_text(encoding='utf-8'))
        if not run.get('finished_at') or run.get('error'):
            return CacheDecision(False, 'unfinished_or_failed_detection')
        if run.get('pdf_sha256') != source['sha256'] or run.get('pdf_pages') != source['pdf_pages']:
            return CacheDecision(False, 'different_document')
        if run.get('detector_code_sha256') != code_sha256 or run.get('model_files_sha256') != model_hashes or run.get('packages') != packages or run.get('dpi') != dpi:
            return CacheDecision(False, 'different_code_model_or_runtime')
        if {p['pdf_page_index'] for p in run['pages']} != set(range(source['pdf_pages'])):
            return CacheDecision(False, 'incomplete_page_coverage')
        for index in range(source['pdf_pages']):
            page = json.loads((work/'detection'/f'page-{index+1:03}.json').read_text(encoding='utf-8'))
            if page['document_sha256'] != source['sha256'] or page['pdf_page_index'] != index:
                return CacheDecision(False, 'different_page_identity')
            if not verified_file(workspace, work, page['image'], page['image_sha256']):
                return CacheDecision(False, 'missing_or_modified_page_image')
            if any(not verified_file(workspace, work, e['crop_path'], e['crop_sha256']) for e in page['entries']):
                return CacheDecision(False, 'missing_or_modified_crop')
        return CacheDecision(True, 'complete_same_inputs_code_model_runtime_and_files')
    except (OSError, ValueError, KeyError, TypeError):
        return CacheDecision(False, 'missing_or_invalid_cache_metadata')


def recognition_cache_matches(page, document_sha256, model_sha256, config_sha256, code_sha256, packages):
    return (page.get('document_sha256') == document_sha256
            and page.get('recognizer_model_sha256') == model_sha256
            and page.get('config_sha256') == config_sha256
            and page.get('recognizer_code_sha256') == code_sha256
            and page.get('runtime_packages') == packages)
