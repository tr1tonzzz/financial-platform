"""A interrupted/changed processing run must regenerate data, never silently reuse it."""
import hashlib
import json
from pathlib import Path
import sys
import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'src'))
from financial_pipeline.cache import detection_cache, recognition_cache_matches


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding='utf-8')


@pytest.fixture
def cached(tmp_path):
    # Bytes are synthetic hash fixtures, not photos or company OCR results.
    work = tmp_path/'runtime/processing/fixture'
    image, crop = work/'detection/image.png', work/'detection/crop.png'
    image.parent.mkdir(parents=True)
    image.write_bytes(b'synthetic image hash fixture')
    crop.write_bytes(b'synthetic crop hash fixture')
    save(work/'source.json', {'sha256': 'pdf-hash', 'pdf_pages': 1})
    save(work/'detection/run.json', {'finished_at': 'synthetic', 'error': None, 'pdf_sha256': 'pdf-hash',
                                   'pdf_pages': 1, 'pages': [{'pdf_page_index': 0}], 'dpi': 180,
                                   'detector_code_sha256': 'code-v1', 'model_files_sha256': {'weights': 'model-v1'}, 'packages': {'paddle': '1'}})
    save(work/'detection/page-001.json', {'document_sha256': 'pdf-hash', 'pdf_page_index': 0,
                                        'image': str(image.relative_to(tmp_path)), 'image_sha256': hashlib.sha256(image.read_bytes()).hexdigest(),
                                        'entries': [{'crop_path': str(crop.relative_to(tmp_path)), 'crop_sha256': hashlib.sha256(crop.read_bytes()).hexdigest()}]})
    return tmp_path, work


def decide(cached):
    root, work = cached
    return detection_cache(work, root, 'code-v1', {'weights': 'model-v1'}, {'paddle': '1'})


def test_complete_unchanged_run_can_be_reused(cached):
    assert decide(cached).reusable


@pytest.mark.parametrize('change', [{'finished_at': None}, {'error': 'interrupted'}, {'pages': []},
                                  {'detector_code_sha256': 'upgraded'}, {'packages': {'paddle': '2'}}, {'dpi': 225}])
def test_incomplete_or_changed_run_requires_regeneration(cached, change):
    _, work = cached
    p = work/'detection/run.json'
    save(p, {**json.loads(p.read_text()), **change})
    assert not decide(cached).reusable


def test_modified_crop_requires_regeneration(cached):
    _, work = cached
    (work/'detection/crop.png').write_bytes(b'changed fixture')
    assert not decide(cached).reusable


def test_crop_reference_outside_processing_directory_cannot_be_reused(cached):
    root, work = cached
    outside = root/'outside.png'
    outside.write_bytes(b'synthetic crop hash fixture')
    p = work/'detection/page-001.json'
    page = json.loads(p.read_text())
    page['entries'][0]['crop_path'] = str(outside.relative_to(root))
    save(p, page)
    assert not decide(cached).reusable


def test_recognizer_cache_invalidates_when_code_or_runtime_changes():
    page = {'document_sha256': 'pdf', 'recognizer_model_sha256': 'model', 'config_sha256': 'config',
            'recognizer_code_sha256': 'code', 'runtime_packages': {'torch': '1'}}
    assert recognition_cache_matches(page, 'pdf', 'model', 'config', 'code', {'torch': '1'})
    assert not recognition_cache_matches(page, 'pdf', 'model', 'config', 'updated', {'torch': '1'})
    assert not recognition_cache_matches(page, 'pdf', 'model', 'config', 'code', {'torch': '2'})
    assert not recognition_cache_matches({}, 'pdf', 'model', 'config', 'code', {'torch': '1'})
