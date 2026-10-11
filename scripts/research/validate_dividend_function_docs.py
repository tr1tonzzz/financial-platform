"""Validate the research bundle and SRS structure without building a Word file."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parents[2]
BUNDLE=ROOT/'docs/research-dividend-functions'
SRS=ROOT/'docs/research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md'
text=SRS.read_text(encoding='utf-8')
assert 'Phiên bản 3.3 • Ngày 11/10/2026' in text
requirements=re.findall(r'^\*\*((?:FR|BR|DR|IR|NFR|E|D)\d{2})\b',text,re.M)
assert len(requirements)==91 and len(set(requirements))==91
assert not {'FR29','FR30','D09','D10'} & set(requirements)
declared=set(re.findall(r'^### [\d.]+ (BUC\d{2}) —',text,re.M))
assert declared=={f'BUC{i:02d}' for i in range(1,6)}
assert len(re.findall(r'^\| TC-D\d{2} \|',text,re.M))==10
assert len(re.findall(r'^\| D\d{2} \|',text.split('## 18.')[0],re.M))==10
assert len(re.findall(r'^\| TC\d{2} —',text,re.M))==30
assert '## 17.' in text and '### 17.2. UC01' in text

# Preserve other contracts; CR-AN-03 withdraws FR29/30 and updates FR32.
# CR-WEB-01 changes only the database name in the FR38 backup contract.
old=subprocess.check_output(['git','show','HEAD:docs/research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md'],cwd=ROOT).decode('utf-8')
def contracts(content):
    return {m.group(1):m.group(0).strip() for m in re.finditer(r'^\*\*(FR\d{2})[^\n]+',content,re.M)}
old_fr=contracts(old); current_fr=contracts(text)
exceptions={'FR29','FR30','FR32','FR38'}
assert {k:v for k,v in old_fr.items() if k not in exceptions}=={k:v for k,v in current_fr.items() if k not in exceptions}, 'Unrelated baseline FR contracts changed'
assert set(current_fr)==set(old_fr)-{'FR29','FR30'}
assert 'các phân tích FR25–FR28' in current_fr['FR32']
assert current_fr['FR38']==old_fr['FR38'].replace('SQLite','PostgreSQL')
assert 'CR-WEB-01' in text

paths=[*BUNDLE.glob('*.md'),SRS,ROOT/'docs/research-platform/17-giai-thich-chuc-nang-va-du-lieu.md']
checked_links=0
for path in paths:
    content=path.read_text(encoding='utf-8')
    assert '\ufffd' not in content,path
    assert content.count('```')%2==0,path
    for link in re.findall(r'\]\(([^)]+)\)',content):
        if link.startswith(('http:','https:','#','mailto:')):continue
        assert (path.parent/link.split('#')[0]).exists(),(path,link)
        checked_links+=1
snapshots=0
for path in (BUNDLE/'evidence/github').glob('*/inventory.json'):
    inventory=json.loads(path.read_text(encoding='utf-8'))
    assert len(inventory['commit'])==40 and not inventory['tree_truncated']
    for entry in inventory['files']:
        data=(path.parent/entry['path']).read_bytes()
        assert hashlib.sha256(data).hexdigest()==entry['sha256']
        snapshots+=1
case=json.loads((BUNDLE/'evidence/real-cases.json').read_text(encoding='utf-8'))
assert hashlib.sha256((ROOT/case['dhg']['local_pdf']).read_bytes()).hexdigest()==case['dhg']['sha256']
results=json.loads((BUNDLE/'evidence/probe-results.json').read_text(encoding='utf-8'))
assert results['dhg']['2025']['cash_after_distribution']=='-125629407467'
assert results['dhg']['2024']['cash_after_distribution']=='248283158326'
assert results['dhg_screen_example']['status']=='fail' and results['dhg_screen_example']['contains_unknown']
result={'scope':'documentation, evidence integrity and independent probe; not production acceptance',
        'srs_version':'3.3','business_ucs':5,'requirement_ids':91,'planned_test_cases':51,
        'preserved_baseline_FR':34,'withdrawn_requirements':['FR29','FR30','D09','D10'],
        'withdrawn_tests':['TC22','TC-D09','TC-D10'],'changed_FR':['FR32','FR38'],
        'old_screening_probe_status':'historical evidence; outside current scope',
        'markdown_files_checked':len(paths),'local_links_checked':checked_links,
        'new_github_repos':3,'source_snapshots_checked':snapshots,'dhg_source_hash':'passed','validation':'passed'}
(BUNDLE/'evidence/document-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=True))
