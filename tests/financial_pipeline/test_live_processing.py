"""Opt-in live regression: one real page, cache reuse and rejection of partial DB writes.

Set FINANCIAL_PIPELINE_LIVE=1. Normal test runs never contact official websites.
This test requires an idle processing workspace and records that only page 7 ran.
"""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
WS = ROOT/'var'
sys.path.insert(0, str(ROOT/'src'))

from financial_pipeline.collection import ReportTarget, collect_report
from financial_pipeline.cache import detection_cache

pytestmark = pytest.mark.skipif(os.getenv('FINANCIAL_PIPELINE_LIVE') != '1', reason='Opt-in real-source/model test')


def test_real_page_cache_and_partial_write_guard():
    from sqlalchemy import select, func
    from financial_pipeline.storage.database import Database
    from financial_pipeline.storage.models import Candidate
    from financial_pipeline.settings import load_settings
    from financial_pipeline.ocr import detection
    settings = load_settings(ROOT/'config/pipeline.json')
    database = Database.from_env_file(settings.database_env)
    SessionLocal = database.sessions
    assert not list((WS/'runtime/processing').iterdir()), 'Live test requires an idle processing workspace'
    logs = WS/'data/runs'/('live_processing_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
    logs.mkdir(parents=True)
    registry = json.loads((ROOT/'config/report-sources.json').read_text(encoding='utf-8'))
    work = None
    observation = {'scope': 'one-page processing regression, not a full-report OCR run', 'pdf_pages_processed': [7]}
    def stage(name, python, script, *args):
        result = subprocess.run([str(python), str(ROOT/'scripts/pipeline_stage.py'), script, *map(str,args), '--config', str(ROOT/'config/pipeline.json')], cwd=ROOT, capture_output=True,
                                text=True, encoding='utf-8', errors='replace')
        (logs/(name+'.log')).write_text(result.stdout+result.stderr, encoding='utf-8')
        return result
    try:
        result = collect_report(ReportTarget('VNM',2025), registry, WS)
        work = result.work_dir
        observation['collection_observation'] = str(result.observation_path.relative_to(WS))
        detector = ROOT/'.venv-paddle/Scripts/python.exe'
        inference = WS/'runtime/venv/Scripts/python.exe'
        assert stage('detect', detector, 'detect', '--work-dir', work, '--pages', '7').returncode == 0
        assert stage('recognize_first', inference, 'recognize', '--work-dir', work, '--pages', '7').returncode == 0
        first = json.loads((work/'ocr/run.json').read_text(encoding='utf-8'))
        assert first['pages'][0]['recomputed_entries'] > 0
        assert stage('recognize_repeat', inference, 'recognize', '--work-dir', work, '--pages', '7').returncode == 0
        repeated = json.loads((work/'ocr/run.json').read_text(encoding='utf-8'))
        assert repeated['pages'][0]['cached_entries'] == repeated['pages'][0]['entries']
        assert repeated['pages'][0]['recomputed_entries'] == 0
        det = json.loads((work/'detection/run.json').read_text(encoding='utf-8'))
        locked = json.loads((settings.detector_lock).read_text(encoding='utf-8'))
        decision = detection_cache(work, WS, hashlib.sha256(Path(detection.__file__).read_bytes()).hexdigest(),
                                   locked['files_sha256'], det['packages'])
        assert not decision.reusable and decision.reason == 'incomplete_page_coverage'
        assert stage('detect_append', detector, 'detect', '--work-dir', work, '--pages', '8', '--append').returncode == 0
        appended = json.loads((work/'detection/run.json').read_text(encoding='utf-8'))
        assert {page['pdf_page_index'] for page in appended['pages']} == {6, 7}
        with SessionLocal() as db:
            before = db.scalar(select(func.count()).select_from(Candidate))
        rejected = stage('store_partial_rejected', inference, 'store', '--work-dir', work)
        assert rejected.returncode != 0 and 'All-page OCR incomplete' in rejected.stderr
        with SessionLocal() as db:
            after = db.scalar(select(func.count()).select_from(Candidate))
        assert before == after
        observation.update(status='passed', recognized_entries=first['pages'][0]['entries'],
                           first_recomputed=first['pages'][0]['recomputed_entries'], repeated_cached=repeated['pages'][0]['cached_entries'],
                           partial_detection_cache_rejected=decision.reason, partial_database_write_rejected=True,
                           detection_append_coverage_verified=[7, 8],
                           database_row_count_unchanged=before == after)
    except Exception as exc:
        observation.update(status='failed', error=f'{type(exc).__name__}: {exc}')
        raise
    finally:
        database.engine.dispose()
        if work:
            expected = (WS/'runtime/processing').resolve()
            assert work.resolve().is_relative_to(expected) and work.resolve() != expected
            shutil.rmtree(work)
        observation['finished_at'] = datetime.now(timezone.utc).isoformat()
        (logs/'observation.json').write_text(json.dumps(observation,ensure_ascii=False,indent=2),encoding='utf-8')
