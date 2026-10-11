// OCR các trang không lấy được lớp chữ PDF.
const fs = require('node:fs');
const path = require('node:path');

async function main() {
  if (!process.argv[2]) throw new Error('Usage: node ocr.cjs <output-directory>');
  const output = path.resolve(process.argv[2]);
  const probe = JSON.parse(fs.readFileSync(path.join(output, 'pdf-probe.json'), 'utf8'));
  if (!probe.ocr_pages.length) {
    console.log('PDF text is available. No pages need OCR.');
    return;
  }
  const { createWorker } = require('tesseract.js');
  // Nhận dạng tiếng Việt và Anh bằng engine LSTM; lưu dữ liệu ngôn ngữ để dùng lại.
  const worker = await createWorker(['vie', 'eng'], 1, {
    cachePath: path.join(output, 'ocr-cache'),
  });
  try {
    for (const page of probe.ocr_pages) {
      // Chờ OCR xong ảnh hiện tại rồi mới lưu văn bản và chuyển sang trang tiếp theo.
      const { data } = await worker.recognize(path.join(output, `page-${page}.png`));
      fs.writeFileSync(path.join(output, `page-${page}-ocr.txt`), data.text, 'utf8');
      console.log(`OCR page ${page} complete`);
    }
  } finally {
    // Đóng worker và giải phóng tài nguyên kể cả khi OCR lỗi.
    await worker.terminate();
  }
}

main().catch(error => { console.error(error.message); process.exitCode = 1; });
