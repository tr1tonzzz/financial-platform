# N3 — Dữ liệu và thí nghiệm đối chiếu phạm vi

Protocol đề xuất, chưa chạy. [Đề xuất](01-de-xuat-nghien-cuu.md), [IT](03-ky-thuat-it.md).

## 1. Chọn case

Tìm trong pilot một công ty phát hành có cả báo cáo riêng và hợp nhất kiểm toán cùng kỳ, công bố cổ tức và thuyết minh có thể đọc. Chọn theo tiêu chí nguồn trước, không chọn chỉ vì chênh lệch tiền lớn. Ghi mọi case đã xem và lý do loại để tránh trình bày case hiếm như tình trạng phổ biến.

Một cặp báo cáo không đủ suy rộng toàn thị trường. Nếu nguồn đủ và công sức cho phép, thêm một năm trước để xem sự khác biệt có nhất quán hay chỉ thời điểm.

## 2. Dữ liệu đối chiếu

Gold gồm entity/phạm vi, sáu chỉ tiêu tại cả hai báo cáo, lợi nhuận thuộc công ty mẹ nếu có, cổ tức nhận được công bố, bằng chứng hạn chế và sự kiện cổ tức của issuer. Mỗi số/đoạn có đơn vị, kỳ, trang và ngày khả dụng xác minh được.

Giữ nhãn ba trạng thái cho hạn chế: được công bố có; được công bố không trong phạm vi thông tin cụ thể; chưa xác định. Không gán “không” chỉ vì keyword search không tìm thấy. Không biến tiền trả cổ tức tổng hợp của tập đoàn thành số chi của pháp nhân mẹ khi không đủ đối chiếu.

## 3. Thí nghiệm

So sánh cách giải thích từ hợp nhất đơn lẻ với cách giải thích từ cặp báo cáo và notes. Dùng câu hỏi cố định: số tiền nào thuộc issuer? phạm vi của lợi nhuận là gì? có nguồn về chuyển tiền không? đâu là phần chưa biết? Reviewer đánh giá đúng ngữ nghĩa và nguồn, không chấm “hay” bằng độ dài trả lời.

Kiểm tra các lỗi đối chứng: ghép sai năm, đảo phạm vi, clone báo cáo còn thiếu và bỏ evidence hạn chế. Đo tỷ lệ nhận diện đúng entity/phạm vi, số phép so đủ điều kiện, lỗi kết luận và phút review. Mọi tỷ lệ phải có số cặp/facts làm mẫu số.

## 4. Tiêu chí ra quyết định

Giữ N3 trong báo cáo nếu cho thấy một kết luận được bổ sung/thu hẹp bằng evidence rõ hoặc một giới hạn quan trọng được phát hiện. Nếu chỉ có hai bảng số nhưng không thêm căn cứ, có thể lưu appendix thay vì làm module chính.

Không tuyên bố đã xác định toàn bộ khả năng phân phối tiền, nguyên nhân cắt cổ tức hay mức cổ tức hợp pháp. Một case không chứng minh ưu thế dự báo của mô hình sử dụng báo cáo riêng.

## 5. Artifact khi triển khai

Manifest cặp báo cáo, gold facts, phiếu notes, bảng so sánh hai phạm vi và bản diễn giải có dẫn nguồn. Ghi báo cáo chưa đọc, giả định và hạn chế. Những artifact này chưa được tạo bởi lượt viết tài liệu; không dùng N3 làm yêu cầu nghiệm thu toàn mẫu.
