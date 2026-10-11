# Dữ liệu cần thu thập cho UC-1, UC-2, UC-3 và UC-5

Ngày lập: **11/10/2026**. Dùng cùng [kế hoạch thực hiện](28-ke-hoach-thuc-hien-uc-1-2-3-5.md). Các trường bên dưới là đầu vào phục vụ những lát cắt đã chọn; nhóm mở rộng không tự trở thành yêu cầu MVP.

**Đã chốt theo người thực hiện:** HPG, VNM, FPT, năm 2023–2025. [Quyết định phạm vi/stack PaddleOCR](31-chot-pham-vi-va-stack-paddleocr.md), [manifest chín báo cáo đích](../../config/pilot-scope.json). [Danh sách ứng viên trước quyết định](30-danh-sach-doanh-nghiep-de-chon-pham-vi.md) giữ làm lịch sử lựa chọn.

## 1. Thu gì trước?

1. Một PDF năm có thể đọc và sáu chỉ tiêu đã kiểm để chạy UC-1 → UC-2.
2. Ba năm của công ty đầu; thêm công ty thứ hai cùng phạm vi để chạy UC-3.
3. Thông báo cổ tức và khoản thực chi của một ca để chạy UC-5; chỉ tổng hợp thành lịch sử năm khi kiểm đủ nguồn.
4. Hoàn thiện pilot ba doanh nghiệp × FY2023–FY2025. Không dùng Q1/2026 hoặc H1/2026 thay báo cáo năm.

**Đích kiểm kê:** 9 báo cáo năm, **54 ô chỉ tiêu lõi**. Số so sánh FY2024 trong PDF FY2025 là bằng chứng cho một ô và một phiên bản, không được ghi rằng đã thu báo cáo gốc FY2024. Báo cáo gốc/sửa có thời điểm công bố khác nhau phải giữ riêng. Thiếu nguồn hoặc ô chưa xác nhận được thì ghi thiếu, không đánh dấu hoàn thành bộ dữ liệu và không đổi thành 0.

## 2. Dữ liệu nền dùng chung

| Nhóm | Trường cần lưu | Phục vụ việc gì? |
|---|---|---|
| Doanh nghiệp | Mã, tên, sàn; ngành và nguồn ngành nếu sử dụng; mã định danh ổn định | Chọn đúng công ty; tránh ghép do tên tương tự. Ngành chưa xác nhận không làm benchmark |
| Tài liệu | URL catalog/PDF, tên nguồn, ngày tải, ngày công bố nếu có bằng chứng, SHA-256, tệp gốc, số trang, phiên bản/bản sửa | Truy xuất và tái kiểm; không nhầm tải mới là công bố mới |
| Ngữ cảnh báo cáo | Ngày đầu/cuối kỳ, năm tài chính, loại năm/quý/lũy kế; hợp nhất/riêng lẻ; kiểm toán/soát xét/chưa kiểm; tiền tệ và đơn vị | Ngăn ghép kỳ/phạm vi sai; chuẩn hóa giá trị |
| Từng ô số | Chỉ tiêu chuẩn, nhãn gốc/mã dòng, giá trị gốc và chuẩn hóa, đơn vị gốc; trang PDF/trang in, cột và đoạn/vùng nguồn; cách trích | Mở số về đúng trang/cột; biết đơn vị/dấu đã chuyển thế nào |
| Kiểm duyệt | Candidate/đã duyệt/thiếu/mơ hồ, lý do, người và ngày kiểm, sửa trước/sau, phiên bản | Chỉ đưa số đã duyệt vào phân tích; giữ lịch sử thay đổi |
| Lần phân tích | Mã/kỳ/scope đã chọn, chỉ tiêu/công thức, ID phiên bản dữ liệu, nhận xét, ngày lưu | Mở lại đúng kết quả, không âm thầm thay bằng số mới |

Ngày công bố chưa biết phải để trống có lý do; ngày hệ thống thu thập không được dùng giả làm ngày thị trường đã biết. Giữ metadata này cũng giúp nghiên cứu dự đoán về sau tránh dùng thông tin tương lai, nhưng chưa xây dataset ML ở giai đoạn này.

## 3. Sáu chỉ tiêu lõi

