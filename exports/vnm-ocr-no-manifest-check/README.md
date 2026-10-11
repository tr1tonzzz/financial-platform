# Thử nghiệm Vinamilk: tải mẫu, đọc PDF, OCR và trích số

## Công cụ và phiên bản

| Công cụ | Phiên bản dùng trong thử nghiệm |
|---|---|
| Python | 3.12.14 |
| pypdf | 6.10.0 |
| Node.js | 24.15.0 |
| Tesseract.js | 7.0.0 |
| Poppler (`pdftoppm`) | 26.07.0 |

## Cài thư viện

Chạy các lệnh sau tại folder chứa các script:

```powershell
python -m pip install pypdf==6.10.0
npm install tesseract.js@7.0.0 --no-save --package-lock=false
```

Tesseract.js được cài vào `node_modules/` ngay trong folder này.
`--no-save` không ghi khai báo gói; `--package-lock=false` không tạo file khóa.

## Bước 1 — Tải mẫu từ URL định sẵn

```powershell
python download_sample.py output
```

URL danh mục và PDF được khai báo trong `download_sample.py`.
Tạo `output/catalog.html`, `output/sample.pdf` và `output/source-probe.json`.

## Bước 2 — Thử đọc lớp chữ PDF

```powershell
python read_pdf.py output
```

Script dùng pypdf thử lấy chữ trên từng trang, lưu thành `page-N-pdf.txt`.
File `pdf-probe.json` ghi số trang, số ký tự và danh sách trang cần OCR.

- Nếu các trang 12–14 có chữ: bỏ qua bước 3 và 4, chuyển thẳng đến bước 5.
- Nếu có trang không lấy được chữ: thực hiện bước 3 và 4 cho những trang đó.

## Bước 3 — Chuyển trang không đọc được thành ảnh

```powershell
python render_pages.py output
```

Nếu Poppler chưa nằm trong PATH, dùng đường dẫn thực tế:

```powershell
python render_pages.py output --pdftoppm "C:/path/to/poppler/Library/bin/pdftoppm.exe"
```

Script đọc `pdf-probe.json`, chỉ chuyển các trang cần OCR thành PNG ở 220 DPI.

## Bước 4 — Đọc OCR

```powershell
node ocr.cjs output
```

Script đọc `pdf-probe.json`, chỉ OCR các trang không lấy được lớp chữ.
Lưu văn bản vào `page-N-ocr.txt`. Dữ liệu ngôn ngữ nằm trong `output/ocr-cache/`.

## Bước 5 — Trích số

```powershell
python extract_numbers.py output
```

Script lấy số từ văn bản PDF nếu đọc được, hoặc văn bản OCR nếu trang cần OCR.
Tạo `output/data.json` và in số liệu ra terminal.

## Các file kết quả trong `output/`

| File | Nội dung |
|---|---|
| `catalog.html` | HTML tải từ danh mục |
| `sample.pdf` | Báo cáo PDF tải về |
| `source-probe.json` | URL và nhật ký tải |
| `page-N-pdf.txt` | Văn bản trích trực tiếp của từng trang PDF |
| `pdf-probe.json` | Kết quả đọc lớp chữ và trang cần OCR |
| `page-N.png` | Ảnh những trang cần OCR |
| `page-N-ocr.txt` | Văn bản OCR |
| `data.json` | Số liệu trích được |
