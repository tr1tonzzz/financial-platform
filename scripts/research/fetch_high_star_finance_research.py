"""Capture public repository metadata and immutable README evidence; never execute projects."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import subprocess
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'docs/research-high-star-finance/evidence/github'
REPOS = [
    'OpenBB-finance/OpenBB', 'ghostfolio/ghostfolio', 'afadil/wealthfolio',
    'portfolio-performance/portfolio', 'stocknear/frontend',
    'Fincept-Corporation/FinceptTerminal', 'Open-Dev-Society/OpenStock',
    'ranaroussi/yfinance', 'akfamily/akshare', 'waditu/tushare',
    'financedata-org/FinanceDataReader', 'pydata/pandas-datareader',
    'JerBouma/FinanceToolkit', 'JerBouma/FinanceDatabase', 'dgunning/edgartools',
    'theOGognf/finagg', 'thinh-vu/vnstock', 'ranaroussi/quantstats',
    'robertmartin8/PyPortfolioOpt', 'dcajasn/Riskfolio-Lib', 'pmorissette/bt',
    'polakowo/vectorbt', 'microsoft/qlib', 'QuantConnect/Lean',
    'freqtrade/freqtrade', 'kernc/backtesting.py', 'ricequant/rqalpha',
    'stefan-jansen/zipline-reloaded', 'vnpy/vnpy', 'bukosabino/ta',
    'wilsonfreitas/awesome-quant', 'stefan-jansen/machine-learning-for-trading',
    'GavrielP1/SALARY-2045', 'sonnymay/dividend-tracker',
    'EmanueleSturzo/portfolio-analytics', 'OpenBB-finance/backends-for-openbb',
]


def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'FAP-read-only-research',
                                               'Accept': 'application/vnd.github+json'})
    with urllib.request.urlopen(req, timeout=40) as response:
        return response.read()


def collect(requested):
    destination = OUT / requested.replace('/', '__')
    destination.mkdir(parents=True, exist_ok=True)
    saved = destination / 'inventory.json'
    if saved.exists():
        return json.loads(saved.read_text(encoding='utf-8'))
    try:
        meta = json.loads(get('https://api.github.com/repos/' + requested))
        repo = meta['full_name']
        # Public Git ref lookup avoids spending another API request per repo.
        ref = subprocess.check_output(['git', 'ls-remote', 'https://github.com/' + repo + '.git',
                                       'refs/heads/' + meta['default_branch']],
                                      timeout=50, text=True).strip()
        sha = ref.split()[0]
        if len(sha) != 40:
            raise ValueError('No resolved default branch SHA')
        files = []
        for filename in ['README.md', 'readme.md', 'README.rst', 'README', 'Readme.md']:
            try:
                raw = get(f'https://raw.githubusercontent.com/{repo}/{sha}/{filename}')
            except urllib.error.HTTPError as exc:
                if exc.code == 404:
                    continue
                raise
            (destination / filename).write_bytes(raw)
            files.append({'path': filename, 'bytes': len(raw),
                          'sha256': hashlib.sha256(raw).hexdigest()})
            break
        data = {'requested_repo': requested, 'repo': repo, 'sha': sha,
                'stars': meta['stargazers_count'], 'forks': meta['forks_count'],
                'archived': meta['archived'], 'default_branch': meta['default_branch'],
                'description': meta['description'], 'pushed_at': meta['pushed_at'],
                'retrieved_on': '2026-10-11', 'license_metadata': meta.get('license'),
                'files': files, 'review_level': 'metadata and README',
                'method': 'static evidence capture; no installation or execution'}
        saved.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        return data
    except Exception as exc:
        data = {'requested_repo': requested, 'error': str(exc), 'retrieved_on': '2026-10-11'}
        (destination / 'fetch-error.json').write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
        return data


def capture_tree(requested):
    folder = OUT / requested.replace('/', '__')
    path = folder / 'inventory.json'
    inv = json.loads(path.read_text(encoding='utf-8'))
    if 'tree_paths' not in inv:
        tree = json.loads(get(f"https://api.github.com/repos/{inv['repo']}/git/trees/{inv['sha']}?recursive=1"))
        inv['tree_truncated'] = tree.get('truncated', False)
        inv['tree_paths'] = [entry['path'] for entry in tree['tree'] if entry['type'] == 'blob']
        path.write_text(json.dumps(inv, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return inv['tree_paths']


def capture_files(requested, paths):
    folder = OUT / requested.replace('/', '__')
    path = folder / 'inventory.json'
    inv = json.loads(path.read_text(encoding='utf-8'))
    existing = {f['path'] for f in inv['files']}
    for filename in paths:
        if filename in existing:
            continue
        if 'tree_paths' in inv and filename not in inv['tree_paths']:
            raise ValueError(filename)
        raw = get(f"https://raw.githubusercontent.com/{inv['repo']}/{inv['sha']}/{filename}")
        target = folder / filename
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
        inv['files'].append({'path': filename, 'bytes': len(raw),
                             'sha256': hashlib.sha256(raw).hexdigest()})
    inv['review_level'] = 'README and selected implementation files'
    path.write_text(json.dumps(inv, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return {'repo': inv['repo'], 'paths': paths}


if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(collect, REPOS))
    (OUT.parent / 'repository-survey.json').write_text(
        json.dumps(results, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for r in sorted(results, key=lambda r: r.get('stars', -1), reverse=True):
        print(json.dumps({k: r.get(k) for k in ['repo', 'stars', 'sha', 'archived', 'error']}, ensure_ascii=True))
