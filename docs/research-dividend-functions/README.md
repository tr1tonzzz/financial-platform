# Nghiên cứu triển khai chức năng hỗ trợ thẩm định cổ tức

**Lịch sử nghiên cứu trước CR-AN-03:** phần sàng lọc/criteria/pass-fail-unknown G01 và BUC04 cũ đã loại theo yêu cầu người thực hiện ngày11/10/2026. Chỉ kế thừa lưu nhận xét/câu hỏi/bằng chứng và snapshot. [SRS v3.3/mục18](../research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md) và [danh mục UC v2.0](../research-platform/27-yeu-cau-chuc-nang-va-vi-du.md) là nguồn hiện hành; prototype cũ giữ làm bằng chứng lịch sử.

Ngày 11/10/2026; bổ sung theo góp ý giảng viên. Ba chức năng được hiểu theo kết luận nghiên cứu trước: **G02 — bao phủ chi đầu tư và phân phối bằng dòng tiền; G03 — lịch sử cổ tức trên cơ sở cổ phiếu so sánh được; G01 — sàng lọc và hồ sơ thẩm định có giải thích**.

Kết luận: cả ba khả thi ở quy mô pilot có dữ liệu được duyệt. G02 nên làm một ca trước; G03 cần giới hạn loại sự kiện; G01 có thể bắt đầu bằng sáu chỉ tiêu hiện hữu và nhận thêm kết quả G02/G03 khi đủ dữ liệu. Nút thắt là xác nhận ý nghĩa, phạm vi, thời điểm và độ đầy đủ của dữ liệu, hơn là phép tính. Chưa đủ bằng chứng để cam kết tự động toàn thị trường hoặc cải thiện lợi nhuận đầu tư.

| Tài liệu | Dùng để làm gì |
|---|---|
| [01 — UC lớn và phân rã](01-uc-lon-va-phan-ra.md) | Cấu trúc chức năng, tác nhân, luồng và ánh xạ yêu cầu cũ/mới |
| [02 — G02: bao phủ tiền mặt](02-g02-bao-phu-tien-mat.md) | Định nghĩa, hợp đồng dữ liệu, thiết kế và ca DHG thật |
| [03 — G03: lịch sử và cơ sở cổ phiếu](03-g03-lich-su-va-co-so-co-phieu.md) | Luận chứng cổ tức cổ phiếu, loại sự kiện, ca FPT và giới hạn |
| [04 — G01: sàng lọc và thẩm định](04-g01-sang-loc-va-ho-so.md) | Bộ tiêu chí, logic ba trạng thái, hồ sơ công việc và đánh giá ích lợi |
| [05 — Thiết kế, khả thi và kế hoạch](05-thiet-ke-kha-thi-va-ke-hoach.md) | Lược đồ, giao diện xử lý, phụ thuộc, công sức và thứ tự triển khai |
| [06 — Nghiên cứu GitHub bổ sung](06-github-bo-sung-va-y-tuong.md) | Thêm ba repository, bằng chứng code và ý tưởng áp dụng ở Việt Nam |
| [07 — Minh chứng và protocol](07-minh-chung-va-protocol.md) | Phân biệt thực nghiệm đã chạy với nghiệm thu còn thiếu |
| [Nguồn](sources.md) | Commit, nguồn Việt Nam và đường tới các snapshot để tra soát |

Yêu cầu chính thức để triển khai nằm trong [SRS v3.2 dự thảo](../research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md), mục 3/5/16/17. Bản 3.2 đổi cấu trúc UC và thêm CR-DIV-02; không sửa nghĩa các mã FR01–FR38, BR01–BR12 hay E01–E10 đã có. D01–D12 là yêu cầu bổ sung theo ca pilot được chọn, chưa được giảng viên phê duyệt và chưa nghiệm thu ứng dụng. Kế hoạch 167 giờ trước đây vẫn là dự toán baseline; giờ mới được ghi riêng.

**Đã thực hiện:** đọc tĩnh code ở commit cố định; kiểm trang BCLCTT DHG; đối chiếu thông báo FPT; chạy prototype tính và kiểm quy tắc độc lập. **Chưa thực hiện:** tích hợp vào ứng dụng, thu tự động các trường mới, duyệt độc lập bộ gold, kiểm thử người dùng và đo hiệu quả đầu tư. Không chạy hoặc cài đặt các dự án GitHub khảo sát.

Các bộ nghiên cứu liên quan: [GitHub đợt trước](../research-github-dividend/README.md), [cầu nối lợi nhuận–CFO](../research-profit-cash-dividend/README.md), [kế hoạch theo góp ý](../research-platform/26-ke-hoach-nghien-cuu-sau-gop-y-giang-vien.md).
