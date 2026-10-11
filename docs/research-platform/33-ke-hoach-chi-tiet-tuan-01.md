# Kế hoạch chi tiết tuần này — UC-1 cơ bản và tích hợp Paddle

Ngày lập: **11/10/2026**. Tuần 1 làm tiếp theo [kế hoạch 10 tuần, nội dung v6](32-ke-hoach-10-tuan-tiep-theo.md); ngày bắt đầu chọn trong [checklist HTML](checklist-10-tuan-v4.html). **24 giờ dự toán**, chưa phải giờ đã làm; tăng 8 giờ so pilot để dựng FastAPI/PostgreSQL và nối React.

**Đầu ra là web local React + FastAPI + PostgreSQL.** Script xử lý PDF/OCR được tái sử dụng trong backend; chưa xây ứng dụng desktop/mobile hoặc một giao diện Streamlit song song. [Stack hiện hành](31-chot-pham-vi-va-stack-paddleocr.md).

**Đích cuối tuần:** một BCTC năm của HPG/VNM/FPT đi được từ tài liệu đến bảng sáu chỉ tiêu đã duyệt hoặc thiếu có lý do; người dùng xem nguồn từng ô và xuất CSV. Paddle thay bước OCR trong pipeline đã thử, không dành tuần này kiểm lại toàn bộ stack.

**Căn cứ Báo cáo 2:** giữ sáu chỉ tiêu nền đã nêu trong báo cáo; xem [từ điển và hợp đồng dữ liệu chi tiết](35-dac-ta-metrics-tu-bao-cao-02.md). Thực nghiệm cũ là **LNST/CFO/tiền chi cổ tức × hai kỳ**, không phải đã trích đủ sáu chỉ tiêu nền. Không chọn lại metrics hoặc lấy kết quả Tesseract cũ làm số đo Paddle. [Tuần 2 chi tiết](34-ke-hoach-chi-tiet-tuan-02.md) tiếp nối kho và màn hình tuần này.

### Lát cắt UC-1 và trình tự triển khai

| UC nhỏ | Input → xử lý → output tuần 1 | Tiêu chí kiểm |
|---|---|---|
| F01.1 — Tra cứu doanh nghiệp và hồ sơ cơ bản | Mã trong manifest → tìm hồ sơ → tên/mã và tình trạng dữ liệu | Không nhận nhầm tên doanh nghiệp trong PDF |
| F01.2 — Xem dữ liệu tài chính nhiều kỳ | Mã/năm/scope → truy vấn reviewed facts → bảng sáu trường một năm | Số chưa duyệt không hiện như số chính thức; chưa làm bảng ba năm |
| F01.3 — Chọn và xuất bộ dữ liệu | Bộ chọn một năm → tạo CSV với value/status/source → file đọc lại được | Không mất dấu âm, đơn vị hoặc biến thiếu thành 0 |
| F01.4 — Tra cứu định nghĩa và truy xuất bằng chứng | Chọn ô → tìm metric definition + locator → nghĩa chỉ tiêu và đúng trang/cột PDF | Chỉ mở trang chủ IR không đủ chứng minh nguồn ô |
| F01.5 — Xem độ đầy đủ và phiên bản dữ liệu | Chọn doanh nghiệp/kỳ → tổng hợp tình trạng sáu chỉ tiêu cần cung cấp → xem số đã duyệt, thiếu, chờ duyệt và bản dữ liệu được chọn | Tải được PDF chưa đồng nghĩa có đủ số liệu đã duyệt |
| F01.6 — Thu thập, chuẩn hóa và duyệt dữ liệu tài chính | Người vận hành thu PDF → trích số bằng text/Paddle → chuẩn hóa → đối chiếu và duyệt → cung cấp số liệu cho người dùng | Giữ số gốc, số chuẩn hóa, cách trích, nguồn và lịch sử duyệt |

Tên UC nhỏ dùng **động từ + đối tượng/mục đích thao tác**. F01.5 là thao tác xem của người theo dõi tài chính; F01.6 là chức năng hỗ trợ do người vận hành thực hiện, có thể phân rã tiếp khi code, không phải một UC lớn tên “Nền dữ liệu”.

