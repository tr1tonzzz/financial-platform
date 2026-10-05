# N2 — Mô phỏng sức chịu đựng khi duy trì cổ tức

Đề xuất sau lõi dữ liệu; chưa triển khai. [Tài chính](02-kien-thuc-tai-chinh.md), [IT](03-ky-thuat-it.md), [protocol](04-du-lieu-thi-nghiem-danh-gia.md).

## Bài toán

Thay vì chỉ hỏi doanh nghiệp có tín hiệu rủi ro hay không, N2 hỏi: nếu tiền từ kinh doanh giảm, doanh nghiệp vẫn đầu tư và trả nợ gốc, việc giữ mức cổ tức sẽ làm tiền cuối kỳ thay đổi thế nào? Đầu ra là bảng kịch bản và điều kiện thiếu hụt tiền theo giả định.

Ví dụ giả định: người dùng giữ một khoản chi cổ tức đã nêu, nhập ba mức giảm CFO và quan sát tiền cuối năm/so với mức dự trữ giả định. Mỗi đầu vào phân biệt số lịch sử có nguồn với giả định tương lai. Không gọi kịch bản này là dự báo xác suất doanh nghiệp cắt cổ tức.

## Câu hỏi nghiên cứu

- Có thể tạo phép tính dòng tiền kịch bản có nguồn, không đếm hai lần các khoản chi không?
- Tiền còn lại nhạy nhất với giả định nào: CFO, CapEx, trả nợ gốc hay cổ tức?
- Đầu vào nào có thể lấy từ báo cáo, đầu vào nào phải ghi là giả định và điều đó giới hạn kết luận ra sao?

Nguồn đọc về quyết định cổ tức/FCFE tại [sổ nguồn B03](../02-tai-lieu-va-co-so-lua-chon.md). Cân đối tiền trong N2 là thiết kế riêng; không tuyên bố sao chép hay kiểm chứng mô hình của Damodaran.

## Giá trị và phụ thuộc

Hướng này làm câu chuyện cổ tức dễ trình bày và có khả năng tương tác rõ. Tuy nhiên sáu chỉ tiêu lõi chưa đủ: cần nguồn cho dòng đầu tư, tài trợ, khoản chi cổ tức và phạm vi tiền có thể sử dụng. Giả định sai có thể tạo kết quả rất chính xác về số học nhưng sai về ý nghĩa.

N2 phù hợp một case đọc kỹ sau khi pipeline và phân tích lõi hoàn thành. Bắt đầu ở cấp năm; lịch trong năm chỉ nghiên cứu khi có thời điểm dòng tiền và nghĩa vụ đến hạn, không chia số năm cho 12 để giả làm dự báo tháng.

## Quyết định

Chưa chọn N2 làm yêu cầu MVP. Chỉ làm nếu case có đủ dữ liệu và còn công sức đã đo, hoặc thay một phần mở rộng khác. Không cần ML/LLM; phép tính xác định, lưu phiên bản giả định và nguồn là đủ cho bản đầu.

Không đánh giá tính hợp pháp của mức chi trả, không suy tiền cuối năm dương thành chắc chắn thanh toán đúng mọi ngày trong năm. Tính mới cần chứng minh bằng quy trình kiểm chứng kịch bản, không bằng việc thêm thanh trượt vào dashboard.
