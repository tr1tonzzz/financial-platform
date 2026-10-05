import fs from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
import { FileBlob, PresentationFile } from '@oai/artifact-tool';
import {finalizePresentation} from 'file:///C:/Users/admin/.codex/plugins/cache/openai-primary-runtime/presentations/26.909.12148/skills/presentations/container_tools/artifact_tool_utils.mjs';

const root=process.cwd();
const build=path.join(root,'data-sets/research-evidence/2026-10-03-direction-change/build');
const out=path.join(root,'data-sets/research-evidence/2026-10-03-direction-change/output');
await fs.mkdir(out,{recursive:true});
const source=path.join(root,'docs/research-platform/reports/de-xuat-project.pptx');
const runId=Date.now();
const reference=path.join(build,'source-reference-'+runId+'.pptx');
await fs.copyFile(source,reference);
const sha=createHash('sha256').update(await fs.readFile(reference)).digest('hex');
const content=JSON.parse(await fs.readFile(path.join(root,'docs/research-platform/reports/noi-dung-de-xuat.json'),'utf8'));
const deck=await PresentationFile.importPptx(await FileBlob.load(source));
const records=(await deck.inspect({kind:'slide,textbox,shape,notes',maxChars:50000})).ndjson.trim().split('\n').map(JSON.parse);
for(let i=0;i<content.slides.length;i++){
  const boxes=records.filter(r=>r.kind==='textbox'&&r.slide===i+1);
  const texts=content.slides[i].texts;
  if(boxes.length!==texts.length)throw new Error('Text shape count differs on slide '+(i+1));
  for(let j=0;j<boxes.length;j++){
    const shape=deck.resolve(boxes[j].id);
    if(boxes[j].text.includes('\n'))shape.text=texts[j];
    else shape.text.replace(boxes[j].text,texts[j]);
  }
  deck.slides.items[i].speakerNotes.textFrame.setText(content.slides[i].notes);
}
const candidate=path.join(build,'candidate.pptx');
await(await PresentationFile.exportPptx(deck)).save(candidate);
const base='C:/Users/admin/.codex/plugins/cache/openai-primary-runtime/presentations/26.909.12148/skills/presentations/container_tools';
const final=path.join(out,'de-xuat-project-'+runId+'.pptx');
await finalizePresentation({
  workspaceDir:root,candidatePath:candidate,finalPath:final,
  pythonExecutable:'C:/Users/admin/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe',
  integrityValidatorPath:path.join(base,'inspect_presentation_package_integrity.py'),
  layoutValidatorPath:path.join(base,'inspect_presentation_layout_geometry.py'),
  layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit'],
  explicitTotalSlideCount:6,
  fontPolicy:{basis:'reference',families:['Arial'],referencePath:reference,referenceSha256:sha},
  verifyArtifactToolImport:true,receiptPath:path.join(build,'finalization-receipt-'+runId+'.json')
});
const checked=await PresentationFile.importPptx(await FileBlob.load(final));
const actual=(await checked.inspect({kind:'textbox',maxChars:50000})).ndjson.trim().split('\n').map(JSON.parse);
for(let i=0;i<content.slides.length;i++){
 const texts=actual.filter(r=>r.kind==='textbox'&&r.slide===i+1).map(r=>r.text);
 if(JSON.stringify(texts)!==JSON.stringify(content.slides[i].texts))throw new Error('Exported content differs on slide '+(i+1));
}
await fs.writeFile(path.join(build,'after.ndjson'),(await checked.inspect({kind:'slide,textbox,notes',maxChars:50000})).ndjson);
for(let i=0;i<checked.slides.items.length;i++){
  const png=await checked.slides.items[i].export({format:'png',scale:1});
  await fs.writeFile(path.join(build,'after-'+(i+1)+'.png'),new Uint8Array(await png.arrayBuffer()));
}
await fs.copyFile(final,source);
console.log('Updated and validated six editable slides, rendered all six');