**Giải thích thuật ngữ:** `target` là một ô số cần cung cấp, ví dụ CFO HPG năm 2025; `candidate` là số máy trích hoặc người nhập nhưng chưa duyệt; `fact` trong luồng này là số liệu đã được duyệt cùng nguồn. Ví dụ đã tải một PDF chứa sáu chỉ tiêu, mới duyệt bốn thì hiển thị **4/6 đã duyệt**, hai ô còn lại ghi chờ duyệt hoặc thiếu đúng tình trạng, không báo đã có đủ dữ liệu.

Tên module dưới đây là **gợi ý khi viết code**, chưa có nghĩa repository đã triển khai: `ingestion` đọc manifest/tải và lưu tài liệu; `extraction` đọc text/Paddle và chọn dòng/cột; `normalization` đổi đơn vị/dấu; `repository` lưu/truy vấn PostgreSQL; `review` kiểm và ghi audit; `ui` cung cấp bảng/bộ chọn/nguồn/export. Có thể gộp module lúc đầu, nhưng không trộn công thức UC-2 vào parser hoặc tính từ candidate chưa duyệt.

**Tối thiểu schema tuần 1:** `documents/document_versions` giữ URL/hash/kỳ/scope/unit; `candidates` giữ raw/normalized/metric/locator/method/status; `facts` giữ giá trị đã duyệt và tham chiếu candidate/revision; `reviews` giữ hành động, trước–sau/lý do/người/thời điểm. Định nghĩa trường cụ thể ở tài liệu 35; transaction/revision được củng cố tuần 2. UI đọc DB qua truy vấn, không đọc trực tiếp CSV thử nghiệm làm nguồn chính.

## 1. Kế thừa và phần cần viết

| Kế thừa | Việc mới |
|---|---|
| HTTP/download, kiểm PDF/hash, crawler mẫu | Nối một BCTC năm đúng kỳ/scope vào ứng dụng; assisted báo riêng |
| pypdf và Poppler đã thử | Dùng lại đọc/render, chọn đúng trang BCTC năm, không giữ cứng trang 12–14 của VNM quý |
| Ảnh VNM Q1/2026 và kết quả Tesseract | Thử adapter Paddle trên ảnh có sẵn; không dùng quý 2026 thay dữ liệu năm |
| Manifest ba mã/chín báo cáo/54 ô đã chốt | Nối ledger trạng thái thực, không chọn lại doanh nghiệp |
| Định nghĩa sáu trường | Candidate, PostgreSQL tối thiểu, duyệt/sửa, bảng React và CSV |

Mã tham khảo: [demo VNM đang lưu](../../exports/demo1-vnm/README.md), [read_pdf.py](../../exports/demo1-vnm/read_pdf.py), [render_pages.py](../../exports/demo1-vnm/render_pages.py), [crawler](../../scripts/research/crawl_official_reports.py). Script demo có tên file/trang cố định; tách phần tái sử dụng thành hàm nhận đường dẫn và số trang. Crawler cũ chưa tự hỗ trợ FPT chỉ bằng đổi tham số mã.

## 2. Đầu vào tuần này

- [Manifest HPG/VNM/FPT](../../config/pilot-scope.json), sáu trường `net_income_total`, `cfo`, `cash_equivalents`, `total_assets`, `total_liabilities`, `total_equity`.
- Một BCTC năm hợp nhất đã kiểm toán; ưu tiên HPG FY2025 đã thu trong thực nghiệm nếu tệp/hash còn đúng. Có thể chọn VNM/FPT khi nguồn phù hợp hơn, nhưng không đợi đủ chín PDF mới làm màn hình.
- Python 3.12 và stack đã chốt tại [tài liệu 31](31-chot-pham-vi-va-stack-paddleocr.md). Chỉ kiểm/cài phần Paddle còn thiếu hoặc lỗi tương thích thực tế.
- Sáu ô tham chiếu: nhãn, cột, đơn vị, kỳ/scope, trang và số gốc. Đối chiếu cùng người thực hiện phải ghi tự kiểm, chưa là gold độc lập.

## 3. Năm buổi, tổng 24 giờ

| Buổi | Giờ | Nhiệm vụ | Kết quả cần có |
|---|---:|---|---|
| 1 | 3 | W01-01 thay OCR; W01-02 nối manifest/ledger | Adapter Paddle, log thật; ledger chín báo cáo/54 ô đích |
| 2 | 2 | W01-03 chọn BCTC năm, đọc sáu ô | PDF/hash/source, kỳ/scope/unit và ô tham chiếu |
| 3 | 6 | Phần đầu W01-04: schema, migration, services và FastAPI | PostgreSQL, candidates; API đọc danh mục/facts/nguồn |
| 4 | 11 | Phần còn lại W01-04 (4h): API duyệt; W01-05 (7h): web React | API review/export và giao diện đi hết luồng |
| 5 | 2 | W01-06 kiểm luồng, minh chứng, Word/slide | Demo thật, giờ/lỗi và nháp báo cáo đúng kết quả |

