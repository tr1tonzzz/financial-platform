# Kỹ thuật IT cho theo dõi công nợ và mô phỏng dòng tiền doanh nghiệp nhỏ

Schema invoice/payment/allocation, validation CSV, giao dịch nhiều khoản thanh toán, engine mô phỏng theo ngày/tuần và quản lý scenario. Có data lineage, chống trùng, kiểm thử timeline và snapshot. Bài tập: unit test hai payment cho một invoice và một khoản đến hạn chuyển qua tuần sau. OCR hóa đơn là mở rộng riêng, không trộn vào pilot khi chưa có dữ liệu.

Đầu ra cần giữ: source code module, dữ liệu đầu vào có nguồn, cấu hình, test phù hợp, log chạy và hạn chế. Đọc được dữ liệu hoặc gọi được thư viện không thay thế đánh giá đúng/sai trên bộ mẫu.

Nguồn và hồ sơ: [Odoo reporting](https://www.odoo.com/documentation/19.0/applications/finance/accounting/reporting.html), tìm kiếm đọc được mục cash flow/short-term forecast; web open trực tiếp có lúc lỗi. Đây là bằng chứng nhu cầu/chức năng đã có, không phải nguồn dataset.
