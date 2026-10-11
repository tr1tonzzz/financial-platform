"""Build an inspectable research gap ledger; this is not implementation progress."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'docs/research-investor-support/evidence'
CATALOG = ROOT / 'docs/research-platform/27-yeu-cau-chuc-nang-va-vi-du.md'
NOT_DRAWN = {'F02.2', 'F02.6', 'F02.7', 'F03.3', 'F03.4'}
PARTIAL = {'F01.1', 'F01.3', 'F02.3', 'F02.5', 'F05.2', 'F05.3'}
OUTSIDE_SRS = {'F02.2', 'F02.6', 'F02.7', 'F03.1', 'F03.3', 'F03.4',
               'F04.1', 'F04.2', 'F04.3', 'F04.5', 'F05.5'}
DATA_GAPS = {
    'F01.2': 'Six core fields are not full statements; further reviewed rows required.',
    'F02.2': 'Net revenue and gross profit.',
    'F02.3': 'Current assets/liabilities and separately defined short/long interest-bearing debt.',
    'F02.5': 'Reviewed component rows, cash-flow method, source and period context.',
    'F02.6': 'Revenue, compatible income/equity, beginning and ending balances; 2022 opening basis if analyzing FY2023.',
    'F02.7': 'Quarter/YTD and plan data, outside selected annual pilot.',
    'F03.4': 'Eligible industry sample; three chosen cross-industry firms are not a benchmark.',
    'F05.1': 'Complete dividend event/component ledger by profit year.',
    'F05.3': 'Defined CAPEX/distributions with source and compatible scope.',
    'F05.4': 'Supported stock event chain and verified effective basis dates.',
    'F05.5': 'Common-shareholder payout/earnings or matched DPS/EPS and basis; not consolidated NI by default.',
}

rows = []
for match in re.finditer(r'^\| (F0[1-5]\.\d+) \| ([^|]+) \|', CATALOG.read_text(encoding='utf-8'), re.M):
    uc, title = match.group(1), match.group(2).strip()
    visual = 'not_drawn' if uc in NOT_DRAWN else 'partially_illustrated' if uc in PARTIAL else 'illustrated'
    if uc == 'F05.5':
        visual = 'only_insufficient_data_state_illustrated'
    rows.append({'function_id': uc, 'title': title, 'visual_status': visual,
                 'application_status': 'not_implemented_as_end_to_end_web_function',
                 'srs_relation': 'catalog_candidate_or_extension' if uc in OUTSIDE_SRS else 'existing_foundation_does_not_cover_every_catalog_interaction',
                 'data_gap': DATA_GAPS.get(uc),
                 'evidence': ['docs/research-platform/27-yeu-cau-chuc-nang-va-vi-du.md',
                              'docs/research-platform/36-thiet-ke-man-hinh-5-uc.md',
                              'docs/design-5-uc/manifest.json']})

data = {
    'date': '2026-10-11', 'status': 'proposed_not_integrated',
    'purpose': 'Research review of investor/analyst support; no financial recommendation or proof of improved returns.',
    'baseline': {'pilot_reports': 9, 'core_metrics': 6, 'core_targets': 54,
                 'active_srs_requirements': 91, 'planned_srs_test_cases': 51,
                 'plan_version': 6, 'plan_estimated_hours': 195},
    'functions': rows,
    'packages': [
        {'id': 'A', 'purpose': 'Analyze revenue and profit margins', 'status': 'proposed_not_integrated',
         'new_metrics': ['net_revenue', 'gross_profit'], 'extra_targets_full_pilot': 18,
         'targets_with_core': 72, 'extra_hours_full_pilot': [12, 20]},
        {'id': 'B', 'purpose': 'Analyze liquidity and interest-bearing debt', 'status': 'proposed_not_integrated',
         'new_metrics': ['current_assets', 'current_liabilities', 'short_term_borrowings_and_finance_leases', 'long_term_borrowings_and_finance_leases'],
         'extra_targets_full_pilot': 36, 'targets_with_core_and_A': 108,
         'extra_hours_full_pilot': [18, 28], 'extra_hours_one_firm_three_years': [8, 14]},
        {'id': 'C', 'purpose': 'Analyze compatible average-balance returns and DuPont', 'status': 'proposed_not_integrated',
         'condition': 'Correct income/equity scope. Parent-shareholder ROE requires parent NI and equity. Revenue from A. Not all bank/financial-sector definitions supported.',
         'possible_extra_opening_balance_targets_full_pilot': 6,
         'extra_hours_one_ready_case': [8, 14]},
        {'id': 'U', 'purpose': 'Choose metrics, drill into evidence, compare multi-year trends and save context',
         'status': 'proposed_not_integrated', 'extra_bctc_targets': 0, 'extra_hours': [6, 10]},
    ],
    'combined_A_B_U_extra_hours': [36, 58],
    'boundaries': ['No screening/A04/pass-fail ranking or renamed screening alerts.',
                   'No automatic modification of SRS counts, six-field pilot manifest or 195-hour schedule.',
                   'UC-F06/07, price/yield, quarterly/TTM, ML and sector benchmark remain conditional extensions.',
                   'Mockup numbers and source layouts are synthetic; no deployed application.',
                   'Needs and priorities are design inferences, not independent investor interviews.'],
}
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'gap-review.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
web_sources = [
    ('CFA analysis framework', 'https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/introduction-financial-statement-analysis', 'Official curriculum overview reviewed; not a user study for this project.'),
    ('CFA analytical techniques', 'https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/financial-analysis-techniques', 'Official overview: interpretation, comparisons and ratio categories.'),
    ('CFA free cash flow valuation', 'https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/free-cash-flow-valuation', 'Official overview; not a validated valuation model or market forecast.'),
    ('Vnstock Fundamental', 'https://vnstocks.com/docs/vnstock/phan-tich-co-ban-fundamental', 'Documented interface and code reviewed. No authenticated/live pilot queries executed.'),
    ('HPG financial-report catalog', 'https://www.hoaphat.com.vn/quan-he-co-dong/bao-cao-tai-chinh', 'Catalog lists consolidated/standalone audited FY2025 and explanation documents. This round did not verify individual financial cells.'),
    ('FPT FY2025 annual-report business review', 'https://bctn2025.fpt.com/vi/phan-tich-hoat-dong-kinh-doanh/danh-gia-chung/', 'Official page and business-block navigation reviewed. Segment/plan normalization still proposed.'),
    ('VNM issuer search', 'https://www.vinamilk.com.vn/', 'Search did not establish the full current annual-report set; not claimed as complete coverage.'),
]
(OUT / 'web-sources.json').write_text(json.dumps(
    {'reviewed_on': '2026-10-11', 'method': 'Browser/search review of primary sources. No copied full web articles.',
     'sources': [{'title': t, 'url': u, 'limitations': lim} for t,u,lim in web_sources]},
    ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'reviewed_core_catalog_functions': len(rows), 'mandatory_scope_changed': False}))