### Buổi 1 — Thay đúng bước OCR

1. Xác định interpreter/environment đã dùng, package và công cụ render đã chạy. Không thử lại mọi thư viện hoặc xóa môi trường cũ.
2. Cài PaddleOCR/PaddlePaddle CPU tương thích trong môi trường project; chọn model tiếng Việt. Khóa package/model sau lần chạy thành công.
3. Adapter nhận ảnh, trang và thông tin tài liệu; trả text, bbox, confidence, engine/model và lỗi. Thử ảnh VNM có sẵn trước, rồi dùng trang BCTC năm.
4. Giữ pypdf/Poppler và nhánh text khi dùng được; scan/text không hữu ích đi Paddle. Có chữ không đồng nghĩa chọn đúng số/cột.
5. Nối manifest vào ledger report/metric với trạng thái chưa thu/chưa trích/chờ duyệt/thiếu. Không đánh dấu dữ liệu đã có chỉ vì mã được chốt.

**Timebox:** khoảng 2 giờ ban đầu cho đổi Paddle, 1 giờ ledger. Nếu Paddle lỗi, ghi nguyên nhân và tiếp tục các phần kho/bảng bằng số có nguồn; dành thời gian xử lý lỗi khi cần, không gọi số nhập tay là Paddle đã trích.

### Buổi 2 — Một báo cáo năm, sáu ô thật

1. Kiểm mã, năm/khoảng kỳ, hợp nhất, kiểm toán, đơn vị tại bìa/header/bảng; tên file chỉ là candidate.
2. Giữ PDF gốc, URL, hash, ngày thu; ngày công bố chỉ ghi khi có nguồn, không lấy ngày tải thay thế.
3. Tìm LNST tổng trên KQKD, CFO trên lưu chuyển tiền tệ; tiền/tài sản/nợ/vốn chủ trên bảng cân đối. Ghi nhãn/mã dòng, trang PDF và cột năm.
   - LNST và CFO là số phát sinh cả năm; bốn trường còn lại là số dư cuối năm. Ghi khoảng kỳ/ngày số dư riêng.
   - Tổng LNST hợp nhất không thay bằng LNST cổ đông mẹ; nợ phải trả không thay bằng nợ vay; tiền và tương đương tiền không chỉ lấy dòng tiền.
   - Chọn cột năm hiện tại cho báo cáo đầu; giữ nhãn cột so sánh và “đã phân loại lại” nếu dùng để kiểm chéo.
4. Nhập sáu ô tham chiếu. Không xác định được thì ghi thiếu/mơ hồ và lý do, không tạo số để đủ sáu.
5. Ghi tài liệu dùng phát triển parser; bản dịch/số so sánh/bản sửa gần giống không chuyển sang tập kiểm độc lập.

**Đầu ra:** một báo cáo được xác nhận ngữ cảnh và bảng tham chiếu. Không yêu cầu thu một PDF mỗi mã trước khi dựng UC-1.

### Buổi 3 — Candidate và kho tối thiểu

1. Tìm nhãn và cột từ text/Paddle; giữ số thô và quy tắc chuẩn hóa. Confidence không thay việc kiểm số.
2. Lưu tối thiểu tài liệu/phiên bản, candidate, số đã duyệt và review. Tên bảng/module chọn khi code; schema trong tài liệu chưa là phần đã chạy.
3. Mỗi target giữ mã/metric/kỳ/scope/raw/normalized/unit/source/hash/trang/cột hoặc bbox/extraction method/status/reason.
4. Số tiền dùng integer/Decimal; ngoặc âm giữ dấu, nghìn/triệu chuyển đúng; gạch/cột mơ hồ không thành 0.
5. Đọc lại dữ liệu đã lưu để kiểm metadata còn đầy đủ. Candidate chưa duyệt không xuất lên bảng số chính thức.

**Đầu ra:** DB/candidate của một báo cáo, sáu targets có số hoặc trạng thái. Chưa yêu cầu trích tốt mọi bố cục.

