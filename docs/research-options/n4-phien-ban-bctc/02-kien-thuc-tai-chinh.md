# N4 — Kiến thức tài chính khi đọc phiên bản báo cáo

[Đề xuất](01-de-xuat-nghien-cuu.md), [protocol](04-du-lieu-thi-nghiem-danh-gia.md).

## 1. Các nguyên nhân khác nhau

Thay đổi số giữa tài liệu có thể đến từ kỳ/phạm vi khác, đơn vị, tái phân loại, chính sách, ước tính, sửa sai hoặc lỗi parser. [IAS 8 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-8-basis-of-preparation-of-financial-statements/) phân biệt thay đổi ước tính với sửa sai, và mô tả sửa sai kỳ trước qua thông tin so sánh khi phù hợp. Đây là tài liệu khái niệm; không gán quy tắc IFRS trực tiếp cho mọi BCTC VAS.

Nhãn đề xuất: `same_value`, `rounding_or_unit`, `presentation_reclassification`, `policy_change_disclosed`, `error_correction_disclosed`, `scope_or_period_mismatch`, `extraction_error`, `unexplained_difference`. Chỉ gán loại có chữ `disclosed` khi có đoạn nguồn; danh mục này là quy ước nghiên cứu, không phải kết luận kiểm toán.

## 2. Điều kiện so sánh số

Hai facts phải cùng thực thể, kỳ, độ dài kỳ với số dòng tiền/lợi nhuận, metric, phạm vi và cơ sở kế toán có thể đối chiếu. Số cuối kỳ khác dòng phát sinh cả kỳ. Đổi đơn vị không xử lý được khác phạm vi riêng/hợp nhất, và cột “năm trước” không luôn giữ nguyên cơ sở của bản đã công bố trước đó.

Cột so sánh năm trước ở báo cáo năm sau là bằng chứng công bố mới cho kỳ cũ. Giữ nó bên cạnh bản gốc; ghi notes về điều chỉnh nếu có. Không mặc định cột so sánh là phiên bản “đúng hơn” khi chưa xác định nguồn và chính sách chọn bản.

## 3. Ba loại thời gian

- Kỳ tài chính: số liệu phản ánh thời đoạn/ngày nào.
- Thời điểm công khai: có bằng chứng người đọc có thể biết tài liệu từ ngày nào.
- Thời điểm hệ thống thu thập/review: hệ thống thực sự lưu hoặc sửa dữ liệu khi nào.

Ngày tải không thay ngày công bố. Không biết ngày công bố thì không đưa vào backtest cần biết tại thời điểm, hoặc dùng một chính sách bảo thủ được định nghĩa trước và báo cáo mẫu loại. Phân tích latest cho tra cứu hiện tại tách khỏi phân tích lịch sử.

## 4. Đo chênh lệch và ảnh hưởng

```text
delta = value_later - value_earlier
relative_delta = delta / abs(value_earlier), chỉ khi value_earlier != 0
```

Giá trị trước bằng 0 thì chỉ báo delta tuyệt đối. Làm tròn theo đơn vị gốc; ngưỡng lọc cảnh báo do nghiên cứu đề xuất không tự là mức trọng yếu kiểm toán. Tính lại chỉ số trên hai bộ số cùng cơ sở và ghi đầu vào; không pha trộn giá trị mới/cũ giữa tử và mẫu mà thiếu chính sách.

Nếu cảnh báo cổ tức đổi vì dữ liệu bổ sung được công bố muộn, chỉ mô tả ảnh hưởng phiên bản; không xem kết quả muộn là chất lượng dự báo tại thời điểm cũ.
