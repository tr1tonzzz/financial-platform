# Đặc tả yêu cầu: Phân tích tính bền vững cổ tức tiền mặt Việt Nam

> **Trạng thái 03/10/2026 — hồ sơ khảo sát trước.** Project hiện hành tập trung thu thập, kiểm định và phân tích lợi nhuận–dòng tiền–cổ tức tiền mặt. Xem [SRS hiện hành](../research-platform/02-de-tai-va-srs.md) và [phương pháp thống nhất](../research-platform/11-phuong-phap-thu-thap-va-xu-ly.md). Các ngưỡng cảnh báo, dự báo, scope và lịch cũ bên dưới chỉ để tham khảo; không là yêu cầu MVP hiện hành.

Phiên bản: 2.0 — 03/10/2026. Tên file được giữ để các liên kết vẫn hoạt động; toàn bộ yêu cầu trong bản này thuộc ý tưởng mới.

## 1. Mục đích và câu chuyện thực tế

Một người theo dõi doanh nghiệp có lãi và thường trả cổ tức muốn biết mức chi trả có được dòng tiền hỗ trợ hay không. Để trả lời, họ phải nối BCTC PDF với nhiều thông báo cổ tức, phân biệt kỳ tài chính, ngày công bố, đơn vị và phiên bản báo cáo.

Đề tài: **Hệ thống thu thập, chuẩn hóa và phân tích dữ liệu BCTC–cổ tức tiền mặt Việt Nam để đánh giá khả năng duy trì cổ tức và nghiên cứu cảnh báo sớm rủi ro cắt giảm.**

Trọng tâm học thuật là kỹ thuật dữ liệu và phân tích dữ liệu tài chính. Web/API phục vụ tra cứu dữ liệu có nguồn và giải thích kết quả. Sản phẩm chính gồm bộ dữ liệu tự thu thập, pipeline có kiểm định, phân tích định lượng và các nghiên cứu tình huống.

## 2. Câu hỏi nghiên cứu và kết quả

- RQ1: Có thể tự thu thập và chuẩn hóa các chỉ tiêu cốt lõi với độ chính xác, độ phủ và nguồn truy vết đo được không?
- RQ2: Nhóm giảm/ngừng cổ tức có đặc điểm lợi nhuận, dòng tiền và nợ khác nhóm duy trì như thế nào?
- RQ3: Quy tắc cảnh báo, và mô hình đơn giản nếu đủ mẫu, có cải thiện so với baseline duy trì mức chi trả trước đó không?

Kết quả nghiên cứu có thể cho thấy tín hiệu dự báo yếu. Đề tài vẫn có giá trị nếu dữ liệu, cách kiểm định và giới hạn được báo cáo đầy đủ. Quan hệ thống kê chưa chứng minh quan hệ nhân quả.

## 3. Phạm vi MVP và giới hạn

| Thành phần | Quy định |
|---|---|
| Thời gian | 12–13 tuần; kế hoạch chuẩn là 13 tuần |
| Doanh nghiệp | Pilot 10 doanh nghiệp phi tài chính; tối thiểu khả thi 30; mục tiêu mở rộng 60–80 sau khi pipeline ổn định |
| Khoảng năm | 2020–2024 cho phân tích lịch sử ban đầu; thêm 2025 nếu đủ tài liệu và cửa sổ kết quả đã khép lại |
| Báo cáo | BCTC năm đã kiểm toán; ưu tiên hợp nhất; báo cáo riêng được đánh dấu, phân tích tách biệt |
| Chỉ tiêu lõi | LNST toàn doanh nghiệp, CFO, tiền và tương đương tiền, tổng tài sản, nợ phải trả, vốn chủ sở hữu |
| Cổ tức | Sự kiện tiền mặt, DPS, ngày công bố/chốt quyền/thanh toán dự kiến, năm lợi nhuận nếu được nêu |
| Mở rộng | EPS, LNST thuộc cổ đông công ty mẹ, doanh thu, cổ phiếu được hưởng quyền, tiền cổ tức thực trả, nợ vay |
| Sản phẩm | Dataset có nguồn, báo cáo chất lượng, phân tích quan hệ, điểm cảnh báo giải thích được, web/API tối thiểu |