**Phần backend/database cần viết trong buổi này:** cấu hình DB từ môi trường, SQLAlchemy models/session, migration Alembic đầu, services độc lập parser và routes FastAPI. Lệnh batch trích số vào DB dùng chung services; chạy OCR không gắn vào mỗi lần người dùng mở bảng. Tối thiểu kiểm migration trên DB sạch và đọc lại sáu targets qua API.

### Buổi 4 — Duyệt và cung cấp dữ liệu

1. Duyệt/sửa cạnh trang nguồn: giữ số trước–sau, lý do, người/thời điểm và phiên bản; thiếu provenance không publish.
2. React chọn mã/năm/scope, bảng sáu chỉ tiêu có unit/status. Mã/kỳ chưa có dữ liệu hiện chưa cung cấp.
3. Chọn một ô để mở đúng PDF/trang/cột; chỉ mở trang chủ doanh nghiệp chưa đủ truy xuất nguồn ô số.
4. Xuất CSV UTF-8: số reviewed, unit/scope/period/status/source refs. Ô thiếu để trống + lý do, khác số 0 có bằng chứng.
5. Mở lại app và CSV để kiểm số giữ nguyên; phân biệt bước tự động và bước người vận hành sửa/nhập.

**Frontend:** khởi tạo React/TypeScript/Vite; hai khu vực khai thác dữ liệu và duyệt; API client dùng URL cấu hình; có loading/error/empty. Bộ chọn mã/năm/scope giữ nhất quán; đổi bộ chọn phải hủy hoặc bỏ kết quả request cũ. PDF/trang nguồn mở từ API document ID, không dùng đường dẫn máy trực tiếp trong browser.

**API tối thiểu dự kiến, chưa triển khai:**

| Route | Phục vụ |
|---|---|
| `GET /api/issuers`, `/api/metrics` | Bộ chọn ba mã và định nghĩa sáu trường |
| `GET /api/facts?issuer=HPG&years=2025&scope=consolidated` | Reviewed facts và targets thiếu/chờ duyệt; bộ lọc chỉ tiêu tùy chọn |
| `GET /api/facts/{id}/evidence` | Định nghĩa, raw/unit, trang/cột/source và revision |
| `GET /api/documents/{id}/file` | PDF đúng phiên bản, giới hạn vào tài liệu đã ghi nhận |
| `GET /api/candidates`, `POST /api/candidates/{id}/reviews` | Hàng đợi và quyết định duyệt/sửa/từ chối, lý do + expected revision |
| `GET /api/exports/facts.csv` | CSV đúng bộ lọc, do backend tạo từ số chính xác |

Tên routes có thể tinh chỉnh khi code nhưng phải cập nhật OpenAPI/README và giữ hợp đồng dữ liệu. API tiền trả chuỗi Decimal/null; không để React làm tròn số gốc. Review và fact/audit cùng transaction; CORS giới hạn frontend local; chưa coi lựa chọn màn hình “vận hành” là phân quyền nhiều người dùng.

**Đầu ra:** tài liệu→candidate→duyệt→bảng→nguồn→CSV, thay vì chỉ thêm một ảnh OCR vào báo cáo.

### Buổi 5 — Kiểm và chuẩn bị trao đổi

- Chạy luồng thật đến CSV, ghi file/run/config và ảnh.
- Kiểm một ca thiếu/sai cột/đơn vị bằng fixture được gắn nhãn, không trình như số doanh nghiệp.
- Báo số candidate trước và số sau duyệt nếu đã đo. Chưa đo ghi chưa đo; không dùng lại 6/6 ô Tesseract làm kết quả Paddle.
- Ghi giờ thực, lỗi, mức UC-1 đạt và ba việc tiếp theo.

**Kiểm tối thiểu cuối tuần:** (1) sáu targets đối chiếu nhãn/cột/đơn vị/kỳ/scope với nguồn; (2) một fixture ngoặc âm và đơn vị triệu; (3) một ô thiếu/mơ hồ không thành 0; (4) candidate chưa duyệt không publish; (5) sửa số giữ trước–sau; (6) bảng→nguồn→CSV→mở lại giữ đúng giá trị. Ghi input/expected/actual và file/run; số liệu fixture không trình thành số doanh nghiệp thật.

## 4. Đầu ra cuối tuần cần lưu

Các đường dẫn là **đích tạo khi làm**, không phải minh chứng đã tồn tại:

