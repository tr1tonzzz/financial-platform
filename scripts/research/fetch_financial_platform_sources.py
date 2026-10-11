"""Static, immutable source evidence for research into platform analysis tasks."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import sys
import urllib.request

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'docs/research-financial-platform-direction/evidence/github'
REPOS=['dgunning/edgartools','theOGognf/finagg','JerBouma/FinanceDatabase',
       'Fincept-Corporation/FinceptTerminal','OpenBB-finance/backends-for-openbb']

def get(url):
    req=urllib.request.Request(url,headers={'User-Agent':'FAP-static-research','Accept':'application/vnd.github+json'})
    with urllib.request.urlopen(req,timeout=45) as r:return r.read()

def collect(repo):
    directory=OUT/repo.replace('/','__')
    directory.mkdir(parents=True,exist_ok=True)
    target=directory/'inventory.json'
    if target.exists():raise FileExistsError(f'Existing evidence: {directory}')
    meta=json.loads(get('https://api.github.com/repos/'+repo))
    c=json.loads(get('https://api.github.com/repos/'+repo+'/commits/'+meta['default_branch']))
    sha=c['sha']
    tree=json.loads(get('https://api.github.com/repos/'+repo+'/git/trees/'+sha+'?recursive=1'))
    paths=[x['path'] for x in tree['tree'] if x['type']=='blob']
    files=[]
    for path in paths:
        if path.lower() not in ('readme.md','license','license.md','license.txt'):continue
        data=get(f'https://raw.githubusercontent.com/{repo}/{sha}/{path}')
        (directory/path).write_bytes(data)
        files.append({'path':path,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
    inventory={'repo':repo,'sha':sha,'commit_date':c['commit']['committer']['date'],
               'retrieved_on':'2026-10-11','license':meta.get('license'),'tree_truncated':tree.get('truncated'),
               'paths':paths,'files':files,'method':'static review only; no project installation/execution'}
    target.write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    matches=[p for p in paths if any(term in p.lower() for term in ('compar','screener','watchlist','chart','stitch','entityfacts','widget','financials','database','dashboard','analytics'))]
    return {'repo':repo,'sha':sha,'file_count':len(paths),'truncated':tree.get('truncated'),'candidate_paths':matches[:70]}

def extra(repo,paths):
    directory=OUT/repo.replace('/','__')
    target=directory/'inventory.json'
    inventory=json.loads(target.read_text(encoding='utf-8'))
    existing={f['path'] for f in inventory['files']}
    for path in paths:
        if path in existing:continue
        if path not in inventory['paths']:raise ValueError(path)
        data=get(f"https://raw.githubusercontent.com/{repo}/{inventory['sha']}/{path}")
        destination=directory/path
        destination.parent.mkdir(parents=True,exist_ok=True)
        destination.write_bytes(data)
        inventory['files'].append({'path':path,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
    target.write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return {'repo':repo,'downloaded_paths':paths}

if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(collect,REPOS):print(json.dumps(result,ensure_ascii=True))
