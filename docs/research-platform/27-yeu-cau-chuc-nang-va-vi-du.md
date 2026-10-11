# Yêu cầu chức năng — mục đích, phân rã và ví dụ

Phiên bản **2.0**, ngày **11/10/2026**. Theo yêu cầu người thực hiện: bỏ **Tìm và khám phá trường hợp cần chú ý (A04)**; ưu tiên người theo dõi tài chính doanh nghiệp và nhà đầu tư; tổ chức **UC lớn → chức năng nhỏ**.

Đây là danh mục yêu cầu và ứng viên để lựa chọn phát triển. Phần có trong SRS được chỉ rõ; phần bổ sung chưa tự trở thành nghĩa vụ nghiệm thu. [SRS v3.3](22-srs-dac-ta-yeu-cau-phan-mem.md) rút FR29/FR30/D09/D10. UC-F bên dưới là cấu trúc sản phẩm để nghiên cứu, không đổi ID truy vết kỹ thuật cũ. Hiện chưa có ứng dụng hoàn chỉnh; prototype tính toán không đồng nghĩa cả chức năng đã triển khai.

**Ưu tiên mới nhất 11/10/2026:** theo người thực hiện, tập trung **UC-F01 → UC-F02 → UC-F03 → UC-F05**, sau đó **UC-F04**. Xem [tiến độ có bằng chứng và kế hoạch từng mốc](28-ke-hoach-thuc-hien-uc-1-2-3-5.md), [dữ liệu cần thu thập](29-du-lieu-can-thu-thap-cho-uc-1-2-3-5.md). Thứ tự này chọn lát cắt thực hiện; không yêu cầu làm toàn bộ chức năng nhỏ của một UC trước khi bắt đầu UC kế tiếp.

## 1. Hệ thống giúp người dùng làm gì?

**Phạm vi/stack đã chốt:** HPG/VNM/FPT, BCTC năm 2023–2025; OCR chính PaddleOCR. [Quyết định hiện hành](31-chot-pham-vi-va-stack-paddleocr.md). Đây là mẫu triển khai/kiểm chứng, không là benchmark ngành hoặc phạm vi toàn thị trường.

**Người dùng chính:** người theo dõi tài chính doanh nghiệp và người đầu tư cần tự tìm hiểu doanh nghiệp. Người vận hành dữ liệu là vai trò hỗ trợ, thực hiện thu thập, trích xuất, chuẩn hóa và duyệt số liệu.

Một lần sử dụng điển hình: chọn doanh nghiệp → xem dữ liệu nhiều kỳ → phân tích bằng bảng/biểu đồ → so sánh với doanh nghiệp tự chọn → xem công bố và lịch cổ tức → lưu nhận xét cùng bằng chứng để tiếp tục theo dõi.

**Đánh giá chiều sâu sau bản vẽ:** [nghiên cứu mức hỗ trợ người đầu tư](37-danh-gia-muc-do-ho-tro-nha-dau-tu.md) phân biệt chức năng chưa vẽ với phần còn thiếu dữ liệu/phạm vi thực hiện. Năm UC chính phù hợp về nhóm; sáu chỉ tiêu và vài biểu đồ chưa đủ phân tích tài chính toàn diện. Gói doanh thu/biên, thanh khoản/nợ vay và tương tác phân tích vẫn là đề xuất, chưa đổi ID, 38 chức năng, nghĩa vụ SRS hoặc kế hoạch v6.

Các ví dụ A/B và con số bên dưới là giả định để giải thích chức năng, không phải dữ liệu doanh nghiệp hoặc kết quả đã triển khai.

