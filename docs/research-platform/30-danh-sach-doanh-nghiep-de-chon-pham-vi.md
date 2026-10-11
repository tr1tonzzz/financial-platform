# Danh sách doanh nghiệp để lựa chọn phạm vi project

Ngày lập: **11/10/2026**. **Quyết định sau khảo sát: người thực hiện đã chốt HPG/VNM/FPT và PaddleOCR.** [Phạm vi/stack hiện hành](31-chot-pham-vi-va-stack-paddleocr.md). Các phương án bên dưới được giữ làm lịch sử lựa chọn, không còn là mẫu chưa chốt. Lựa chọn dưới đây phục vụ phát triển/kiểm thử UC-F01/02/03/05, không phải đánh giá mức hấp dẫn đầu tư của cổ phiếu.

## 1. Project có giới hạn doanh nghiệp không?

**Có. Phạm vi triển khai và nghiệm thu hiện tại là bộ dữ liệu của một nhóm doanh nghiệp được xác định trước**, không bao phủ toàn thị trường. [SRS v3.3/FR01](22-srs-dac-ta-yeu-cau-phan-mem.md) đặt pilot ba doanh nghiệp × ba năm; tên doanh nghiệp sau đó đã chốt là HPG/VNM/FPT. [Kế hoạch thực hiện](28-ke-hoach-thuc-hien-uc-1-2-3-5.md) và [dữ liệu cần thu](29-du-lieu-can-thu-thap-cho-uc-1-2-3-5.md) dùng FY2023–FY2025.

Giới hạn này là giới hạn dữ liệu được thu, duyệt và kiểm chứng. Định hướng thiết kế là lưu danh sách/nguồn trong cấu hình để thêm doanh nghiệp sau, thay vì viết phép tính riêng cho ba mã. Tuy nhiên, thêm mã chưa có nghĩa tự động trích được báo cáo đúng: vẫn phải xác nhận nguồn, bố cục, phạm vi và kiểm kết quả. Repository hiện chưa có ứng dụng hoàn chỉnh để khẳng định đã làm được việc mở rộng này.

- Người dùng tra cứu/so sánh trong danh sách đã được cung cấp dữ liệu; không mặc định nhập mã bất kỳ là có kết quả.
- Ba doanh nghiệp × ba năm tương ứng chín báo cáo đích và 54 ô lõi, chưa tính ô cổ tức/cầu nối và phiên bản. Năm doanh nghiệp sẽ thành 15 báo cáo/90 ô; tăng mẫu phải dự toán lại thu thập/duyệt.
- Không suy kết quả thử ở vài doanh nghiệp thành khả năng áp dụng toàn thị trường.

## 2. Danh sách ứng viên

Cột “nên dùng” là đề xuất lựa chọn ca nghiên cứu, không phải kết luận đã kiểm đủ dữ liệu lịch sử. Nguồn chính thức đã tìm/đọc ở mức catalog hoặc tài liệu mẫu; chưa tải/xác nhận bộ báo cáo ba năm của tất cả mã.

