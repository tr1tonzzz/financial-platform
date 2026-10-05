// Research OCR on a small, explicitly selected set of rendered PDF pages.
// Usage: node probe_ocr.cjs <tesseract.js module directory> <page-jobs.json> <output-dir>
const fs = require('node:fs');
const path = require('node:path');
const { performance } = require('node:perf_hooks');

(async () => {
  const moduleDirectory = path.resolve(process.argv[2]);
  const { createWorker } = require(moduleDirectory);
  const jobs = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
  const outputDirectory = path.resolve(process.argv[4]);
  fs.mkdirSync(outputDirectory, { recursive: true });
  const cachePath = path.join(outputDirectory, 'ocr-cache');
  fs.mkdirSync(cachePath, { recursive: true });
  const initStart = performance.now();
  const worker = await createWorker(['vie', 'eng'], 1, { cachePath });
  const run = {
    tesseract_js_version: require(path.join(moduleDirectory, 'package.json')).version,
    languages: ['vie', 'eng'],
    initialization_seconds: (performance.now() - initStart) / 1000,
    results: [],
    warning: 'OCR confidence is not measured accuracy; compare numbers with the original page.',
  };
  try {
    for (const job of jobs) {
      const started = performance.now();
      const { data } = await worker.recognize(job.image, {}, { text: true, blocks: true });
      fs.writeFileSync(path.join(outputDirectory, job.id + '-ocr.txt'), data.text, 'utf8');
      fs.writeFileSync(path.join(outputDirectory, job.id + '-ocr-blocks.json'), JSON.stringify(data.blocks), 'utf8');
      const result = {
        ...job,
        elapsed_seconds: (performance.now() - started) / 1000,
        confidence: data.confidence,
        text_chars: data.text.length,
      };
      run.results.push(result);
      fs.writeFileSync(path.join(outputDirectory, 'ocr-run.json'), JSON.stringify(run, null, 2), 'utf8');
      console.log(JSON.stringify(result));
    }
  } finally {
    await worker.terminate();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
