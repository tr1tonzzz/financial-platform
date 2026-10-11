# Nghiên cứu bổ sung: chiều sâu chức năng hỗ trợ phân tích và đầu tư

Ngày **11/10/2026**. Kế thừa khảo sát [36 repository](../research-high-star-finance/README.md), chọn **12 repo** để kiểm sâu theo câu hỏi người dùng; lưu **32 tệp mã nguồn tại commit cố định**. Đây là đọc mã/tài liệu, **chưa cài hoặc chạy các platform**, chưa phỏng vấn người dùng. Một số tệp đã được khảo sát trước; không báo 12 repo này là 12 repo mới.

Kết luận sản phẩm và đề xuất: [đánh giá mức hỗ trợ người đầu tư](../research-platform/37-danh-gia-muc-do-ho-tro-nha-dau-tu.md). Cấu trúc năm UC giữ nguyên; bổ sung vẫn là đề xuất, chưa cập nhật nghĩa vụ SRS hoặc lịch v6.

## Nguồn và bài học cụ thể

Sao là snapshot của khảo sát trước trong cùng ngày, không truy vấn lại khi thu mã bổ sung. Mức sao giúp ưu tiên tìm đọc, không chứng minh chất lượng phân tích, công thức hay dữ liệu Việt Nam. Các link mã dưới đây gắn commit; metadata/hash/tệp local tại [source-capture.json](evidence/source-capture.json).

