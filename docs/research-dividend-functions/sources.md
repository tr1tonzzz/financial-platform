# Sổ nguồn và truy vết nghiên cứu

Kiểm tra ngày 11/10/2026. Repo được đọc ở commit cố định; metadata commit/license và SHA-256 từng file nằm trong inventory. Không dựa vào stars để kết luận chất lượng.

| Dự án | Commit kiểm tra | Snapshot cục bộ |
|---|---|---|
| [oliverbrown/stock_screener](https://github.com/oliverbrown/stock_screener/tree/8c5f8c59d857606dedd991c25e9c510f2d133622) | 8c5f8c59d857606dedd991c25e9c510f2d133622 | [inventory](evidence/github/oliverbrown__stock_screener/inventory.json) |
| [carlosbrown2/dividend-screener](https://github.com/carlosbrown2/dividend-screener/tree/39fc5ad1f20df5dbe540a9256879380f7d7efef9) | 39fc5ad1f20df5dbe540a9256879380f7d7efef9 | [inventory](evidence/github/carlosbrown2__dividend-screener/inventory.json) |
| [neurobloomai/market-tools](https://github.com/neurobloomai/market-tools/tree/c4f44a9c42d49b16e55bca184f00f0e97aebc565) | c4f44a9c42d49b16e55bca184f00f0e97aebc565 | [inventory](evidence/github/neurobloomai__market-tools/inventory.json) |

Nguồn kỹ thuật kiểm tra trực tiếp: stock_screener.py phần saved screens/value-trap/reasons; funcs.py phần đọc spreadsheet và payout; dividend_plays_for_longterm.py phần normalize metrics, dividend_grade, passes_filter và danh sách biên tập rủi ro. Tên/path/function giúp mở lại bằng chứng; các suy luận áp dụng Việt Nam được viết riêng trong tài liệu 06. [Script thu nguồn](../../scripts/research/fetch_dividend_function_sources.py) chạy lại sẽ thu commit hiện tại, không thay đổi nghĩa commit đã trích dẫn; muốn làm đợt mới phải lưu directory/version khác trước khi chạy, tránh ghi đè bằng chứng đợt này.

Nguồn trước dùng lại: [FinanceToolkit công thức solvency](https://github.com/JerBouma/FinanceToolkit/blob/37ed6f01465b4bfb6718b07e1d65826734f53337/financetoolkit/ratios/solvency_model.py#L267), [Dividend CLI adjustment](https://github.com/Santhosh-004/dividend-cli/blob/7c6033b11db694eb101d2b27217441c7184e9c4f/dividend_calculator/utils.py#L173), [OpenBB splits schema](https://github.com/OpenBB-finance/OpenBB/blob/ae0268771f761b036996d81bd21522ce79d95415/openbb_platform/core/openbb_core/provider/standard_models/historical_splits.py), [Ghostfolio concentration rule](https://github.com/ghostfolio/ghostfolio/blob/8fa4f6a6739afee82461b3aa48f47dfa6a396dc8/apps/api/src/models/rules/account-cluster-risk/current-investment.ts#L33). Xem [sổ nguồn đợt trước](../research-github-dividend/sources.md) cho chín repo đầy đủ.

| Nguồn Việt Nam | Nội dung xác minh / giới hạn |
|---|---|
| [DHG BCTC kiểm toán 2025](https://dhgpharma.com.vn/sites/default/files/2026-03/DHG-Audited-FS-2025-VN.pdf) | PDF trang 11/in 9, mã 20/21/36; scope công ty; source hash trong real-cases; chép thủ công và tự kiểm, chưa gold độc lập |
| [FPT phát hành tăng vốn, VSDC 14/07/2025](https://vsdc.vn/vi/ad1/184974) | 20:3, record 22/07/2025, floor/hủy phần lẻ; không tự cung cấp mọi ngày basis |
| [FPT đăng ký bổ sung, VSDC 26/08/2025](https://vsdc.vn/vi/ad1/186572) | Đăng ký thêm cổ phiếu; không tự chứng minh credit/trade date hoặc entitlement tài khoản |
| [FPT cổ tức còn lại 2024](https://vsdc.vn/vi/ad1/183589) | Một đợt tiền mặt, khác profit_year đợt 2025 |
| [FPT tạm ứng đợt 1 năm 2025](https://vsdc.vn/vi/ad1/189195) | Một đợt tiền mặt; không total annual DPS hoặc confirmed receipt |

Từ mã nguồn tham khảo tới yêu cầu Việt Nam là **suy luận thiết kế**, chưa là hiệu quả đã đo. Không tải hoặc tái sử dụng media từ website; nguồn PDF DHG đã có trong hồ sơ dự án, ảnh dùng để kiểm số liệu. Không lấy thông báo quyền làm bằng chứng cổ tức đã thực nhận.
