"""Validate saved sources and active UC documentation; no production acceptance."""
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
BUNDLE=ROOT/'docs/research-high-star-finance'
BASE=BUNDLE/'evidence/github'
inventories=[json.loads(p.read_text(encoding='utf-8')) for p in BASE.glob('*/inventory.json')]
assert len(inventories)==len({i['repo'] for i in inventories})==36
assert sum(i['stars']>=3000 for i in inventories)==25
assert sum(i['stars']>=10000 for i in inventories)==12
assert sum(any(not f['path'].lower().startswith('readme') for f in i['files']) for i in inventories)==17
files=0
lookup={}
for inv in inventories:
    folder=BASE/inv['requested_repo'].replace('/','__')
    lookup[inv['repo']]=(inv,folder)
    assert len(inv['sha'])==40 and inv['retrieved_on']=='2026-10-11'
    for entry in inv['files']:
        raw=(folder/entry['path']).read_bytes()
        assert len(raw)==entry['bytes']
        assert hashlib.sha256(raw).hexdigest()==entry['sha256'],(inv['repo'],entry['path'])
        files+=1
assert files==87
ledger=json.loads((BUNDLE/'evidence/code-reference-ledger.json').read_text(encoding='utf-8'))
assert len(ledger)==34 and len({e['repo'] for e in ledger})==17
for entry in ledger:
    inv,folder=lookup[entry['repo']]
    assert entry['sha']==inv['sha']
    assert entry['path'] in {f['path'] for f in inv['files']}
    lines=(folder/entry['path']).read_text(encoding='utf-8').splitlines()
    assert entry['locator'] in lines[entry['line']-1]
    assert entry['url'].endswith(f"#L{entry['line']}")
survey=json.loads((BUNDLE/'evidence/repository-survey.json').read_text(encoding='utf-8'))
assert {i['repo']:i for i in survey}=={i['repo']:i for i in inventories}
catalogue=ROOT/'docs/research-platform/27-yeu-cau-chuc-nang-va-vi-du.md'
text=catalogue.read_text(encoding='utf-8')
assert 'Phiên bản **2.0**' in text and 'bỏ **Tìm và khám phá trường hợp cần chú ý (A04)**' in text
ucs=re.findall(r'^## \d+\. (UC-F\d{2}) —',text,re.M)
assert ucs==[f'UC-F{i:02d}' for i in range(1,8)]
children=re.findall(r'^\| (F\d{2}\.\d+) \|',text,re.M)
assert len(children)==len(set(children))==38
assert {i:sum(c.startswith(f'F{i:02d}.') for c in children) for i in range(1,8)}=={1:6,2:8,3:4,4:5,5:6,6:5,7:4}
srs=(ROOT/'docs/research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md').read_text(encoding='utf-8')
ids=re.findall(r'^\*\*((?:FR|BR|DR|IR|NFR|E|D)\d{2})\b',srs,re.M)
assert len(ids)==len(set(ids))==91
assert not {'FR29','FR30','D09','D10'}&set(ids)
assert '## 18. CR-AN-03' in srs
bridge_trace=srs.split('### 15.4.')[1].split('## 16.')[0]
bridge_tests=set(re.findall(r'\bP\d{2}\b',bridge_trace))
assert bridge_tests=={f'P{i:02d}' for i in range(1,12)}
tests=[*re.findall(r'^\| (TC\d{2}) —',srs,re.M),*sorted(bridge_tests),*re.findall(r'^\| (TC-D\d{2}) \|',srs,re.M)]
assert len(tests)==len(set(tests))==51
assert not {'TC22','TC-D09','TC-D10'}&set(tests)
paths=[*BUNDLE.glob('*.md'),catalogue,ROOT/'docs/research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md']
links=0
for path in paths:
    body=path.read_text(encoding='utf-8')
    assert '\ufffd' not in body and body.count('```')%2==0,path
    for target in re.findall(r'\]\(([^)]+)\)',body):
        if target.startswith(('http:','https:','#','mailto:')):continue
        assert (path.parent/target.split('#')[0]).exists(),(path,target)
        links+=1
result={'scope':'static research evidence/document consistency; no project execution or application acceptance',
        'retrieval_date':'2026-10-11','repositories':36,'repos_ge_3000_stars':25,'repos_ge_10000_stars':12,
        'readme_repos':35,'selected_code_repos':17,'source_files_hash_checked':files,'code_references_checked':len(ledger),
        'catalogue_version':'2.0','macro_uc_groups':7,'child_functions':38,'srs_version':'3.3',
        'active_requirement_ids':91,'planned_test_cases':51,'local_links_checked':links,'validation':'passed'}
(BUNDLE/'evidence/research-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=True))
