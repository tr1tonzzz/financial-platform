# N1 — Giải thích khả năng chuyển lợi nhuận thành tiền

Trạng thái: đề xuất mở rộng cho case study, 03/10/2026. [Tài chính](02-kien-thuc-tai-chinh.md), [IT](03-ky-thuat-it.md), [thí nghiệm](04-du-lieu-thi-nghiem-danh-gia.md).

## Bài toán và giá trị mới

Sáu chỉ tiêu lõi cho thấy lợi nhuận và CFO khác nhau nhưng chưa giải thích vì sao. N1 bổ sung cầu nối từ lợi nhuận đến CFO và các biến vốn lưu động để trả lời: dòng tiền yếu đi có liên quan tăng phải thu, tăng tồn kho, thay đổi phải trả hay các điều chỉnh khác?

Ví dụ giả định: doanh nghiệp có LNST dương, CFO thấp, vẫn công bố cổ tức. Người xem cần thấy khoản tăng phải thu và dòng điều chỉnh tương ứng, cùng trang nguồn. Đây là giải thích theo báo cáo, chưa chứng minh khách hàng mất khả năng trả nợ hoặc công ty quản trị lợi nhuận.

## Câu hỏi nghiên cứu

- Có thể chuẩn hóa các dòng cầu nối CFO và ghi nhận phần chưa giải thích với nguồn truy vết không?
- Phân tích chi tiết có làm ba case BCTC–cổ tức dễ kiểm chứng hơn so với chỉ hiển thị CFO/LNST không?
- Chỉ khi mẫu đủ: thay đổi vốn lưu động có thêm thông tin so với sáu chỉ tiêu lõi trong cùng protocol đánh giá ngoài mẫu không?

Nguồn IAS 7 và nghiên cứu liên quan chất lượng lợi nhuận ở [sổ tài liệu](../02-tai-lieu-va-co-so-lua-chon.md). B01/B02 cho thấy có công trình liên quan; không mặc nhiên biến một tỷ số đơn giản thành thước đo đầy đủ chất lượng lợi nhuận.

## Phương án triển khai

Giữ pipeline hiện hành. Chọn tối đa ba case thuộc phân tích đã có, ưu tiên báo cáo CFO gián tiếp và các dòng vốn lưu động đủ rõ. Trích thêm thủ công có lưu vết trước khi tự động hóa. Tạo bảng cầu nối, chỉ số có điều kiện và biểu đồ kèm phần chưa đối chiếu được.

N1 có thể làm đề tài riêng về khả năng chuyển lợi nhuận thành tiền nếu sau này bỏ cổ tức, nhưng chưa khuyến nghị đổi trọng tâm: khi giữ cổ tức làm ứng dụng, kết quả vẫn nối với câu chuyện hiện hành.

## Quyết định chọn/không chọn

Chọn ở mức case nếu nguồn, dấu và kỳ của dòng CFO đối chiếu được. Không suy ra chi tiết cầu nối từ biến động bảng cân đối đơn thuần. Nếu báo cáo dùng phương pháp trực tiếp hoặc thiếu thuyết minh, trình bày dữ liệu có thật và mức thiếu; không cố dựng cầu nối để đủ hình.

Không yêu cầu cả 30 công ty có thêm các chỉ tiêu. Khi nâng N1 thành tính năng diện rộng, đo lại công sức và cập nhật bộ đặc tả. Giá trị trước mắt là độ sâu và khả năng kiểm chứng của phân tích, không phải tăng số lượng mô hình.