| Chỉ tiêu | Vị trí thường tìm | UC sử dụng | Chú ý |
|---|---|---|---|
| LNST toàn doanh nghiệp (`NI_total`) | Báo cáo kết quả kinh doanh | 1/2/3 | Phân biệt tổng LNST với phần thuộc cổ đông công ty mẹ; không tự đổi sang EPS |
| CFO | Báo cáo lưu chuyển tiền tệ | 1/2/3/5 | Giữ dấu; không nhầm tổng lưu chuyển thuần cả kỳ |
| Tiền và tương đương tiền | Bảng cân đối kế toán | 1/2/3 | Không gộp đầu tư ngắn hạn chỉ vì dễ thanh khoản |
| Tổng tài sản | Bảng cân đối kế toán | 1/2/3 | Số cuối kỳ, cùng ngày với các số nguồn vốn |
| Tổng nợ phải trả | Bảng cân đối kế toán | 1/2/3 | Không thay bằng nợ vay; không dùng làm nợ ngắn hạn |
| Tổng vốn chủ sở hữu | Bảng cân đối kế toán | 1/2/3 | Đúng scope; chưa đủ cho ROE bình quân nếu thiếu đầu kỳ |

Khóa dữ liệu cần phân biệt doanh nghiệp + chỉ tiêu + khoảng kỳ/ngày số dư + scope + phiên bản. Kiểm tài sản≈nợ phải trả+vốn chủ sở hữu theo độ làm tròn của nguồn; kiểm này hỗ trợ phát hiện sai đơn vị/cột, không thay kiểm từng ô.

**Nếu chọn thêm doanh thu:** thêm 9 ô cho pilot, thành 63 ô tài chính trước các trường cổ tức/cầu nối; đặc tả bổ sung để làm tăng trưởng doanh thu và biên ròng. Chưa mặc định mở tất cả ba BCTC. Chưa có doanh thu thì giao diện không cung cấp biên lợi nhuận như đã có dữ liệu.

## 4. Dữ liệu riêng cho phân tích sâu và cổ tức

| Nhóm | Cần thu | Chức năng nhỏ / giới hạn |
|---|---|---|
| Cầu nối CFO | LNTT; điều chỉnh khấu hao, dự phòng, lãi vay và các dòng khác; biến động phải thu/tồn kho/phải trả; thuế và các dòng cuối theo mẫu; tổng phụ và CFO | F02.5: đối chiếu tổng và đóng góp từng khoản. Không suy từ sáu tổng số |
| CAPEX và khoản chi | Dòng tiền mua sắm/xây dựng TSCĐ, tài sản dài hạn đúng định nghĩa; các khoản bán/thu khác tách riêng; dòng cổ tức/lợi nhuận trả chủ sở hữu; tên dòng, dấu, scope, kỳ | F05.3/G02: chuẩn hóa khoản chi thành độ lớn theo quy tắc được duyệt. Nếu nguồn gộp thì nhãn kết quả phải ghi khoản phân phối gộp |
| Sự kiện cổ tức tiền mặt | ID/URL/hash thông báo; doanh nghiệp; ngày công bố; năm lợi nhuận; tạm ứng/đợt/còn lại; DPS; tỷ lệ và cơ sở mệnh giá nếu nguồn ghi; ngày đăng ký cuối cùng; ngày thanh toán dự kiến; trạng thái; bản sửa/hủy và quan hệ thay thế | F05.1/.2: lịch sử và vòng đời. Tỷ lệ 10% mệnh giá không phải lợi suất thị trường 10% |
| Thành phần sự kiện | Một thành phần mỗi năm lợi nhuận/đợt/loại quyền; liên kết thông báo gốc | Không cộng cả thông báo hỗn hợp vào một năm hoặc đếm notice và bản sửa hai lần |
| Cơ sở cổ phiếu | Loại sự kiện, tỷ lệ, thời điểm hiệu lực có bằng chứng, số cổ phiếu/cơ sở trước–sau nếu cần, quy tắc làm tròn, nguồn và độ đầy đủ chuỗi | F05.4/G03: chỉ điều chỉnh loại sự kiện được hỗ trợ; không áp hệ số phát hành miễn phí cho mọi phát hành quyền |
| Xác nhận thanh toán | Nguồn chứng minh trạng thái thanh toán nếu có; khoản thực chi trên BCTC và ngữ cảnh; tiền thực nhận của nhà đầu tư chỉ khi có sổ giao dịch riêng | Lịch trả không chứng minh đã trả. Không suy dòng chi BCTC thuộc chính một notice hoặc tiền đã về tài khoản |
| Kiểm kê lịch sử | Giai đoạn tra cứu, nguồn đã kiểm, notice thiếu/mơ hồ, trạng thái đầy đủ tính đến ngày nào, lý do | Chỉ cộng DPS năm khi đủ cơ sở; không có notice chưa đồng nghĩa không trả cổ tức |

