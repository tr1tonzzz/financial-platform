# Tính khả thi và cách thực hiện các nhóm chức năng

Ngày 11/10/2026. Phục vụ lựa chọn phát triển theo [danh mục UC-F01–07](../research-platform/27-yeu-cau-chuc-nang-va-vi-du.md). Mức khả thi dưới đây là đánh giá thiết kế dựa trên dữ liệu/phần mềm hiện có, chưa phải kết quả chạy ứng dụng nguồn hoặc cam kết đủ giờ triển khai tất cả.

## 1. Những gì hiện có và khoảng trống

Hiện có đặc tả sáu trường tài chính lõi, vòng đời cổ tức, nguồn/phiên bản/snapshot, ca cầu nối và prototype G02/G03/lưu hồ sơ. Chưa có ứng dụng người dùng hoàn chỉnh hoặc bộ dữ liệu lịch sử đã nghiệm thu. Dữ liệu/API trong repo tham chiếu chưa được thử đối chứng cho pilot Việt Nam. Việc có mã tính hoặc vẽ biểu đồ chưa chứng minh cả tác vụ từ nguồn đến đầu ra dùng được.

Sáu trường lõi: LNST toàn doanh nghiệp/nhóm, CFO, tiền và tương đương tiền, tổng tài sản, nợ phải trả, tổng vốn chủ sở hữu. Pilot vẫn là 3 doanh nghiệp phi tài chính × 2023–2025. Trước mắt dùng Python/SQLite/pandas/Streamlit đã dự kiến; không cần đổi toàn bộ công nghệ theo terminal nguồn.

## 2. Dữ liệu → chức năng → điều kiện hoàn thành