| Mã | Doanh nghiệp / lĩnh vực | Nên dùng để nghiên cứu gì? | Lợi thế hoặc phần cần kiểm | Nguồn |
|---|---|---|---|---|
| **VNM** | Vinamilk — sữa/thực phẩm | Xu hướng lợi nhuận–CFO; lịch cổ tức theo năm lợi nhuận | Đã có ca quý và notice trong repository; cần bổ sung BCTC năm, kiểm khả năng truy cập catalog | [IR](https://www.vinamilk.com.vn/investor/reports/financial), [notice VSDC](https://vsdc.vn/vi/ad1/197038) |
| **VHC** | Vĩnh Hoàn — thủy sản | Lợi nhuận, CFO và các khoản vốn lưu động; ca báo cáo hợp nhất | Đã có PDF FY2025 và crawler; cần duyệt số/lịch sử cổ tức đủ kỳ | [Nhà đầu tư](https://www.vinhhoan.com/investors/) |
| **HPG** | Hòa Phát — thép/công nghiệp | Biến động lợi nhuận–dòng tiền, CAPEX và cơ sở cổ phiếu | Đã có adapter/PDF; cần kiểm CAPEX và sự kiện vốn thay vì giả định chỉ có cổ tức tiền mặt | [BCTC](https://www.hoaphat.com.vn/quan-he-co-dong/bao-cao-tai-chinh) |
| **DHG** | Dược Hậu Giang — dược phẩm | Cầu nối CFO, tiền sau CAPEX và khoản phân phối chủ sở hữu | Đã có ca tính sâu; báo cáo của ca hiện dùng scope entity, không ghép mặc định với số hợp nhất | [BCTC](https://dhgpharma.com.vn/vi/bao-cao-tai-chinh) |
| **BMP** | Nhựa Bình Minh — vật liệu/ống nhựa | Hồ sơ cổ tức tiền mặt; đối chiếu lợi nhuận, CFO và khoản chi | Có công bố cổ tức và BCTC chính thức; cần kiểm sự thay đổi phạm vi hợp nhất qua các năm | [Công bố](https://binhminhplastic.com.vn/co-dong/cong-bo-thong-tin?year=2025), [BCTN 2025 có BCTC](https://binhminhplastic.com.vn/Data/Sites/1/media/co-dong/bctn/20260414---bmp---bctn-nam-2025-tieng-viet.pdf) |
| **DPM** | Đạm Phú Mỹ — phân bón | Quan hệ lợi nhuận, CFO, CAPEX và phân phối tiền trong doanh nghiệp sản xuất | Có catalog BCTC/ĐHĐCĐ; parser và lịch sử sự kiện chưa thử trong project | [BCTC](https://www.dpm.vn/en/bao-cao-tai-chinh), [nhà đầu tư](https://www.dpm.vn/quan-he-nha-dau-tu) |
| **NT2** | Điện lực Dầu khí Nhơn Trạch 2 — điện | Khấu hao, CFO, nợ vay và khoản chi cổ tức | Có BCTC mẫu chính thức với dòng khấu hao/khoản phân phối; chưa kiểm bộ ba năm | [BCTC 2024 mẫu](https://www.pvpnt2.vn/SharedFiles/Download.aspx?fileid=321), [báo cáo](https://www.pvpnt2.vn/tong-ket-va-bao-cao) |
| **FPT** | FPT — công nghệ/viễn thông/giáo dục | Cổ tức tiền mặt và sự kiện cổ phiếu; basis DPS | Đã có ca quy tắc quyền, chưa có chuỗi basis đủ; cần kiểm thay đổi phạm vi hợp nhất và tính so sánh lịch sử | [Nhà đầu tư](https://fpt.com/vi/nha-dau-tu), [BCTC trong BCTN 2025](https://fpt.com/-/media/project/fpt-corporation/fpt/ir/information-disclosures/year-report/2026/april/bctn-2025.pdf) |
| **REE** | Cơ Điện Lạnh — cơ điện, điện/nước và các hoạt động khác | Phân tích tập đoàn có nhiều hoạt động; phân biệt tiền cấp tập đoàn và khả năng phân phối | Có catalog riêng công ty mẹ/hợp nhất; cần thêm công sức phân biệt chủ thể và lợi nhuận từ đơn vị liên kết | [BCTC](https://www.reecorp.com/danh-muc-bao-cao/bao-cao-tai-chinh/page/2/) |

Không xếp mức cổ tức, tỷ suất hoặc tính ổn định của cổ tức khi chưa kiểm lịch sử. Không chọn toàn bộ chín mã chỉ vì có nguồn công khai.

## 3. Các phương án để người thực hiện chọn

| Phương án | Nhóm đề xuất | Phù hợp khi | Điều kiện |
|---|---|---|---|
| **A — Tận dụng thực nghiệm hiện có** | **VNM, VHC, HPG** | Muốn nhanh có bộ ba cho nền dữ liệu, phân tích và so sánh; tiếp tục mẫu đã nghiên cứu | Ưu tiên hợp nhất; xác nhận đủ báo cáo 2023–2025 và ledger cổ tức. DHG làm ca bổ trợ nếu cần G02/cầu nối, ghi rõ ngoài mẫu so sánh chính |
| **B — Tập trung hồ sơ cổ tức tiền mặt** | **VNM, BMP, DHG** | Muốn ưu tiên UC-5 và tận dụng ca DHG | Kiểm đầy đủ nguồn từng năm và thống nhất chính sách scope. Có thể phân tích từng công ty nhưng không ghép scope khác nhau như một so sánh tương thích. BMP cần kiểm tính nhất quán phạm vi qua năm |
| **C — Thêm ca thay đổi cơ sở cổ phiếu** | **VNM, VHC, FPT** | Muốn đầu tư công sức vào F05.4/G03 | Cần ledger vốn/ngày hiệu lực và phạm vi hợp nhất; nguồn có thật mới điều chỉnh DPS. Không mặc định FPT là ca dễ hơn HPG |

**Đề xuất bắt đầu bằng A** vì giảm việc làm lại nguồn/fixture, không phải vì ba cổ phiếu tốt hơn. Nếu trọng tâm thầy yêu cầu nghiêng mạnh về hồ sơ cổ tức tiền mặt thì chọn B sau khi kiểm scope. DPM/NT2/REE là ứng viên thay thế/mở rộng, không bắt buộc thu ngay.

Ba mã khác ngành vẫn dùng được để đặt số và tỷ số cạnh nhau, nhưng không tạo benchmark ngành hoặc suy công ty tốt hơn từ một tỷ số. Nếu mục tiêu chính là so sánh đối thủ cùng ngành, cần lựa chọn mẫu khác theo ngành và kiểm nguồn cho mẫu đó; các nhóm A/B/C chưa đáp ứng mục tiêu này.

## 4. Điều kiện chốt một mã vào phạm vi

1. Có báo cáo năm 2023–2025 xác nhận đúng kỳ, chủ thể, phạm vi và mức kiểm toán; chỉ tìm thấy catalog chưa đủ.
2. Có thể xác nhận sáu trường lõi và giữ nguồn từng ô, kể cả trạng thái thiếu có lý do.
3. Với UC-5, có nguồn để tra cứu lịch sử cổ tức theo năm lợi nhuận và sự kiện vốn cần thiết; không tìm thấy thông báo không được chuyển thành 0.
4. Chọn ca có dữ liệu phục vụ câu hỏi phân tích cụ thể, không chỉ chọn tên doanh nghiệp quen thuộc.
5. Ghi rõ nhóm so sánh chính/ca bổ trợ. Ca bổ trợ thêm một mã vẫn có công sức riêng, không gọi dữ liệu của nó là ngoài phạm vi để bỏ qua kiểm duyệt.

Sau khi người thực hiện chọn, cập nhật manifest/SRS nếu số doanh nghiệp hoặc điều kiện pilot thay đổi; lập danh sách PDF và notice cần thu cho đúng các mã đó. Sau khi lập danh sách, người thực hiện đã chốt HPG/VNM/FPT; xem tài liệu 31 và manifest hiện hành. Các phương án A/B/C không tự thay quyết định này.