| UC lớn | Mục đích thực tế | Vị trí đề xuất |
|---|---|---|
| UC-F01 — Khai thác dữ liệu tài chính doanh nghiệp | Có bộ số liệu sử dụng được, tránh đọc và nhập lại từng PDF | Nền tảng, làm trước |
| UC-F02 — Phân tích dữ liệu tài chính | Hiểu doanh nghiệp thay đổi thế nào và khoản nào giải thích sự thay đổi | Trọng tâm sử dụng |
| UC-F03 — So sánh tài chính doanh nghiệp | Đối chiếu doanh nghiệp mình quan tâm trên cùng cơ sở | Trọng tâm sử dụng |
| UC-F04 — Theo dõi doanh nghiệp và sự kiện | Tiếp tục theo dõi doanh nghiệp đã chọn khi có công bố mới | Sau lát cắt UC-F01/02/03/05 |
| UC-F05 — Phân tích cổ tức | Hiểu lịch sử, cơ sở cổ phiếu và khả năng bao phủ các khoản chi | Ưu tiên cùng 01/02/03, trước 04 |
| UC-F06 — Theo dõi danh mục đầu tư | Biết tài sản đang nắm giữ, kết quả và thu nhập thực nhận | Mở rộng, cần giao dịch và giá |
| UC-F07 — Mô phỏng kịch bản và định giá | Thử giả định của mình, xem kết quả nhạy với giả định nào | Mở rộng, chọn từng mô hình |

Biểu đồ là chức năng nhỏ của UC phân tích, so sánh hoặc danh mục tương ứng. Tra cứu nguồn, lưu lần phân tích và xuất kết quả là năng lực dùng chung. Thu thập/trích xuất/duyệt là phân rã phục vụ UC-F01. Không lập một UC lớn chỉ để vẽ biểu đồ, tính một tỷ số hay tải một báo cáo.

## 2. UC-F01 — Khai thác dữ liệu tài chính doanh nghiệp

**Giải quyết:** người dùng muốn có dữ liệu đúng doanh nghiệp/kỳ và sử dụng tiếp mà không tự tổng hợp từ nhiều tài liệu. Đầu vào: doanh nghiệp, giai đoạn, phạm vi báo cáo và chỉ tiêu. Đầu ra: bảng chuẩn hóa, trạng thái đầy đủ, định nghĩa và bằng chứng nguồn.

| UC nhỏ | Chức năng | Mục đích và ví dụ đơn giản |
|---|---|---|
| F01.1 | Tra cứu doanh nghiệp và hồ sơ cơ bản | Tìm đúng mã/tên; biết sàn và ngành khi có nguồn xác nhận |
| F01.2 | Xem dữ liệu tài chính nhiều kỳ | Đọc cùng một chỉ tiêu qua 2023–2025 trong một bảng; mở rộng thành ba báo cáo khi đủ dòng |
| F01.3 | Chọn và xuất bộ dữ liệu | Chọn A/B, LNST và CFO trong ba năm; xuất dữ liệu kèm đơn vị/trạng thái |
| F01.4 | Tra cứu định nghĩa và truy xuất bằng chứng | Chọn ô CFO 2025 để biết nghĩa chỉ tiêu và xem đúng trang báo cáo |
| F01.5 | Xem độ đầy đủ và phiên bản dữ liệu | Biết số còn thiếu hoặc đã sửa; không coi ô trống là 0 |
| F01.6 | Thu thập, chuẩn hóa và duyệt dữ liệu tài chính | Phát hiện/tải → trích candidates → kiểm tra → duyệt → cung cấp số cho người dùng |

**Phạm vi hiện có:** sáu chỉ tiêu lõi và luồng dữ liệu/nguồn đã đặc tả trong FR01–FR18/FR31–FR38. Kho toàn bộ ba BCTC, danh mục ngành đầy đủ và màn hình chọn nhiều chỉ tiêu là bổ sung. Chưa có doanh thu thì phải thể hiện chưa cung cấp chỉ tiêu.

Tên UC nhỏ bắt đầu bằng động từ và mô tả thao tác của tác nhân. F01.5 phục vụ người theo dõi tài chính xem số liệu đã có/thiếu/đã sửa; F01.6 do người vận hành thực hiện để cung cấp bộ số đã duyệt. “Độ đầy đủ” và “nền dữ liệu” chỉ là khái niệm mô tả, không dùng làm tên UC.

**Minh chứng hoàn thành:** chọn A/B và giai đoạn → nhận dữ liệu kể cả mục thiếu → kiểm một ô về nguồn → xuất và mở lại được. Lấy đủ PDF chưa hoàn thành UC này.

## 3. UC-F02 — Phân tích dữ liệu tài chính

