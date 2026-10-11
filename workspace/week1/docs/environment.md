# Môi trường đã chạy — Vinamilk 2025, ngày 11/10/2026

Windows CPU, Python 3.12.15 tại `.venv-paddle/`; tạo bằng uv 0.13.0. `venv/` Python 3.14.7 cũ được giữ nguyên. Runtime Python quản lý trong `.tools/python/`; hai thư mục mới được Git-ignore.

PaddlePaddle 3.2.2, PaddleOCR 3.3.2, PaddleX 3.3.13. [Package lock](../config/requirements-paddle-win-py312.lock.txt) là kết quả freeze môi trường đã smoke thành công. Cài lại package bằng:

```powershell
.tools/bootstrap/bin/uv.exe pip install --python .venv-paddle/Scripts/python.exe -r workspace/week1/config/requirements-paddle-win-py312.lock.txt
```

Model detection `PP-OCRv5_mobile_det`; recognition `latin_PP-OCRv5_mobile_rec`, `lang=vi`, OCR v5. [Model lock](../config/paddleocr-models.lock.json) ghi SHA-256 của các file model đã dùng, không gồm cache. Model tải ở thư mục `.paddlex/official_models/` của tài khoản Windows; không nằm trong Git. Lock model dùng kiểm tính đồng nhất; chưa có kho model đóng gói để tự phục hồi offline.

Thiết lập: CPU, 4 threads, `enable_mkldnn=False`, tắt document orientation, unwarping và textline orientation; detection side limit 1600/max. PyMuPDF render PDF thành ảnh 180 DPI; toàn bộ text/giá trị đầu vào parser lấy từ Paddle, không từ text native PDF hay công cụ đọc PDF của Codex.

Paddle `run_check()` và inference ảnh VNM Q1 đã thành công. Hai phiên OCR PDF VNM 2025 cũng thành công (22 trang trong PDF 63 trang). [Nhật ký và lệnh chạy](vnm-2025.md), [smoke](evidence/vnm-2025/smoke-run.json), [OCR chính](evidence/vnm-2025/annual-ocr-run.json), [OCR bổ sung ngữ cảnh](evidence/vnm-2025/context-ocr-run.json).

Chưa kiểm nghiệm lợi thế chất lượng so với Tesseract; chưa cài/chạy web React + FastAPI + PostgreSQL trong lát cắt này. Sáu candidate chờ duyệt, không phải gold độc lập. Giờ công người thực hiện chưa ghi nhận; thời gian máy trong log không thay thế giờ công.

