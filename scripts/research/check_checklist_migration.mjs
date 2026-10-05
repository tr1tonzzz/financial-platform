import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const html=fs.readFileSync('docs/research-platform/checklist-13-tuan.html','utf8');
const plan=JSON.parse(html.match(/<script[^>]*id="plan-data"[^>]*>(.*?)<\/script>/s)[1]);
const script=html.match(/<script>\s*([\s\S]*?)<\/script>/)[1];
new vm.Script(script);
const validation=script.slice(script.indexOf('function validate(data)'),script.indexOf('function warn(text)'));
const context={PLAN:plan,VERSION:plan.version,KEY:plan.id,validTasks:new Set(plan.weeks.flatMap(w=>w.tasks.map((_,i)=>'w'+w.n+'-t'+i))),warn:()=>{}};
context.fresh=()=>({version:3,project:plan.id,start:'',checked:{},notes:{}});
vm.createContext(context);vm.runInContext(validation+';this.check=validate;',context);
for(const prior of plan.legacyIds){
  const input={version:prior.version,project:prior.id,start:'2026-10-05',checked:{'w1-t0':true},notes:{1:'Nguồn và giờ thực'}};
  const output=context.check(input);
  assert.equal(output.start,input.start);assert.equal(output.notes[1],input.notes[1]);assert.equal(Object.keys(output.checked).length,0);
  assert.equal(input.checked['w1-t0'],true);
}
const output=context.check({version:3,project:plan.id,start:'2026-10-05',checked:{'w1-t0':true,unknown:true},notes:{1:'mới'}});
assert.equal(output.checked['w1-t0'],true);assert.equal(Object.keys(output.checked).length,1);
assert.throws(()=>context.check({version:9,project:plan.id,checked:{},notes:{}}));
console.log('Checklist syntax and v1/v2 migration passed; dates/notes retained, old ticks not applied, current ticks retained.');
