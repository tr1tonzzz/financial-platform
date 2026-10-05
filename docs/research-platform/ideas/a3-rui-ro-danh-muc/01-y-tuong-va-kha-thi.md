# Phân tích rủi ro và hiệu quả danh mục

Khảo sát và đề xuất ngày 03/10/2026. Trạng thái: thiết kế/đánh giá khả thi, không phải chức năng ứng dụng đã hoàn thành.

## Bài toán và người dùng

Người dùng muốn kiểm tra một danh mục giả định biến động và sụt giảm ra sao, so với nắm giữ đơn giản. Đầu ra là phân tích dữ liệu lịch sử và mô phỏng có giả định.

## Dữ liệu và bằng chứng khả thi

Giá cuối ngày, lịch giao dịch, giá điều chỉnh, sự kiện doanh nghiệp và benchmark. Đã đọc README chính thức Vnstock; chưa chạy tải hay xác nhận độ phủ 2025–2026. Thư viện kết nối nguồn thứ ba và giấy phép phần mềm không cấp quyền dữ liệu nguồn.

## MVP nếu chọn hướng này

CSV giá có nguồn cho 5–10 mã; kiểm tra dữ liệu, tính returns, volatility, drawdown và so sánh equal-weight với buy-and-hold. Không giao dịch thật hoặc dự báo giá làm lõi.

## Đóng góp IT và cách đánh giá

Đối chiếu return/drawdown với ví dụ tính tay; backtest không nhìn tương lai, có phí giả định, kiểm tra dữ liệu điều chỉnh. Chia train/test theo thời gian nếu chọn tham số chiến lược.

## Điểm khó cần xử lý

Nguồn giá, điều chỉnh chia tách/cổ tức, survivorship bias, phí và thống kê khó hơn nền hiện tại. Chưa có benchmark nguồn thật trong repo.

## Liên thông lên đồ án tốt nghiệp

Tối ưu danh mục có ràng buộc hoặc phân tích rủi ro ngoài mẫu, sau khi giải quyết nguồn và phương pháp; vẫn là nhánh độc lập với quan hệ BCTC–cổ tức.

## Tài liệu đi kèm

[Kiến thức tài chính](02-kien-thuc-tai-chinh.md); [kỹ thuật IT](03-ky-thuat-it.md). Nguồn: [README chính thức Vnstock](https://github.com/thinh-vu/vnstock). Thông tin ở đây là khảo sát tài liệu, chưa phải thử tải giá.
