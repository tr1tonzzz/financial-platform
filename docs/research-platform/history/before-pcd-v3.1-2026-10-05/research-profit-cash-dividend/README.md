# Nghiên cứu kết hợp lợi nhuận – dòng tiền kinh doanh – cổ tức tiền mặt

Ngày: **04/10/2026** · Phiên bản: **1.0** · Trạng thái: đề xuất để lựa chọn và trao đổi với giảng viên.

**Tên được nghiên cứu:** “Xây dựng hệ thống thu thập, chuẩn hóa và phân tích lợi nhuận, dòng tiền kinh doanh trong mối liên hệ với cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam.”

**Kết luận: khả thi có điều kiện và nên kết hợp.** Lấy lợi nhuận và khả năng chuyển thành tiền làm trục; cổ tức là lớp đối chiếu chính sách phân phối. Dùng chung một pipeline dữ liệu, bổ sung cầu nối CFO cho một số ca. Không cần xây ba hệ thống độc lập. Với project 13 tuần, giữ pilot 3 doanh nghiệp × 2023–2025, mở lên 5–8 doanh nghiệp sau gate công sức; phân tích cầu nối sâu cho 1–3 ca. Chưa đủ cơ sở cam kết tự động hóa toàn thị trường hay dự báo cổ tức.

## Bộ tài liệu theo workflow

| Thứ tự | Tài liệu | Quyết định/đầu ra |
|---|---|---|
| 1 | [01 — Đề xuất và tính khả thi](01-de-xuat-va-tinh-kha-thi.md) | Có nên kết hợp, giá trị và phạm vi |
| 2 | [02 — Cơ sở nghiên cứu và sổ nguồn](02-co-so-nghien-cuu-va-so-nguon.md) | Bằng chứng, prior art, giới hạn truy cập |
| 3 | [03 — Nghiệp vụ tài chính và từ điển](03-nghiep-vu-va-tu-dien.md) | Chỉ tiêu, công thức, quy tắc ghép |
| 4 | [04 — Nguồn, chuẩn hóa và chất lượng](04-nguon-chuan-hoa-va-chat-luong.md) | Source plan, grain, missing, kiểm soát sai lệch |
| 5 | [05 — Thiết kế và workflow](05-thiet-ke-va-workflow.md) | Luồng nghiên cứu, xử lý, phân tích, schema |
| 6 | [06 — Đặc tả bổ sung và truy vết](06-dac-ta-bo-sung-va-truy-vet.md) | Yêu cầu mới, ánh xạ SRS v3.0, nghiệm thu |
| 7 | [07 — Kế hoạch, thí nghiệm và kiểm thử](07-ke-hoach-thi-nghiem-va-kiem-thu.md) | Lộ trình 13 tuần, gate, đánh giá |
| 8 | [08 — Ca thực tế DHG và VNM](08-ca-thuc-te-dhg-vnm.md) | Chứng minh cách kết hợp bằng nguồn thật |
| 9 | [09 — Đề cương trao đổi với giảng viên](09-de-cuong-trao-doi-voi-giang-vien.md) | Bản trình bày ngắn và các điểm cần chốt |

## Quan hệ với hồ sơ trước

[SRS-FAP-01 v3.0](../research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md) vẫn là baseline triển khai. Hồ sơ này là nghiên cứu bổ sung, chưa thay đổi phê duyệt, kế hoạch hay mẫu số nghiệm thu. Tiếp nối [N1: chuyển lợi nhuận thành tiền](../research-options/n1-loi-nhuan-dong-tien/01-de-xuat-nghien-cuu.md) và [I2: dòng tiền–cổ tức](../research-development/i2-dong-tien-co-tuc/01-de-xuat-nghien-cuu.md), nhưng sử dụng phạm vi hiện hành 3→5–8 doanh nghiệp, không kế thừa quy mô 30–80 doanh nghiệp ở hồ sơ cũ.

Điểm mới của lần nghiên cứu này: chuyển từ ý tưởng kết hợp sang quy tắc cầu nối có residual, phân biệt ba cách ghép cổ tức, ca DHG đối chiếu số thật và yêu cầu/test bổ sung có thể triển khai. Không mặc định đổi tên là tăng chức năng: dashboard ba chuỗi đã nằm trong SRS; cầu nối chi tiết là phần bổ sung có chi phí thực.

## Bằng chứng có thể kiểm tra

- [Dữ liệu chép từ nguồn và phép tính ca DHG](evidence/case-dhg-2025.json).
- [Kết quả kiểm tra số học và liên kết tài liệu](evidence/verification.json).
- [Script tái lập](../../scripts/research/verify_profit_cash_dividend.py): chạy `python scripts/research/verify_profit_cash_dividend.py` từ root dự án.
- Nguồn trực tuyến được kiểm tra trong ngày 04/10/2026; ảnh/PDF DHG tái sử dụng từ kho khảo sát 03/10/2026 và đọc lại trang cần thiết trong lượt này. Chưa chạy lại crawler toàn bộ, chưa có tập kiểm thử độc lập cho extension.

Các sơ đồ là thiết kế đề xuất, không phải chức năng đã vận hành. Tài liệu Markdown là nguồn chỉnh sửa; đọc theo thứ tự 01 → 03 → 05 → 07 nếu muốn nắm nhanh cách làm.
