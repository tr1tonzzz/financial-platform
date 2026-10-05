# Quyết định chọn ngách BCTC và cổ tức tiền mặt

**Cập nhật hướng triển khai 05/10/2026:** Xây dựng hệ thống thu thập, chuẩn hóa và phân tích lợi nhuận, dòng tiền kinh doanh trong mối liên hệ với cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam. Lấy lợi nhuận→chuyển thành tiền làm trục, đối chiếu cổ tức; [SRS v3.1](22-srs-dac-ta-yeu-cau-phan-mem.md) tích hợp cầu nối CFO tối thiểu một ca, mục tiêu 1–3 sau gate. Giữ pilot/sáu trường; chưa ghi nhận phê duyệt giảng viên. Các quyết định ngày 03–04/10 bên dưới là bối cảnh trước cập nhật này.

Ngày 03/10/2026, người thực hiện chọn **hệ thống thu thập và phân tích mối quan hệ giữa lợi nhuận, dòng tiền và cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam**.

## Vì sao chọn

Ưu tiên hiện tại là một câu hỏi nghiệp vụ rõ và hệ thống dữ liệu kiểm chứng được. Lợi nhuận–dòng tiền–cổ tức cho câu hỏi cụ thể, tận dụng nguồn/crawler đã nghiên cứu và tạo bài toán ghép tài liệu với sự kiện. A1 sức khỏe tài chính từng được ưu tiên vì an toàn về dữ liệu, nhưng phạm vi phân tích rộng hơn nhu cầu này. [Nghiên cứu lần hai ngày 04/10/2026](20-nghien-cuu-lan-hai-va-chot-de-tai.md) xác nhận giữ tên/phạm vi và chọn đối chiếu phiên bản/ảnh hưởng làm hướng đồ án ưu tiên; dự đoán còn là tùy chọn.

| Tiêu chí | Đánh giá có căn cứ |
|---|---|
| Dữ liệu BCTC | Đã tự tìm/tải nguồn mới; OCR và chuẩn hóa vẫn cần công sức |
| Cổ tức | Có bốn thông báo mẫu; đủ lịch sử và adapter phát hiện tự động còn cần pilot |
| Vừa học vừa làm | Phù hợp khi chỉ phân tích mô tả, sáu trường lõi, 5–8 doanh nghiệp sau gate |
| Đóng góp IT | Collector, PDF/OCR, event lifecycle, schema, validation, UI và thí nghiệm |
| Liên thông tốt nghiệp | Ưu tiên đối chiếu phiên bản và ảnh hưởng tới kết quả; dự đoán chỉ khi đủ dữ liệu, chia thời gian và baseline |

Đây là đánh giá thiết kế, không là điểm số khách quan, xác nhận của hội đồng hoặc kết quả accuracy. Quan hệ tài chính không được tuyên bố là phát minh mới; điểm đáng làm là dữ liệu Việt Nam tự thu thập và pipeline có kiểm chứng.

## Phạm vi chốt

Người thực hiện chọn A2 ở mức thu thập–kiểm định–phân tích. Giữ dữ liệu gốc, sáu chỉ tiêu BCTC, mức cổ tức tiền mặt công bố theo năm lợi nhuận và timeline. Không xây predictor, score rủi ro hay hỏi đáp AI như nghĩa vụ project.

Pilot ba doanh nghiệp × ba năm; sau đo công sức chốt 5–8 doanh nghiệp. Case 2026 là cập nhật riêng, không trộn quý/bán niên vào bảng năm. Tên đăng ký và nghiệm thu cần trao đổi với thầy.

## Quyết định trước và các phương án khác

Bảng chấm A1–A7 trước dựa trên trọng số có chủ đích, không chứng minh A1 luôn tốt hơn. Bản đó đã được lưu trong [snapshot A1](history/a1-2026-10-03.zip). A3 danh mục, A4 cá nhân, A5 SME, A6 hỏi đáp, A7 vĩ mô là phương án khảo sát; người thực hiện đã chọn tập trung A2, nên không đưa chúng vào backlog hiện hành.

[Phương pháp thống nhất](11-phuong-phap-thu-thap-va-xu-ly.md) xử lý rủi ro chính của A2: năm lợi nhuận khác năm thanh toán, không thấy thông báo không bằng 0, scope riêng/hợp nhất khác nhau và thay đổi cơ sở cổ phiếu.
