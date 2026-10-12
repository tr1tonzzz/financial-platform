"""Generic writer persistence checks in disposable PostgreSQL schemas."""
import sys
import uuid
from pathlib import Path
import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, select, func, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from financial_pipeline.storage.database import Database
from financial_pipeline.storage.models import Candidate, Document, ExtractionRun
from financial_pipeline.storage import repository as storage
from financial_pipeline.storage.migrate import upgrade_schema
from financial_pipeline.settings import load_settings
ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture
def isolated(monkeypatch):
    settings = load_settings(ROOT/'config/pipeline.json')
    if not settings.database_env.exists():
        pytest.skip('Local PostgreSQL profile not configured')
    database = Database.from_env_file(settings.database_env)
    engine = database.engine
    schema = 'generic_test_' + uuid.uuid4().hex
    with engine.begin() as connection:
        connection.execute(text(f'CREATE SCHEMA {schema}'))
    temporary = create_engine(engine.url, connect_args={'options': f'-csearch_path={schema}'})
    upgrade_schema(temporary)
    sessions = sessionmaker(temporary, expire_on_commit=False)
    monkeypatch.setattr(storage, 'persist', lambda source, rows, summary, supplied_sessions=None, original=storage.persist: original(source, rows, summary, supplied_sessions or sessions))
    try:
        yield sessions
    finally:
        temporary.dispose()
        with engine.begin() as connection:
            connection.execute(text(f'DROP SCHEMA {schema} CASCADE'))
        database.engine.dispose()


def fixtures(ticker, sha):
    source = {'ticker': ticker, 'fiscal_year': 2025, 'sha256': sha*64, 'path': 'synthetic-not-a-report.pdf'}
    values = ['-250', None, '0', '123456789012345678901', '2000', '3000']
    rows = [dict(metric_code=code, value_vnd=value, status='pending_review' if value is not None else 'missing_or_ambiguous',
                 reason=None if value is not None else 'synthetic missing', evidence=None, fixture=True)
            for code,value in zip(storage.RULES, values)]
    return source, rows


def test_two_reports_exact_decimal_null_and_idempotency(isolated):
    for ticker, sha in [('FIXTURE_A', 'a'), ('FIXTURE_B', 'b')]:
        source, rows = fixtures(ticker, sha)
        run_id, output = storage.persist(source, rows, {'checked_at': 'first', 'fixture': True})
        repeated_id, repeated = storage.persist(source, rows, {'checked_at': 'later', 'fixture': True})
        assert run_id == repeated_id and output == repeated
        assert [r['value_vnd'] for r in output] == [r['value_vnd'] for r in rows]
    with isolated() as db:
        assert db.scalar(select(func.count()).select_from(Document)) == 2
        assert db.scalar(select(func.count()).select_from(ExtractionRun)) == 2
        assert db.scalar(select(func.count()).select_from(Candidate)) == 12


def test_constraint_failure_rolls_back_whole_report(isolated):
    source, rows = fixtures('INVALID', 'c')
    rows[1]['status'] = 'pending_review'
    with pytest.raises(IntegrityError):
        storage.persist(source, rows, {'fixture': True})
    with isolated() as db:
        assert db.scalar(select(func.count()).select_from(Document)) == 0
        assert db.scalar(select(func.count()).select_from(Candidate)) == 0


@pytest.mark.parametrize('mutation', ['partial', 'duplicate'])
def test_invalid_target_set_never_commits_partial_report(isolated, mutation):
    source, rows = fixtures('INCOMPLETE', 'e')
    if mutation == 'partial':
        rows = rows[:-1]
    else:
        rows[-1] = rows[0].copy()
    with pytest.raises(ValueError, match='exactly one candidate'):
        storage.persist(source, rows, {'fixture': True})
    with isolated() as db:
        assert db.scalar(select(func.count()).select_from(Document)) == 0
        assert db.scalar(select(func.count()).select_from(ExtractionRun)) == 0
        assert db.scalar(select(func.count()).select_from(Candidate)) == 0