**Giải quyết:** hiểu tình hình doanh nghiệp, thay vì chỉ nhận con số tổng hợp. Đầu vào: dữ liệu đã duyệt qua các kỳ tương thích. Xử lý: đối chiếu thời gian, tính chỉ tiêu có điều kiện và phân rã khi đủ dữ liệu. Đầu ra: bảng, biểu đồ, công thức, khoản đóng góp và câu hỏi để đọc tiếp.

| UC nhỏ | Chức năng | Mục đích và ví dụ đơn giản |
|---|---|---|
| F02.1 | Xem biểu đồ và bảng xu hướng tài chính | LNST tăng 90→100 tỷ nhưng CFO giảm 130→80 tỷ: nhìn rõ hai hướng; chọn điểm để đọc số/nguồn |
| F02.2 | Phân tích tăng trưởng và biên lợi nhuận | Doanh thu tăng nhưng biên ròng giảm 10%→8%: thấy lợi nhuận không tăng tương ứng |
| F02.3 | Phân tích cơ cấu tài sản và nguồn vốn | Xem tiền, phải thu, tồn kho hoặc nợ vay chiếm bao nhiêu; so cơ cấu khi quy mô đổi |
| F02.4 | Phân tích khả năng chuyển lợi nhuận thành tiền | LNST 100/CFO 80 tỷ: CFO/LNST=0,8 khi hợp lệ; đặt lịch sử hai chỉ tiêu cạnh nhau |
| F02.5 | Phân rã dòng tiền và chênh lệch các kỳ | Cầu nối LNTT→CFO chỉ ra điều chỉnh phi tiền/vốn lưu động; biết phải thu góp bao nhiêu vào thay đổi CFO |
| F02.6 | Phân tích sinh lời và DuPont | Tách ROE thành biên lợi nhuận, vòng quay tài sản và hệ số vốn; hiểu ROE tăng nhờ phần nào |
| F02.7 | Đối chiếu quý/cùng kỳ và kế hoạch–thực hiện | Doanh thu sáu tháng 600/kế hoạch năm 1.200 tỷ=50%: xem tiến độ; chưa suy hoàn thành cả năm |
| F02.8 | Lưu, chú thích và xuất lần phân tích | Lưu doanh nghiệp, giai đoạn, chỉ tiêu, bảng/biểu đồ, nhận xét và bản dữ liệu; mở lại đúng bối cảnh |

**Ví dụ, số giả định:** chọn A → xem LNST/CFO 2023–2025 → chọn năm CFO giảm → xem cầu nối với dòng đã duyệt → tra soát khoản phải thu → ghi câu hỏi cần đọc thuyết minh. Hệ thống cung cấp cơ sở diễn giải; người dùng tự hình thành nhận xét.

**Phạm vi hiện có:** FR25–FR27 có xu hướng/tỷ số tiền–nợ phải trả–tài sản; E01–E10 có cầu nối theo ca; FR34/35 và D11/12 có nền lưu/xuất. Chọn chỉ tiêu, liên kết bảng/biểu đồ, biên lợi nhuận, cơ cấu chi tiết, DuPont, quý và kế hoạch là bổ sung. Nợ phải trả/tài sản không thay tỷ lệ nợ vay hoặc thanh khoản ngắn hạn.

**Dữ liệu cần thêm:** doanh thu cho biên ròng; tài sản/nợ ngắn hạn cho thanh khoản; phải thu/tồn kho/nợ vay cho cơ cấu; số dư đầu–cuối kỳ và lợi nhuận/vốn cùng phạm vi cho ROE/DuPont; mục tiêu có ngày công bố/đơn vị/kỳ cho kế hoạch. Tách quý từ số lũy kế chỉ khi hai khoảng kỳ/phiên bản tương thích; giữ cả số gốc và số suy ra. Không dựng phân rã từ sáu số tổng khi thiếu dòng cấu thành.

## 4. UC-F03 — So sánh tài chính doanh nghiệp

**Giải quyết:** một số liệu cần cơ sở đối chiếu; CFO lớn hơn có thể chỉ vì doanh nghiệp lớn hơn. Đầu vào: **doanh nghiệp do người dùng chọn**, kỳ, phạm vi và chỉ tiêu. Đầu ra: bảng/biểu đồ, khác biệt và chỗ chưa đủ cơ sở.

