# Thiết kế tổng quan 5 UC

Ngày 11/10/2026. [Bản xem tương tác](index.html), [bộ 10 SVG](man-hinh-5-uc-svg.zip), [manifest](manifest.json).

**Trạng thái:** đã hoàn thành bản thiết kế local. Tệp Figma `GbpKDOPNhXuCYC2X2Yt7sa` đã được tạo nhưng công cụ báo hết hạn mức Starter trước khi ghi màn hình; canvas vẫn trống. Không coi tệp trống là thiết kế đã hoàn tất trong Figma.

## Cách xem và nhập Figma

Mở index.html, chọn một trong 10 màn hình hoặc bấm mục bên trái/các nút dẫn tới chi tiết. Đây là prototype điều hướng; bộ chọn, duyệt, lưu và xuất chưa xử lý dữ liệu thật. Bảng tiền dùng tỷ đồng; DPS dùng đồng/cổ phiếu. **Tất cả số liệu, lịch công bố và bố cục tài liệu đều là giả định minh họa**, không là số tài chính doanh nghiệp đã đối chiếu.

Giải nén bộ SVG, kéo các tệp vào Figma Design. Các màn hình chứa text/shape/path chỉnh sửa được, không là ảnh chụp toàn giao diện. Dùng font Be Vietnam Pro đã được xác nhận có trong Figma. SVG nhập vào không tự thành auto-layout/components; bước tiếp theo là tổ chức các lớp, liên kết prototype và chuyển phần dùng chung sang components/tokens. Không import ảnh PNG của toàn màn hình để thay lớp chỉnh sửa.

## Danh mục màn hình

| Màn hình | Vai trò | UC nhỏ |
|---|---|---|
| [UC-1 · Khai thác dữ liệu](uc1.svg) | Bảng nhiều kỳ, bộ chọn, độ đầy đủ, nguồn và xuất | F01.1, F01.2, F01.3, F01.4, F01.5, F01.6 |
| [UC-2 · Phân tích tài chính](uc2.svg) | Biểu đồ LNST–CFO, tỷ số có điều kiện và nhận xét | F02.1, F02.4, F02.5, F02.8 |
| [UC-3 · So sánh doanh nghiệp](uc3.svg) | So nhóm tự chọn; giải thích khác ngành | F03.1, F03.2 |
| [UC-4 · Theo dõi doanh nghiệp](uc4.svg) | Danh sách quan tâm, công bố, phiên bản và lịch sự kiện | F04.1, F04.2, F04.3, F04.4, F04.5 |
| [UC-5 · Phân tích cổ tức](uc5.svg) | DPS/năm lợi nhuận, coverage, lịch trả và bối cảnh tiền | F05.1, F05.2, F05.3, F05.4, F05.5, F05.6 |
| [Chi tiết · Nguồn và định nghĩa](source.svg) | Một ô về định nghĩa và đúng dòng/cột/trang nguồn | F01.4, F01.5 |
| [Chi tiết · Duyệt và tra soát](review.svg) | Vai trò vận hành: đối chiếu, duyệt/sửa và giữ audit | F01.6 |
| [Chi tiết · Cầu nối CFO](bridge.svg) | Cầu nối CFO, khoản đóng góp và residual | F02.5 |
| [Chi tiết · Cơ sở DPS](basis.svg) | Giữ DPS gốc, chặn điều chỉnh khi thiếu cơ sở | F05.4, F05.5 |
| [Chi tiết · Hồ sơ phân tích](saved.svg) | Giữ bối cảnh, bằng chứng, nhận xét/câu hỏi | F02.8, F05.6 |

## Những quyết định thể hiện trên giao diện

- Năm, hợp nhất/riêng lẻ, unit và tình trạng dữ liệu hiện rõ; thiếu khác 0.
- UC-1 phục vụ khai thác dữ liệu; duyệt/trích là màn hình hỗ trợ vận hành.
- Biểu đồ thuộc UC-2/3/5, không thành một UC độc lập. Chưa đưa DuPont/quý/định giá vào lát cắt đầu.
- So sánh HPG/VNM/FPT là nhóm tự chọn khác ngành; không xếp hạng, sàng lọc hoặc cảnh báo tiêu chí.
- Lịch thanh toán chưa là xác nhận thực trả; năm lợi nhuận khác năm công bố.
- DPS gốc/điều chỉnh và tiền thực chi trên BCLCTT tách riêng. Thiếu basis/coverage chặn tăng trưởng/payout.
- Hồ sơ lưu giữ số nguồn và version đã dùng; dữ liệu mới không tự sửa nhận xét cũ.
- UC-4 được vẽ để thấy sản phẩm tổng thể, vẫn triển khai sau UC-1/2/3/5.

Thiết kế này không bổ sung nghĩa vụ SRS chỉ vì có màn hình. Các mục F04, giao diện hồ sơ và tương tác biểu đồ là đề xuất/lát cắt đã ghi ở danh mục; chưa triển khai hoặc nghiệm thu. Đối chiếu với [yêu cầu chức năng](../research-platform/27-yeu-cau-chuc-nang-va-vi-du.md), [stack](../research-platform/31-chot-pham-vi-va-stack-paddleocr.md) và [kế hoạch](../research-platform/32-ke-hoach-10-tuan-tiep-theo.md).
