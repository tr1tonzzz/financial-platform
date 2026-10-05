# I1 — Nghiên cứu dữ liệu BCTC có truy vết

Ngày: 03/10/2026. Mức ưu tiên: P0, lõi MVP, trả lời RQ1. [Bộ hồ sơ](../README.md).

## 1. Vấn đề và kết luận đề xuất

Một số tài chính chỉ dùng được khi xác định đúng đơn vị, kỳ, phạm vi báo cáo và vị trí nguồn. Vì vậy nên nghiên cứu **pipeline trích xuất có kiểm định và review**, rồi đo độ đúng cùng công sức. Đây là điều kiện để mọi phân tích cổ tức phía sau đáng tin.

Khảo sát Vinamilk cho thấy PDF có text nhưng table detector mặc định không trả bảng. Parser theo vùng đọc được sáu chỉ tiêu trong một file; chưa chứng minh độ đúng trên nhiều bố cục. [Bằng chứng thực hiện](../03-khao-sat-nguon-thuc-te.md).

## 2. Câu hỏi và giả thuyết

- I1-RQ1: parser theo nhãn và vùng có tăng độ đúng kết hợp so với tìm nhãn trong text toàn trang không?
- I1-RQ2: validation nghiệp vụ phát hiện được những lỗi đơn vị/kỳ/phạm vi nào, và bỏ sót gì?
- I1-RQ3: thời gian làm sạch một báo cáo có giảm so với nhập tay, sau khi tính cả review và lỗi còn lại không?

Giả thuyết thăm dò: giữ tọa độ và thông tin cột làm giảm nhầm năm; review tập trung các trường thiếu metadata giúp giảm công sức. Chưa có kết quả để xác nhận hai giả thuyết này.

## 3. Phạm vi và đóng góp

Sáu facts lõi trên BCTC năm kiểm toán 2020–2024 của doanh nghiệp phi tài chính. Pilot 10 công ty; mẫu MVP 30; mở rộng 60–80 theo PP. Ưu tiên một cơ sở kế toán và hợp nhất; loại khác giữ tách biệt.

Đóng góp gồm benchmark lỗi thực tế, bộ mapping có phiên bản, provenance tới trang/vùng và quy trình sửa có lưu vết. Không gọi thư viện parser hoặc một tập regex là thuật toán mới. Chất lượng dữ liệu và khả năng tái lập là điểm đánh giá chính.

## 4. Phương án kỹ thuật cần so sánh

| Phương án | Vai trò | Điều kiện |
|---|---|---|
| Đọc/nhập tay | Baseline công sức và gold | Ghi thời gian và lỗi nhập; kiểm tra lại |
| Text toàn trang + nhãn | Baseline tự động | Giữ raw; dễ nhầm cột/spread |
| Text theo vùng/tọa độ + nhãn + validation | Phương án đề xuất | Có metadata, locator và review |
| OCR + quy trình trên | Nhánh bổ sung | Chỉ khi scan có tỷ trọng đáng kể và còn quỹ giờ |

Tự động hóa toàn bộ và hỗ trợ review là hai mức cần đo riêng. Không ghi số sau sửa tay thành độ chính xác parser tự động.

## 5. Sản phẩm và tiêu chí

Raw manifest, gold facts, parser/mapping specification, bảng coverage/accuracy/error, log review, snapshot và hướng dẫn chạy lại. Ngưỡng SRS đề xuất: ≥95% độ đúng kết hợp, ≥80% độ phủ lõi, 100% provenance trên facts xuất bản. Đây là mục tiêu, chưa đạt.

Tiêu chí thành công học thuật còn gồm kết luận rõ parser sai ở đâu và công sức cần bao nhiêu, kể cả nếu không đạt ngưỡng. Không dùng fixture giả để thay benchmark nguồn thật.

## 6. Tài liệu cần dùng và bước tiếp

Đọc [tài chính/ngữ nghĩa](02-kien-thuc-tai-chinh.md), [IT/provenance](03-ky-thuat-it.md), [protocol benchmark](04-du-lieu-thi-nghiem-danh-gia.md). Nguồn nền: [pdfplumber](https://github.com/jsvine/pdfplumber) và [W3C PROV-DM](https://www.w3.org/TR/prov-dm/); mức đọc ở T01/T02 trong sổ nguồn.

Bước nghiên cứu tiếp: lấy 20 BCTC phù hợp cohort từ ít nhất 10 công ty; đánh dấu text/scan/spread; đọc gold trước khi tinh chỉnh parser; tách file đánh giá cuối.