| UC nhỏ | Chức năng | Mục đích và ví dụ đơn giản |
|---|---|---|
| F03.1 | So sánh chỉ tiêu nhiều doanh nghiệp | Đặt A/B cạnh nhau, cùng năm; xem doanh thu, lợi nhuận, CFO khi có dữ liệu |
| F03.2 | So sánh tỷ số và cơ cấu | A có CFO 80/LNST 100=0,8; B có CFO 60/LNST 50=1,2: phân biệt quy mô và tỷ số |
| F03.3 | So sánh xu hướng qua nhiều kỳ | A cải thiện biên lợi nhuận, B giảm; xem các đường cùng giai đoạn/đơn vị |
| F03.4 | Đối chiếu với nhóm ngành xác định mẫu | Nếu đủ công ty cùng ngành: xem trung vị/phân bố, danh sách mẫu và số thiếu |

**Điều kiện:** không tự ghép riêng lẻ với hợp nhất hoặc năm với quý. Benchmark cần danh mục ngành, chính sách chọn mẫu và dữ liệu; ba công ty khác ngành không là trung bình ngành. So DPS cần basis phù hợp trong từng chuỗi.

**Phạm vi:** số liệu/tỷ số nền có trong SRS; bảng nhiều doanh nghiệp và benchmark là bổ sung. UC phục vụ đối chiếu doanh nghiệp đã chọn. Tự tìm mã theo điều kiện tài chính, phân loại đạt/không đạt và sàng lọc ứng viên đã loại bỏ.

## 5. UC-F04 — Theo dõi doanh nghiệp và sự kiện

**Giải quyết:** biết công bố/dữ liệu mới của doanh nghiệp mình theo dõi. Đầu vào: danh sách tự chọn và tài liệu/sự kiện ghi nhận. Đầu ra: dòng cập nhật, lịch có nguồn và đường tới phân tích liên quan.

| UC nhỏ | Chức năng | Mục đích và ví dụ đơn giản |
|---|---|---|
| F04.1 | Quản lý danh sách theo dõi | Thêm A/B để lần sau mở nhanh; không cần khai báo đã mua cổ phiếu |
| F04.2 | Xem công bố mới theo doanh nghiệp | Biết A có BCTC/báo cáo thường niên/nghị quyết mới; xem ngày/văn bản nguồn |
| F04.3 | Xem lịch sự kiện có nguồn | Lịch ĐHĐCĐ, ngày đăng ký cuối cùng, lịch thanh toán; phân biệt dự kiến và đã sửa |
| F04.4 | Đối chiếu dữ liệu trước/sau cập nhật | CFO 120→125 tỷ sau duyệt bản sửa; xem số và nguồn cũ/mới |
| F04.5 | Tiếp tục phân tích từ cập nhật | Từ báo cáo mới mở F02; giữ nhận xét cũ và tạo bản mới khi người dùng chọn |

**Phạm vi:** nền phiên bản/revision/cổ tức/snapshot đã đặc tả; watchlist, dòng công bố và lịch tổng hợp là bổ sung. BCTC/công bố trước, tin tức rộng sau nếu nguồn phù hợp; cập nhật trong ứng dụng trước. Ngày hệ thống thu khác ngày nguồn công bố; không suy lịch báo cáo khi chưa có nguồn. Theo dõi doanh nghiệp đã chọn, không tái lập A04 dưới tên cảnh báo.

## 6. UC-F05 — Phân tích cổ tức

**Giải quyết:** đọc đúng lịch sử chính sách và xem cổ tức trong quan hệ với lợi nhuận/dòng tiền. Đầu vào: tài chính, thông báo, đợt quyền, năm lợi nhuận và sự kiện cổ phiếu. Đầu ra: lịch sử DPS, khoản cấu thành, phép tính bao phủ có nguồn và giới hạn.

