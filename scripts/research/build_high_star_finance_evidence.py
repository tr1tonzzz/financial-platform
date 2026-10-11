"""Build source ledgers from captured files; no remote calls or project execution."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / 'docs/research-high-star-finance'
BASE = BUNDLE / 'evidence/github'

# Type, useful capability, transfer constraint. Stars never determine priority alone.
NOTES = {
    'openbq-org/OpenBB': ('Nền tảng dữ liệu', 'Ba BCTC, cổ tức, lịch, đối chiếu, tin theo doanh nghiệp', 'Router phụ thuộc provider; không coi Workspace là toàn bộ mã mở'),
    'freqtrade/freqtrade': ('Bot giao dịch', 'Backtest và báo cáo chiến lược', 'Thiên về crypto/đặt lệnh; không ưu tiên cho theo dõi BCTC'),
    'microsoft/qlib': ('Framework nghiên cứu ML', 'Quy trình dữ liệu và đánh giá mô hình', 'Cần dữ liệu giá/nhãn; không đưa dự báo ML vào UC chính'),
    'vnpy/vnpy': ('Framework giao dịch', 'Kết nối gateway, dữ liệu thị trường', 'Không phải nền tảng đọc BCTC; không bổ sung đặt lệnh'),
    'Fincept-Corporation/FinceptTerminal': ('Terminal tài chính', 'Xu hướng BCTC, mô hình định giá, kịch bản/độ nhạy', 'Cần phân biệt giao diện, script tính và nguồn dữ liệu'),
    'wilsonfreitas/awesome-quant': ('Danh mục liên kết', 'Phát hiện thư viện cùng lĩnh vực', 'Không là bằng chứng chức năng đã triển khai'),
    'ranaroussi/yfinance': ('Thư viện dữ liệu', 'BCTC nhiều kỳ, lịch, cổ tức và estimates', 'Phụ thuộc Yahoo; không mặc định mã/lịch sử Việt Nam đủ'),
    'akfamily/akshare': ('Thư viện dữ liệu', 'Ba BCTC, danh sách công bố, quyền/cổ tức', 'Adapter Trung Quốc không dùng nguyên cho Việt Nam'),
    'QuantConnect/Lean': ('Engine giao dịch/backtest', 'Sự kiện doanh nghiệp trong mô phỏng, kế toán danh mục', 'Phạm vi chiến lược rộng; chỉ học tách giá/sự kiện'),
    'stefan-jansen/machine-learning-for-trading': ('Tài liệu/code sách', 'Ví dụ phân tích và đánh giá', 'Không là sản phẩm nền tảng đã triển khai'),
    'Open-Dev-Society/OpenStock': ('Ứng dụng theo dõi cổ phiếu', 'Trang doanh nghiệp, watchlist, tin', 'Widget/nguồn ngoài; price alert bị chặn bởi cờ Cloud'),
    'waditu/tushare': ('SDK dữ liệu', 'Cấu trúc truy vấn API tài chính', 'Client chuyển tên API/fields tới server; không chứng minh dữ liệu miễn phí/đủ'),
    'JerBouma/FinanceDatabase': ('Danh mục tài sản', 'Tra cứu tên/mã, ngành, quốc gia', 'README nói không cung cấp fundamentals/giá cập nhật'),
    'ghostfolio/ghostfolio': ('Ứng dụng danh mục', 'Giao dịch, thu nhập cổ tức theo kỳ, watchlist, benchmark', 'Cần vị thế/giao dịch/giá và dữ liệu Việt Nam'),
    'polakowo/vectorbt': ('Thư viện phân tích/backtest', 'Đồ thị kết quả và tham số mô phỏng', 'Không chuyển toàn bộ backtest thành yêu cầu đề tài'),
    'wealthfolio/wealthfolio': ('Ứng dụng danh mục/cá nhân', 'Thu nhập, hiệu quả, biểu đồ phân bổ, nhập hoạt động', 'Tách phần đầu tư khỏi chi tiêu cá nhân; cần ledger'),
    'kernc/backtesting.py': ('Thư viện backtest', 'Báo cáo hiệu quả và đồ thị chiến lược', 'Đòi hỏi OHLC/chiến lược; thấp hơn nhu cầu tài chính doanh nghiệp'),
    'ranaroussi/quantstats': ('Thư viện phân tích hiệu quả', 'Báo cáo lợi suất, drawdown, đối chiếu benchmark', 'Nhận chuỗi returns; không thay bộ tính returns từ giao dịch'),
    'ricequant/rqalpha': ('Framework backtest/giao dịch', 'Kế toán danh mục và sự kiện', 'Dữ liệu tài chính RQData là dịch vụ tách riêng; không coi README là dữ liệu sẵn'),
    'PyPortfolio/PyPortfolioOpt': ('Thư viện tối ưu danh mục', 'Phân bổ theo trọng số và ngân sách, số cổ phiếu nguyên', 'Giá/returns/ràng buộc là dữ liệu mới; tối ưu chưa cần ở bước đầu'),
    'JerBouma/FinanceToolkit': ('Thư viện phân tích tài chính', 'Biên lợi nhuận, ROE, DuPont, DCF/DDM', 'Kiểm công thức, scope và số dư bình quân; không nhập hàng trăm tỷ số'),
    'bukosabino/ta': ('Thư viện chỉ báo kỹ thuật', 'Chỉ báo từ giá/khối lượng', 'Không phục vụ trực tiếp câu hỏi BCTC/cổ tức'),
    'dcajasn/Riskfolio-Lib': ('Thư viện rủi ro/tối ưu', 'Biểu đồ phân bổ và đóng góp rủi ro', 'Đầu vào returns/trọng số; rủi ro thống kê cần đủ lịch sử'),
    'portfolio-performance/portfolio': ('Ứng dụng danh mục', 'Ma trận thu nhập theo tháng, hiệu quả/biểu đồ', 'Không dùng số dư BCTC làm vị thế nhà đầu tư'),
    'pydata/pandas-datareader': ('Thư viện dữ liệu', 'Nguồn vĩ mô FRED/World Bank và các nguồn khác', 'Bối cảnh vĩ mô để sau; không thay kho BCTC Việt Nam'),
    'pmorissette/bt': ('Thư viện backtest', 'Chiến lược phân bổ và báo cáo', 'Chưa cần tái cân bằng tự động để đáp ứng theo dõi doanh nghiệp'),
    'dgunning/edgartools': ('Thư viện filings/XBRL', 'Truy vấn nhiều kỳ/as_of, ghép BCTC, tách quý lũy kế', 'SEC/XBRL khác PDF Việt Nam; cần lưu provenance khi suy ra quý'),
    'stefan-jansen/zipline-reloaded': ('Engine backtest', 'Xử lý dữ liệu và hiệu quả chiến lược', 'Không ưu tiên kết nối broker/chiến lược cho MVP'),
    'FinanceData/FinanceDataReader': ('Thư viện dữ liệu', 'Danh mục niêm yết, giá, chỉ số, xuất dữ liệu', 'Nguồn chính Hàn Quốc/quốc tế; không mặc định bao phủ Việt Nam'),
    'thinh-vu/vnstock': ('Thư viện dữ liệu Việt Nam', 'BCTC năm/quý và tỷ số qua provider', 'Lựa chọn đáng thử đối chứng; chưa kiểm đủ pilot/nguồn/phiên bản'),
    'theOGognf/finagg': ('Thư viện tổng hợp dữ liệu', 'Raw/refined trong SQL, feature và đối chiếu ngành', 'SEC/FRED khác nguồn Việt Nam; mẫu ngành phải được xác định'),
    'OpenBB-finance/backends-for-openbb': ('Ví dụ tích hợp — archived', 'Hợp đồng JSON/widget/bộ chọn dùng chung', 'Repo đã archived ở lần kiểm; dữ liệu ví dụ không là dữ liệu thị trường'),
    'GavrielP1/SALARY-2045': ('Ứng dụng ngách cổ tức', 'Lịch thu nhập, đóng góp vị thế, mục tiêu thu nhập', 'Sao thấp nhưng sát ngách; dự phóng/score README chưa được thẩm định'),
    'stocknear/frontend': ('Giao diện nền tảng', 'Chọn chỉ tiêu, bảng/biểu đồ đa chuỗi, earnings guidance', 'Không có README tại commit; frontend không chứng minh backend/nguồn hoạt động'),
    'sonnymay/dividend-tracker': ('Ứng dụng ngách cổ tức', 'Thu nhập và phân bổ theo vị thế', 'Chỉ đọc README đợt này; không kế thừa AI chat/yield dự phóng làm mặc định'),
    'EmanueleSturzo/portfolio-analytics': ('Dashboard danh mục', 'Holdings, phân bổ, benchmark, cổ tức', 'Chỉ đọc README đợt này; không chứng minh tính đúng toàn bộ metrics'),
}

# Requested names match the local capture folders; immutable links use canonical names.
# repo, path, exact locator, observed behavior, product lesson, adaptation
EVIDENCE = [
 ('OpenBB-finance/OpenBB','openbb_platform/extensions/equity/openbb_equity/fundamental/fundamental_router.py','async def balance(', 'Router có balance/income/cash, dividends và filings', 'F01.2/F05.1: dữ liệu theo loại nghiệp vụ', 'Endpoint khai báo và chuyển tới provider; chưa chạy provider'),
 ('OpenBB-finance/OpenBB','openbb_platform/extensions/equity/openbb_equity/calendar/calendar_router.py','async def dividend(', 'Router riêng cho dividend/events/earnings', 'F04.3: lịch có loại sự kiện', 'Ngày BCTC/quyền Việt Nam phải có nguồn; không suy lịch theo Mỹ'),
 ('OpenBB-finance/OpenBB','openbb_platform/extensions/equity/openbb_equity/compare/compare_router.py','async def company_facts(', 'Endpoint đối chiếu company facts', 'F03: đặt dữ liệu công ty cạnh nhau', 'Chọn nhóm thủ công trước; không tự tìm mã đạt ngưỡng'),
 ('OpenBB-finance/OpenBB','openbb_platform/extensions/news/openbb_news/news_router.py','async def company(', 'Router tin theo doanh nghiệp', 'F04.2: feed theo doanh nghiệp đã chọn', 'Ưu tiên công bố chính thức; không coi news là fact BCTC'),
 ('stocknear/frontend','src/lib/components/Financial/FinancialMetricPicker.svelte','selectedIds', 'Chọn metric, nhóm income/balance/cashflow/ratios', 'F02.1: người dùng chọn dữ liệu muốn xem', 'Chọn chỉ tiêu khác với sàng lọc cổ phiếu; chưa kiểm backend'),
 ('stocknear/frontend','src/lib/components/Financial/FinancialMultiSeriesCard.svelte','<script', 'Thành phần giao diện cho nhiều chuỗi tài chính', 'F02.1/F03.3: bảng/biểu đồ cùng tập số', 'Code có nhánh giá trị thiếu về 0; FAP giữ null/khoảng trống'),
 ('stocknear/frontend','src/lib/components/EarningsGuidance.svelte','selectLatestGuidanceRow', 'Giao diện chọn bản guidance gần nhất', 'F02.7: chuyển thể sang kế hoạch–thực hiện', 'Guidance nước ngoài khác nghị quyết/kế hoạch Việt Nam; cần nguồn riêng'),
 ('JerBouma/FinanceToolkit','financetoolkit/ratios/profitability_model.py','def get_net_profit_margin(', 'Công thức net income/revenue; có ROE và income quality', 'F02.2/.4: chỉ tiêu có định nghĩa', 'Chưa có doanh thu thì không tính margin; kiểm tử số/scope'),
 ('JerBouma/FinanceToolkit','financetoolkit/models/dupont_model.py','def get_dupont_analysis(', 'ROE phân rã margin × turnover × multiplier', 'F02.6: giải thích thành phần sinh lời', 'Cần doanh thu và tài sản/vốn bình quân cùng scope'),
 ('JerBouma/FinanceToolkit','financetoolkit/models/intrinsic_model.py','def get_intrinsic_value(', 'Mô hình dòng tiền chiết khấu; file có FCFF/FCFE/DDM', 'F07.3: công thức/giả định kiểm lại được', 'Không lấy CFO−CAPEX làm FCFF/FCFE một cách mặc định'),
 ('Fincept-Corporation/FinceptTerminal','fincept-qt/src/screens/equity_research/EquityFinancialsTab_Populate.cpp','populate', 'Các hàm populate dữ liệu tài chính và tạo biểu đồ', 'F02.1/.3: tổ chức góc nhìn BCTC', 'Giao diện và nguồn backend phải kiểm tách nhau'),
 ('Fincept-Corporation/FinceptTerminal','fincept-qt/scripts/Analytics/corporateFinance/valuation/dcf_model.py','def sensitivity_analysis(', 'Lặp WACC/growth; chặn WACC≤g, tính ma trận; có scenario_analysis', 'F07.2/.4: kịch bản và độ nhạy', 'Không dùng bear/bull mặc định của repo làm chuẩn; cần giả định người dùng'),
 ('dgunning/edgartools','edgar/entity/query.py','def as_of(', 'Lọc facts theo ngày filing; hỗ trợ năm/kỳ và bảng', 'F01.2/.5: mốc dữ liệu và nhiều kỳ', 'Ở Việt Nam phải lưu ngày công bố và ngày quan sát riêng'),
 ('dgunning/edgartools','edgar/xbrl/stitching/core.py','def _unaccumulate_cashflow_ytd(', 'Tách cashflow lũy kế thành quý từ các kỳ cùng đầu năm', 'F02.7: phân tích quý đúng loại kỳ', 'Kiểm đủ kỳ/scope/revision; không trừ các dòng stock cuối kỳ'),
 ('ranaroussi/yfinance','yfinance/scrapers/fundamentals.py','def get_income_time_series(', 'Có time series income/balance/cash theo frequency', 'F01.2: nhiều loại báo cáo/nhiều kỳ', 'Không mặc định đủ mã Việt Nam hoặc nguồn là BCTC chính thức'),
 ('ranaroussi/yfinance','yfinance/scrapers/analysis.py','def revenue_estimate(', 'Tách revenue/earnings estimates khỏi earnings history', 'F02.7/F07: tách lịch sử và dự tính', 'Estimates bên phân tích khác mục tiêu doanh nghiệp công bố'),
 ('akfamily/akshare','akshare/stock_feature/stock_three_report_em.py','def stock_profit_sheet_by_yearly_em(', 'Có income/balance/cash năm/quý qua Eastmoney', 'F01.2: nhóm ba báo cáo', 'Adapter Trung Quốc không phải bộ đọc PDF Việt Nam'),
 ('akfamily/akshare','akshare/stock_feature/stock_disclosure_cninfo.py','def stock_zh_a_disclosure_report_cninfo(', 'Truy vấn công bố; định dạng tiêu đề/ngày/URL', 'F04.2: công bố cần có metadata và chứng từ', 'Nối nguồn IR/công bố Việt Nam; loại trùng/cập nhật riêng'),
 ('akfamily/akshare','akshare/stock/stock_dividend_cninfo.py','def stock_dividend_cninfo(', 'Truy vấn thông tin cổ tức từ CNInfo', 'F05: cổ tức là dữ liệu sự kiện riêng', 'Kiểm năm lợi nhuận và basis, không đồng nhất với thực nhận'),
 ('thinh-vu/vnstock','vnstock/api/financial.py','def balance_sheet(', 'Facade cung cấp balance/income/cash/ratio', 'F01.2: ứng viên nguồn Việt Nam', 'Đối chứng với PDF pilot trước chọn làm nguồn'),
 ('thinh-vu/vnstock','vnstock/explorer/vci/financial.py','def _get_financial_report(', 'Provider dựng BCTC từ dữ liệu truy vấn', 'F01: tách provider khỏi lớp phân tích', 'Kiểm mapping, history, missing, revision; chưa chạy ở đợt này'),
 ('JerBouma/FinanceDatabase','financedatabase/query_model.py','def search_rows(', 'Tìm trong danh mục, lọc thuộc tính', 'F01.1: tìm đúng doanh nghiệp/ngành', 'Danh mục không chứa fundamentals cập nhật; không biến thành screener'),
 ('waditu/tushare','tushare/pro/client.py','def query(', 'Client gửi api_name/token/params/fields tới server', 'F01: hợp đồng nguồn và dữ liệu độc lập', 'Chỉ chứng minh client; chưa xác nhận endpoint/điều kiện dữ liệu'),
 ('Open-Dev-Society/OpenStock','lib/actions/watchlist.actions.ts','export async function addToWatchlist(', 'Thêm/xóa/lấy watchlist theo người dùng', 'F04.1: theo dõi danh sách tự chọn', 'Không cần vị thế; không tự tìm trường hợp tài chính'),
 ('Open-Dev-Society/OpenStock','lib/actions/alert.actions.ts','export async function createAlert(', 'createAlert kiểm cờ alertsEnabled và nêu OpenStock Cloud', 'Không dùng README để kết luận mọi tính năng miễn phí', 'Không đề xuất alert giá ở giai đoạn BCTC này'),
 ('ghostfolio/ghostfolio','apps/api/src/app/portfolio/portfolio.service.ts','public getDividends(', 'Lấy cổ tức danh mục; nhóm month/quarter/year', 'F06.5: thu nhập theo kỳ/vị thế', 'Tách thực nhận cá nhân khỏi DPS công bố của công ty'),
 ('ghostfolio/ghostfolio','apps/api/src/app/endpoints/watchlist/watchlist.service.ts','public async createWatchlistItem(', 'Service quản lý watchlist', 'F04.1: danh sách quan tâm', 'Dữ liệu quotes không tự thành dữ liệu BCTC'),
 ('afadil/wealthfolio','crates/core/src/portfolio/income/income_service.rs','fn get_income_summary(&self, account_ids:', 'Tổng hợp income activities theo tài khoản, có kỳ YTD', 'F06.5: thu nhập có ledger/tài khoản', 'Không dùng net_income doanh nghiệp làm income nhà đầu tư; không chép growth nền≤0 thành0'),
 ('afadil/wealthfolio','apps/frontend/src/pages/holdings/components/composition-chart.tsx','export function PortfolioComposition(', 'Biểu đồ composition, tùy chọn donut/treemap', 'F06.3: tỷ trọng danh mục', 'Phải có giá và vị thế; xử lý thiếu khác với 0'),
 ('afadil/wealthfolio','crates/core/src/portfolio/performance/performance_service.rs','async fn measure_rows(', 'Đọc valuations/lots/disposals rồi chuyển vào engine đo hiệu quả', 'F06.4: hiệu quả cần nhiều dữ liệu hơn NAV cuối kỳ', 'Chưa thẩm định công thức engine; README TWR/MWR là mô tả sản phẩm'),
 ('portfolio-performance/portfolio','name.abuchen.portfolio.ui/src/name/abuchen/portfolio/ui/views/payments/PaymentsViewModel.java','public enum Mode', 'Mode DIVIDENDS/INTEREST/TAXES/FEES và dữ liệu tháng', 'F06.5: bảng thu nhập theo kỳ/loại khoản', 'Phí/thuế cần nguồn hoặc giả định phù hợp Việt Nam'),
 ('ranaroussi/quantstats','quantstats/reports.py','def html(', 'Báo cáo từ returns và benchmark, đồng bộ ngày', 'F06.4: báo cáo hiệu quả đối chiếu được', 'Cần bộ tính returns từ ledger; benchmark cùng loại lợi suất'),
 ('dcajasn/Riskfolio-Lib','riskfolio/src/PlotFunctions.py','def plot_risk_con(', 'Biểu đồ đóng góp rủi ro theo trọng số/returns', 'F06: hướng phân tích danh mục sau dữ liệu', 'Chưa ưu tiên rủi ro thống kê trước ledger/giá đủ'),
 ('robertmartin8/PyPortfolioOpt','pypfopt/discrete_allocation.py','def greedy_portfolio(', 'Đổi trọng số và ngân sách thành số cổ phiếu nguyên', 'F07: ý tưởng phân bổ giả định giai đoạn xa hơn', 'Chưa đưa tối ưu/tái cân bằng vào danh mục UC bắt buộc'),
]


def build():
    inventories = []
    requested = {}
    for path in BASE.glob('*/inventory.json'):
        inv = json.loads(path.read_text(encoding='utf-8'))
        inventories.append(inv)
        requested[inv['requested_repo']] = (inv, path.parent)
    inventories.sort(key=lambda i: (-i['stars'], i['repo']))
    assert len(inventories) == 36 and set(NOTES) == {i['repo'] for i in inventories}
    (BUNDLE / 'evidence/repository-survey.json').write_text(
        json.dumps(inventories, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = [
        '# Khảo sát repository và mức bằng chứng', '',
        'Truy xuất ngày **11/10/2026**. Số sao là giá trị từ GitHub API tại lần truy xuất, không dùng số trong badge hoặc kết quả tìm kiếm lưu đệm. Commit đầu nhánh được xác định bằng Git và cố định khi lưu tệp.', '',
        '## 1. Phương pháp và phạm vi', '',
        '- 36 repo hợp lệ; 25 repo có ít nhất 3.000 sao, 12 repo ít nhất 10.000 sao. Ưu tiên sao cao rồi xét độ phù hợp với tài chính doanh nghiệp/cổ tức.',
        '- README của 35 repo; mã chọn lọc của 17 repo; tổng 87 tệp lưu. Đây không phải 36 ứng dụng đã chạy hay 36 repo mới hoàn toàn: có repo được đọc lại từ đợt trước.',
        '- Nền tảng, thư viện, bot, sách và danh mục liên kết được phân loại riêng. Dự án sao thấp được giữ khi sát ngách hoặc có giao diện tài chính đáng học.',
        '- Mức R: metadata và README, chức năng là mô tả của tác giả. Mức C: thêm tệp triển khai chọn lọc, chứng minh hành vi cụ thể trong tệp; chưa kiểm vận hành toàn hệ thống.',
        '- Không clone/cài/chạy code dự án nguồn; không xác nhận tốc độ, độ đúng tài chính, tính sẵn có của API hoặc hiệu quả đầu tư.', '',
        '## 2. Danh mục theo số sao', '',
        '| # | Repo / nguồn cố định | Sao | Loại | Ý tưởng đáng học | Mức / lưu ý chuyển thể |',
        '|---|---|---:|---|---|---|',
    ]
    for n, inv in enumerate(inventories, 1):
        kind, lesson, constraint = NOTES[inv['repo']]
        files = inv['files']
        readme = next((f['path'] for f in files if f['path'].lower().startswith('readme')), None)
        link = f"https://github.com/{inv['repo']}/blob/{inv['sha']}/{readme}" if readme else f"https://github.com/{inv['repo']}/tree/{inv['sha']}"
        code = any(not f['path'].lower().startswith('readme') for f in files)
        lines.append(f"| {n} | [{inv['repo']}]({link}) | {inv['stars']:,} | {kind} | {lesson} | {'C' if code else 'R'} — {constraint} |")
    lines.extend([
        '', '## 3. Định danh và khả năng kiểm lại', '',
        'Tên cũ OpenBB-finance/OpenBB được GitHub chuyển tới openbq-org/OpenBB; afadil/wealthfolio tới wealthfolio/wealthfolio; robertmartin8/PyPortfolioOpt tới PyPortfolio/PyPortfolioOpt; financedata-org/FinanceDataReader tới FinanceData/FinanceDataReader. Link bằng chứng dùng tên trả về thực tế.', '',
        'Các lần thử stocknear/stocknear, stocknear/backend, pandas-datareader/pandas-datareader và rqalpha/rqalpha trả 404; không tính là repo đã khảo sát. Sau đó xác định stocknear/frontend, pydata/pandas-datareader và ricequant/rqalpha. Hồ sơ lỗi được giữ để tra cứu. OpenBB-finance/backends-for-openbb có archived=true tại lần kiểm.', '',
        '[Metadata tổng hợp](evidence/repository-survey.json) ghi sao, forks, SHA, nhánh, archived, giấy phép metadata, mô tả, thời điểm truy xuất và hash từng tệp. Inventory từng thư mục trong [bằng chứng](evidence/github) giữ đường dẫn và cây tệp khi đã truy vấn. Không coi giấy phép metadata là thẩm định đủ quyền tích hợp code; đợt này chỉ chuyển thể ý tưởng.', '',
        '[Minh chứng mã và bài học](02-minh-chung-ma-va-bai-hoc.md) · [Danh mục UC](../research-platform/27-yeu-cau-chuc-nang-va-vi-du.md).',
    ])
    (BUNDLE / '01-khao-sat-repository.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    refs = []
    lines = ['# Minh chứng mã và chuyển thể chức năng', '',
             'Các nhận xét dưới đây dựa trên tệp công khai đã lưu tại commit cố định. “Có code” chỉ nói về hành vi được đọc trong tệp, không tuyên bố đã cài/chạy hoặc thẩm định toàn dự án. Cột chuyển thể là suy luận thiết kế cho FAP.', '',
             '## 1. Dữ liệu, phân tích, theo dõi và danh mục', '',
             '| Nguồn tại dòng mã | Hành vi quan sát được | UC/ý tưởng chuyển thể | Điều cần điều chỉnh ở Việt Nam/FAP |',
             '|---|---|---|---|']
    for name, path, needle, observed, lesson, adaptation in EVIDENCE:
        inv, folder = requested[name]
        text = (folder / path).read_text(encoding='utf-8').splitlines()
        found = [i + 1 for i, line in enumerate(text) if needle in line]
        assert found, (name, path, needle)
        line = found[0]
        url = f"https://github.com/{inv['repo']}/blob/{inv['sha']}/{path}#L{line}"
        refs.append({'repo': inv['repo'], 'requested_repo': name, 'sha': inv['sha'],
                     'path': path, 'line': line, 'locator': needle, 'url': url,
                     'observed': observed, 'product_lesson': lesson, 'adaptation': adaptation})
        lines.append(f"| [{inv['repo']} — `{Path(path).name}:{line}`]({url}) | {observed} | {lesson} | {adaptation} |")
    lines.extend([
        '', '## 2. Bài học chọn chức năng', '',
        '**Dữ liệu và phân tích phải liên thông.** OpenBB tách dữ liệu theo nghiệp vụ; stocknear tổ chức chọn metric, bảng và biểu đồ; FinanceToolkit cho công thức minh bạch. Chuyển thể thành một bộ chọn doanh nghiệp/kỳ/scope/chỉ tiêu dùng chung, chọn điểm biểu đồ để xem bảng và nguồn, rồi lưu lần phân tích. Đây là cách kết hợp của nghiên cứu này, không khẳng định một repo chứa nguyên workflow FAP.', '',
        '**Theo dõi khác với tìm mã.** Watchlist trong OpenStock/Ghostfolio là danh sách người dùng tự chọn. FAP dùng danh sách này để xem dữ liệu/công bố mới; không thêm bộ phân loại đạt/không đạt hay tự phát hiện mã theo tỷ số.', '',
        '**Thu nhập đầu tư khác với lợi nhuận doanh nghiệp.** Ghostfolio/Wealthfolio/Portfolio Performance có cấu trúc thu nhập dựa trên danh mục/hoạt động. FAP cần ledger và điều kiện quyền nếu mở UC-F06; DPS công bố của công ty và tiền vào tài khoản nhà đầu tư thuộc hai đối tượng dữ liệu khác nhau.', '',
        '**Kịch bản cần giữ giả định.** Fincept và FinanceToolkit cung cấp tính toán theo đầu vào. Học công thức/ma trận độ nhạy; không chép các giả định bear/bull, CAGR cổ tức hoặc tỷ lệ chiết khấu thành chuẩn cho doanh nghiệp Việt Nam.', '',
        '**Không sao chép cách xử lý thiếu số.** Một số code hiển thị hoặc growth dùng 0 khi không có nền phù hợp. Quy tắc FAP vẫn là null/status/reason, khoảng trống biểu đồ và chặn phép tính phụ thuộc. Đọc repo nhiều sao vẫn cần đánh giá chi tiết này.', '',
        '## 3. Giới hạn và các nguồn mức README', '',
        'Các repo ML/backtest/technical indicators chỉ được dùng để khảo sát ranh giới sản phẩm; không phải minh chứng cần bổ sung ML, giao dịch hoặc hàng trăm chỉ báo. SALARY-2045 và hai tracker sao thấp gợi ý lịch thu nhập/mục tiêu nhưng chưa thẩm định code đợt này; không dùng dividend safety score hoặc dự phóng từ lịch sử làm kết luận an toàn.', '',
        '[Khảo sát và README của tất cả repo](01-khao-sat-repository.md) ghi rõ mức R/C. [Sổ tham chiếu mã máy đọc được](evidence/code-reference-ledger.json) giúp kiểm các dòng và commit; SHA-256 nằm trong inventory. [Khả thi và cách thực hiện](03-kha-thi-va-thu-tu-thuc-hien.md).',
    ])
    (BUNDLE / '02-minh-chung-ma-va-bai-hoc.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    (BUNDLE / 'evidence/code-reference-ledger.json').write_text(json.dumps(refs, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'repos': len(inventories), 'files': sum(len(i['files']) for i in inventories), 'code_references': len(refs)}))


if __name__ == '__main__':
    build()
