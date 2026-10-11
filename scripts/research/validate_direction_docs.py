"""Check active-document consistency, references and the shared plan."""
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'docs/research-platform'
HISTORY=BASE/'history/before-pcd-v3.1-2026-10-05'
files=[ROOT/'docs/README.md',ROOT/'docs/research-design.md',*BASE.glob('*.md'),* (ROOT/'docs/research-profit-cash-dividend').glob('*.md'),*(ROOT/'docs/research-dividend-functions').glob('*.md'),*(ROOT/'docs/research-financial-platform-direction').glob('*.md'),*(ROOT/'docs/research-high-star-finance').glob('*.md'),BASE/'reports/README.md']
broken=[];existing=[]
for path in files:
    content=path.read_text(encoding='utf8')
    assert '\ufffd' not in content,path
    assert content.count('```')%2==0,path
    for target in re.findall(r'\]\(([^)]+)\)',content):
        if target.startswith(('http:','https:','#','mailto:')):continue
        target=target.split('#')[0]
        if not (path.parent/target).exists():
            old=HISTORY/path.relative_to(ROOT/'docs')
            issue={'file':str(path.relative_to(ROOT)),'target':target}
            (existing if old.exists() and target in old.read_text(encoding='utf8') else broken).append(issue)
plan=json.loads((BASE/'checklist-13-tuan.json').read_text(encoding='utf8'))
embedded=re.search(r'<script[^>]*id="plan-data"[^>]*>(.*?)</script>',(BASE/'checklist-13-tuan.html').read_text(encoding='utf8'),re.S)
assert embedded and json.loads(embedded.group(1))==plan,'HTML/JSON drift'
assert plan['version']==3 and plan['srs']=='SRS-FAP-01 v3.1'
assert sum(sum(w['hours'].values()) for w in plan['weeks'])==167
assert sum(w['hours']['extension'] for w in plan['weeks'])==24
assert len({r for w in plan['weeks'] for r in w['requirements']})==83
assert len({t for w in plan['weeks'] for t in w['tests']})==42
current_version=re.search(r'^Phiên bản ([\d.]+) •',(BASE/'22-srs-dac-ta-yeu-cau-phan-mem.md').read_text(encoding='utf8'),re.M).group(1)
current_plan=json.loads((BASE/'checklist-10-tuan-v4.json').read_text(encoding='utf8'))
current_embedded=re.search(r'<script[^>]*id="plan-data"[^>]*>(.*?)</script>',(BASE/'checklist-10-tuan-v4.html').read_text(encoding='utf8'),re.S)
assert current_embedded and json.loads(current_embedded.group(1))==current_plan,'Current HTML/JSON drift'
assert current_plan['version']==6 and current_plan['srs']=='SRS-FAP-01 v3.3'
assert len(current_plan['weeks'])==10 and sum(w['hours'] for w in current_plan['weeks'])==195
assert sum(len(w['tasks']) for w in current_plan['weeks'])==60
assert len({r for w in current_plan['weeks'] for r in w['requirements']})==91
assert len({t for w in current_plan['weeks'] for t in w['tests']})==51
result={'scope':'documentation only; no application acceptance tests','files_checked':len(files),'new_broken_links':broken,'preexisting_broken_links':existing,'plan_version':3,'current_srs_version':current_version,'plan_baseline_srs_version':'3.1','plan_baseline_hours':167,'plan_baseline_requirement_ids':83,'plan_baseline_tests':42,'dividend_extension_schedule':'not yet merged; separately estimated in CR-DIV-02'}
result.update({'plan_version':6,'current_plan_weeks':10,'current_plan_hours_estimated':195,'current_plan_tasks':60,'current_plan_requirements_mapped':91,'current_plan_tests_mapped':51,'legacy_plan_version':3,'dividend_extension_schedule':'Selected slices mapped in v6; hours still estimates, not application acceptance'})
qa=ROOT/f'_plan_render/srs-v{current_version}';qa.mkdir(parents=True,exist_ok=True)
(qa/'direction-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(result,ensure_ascii=False))
assert not broken,'New broken references'
