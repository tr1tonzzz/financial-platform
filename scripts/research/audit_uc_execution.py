"""Inventory local UC evidence; does not run OCR, crawl, or application tests."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'docs/research-platform/evidence/uc-priority-audit-2026-10-11.json'


def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8-sig'))


def fingerprint(path, expected=None):
    relative = Path(path)
    target = ROOT / relative
    digest = hashlib.sha256(target.read_bytes()).hexdigest() if target.is_file() else None
    return {'path': relative.as_posix(), 'exists': target.is_file(),
            'sha256': digest, 'expected_sha256': expected,
            'hash_matches': digest == expected if expected else None}


def main():
    crawl = read('docs/research-crawl-methods/crawl-evidence.json')
    pdfs = [fingerprint(Path(crawl['raw_directory_relative_to_repo']) / row['saved_path'], row['sha256'])
            for row in crawl['reports']]
    vnm_root = 'data-sets/research-evidence/2026-10-06-report-01-vnm-q1-2026'
    vnm = read(vnm_root + '/source-probe.json')
    dhg = read('docs/research-profit-cash-dividend/evidence/case-dhg-2025.json')
    raw = [*pdfs, fingerprint(Path(vnm_root) / vnm['pdf_path'], vnm['pdf_sha256']),
           fingerprint(dhg['source_local_path'], dhg['expected_sha256'])]
    residuals = {year: sum(row[year] for row in dhg['bridge_leaves']) - value
                 for year, value in dhg['reported_cfo'].items()}
    sources = ['scripts/research/crawl_official_reports.py',
               'scripts/research/probe_vnm_q1.py', 'scripts/research/check_vnm_q1.py',
               'scripts/research/dividend_functions_probe.py',
               'scripts/research/extract_recent_dividend_examples.py',
               'scripts/research/test_crawl_official_reports.py',
               'scripts/research/test_dividend_functions_probe.py']
    report = {
        'record_created_at_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Local inventory/hash checks and recalculation of manually recorded DHG bridge. Not application acceptance, not new OCR or source retrieval.',
        'priority': ['UC-F01', 'UC-F02', 'UC-F03', 'UC-F05', 'UC-F04'],
        'src_files': [p.relative_to(ROOT).as_posix() for p in sorted((ROOT / 'src').rglob('*')) if p.is_file()],
        'raw_evidence': raw, 'source_code': [fingerprint(p) for p in sources],
        'crawl_pdf_count_in_this_manifest': len(pdfs),
        'deduplication_note': 'Additional VNM and DHG case sources may overlap other research manifests; do not interpret this list as total unique project corpus.',
        'vnm_oct06_comparison': read(vnm_root + '/comparison.json'),
        'dhg_manual_bridge_residual_vnd': residuals,
        'review_limitations': ['Manual facts reviewed by research author; no independently verified gold.',
                              'VNM six checked cells represent three lines and two periods, not six distinct core metrics.',
                              'No UI or full application acceptance inferred from source/test presence.'],
    }
    assert all(row['exists'] and row['hash_matches'] for row in raw), 'Missing or changed raw PDF evidence'
    assert all(row['exists'] for row in report['source_code']), 'Missing prototype source'
    assert all(value == 0 for value in residuals.values()), 'DHG bridge residual differs'
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'raw_pdf_records_verified': len(raw), 'src_file_count': len(report['src_files']),
                      'dhg_bridge_residuals': residuals, 'output': OUT.relative_to(ROOT).as_posix()}))


if __name__ == '__main__':
    main()
