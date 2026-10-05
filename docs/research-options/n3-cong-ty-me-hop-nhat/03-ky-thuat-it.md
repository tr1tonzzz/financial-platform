# N3 — Kỹ thuật IT cho đối chiếu hai phạm vi

Thiết kế đề xuất. [Tài chính](02-kien-thuc-tai-chinh.md), [thí nghiệm](04-du-lieu-thi-nghiem-danh-gia.md).

## 1. Nhận diện thực thể và khóa dữ liệu

Tách `issuer_id`, `reporting_entity_id` và `group_id` khi cần. Document ghi phạm vi `consolidated/separate/unknown`, kỳ, chuẩn mực, ngày công bố và phiên bản. Khóa facts bao gồm phạm vi, thực thể, kỳ, metric và nguồn; không dùng chỉ mã cổ phiếu–năm–metric vì sẽ ghi đè hai báo cáo.

Trạng thái `unknown` không tự chuyển thành hợp nhất chỉ vì document chứa tên tập đoàn. Ghi evidence nhận diện phạm vi từ tiêu đề/báo cáo kiểm toán; review khi tiêu đề và nội dung mâu thuẫn.

## 2. Ghép cặp có điều kiện

Tạo `report_pair` có hai document, tiêu chí kỳ/ngày kết thúc, chuẩn mực, đơn vị đã đổi và version policy. Không ghép báo cáo kiểm toán năm này với bản chưa kiểm toán/khác kỳ rồi gọi cùng cơ sở. Cặp thiếu báo cáo riêng trả `unpaired`, không clone số hợp nhất.

Mỗi phép so chỉ lấy facts đã duyệt từ đúng cặp; không dùng báo cáo riêng làm fallback cho một metric còn thiếu trong bảng hợp nhất. Việc đổi đơn vị không đủ để sửa khác biệt phạm vi hoặc chuẩn mực.

## 3. Evidence thuyết minh

Lưu `note_evidence` với loại: cổ tức nhận, khoản đầu tư, hạn chế sử dụng tiền, hạn chế chuyển tiền hoặc loại khác; gồm đoạn nguyên gốc ngắn, trang/vị trí, entity được nhắc, thời điểm áp dụng và trạng thái reviewer. Trích snippet ngắn đủ làm căn cứ; lưu raw gốc để đọc trong ngữ cảnh.

Từ khóa giúp tìm ứng viên, nhưng không dùng từ “hạn chế” đơn lẻ để gán một quan hệ tài chính. Ban đầu dùng review thủ công và full text search. Chưa cần graph database; bảng quan hệ có evidence đủ cho một case.

## 4. Trình bày và tái lập

UI hai cột riêng/hợp nhất, màu/nhãn phạm vi rõ; biểu đồ không cộng gộp. Mỗi kết luận có links đến facts và thuyết minh. Export cặp tài liệu, nguồn, phiên bản mapping và tiêu chí ghép.

Kiểm tra cần có khi triển khai: nhầm pháp nhân, ghép sai kỳ, thiếu phạm vi, ghi đè, fallback trộn hai báo cáo và suy nhãn hạn chế không có đoạn nguồn. Khái niệm provenance tham khảo [W3C PROV-DM](https://www.w3.org/TR/prov-dm/); chưa tuyên bố schema đáp ứng mọi yêu cầu chuẩn.
