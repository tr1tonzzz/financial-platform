# N4 — Đối chiếu phiên bản và chất lượng công bố BCTC

Hướng mở rộng kỹ thuật dữ liệu hoặc phương án thay thế có điều kiện; chưa triển khai. [Tài chính](02-kien-thuc-tai-chinh.md), [IT](03-ky-thuat-it.md), [protocol](04-du-lieu-thi-nghiem-danh-gia.md).

## Bài toán

Số của một kỳ có thể xuất hiện trong báo cáo gốc, bản sửa đổi hoặc cột so sánh của báo cáo kỳ sau. N4 hỏi các giá trị có thực sự cùng cơ sở không, số nào người nghiên cứu có thể biết tại một ngày, và chọn phiên bản ảnh hưởng chỉ số như thế nào.

Lưu lịch sử đã có trong ghi chú cũ và thiết kế hiện hành. Giá trị nghiên cứu bổ sung của N4 là xây bộ cặp đối chiếu, phân loại khác biệt và đo ảnh hưởng trước/sau lựa chọn phiên bản; không gọi việc append thêm record là phương pháp mới.

## Câu hỏi nghiên cứu

- Có thể phát hiện chênh lệch thật giữa hai công bố cùng cơ sở và phân biệt với lỗi trích xuất/đơn vị/phạm vi không?
- Truy vấn theo ngày thông tin công khai khác lấy giá trị mới nhất ở những case nào?
- Dùng số so sánh/điều chỉnh công bố muộn làm thay đổi chỉ số hoặc cảnh báo lịch sử ra sao?

Nguồn IAS 8 và SEC trong [sổ nguồn](../02-tai-lieu-va-co-so-lua-chon.md) giúp định nghĩa vấn đề; case nghiên cứu vẫn phải là báo cáo Việt Nam trong phạm vi project. SEC không thay nguồn dữ liệu Việt Nam.

## Hai cách lựa chọn

**Trong đề tài hiện hành:** giữ versioning cơ bản bắt buộc; thêm vài cặp báo cáo để đánh giá ảnh hưởng phiên bản, nếu tìm được nguồn. Nó hỗ trợ tính tin cậy và tránh rò rỉ thời gian khi phân tích cổ tức.

**Làm đề tài thay thế:** “Hệ thống thu thập, chuẩn hóa và đối chiếu phiên bản BCTC doanh nghiệp Việt Nam có truy vết.” Câu hỏi chính chuyển thành chất lượng dữ liệu và khả năng tái lập; cổ tức có thể là một case ứng dụng. Chỉ cân nhắc sau pilot nếu không xây được nhãn cổ tức đủ căn cứ. Tên này chưa được chọn thay tên hiện hành.

## Giá trị và điều kiện

Hướng này gắn rõ với data engineering và cho phép đánh giá bằng gold cặp tài liệu, nhưng không tự dễ: báo cáo gốc có thể bị thay trên URL, ngày công bố thiếu, số so sánh khác cơ sở và sự kiện điều chỉnh hiếm. Cần mẫu đối chiếu thật; không dựng ví dụ giả làm bằng chứng doanh nghiệp.

Không gọi mọi chênh lệch là gian lận hoặc sai sót kế toán. Những trường hợp chưa có notes giải thích phải giữ “chưa xác định”.
