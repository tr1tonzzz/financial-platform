# Theo dõi công nợ và mô phỏng dòng tiền doanh nghiệp nhỏ

Khảo sát và đề xuất ngày 03/10/2026. Trạng thái: thiết kế/đánh giá khả thi, không phải chức năng ứng dụng đã hoàn thành.

## Bài toán và người dùng

Doanh nghiệp nhỏ có doanh thu nhưng thiếu tiền khi khách trả chậm. Hệ thống dự kiến thu/chi từ hóa đơn, khoản đến hạn và điều kiện thanh toán.

## Dữ liệu và bằng chứng khả thi

Hóa đơn, khoản phải thu/phải trả, lịch thanh toán và số dư ngân hàng do đơn vị hợp tác cung cấp. Đã đọc tài liệu sản phẩm Odoo; chưa có đơn vị hoặc dữ liệu thật. BCTC niêm yết công khai không thay thế được giao dịch/đến hạn nội bộ.

## MVP nếu chọn hướng này

CSV invoices/payments, aging công nợ và mô phỏng 8–13 tuần theo kịch bản trả đúng hạn/chậm; cho sửa giả định. Hệ thống theo dõi thanh toán một phần, không xây toàn bộ phần mềm kế toán.

## Đóng góp IT và cách đánh giá

Đối chiếu số dư và aging, kiểm thử thanh toán một phần/quá hạn, đo sai số dự toán trên lịch sử khi có dữ liệu thật. Dữ liệu mô phỏng chỉ xác minh thuật toán/kịch bản.

## Điểm khó cần xử lý

Thiếu dữ liệu hợp tác là blocker lớn; OCR hóa đơn và chuẩn hóa nghiệp vụ có thể vượt thời gian. Không tuyên bố chính xác dự báo từ dữ liệu giả lập.

## Liên thông lên đồ án tốt nghiệp

Đánh giá mô hình ngày thanh toán hoặc tối ưu kịch bản thu/chi nếu có doanh nghiệp cung cấp lịch sử đủ dài và yêu cầu thực.

## Tài liệu đi kèm

[Kiến thức tài chính](02-kien-thuc-tai-chinh.md); [kỹ thuật IT](03-ky-thuat-it.md). Nguồn: [Odoo reporting](https://www.odoo.com/documentation/19.0/applications/finance/accounting/reporting.html), tìm kiếm đọc được mục cash flow/short-term forecast; web open trực tiếp có lúc lỗi. Đây là bằng chứng nhu cầu/chức năng đã có, không phải nguồn dataset.
