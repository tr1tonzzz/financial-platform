# Các yêu cầu chức năng ứng viên rút ra từ GitHub

Ngày 11/10/2026. `G01–G10` là **mã nghiên cứu bổ sung**, chưa là FR mới của SRS. Nhu cầu có bằng chứng từ repository/phản hồi được ghi nguồn; tính hữu ích cho nhà đầu tư Việt Nam là giả thuyết cần thử. Mỗi đầu ra phải giữ `as_of`, kỳ, scope, đơn vị, coverage, source/version và lý do không tính được.

## G01 — Sàng lọc và lập hồ sơ thẩm định cổ tức

**Nhu cầu/quyết định:** trong các doanh nghiệp theo dõi, doanh nghiệp nào cần đọc trước và vấn đề nào cần kiểm tra? Nguồn ý tưởng: [Dividend CLI](https://github.com/Santhosh-004/dividend-cli), [bộ lọc nhiều điều kiện](https://github.com/aspirin188/dividend-low-vol-tracker/blob/7ca601f6bb3f9f3411bfce3f70b80a6708e93ea1/server/services/scorer.py#L179).

- **Đầu vào:** sáu financial facts đã duyệt, DPS theo năm lợi nhuận, coverage/basis và các điều kiện người dùng chọn. Chưa dùng yield/payout nếu thiếu dữ liệu tương ứng.
- **Xử lý:** kiểm đủ dữ liệu trước từng điều kiện; phân loại `đạt điều kiện`, `không đạt`, `chưa đủ cơ sở`. Tái dùng các ca LNST tăng/CFO giảm, cổ tức tăng/LNST hoặc CFO giảm; không tự đổi đó thành khuyến nghị mua/bán.
- **Đầu ra:** danh sách kết quả, lý do theo từng tiêu chí, thông tin thiếu, đường tới operands/nguồn và ghi chú thẩm định. Người dùng lưu bộ tiêu chí và snapshot để xem lại.
- **Ví dụ:** “CFO giảm hai năm trong khi DPS giữ nguyên; cần tra soát khoản biến động vốn lưu động và chi đầu tư”. Nếu một năm DPS partial thì không kết luận cổ tức cả năm giảm.
- **Chấp nhận:** dữ liệu thiếu không vượt điều kiện; mọi lý do truy được về phép tính; đổi tiêu chí cập nhật kết quả và lưu bộ tiêu chí; một doanh nghiệp có thể cần đọc sâu dù không được đưa vào danh sách đạt.
- **SRS:** FR25–29/31–32 và UC06 đã có nền. Mới ở hồ sơ tác vụ, lưu tiêu chí/ghi chú và trạng thái theo điều kiện; không tuyên bố bộ lọc cũ hoàn toàn là chức năng mới. Không thay nghĩa vụ các FR nền.

## G02 — Phân tích bao phủ chi đầu tư và cổ tức bằng tiền tạo ra từ kinh doanh

**Nhu cầu/quyết định:** cổ tức tiền mặt trong kỳ có nằm trong phần tiền tạo ra sau chi đầu tư, hay cần đọc thêm nguồn lực khác? Ý tưởng từ [FinanceToolkit](https://github.com/JerBouma/FinanceToolkit/blob/37ed6f01465b4bfb6718b07e1d65826734f53337/financetoolkit/ratios/solvency_model.py#L267). Câu hỏi về khả năng duy trì có căn cứ nghề nghiệp tại [CFA Institute](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/analysis-of-dividends-and-share-repurchases).

- **Đầu vào tối thiểu:** CFO; `capex_cash_outflow` là độ lớn khoản tiền chi mua/sắm/xây dựng tài sản được định nghĩa rõ; `cash_dividends_paid` là tiền cổ tức thực chi phù hợp cùng chủ thể/kỳ; cả ba đã duyệt và có nguồn. Nếu dòng nguồn gộp “cổ tức, lợi nhuận đã trả” chưa tách được, lưu đúng nhãn gộp và không đổi thành cổ tức phổ thông.
- **Xử lý:** `cash_after_capex = CFO − CAPEX`; `cash_after_capex_and_dividends = CFO − CAPEX − D`; `coverage = CFO / (CAPEX + D)` khi CAPEX,D không âm và tổng >0. Dòng chi trong PDF có dấu âm được chuẩn hóa thành độ lớn sau xác minh ý nghĩa. Không dùng `abs` để che lỗi mapping.
- **Đầu ra:** bảng phân bổ CFO, số dư và tỷ số; nêu “CFO kỳ này chưa bao phủ hai khoản chi” nếu số dư âm. Hiện tiền đầu kỳ/cuối kỳ và vay khi có dữ liệu phù hợp để định hướng tra soát; không quy kết nguồn tài trợ chỉ bằng tương quan.
- **Ví dụ giả lập đã tính:** A có LNST=100, CFO=120, CAPEX=80, D=60; CFO/LNST=1,2 nhưng bao phủ=0,857 và số dư=−20. B có LNST=100, CFO=95, CAPEX=20, D=40; CFO/LNST=0,95 nhưng bao phủ=1,583 và số dư=35. Một tỷ số chuyển lợi nhuận thành tiền không đủ để đánh giá phân phối.
- **Chấp nhận:** thiếu một dòng → không tính; denominator=0 → không áp dụng; CFO âm giữ dấu âm; scope/kỳ lệch bị chặn; thông báo DPS không thay D thực chi; nguồn gộp có nhãn riêng. Chênh lệch âm không sinh nhãn “sắp cắt cổ tức” hay “vay trả cổ tức”.
- **SRS:** mở E10 có điều kiện và thêm CAPEX; cần change record/dictionary/test mới. Sáu chỉ tiêu chưa đủ. Chỉ nên triển khai một ca đọc/duyệt thủ công trước để kiểm công sức.

**Giới hạn:** không gọi `CFO−CAPEX` là FCFE; chưa bao quát nghĩa vụ nợ đến hạn, quỹ tiền mặt tích lũy, cấu trúc công ty mẹ/con hay chất lượng khoản chi đầu tư. Có thể trả cổ tức từ nguồn tích lũy dù CFO kỳ này thiếu; có thể cần giữ tiền dù tỷ số bao phủ >1.

## G03 — Tra soát lịch sử cổ tức khi cơ sở cổ phiếu thay đổi

**Nhu cầu/quyết định:** DPS giảm là chính sách tiền mặt giảm, hay do số cổ phiếu tăng? Nguồn: [Dividend CLI adjustment](https://github.com/Santhosh-004/dividend-cli/blob/7c6033b11db694eb101d2b27217441c7184e9c4f/dividend_calculator/utils.py#L173), [OpenBB split schema](https://github.com/OpenBB-finance/OpenBB/blob/ae0268771f761b036996d81bd21522ce79d95415/openbb_platform/core/openbb_core/provider/standard_models/historical_splits.py).

- **Đầu vào:** DPS nguyên bản; loại/tỷ lệ/ngày hiệu lực/trạng thái sự kiện cổ phiếu; thứ tự ngày quyền; phương pháp điều chỉnh của nguồn; phạm vi vị thế mô phỏng.
- **Xử lý:** xác định chuỗi so sánh được, giữ raw; tạo DPS quy về một cơ sở cố định hoặc khoản thu trên vị thế gốc, ghi rõ cơ sở. Không điều chỉnh hai lần dữ liệu provider đã adjusted. Chỉ xử lý loại sự kiện đã có quy tắc; quyền mua/ESOP không áp dụng như stock split.
- **Đầu ra:** đồ thị gốc và quy đổi với nhãn; bảng tác động số lượng cổ phiếu; lời giải thích và chứng từ. Thiếu tỷ lệ/hiệu lực → chuỗi bị chặn so sánh qua điểm đó.
- **Ví dụ giả lập:** 100 cổ phiếu ×1.000 đồng =100.000 đồng; sau cổ tức cổ phiếu 20%, giả sử 120 cổ phiếu đều có quyền ở lần tiền mặt sau, ×900=108.000 đồng. DPS gốc giảm 10% nhưng khoản thu của vị thế gốc tăng 8%.
- **Chấp nhận:** ca không sự kiện không đổi; ca nhiều sự kiện cộng dồn đúng; ngày quyền trùng cần quy tắc chứng minh hoặc báo chưa xử lý; hủy sự kiện không còn làm tăng cổ phiếu; chưa xác định quyền không báo thực nhận; không tự chia lại EPS đã được doanh nghiệp hồi tố.
- **SRS:** làm sâu FR28/basis nhưng thêm ledger corporate actions là mở rộng dữ liệu. Luận chứng “chỉ phân tích tiền mặt” vẫn giữ được nếu sự kiện cổ phiếu được dùng để kiểm cơ sở, không cộng tỷ lệ cổ phiếu vào tiền thu.

## G04 — So sánh hồ sơ cổ tức của các doanh nghiệp

**Nhu cầu/quyết định:** giữa hai ứng viên có lịch sử cổ tức tương tự, điểm nào cần thẩm định khác nhau? Nguồn: [FinanceToolkit ratios](https://github.com/JerBouma/FinanceToolkit), [notebook so ngành](https://github.com/hsteffens/dividend_analysis/blob/53469d0da4127402f500af5ef5ea6c8a44a5ce9c/Analytic%20Dividend%20Analysis.ipynb).

- **Đầu vào:** tập doanh nghiệp chọn, năm/scope/basis tương thích; LNST/CFO/DPS và các chỉ tiêu G02 khi đủ; ngành là metadata mới nếu dùng.
- **Xử lý:** đối chiếu từng chiều, giữ số liệu và tỷ số, giải thích mốc thời gian; không so quy mô bằng số tuyệt đối để tự kết luận chất lượng; không lấy trung bình ngành điền thiếu.
- **Đầu ra:** bảng 2–3 doanh nghiệp có điểm mạnh, vấn đề cần đọc, mức đủ dữ liệu; người dùng thấy trade-off thay vì “mã tốt nhất”.
- **Chấp nhận:** ô không hợp lệ có lý do; không có điểm tổng nếu chưa chốt/kiểm định trọng số; nhóm 3 công ty không gọi benchmark toàn ngành; thay as_of phải cập nhật đồng bộ cả hai phía.
- **SRS:** UC06/FR32 có nền; thao tác so song song và tổng hợp luận điểm là bổ sung nhỏ. Dữ liệu ngành và benchmark lớn là phần mới riêng.

## G05 — Ước tính khoản thu và lịch cổ tức theo quyền đã công bố

**Nhu cầu/quyết định:** dự kiến nhận bao nhiêu, từ doanh nghiệp nào, vào mốc nào? Dấu vết nhu cầu: [Ghostfolio Discussion #5867](https://github.com/ghostfolio/ghostfolio/discussions/5867); cách triển khai tham khảo [SALARY income](https://github.com/GavrielP1/SALARY-2045/blob/806cdaa821c7a4eb04a0f1bc7cf59c0a30314e0a/app.py#L1159), [OpenBB calendar](https://github.com/OpenBB-finance/OpenBB/blob/ae0268771f761b036996d81bd21522ce79d95415/openbb_platform/core/openbb_core/provider/standard_models/calendar_dividend.py#L26).

- **Đầu vào:** notice đã duyệt, DPS, ngày quyền/thanh toán và hiệu lực; số cổ phiếu đủ điều kiện người dùng xác nhận hoặc vị thế mô phỏng có ghi giả định.
- **Xử lý:** khoản gộp dự kiến = số cổ phiếu có quyền × DPS; tổng theo tháng thanh toán dự kiến và theo doanh nghiệp; giữ bảng theo năm lợi nhuận riêng. Nếu chưa có vị thế lịch sử thì không tự nhận số nắm giữ hiện tại là số có quyền.
- **Đầu ra:** lịch khoản thu **đã công bố/dự kiến**, thay lịch/hủy quyền, total và nguồn; phần dự báo theo lịch sử phải nằm ở góc nhìn giả định khác.
- **Chấp nhận:** chưa có ngày trả thì vào nhóm chưa rõ lịch; hủy/sửa không tính trùng; notice chứa hai profit_year vẫn chỉ một khoản thu theo sự kiện; không tự giả định mọi mã trả quý hoặc lặp lần trả gần nhất; không báo “đã nhận” từ lịch.
- **SRS:** UC05/FR21–24/E07 giữ nền; phép nhân với vị thế là chức năng mới, cần dữ liệu người dùng. Nên để sau G02/G03 hoặc làm demo mô phỏng nhỏ.

## G06 — Đánh giá mức tập trung thu nhập cổ tức

**Nhu cầu/quyết định:** nguồn thu phụ thuộc quá nhiều vào một doanh nghiệp/ngành không? Nguồn mẫu: [Ghostfolio rule về tỷ trọng tập trung](https://github.com/ghostfolio/ghostfolio/blob/8fa4f6a6739afee82461b3aa48f47dfa6a396dc8/apps/api/src/models/rules/account-cluster-risk/current-investment.ts#L33); việc chuyển từ vốn sang thu nhập là đề nghị mới của FAP.

- **Đầu vào:** khoản thu G05 trên cùng cửa sổ/trạng thái/currency, doanh nghiệp và ngành; phần chưa rõ phải tách.
- **Xử lý:** `income_weight_i = income_i / total_income`; tổng>0. Nếu người dùng đặt ngưỡng tập trung thì diễn giải là tiêu chí của họ, không chuẩn an toàn chung.
- **Đầu ra:** tỷ trọng theo doanh nghiệp/ngành và tác động giảm cổ tức của nguồn lớn nhất. Tập trung thu nhập khác tập trung vốn; ghi đúng cơ sở.
- **Ví dụ giả lập:** A cung cấp 75% thu nhập, B 25%; A giảm 50% thì thu nhập tổng giảm 37,5% trong kịch bản các khoản khác giữ nguyên.
- **Chấp nhận:** tổng bằng 0 không có tỷ trọng; khoản chưa rõ không bị bỏ rồi trình bày phần còn lại như toàn danh mục; không suy chỉ hai mã là danh mục đủ đa dạng.
- **SRS:** mới, phụ thuộc G05 và dữ liệu vị thế/ngành. Trì hoãn trong MVP nền.

## G07 — Theo dõi thay đổi ảnh hưởng tới hồ sơ thẩm định

**Nhu cầu/quyết định:** sau khi đã đọc một doanh nghiệp, thông tin mới có làm nhận định cũ cần kiểm tra lại không? Nguồn mẫu: quy tắc diễn giải trong [Ghostfolio](https://github.com/ghostfolio/ghostfolio/blob/8fa4f6a6739afee82461b3aa48f47dfa6a396dc8/apps/api/src/models/rule.ts); cơ chế impact dưới đây là suy luận thiết kế, chưa xác nhận có cùng chức năng trong repo.

- **Đầu vào:** danh sách theo dõi, tiêu chí/ghi chú, snapshot cũ/mới, operands và notice versions.
- **Xử lý:** đối chiếu dữ kiện thay đổi; tính lại kết quả phụ thuộc; phân biệt thay nội dung phân tích với thay hash/bố cục; tạo việc cần tra soát.
- **Đầu ra:** hộp thay đổi trong ứng dụng: “DPS năm X được điều chỉnh → đánh giá lịch sử bị ảnh hưởng”, số trước/sau, nguồn và lý do. Chưa gửi thông báo bên ngoài trong đề xuất này.
- **Chấp nhận:** layout-only không tạo cảnh báo chỉ tiêu; replay snapshot cũ giữ kết quả cũ; xuất hiện/hết trạng thái thiếu cũng là thay đổi giải thích được.
- **SRS:** nền FR18/35 và versions; impact-to-case engine mới. Phù hợp hướng đồ án tiếp nối, chưa ưu tiên đợt đầu.

## G08 — Tra soát nguyên nhân tỷ suất cổ tức cao

**Nhu cầu/quyết định:** yield cao vì tiền cổ tức tăng hay vì giá giảm/khoản bất thường? Nguồn: [dividend_analysis](https://github.com/hsteffens/dividend_analysis), [Dividend CLI yield helper](https://github.com/Santhosh-004/dividend-cli/blob/7c6033b11db694eb101d2b27217441c7184e9c4f/dividend_calculator/utils.py#L15).

- **Đầu vào:** giá tại ngày định giá, DPS trailing hoặc forward với định nghĩa cửa sổ rõ, corporate actions, regular/special nếu chứng cứ có.
- **Xử lý:** tính riêng trailing yield và yield theo khoản công bố; đối chiếu biến động giá/DPS cùng cơ sở; phân rã yếu tố, không gọi high yield tự động là bẫy.
- **Đầu ra:** “yield tăng do giá giảm trong khi DPS chưa đổi”, nguồn ngày giá, mức cổ tức và phần bất thường.
- **Ví dụ giả lập:** DPS=1.000; giá 20.000→10.000; yield 5%→10%, tiền cổ tức không tăng. Không suy mua ở giá thấp đó có lợi hơn nếu chưa thẩm định doanh nghiệp.
- **Chấp nhận:** giá≤0 không tính; tỷ lệ trên mệnh giá không dùng làm yield; giá/DPS đã điều chỉnh khác basis bị chặn; lịch dự kiến không trộn trailing paid.
- **SRS:** mới, cần giá và định nghĩa yield; nằm ngoài nền hiện tại. Chưa làm trước G02/G03.

## G09 — Kịch bản sức chịu đựng của dòng tiền cổ tức

**Nhu cầu/quyết định:** nếu tiền kinh doanh giảm hoặc chi đầu tư tăng, biên dòng tiền thay đổi thế nào? Nguồn mẫu: [SALARY dự kiến thu nhập](https://github.com/GavrielP1/SALARY-2045); phiên bản FAP tập trung phép tính điều kiện, chưa dự báo xác suất.

- **Đầu vào:** ca G02 đã duyệt; người dùng chọn thay đổi CFO/CAPEX/D và mục tiêu dư tiền.
- **Xử lý:** tính số dư theo kịch bản; lưu baseline/giả định; giải thích yếu tố làm thay đổi. Không tự ước lượng tốc độ tăng trưởng hay khuyến nghị mức cổ tức hợp pháp.
- **Đầu ra:** bảng baseline/giảm CFO/tăng CAPEX và mức chênh; nguồn baseline, giả định mới, giới hạn.
- **Chấp nhận:** giả định 0 tái lập baseline; thay CFO không sửa dữ liệu lịch sử; dòng tiền thiếu không có mô phỏng giả như dữ liệu thật.
- **SRS:** mới, làm sau khi G02 có dữ liệu tin cậy. Giá trị chủ yếu giúp hiểu độ nhạy, chưa là đánh giá chiến lược hay mô hình dự báo.

## G10 — Đối soát cổ tức công bố với tiền thực nhận

**Nhu cầu/quyết định:** khoản dự kiến đã về tài khoản chưa, chênh do quyền, phí/thuế hay dữ liệu? Nguồn nghiệp vụ: [Portfolio Performance dividend manual](https://help.portfolio-performance.info/en/reference/transaction/dividend/), [Ghostfolio Issue #2126](https://github.com/ghostfolio/ghostfolio/issues/2126).

- **Đầu vào:** G05, sao kê/ghi nhận người dùng, số có quyền, gross/fee/tax/net và tài khoản.
- **Xử lý:** ghép payment với entitlement, so gộp/ròng có chứng cứ, giữ một-to-many khi nhiều tài khoản/lần thanh toán; chưa biết nguyên nhân không tự gán thuế.
- **Đầu ra:** đã khớp/chênh/chưa nhận hoặc chưa có chứng cứ, ngày thực nhận, nguồn xác nhận.
- **Chấp nhận:** chuyển nhiều tài khoản không gộp mất định danh; sửa lịch không ghi đè actual; tổng net khác gross được giải thích bằng các khoản có nguồn; chưa áp dụng tỷ lệ thuế mặc định.
- **SRS:** khác FR22 chứng cứ doanh nghiệp thực chi; cần dữ liệu cá nhân/sổ tài khoản. Nên làm nhánh riêng sau MVP, không kéo scope nền vào quản lý danh mục đầy đủ.

## Dữ liệu bổ sung theo chức năng

| Lớp dữ liệu | Có nền trong FAP | Phần mới cần xác minh | UC sử dụng |
|---|---|---|---|
| Financial facts + provenance | Sáu facts, scope/kỳ/version, cầu nối theo ca | CAPEX, dòng tiền cổ tức đúng nghĩa, nợ vay/lãi nếu mở | G01/G02/G04/G09 |
| Dividend events | Components profit_year, timeline, lifecycle và coverage theo thiết kế | Xác nhận thực chi đủ chi tiết; phân loại regular/special nếu làm | G01/G02/G05/G08 |
| Corporate actions | Basis comparability trong thiết kế | Ledger loại/tỷ lệ/hiệu lực/ngày quyền, raw/adjusted method | G03/G08 |
| Người dùng | Chưa thấy sổ vị thế/giao dịch hoàn chỉnh | Vị thế đủ điều kiện hoặc mô phỏng, mục tiêu và tiêu chí | G01/G05/G06/G10 |
| Market/reference | Issuer IDs | Giá tại as_of, ngành, historical basis | G04/G06/G08 |
| Impact/workflow | Versions, snapshots, audit | Kết quả phụ thuộc, ghi chú thẩm định và danh sách theo dõi | G01/G07 |

Hành vi bất biến: không quy thiếu thành 0, không trộn năm lợi nhuận và năm thanh toán, không suy công bố là đã trả, không dùng nợ phải trả như nợ vay, không suy hợp nhất thành quyền phân phối của mẹ. Mỗi UC chỉ kích hoạt khi đầu vào đủ nghĩa và chất lượng.
