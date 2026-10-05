import fs from 'node:fs/promises';
import path from 'node:path';
import { FileBlob, PresentationFile } from '@oai/artifact-tool';

const root = process.cwd();
const output = path.join(root, 'data-sets/research-evidence/2026-10-03-direction-change/build');
const source = path.join(root, 'docs/research-platform/reports/de-xuat-project.pptx');
const deck = await PresentationFile.importPptx(await FileBlob.load(source));
await fs.writeFile(path.join(output, 'before.ndjson'), (await deck.inspect({kind:'slide,textbox,shape,notes,layout',maxChars:40000})).ndjson);
for (let i = 0; i < deck.slides.items.length; i++) {
  const slide = deck.slides.items[i];
  const png = await slide.export({format:'png',scale:1});
  await fs.writeFile(path.join(output, `before-${i+1}.png`), new Uint8Array(await png.arrayBuffer()));
}
console.log(`Inspected ${deck.slides.items.length} source slides`);
