# Tính khả thi và nguồn BCTC gần hiện tại

> **Trạng thái 03/10/2026 — hồ sơ thử nghiệm thu thập.** Project hiện hành tập trung thu thập, kiểm định và phân tích lợi nhuận–dòng tiền–cổ tức tiền mặt. Xem [SRS hiện hành](../research-platform/02-de-tai-va-srs.md) và [phương pháp thống nhất](../research-platform/11-phuong-phap-thu-thap-va-xu-ly.md). Các ngưỡng cảnh báo, dự báo, scope và lịch cũ bên dưới chỉ để tham khảo; không là yêu cầu MVP hiện hành.

Khảo sát ngày 03/10/2026. Kết quả dưới đây là thực nghiệm của repo, không suy ra từ việc một URL xuất hiện trong kết quả tìm kiếm.

## 1. Dữ liệu gần hiện tại có tồn tại không?

Có. Crawler đọc danh mục chính thức và tải được tám PDF trong bảng. Ngày trên danh mục khác ngày sửa file HTTP; năm nằm trong thư mục upload khác kỳ tài chính.

| Doanh nghiệp | FY2025: trang; ngày trên danh mục | H1/2026: trang; ngày trên danh mục | Mức xác nhận |
|---|---|---|---|
| HPG | 53; 27/03/2026 | 67; 28/08/2026 | Tự tìm link và tải; metadata ứng viên từ từng dòng danh mục |
| DHG | 40; 21/03/2026 | 45; 14/08/2026 | Tự tìm link và tải; scope chưa được classifier xác nhận từ tiêu đề |
| VHC | 64; không thấy ngày công bố trong anchor/context đã lấy | 65; tương tự | Tự tìm link và tải; không thay publication_date bằng Last-Modified |
| HPA | 41; 25/03/2026 | 48; 28/08/2026 | Tự tìm/tải; đã đọc ảnh trang 1 xác nhận hợp nhất, năm 2025 kiểm toán và kỳ 6 tháng kết thúc 30/06/2026 soát xét |

Danh mục chính thức: [HPG](https://www.hoaphat.com.vn/quan-he-co-dong/bao-cao-tai-chinh), [DHG](https://dhgpharma.com.vn/vi/bao-cao-tai-chinh), [VHC](https://www.vinhhoan.com/investors-2/), [HPA](https://nongnghiep.hoaphat.com.vn/quan-he-co-dong/bao-cao-tai-chinh). Hash và URL từng PDF nằm trong [bằng chứng](crawl-evidence.json).

Năm tài chính 2026 chưa kết thúc tại ngày khảo sát nên không lấy “BCTC năm 2026 kiểm toán” làm mục tiêu hiện tại. Chưa kiểm tra hay chứng minh BCTC quý III/2026 đã được công bố. Dữ liệu mới phải gắn với **kỳ đã kết thúc và tài liệu đã công bố**, không chỉ chọn nhãn năm lớn nhất.

## 2. Ưu tiên các loại nguồn

| Nguồn | Dùng cho việc gì? | Kết luận ở thời điểm khảo sát |
|---|---|---|
| IR doanh nghiệp | Nguồn chính của PDF và tiêu đề/ngày công bố | Bốn nguồn đã thử end-to-end; dễ bắt đầu nhất |
| HNX/công bố của sở | Đối chiếu, bổ sung doanh nghiệp không có IR ổn định | Khảo sát trước đã tải được một PDF VHE bằng curl Schannel với TLS xác thực; chưa tích hợp vào crawler mới |
| HOSE | Nguồn có tiềm năng để bổ sung | Chưa có thực nghiệm thành công trong bộ này; không đánh dấu sẵn là adapter hoạt động |
| Website dữ liệu/API bên thứ ba | Đối chiếu hoặc nâng cấp nếu có quyền sử dụng | Không là điều kiện để hoàn thành MVP; chưa đo độ phủ/độ trễ hay cam kết miễn phí |
| Dataset tĩnh | Bài tập học/đối chiếu phương pháp | Không thay nguồn dữ liệu chạy demo tự thu thập |

Một seed danh mục IR là cấu hình nguồn; không phải dataset chứa sẵn số tài chính. Crawler cũng chưa tự tìm mọi doanh nghiệp trên Internet: danh sách issuer và URL danh mục được người phát triển chọn, link PDF do chương trình phát hiện.

## 3. Chính sách nguồn và khả năng tải

Không đồng nhất “HTTP 200” với chính sách cho phép khai thác hay quyền phân phối lại tài liệu. Prototype kiểm tra robots, chỉ vào host HTTPS đã khai báo, giữ TLS xác thực và không theo redirect chưa kiểm tra.

DHG/VHC: đọc được robots và đường dẫn mẫu không bị chặn theo parser pilot. HPG/HPA: robots danh mục đọc được nhưng robots host file trả 403; bốn PDF thử tải bằng cờ rõ ràng `--allow-unknown-robots`, có trạng thái `unknown_policy_probe`. Cờ này không ghi đè Disallow đã đọc. Với collector dùng thường xuyên, ưu tiên nguồn có chính sách rõ hoặc xác minh nguồn trước khi bật lịch chạy.

REE từng có Disallow cho PDF; FPT có đường tải `/api/` bị chặn theo khảo sát trước, nên không dùng việc thay User-Agent, proxy hoặc gọi API bị chặn để đạt chỉ tiêu. Xem [khảo sát cũ](../research-recent-data/README.md) để tách kết quả trước và sau; tám PDF mới không cộng thành tám doanh nghiệp mới.

## 4. Phạm vi khả thi

Khả thi cao: danh sách doanh nghiệp nhỏ, cập nhật theo lịch công bố, xử lý PDF hữu hạn, xác nhận metadata và duyệt số khi cần. Khả thi có điều kiện: mở rộng 5–10 doanh nghiệp cần đo số adapter, layout, phút review. Chưa có cơ sở: toàn bộ thị trường, mọi quý, số liệu đúng hoàn toàn tự động, cập nhật tức thời hoặc crawler không bao giờ phải sửa khi website thay đổi.
