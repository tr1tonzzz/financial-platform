# I1 — Kỹ thuật IT: thu thập, parser và provenance

Ngày: 03/10/2026. Thiết kế đề xuất chi tiết hóa SDD; chưa có pipeline triển khai trong repository.

## 1. Luồng xử lý và hợp đồng dữ liệu

```text
company/year → discovered URL → downloaded raw + SHA-256
→ page/region candidates → normalized facts
→ validation + human review → published facts → dataset manifest
```

Mỗi bước giữ đầu vào, trạng thái và version. Phân biệt download fail, parse fail và review reject để đo đúng độ phủ. Chạy lại phải tiếp tục từ bước lỗi, không tải/nhân bản mọi tài liệu.

## 2. Adapter nguồn và kho raw

Adapter trả URL tài liệu, metadata công bố và phương thức phát hiện; downloader xử lý HTTP, timeout, retry hữu hạn, kiểm tra MIME/header PDF và lưu hash. URL không đủ làm định danh nội dung vì cùng URL có thể đổi file; hash giống nhau cũng không có nghĩa metadata/nguồn công bố giống nhau.

Lưu raw theo hash và bảng document–file; giữ công ty, kỳ, nguồn, published_at, retrieved_at, audit_status, scope và basis. Chỉ thêm trình duyệt tự động sau khi nguồn cần JavaScript đã được kiểm tra. Khảo sát VSDC local lỗi TLS: kiểm tra cấu hình CA/đường nguồn hợp lệ, không đặt `verify=False` làm giải pháp mặc định.

## 3. Parser theo cấu trúc

1. Nhận diện PDF text/scan theo ký tự có thể đọc; kiểm tra trang ảnh dù PDF có một ít chữ.
2. Tách spread/cột bằng vùng; xác định tiêu đề năm và đơn vị.
3. Lấy từ/nhãn cùng tọa độ; kết hợp nhãn, mã dòng và loại bảng.
4. Liên kết dòng xuống hàng, bắt số dưới đúng cột; giữ nhiều ứng viên khi mơ hồ.
5. Parse bằng Decimal; chuẩn hóa nhãn/Unicode nhưng giữ raw nguyên gốc.
6. Áp dụng validation và đưa lỗi/metadata thiếu sang review.

pdfplumber hỗ trợ `crop`, text và tọa độ; thử chiến lược theo vùng trước khi viết parser tổng quát. [Tài liệu dự án](https://github.com/jsvine/pdfplumber). OCR có thể dùng [Tesseract](https://github.com/tesseract-ocr/tesseract), nhưng phải đo riêng lỗi dấu âm và chữ số.

## 4. Thiết kế provenance tối thiểu

Áp dụng khái niệm entity/activity/agent của [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) vào bảng quan hệ:

| Bảng/liên kết | Trường cần có |
|---|---|
| `source_document`, `document_file` | URL, hash, thời điểm, scope, basis, audit evidence |
| `extraction_candidate` | page_pdf, page_printed, bbox/locator, raw label/value/unit/year, method/version |
| `financial_fact_version` | metric, period, value_vnd, candidate_id, available_at, validation/review |
| `review_decision` | fact, old/new, reviewer, reason, evidence, reviewed_at |
| `snapshot_fact` | snapshot, fact_version_id, selection_reason |

Truy từ chart/API → metric result → fact versions → candidates → hash file + vùng. Phân biệt provenance đầy đủ với nguồn đáng tin và fact đúng; cả ba phải được kiểm tra.

## 5. Ràng buộc và xuất bản

Số tiền gốc lưu [NUMERIC](https://www.postgresql.org/docs/current/datatype-numeric.html); quan hệ dùng [FK/UNIQUE/CHECK](https://www.postgresql.org/docs/current/ddl-constraints.html). Kiểm tra period_end ≥ period_start, multiplier dương, version có nguồn; các quy tắc liên bảng cần validation trong pipeline.

Đề xuất khóa fact gồm company, metric, period, scope, basis, file/source version và parser version. Không ghi đè bản đã duyệt khi parser chạy lại; snapshot chọn version rõ. Facts chưa rõ đơn vị/phạm vi không xuất bản để tính tỷ số.

## 6. Những kỹ năng cần học và giới hạn

Python đọc file/HTTP/Decimal; regex và Unicode; SQL quan hệ/transaction; cấu trúc PDF và tọa độ; kiểm thử fixture; logging và manifest. Bắt đầu batch script đơn tiến trình; chưa cần Kafka, Spark, microservices hoặc graph database ở quy mô đề tài.

Benchmark và kiểm tra tái lập ở [protocol I1](04-du-lieu-thi-nghiem-danh-gia.md). Kiến trúc chỉ mở rộng khi đo được nút thắt.
