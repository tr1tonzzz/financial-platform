# Khảo sát repository và mức bằng chứng

Truy xuất ngày **11/10/2026**. Số sao là giá trị từ GitHub API tại lần truy xuất, không dùng số trong badge hoặc kết quả tìm kiếm lưu đệm. Commit đầu nhánh được xác định bằng Git và cố định khi lưu tệp.

## 1. Phương pháp và phạm vi

- 36 repo hợp lệ; 25 repo có ít nhất 3.000 sao, 12 repo ít nhất 10.000 sao. Ưu tiên sao cao rồi xét độ phù hợp với tài chính doanh nghiệp/cổ tức.
- README của 35 repo; mã chọn lọc của 17 repo; tổng 87 tệp lưu. Đây không phải 36 ứng dụng đã chạy hay 36 repo mới hoàn toàn: có repo được đọc lại từ đợt trước.
- Nền tảng, thư viện, bot, sách và danh mục liên kết được phân loại riêng. Dự án sao thấp được giữ khi sát ngách hoặc có giao diện tài chính đáng học.
- Mức R: metadata và README, chức năng là mô tả của tác giả. Mức C: thêm tệp triển khai chọn lọc, chứng minh hành vi cụ thể trong tệp; chưa kiểm vận hành toàn hệ thống.
- Không clone/cài/chạy code dự án nguồn; không xác nhận tốc độ, độ đúng tài chính, tính sẵn có của API hoặc hiệu quả đầu tư.

## 2. Danh mục theo số sao

