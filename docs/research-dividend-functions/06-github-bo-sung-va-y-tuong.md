# Nghiên cứu GitHub bổ sung và ý tưởng thực tế cho Việt Nam

Ngày 11/10/2026. Tiếp nối chín dự án ở [đợt trước](../research-github-dividend/01-khao-sat-du-an-va-bang-chung.md); đợt này thêm ba repository, tổng **12 repository khác nhau**. Đã tải metadata/tree và đọc code ở commit cố định, không cài/chạy dự án. Đây là bằng chứng về cách triển khai và rủi ro dữ liệu, chưa chứng minh có người dùng Việt Nam cần hoặc hiệu quả đầu tư. Nguồn/commit/license/hash ở [sources](sources.md) và inventories.

## Những gì xác minh được từ code

| Dự án / bằng chứng | Ý tưởng có thể chuyển sang FAP | Điều phải thay khi áp dụng Việt Nam |
|---|---|---|
| [oliverbrown/stock_screener](https://github.com/oliverbrown/stock_screener/blob/8c5f8c59d857606dedd991c25e9c510f2d133622/stock_screener.py#L1680): `load_screens`, `apply_screen`, hai file cấu hình; phần lý do/value trap tại khoảng 1280–1340 | Lưu bộ tiêu chí cá nhân, giải thích mỗi hồ sơ, cảnh báo theo điều kiện | Không sao chép nhãn buy/sell, ngưỡng Mỹ hay Yahoo FCF; dùng reviewed facts, period/scope/unit và unknown. Không mặc định ETF/ADR giống cổ phiếu phi tài chính Việt Nam |
| [carlosbrown2/dividend-screener](https://github.com/carlosbrown2/dividend-screener/blob/39fc5ad1f20df5dbe540a9256879380f7d7efef9/funcs.py#L6): đọc Dividend Champions, `clean_data` suy EPS từ Price/P-E và annualized payout từ Current Div×Payouts/Year | Xem lịch sử/chính sách nhiều chiều và cohort người dùng chọn | Không có sẵn danh sách Champions Việt Nam; thông báo theo đợt không mặc định trả quý. Không dùng chuỗi suy ngược EPS/payout khi thiếu price basis hoặc EPS phù hợp |
| [neurobloomai/market-tools](https://github.com/neurobloomai/market-tools/blob/c4f44a9c42d49b16e55bca184f00f0e97aebc565/dividend_plays_for_longterm.py#L312): lấy Yahoo metrics, `dividend_grade`, `passes_filter`; tập RISKY_COVERAGE_TICKERS được gán thủ công | Tách tiền tạo ra, chất lượng và điểm cần đọc; cân nhắc loại doanh nghiệp khi đánh giá | Code có nhiều `or 0` và heuristic yield, nên không lấy missing=0 hay điểm A+ làm chuẩn; danh sách rủi ro có biên tập thủ công, không phải mô hình tự phát hiện đã kiểm định |

Hai hướng nghiên cứu đáng giữ: criterion có thể cấu hình và hồ sơ giải thích bằng dữ liệu. Phần cần tránh: trọng số không kiểm định, lấy lịch trả Mỹ áp cho Việt Nam, biến số thiếu thành 0, dùng nhãn rủi ro biên tập như kết quả thuật toán. Các tên cảnh báo ở repository là lựa chọn tác giả, không là kết luận FAP về mã Việt Nam.

## Ý tưởng mới hoặc làm rõ hơn sau lần khảo sát này

| Mã / nhu cầu | UC lớn và cách làm | Dữ liệu / test tối thiểu | Mức ưu tiên và tính mới |
|---|---|---|---|
| H01 — Bộ tiêu chí thẩm định dùng lại | BUC04: lưu/version bộ lọc, mô tả mục đích, chỉ metric trong registry | Facts/basis/coverage; mở lại cho đúng tập/as_of và trạng thái | Cao; làm sâu G01, đã vào D09–D10; chưa là chức năng độc lập thứ tư |
| H02 — Danh sách vấn đề cần bổ sung bằng chứng | BUC05: issue “thiếu CAPEX”, “scope khác”, “basis chưa xác định”; giao tác vụ cho chính người dùng local, đánh dấu xử lý bằng nguồn | Reason từ metric, note/task/evidence; giải quyết issue không tự sửa facts | Cao; làm sâu G01 vào D11, tránh hồ sơ chỉ có biểu đồ |
| H03 — Tra soát khác biệt giữa nguồn/phiên bản | BUC01/05: bảng trước–sau, nguồn ưu tiên, review chọn revision, xem nhận xét nào chịu ảnh hưởng | Fact versions/lineage, active revision; bản sửa không xóa lịch sử | Trung bình; FR18 đã giữ revisions, mới ở task ảnh hưởng/luận điểm. Tái nối G07 đợt trước; chưa đưa tự động vào D01–12 |
| H04 — Hồ sơ chi trả đều đặn với độ đầy đủ | BUC03/04: đếm năm có thông báo tiền mặt trong cửa sổ đã rà, năm không đủ cơ sở tách riêng | Annual coverage, profit_year, basis; thử missing khác “không công bố sau rà soát” | Trung bình; mở rộng dữ liệu ≥5 năm trước khi gọi chuỗi ổn định. Giai đoạn hiện tại 3 năm chỉ mô tả cửa sổ, không danh hiệu dividend champion |
| H05 — Tra soát lợi suất cao do giá giảm hay DPS tăng | BUC02/04: khi đã bổ sung giá cùng thời điểm, phân rã thay đổi yield theo DPS/price, liên kết G02 | Giá/basis/date, trailing cash dividends complete; special dividend và partial riêng | Sau pilot; làm sâu G08 cũ, cần nhánh dữ liệu giá. Không cộng tỷ lệ trên mệnh giá với yield thị trường |
| H06 — Kiểm lại hồ sơ khi luận điểm hết dữ liệu hỗ trợ | BUC05: metric đổi khiến criterion pass→fail/unknown thì yêu cầu đọc lại note | Dossier frozen/current, dependency refs, revision diff; không đổi kết luận người dùng tự động | Sau pilot; liên quan G07, giá trị là giảm bỏ sót khi công bố sửa. Chưa cần email, job nền hoặc đa người dùng |

G05/G06/G09/G10 ở đợt trước vẫn là hướng theo dõi thu nhập và kịch bản: có tính ứng dụng nhưng cần vị thế/quyền/giá hoặc dữ liệu thực nhận. Không đưa chúng vào cùng pilot chỉ để danh mục chức năng dài hơn. H01/H02 được hợp nhất vào G01; H03/H06 dùng một nhánh quản lý thay đổi; H04/H05 là ứng viên sau khi chứng minh dữ liệu đủ. Tránh đếm cùng một ý tưởng hai lần bằng hai tên.

## Xác minh nhu cầu trước khi mở phạm vi

Tạo prototype tác vụ và hỏi người dùng thực hiện quyết định “đọc hồ sơ nào, cần kiểm tra gì tiếp”; không chỉ hỏi có thích giao diện. Một nhu cầu mới được ưu tiên khi có ca Việt Nam kiểm chứng, dữ liệu khả dụng, tác vụ cụ thể và cách đo lỗi/công sức. Lịch chi trả, phần lẻ, năm lợi nhuận và dữ liệu chỉnh basis phải kiểm từ công bố chính thức. Dữ liệu vendor có thể làm nguồn discovery/đối chiếu nhưng chưa thay reviewed source. License trong inventory phục vụ quyết định tái sử dụng sau này; nghiên cứu này đề xuất thiết kế độc lập và không tích hợp code tải về vào ứng dụng.
