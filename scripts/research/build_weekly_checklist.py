"""Build an offline weekly checklist from the shared, reviewed 13-week plan."""
import json
from build_execution_plan import build
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'docs/research-platform'
plan=json.loads((BASE/'checklist-13-tuan.json').read_text(encoding='utf-8'))
validation=build(plan,BASE)
template=(ROOT/'scripts/research/templates/checklist-13-tuan.html').read_text(encoding='utf-8')
assert len(plan['weeks'])==13
assert [c['weeks'][-1] for c in plan['cycles']]==[2,4,6,8,10,12,13]
encoded=json.dumps(plan,ensure_ascii=False).replace('</','<\\/')
(BASE/'checklist-13-tuan.html').write_text(template.replace('__PLAN__',encoded),encoding='utf-8')
print(json.dumps(validation))
