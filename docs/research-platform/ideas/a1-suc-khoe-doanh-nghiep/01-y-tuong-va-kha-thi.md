# Phân tích sức khỏe tài chính doanh nghiệp

> **Phương án A1 trước, không còn là scope triển khai.** Kiến thức/pipeline có thể tái sử dụng cho [hướng A2 hiện hành](../../README.md); mức 10 doanh nghiệp/chín chỉ tiêu ở đây là đề xuất cũ.

Khảo sát và đề xuất ngày 03/10/2026. Trạng thái: thiết kế/đánh giá khả thi, không phải chức năng ứng dụng đã hoàn thành.

## Bài toán và người dùng

Người học hoặc người phân tích cần so sánh lợi nhuận, tiền và cấu trúc tài chính của doanh nghiệp nhưng phải đọc nhiều PDF khác bố cục và kiểm tra ý nghĩa từng số. Người dùng chọn công ty và kỳ, xem xu hướng, công thức, mức đủ dữ liệu và mở đúng vị trí nguồn.

## Dữ liệu và bằng chứng khả thi

BCTC năm chính thức, metadata doanh nghiệp và ngành. Khảo sát trước đã tải 15 PDF của 5 công ty; mới đối chiếu sáu chỉ tiêu trên hai báo cáo. Doanh thu thuần, tài sản ngắn hạn và nợ ngắn hạn là ba trường bổ sung phải xác minh ở pilot. Không cần cổ tức hoặc giá thị trường để hoàn thành lõi.

## MVP nếu chọn hướng này

Pilot 3 công ty × 2 năm; mục tiêu project 10 công ty × 2023–2025, chín chỉ tiêu, ba nhóm phân tích, hàng đợi duyệt và dashboard. Các mục tiêu chỉ đạt sau kiểm tra nguồn và công sức, không dựa vào số file tải được.

## Đóng góp IT và cách đánh giá

So sánh text-only với OCR có xử lý cột, đo đúng số/đơn vị/kỳ/scope, độ phủ, phút sửa, khả năng chạy lại. Ba case phải truy được từ chart về số gốc. Kết quả trước và sau người duyệt được báo cáo riêng.

## Điểm khó cần xử lý

PDF scan, đổi mã dòng, nhầm cột, thiếu năm và khác cơ sở kế toán. Hạn chế ngành ngân hàng/bảo hiểm; không tạo điểm sức khỏe tổng hợp hoặc xác suất phá sản khi chưa kiểm định.

## Liên thông lên đồ án tốt nghiệp

Ưu tiên phát triển hỏi đáp số liệu có dẫn nguồn và phép tính kiểm chứng trên dataset đã duyệt; hoặc nghiên cứu phát hiện bất thường/phiên bản như một hướng thay thế. Không buộc triển khai mọi nhánh.

## Tài liệu đi kèm

[Kiến thức tài chính](02-kien-thuc-tai-chinh.md); [kỹ thuật IT](03-ky-thuat-it.md). Nguồn: [Khảo sát dữ liệu thật](../../../research-recent-data/README.md); [SEC hướng dẫn BCTC](https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements); [pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html).