def test_store_service_validates_full_provenance_exports_and_cleans(isolated, tmp_path, monkeypatch):
    """Synthetic OCR boundary, real PostgreSQL; not a financial accuracy test."""
    from dataclasses import replace
    import hashlib
    import json
    from financial_pipeline.storage import service
    from financial_pipeline.ocr import detection, recognition
    workspace = tmp_path/'workspace'
    work = workspace/'runtime/processing/synthetic'
    for directory in [work/'detection', work/'ocr', workspace/'data/raw']:
        directory.mkdir(parents=True)
    def save(path, payload):
        path.write_text(json.dumps(payload), encoding='utf-8')
    def sha(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()
    pdf = workspace/'data/raw/synthetic.pdf'
    pdf.write_bytes(b'synthetic boundary fixture, not a real report')
    config = tmp_path/'config.yml'
    config.write_text('synthetic configuration')
    lock = tmp_path/'model.json'
    save(lock, {'weights_sha256': 'f'*64})
    settings = replace(load_settings(ROOT/'config/pipeline.json'), workspace=workspace,
                       vietocr_config=config, vietocr_lock=lock)
    source, rows = fixtures('SERVICE', 'f')
    source.update(path=str(pdf.relative_to(workspace)), sha256=sha(pdf), pdf_pages=1,
                  acquisition_mode='automatic_official_catalog',
                  discovery={'complete': True, 'pages_visited': 1, 'expected_pages': 1},
                  catalog_candidate={'eligible': True})
    save(work/'source.json', source)
    crop = work/'detection/crop.png'
    crop.write_bytes(b'synthetic crop boundary')
    entry = {'id': '0:0', 'crop_path': str(crop.relative_to(workspace)), 'crop_sha256': sha(crop), 'preprocessing_version': 3}
    det_page = work/'detection/page-001.json'
    save(det_page, {'entries': [entry]})
    detector_run = {'finished_at': 'fixture', 'error': None, 'pdf_pages': 1, 'pdf_sha256': sha(pdf),
                    'pages': [{'pdf_page_index': 0}], 'dpi': 180, 'packages': {'fixture': 'test'},
                    'config': {'fixture': True}, 'model_files_sha256': {}, 'detector_code_sha256': sha(Path(detection.__file__))}
    recognition_run = {'finished_at': 'fixture', 'error': None, 'document_sha256': sha(pdf),
                       'recognizer_code_sha256': sha(Path(recognition.__file__)), 'packages': {'fixture': 'test'},
                       'pages': [{'pdf_page_index': 0, 'entries': 1}]}
    save(work/'detection/run.json', detector_run)
    save(work/'ocr/run.json', recognition_run)
    save(work/'ocr/page-001.json', {'pdf_page_index': 0, 'document_sha256': sha(pdf),
         'engine': 'PaddleDetection+VietOCR', 'config_sha256': sha(config), 'recognizer_model_sha256': 'f'*64,
         'recognizer_code_sha256': recognition_run['recognizer_code_sha256'], 'runtime_packages': recognition_run['packages'],
         'detection_result': str(det_page.relative_to(workspace)), 'detection_sha256': sha(det_page), 'entries': [entry]})
    monkeypatch.setattr(service, 'parse_report', lambda pages, source: (rows, {'fixture': True, 'context': {'verified': True},
                                                                         'present_count': 5, 'statement_pages': []}))
    first, destination = service.store_report(work, settings, isolated)
    assert {file.name for file in destination.iterdir()} == {'source.json', 'processing.json', 'candidates.json', 'database-readback.csv'}
    repeated, _ = service.store_report(work, settings, isolated, cleanup=True)
    assert first == repeated and not work.exists()
    with isolated() as db:
        assert db.scalar(select(func.count()).select_from(Candidate)) == 6


def test_catalog_refresh_does_not_duplicate_facts_but_rule_version_does(isolated):
    source, rows = fixtures('REFRESH', 'd')
    source.update(acquisition_mode='automatic_official_catalog', collector_code_sha256={'rules': 'v1'},
                  collection_observation='first.json', discovery={'catalog_requests': [{'retrieved_at': 'first'}]})
    first, _ = storage.persist(source, rows, {'fixture': True})
    refreshed = {**source, 'collection_observation': 'later.json', 'retrieved_at': 'later',
                 'discovery': {'catalog_requests': [{'retrieved_at': 'later', 'sha256': 'different HTML nonce'}]}}
    repeated, _ = storage.persist(refreshed, rows, {'fixture': True})
    assert first == repeated
    upgraded, _ = storage.persist({**refreshed, 'collector_code_sha256': {'rules': 'v2'}}, rows, {'fixture': True})
    assert upgraded != first
