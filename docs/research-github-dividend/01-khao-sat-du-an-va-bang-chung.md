# Khảo sát dự án và bằng chứng từ mã

Ngày đọc: 11/10/2026. Mã được chụp theo commit trong [sổ nguồn](sources.md); đường dẫn bên dưới là nguồn chính. Phân loại **README** là tuyên bố chức năng, **mã** là hành vi quan sát qua đọc, **test** là kiểm tra được tác giả viết nhưng chưa chạy tại FAP, **phản hồi** là nhu cầu/lỗi được người dùng thuật lại. Không coi bốn mức đó tương đương nghiệm thu thực tế.

## 1. JerBouma/FinanceToolkit — bao phủ dòng tiền và công thức minh bạch

Commit `37ed6f0`; MIT theo metadata GitHub. [Repository](https://github.com/JerBouma/FinanceToolkit).

**Nhu cầu:** người đọc muốn hiểu phép tính chỉ tiêu và đối chiếu khả năng tạo tiền với các khoản sử dụng tiền. **Mã:** `get_capex_coverage_ratio` lấy CFO / |CAPEX|; `get_dividend_capex_coverage_ratio` lấy CFO / (|CAPEX| + |dividends|). `get_dividend_payout_ratio` lấy |dividends| / net income. [Solvency model, dòng 246–288](https://github.com/JerBouma/FinanceToolkit/blob/37ed6f01465b4bfb6718b07e1d65826734f53337/financetoolkit/ratios/solvency_model.py#L246), [valuation model, dòng 437](https://github.com/JerBouma/FinanceToolkit/blob/37ed6f01465b4bfb6718b07e1d65826734f53337/financetoolkit/ratios/valuation_model.py#L437).

**Test đã đọc:** có test gọi tỷ số bao phủ trên dãy CFO/CAPEX/dividends, dùng recorder; chưa chạy và chưa đánh giá độ bao phủ test. [Test](https://github.com/JerBouma/FinanceToolkit/blob/37ed6f01465b4bfb6718b07e1d65826734f53337/tests/ratios/test_solvency_model.py#L83).

**Ứng dụng cho FAP:** G02 phân tích bao phủ và số dư sau các khoản chi; G04 so sánh doanh nghiệp trên cùng cơ sở. Cần thêm CAPEX tiền mặt và dòng cổ tức thực chi phù hợp. Các hàm mô hình được đọc không tự kiểm phạm vi báo cáo, năm lợi nhuận cổ tức, zero/âm/thiếu; FAP phải kiểm trước tính. Không biến `abs` thành quy tắc sửa mọi dấu nguồn hoặc gọi số dư sau CAPEX là FCFE.

## 2. Santhosh-004/dividend-cli — lịch sử cổ tức có cơ sở cổ phiếu

Commit `7c6033b`; MIT. [Repository](https://github.com/Santhosh-004/dividend-cli).

**Nhu cầu:** cổ tức có tăng thật không, lịch sử có bị chia tách làm khó hiểu không, và mã nào phù hợp tiêu chí lịch sử? **Mã:** `adjust_dividends` lưu giá trị raw và khoản thu quy về một cổ phiếu gốc, dùng các tỷ lệ split trước/sau ngày sự kiện; `classify_years` phân loại tăng/giữ/giảm/dừng; `dividend_quality_score` dùng trọng số lịch sử do tác giả chọn. [Utils](https://github.com/Santhosh-004/dividend-cli/blob/7c6033b11db694eb101d2b27217441c7184e9c4f/dividend_calculator/utils.py#L173), [schema split](https://github.com/Santhosh-004/dividend-cli/blob/7c6033b11db694eb101d2b27217441c7184e9c4f/dividend_calculator/db.py#L58).

**Test đã đọc:** tăng trưởng, phân loại năm và score; ca giá 0/yield 0 cũng được chấp nhận trong test nguồn. [Test utils](https://github.com/Santhosh-004/dividend-cli/blob/7c6033b11db694eb101d2b27217441c7184e9c4f/tests/test_utils.py).

**Ứng dụng:** G03 giữ DPS gốc/cơ sở điều chỉnh, G01 bộ lọc. **Điều chỉnh bắt buộc:** mã giả định dữ liệu Yahoo đã điều chỉnh ngược; PDF/VSDC là cơ sở khác, không áp dụng bước hoàn nguyên nếu đầu vào đã raw. Split không đồng nghĩa mọi cổ tức bằng cổ phiếu/quyền mua. Việc điền năm trống bằng 0 trong helper CAGR phải thay bằng coverage của FAP. Chấm lịch sử không chứng minh khả năng duy trì cổ tức tương lai.

## 3. aspirin188/dividend-low-vol-tracker — sàng lọc nhiều điều kiện

Commit `7ca601f`; metadata không thấy giấy phép, inventory không có tệp license. [Repository](https://github.com/aspirin188/dividend-low-vol-tracker).

**Nhu cầu:** thu hẹp tập cổ phiếu để đọc sâu theo cổ tức, lợi nhuận, ROE, nợ và biến động. **Mã:** `filter_stocks` lấy tham số cấu hình; `calculate_scores` ghép các yếu tố; các nhánh kiểm riêng cho tăng trưởng, chất lượng CFO và nợ. [Scorer](https://github.com/aspirin188/dividend-low-vol-tracker/blob/7ca601f6bb3f9f3411bfce3f70b80a6708e93ea1/server/services/scorer.py#L179).

**Phát hiện:** docstring nói loại dữ liệu không đầy đủ, nhưng tại dòng 274, 304 và 325, một số chỉ tiêu thiếu được cho qua. Đây là khác biệt giữa mô tả và nhánh mã, không khẳng định mọi lọc đều cho qua hay ứng dụng không hoạt động. [Nhánh thiếu](https://github.com/aspirin188/dividend-low-vol-tracker/blob/7ca601f6bb3f9f3411bfce3f70b80a6708e93ea1/server/services/scorer.py#L271). Đã đọc một số ca dữ liệu giả trong `test_scorer.py`; chưa chạy.

**Ứng dụng:** G01 lưu tiêu chí và lý do từng doanh nghiệp đạt/không đạt/chưa đủ cơ sở. Học cách chia điều kiện và cấu hình; chưa dùng ngưỡng thị trường Trung Quốc hoặc điểm đa yếu tố như chuẩn đầu tư Việt Nam. Không dùng toàn bộ total_liabilities thay cho debt.

## 4. GavrielP1/SALARY-2045 — mục tiêu thu nhập và lịch dự kiến

Commit `806cdaa`; MIT. [Repository](https://github.com/GavrielP1/SALARY-2045).

**Nhu cầu:** từng khoản nắm giữ tạo bao nhiêu tiền, tháng nào nhận, gần mục tiêu thu nhập đến đâu? README có overview, holdings, calendar, goals và stock deep-dive. **Mã:** `/api/income` kéo dài chu kỳ từ lịch sử lần trả gần nhất và tần suất, nhân với số cổ phiếu; `_safety_score` có trọng số cố định nhưng bỏ yếu tố thiếu và phân bổ lại trọng số. [Income](https://github.com/GavrielP1/SALARY-2045/blob/806cdaa821c7a4eb04a0f1bc7cf59c0a30314e0a/app.py#L1159), [score](https://github.com/GavrielP1/SALARY-2045/blob/806cdaa821c7a4eb04a0f1bc7cf59c0a30314e0a/app.py#L258).

**Ứng dụng:** G05 khoản thu theo quyền đã công bố; G06 mức tập trung thu nhập; G09 kịch bản giảm cổ tức. **Điều chỉnh:** số cổ phiếu hiện tại không luôn là số có quyền, lịch lặp không phải thông báo trả, và thiếu FCF/nợ không nên làm điểm nhìn cao hơn. Điểm payout và EPS/annual dividend còn có thể phản ánh cùng một quan hệ, cần kiểm nguy cơ tính trùng nếu nghiên cứu score. Không kế thừa phép cộng dividend rate hiện tại vào price return như tổng mức sinh lời đã thực hiện.

## 5. ghostfolio/ghostfolio — danh mục, thu nhập và quy tắc giải thích được

Commit `8fa4f6a`; AGPL-3.0 theo GitHub. [Repository](https://github.com/ghostfolio/ghostfolio).

**Mã:** `getDividends` nhận activities và groupBy; quy tắc tập trung theo tài khoản tìm tỷ trọng lớn nhất và trả diễn giải với ngưỡng cấu hình. [Dividend service](https://github.com/ghostfolio/ghostfolio/blob/8fa4f6a6739afee82461b3aa48f47dfa6a396dc8/apps/api/src/app/portfolio/portfolio.service.ts#L458), [rule](https://github.com/ghostfolio/ghostfolio/blob/8fa4f6a6739afee82461b3aa48f47dfa6a396dc8/apps/api/src/models/rules/account-cluster-risk/current-investment.ts#L33).

**Phản hồi:** Discussion #5867 muốn chi tiết nguồn thu/ngày/năm; Issue #2126 thuật lại nhầm ngày và ghép tài khoản ở phiên bản 1.286.0. [Discussion](https://github.com/ghostfolio/ghostfolio/discussions/5867), [issue](https://github.com/ghostfolio/ghostfolio/issues/2126).

**Ứng dụng:** G05, G06 và G07. Quy tắc hiện đọc là tập trung giá trị theo tài khoản; đề nghị tập trung **thu nhập cổ tức theo doanh nghiệp/ngành** là suy luận mới cho FAP, chưa phải tính năng đã xác nhận trong code đó. Danh sách theo dõi phân tích nhẹ có thể làm trước sổ giao dịch đầy đủ. Phản hồi lịch sử không xác nhận lỗi còn ở commit hiện tại.

## 6. portfolio-performance/portfolio — thực nhận và hiệu suất

Commit `b09410e`; EPL-1.0 theo metadata. [Repository](https://github.com/portfolio-performance/portfolio).

**Tài liệu nghiệp vụ:** giao dịch cổ tức tách số cổ phiếu, gross, phí, thuế và tiền ghi có; ex-date khác ngày giao dịch nhận tiền. [Manual chính thức](https://help.portfolio-performance.info/en/reference/transaction/dividend/).

**Test đã đọc:** `Issue1897AddFeesToDividendTransactionsTest` kiểm đơn vị fee/tax và snapshot; `Issue1879...MultipleAccountsTest` kiểm kết quả khi chứng khoán ở nhiều tài khoản. Hai PR lịch sử liên quan có nguồn phản hồi/test: [PR 1897](https://github.com/portfolio-performance/portfolio/pull/1897), [PR 1879](https://github.com/portfolio-performance/portfolio/pull/1879), [test fee](https://github.com/portfolio-performance/portfolio/blob/b09410e06ed3153e3ab256ffe579f97511adbf3d/name.abuchen.portfolio.tests/src/issues/Issue1897AddFeesToDividendTransactionsTest.java#L51).

**Ứng dụng:** G10 đối soát công bố–dự kiến–thực nhận, báo riêng khoản gộp/ròng. Giá trị thực tế cao nhưng cần dữ liệu người dùng và sổ giao dịch. Không nên kéo FAP thành ứng dụng kế toán danh mục ngay trong đợt bổ sung này. Không sao chép quy tắc thuế nước ngoài sang Việt Nam.

## 7. OpenBB-finance/OpenBB — hợp đồng dữ liệu lịch cổ tức

Commit `ae02687`; GitHub license `NOASSERTION`, chưa phân loại đầy đủ giấy phép các module. [Repository](https://github.com/OpenBB-finance/OpenBB).

**Mã đọc:** model lịch có ex_dividend_date, record_date, payment_date, declaration_date và amount có thể thiếu; historical model nhỏ hơn, có ex-date và amount; split model có numerator/denominator. [Calendar](https://github.com/OpenBB-finance/OpenBB/blob/ae0268771f761b036996d81bd21522ce79d95415/openbb_platform/core/openbb_core/provider/standard_models/calendar_dividend.py#L26), [history](https://github.com/OpenBB-finance/OpenBB/blob/ae0268771f761b036996d81bd21522ce79d95415/openbb_platform/core/openbb_core/provider/standard_models/historical_dividends.py#L33).

**Ứng dụng:** G03 và G05 lưu các mốc riêng, không sử dụng một `date` cho mọi ý nghĩa. Model không đủ để suy API/provider nào có đủ ngày, dữ liệu Việt Nam hoặc đã thực chi. FAP còn cần profit_year components, hiệu lực bản sửa và xác nhận thanh toán; chưa thấy các trường này trong hai model vừa đọc. Đây là nhận định có giới hạn về model đã đọc, không về toàn nền tảng.

## 8. thinh-vu/vnstock — nguồn dữ liệu Việt Nam để đối chiếu

Commit `88825be`; source-available với giấy phép riêng theo README/LICENSE.md, không gọi là MIT hoặc OSI open source. [Repository](https://github.com/thinh-vu/vnstock), [license tại commit](https://github.com/thinh-vu/vnstock/blob/88825be3f9aab729362e6fca178eb6e9ae4d3f88/LICENSE.md).

**Mã:** giao diện có income_statement, balance_sheet, cash_flow và ratio; implementation VCI xử lý các báo cáo. [Equity fundamental](https://github.com/thinh-vu/vnstock/blob/88825be3f9aab729362e6fca178eb6e9ae4d3f88/vnstock/ui/domains/fundamental/equity.py#L69), [financial](https://github.com/thinh-vu/vnstock/blob/88825be3f9aab729362e6fca178eb6e9ae4d3f88/vnstock/explorer/vci/financial.py#L519).

**Ứng dụng:** khảo sát khả năng thu CAPEX/dividend-paid/EPS/ngành và đối chiếu PDF đã duyệt. Chưa thực gọi API để xác nhận các trường đó đủ cho pilot. Nhánh `dropna` có `fillna(0)`; cần giữ raw/metadata và kiểm phương án lấy thiếu đúng nghĩa. Dữ liệu provider chuẩn hóa không mặc định có locator tới trang PDF hoặc provenance bằng chứng pháp lý. Không đổi nguồn chuẩn FAP chỉ vì một API thuận tiện hơn.

## 9. hsteffens/dividend_analysis — notebook yield–payout theo ngành

Commit `53469d0`; Apache-2.0. [Repository](https://github.com/hsteffens/dividend_analysis).

**Nhu cầu/phương pháp:** phân tích cổ phiếu NASDAQ có cổ tức trong 2023 bằng yield và payout; thống kê/biểu đồ và so sánh theo ngành. **Mã notebook đã đọc:** cell 27 điền thiếu bằng trung bình ngành, cell 35 gọi cách đó cho yield/payout; cell 63 xếp `DividendYield` và `PayoutRatio` cùng chiều giảm dần. [Notebook](https://github.com/hsteffens/dividend_analysis/blob/53469d0da4127402f500af5ef5ea6c8a44a5ce9c/Analytic%20Dividend%20Analysis.ipynb).

**Ứng dụng:** G04 so sánh nhiều chiều và G08 tra soát cổ tức cao. Không kế thừa việc gọi top yield/payout là hấp dẫn, hoặc dùng số trung bình ngành thay số doanh nghiệp đã xác minh. So ngành có thể có ích nhưng mẫu FAP 3 công ty không tạo benchmark toàn ngành. Đây là coursework/notebook, không bằng chứng mô hình đầu tư đã kiểm định hoặc hệ thống production.

## Đọc gì tiếp nếu chọn một nhánh?

G02: đọc controller/mapping của FinanceToolkit và báo cáo gốc doanh nghiệp để xác định chính xác dòng chi. G03: đọc fetch/schema/tests split của Dividend CLI và notice cổ phiếu thật của Việt Nam. G01: đọc bộ lọc/UI nhưng tự thiết kế trạng thái thiếu và thuật ngữ phù hợp. G05/G10: đọc manual/fixtures Portfolio Performance và tạo ca có ngày quyền/ngày trả khác nhau. Các bước này là backlog sau khảo sát, chưa mô tả như đã kiểm thử.
