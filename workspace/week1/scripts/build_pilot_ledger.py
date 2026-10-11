"""Reconcile the 9-report/54-target manifest with recorded local execution evidence."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'workspace/week1/data'


def csv_rows(path):
    if not path.exists():
        return []
    with path.open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def write(path, rows):
    with path.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    manifest = json.loads((Path(__file__).resolve().parents[1] / 'config/pilot-scope.json').read_text(encoding='utf-8'))
    reports, targets = [], []
    hpg = json.loads((OUT / 'source-manifest.json').read_text(encoding='utf-8')) if (OUT / 'source-manifest.json').exists() else None
    vnm_path = OUT / 'vnm-2025/source.json'
    vnm = json.loads(vnm_path.read_text(encoding='utf-8')) if vnm_path.exists() else None
    references = csv_rows(OUT / 'reference-facts.csv') + csv_rows(OUT / 'vnm-2025/reference-facts.csv')
    for issuer in manifest['issuers']:
        for year in manifest['fiscal_years']:
            ticker = issuer['ticker']
            ref_map = {r['metric_code']:r for r in references if r['ticker'] == ticker and int(r['fiscal_year']) == year}
            source = hpg if (ticker,year) == ('HPG',2025) else vnm if (ticker,year) == ('VNM',2025) else None
            verified = bool(source) and (source.get('context_status') == 'verified_from_paddle_text' or ticker == 'HPG')
            reports.append({'ticker':ticker,'fiscal_year':year,'scope':'consolidated','report_status':'context_verified' if verified else 'collected_pending_context_verification' if source else 'not_registered', 'source_url':(source or {}).get('source_url',(source or {}).get('url','')), 'pdf_sha256':(source or {}).get('pdf_sha256',(source or {}).get('sha256','')), 'reference_count':len(ref_map),'reviewed_fact_count':0,'selected_first_report': ticker == 'VNM' and year == 2025, 'reason':'See logged local source evidence' if source else 'Manifest target; no verified execution evidence registered here'})
            for metric in manifest['core_metrics']:
                ref = ref_map.get(metric)
                targets.append({'ticker':ticker,'fiscal_year':year,'scope':'consolidated','metric_code':metric,'status':ref['review_status'] if ref else 'not_extracted', 'reference_value_vnd': ref.get('normalized_value_vnd','') if ref else '', 'reviewed_value_vnd':'', 'reference_id':ref.get('reference_id','') if ref else '', 'reason':ref.get('reason','') if ref else 'No candidate/reference registered; not a zero'})
    if len(reports) != manifest['expected_report_count'] or len(targets) != manifest['expected_core_fact_count']:
        raise ValueError('Manifest count mismatch')
    write(OUT / 'ledger-reports.csv', reports)
    write(OUT / 'ledger-targets.csv', targets)
    print(f'Registered {len(reports)} reports / {len(targets)} targets; no facts published')


if __name__ == '__main__':
    main()