| UC/chức năng | Dữ liệu và phần cần thêm | Cách thực hiện vừa sức | Khả thi / điểm phải giải quyết | Tác vụ kiểm chứng |
|---|---|---|---|---|
| F01.1–.5, F02.1/.4, F03.1/.2 | Sáu trường đã duyệt, kỳ/scope/đơn vị/nguồn; dữ liệu thiếu có lý do | Một truy vấn chung trả bảng dài theo company/period/metric; bảng và biểu đồ cùng bộ chọn; chỉ số cùng registry | Cao về phần mềm; còn phụ thuộc hoàn thành dữ liệu pilot | Chọn A/B, 3 năm; xem xu hướng/tỷ số; một ô thiếu; mở đúng trang nguồn; xuất đúng dữ liệu |
| F02.8, F05.6 | Snapshot, công thức, ghi chú, cấu hình góc nhìn | Lưu cấu hình có phiên bản; ghi chú riêng facts; mở bản cũ hoặc tạo bản mới có chủ đích | Cao với bố cục cố định; không cần trình kéo thả dashboard | Sửa số hiện hành nhưng lần phân tích cũ vẫn giữ số/ghi chú/nguồn cũ |
| F02.2 — biên lợi nhuận | Thêm doanh thu thuần; lợi nhuận gộp/giá vốn nếu chọn biên gộp | Mở registry/target/duyệt cho nhóm này; biểu đồ doanh thu và biên, bảng delta | Vừa; lợi ích rõ, dữ liệu mở rộng ít hơn toàn bộ BCTC | Doanh thu tăng nhưng biên giảm; mẫu thiếu doanh thu không có margin |
| F02.3 — cơ cấu/thanh khoản | Chọn một bộ: tài sản ngắn hạn, nợ ngắn hạn, phải thu, tồn kho, nợ vay; định nghĩa dòng | Bảng common-size/stacked bar; tỷ số có công thức; nhóm con không cộng chồng | Vừa; mapping và mẫu số quan trọng hơn đồ thị | Tổng nhóm không đếm trùng; chặn mẫu số 0; phân biệt nợ vay và nợ phải trả |
| F02.5/F05.3 — cầu nối và khoản chi | LNTT/các dòng điều chỉnh đã duyệt, CFO; CAPEX và phân phối thực chi đúng kỳ/scope | Bảng/waterfall giữ dấu; residual riêng; tính G02 rồi mở dòng nguồn | Vừa cho 1–3 ca; không bảo đảm tự động mọi mẫu | Tái tính một cầu nối; residual đúng; thiếu CAPEX chỉ chặn kết quả phụ thuộc |
| F02.6 — DuPont | Doanh thu, LNST/vốn tương ứng, tài sản/vốn đầu–cuối kỳ | Tính ba thành phần theo policy; biểu đồ thành phần qua năm; lưu operands | Vừa; đầu kỳ và phạm vi cổ đông thường cần định nghĩa | Tích ba thành phần khớp ROE; chặn vốn bình quân≤0 nếu policy quy định không diễn giải ROE thường |
| F02.7 — quý/cùng kỳ | Ngày bắt đầu/kết thúc kỳ, loại stock/flow; số lũy kế và bản sửa | Giữ dữ liệu gốc; sinh quý từ các flow lũy kế tương thích; ghi lineage | Vừa–khó; quý bổ sung nguồn và khối lượng duyệt | Quý II=6 tháng−quý I đúng khi đủ; không trừ số dư tài sản; thiếu kỳ trước để null |
| F02.7 — kế hoạch–thực hiện | Nghị quyết/ĐHĐCĐ/kế hoạch có nguồn, ngày công bố, revisions; thực tế cùng metric/scope | Bảng target/actual/progress; kèm văn bản và kỳ; mục tiêu khoảng giữ khoảng | Vừa; kế hoạch có thể sửa, lợi nhuận khác scope; không tự mùa vụ hóa | Actual 600/target 1.200=50%; target sửa mở được bản cũ; mục tiêu chưa cùng scope bị chặn |
| F03.3/.4 — xu hướng/benchmark | Nhóm công ty người dùng chọn; ngành có nguồn; đủ mẫu/quy tắc chọn | So xu hướng trước; benchmark sau, hiển thị danh sách/missing và trung vị | Cao cho nhóm tự chọn, vừa–khó cho chuẩn ngành | Hai công ty cùng kỳ; ba công ty khác ngành không xuất nhãn “trung bình ngành” |
| F04.1/.2/.4/.5 | Watchlist tự chọn; metadata công bố; facts revisions; snapshot | Bảng theo dõi/công bố và trước–sau; liên kết sang phân tích; cập nhật sau duyệt | Vừa; phải nhận diện trùng và quan hệ bản sửa | Có công bố mới của A, không có B; số sửa đúng trước/sau; bản phân tích cũ không đổi |
| F04.3 — lịch | Sự kiện chính thức, loại ngày, ngày dự kiến/đã sửa, nguồn | Lịch/bảng sự kiện của watchlist; ngày chưa biết để trống, canceled giữ dấu vết | Vừa; khó ở discovery và vòng đời, không ở calendar UI | Quyền dời lịch hiển thị bản hiệu lực và nguồn; chưa có ngày thì không bịa mốc |
| F05.1/.2/.4 | Notices/components, năm lợi nhuận, coverage, revisions, ledger cổ phiếu | Biểu đồ DPS theo profit_year, timeline ngày; chuỗi gốc/tham chiếu có điều kiện | Vừa; tái sử dụng G03, nhưng cần chain/basis đầy đủ | Năm trả khác năm lợi nhuận; canceled không biến DPS năm thành0; thiếu basis chặn so chuỗi |
| F05.5 — payout | Khoản phân phối cho cổ đông thường và lợi nhuận tương ứng; scope, năm, trạng thái policy/paid | Metric riêng theo policy/cash paid; không ghép tổng công bố với cashflow thực chi âm thầm | Vừa–khó; dữ liệu đúng chủ thể mới quyết định tính được | Không DPS/LNST; không ghép tiền trả trong năm với profit_year sai; mẫu thiếu thông tin để null |
| F06.1/.2/.3/.5 | Giao dịch, phí, sự kiện, vị thế, đủ quyền, giá và tiền thực nhận | Nhập tay/CSV; lot/ledger; bảng holdings và phân bổ; income ledger theo tháng | Vừa–khó; mở một miền dữ liệu mới ngoài BCTC | Mua/bán/stock action đúng số còn giữ; tiền cổ tức dự kiến khác thực nhận; giá thiếu không định giá0 |
| F06.4 — hiệu quả | Ledger nộp/rút, valuations theo ngày, dividend/fee, benchmark và basis | Chọn TWR hoặc MWR theo câu hỏi; ghi policy ngày/dòng tiền; đồ thị và báo cáo | Khó hơn holdings; không lấy trực tiếp NAV delta làm return | Nộp thêm tiền không tạo lợi nhuận; benchmark cùng cơ sở cổ tức; thiếu giá/dòng tiền được nêu |
| F07.1/.2 — giả định dòng tiền | G02 đã duyệt + overrides người dùng + bản gốc | Tách scenario_inputs khỏi financial_facts; tính bằng cùng registry; so/lưu giả định | Cao sau G02; không cần mô hình ML | CFO120→150 đổi số dư−20→10, facts gốc không đổi; biết ô nào là giả định |
| F07.3/.4 — DCF/DDM/độ nhạy | FCFF/FCFE/DPS phù hợp; dự phóng, discount, g, nợ vay, tiền, shares | Chọn một mô hình; bảng assumptions và công thức; ma trận một–hai biến | Vừa về tính toán, khó về đầu vào/diễn giải; chưa thuộc MVP | Chặn r≤g; không dùng nợ phải trả thay nợ vay; lặp lại kết quả từ assumptions lưu |

