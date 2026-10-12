"""Generate verification evidence from tests, current outputs and PostgreSQL."""
import argparse
import csv
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'src'))
from financial_pipeline.settings import load_settings


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', '--profile', dest='profile', type=Path, default=ROOT/'config/pipeline.json')
    parser.add_argument('--tests-only', action='store_true')
    parser.add_argument('--baseline-observation', type=Path)
    args = parser.parse_args()
    settings = load_settings(args.profile)
    out = settings.workspace/'data/verification/pipeline'
    out.mkdir(parents=True, exist_ok=True)
    result = subprocess.run([sys.executable, '-m', 'pytest', '-q', '--junitxml', str(out/'tests.xml')],
                            cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace')
    (out/'tests.log').write_text(result.stdout+result.stderr, encoding='utf-8')
    suite = ET.parse(out/'tests.xml').getroot().find('testsuite')
    counts = {key: int(suite.attrib[key]) for key in ['tests', 'failures', 'errors', 'skipped']}
    counts.update(passed=counts['tests']-counts['failures']-counts['errors']-counts['skipped'], exit_code=result.returncode)
    save(out/'test-summary.json', counts)
    if result.returncode:
        raise RuntimeError(f'Tests failed; see {out}')
    if args.tests_only:
        print(json.dumps(counts))
        return
    from sqlalchemy import select
    from financial_pipeline.storage.database import Database
    from financial_pipeline.storage.models import Candidate, ExtractionRun, DocumentVersion, Document
    from financial_pipeline.ocr import detection, recognition
    from financial_pipeline.extraction import parser as financial_parser
    from financial_pipeline.extraction import normalization
    expected_codes = {'detector_code_sha256': hashlib.sha256(Path(detection.__file__).read_bytes()).hexdigest(),
                      'recognizer_code_sha256': hashlib.sha256(Path(recognition.__file__).read_bytes()).hexdigest(),
                      'parser_sha256': hashlib.sha256(Path(financial_parser.__file__).read_bytes()).hexdigest(),
                      'normalization_sha256': hashlib.sha256(Path(normalization.__file__).read_bytes()).hexdigest(),
                      'recognition_config_sha256': hashlib.sha256(settings.vietocr_config.read_bytes()).hexdigest(),
                      'recognizer_model_sha256': hashlib.sha256(settings.vietocr_weights.read_bytes()).hexdigest()}
    baseline = {} if args.baseline_observation is None else {
        row['ticker']: row['database_run_id'] for row in json.loads(args.baseline_observation.read_text(encoding='utf-8'))['reports']}
    reports = []
    with Database.from_env_file(settings.database_env) as database, database.sessions() as db:
        for folder in sorted((settings.workspace/'data/processed').iterdir()):
            source = json.loads((folder/'source.json').read_text(encoding='utf-8'))
            processing = json.loads((folder/'processing.json').read_text(encoding='utf-8'))
            candidates = json.loads((folder/'candidates.json').read_text(encoding='utf-8'))
            with (folder/'database-readback.csv').open(encoding='utf-8-sig', newline='') as stream:
                readback = list(csv.DictReader(stream))
            ids = {int(row['extraction_run_id']) for row in readback}
            assert len(ids) == 1 and len(readback) == len(candidates) == 6
            run_id = ids.pop()
            run = db.get(ExtractionRun, run_id)
            version = db.get(DocumentVersion, run.document_version_id)
            document = db.get(Document, version.document_id)
            assert (document.ticker, document.fiscal_year, version.sha256) == (source['ticker'], source['fiscal_year'], source['sha256'])
            stored = {row.metric_code: row for row in db.scalars(select(Candidate).where(Candidate.extraction_run_id == run_id))}
            for row in candidates:
                actual = stored[row['metric_code']]
                assert actual.evidence == row and format(actual.value, 'f') == row['value_vnd']
                assert actual.status == row['status'] == 'pending_review'
                csv_row = next(r for r in readback if r['metric_code'] == row['metric_code'])
                assert csv_row['value_vnd'] == row['value_vnd'] and csv_row['status'] == actual.status
            assert processing['all_pages_processed'] and processing['context']['verified']
            assert hashlib.sha256((settings.workspace/source['path']).read_bytes()).hexdigest() == source['sha256']
            assert run.provenance['processing']['pdf_pages'] == processing['pdf_pages'] == source['pdf_pages']
            mismatches = {key: {'recorded': processing.get(key), 'current': value}
                          for key, value in expected_codes.items() if processing.get(key) != value}
            volatile = {'checked_at', 'recognition_cache_entries', 'recognition_recomputed_entries'}
            assert {k: v for k, v in run.provenance['processing'].items() if k not in volatile} == {
                k: v for k, v in processing.items() if k not in volatile}
            values = {key: value.value for key, value in stored.items()}
            assert values['total_assets'] == values['total_liabilities']+values['total_equity']
            previous = baseline.get(source['ticker'])
            unchanged = None
            if previous:
                previous_values = {row.metric_code: row.value for row in db.scalars(select(Candidate).where(Candidate.extraction_run_id == previous))}
                unchanged = values == previous_values
            reports.append({'ticker': source['ticker'], 'database_run_id': run_id, 'rows_verified': len(stored),
                            'pdf_pages': processing['pdf_pages'], 'current_service_hashes_verified': not mismatches,
                            'processing_version_mismatches': mismatches,
                            'balance_equation_exact': True, 'previous_run_id': previous,
                            'values_unchanged_from_previous_run': unchanged})
    current = all(report['current_service_hashes_verified'] for report in reports)
    observation = {'status': 'passed' if current else 'historical_data_verified', 'tests': counts, 'reports': reports,
                   'processing_directory_empty': not list((settings.workspace/'runtime/processing').iterdir()),
                   'finished_at': datetime.now(timezone.utc).isoformat()}
    save(out/'observation.json', observation)
    print(json.dumps(observation, ensure_ascii=False))


if __name__ == '__main__':
    main()