| # | Repo / nguồn cố định | Sao | Loại | Ý tưởng đáng học | Mức / lưu ý chuyển thể |
|---|---|---:|---|---|---|
| 1 | [openbq-org/OpenBB](https://github.com/openbq-org/OpenBB/blob/ae0268771f761b036996d81bd21522ce79d95415/README.md) | 74,088 | Nền tảng dữ liệu | Ba BCTC, cổ tức, lịch, đối chiếu, tin theo doanh nghiệp | C — Router phụ thuộc provider; không coi Workspace là toàn bộ mã mở |
| 2 | [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade/blob/9a2f03a6bf8408f155591304c78aab20ca5c44cc/README.md) | 55,237 | Bot giao dịch | Backtest và báo cáo chiến lược | R — Thiên về crypto/đặt lệnh; không ưu tiên cho theo dõi BCTC |
| 3 | [microsoft/qlib](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/README.md) | 49,272 | Framework nghiên cứu ML | Quy trình dữ liệu và đánh giá mô hình | R — Cần dữ liệu giá/nhãn; không đưa dự báo ML vào UC chính |
| 4 | [vnpy/vnpy](https://github.com/vnpy/vnpy/blob/c6e231caf32b7fc97e6459817fff66458cf7e7c4/README.md) | 45,803 | Framework giao dịch | Kết nối gateway, dữ liệu thị trường | R — Không phải nền tảng đọc BCTC; không bổ sung đặt lệnh |
| 5 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal/blob/3f444cb7ab712d85a57d270d5edd6e7a2ef50d55/README.md) | 32,370 | Terminal tài chính | Xu hướng BCTC, mô hình định giá, kịch bản/độ nhạy | C — Cần phân biệt giao diện, script tính và nguồn dữ liệu |
| 6 | [wilsonfreitas/awesome-quant](https://github.com/wilsonfreitas/awesome-quant/blob/48e48a76b2054b5fe6eede6852ffef7783b992ce/README.md) | 30,030 | Danh mục liên kết | Phát hiện thư viện cùng lĩnh vực | R — Không là bằng chứng chức năng đã triển khai |
| 7 | [ranaroussi/yfinance](https://github.com/ranaroussi/yfinance/blob/5cae563642b59f49adf6a04a5ad6744f8b0e084d/README.md) | 25,489 | Thư viện dữ liệu | BCTC nhiều kỳ, lịch, cổ tức và estimates | C — Phụ thuộc Yahoo; không mặc định mã/lịch sử Việt Nam đủ |
| 8 | [akfamily/akshare](https://github.com/akfamily/akshare/blob/fac1e50ebf9b907960d6aab4c3df658559689f39/README.md) | 22,886 | Thư viện dữ liệu | Ba BCTC, danh sách công bố, quyền/cổ tức | C — Adapter Trung Quốc không dùng nguyên cho Việt Nam |
| 9 | [QuantConnect/Lean](https://github.com/QuantConnect/Lean/blob/80e7843f645673bcbeaab963049f76f20f6785e1/readme.md) | 21,956 | Engine giao dịch/backtest | Sự kiện doanh nghiệp trong mô phỏng, kế toán danh mục | R — Phạm vi chiến lược rộng; chỉ học tách giá/sự kiện |
| 10 | [stefan-jansen/machine-learning-for-trading](https://github.com/stefan-jansen/machine-learning-for-trading/blob/3d159425061a50a07825e0f85566b64c5124f9a1/README.md) | 21,293 | Tài liệu/code sách | Ví dụ phân tích và đánh giá | R — Không là sản phẩm nền tảng đã triển khai |
| 11 | [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock/blob/d890d910c8746d9794b39520199c6ed6735d2d1e/README.md) | 20,007 | Ứng dụng theo dõi cổ phiếu | Trang doanh nghiệp, watchlist, tin | C — Widget/nguồn ngoài; price alert bị chặn bởi cờ Cloud |
| 12 | [waditu/tushare](https://github.com/waditu/tushare/blob/093856995af0811d3ebbe8c179b8febf4ae706f0/README.md) | 15,444 | SDK dữ liệu | Cấu trúc truy vấn API tài chính | C — Client chuyển tên API/fields tới server; không chứng minh dữ liệu miễn phí/đủ |
| 13 | [JerBouma/FinanceDatabase](https://github.com/JerBouma/FinanceDatabase/blob/daf39af72cde42352a47d7981ae2e8b53d2f0d55/README.md) | 9,452 | Danh mục tài sản | Tra cứu tên/mã, ngành, quốc gia | C — README nói không cung cấp fundamentals/giá cập nhật |
| 14 | [ghostfolio/ghostfolio](https://github.com/ghostfolio/ghostfolio/blob/8fa4f6a6739afee82461b3aa48f47dfa6a396dc8/README.md) | 9,437 | Ứng dụng danh mục | Giao dịch, thu nhập cổ tức theo kỳ, watchlist, benchmark | C — Cần vị thế/giao dịch/giá và dữ liệu Việt Nam |
| 15 | [polakowo/vectorbt](https://github.com/polakowo/vectorbt/blob/f54802a5982c9fd8123d85c3b5a1d06a80b2726a/README.md) | 9,331 | Thư viện phân tích/backtest | Đồ thị kết quả và tham số mô phỏng | R — Không chuyển toàn bộ backtest thành yêu cầu đề tài |
| 16 | [wealthfolio/wealthfolio](https://github.com/wealthfolio/wealthfolio/blob/ace5c5243d890f22cf68118ed74986cac8f4cb17/README.md) | 9,160 | Ứng dụng danh mục/cá nhân | Thu nhập, hiệu quả, biểu đồ phân bổ, nhập hoạt động | C — Tách phần đầu tư khỏi chi tiêu cá nhân; cần ledger |
| 17 | [kernc/backtesting.py](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/README.md) | 9,033 | Thư viện backtest | Báo cáo hiệu quả và đồ thị chiến lược | R — Đòi hỏi OHLC/chiến lược; thấp hơn nhu cầu tài chính doanh nghiệp |
| 18 | [ranaroussi/quantstats](https://github.com/ranaroussi/quantstats/blob/9ef4c6d0a4ffe7831f6ebba6a5824fd33a90c05a/README.md) | 7,694 | Thư viện phân tích hiệu quả | Báo cáo lợi suất, drawdown, đối chiếu benchmark | C — Nhận chuỗi returns; không thay bộ tính returns từ giao dịch |
| 19 | [ricequant/rqalpha](https://github.com/ricequant/rqalpha/blob/284b78a1975bd2d6c4bee8fde35586e6846bfd96/README.rst) | 6,818 | Framework backtest/giao dịch | Kế toán danh mục và sự kiện | R — Dữ liệu tài chính RQData là dịch vụ tách riêng; không coi README là dữ liệu sẵn |
| 20 | [PyPortfolio/PyPortfolioOpt](https://github.com/PyPortfolio/PyPortfolioOpt/blob/a6638d2e06dae6f444fd022cfd4b3c528902a85b/README.md) | 6,092 | Thư viện tối ưu danh mục | Phân bổ theo trọng số và ngân sách, số cổ phiếu nguyên | C — Giá/returns/ràng buộc là dữ liệu mới; tối ưu chưa cần ở bước đầu |
| 21 | [JerBouma/FinanceToolkit](https://github.com/JerBouma/FinanceToolkit/blob/37ed6f01465b4bfb6718b07e1d65826734f53337/README.md) | 5,410 | Thư viện phân tích tài chính | Biên lợi nhuận, ROE, DuPont, DCF/DDM | C — Kiểm công thức, scope và số dư bình quân; không nhập hàng trăm tỷ số |
| 22 | [bukosabino/ta](https://github.com/bukosabino/ta/blob/a890410710a6e483c9ba08da7f3dd5089e4b9dff/README.md) | 5,235 | Thư viện chỉ báo kỹ thuật | Chỉ báo từ giá/khối lượng | R — Không phục vụ trực tiếp câu hỏi BCTC/cổ tức |
| 23 | [dcajasn/Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib/blob/7b1b26ac9760974c12ecefe290a9d3bd37b66b7a/README.md) | 4,540 | Thư viện rủi ro/tối ưu | Biểu đồ phân bổ và đóng góp rủi ro | C — Đầu vào returns/trọng số; rủi ro thống kê cần đủ lịch sử |
| 24 | [portfolio-performance/portfolio](https://github.com/portfolio-performance/portfolio/blob/ec5ce7ef1ffcbad0fcef4d3b5782e00efa55f297/README.md) | 4,092 | Ứng dụng danh mục | Ma trận thu nhập theo tháng, hiệu quả/biểu đồ | C — Không dùng số dư BCTC làm vị thế nhà đầu tư |
| 25 | [pydata/pandas-datareader](https://github.com/pydata/pandas-datareader/blob/9a3e2fe8c4e202bf9be6b4543fd1a06c3cdce7de/README.md) | 3,274 | Thư viện dữ liệu | Nguồn vĩ mô FRED/World Bank và các nguồn khác | R — Bối cảnh vĩ mô để sau; không thay kho BCTC Việt Nam |
| 26 | [pmorissette/bt](https://github.com/pmorissette/bt/blob/651e3e1479f37b70fd66f0a0f3b0c1ff95a75205/README.md) | 2,996 | Thư viện backtest | Chiến lược phân bổ và báo cáo | R — Chưa cần tái cân bằng tự động để đáp ứng theo dõi doanh nghiệp |
| 27 | [dgunning/edgartools](https://github.com/dgunning/edgartools/blob/246010946cdbe588b0397643fb1598a04fe0cad6/README.md) | 2,781 | Thư viện filings/XBRL | Truy vấn nhiều kỳ/as_of, ghép BCTC, tách quý lũy kế | C — SEC/XBRL khác PDF Việt Nam; cần lưu provenance khi suy ra quý |
| 28 | [stefan-jansen/zipline-reloaded](https://github.com/stefan-jansen/zipline-reloaded/blob/943010b9da848e317fc520de87edade2b884d329/README.md) | 1,960 | Engine backtest | Xử lý dữ liệu và hiệu quả chiến lược | R — Không ưu tiên kết nối broker/chiến lược cho MVP |
| 29 | [FinanceData/FinanceDataReader](https://github.com/FinanceData/FinanceDataReader/blob/addcbb7e887f0db6176a87d323de5de28357b5f4/README.md) | 1,554 | Thư viện dữ liệu | Danh mục niêm yết, giá, chỉ số, xuất dữ liệu | R — Nguồn chính Hàn Quốc/quốc tế; không mặc định bao phủ Việt Nam |
| 30 | [thinh-vu/vnstock](https://github.com/thinh-vu/vnstock/blob/88825be3f9aab729362e6fca178eb6e9ae4d3f88/README.md) | 1,412 | Thư viện dữ liệu Việt Nam | BCTC năm/quý và tỷ số qua provider | C — Lựa chọn đáng thử đối chứng; chưa kiểm đủ pilot/nguồn/phiên bản |
| 31 | [theOGognf/finagg](https://github.com/theOGognf/finagg/blob/614631d8e26bdbb21c1a6e6a3a10972a00e1d24b/README.md) | 547 | Thư viện tổng hợp dữ liệu | Raw/refined trong SQL, feature và đối chiếu ngành | R — SEC/FRED khác nguồn Việt Nam; mẫu ngành phải được xác định |
| 32 | [OpenBB-finance/backends-for-openbb](https://github.com/OpenBB-finance/backends-for-openbb/blob/a6293707576e16edda8305adda95b07b6a4b968b/README.md) | 221 | Ví dụ tích hợp — archived | Hợp đồng JSON/widget/bộ chọn dùng chung | R — Repo đã archived ở lần kiểm; dữ liệu ví dụ không là dữ liệu thị trường |
| 33 | [GavrielP1/SALARY-2045](https://github.com/GavrielP1/SALARY-2045/blob/806cdaa821c7a4eb04a0f1bc7cf59c0a30314e0a/README.md) | 47 | Ứng dụng ngách cổ tức | Lịch thu nhập, đóng góp vị thế, mục tiêu thu nhập | R — Sao thấp nhưng sát ngách; dự phóng/score README chưa được thẩm định |
| 34 | [stocknear/frontend](https://github.com/stocknear/frontend/tree/a97f990ea2567303de88279ed020c4f16f4ddbbd) | 44 | Giao diện nền tảng | Chọn chỉ tiêu, bảng/biểu đồ đa chuỗi, earnings guidance | C — Không có README tại commit; frontend không chứng minh backend/nguồn hoạt động |
| 35 | [EmanueleSturzo/portfolio-analytics](https://github.com/EmanueleSturzo/portfolio-analytics/blob/1f98bbce7ec8f14968a2937d4f7d38ae4e1f5658/README.md) | 0 | Dashboard danh mục | Holdings, phân bổ, benchmark, cổ tức | R — Chỉ đọc README đợt này; không chứng minh tính đúng toàn bộ metrics |
| 36 | [sonnymay/dividend-tracker](https://github.com/sonnymay/dividend-tracker/blob/278046c8212131c44e3cd27b9db600fefbe502c2/README.md) | 0 | Ứng dụng ngách cổ tức | Thu nhập và phân bổ theo vị thế | R — Chỉ đọc README đợt này; không kế thừa AI chat/yield dự phóng làm mặc định |

## 3. Định danh và khả năng kiểm lại

Tên cũ OpenBB-finance/OpenBB được GitHub chuyển tới openbq-org/OpenBB; afadil/wealthfolio tới wealthfolio/wealthfolio; robertmartin8/PyPortfolioOpt tới PyPortfolio/PyPortfolioOpt; financedata-org/FinanceDataReader tới FinanceData/FinanceDataReader. Link bằng chứng dùng tên trả về thực tế.

Các lần thử stocknear/stocknear, stocknear/backend, pandas-datareader/pandas-datareader và rqalpha/rqalpha trả 404; không tính là repo đã khảo sát. Sau đó xác định stocknear/frontend, pydata/pandas-datareader và ricequant/rqalpha. Hồ sơ lỗi được giữ để tra cứu. OpenBB-finance/backends-for-openbb có archived=true tại lần kiểm.

[Metadata tổng hợp](evidence/repository-survey.json) ghi sao, forks, SHA, nhánh, archived, giấy phép metadata, mô tả, thời điểm truy xuất và hash từng tệp. Inventory từng thư mục trong [bằng chứng](evidence/github) giữ đường dẫn và cây tệp khi đã truy vấn. Không coi giấy phép metadata là thẩm định đủ quyền tích hợp code; đợt này chỉ chuyển thể ý tưởng.

[Minh chứng mã và bài học](02-minh-chung-ma-va-bai-hoc.md) · [Danh mục UC](../research-platform/27-yeu-cau-chuc-nang-va-vi-du.md).