| UC nhỏ | Chức năng | Mục đích và ví dụ đơn giản |
|---|---|---|
| F05.1 | Xem lịch sử và biểu đồ cổ tức tiền mặt | Xem DPS theo năm lợi nhuận, đợt cấu thành và mức đầy đủ |
| F05.2 | Đối chiếu chính sách, quyền, lịch thanh toán | Trả tháng6/2026 thuộc lợi nhuận2025: xem đúng cả năm lợi nhuận và lịch |
| F05.3 | Phân tích tiền sau chi đầu tư và phân phối | CFO 120−CAPEX 80−thực chi 60=−20 tỷ: ba khoản vượt CFO kỳ; chưa suy nguồn tài trợ |
| F05.4 | Kiểm cơ sở cổ phiếu và tính so sánh DPS | Số cổ phiếu đổi: xem DPS gốc và chuỗi tham chiếu khi có cơ sở điều chỉnh |
| F05.5 | Đối chiếu phân phối với lợi nhuận phù hợp | Tính payout khi biết khoản cho cổ đông thường, lợi nhuận và scope tương ứng; không DPS/LNST tổng |
| F05.6 | Lưu nhận xét/câu hỏi về cổ tức | Ghi “cần kiểm CAPEX và dòng vay”, gắn số/nguồn để rà lại |

**Phạm vi hiện có:** FR19–FR24/FR28 và D01–D08; nhận xét dùng D11/12. Payout hoàn chỉnh cần thêm dữ liệu đúng chủ thể. G02 tính theo khoản chi đã định nghĩa; không mặc định CFO−CAPEX là FCFE hoặc cổ tức công bố là tiền thực trả.

**Cổ tức bằng cổ phiếu:** chưa cộng vào thu nhập tiền mặt, nhưng giữ sự kiện để kiểm basis DPS/EPS/vị thế. Bỏ toàn bộ sự kiện dễ làm chuỗi trên mỗi cổ phiếu bị diễn giải sai. Lịch thanh toán chưa chứng minh tiền về tài khoản nhà đầu tư.

## 7. UC-F06 — Theo dõi danh mục đầu tư — mở rộng

**Giải quyết:** theo dõi khoản đang nắm giữ và thu nhập của chính mình. UC-F04 chỉ cần danh sách quan tâm; UC này cần giao dịch, vị thế và tiền.

| UC nhỏ | Chức năng | Mục đích và ví dụ đơn giản |
|---|---|---|
| F06.1 | Nhập giao dịch và xác lập vị thế | Nhập mua/bán, phí, sự kiện từ sổ/CSV; tính số cổ phiếu còn giữ |
| F06.2 | Theo dõi giá trị và lãi/lỗ | Xem giá vốn, giá thị trường, lãi/lỗ đã/chưa thực hiện và thời điểm giá |
| F06.3 | Xem biểu đồ phân bổ | A chiếm 60% giá trị cổ phiếu; xem tỷ trọng doanh nghiệp/ngành và tiền mặt |
| F06.4 | Đánh giá hiệu quả và đối chiếu benchmark | Xử lý nộp/rút tiền, cổ tức trước tính lợi suất; benchmark cùng cơ sở |
| F06.5 | Theo dõi cổ tức dự kiến và thực nhận | 1.000 cổ phiếu đủ quyền×1.500 đồng=1,5 triệu gộp dự kiến; tiền thực nhận ghi riêng, tổng theo tháng |

**Điều kiện ở Việt Nam:** ledger giao dịch/sự kiện, nguồn giá có ngày/trạng thái, chính sách giá vốn, phí/thuế theo nguồn hoặc giả định khai báo, đủ quyền và tiền thực nhận. Nhập tay/CSV trước kết nối tài khoản. Không suy đủ quyền từ số giữ hôm nay; không coi tăng NAV do nộp tiền là lợi suất. Benchmark giá và lợi suất gồm cổ tức phải phân biệt. Chưa thuộc MVP sáu trường BCTC.

## 8. UC-F07 — Mô phỏng kịch bản và định giá — mở rộng

**Giải quyết:** hiểu kết quả đổi ra sao khi giả định đổi. Đầu vào: bản dữ liệu gốc, giả định người dùng và mô hình có công thức. Đầu ra: bảng kịch bản/độ nhạy và bản giả định lưu được.

