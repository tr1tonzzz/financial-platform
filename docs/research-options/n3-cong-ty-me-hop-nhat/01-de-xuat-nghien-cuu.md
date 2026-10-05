# N3 — Đối chiếu công ty mẹ với số liệu hợp nhất

Đề xuất case chuyên sâu, chưa thực hiện. [Tài chính](02-kien-thuc-tai-chinh.md), [IT](03-ky-thuat-it.md), [đánh giá](04-du-lieu-thi-nghiem-danh-gia.md).

## Bài toán mới

Dashboard thường ưu tiên hợp nhất để phản ánh tập đoàn. N3 thêm câu hỏi: tiền và dòng tiền ở pháp nhân phát hành cổ phiếu khác số hợp nhất ra sao, và tài liệu có cho biết nguồn tiền nhận từ công ty con/hạn chế chuyển tiền hay không?

Ví dụ giả định: tập đoàn có tiền lớn nhưng báo cáo riêng của công ty mẹ có số tiền thấp hơn và ghi nhận khoản cổ tức nhận từ công ty con. Người xem cần đọc cả hai phạm vi trước khi diễn giải nguồn hỗ trợ chi cổ tức của công ty mẹ. Không kết luận phần chênh lệch là tiền bị phong tỏa.

## Câu hỏi nghiên cứu

- Có thể ghép báo cáo riêng/hợp nhất cùng kỳ, chuẩn mực và phiên bản, giữ nguồn độc lập không?
- Case về cổ tức thay đổi cách diễn giải thế nào khi bổ sung dữ liệu công ty mẹ và thuyết minh?
- Hạn chế chuyển tiền được công bố trực tiếp hay chỉ là điều chưa biết?

IAS 27/IFRS 12 tại [sổ nguồn](../02-tai-lieu-va-co-so-lua-chon.md) là gợi ý khái niệm; phải đọc chuẩn mực/chính sách và thuyết minh của báo cáo Việt Nam cụ thể. Không tự khẳng định điều kiện pháp lý chia cổ tức từ chỉ số.

## Giá trị và chi phí

N3 làm sâu ngữ nghĩa tài chính, khắc phục nguy cơ xem toàn bộ tiền hợp nhất là nguồn tiền trực tiếp của bên chi trả. Khó khăn là số lượng tài liệu tăng, thuyết minh cần review, và không có đủ dữ liệu để tái dựng mạng chuyển tiền hoàn chỉnh.

Chỉ làm một case có cặp báo cáo cùng năm và thuyết minh đủ. Không áp mô hình “dòng tiền công ty mẹ” lên toàn mẫu chỉ vì dữ liệu hợp nhất sẵn có. Báo cáo riêng và hợp nhất có thể bắt đầu CFO từ các cấu phần khác nhau; không dùng chênh lệch như một đẳng thức loại trừ đơn giản.

## Quyết định

N3 là hướng đào sâu sau N1 hoặc một chủ đề luận văn tài chính riêng khi có thời gian đọc báo cáo. Chưa chọn làm lõi MVP. Trong phạm vi hiện tại vẫn bắt buộc gắn đúng `statement_scope`; yêu cầu đó không phụ thuộc có triển khai N3 hay không.
