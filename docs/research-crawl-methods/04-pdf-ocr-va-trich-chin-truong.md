# Kỹ thuật IT: từ PDF đến chín trường có kiểm chứng

> **Trạng thái 03/10/2026 — hồ sơ thử nghiệm thu thập.** Project hiện hành tập trung thu thập, kiểm định và phân tích lợi nhuận–dòng tiền–cổ tức tiền mặt. Xem [SRS hiện hành](../research-platform/02-de-tai-va-srs.md) và [phương pháp thống nhất](../research-platform/11-phuong-phap-thu-thap-va-xu-ly.md). Các ngưỡng cảnh báo, dự báo, scope và lịch cũ bên dưới chỉ để tham khảo; không là yêu cầu MVP hiện hành.

## 1. Crawl file và trích số là hai gate

Đã vượt gate thu thập: tám PDF tự tìm/tải, mở được bằng pypdf. Chưa vượt gate dataset: chưa có chín trường đã duyệt trên tám tài liệu. Không lấy download success rate làm accuracy số tài chính.

Trong mẫu mới, script đếm trang và thử `extract_text` trên **12 trang đầu mỗi PDF**, ngưỡng “text đủ để khảo sát” là trên 100 ký tự. Kết quả 0/96 trang đạt ngưỡng, tổng tài liệu có 423 trang. Đây là chỉ báo cần OCR cho các trang chính; chưa là kiểm tra từng trang toàn tài liệu, chưa là benchmark parser. [pdfplumber](https://github.com/jsvine/pdfplumber) cung cấp text/tọa độ/bảng cho PDF có lớp text; không tự biến ảnh scan thành số đúng.

Khảo sát trước trên 15 PDF có nhiều tài liệu không có text đủ dùng; một PDF HPG Q1/2026 có text dài nhưng lỗi encoding. Vì vậy không chỉ hỏi “có text hay không”: cần tỷ lệ ký tự lỗi, nhãn tài chính có thể đọc, trật tự cột và header kỳ/unit.

## 2. Luồng trích xuất đề xuất

1. Kiểm tra `%PDF-`, mở được, đếm trang; giữ file raw và SHA-256.
2. Đọc text/tọa độ các trang; dò mục lục và các bảng chính. Quyết định OCR theo từng trang thay vì OCR toàn bộ thuyết minh ngay.
3. Render trang cần thiết khoảng 220–300 dpi; xử lý nghiêng/độ tương phản khi thực nghiệm cho thấy cần. Không mặc định xử lý ảnh luôn tăng accuracy.
4. OCR `vie+eng`, giữ text và bounding boxes, runtime, engine/model version. [Tesseract](https://github.com/tesseract-ocr/tesseract) là baseline phù hợp; Tesseract.js đã được chạy trong khảo sát trước. Chưa có so sánh PaddleOCR/layout model trong lần này.
5. Nhận dạng loại bảng, header kỳ/phạm vi/đơn vị, nhãn và mã chỉ tiêu; gom dòng bị ngắt.
6. Xác định ô theo cột/tọa độ, chuẩn hóa số; tạo **candidate**, không tự xuất như fact đã đúng.
7. Validator và màn hình review kiểm tra; lưu sửa đổi trước/sau/lý do, rồi xuất dữ liệu đã duyệt.

Ví dụ báo cáo scan có chữ “Doanh thu thuần về bán hàng và” trên một dòng, “cung cấp dịch vụ” ở dòng sau. Regex tìm nhãn trên một dòng đơn có thể không thấy. Cần cửa sổ nhiều dòng hoặc cấu trúc hàng/ô, nhưng giới hạn phạm vi để không kéo số của hàng khác.

## 3. Những kỹ thuật nên so sánh

| Baseline/phương án | Vai trò | Trạng thái |
|---|---|---|
| B0: text-only + nhãn | Baseline để thấy thiếu dữ liệu scan | Đã có khảo sát text; chưa benchmark chín trường trên holdout |
| B1: text + OCR fallback + parser cột | Phương án MVP | OCR và regex sáu trường đã thử trước; parser chín trường/cột còn cần xây |
| B2: B1 + validation + human review | Dữ liệu xuất bản có kiểm chứng | Quy trình thiết kế; các ví dụ đã đối chiếu tay, chưa có UI/audit ứng dụng |
| Layout/table model hoặc LLM | Nâng cấp khi B1 có lỗi đo được | Chưa cần trong MVP; chưa chứng minh tốt hơn hoặc tiết kiệm công sức |

OCR confidence không phải xác suất số tiền đúng. Một chữ nhãn sai có thể mất trường; một chữ số sai có thể làm lệch hàng tỷ đồng. Không cho LLM tự điền trường thiếu bằng suy đoán; nếu dùng thì phải trả locator và bị kiểm định giống candidate khác.

## 4. Kiểm định phù hợp

Kiểm tra tổng tài sản − tổng nợ − tổng VCSH trong sai số do đơn vị/làm tròn; tài sản ngắn hạn ≤ tổng tài sản, nợ ngắn hạn ≤ tổng nợ; cột kỳ/unit/scope thống nhất; dòng doanh thu thuần đúng loại, LNST tổng khác phần cổ đông mẹ. Dùng dấu âm và missing đúng quy tắc tài liệu. Cân đối đúng chỉ là một kiểm tra: nếu parser lấy đồng loạt cột năm trước thì phép cân đối vẫn có thể đúng.

Không tự gán giá trị 0 khi không trích được. Không bỏ các trường khó khỏi mẫu số đánh giá. Một fact chỉ được công bố khi có document hash/version, trang/locator, kỳ, đơn vị, scope và trạng thái review.

## 5. Bằng chứng OCR hiện có và việc chưa làm

Khảo sát trước dùng 10 trang chọn từ DHG FY2025 và VNM Q1/2026; sáu trường × hai PDF = 12 ô được đối chiếu ảnh, regex tìm khớp 11/12 trước sửa tay. Người viết parser cũng tham gia đối chiếu, nên đây là mẫu phát triển, không phải gold độc lập. Xem [bằng chứng trước](../research-recent-data/ocr-core-check.json).

Lần nghiên cứu crawl này không chạy lại OCR trên toàn tám PDF mới, không mở rộng kết quả cũ thành “chín trường đã đạt”. Gate tiếp theo là sáu BCTC pilot, chín target/tài liệu, bảng missing/lỗi và phút review. Chỉ sau đó chốt số công ty và mức tự động hóa thực tế.