| Repository / sao snapshot | Đã kiểm gì trong mã? | Bài học áp dụng / giới hạn |
|---|---|---|
| [OpenBB](https://github.com/openbq-org/OpenBB) — 74.088 | Router fundamental tách balance/cash/income; models tài chính và trailing dividend yield | Tách dữ liệu nguồn với phân tích; nhiều chỉ tiêu và provider không tự bảo đảm cùng định nghĩa. Ý tưởng chuyển được, các provider không tự có đủ ba mã Việt Nam |
| [FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) — 32.370 | Financials views: bảng/biểu đồ/margin/cash/debt; peers; xuất CSV và xử lý missing | UC phân tích cần bảng + biểu đồ + drill-down + xuất; tham khảo thao tác, không sao chép ngưỡng màu/ranking hoặc FCF mặc định |
| [yfinance](https://github.com/ranaroussi/yfinance) — 25.489 | Time series income/balance/cash; yearly/quarterly/trailing và trường hợp rỗng | Cần phân biệt stock/flow và tần suất; API truy được một mã không chứng minh độ phủ đầy đủ Việt Nam |
| [AKShare](https://github.com/akfamily/akshare) — 22.886 | Truy vấn công bố CNINFO, mã/tên/tiêu đề/ngày/link | Tham khảo tổ chức sự kiện có nguồn; cần adapter doanh nghiệp/nguồn Việt Nam, không dùng CNINFO làm dữ liệu pilot |
| [Ghostfolio](https://github.com/ghostfolio/ghostfolio) — 9.437 | Tổng hợp dividends từ activities, nhóm theo kỳ | Thu nhập danh mục cần hoạt động/vị thế; biểu đồ DPS doanh nghiệp không thay sổ thu nhập cá nhân |
| [Wealthfolio](https://github.com/wealthfolio/wealthfolio) — 9.160 | Income UI và income service, tổng theo tháng/tài sản/loại thu nhập | Thiết kế đầu ra theo câu hỏi “thu nhập từ đâu”; chỉ chuyển sang UC-F06 khi có ledger |
| [QuantStats](https://github.com/ranaroussi/quantstats) — 7.694 | Hàm `html` nhận returns, benchmark và output, tạo báo cáo | Học cách lưu/xuất một kết quả phân tích đầy đủ; lợi suất/drawdown ở đây không phải tỷ số BCTC |
| [FinanceToolkit](https://github.com/JerBouma/FinanceToolkit) — 5.410 | Các model profitability/liquidity/solvency/efficiency và DuPont | Chọn nhóm chỉ tiêu theo câu hỏi; kiểm operands/công thức. Hữu ích nhất để làm sâu UC-F02 |
| [Portfolio Performance](https://github.com/portfolio-performance/portfolio) — 4.092 | Ma trận khoản thu theo tháng, trung bình/tổng | Thu nhập thực nhận thuộc UC-F06; không đưa vào UC-F05 bằng cách giả định nhà đầu tư đủ quyền |
| [EdgarTools](https://github.com/dgunning/edgartools) — 2.781 | Stitching nhiều kỳ, scope thời gian, missing và nguồn kỳ; query facts | Bảng nhiều năm cần gắn từng số với kỳ/nguồn. XBRL/SEC không thay OCR tài liệu Việt Nam |
| [Vnstock](https://github.com/thinh-vu/vnstock) — 1.412 | Fundamental equity: ba BCTC/ratio; adapter VCI và format report | Nguồn đối chiếu ứng viên sát thị trường Việt Nam; chưa chạy/kiểm đủ dữ liệu mẫu, không mặc định mọi ratio vendor có cùng công thức |
| [Stocknear frontend](https://github.com/stocknear/frontend) — 44 | Metric picker, multi-series, bảng, chart modal, trang revenue, note editor | Ít sao nhưng hợp nhu cầu UX: người dùng chọn chỉ tiêu, xem mở rộng và lưu luận điểm. Đây là frontend, chưa kiểm backend và chất lượng số liệu |

## Bằng chứng cho từng ý tưởng

### 1. Chọn chỉ tiêu rồi phân tích, thay vì chỉ một biểu đồ cố định

Stocknear `FinancialMetricPicker` khai báo nhóm income/balance/cashflow/ratios và các callbacks chọn/reset; `FinancialMultiSeriesCard` nhận nhiều chuỗi và chart mode. Chart modal có lựa chọn range và bar/line. Chuyển thể: nhóm chỉ tiêu do người dùng chọn trong UC-F02, bảng–biểu đồ–nguồn dùng cùng context; chưa cần thêm thị trường, hơn mười năm dữ liệu hoặc gói trả phí.

[Metric picker L22–85](https://github.com/stocknear/frontend/blob/a97f990ea2567303de88279ed020c4f16f4ddbbd/src/lib/components/Financial/FinancialMetricPicker.svelte#L22), [multi-series L7–29](https://github.com/stocknear/frontend/blob/a97f990ea2567303de88279ed020c4f16f4ddbbd/src/lib/components/Financial/FinancialMultiSeriesCard.svelte#L7), [chart modal L38–65](https://github.com/stocknear/frontend/blob/a97f990ea2567303de88279ed020c4f16f4ddbbd/src/lib/components/Financial/FinancialChartModal.svelte#L38).

### 2. Kết hợp doanh thu, lợi nhuận và biên

Fincept views có revenue/gross profit/net income, các margin và chart. FinanceToolkit profitability có hàm biên gộp/ròng; tổng lợi nhuận đơn lẻ không thể cung cấp các biên này. Chuyển thể: thêm doanh thu thuần/lợi nhuận gộp đã duyệt, tính biên đúng kỳ/scope và hiển thị với lịch sử. Đây là làm sâu F02.2, không cần UC lớn riêng cho mỗi tỷ số.

[Fincept views L201–239](https://github.com/Fincept-Corporation/FinceptTerminal/blob/3f444cb7ab712d85a57d270d5edd6e7a2ef50d55/fincept-qt/src/screens/equity_research/EquityFinancialsTab_Views.cpp#L201), [FinanceToolkit profitability L9–57](https://github.com/JerBouma/FinanceToolkit/blob/37ed6f01465b4bfb6718b07e1d65826734f53337/financetoolkit/ratios/profitability_model.py#L9).

### 3. Phân tích thanh khoản, nợ vay và cơ cấu

FinanceToolkit liquidity dùng current assets/current liabilities, working capital và các tỷ số dòng tiền; solvency dùng total debt/assets/equity. Fincept có total liabilities và total debt riêng. Chuyển thể: đưa nghĩa vụ ngắn hạn và vay/nợ thuê tài chính vào UC-F02, không đổi tên tổng nợ phải trả thành nợ vay. Chưa sao chép ngưỡng an toàn hoặc DSCR proxy.

[Liquidity L9–26 và L129–162](https://github.com/JerBouma/FinanceToolkit/blob/37ed6f01465b4bfb6718b07e1d65826734f53337/financetoolkit/ratios/liquidity_model.py#L9), [solvency L9–42](https://github.com/JerBouma/FinanceToolkit/blob/37ed6f01465b4bfb6718b07e1d65826734f53337/financetoolkit/ratios/solvency_model.py#L9), [Fincept balance L362–375](https://github.com/Fincept-Corporation/FinceptTerminal/blob/3f444cb7ab712d85a57d270d5edd6e7a2ef50d55/fincept-qt/src/screens/equity_research/EquityFinancialsTab_Views.cpp#L362).

### 4. So sánh xu hướng có cùng cơ sở

EdgarTools `StatementStitcher` xử lý alignment/concepts/missing; có period sources và tham số discrete quarters. Fincept peers cho nhập mã và so nhiều metric, nhưng có ngưỡng màu mặc định. Chuyển thể: nhóm tự chọn, cùng period/scope, cùng định nghĩa; lấy ý tưởng bảng/chuỗi chứ không xếp hạng ba mã khác ngành.

[EdgarTools L60–119](https://github.com/dgunning/edgartools/blob/246010946cdbe588b0397643fb1598a04fe0cad6/edgar/xbrl/stitching/core.py#L60), [Fincept peers L220–255](https://github.com/Fincept-Corporation/FinceptTerminal/blob/3f444cb7ab712d85a57d270d5edd6e7a2ef50d55/fincept-qt/src/screens/equity_research/EquityPeersTab.cpp#L220).

### 5. Lưu một kết quả nghiên cứu có thể dùng tiếp

Stocknear note editor có symbol, nội dung và callback save. QuantStats HTML nhận kết quả, benchmark và đường xuất. Fincept CSV xuất giá trị thô thay số rút gọn trên bảng và giữ dòng thiếu trống. Chuyển thể: hồ sơ của project giữ context/phiên bản/source refs/nhận xét, có xuất số chính xác và mở lại. Những tính năng provenance này được đề xuất từ yêu cầu project; không khẳng định các repo đều có snapshot tương đương D11/12.

[Note editor L58–65](https://github.com/stocknear/frontend/blob/a97f990ea2567303de88279ed020c4f16f4ddbbd/src/lib/components/MarkdownNoteEditor.svelte#L58), [QuantStats reports L206–270](https://github.com/ranaroussi/quantstats/blob/9ef4c6d0a4ffe7831f6ebba6a5824fd33a90c05a/quantstats/reports.py#L206), [Fincept export L136–152](https://github.com/Fincept-Corporation/FinceptTerminal/blob/3f444cb7ab712d85a57d270d5edd6e7a2ef50d55/fincept-qt/src/screens/equity_research/EquityFinancialsTab_Views.cpp#L136).

### 6. Tách DPS doanh nghiệp khỏi thu nhập người nắm giữ

Wealthfolio lấy income activities theo tài khoản; Ghostfolio lấy dividend activities và nhóm kỳ; Portfolio Performance có ma trận tháng. Bài học: UC-F05 giải thích chính sách/khả năng bao phủ của doanh nghiệp. Muốn giải thích thu nhập thực nhận cần UC-F06 với giao dịch và tiền, không chỉ nhân DPS với số cổ phiếu đang có hôm nay.

[Wealthfolio income service L76–107](https://github.com/wealthfolio/wealthfolio/blob/ace5c5243d890f22cf68118ed74986cac8f4cb17/crates/core/src/portfolio/income/income_service.rs#L76), [Ghostfolio L458](https://github.com/ghostfolio/ghostfolio/blob/8fa4f6a6739afee82461b3aa48f47dfa6a396dc8/apps/api/src/app/portfolio/portfolio.service.ts#L458), [Portfolio Performance L49–69](https://github.com/portfolio-performance/portfolio/blob/ec5ce7ef1ffcbad0fcef4d3b5782e00efa55f297/name.abuchen.portfolio.ui/src/name/abuchen/portfolio/ui/views/payments/PaymentsPerMonthMatrixTab.java#L49).

<a id="kiem-cong-thuc-truoc-khi-chuyen-the"></a>
## Kiểm công thức trước khi chuyển thể

1. **Cùng tên, khác công thức:** ở commit đã lưu, FinanceToolkit profitability dùng operating income/interest expense; solvency cùng tên dùng (operating income + D&A)/interest expense. Project phải nêu rõ cơ sở kiểu EBIT/EBITDA và kiểm mapping Việt Nam; không mặc định “lợi nhuận thuần từ hoạt động kinh doanh” trên BCTC Việt Nam đồng nghĩa EBIT. [Profitability L94–117](https://github.com/JerBouma/FinanceToolkit/blob/37ed6f01465b4bfb6718b07e1d65826734f53337/financetoolkit/ratios/profitability_model.py#L94), [solvency L45–62](https://github.com/JerBouma/FinanceToolkit/blob/37ed6f01465b4bfb6718b07e1d65826734f53337/financetoolkit/ratios/solvency_model.py#L45).
2. **Proxy không là nghĩa vụ thực tế:** solvency DSCR dùng operating income/current liabilities, docstring giải thích proxy. Project chưa có lịch trả gốc/lãi thì không dùng nó để kết luận bao phủ nghĩa vụ nợ thực tế. [L65–94](https://github.com/JerBouma/FinanceToolkit/blob/37ed6f01465b4bfb6718b07e1d65826734f53337/financetoolkit/ratios/solvency_model.py#L65).
3. **Đơn vị % và missing:** Fincept peers chuẩn hóa debtToEquity/dividendYield từ %; populate có NaN và kiểm mẫu số. Không sao chép số vendor/màu hoặc biến thiếu thành 0. [Peers L247–253](https://github.com/Fincept-Corporation/FinceptTerminal/blob/3f444cb7ab712d85a57d270d5edd6e7a2ef50d55/fincept-qt/src/screens/equity_research/EquityPeersTab.cpp#L247), [populate L48–62](https://github.com/Fincept-Corporation/FinceptTerminal/blob/3f444cb7ab712d85a57d270d5edd6e7a2ef50d55/fincept-qt/src/screens/equity_research/EquityFinancialsTab_Populate.cpp#L48).
4. **Lưu ý phạm vi source:** Stocknear `SectorSegmentation` là cơ cấu ngành ETF, không là doanh thu theo mảng của doanh nghiệp; không dùng tên file làm bằng chứng cho phân tích segment. [L1–7](https://github.com/stocknear/frontend/blob/a97f990ea2567303de88279ed020c4f16f4ddbbd/src/lib/components/SectorSegmentation.svelte#L1). Đề xuất mảng kinh doanh của project dùng BCTN/thuyết minh Việt Nam, chưa kết luận từ component này.

Đây là kiểm ngữ nghĩa ở đoạn mã cụ thể, chưa là đánh giá toàn bộ độ đúng của thư viện. Không đưa thư viện mới vào stack, không chép mã nguồn vào ứng dụng.

## Nguồn chuyên môn và khả thi tại Việt Nam

- [CFA — Introduction to Financial Statement Analysis](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/introduction-financial-statement-analysis): tài chính, rủi ro và triển vọng là đầu vào cho quyết định; BCTC cần kết hợp thuyết minh/bối cảnh.
- [CFA — Financial Analysis Techniques](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/financial-analysis-techniques): nhóm sinh lời, thanh khoản, solvency, hoạt động; so sánh/xu hướng/common-size và giới hạn của tỷ số. Từ đây suy luận project nên tăng chiều sâu phân tích, chưa suy nhà đầu tư cần mọi tỷ số.
- [CFA — Free Cash Flow Valuation](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/free-cash-flow-valuation): FCFF/FCFE cần điều chỉnh và cơ sở định giá phù hợp; G02 không tự thành FCFE.
- [Vnstock — Fundamental](https://vnstocks.com/docs/vnstock/phan-tich-co-ban-fundamental), [mã equity L70–114](https://github.com/thinh-vu/vnstock/blob/88825be3f9aab729362e6fca178eb6e9ae4d3f88/vnstock/ui/domains/fundamental/equity.py#L70): documented interface cho ba BCTC/ratio, chưa là bằng chứng truy vấn pilot thành công.
- [HPG — danh mục BCTC](https://www.hoaphat.com.vn/quan-he-co-dong/bao-cao-tai-chinh): có BCTC hợp nhất/riêng lẻ kiểm toán 2025 và giải trình; cần thu/đọc/duyệt để dùng số.
- [FPT — BCTN số 2025](https://bctn2025.fpt.com/vi/phan-tich-hoat-dong-kinh-doanh/danh-gia-chung/): có phân tích theo khối/mảng và kế hoạch; là cơ sở chọn ca nghiên cứu segment, chưa chứng minh bộ số đã chuẩn hóa.

Nguồn VNM khi tìm bằng web chưa xác nhận được đủ tài liệu năm ở đúng trang hiện hành; không ghi đủ dữ liệu. Không đổi mẫu ba mã và không mở lại screening/A04.

## Hồ sơ nghiên cứu

- [Source capture: repo/commit/sao/hash và file local](evidence/source-capture.json).
- [Bảng khoảng trống và gói đề xuất](evidence/gap-review.json): tách thiếu màn hình, thiếu dữ liệu và ngoài SRS; trạng thái đề xuất.
- [Nguồn web và giới hạn kiểm chứng](evidence/web-sources.json).
- [Kết luận để dùng với giảng viên](../research-platform/37-danh-gia-muc-do-ho-tro-nha-dau-tu.md).
- [Cách thu mã](../../scripts/research/fetch_investor_support_sources.py): read-only với nguồn, không thực thi project tham khảo.
