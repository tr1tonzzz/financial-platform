"""Download immutable public source snapshots for static review; never execute them."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'docs/research-dividend-functions/evidence/github'
REPOS = ['oliverbrown/stock_screener', 'carlosbrown2/dividend-screener', 'neurobloomai/market-tools']

def get(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'FAP-research', 'Accept': 'application/vnd.github+json'})
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read()

def collect(repo):
    meta = json.loads(get('https://api.github.com/repos/' + repo))
    commit = json.loads(get('https://api.github.com/repos/' + repo + '/commits/' + meta['default_branch']))
    sha = commit['sha']
    tree = json.loads(get('https://api.github.com/repos/' + repo + '/git/trees/' + sha + '?recursive=1'))
    paths = [item['path'] for item in tree['tree'] if item['type'] == 'blob']
    destination = OUT / repo.replace('/', '__')
    if (destination / 'inventory.json').exists():
        raise FileExistsError(f'Immutable evidence already exists: {destination}. Use a new output directory for a new review.')
    destination.mkdir(parents=True, exist_ok=True)
    selected = [p for p in paths if p.lower() in ('readme.md', 'license', 'license.md') or
                (p.endswith(('.py', '.toml')) and not p.startswith(('.github/', 'tests/')) and
                 ('dividend' in p.lower() or 'screen' in p.lower() or len(paths) < 30))]
    files = []
    for path in selected[:18]:
        url = f'https://raw.githubusercontent.com/{repo}/{sha}/{path}'
        data = get(url)
        target = destination / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        files.append({'path': path, 'url': url, 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)})
    inventory = {'repo': repo, 'commit': sha, 'commit_date': commit['commit']['committer']['date'],
                 'retrieved_on': '2026-10-11', 'license': meta.get('license'),
                 'tree_truncated': tree.get('truncated'), 'paths': paths, 'files': files,
                 'method': 'static review; repository code not executed'}
    (destination / 'inventory.json').write_text(json.dumps(inventory, ensure_ascii=False, indent=2), encoding='utf-8')
    return {'repo': repo, 'sha': sha, 'selected': [f['path'] for f in files], 'paths': paths[:45]}

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for result in pool.map(collect, REPOS):
            print(json.dumps(result, ensure_ascii=True))