| UC nhỏ | Chức năng | Mục đích và ví dụ đơn giản |
|---|---|---|
| F07.1 | Thử kịch bản dòng tiền/khoản chi | Giữ CAPEX 80/thực chi 60, đổi CFO 120→150: số dư−20→10 tỷ; lịch sử giữ nguyên |
| F07.2 | So sánh và lưu giả định | Đặt ba kịch bản; xem kết quả và giả định khác nhau ở đâu |
| F07.3 | Mô phỏng định giá DCF/DDM có điều kiện | Đổi tăng trưởng/dòng tiền/chiết khấu; xem giá trị theo mô hình cùng đầu vào |
| F07.4 | Xem bảng/biểu đồ độ nhạy | Biết giá trị mô hình đổi bao nhiêu khi chiết khấu hoặc tăng trưởng dài hạn đổi |

**Ưu tiên:** F07.1 dùng lại G02 nên thử trước. DCF/DDM cần FCFF/FCFE/DPS, dòng dự phóng, nợ vay, tiền, số cổ phiếu và tỷ lệ chiết khấu phù hợp; chặn tổ hợp không hợp lệ như chiết khấu≤tăng trưởng dài hạn trong mô hình vĩnh viễn. Không thay nợ vay bằng nợ phải trả. Kết quả là giá trị theo giả định, không phải giá tương lai đã dự báo.

## 9. Năng lực dùng chung và thứ tự bổ sung

Dùng chung doanh nghiệp/kỳ/scope, định nghĩa/công thức, dữ liệu thiếu có lý do, nguồn từng số, phiên bản và lần phân tích lưu. Truy xuất nguồn để kiểm chứng; đối chiếu để so số; tra soát khi xử lý sai lệch. Không đổi mọi nhãn thành “tra soát”.

| Ưu tiên | Phần nên hoàn thành | Kết quả sử dụng được |
|---|---|---|
| P0 | F01 nền + F02.1/.4/.8 + F03.1/.2 với dữ liệu hiện có | Chọn A/B → bảng/biểu đồ → so cùng cơ sở → nguồn → lưu/xuất |
| P1 | F05 nền/G02/G03; F02.5 theo ca đủ dòng | Phân tích cổ tức cùng cơ sở tiền mặt/cổ phiếu, sau lát cắt P0 và trước UC-F04 |
| P2 | UC-F04 sau khi 01/02/03/05 dùng được | Theo dõi công bố/phiên bản và tiếp tục phân tích doanh nghiệp tự chọn |
| P3 | F02.2/.3/.6/.7, F03.4, UC-F06, UC-F07 theo phần được chọn và nguồn đủ | Mở rộng chiều sâu phân tích, benchmark, danh mục/kịch bản/định giá; chưa tự thuộc đợt đầu |

Đây là thứ tự nghiên cứu/phát triển, không phải lịch tất cả chức năng trong 13 tuần. Chọn lát cắt rồi phân rã đầu vào → xử lý → đầu ra → kiểm chứng. Không cần làm mọi chức năng học được từ GitHub.

## 10. Nguồn nghiên cứu và tài liệu thực hiện

Chuyển thể từ **36 repository**, trong đó25 có ít nhất 3.000 sao tại lần truy xuất 11/10/2026; đọc mã chọn lọc của17 repo. Chưa cài/chạy dự án nguồn; chưa chứng minh tăng lợi nhuận đầu tư. Mức sao giúp ưu tiên khảo sát, không chứng minh độ đúng hoặc mức cần thiết.

- [Kết luận và ý tưởng bổ sung](../research-high-star-finance/README.md).
- [Khảo sát36 repo, số sao, loại và mức đọc](../research-high-star-finance/01-khao-sat-repository.md).
- [Minh chứng mã và chuyển thể cho Việt Nam](../research-high-star-finance/02-minh-chung-ma-va-bai-hoc.md).
- [Khả thi, dữ liệu, thứ tự và tác vụ kiểm chứng](../research-high-star-finance/03-kha-thi-va-thu-tu-thuc-hien.md).
- [SRS hiện hành, quyết định rút chức năng tại mục18](22-srs-dac-ta-yeu-cau-phan-mem.md).
- [Bản trước khi loại A04](history/before-user-removal-2026-10-11.zip).