| Đầu ra | Nội dung |
|---|---|
| `workspace/week1/docs/vnm-2025.md` | Nhật ký buổi/giờ/run, kết quả, lỗi, đã chạy/chưa chạy |
| `environment.md` trong hồ sơ thực hiện | Python/packages/model/device/config và thời điểm kiểm |
| `workspace/week1/data/ledger-reports.csv` | Chín báo cáo đích với nguồn/ngữ cảnh/status thực |
| `ledger-targets.csv`, `reference-facts.csv` | 54 ô đích; sáu ô tham chiếu đầu với locator/cách kiểm |
| PDF/ảnh, `ocr-runs/`, DB, CSV | Nguồn/hash/engine/text/bbox/errors; candidate/review/audit; CSV mở lại được |
| Ảnh/demo UC-1 | Bảng sáu trường, ô truy nguồn, lần duyệt/sửa và CSV |

`workspace/week1/data/` bị Git-ignore, cần sao lưu riêng. Theo yêu cầu tiếp của người thực hiện, code và hồ sơ tuần 1 tập trung tại `workspace/week1/`; nội dung kế hoạch hiện là v6. Hồ sơ DB gồm schema/migration và bản dump PostgreSQL; không coi một file SQLite cũ là DB hiện hành. Lưu lock frontend/backend, OpenAPI và README chạy ba thành phần khi đã thực hiện.

## 5. Gợi ý Word và slide

**Word:** “Triển khai UC-1 khai thác dữ liệu trên một BCTC năm”. Khoảng 1–2 trang nháp tuần; gộp cùng tuần 2 khi báo cáo định kỳ.

1. **Mục tiêu/kế thừa:** báo cáo/sáu trường; tải/text/render đã thử; thay bước OCR và ghép ứng dụng.
   - Kế thừa bảng dữ liệu của Báo cáo 2; làm rõ mẫu cũ đối chiếu ba dòng × hai kỳ, còn tuần này cung cấp sáu chỉ tiêu nền của một BCTC năm.
2. **UC đã thực hiện:** input→candidate→duyệt/lưu→bảng/nguồn/CSV; file/code/run và 2–3 ảnh thật, không viết lại lý thuyết OCR dài.
3. **Kết quả/giới hạn:** số có/thiếu, lỗi, trước/sau review nếu đã đo, giờ và assisted; ba đầu ra tuần 2.

**Slide: bốn slide, mỗi slide một ý.**

| Slide | Nội dung | Minh chứng |
|---|---|---|
| 1 | UC-1 tuần này: BCTC năm→bảng sáu chỉ tiêu có nguồn | Mã/kỳ/scope và mục tiêu một câu |
| 2 | Giữ tải/text/render, OCR đổi Paddle | Sơ đồ ngắn và engine/model từ log thật |
| 3 | Người dùng khai thác dữ liệu thế nào | Bảng→ô số→trang nguồn; ưu tiên demo |
| 4 | Kết quả, lỗi và kế hoạch tuần 2 | Số đếm/giờ thật, tối đa ba việc tiếp |

**Demo 2–3 phút:** chọn mã/năm→bảng→ô số/nguồn→CSV. Mở log khi cần chứng minh Paddle; nếu dùng số nhập có nguồn phải nói rõ. **Trao đổi với thầy:** UC-1 đã đủ cơ bản chưa; nên ưu tiên trích số hay thao tác truy nguồn?

## 6. Điều kiện kết thúc

- [ ] W01-01: adapter Paddle chạy được và log đúng engine/model.
- [ ] W01-02: manifest nối ledger trạng thái thực.
- [ ] W01-03: BCTC năm đúng phạm vi, sáu ô tham chiếu có số/thiếu rõ.
- [ ] W01-04: candidate→PostgreSQL→duyệt/sửa có nguồn chạy được.
- [ ] W01-05: bảng→truy nguồn→CSV dùng được.
- [ ] Luồng trên được thực hiện bằng browser React → FastAPI → PostgreSQL, không chỉ mở CSV hay script riêng; API và migration có minh chứng chạy.
- [ ] W01-06: có log/ảnh, giờ/kết quả kiểm và nháp Word/slide đúng phần đã làm.

Paddle chưa đạt nhưng bảng dùng được bằng số thủ công thì báo **UC-1 demo một phần; tích hợp OCR chưa đạt**, không tick cả tuần hoàn thành. Tuần 2 củng cố revision/review, mở bố cục và ba năm công ty đầu để tuần 3 làm UC-2; mốc demo ba UC cuối tuần 4 giữ nguyên.