60–80 công ty là mục tiêu có điều kiện, không phải cam kết trước pilot. BCTC và cổ tức mới nhất có thể bổ sung cho tra cứu, nhưng chỉ mẫu có đủ thời gian quan sát mới được dùng đánh giá dự báo.

Nguồn ứng viên: công bố HNX/HOSE, thông báo VSDC, trang IR doanh nghiệp. Chọn một nguồn chính sau pilot; khả năng crawl, điều kiện truy cập và độ phủ chưa được xác nhận trong tài liệu thiết kế. VN-Index là chỉ số thị trường, không phải nguồn BCTC doanh nghiệp.

## 4. Người sử dụng và luồng chính

Người thực hiện vận hành crawler và xử lý hàng đợi kiểm tra. Người nghiên cứu xem độ phủ, tải dataset và phân tích. Người xem dashboard chọn doanh nghiệp, đọc BCTC/cổ tức/chỉ số và mở tài liệu gốc.

Luồng bắt buộc: khám phá tài liệu → tải bản gốc → trích xuất → chuẩn hóa → kiểm định → ghép cổ tức → tạo bảng doanh nghiệp–năm → phân tích → hiển thị kết quả có bằng chứng.

## 5. Yêu cầu chức năng

| Mã | Yêu cầu | Tiêu chí nghiệm thu |
|---|---|---|
| VN-FR-01 | Quản lý danh sách doanh nghiệp và phạm vi thu thập | Có mã, tên, ngành, sàn/thị trường, lý do chọn/loại |
| VN-FR-02 | Khám phá và tải tài liệu thật | Lưu URL, nguồn, ngày công bố nếu xác định được, thời điểm tải, loại tài liệu, trạng thái HTTP |
| VN-FR-03 | Lưu bản gốc và chạy lại an toàn | Hash file; chạy lại không nhân bản; bản sửa đổi được giữ riêng |
| VN-FR-04 | Trích xuất chỉ tiêu và bằng chứng | Mỗi ứng viên có nhãn gốc, số gốc, đơn vị, kỳ, trang PDF hoặc vị trí HTML |
| VN-FR-05 | Chuẩn hóa số, đơn vị, kỳ và phạm vi báo cáo | Quy đổi VND, phân biệt âm/ngoặc, số cuối kỳ và số so sánh; không trộn riêng/hợp nhất |
| VN-FR-06 | Kiểm định và sửa có lưu vết | Phát hiện thiếu/nhầm đơn vị/đẳng thức sai; lưu người sửa, giá trị cũ và lý do |
| VN-FR-07 | Chuẩn hóa sự kiện cổ tức | Phân biệt tiền/cổ phiếu, đề xuất/tạm ứng, lịch dự kiến/đã xác nhận thực hiện, đổi lịch và hủy |
| VN-FR-08 | Tạo dữ liệu phân tích theo thời điểm | Lưu ngày chốt thông tin, cửa sổ kết quả và lý do mẫu không đủ điều kiện |
| VN-FR-09 | Phân tích quan hệ | Độ phủ, phân bố, xu hướng, tương quan, so sánh nhóm, ít nhất 3 case study có nguồn |
| VN-FR-10 | Điểm cảnh báo theo quy tắc | Có phiên bản, lý do, số liệu đầu vào; thiếu dữ liệu trả trạng thái không đủ dữ liệu |
| VN-FR-11 | API và dashboard | Tra cứu doanh nghiệp, BCTC, sự kiện, chỉ số, chất lượng và tài liệu gốc |
| VN-FR-12 | Xuất dataset tái lập | Có manifest, từ điển dữ liệu, thời điểm snapshot, phiên bản parser/quy tắc và danh sách loại mẫu |
| VN-FR-13 | ML có điều kiện | Chỉ triển khai khi đạt tiêu chí tại đề cương nghiên cứu; baseline, chia theo thời gian, báo cáo kết quả |

