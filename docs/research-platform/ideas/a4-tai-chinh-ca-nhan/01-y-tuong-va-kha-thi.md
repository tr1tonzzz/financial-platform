# Quản lý thu chi và ngân sách cá nhân

Khảo sát và đề xuất ngày 03/10/2026. Trạng thái: thiết kế/đánh giá khả thi, không phải chức năng ứng dụng đã hoàn thành.

## Bài toán và người dùng

Người dùng muốn hiểu tiền vào/ra, khoản chi định kỳ và khả năng đạt mục tiêu tiết kiệm. Đây là lĩnh vực tài chính khác BCTC doanh nghiệp.

## Dữ liệu và bằng chứng khả thi

CSV do người dùng tự xuất hoặc tự nhập; nhãn chi tiêu tự chấm. Có thể dùng dữ liệu giả lập có gắn nhãn để kiểm thử, nhưng không coi là dữ liệu người dùng thật hoặc bằng chứng phân loại tốt. Chưa có dataset thực của người dùng trong repo.

## MVP nếu chọn hướng này

Import một định dạng CSV, chống giao dịch trùng, chỉnh nhóm chi, báo cáo dòng tiền và ngân sách tháng. Không tích hợp tài khoản ngân hàng khi chưa có đường truy cập chính thức.

## Đóng góp IT và cách đánh giá

Đúng số dư/tổng nhóm, xử lý hoàn tiền/chuyển khoản nội bộ; độ chính xác phân nhóm trên giao dịch thật được phép dùng; thời gian người dùng sửa và khả năng xóa/export dữ liệu.

## Điểm khó cần xử lý

Thuận lợi học phần mềm nhưng dễ chỉ thành CRUD nếu không làm import, reconciliation, phân loại và đánh giá. Tái sử dụng dữ liệu/crawler doanh nghiệp trước đây ít.

## Liên thông lên đồ án tốt nghiệp

Phân loại giao dịch tiếng Việt, nhận diện khoản định kỳ, dự toán dòng tiền cá nhân có đánh giá người dùng. Cần tập giao dịch thật phù hợp và bảo vệ dữ liệu.

## Tài liệu đi kèm

[Kiến thức tài chính](02-kien-thuc-tai-chinh.md); [kỹ thuật IT](03-ky-thuat-it.md). Nguồn: [CFPB spending tracker](https://www.consumerfinance.gov/archive/blog/track-your-spending-with-this-easy-tool/). Nguồn này giải thích nhu cầu theo dõi chi, không cung cấp dataset người dùng cho project.
