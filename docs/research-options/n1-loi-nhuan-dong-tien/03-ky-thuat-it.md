# N1 — Kỹ thuật IT cho cầu nối dòng tiền

Thiết kế đề xuất, chưa triển khai. [Đề xuất](01-de-xuat-nghien-cuu.md), [ngữ nghĩa tài chính](02-kien-thuc-tai-chinh.md).

## 1. Dữ liệu cần bổ sung

Giữ facts có nguồn hiện hành. Mỗi dòng cầu nối lưu `company_id`, `period_start/end`, `statement_scope`, `accounting_basis`, `document_id`, `page`, `raw_label`, `raw_value`, `unit`, `normalized_value`, `cash_sign`, `mapping_version`, `review_status` và `available_at` nếu xác định được.

Thêm `bridge_group`, `parent_line_id` và `include_in_sum` để phân biệt subtotal với thành phần. Một khoản bị OCR hoặc mapping nghi ngờ không đưa vào cầu nối đã duyệt. Phải thu thương mại tách khỏi tổng phải thu; phải trả người bán tách khỏi tổng nợ ngắn hạn.

## 2. Trích xuất và chuẩn hóa

Trước hết dùng text/vị trí PDF và mapping có review. [pdfplumber](https://github.com/jsvine/pdfplumber) hỗ trợ đọc text và vị trí, nhưng PDF mẫu trước đây đã không được nhận diện bảng tự động; cần chọn vùng và kiểm tra tiêu đề/kỳ. Chỉ bổ sung OCR nếu benchmark nguồn scan cho thấy cần thiết.

Pipeline cho từng case: xác định báo cáo tiền tệ/phương pháp → đọc cột năm đúng → chuẩn hóa số và dấu → phân nhóm dòng → duyệt → tính lại cầu nối. Lưu mọi lần sửa với giá trị trước/sau và lý do. Đơn vị số tiền dùng decimal hoặc [PostgreSQL numeric](https://www.postgresql.org/docs/current/datatype-numeric.html).

## 3. Engine giải thích

Tính số từ facts đã duyệt, không để bộ sinh văn bản tự tính. Output gồm dòng khởi đầu, mỗi điều chỉnh có dấu, CFO công bố/tái dựng, residual, mức đầy đủ và dẫn nguồn. Nếu chưa đủ, trả `partial_bridge`, không đánh dấu đã đối chiếu thành công.

DSO/DIO/DPO là functions có domain check: mẫu số dương, đủ số dư đầu kỳ, kỳ/phạm vi trùng và proxy được công bố. Mỗi công thức có phiên bản và danh sách facts đầu vào. Không lấy số liệu bổ sung công bố sau thời điểm dự báo vào features lịch sử.

## 4. UI tối thiểu

Biểu đồ waterfall hoặc bảng có dấu, cột trang nguồn và residual giúp giải thích một case. Người xem chuyển giữa cầu nối CFO và chỉ số vốn lưu động; mỗi phát biểu phải chỉ đến số liệu hỗ trợ. Nội dung có thể tạo từ template, chưa cần LLM.

## 5. Kiểm tra cần thiết khi triển khai

Kiểm tra nhầm năm, dấu ngoặc âm, đổi đơn vị, double count subtotal, thiếu số đầu kỳ và thay đổi phạm vi. Với báo cáo trực tiếp, không ép chạy engine gián tiếp. Việc kiểm tra này là backlog, chưa có test suite hoặc kết quả kiểm thử mới trong lượt tài liệu.