VN-FR-01 đến VN-FR-12 là MVP. VN-FR-13 là mở rộng có điều kiện.

## 6. Quy tắc dữ liệu và nghiệp vụ

- Không tìm thấy sự kiện không đồng nghĩa doanh nghiệp không trả cổ tức. Thiếu độ phủ, cửa sổ chưa khép hoặc lịch chưa xác nhận phải gán unknown/censored.
- Ngày thanh toán trong thông báo là lịch dự kiến cho đến khi có bằng chứng phù hợp; không tự chuyển thành cash_paid.
- Tỷ lệ cổ tức theo mệnh giá phải quy đổi bằng mệnh giá nêu trong tài liệu; không mặc định mọi tỷ lệ là DPS.
- Tổng nợ phải trả khác nợ vay. Tỷ số tiền/nợ phải trả được đặt tên đúng, không gọi là cash ratio chuẩn thanh khoản ngắn hạn.
- CFO/LNST chỉ tính khi LNST dương; trường hợp bằng 0/âm được phân tích bằng trạng thái riêng.
- EPS phải tương thích với DPS và phạm vi cổ đông. Ước tính tổng cổ tức cần số cổ phiếu được hưởng quyền tại sự kiện; thiếu số này thì không tính coverage.
- BCTC hợp nhất hỗ trợ đánh giá nhóm doanh nghiệp; khả năng chia cổ tức của công ty mẹ còn phụ thuộc báo cáo riêng và lợi nhuận có thể phân phối. Ghi giới hạn này trong kết quả.
- Điểm quy tắc là thước đo cảnh báo, không phải xác suất đã hiệu chỉnh.

## 7. Yêu cầu chất lượng

| Mã | Yêu cầu | Mục tiêu nghiệm thu đề xuất |
|---|---|---|
| VN-NFR-01 | Truy vết | 100% số liệu được xuất bản có tài liệu gốc và vị trí bằng chứng |
| VN-NFR-02 | Chính xác | Ít nhất 95% độ chính xác kết hợp số/đơn vị/kỳ/phạm vi trên mẫu kiểm tra độc lập; công bố cả trước và sau sửa thủ công |
| VN-NFR-03 | Độ phủ | Mục tiêu 80% ô chỉ tiêu lõi trong tập đã chốt; công bố mẫu số và nguyên nhân thiếu |
| VN-NFR-04 | Tái lập | Chạy lại từ bản gốc với cùng cấu hình cho cùng dataset; phân biệt kiểm thử giả lập và kết quả dữ liệu thật |
| VN-NFR-05 | Khả năng vận hành | Retry có giới hạn, log lỗi và tiếp tục từ lần chạy dở |
| VN-NFR-06 | Tính khả thi | Một người vận hành trên máy cá nhân; module đơn giản; web ưu tiên đọc dữ liệu |

Các ngưỡng trên là mục tiêu thiết kế, chưa phải số đo đã đạt. Nếu không đạt phải báo cáo và điều chỉnh phạm vi bằng quyết định có lý do.

## 8. Nghiệm thu và tài liệu liên quan

MVP đạt khi có pipeline chạy trên dữ liệu thật của tối thiểu 30 doanh nghiệp trong phạm vi đã chốt, bộ mẫu đối chiếu độc lập, dataset có trạng thái thiếu, phân tích quan hệ và 3 case study, điểm giải thích được, dashboard/API dùng dữ liệu thật và báo cáo giới hạn.

Nguồn đặc tả: [Thiết kế](SDD-FDP-01.md), [Kế hoạch](PP-FDP-01.md), [Kiểm thử](TP-FDP-01.md), [Đề cương nghiên cứu](../research-design.md).