Đối với FY2023–FY2025 cần tra cả thông báo công bố/thanh toán ở năm sau, kể cả 2026 cho lợi nhuận 2025; giữ ngày chốt dữ liệu 11/10/2026 và trạng thái chưa kết thúc nếu còn nghĩa vụ/nguồn chưa xác nhận. Không chỉ lọc notice theo năm trên tiêu đề. Thông báo [VNM](https://vsdc.vn/vi/ad1/197038) là ví dụ năm lợi nhuận khác năm thông báo: phần còn lại năm 2025, ngày đăng ký cuối cùng 29/06/2026 và lịch thanh toán 17/07/2026; lịch này không tự chứng minh đã thanh toán.

Cổ tức cổ phiếu không cộng vào biểu đồ thu nhập tiền mặt, nhưng vẫn thu sự kiện liên quan cơ sở cổ phiếu. Chưa đủ ngày hiệu lực/chuỗi sự kiện thì giữ DPS gốc và ghi chưa đủ cơ sở so sánh; không dựng một chuỗi đã điều chỉnh bằng giả định ngầm.

Payout đầy đủ cần khoản thuộc cổ đông thường và lợi nhuận/EPS cùng chủ thể, kỳ, scope và basis. Các trường này chưa nằm trong bộ sáu chỉ tiêu; để sau. Giá cổ phiếu/giá điều chỉnh cũng chưa cần cho lát cắt đầu; không hứa tính lợi suất cổ tức hoặc định giá khi chưa có nguồn giá và quy tắc ngày giá.

## 5. Đang có gì, còn cần thu gì?

**Pilot đã chốt:** HPG/VNM/FPT, ưu tiên BCTC năm hợp nhất, FY2023–FY2025. Đây là nhóm theo dõi/so sánh tự chọn, không phải nhóm cùng ngành. Nguồn chưa tiếp cận được thì ghi pending và xử lý nguồn cho đúng mã đã chọn; không tự thay doanh nghiệp hoặc giảm điều kiện nguồn.

| Mã/ca | Hiện có trong repository | Việc còn thiếu |
|---|---|---|
| HPG | PDF FY2025 và H1/2026 trong bằng chứng crawler | Thu/xác nhận FY2023–2024; kiểm sáu trường mỗi năm, metadata và bản sửa |
| VHC — nghiên cứu trước, ngoài mẫu chính | PDF FY2025 và H1/2026 trong bằng chứng crawler | Giữ làm fixture/minh chứng lịch sử; không tính vào 9 báo cáo đích HPG/VNM/FPT |
| VNM | Có Q1/2026 với cột so sánh Q1/2025 và thử nghiệm ba dòng; có ví dụ notice cổ tức | Chưa có bằng chứng bộ BCTC năm hợp nhất FY2023–2025 đã duyệt; thu lịch sử và sự kiện vốn cần thiết |
| DHG — ca bổ trợ | FY2025, cột FY2024, kiểm sáu trường ở nghiên cứu OCR; cầu nối và đầu vào G02 đã kiểm thủ công | Giữ scope entity của ca này; chưa ghép với hợp nhất như cùng cơ sở. Chưa có ledger cổ tức đủ ba năm |
| FPT — mẫu chính | Notice phát hành miễn phí và ví dụ quy tắc tỷ lệ/làm tròn | Thu/xác nhận BCTC hợp nhất 2023–2025, duyệt 18 ô; kiểm thay đổi phạm vi hợp nhất; thu chuỗi vốn/ngày hiệu lực và lịch sử cổ tức |

Để chạy demo nhanh có thể dùng các số đã kiểm thủ công của DHG/VNM, hiện rõ cách tạo dữ liệu. Điều đó kiểm được luồng ứng dụng, không chứng minh bộ trích xuất tự động đã tổng quát. Không cộng số PDF từ nhiều đợt khảo sát để báo tổng corpus nếu chưa khử trùng SHA-256; cùng báo cáo tải nhiều lần chỉ là một nội dung nguồn.

## 6. Cách tổ chức thu thập và kiểm duyệt

1. **Manifest trước:** ghi các báo cáo đích gồm mã, kỳ, scope, nguồn dự kiến và trạng thái `chưa tìm / đã tải / đã xác nhận báo cáo / đã duyệt ô / thiếu`. Trang catalog chỉ tạo candidate; kiểm bìa và header mới xác nhận ngữ cảnh.
2. **Giữ tài liệu gốc:** lưu URL, hash, thời điểm thu và đường dẫn; khử trùng nội dung nhưng giữ mọi lần quan sát cần thiết. `data-sets/` hiện bị Git ignore, nên cần bản sao lưu riêng và metadata trong hồ sơ minh chứng; không coi Git đã bảo quản PDF.
3. **Lập ô tham chiếu:** đọc trang có sáu trường và cột đúng, lưu nhãn/giá trị/đơn vị/locator; ghi là đối chiếu thủ công cùng người nếu chưa có người kiểm độc lập.
4. **Chạy trích xuất:** tạo candidate, giữ nguyên số thô; ô mơ hồ cần duyệt. Phân tích chỉ truy vấn các ô đã duyệt.
5. **Kiểm tương thích và sửa:** kiểm dấu/đơn vị, phương trình bảng cân đối, nhãn NI, scope và thời gian; sửa có phiên bản. Mẫu khác cần fixture riêng, không sửa parser để đúng một ô rồi coi đạt toàn corpus.
6. **Thu sự kiện theo doanh nghiệp:** VSDC, trang IR, nghị quyết/ĐHĐCĐ và tài liệu liên quan; giữ cả bản sửa/hủy. Tách thành phần, kiểm coverage theo năm lợi nhuận trước tổng hợp.
7. **Bàn giao dữ liệu theo mốc:** một báo cáo dùng được → lịch sử công ty đầu → nhóm so sánh → hồ sơ cổ tức → pilot. Không chờ thu hàng loạt mới demo giá trị sử dụng.

Mỗi mốc nên có bảng số ô đích / đã duyệt / thiếu / mơ hồ, thời gian xử lý, lỗi đã sửa và người kiểm. Thiếu hợp lệ được trình bày cho người dùng, nhưng vẫn phải báo chưa đạt độ đầy đủ mục tiêu. Việc phân tích có thể chạy trên phần đã duyệt mà không giả tạo phần còn thiếu.

## 7. Dữ liệu chưa ưu tiên thu

Chưa thu giao dịch nhà đầu tư, tick/intraday, dữ liệu toàn thị trường, tin tức phục vụ AI, số liệu mọi ngành hoặc toàn bộ dòng ba BCTC chỉ để mở rộng corpus. DuPont, quý/kế hoạch, benchmark ngành, danh mục và định giá chỉ thêm trường sau khi chọn chức năng và dự toán. ML cần mục tiêu dự đoán, lịch sử dài hơn, thời điểm dữ liệu sẵn có và cách kiểm ngoài mẫu; không mặc định tận dụng 9 quan sát pilot để đưa ra dự đoán đầu tư.

Nguồn chính sau chốt thêm [FPT](https://fpt.com/vi/nha-dau-tu); các nguồn DHG/VHC dưới đây là nghiên cứu trước. Nguồn đã khảo sát: [HPG](https://www.hoaphat.com.vn/quan-he-co-dong/bao-cao-tai-chinh), [VHC](https://www.vinhhoan.com/investors-2/), [DHG](https://dhgpharma.com.vn/vi/bao-cao-tai-chinh), [VNM](https://www.vinamilk.com.vn/investor/reports/financial), [VSDC — ví dụ](https://vsdc.vn/vi/ad1/197038). Đã đọc lại các catalog/notice trừ VNM trả 403 ở công cụ đọc web ngày 11/10; không đồng nghĩa các PDF lịch sử đã được tải/xác nhận. Bằng chứng cục bộ được liên kết trong tài liệu 28.
