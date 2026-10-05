# N1 — Dữ liệu, thí nghiệm và đánh giá

Protocol đề xuất, 03/10/2026; chưa thực hiện. [Tài chính](02-kien-thuc-tai-chinh.md), [IT](03-ky-thuat-it.md).

## 1. Thiết kế case ban đầu

Chọn tối đa ba doanh nghiệp từ mẫu lõi, căn cứ độ đủ nguồn và sự khác biệt lợi nhuận–CFO. Ghi lý do chọn trước khi diễn giải cổ tức; không gọi mẫu chọn theo tình huống là đại diện toàn thị trường. Cố gắng có case dòng tiền yếu, case tương đối ổn định và case thiếu dữ liệu để thể hiện giới hạn.

Mỗi case cần BCTC kiểm toán, bảng CFO và bảng cân đối cùng kỳ; số đầu kỳ nếu tính bình quân; công bố cổ tức đã chuẩn hóa. Thêm một năm trước để đọc biến động. Xác minh báo cáo hợp nhất/riêng, đơn vị và ngày thông tin có thể biết.

## 2. Đối chiếu dữ liệu

Lập bảng gold đọc từ tài liệu gốc với giá trị, dấu, kỳ, trang và người kiểm tra. Dùng cách đọc độc lập với parser; tự nhìn lại output parser chưa phải gold độc lập. Khi không có người kiểm tra thứ hai, ghi hạn chế và lưu checklist đọc lại từ raw trước khi xem output.

Đo: độ đúng dòng trước/sau review, tỷ lệ cầu nối đủ, residual tuyệt đối và trên quy mô, thời gian xử lý từng báo cáo. Sai số cho phép xuất phát từ đơn vị làm tròn của bảng, không chọn tolerance để che dòng bỏ sót. Ghi tổng số dòng kỳ vọng và số dòng kiểm tra để tỷ lệ có mẫu số rõ.

## 3. Đánh giá giá trị giải thích

So sánh hai bản của cùng case: A chỉ có sáu chỉ tiêu lõi; B có cầu nối/vốn lưu động. Dùng bộ câu hỏi cố định: CFO thấp do dòng nào được công bố? còn phần chưa giải thích? kết luận nào có đủ nguồn? Người đánh giá kiểm tra tính đúng, thời gian tìm căn cứ và tỷ lệ phát biểu có evidence.

Nếu chưa có người dùng độc lập, chỉ báo cáo kiểm tra tài liệu theo rubric; không gọi đó là chứng minh cải thiện trải nghiệm người dùng. Không thay “không đủ căn cứ” bằng kết luận chắc chắn để tăng số câu trả lời.

## 4. Nếu mở rộng sang phân tích toàn mẫu

Giữ cùng tập quan sát đủ dữ liệu để so sáu chỉ tiêu lõi với bộ bổ sung. Kiểm soát thay đổi độ phủ, ngành và năm; nếu thử dự báo, áp dụng chia thời gian và gate từ [đề cương](../../research-design.md). Không ngẫu nhiên chia các dòng cùng doanh nghiệp–năm hoặc fit preprocessing trên toàn mẫu.

Mẫu nhỏ chỉ hỗ trợ thống kê mô tả và case. Quan hệ vốn lưu động–cổ tức chưa chứng minh tác động nhân quả. Kết quả bổ sung yếu vẫn phải báo cáo.

## 5. Kết quả cần lưu

`case-selection.md`, bảng dòng CFO có evidence, công thức/phiên bản, residual và lỗi còn lại, bảng câu hỏi đánh giá, ba bản phân tích cùng giới hạn. Đây là danh sách artifact cần tạo khi làm N1; các artifact và dữ liệu đó chưa tồn tại chỉ vì protocol này đã được viết.
