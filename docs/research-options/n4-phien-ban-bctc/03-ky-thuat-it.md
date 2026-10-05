# N4 — Kỹ thuật IT cho phiên bản và truy vấn theo thời điểm

Thiết kế đề xuất; chưa có benchmark. [Tài chính](02-kien-thuc-tai-chinh.md), [thí nghiệm](04-du-lieu-thi-nghiem-danh-gia.md).

## 1. Lưu bất biến và quan hệ phiên bản

`document` có URL, hash, loại, kỳ, phạm vi, ngày công bố kèm evidence, ngày tải và trạng thái. Cùng URL có hash khác là bản khác; nhiều URL có cùng hash có thể là cùng nội dung nhưng vẫn giữ metadata từng nguồn. Không suy quan hệ sửa đổi chỉ từ tên file.

Facts thô không ghi đè. Lưu `document_id`, vị trí, số gốc, đơn vị, giá trị chuẩn hóa, metric, parser/mapping version và review. Bản sửa parser là lịch sử xử lý, không tự trở thành “doanh nghiệp điều chỉnh báo cáo”. Có quan hệ `supersedes` chỉ khi nguồn hỗ trợ hoặc reviewer xác nhận với lý do.

## 2. Public time và system time

Giữ `available_at` đã xác minh của tài liệu và `ingested_at`/lịch sử review riêng. Truy vấn “thông tin công khai tính đến T” khác “hệ thống đã biết gì tại T”. Báo cáo năm cũ tải hôm nay có thể dùng tái dựng thông tin công khai nếu ngày công bố cũ được xác minh; không được giả rằng hệ thống đã lưu nó từ ngày cũ.

Một sửa lỗi trích xuất hôm nay không sửa metadata ngày công bố tài liệu. Phải biết query đang trả fact đã review mới nhất hay fact đúng trạng thái hệ thống tại thời điểm lịch sử. Trường hợp thiếu ngày công bố không lặng lẽ lấy kỳ kết thúc thay thế.

## 3. Chính sách lựa chọn facts

Cung cấp `public_as_of(T)` và `latest_verified` với version policy công bố rõ. As-of lọc ngày khả dụng trước, sau đó chọn bản theo quan hệ/ưu tiên hợp lệ; không dùng ID lớn nhất làm bằng chứng bản doanh nghiệp mới nhất. Nếu nhiều bản không xác định thứ tự/độ ưu tiên, trả conflict cho reviewer.

Ghi `snapshot_id`, policy version và danh sách facts được chọn. Với đánh giá dự báo, ngày phát hành dữ liệu mới cho kỳ cũ không được đưa vào features tại T cũ. Không dùng latest để lấp trường thiếu trong snapshot lịch sử.

## 4. Engine đối chiếu

Ghép facts theo khóa tương thích, chuẩn hóa đơn vị, so delta/tolerance và đối chiếu notes. Trả cả `comparable=false` với lý do khi khác phạm vi/kỳ. Keyword chỉ tạo ứng viên nhãn, reviewer xác nhận nguyên nhân. UI mở hai trang cạnh nhau, số gốc và số đã đổi đơn vị.

Index theo company/metric/period/scope/available_at là ứng viên tối ưu; đo query thực tế trước khi thêm cache/materialized view. [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) và [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) là nguồn tham khảo kỹ thuật, không chứng minh thiết kế đã đúng hoặc tối ưu.

## 5. Kiểm tra khi triển khai

Các tình huống cần kiểm tra: URL bị thay nội dung, mirror cùng hash, số âm đổi dấu, unit mismatch, công bố muộn, parser được sửa, ngày không biết, phạm vi khác và conflict. Phân biệt kết quả xử lý các fixture tổng hợp với đánh giá trên cặp tài liệu thật.
