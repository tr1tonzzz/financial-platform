# Kỹ thuật IT: cập nhật BCTC và giữ lịch sử

> **Trạng thái 03/10/2026 — hồ sơ thử nghiệm thu thập.** Project hiện hành tập trung thu thập, kiểm định và phân tích lợi nhuận–dòng tiền–cổ tức tiền mặt. Xem [SRS hiện hành](../research-platform/02-de-tai-va-srs.md) và [phương pháp thống nhất](../research-platform/11-phuong-phap-thu-thap-va-xu-ly.md). Các ngưỡng cảnh báo, dự báo, scope và lịch cũ bên dưới chỉ để tham khảo; không là yêu cầu MVP hiện hành.

## 1. Tính mới cần được định nghĩa

Hệ thống kiểm tra nguồn theo lịch và xử lý tài liệu mới công bố, không có dữ liệu trước khi doanh nghiệp công bố. Bốn thời điểm khác nhau: `period_end`, `published_at`, `first_seen_at`, `retrieved_at/checked_at`. `Last-Modified` là header sửa tài nguyên trên máy chủ; không tự thay ngày công bố. Tài liệu không có bằng chứng công bố giữ null và lưu first_seen để mô tả thời điểm hệ thống phát hiện.

Độ trễ phát hiện = first_seen − published_at chỉ tính khi biết published_at có độ chính xác tương ứng. Danh mục chỉ có ngày thì không báo độ trễ chính xác đến phút. Chưa đo được độ trễ lịch sử qua hai lần chạy cùng ngày.

## 2. Conditional GET đã được thử

Lần đầu tải PDF: lưu ETag/Last-Modified, SHA-256, byte count, đường dẫn raw. Lần sau kiểm tra lại hash file local trước khi gửi `If-None-Match`, hoặc `If-Modified-Since` khi không có ETag. [HTTP Semantics, RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#name-conditional-requests) là nguồn kỹ thuật cho conditional request và 304.

Ở hai lần chạy cuối: tám PDF lần đầu trả 200; lần sau tám file trả **304 Not Modified**, zero byte PDF body. Danh mục vẫn được fetch trực tiếp ở lần sau. Đây là kiểm tra nguồn thật, khác việc thấy file local rồi bỏ qua mạng.

Nếu máy chủ trả 200, vẫn hash nội dung: cùng hash → không tạo phiên bản mới; khác hash → giữ file cũ, thêm phiên bản mới. Không xem ETag là SHA-256 hoặc coi ETag chứng minh số tài chính đúng. Máy chủ có thể không hỗ trợ conditional request tốt; cần policy kiểm tra lại toàn nội dung định kỳ nếu thấy vấn đề, không tự tuyên bố mọi thay đổi đều phát hiện được.

## 3. Khóa tài liệu và khóa quan sát

Prototype lưu raw theo `pdf/<sha256>.pdf`, history theo URL và chuỗi phiên bản nội dung. Cùng URL đổi bytes được giữ thành phiên bản; cùng bytes không ghi lại file. Kiểm thử offline ba lần: file ban đầu → 304 → file khác nội dung, xác nhận history có hai phiên bản. **Chưa quan sát một BCTC thật đổi nội dung trong thời gian chạy**, không đưa kiểm thử fixture vào thống kê thay đổi thật.

MVP cần tách:

- URL nguồn và các lần kiểm tra HTTP.
- Blob nội dung, hash và đường dẫn bất biến.
- Document metadata: issuer, loại tài liệu, kỳ, scope, assurance, ngôn ngữ, supersedes nếu xác nhận.
- Financial fact: metric, kỳ hiện tại/so sánh, đơn vị, giá trị, document version và locator.
- Snapshot phân tích: danh sách fact version, công thức, config và thời điểm tạo.

Không dedup theo mỗi `company + year`: báo cáo riêng, hợp nhất, quý, bán niên và bản điều chỉnh có thể cùng năm. Hai URL cùng hash là cùng blob nhưng vẫn giữ hai source references. Bản VN/EN có hash khác không được tính là hai quan sát doanh nghiệp–kỳ.

## 4. Bản đính chính và review

Phát hiện file mới khác tên không tự chứng minh nó thay thế bản cũ. Adapter/metadata reviewer xác nhận quan hệ dựa vào tiêu đề/nội dung; giữ `supersedes_document_id` và lý do. Bản không đổi về tên nhưng đổi bytes phải đưa các fact cũ về trạng thái cần kiểm tra trong snapshot cập nhật, không xóa snapshot đã xuất trước.

Với số so sánh trình bày lại, giữ phiên bản fact và nguồn báo cáo mới. UI cho biết đang xem “số theo tài liệu đã công bố lúc đó” hay “số so sánh được trình bày lại”; không trộn âm thầm hai cách trong một biểu đồ.

## 5. Lịch cập nhật đề xuất

Khi có MVP ổn định: kiểm tra các danh mục được phép mỗi ngày hoặc vài ngày, tùy tần suất nguồn; ưu tiên danh sách công ty đã đăng ký. Chỉ tải nội dung khi mới/đổi, và retry hữu hạn rồi ghi failure để lần sau xử lý. Đây là thiết kế cho collector, **chưa tạo automation hay lịch chạy thật**.

Source policy kiểm tra lại theo chu kỳ và khi host thay đổi. Robots parser của prototype hỗ trợ nhóm wildcard/named, wildcard path, dấu `$`, longest literal match và Crawl-delay theo cách bảo thủ; **chưa đầy đủ chuẩn RFC 9309** về mọi trường hợp encoding/group. Với production, dùng parser/framework được kiểm tra hoặc mở rộng test chuẩn; không ghi là tuân thủ đầy đủ chỉ vì đọc robots.txt. [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html) cũng phân biệt robots với cơ chế cấp quyền truy cập.

`history.json` hiện phục vụ nghiên cứu đơn tiến trình; chưa có SQLite transaction, lock đa tiến trình, scheduler hay recovery khi crash giữa cập nhật manifests. PDF được ghi bằng file tạm rồi replace; tính bền vững của toàn collector vẫn cần triển khai trong ứng dụng.