**Common-size** là quy mỗi dòng về tỷ trọng trên mẫu số được chọn, chẳng hạn tài sản/tổng tài sản hoặc chi phí/doanh thu. **DuPont** phân rã ROE; không tự cho biết nguyên nhân kinh tế đã được chứng minh. **TWR/MWR** là hai cách đo hiệu quả khi có dòng tiền vào/ra; chọn theo mục đích, giải thích cho người dùng bằng tiếng Việt. Định nghĩa cụ thể sẽ là phần đặc tả trước triển khai.

## 3. Tổ chức dữ liệu để các UC không thành nhiều màn hình rời

1. **Dữ liệu lõi:** company, reporting_period, financial_fact, metric_definition, source/revision, coverage. Mỗi fact có kỳ, scope, đơn vị, trạng thái và bằng chứng.
2. **Lần phân tích:** companies/periods/metrics/view settings, snapshot_id, formula_version, notes/tasks. Không còn criteria/pass/fail của chức năng sàng lọc.
3. **Theo dõi:** watchlist và disclosure/event với published_at, observed_at, date_type, revision/status. Danh sách tự chọn không cần transaction/position.
4. **Mở rộng khi chọn UC-F06:** account, transaction, position/lot, cash_flow, price, entitlement, income_payment. Phải kiểm liên kết với sự kiện cổ phiếu; không dùng financial_fact thay transaction.
5. **Mở rộng khi chọn UC-F07:** scenario và assumption_override trỏ tới snapshot gốc, model/version, output. Không sửa dữ liệu lịch sử bằng giả định.

Tên thực thể là đề xuất thiết kế. Không cần tạo toàn bộ schema ngay; thêm theo lát cắt được chọn. Kết quả bảng/biểu đồ dùng chung một dataset đã kiểm điều kiện và registry; nguồn thiếu thì hiển thị trạng thái cho chính phần phụ thuộc.

## 4. Thứ tự thực hiện để có sản phẩm sử dụng được

| Đợt đề xuất | Lát cắt hoàn chỉnh | Kết quả cần chứng minh trước chuyển tiếp |
|---|---|---|
| 1 — khai thác/phân tích/so sánh | Hai công ty, ba năm → bảng chuẩn → biểu đồ lợi nhuận/CFO → tỷ số → tra cứu nguồn → lưu/xuất | Số/đơn vị/scope đúng, thiếu không0, bản lưu mở lại đúng; có walkthrough |
| 2 — đào sâu tài chính/cổ tức | Thêm doanh thu và một ca cầu nối/G02/G03 → biểu đồ biên/phân rã → lịch sử cổ tức → câu hỏi có bằng chứng | Đủ operands/nguồn; phép tính và residual đúng; giải thích được basis và giới hạn |
| 3 — theo dõi liên tục | Watchlist → công bố/bản sửa → trước/sau → mở lần phân tích cũ → lập bản mới | Đúng nguồn/ngày/revision; không ghi đè nhận xét và dữ liệu cũ |
| 4 — chọn một nhánh sau pilot | DuPont, quý/kế hoạch, benchmark ngành hoặc kịch bản dòng tiền | Có mẫu dữ liệu cần thiết và nhu cầu được thử; ghi change record cho nhánh chọn |
| 5 — nếu còn phạm vi/công sức | Danh mục hoặc DCF/DDM, không bắt buộc cả hai | Hoàn thành ledger/nguồn giá hoặc định nghĩa đầu vào mô hình trước UI |

