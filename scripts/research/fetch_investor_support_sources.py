"""Read public code at the commits already captured; never execute source projects."""
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
PREVIOUS = ROOT / 'docs/research-high-star-finance/evidence/github'
OUT = ROOT / 'docs/research-investor-support/evidence'
FILES = {
    'OpenBB-finance/OpenBB': [
        'openbb_platform/extensions/equity/openbb_equity/fundamental/fundamental_router.py',
        'openbb_platform/core/openbb_core/provider/standard_models/financial_ratios.py',
        'openbb_platform/core/openbb_core/provider/standard_models/income_statement.py',
        'openbb_platform/core/openbb_core/provider/standard_models/trailing_dividend_yield.py',
    ],
    'Fincept-Corporation/FinceptTerminal': [
        'fincept-qt/src/screens/equity_research/EquityFinancialsTab_Views.cpp',
        'fincept-qt/src/screens/equity_research/EquityPeersTab.cpp',
        'fincept-qt/src/screens/equity_research/EquityFinancialsTab_Populate.cpp',
    ],
    'JerBouma/FinanceToolkit': [
        'financetoolkit/ratios/profitability_model.py',
        'financetoolkit/ratios/liquidity_model.py',
        'financetoolkit/ratios/solvency_model.py',
        'financetoolkit/ratios/efficiency_model.py',
        'financetoolkit/models/dupont_model.py',
    ],
    'stocknear/frontend': [
        'src/lib/components/Financial/FinancialMetricPicker.svelte',
        'src/lib/components/Financial/FinancialMultiSeriesCard.svelte',
        'src/lib/components/Financial/FinancialTable.svelte',
        'src/lib/components/Financial/FinancialChartModal.svelte',
        'src/lib/components/SectorSegmentation.svelte',
        'src/routes/stocks/[tickerID]/statistics/revenue/+page.svelte',
        'src/lib/financials/statementHelpers.ts',
        'src/lib/components/MarkdownNoteEditor.svelte',
    ],
    'thinh-vu/vnstock': [
        'vnstock/ui/domains/fundamental/equity.py',
        'vnstock/explorer/vci/financial.py',
        'vnstock/api/financial.py',
    ],
    'dgunning/edgartools': [
        'edgar/xbrl/stitching/core.py',
        'edgar/entity/query.py',
    ],
    'afadil/wealthfolio': [
        'apps/frontend/src/pages/income/income-page.tsx',
        'crates/core/src/portfolio/income/income_service.rs',
    ],
    'ghostfolio/ghostfolio': [
        'apps/api/src/app/portfolio/portfolio.service.ts',
    ],
    'portfolio-performance/portfolio': [
        'name.abuchen.portfolio.ui/src/name/abuchen/portfolio/ui/views/payments/PaymentsPerMonthMatrixTab.java',
    ],
    'ranaroussi/quantstats': ['quantstats/reports.py'],
    'ranaroussi/yfinance': ['yfinance/scrapers/fundamentals.py'],
    'akfamily/akshare': ['akshare/stock_feature/stock_disclosure_cninfo.py'],
}


def fetch_one(item):
    requested, path = item
    folder = PREVIOUS / requested.replace('/', '__')
    inv = json.loads((folder / 'inventory.json').read_text(encoding='utf-8'))
    url = f"https://raw.githubusercontent.com/{inv['repo']}/{inv['sha']}/{path}"
    dest = OUT / 'github' / requested.replace('/', '__') / path
    try:
        if dest.exists():
            raw, acquisition = dest.read_bytes(), 'local_new_research_cache'
        else:
            request = urllib.request.Request(url, headers={'User-Agent': 'FAP-public-code-research'})
            with urllib.request.urlopen(request, timeout=35) as response:
                raw = response.read()
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(raw)
            acquisition = 'fetched_public_raw_at_fixed_commit'
        return {'requested_repo': requested, 'repo': inv['repo'], 'commit': inv['sha'],
                'stars_snapshot': inv['stars'], 'stars_retrieved_on': inv['retrieved_on'],
                'path': path, 'raw_url': url, 'url': f"https://github.com/{inv['repo']}/blob/{inv['sha']}/{path}",
                'local_path': str(dest.relative_to(ROOT)).replace('\\', '/'),
                'sha256': sha256(raw).hexdigest(), 'bytes': len(raw),
                'lines': len(raw.decode('utf-8').splitlines()), 'acquisition': acquisition}
    except Exception as exc:
        return {'requested_repo': requested, 'path': path, 'raw_url': url, 'error': str(exc)}


if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    items = [(repo, path) for repo, paths in FILES.items() for path in paths]
    with ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(fetch_one, items))
    result = {'researched_on': '2026-10-11',
              'method': 'Further static source review of 12 selected repositories from the earlier 36-repository survey. No project was installed or run. Stars are inherited same-day snapshots, not newly queried.',
              'files': rows}
    (OUT / 'source-capture.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'repositories': len(FILES), 'saved_files': sum('error' not in r for r in rows),
                      'failures': [r for r in rows if 'error' in r]}, ensure_ascii=False))