Chưa có căn cứ để ước lượng chính xác giờ cho mọi nhánh. Dự toán cũ **167 giờ** là baseline; **64–98 giờ** của CR-DIV-02 là dự toán trước khi rút phần sàng lọc, cần tính lại khi chọn phạm vi mới. Không trừ giờ máy móc hoặc gán một mốc hoàn thành mới khi chưa đo nhập/duyệt nguồn và chưa chọn số chức năng.

Để lập dự toán nhanh, triển khai một doanh nghiệp/một kỳ của nhóm dữ liệu mới, ghi thời gian thu–mapping–duyệt–xây đầu ra–kiểm chứng, rồi ước lượng phần cố định và phần theo báo cáo. Khi báo cáo với thầy, trình bày UC nhỏ bằng đầu vào → bước xử lý → đầu ra → minh chứng chạy được; ghi rõ phần nào mới là đề xuất.

## 5. Đo giá trị bằng tác vụ người dùng

| Tác vụ | Đối chiếu đúng/sai | Giá trị quan sát |
|---|---|---|
| Đọc A qua ba năm bằng bảng và biểu đồ | Đúng xu hướng/số thiếu/kỳ/đơn vị từ bộ đã duyệt | Thời gian và số lỗi so với tự tìm trong PDF/bảng |
| So A/B do người dùng chọn | Phân biệt CFO tuyệt đối và CFO/LNST; nhận ra scope không tương thích | Tỷ lệ hoàn thành, lỗi nhầm cơ sở, số lần phải tìm nguồn |
| Giải thích một thay đổi CFO | Đúng dòng đóng góp và residual; không tự suy nguyên nhân không có chứng cứ | Tìm được khoản cần đọc và nguồn của khoản ấy |
| Xem lại sau bản sửa | Xác định số trước/sau và giữ được phân tích cũ | Khả năng tiếp tục theo dõi thay vì làm lại từ đầu |
| Kiểm lịch sử cổ tức | Đúng profit_year, đủ/thiếu, basis; lịch chưa là thực nhận | Lỗi cộng trùng/nhầm năm/nhầm tiền nhận |

Đây là protocol đề xuất, chưa có kết quả người dùng. Kết luận thích hợp là giảm công sức, giảm sai sót đối chiếu và cải thiện khả năng kiểm chứng phân tích khi đã đo; không suy rằng lợi nhuận đầu tư tăng chỉ vì có biểu đồ hoặc tỷ số.

## 6. Tác động tới đặc tả hiện hành

CR-AN-03 tại [SRS mục18](../research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md) rút FR29/FR30/D09/D10 và TC22/TC-D09/TC-D10, sửa TC21 về bộ chọn/biểu đồ. D11/12 giữ lưu nhận xét/snapshot nhưng bỏ tiêu chí sàng lọc. Còn 91 yêu cầu và 51 tình huống dự kiến; không tái dùng mã đã rút.

UC-F01–05 là góc nhìn sản phẩm cho chức năng nền và ứng viên bổ sung. UC-F06/07 là hướng mở rộng. Trước khi tích hợp một phần mới: ghi mục đích người dùng, nguồn/mẫu dữ liệu, đầu vào/xử lý/đầu ra, ngoại lệ, tác vụ chấp nhận và dự toán. Không gọi danh mục nghiên cứu này là phạm vi tất cả chức năng đã chốt.

[Minh chứng nguồn](02-minh-chung-ma-va-bai-hoc.md) · [Khảo sát](01-khao-sat-repository.md) · [Yêu cầu dễ đọc](../research-platform/27-yeu-cau-chuc-nang-va-vi-du.md).
