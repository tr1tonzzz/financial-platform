# Báo cáo phiên làm việc: thu thập theo danh mục và tích hợp code lõi vào src

**Ngày:** 12/10/2026 — giờ Việt Nam. **Project:** Financial Analysis Platform.

## 1. Kết quả và mức sẵn sàng của code

Đã sửa luồng thành **đọc danh mục chính thức → lọc/chọn báo cáo → tải/kiểm PDF → Paddle phát hiện/crop → VietOCR → trích/chuẩn hóa → PostgreSQL → đọc lại**. Phạm vi thực nghiệm: VNM và HPG, BCTC hợp nhất năm 2025, sáu chỉ tiêu mỗi báo cáo.

**Code triển khai đã chuyển vào src:** collection, cache, parser, Paddle/VietOCR service, ORM/migration/repository/persistence và điều phối. Cấu hình nguồn và kiểm thử đã về thư mục chung; package có pyproject và entry point chạy package độc lập. Các phiên sau nâng cấp trên bộ code này, không tạo collector/parser mới theo tuần hoặc phiên.

**Đã xử lý phần trước đây còn để lại workspace:** runner nhận workspace/model/config từ PipelineSettings; interpreter lấy từ profile; engine/session chỉ khởi tạo khi gọi Database, được dispose sau bước migrate/lưu. Import module không kết nối PostgreSQL hoặc nạp Torch/Paddle. Việc phụ thuộc workspace trước đây là điểm phải refactor trong phạm vi đã giao, không phải lý do chờ phiên khác. API/giao diện và quy trình duyệt/công bố chưa nằm trong lát cắt hiện hành.

Báo cáo được soạn theo yêu cầu của người thực hiện. Bảng số liệu/thống kê được code tạo từ CSV đọc lại database, JSON provenance, log chạy và kết quả kiểm thử. Nội dung diễn giải không phải bộ số chuẩn độc lập. Không đổi hash/provenance cũ để gọi kết quả cũ là chạy bằng code mới.

## 2. Hợp đồng đầu vào và quyết định nghiệp vụ

- Đầu vào thường lệ: công ty và năm; hiện hỗ trợ báo cáo năm, hợp nhất, đã kiểm toán, tiếng Việt. URL danh mục, tên pháp lý, adapter và host tải được đăng ký theo công ty một lần.
- URL PDF phải là kết quả discovery, không đặt sẵn trong code hoặc yêu cầu nhập lại mỗi lần chạy.
- Đọc đủ phạm vi danh mục đã khai báo/quan sát trước khi kết luận có hoặc không có báo cáo. Một liên kết tìm thấy chưa chứng minh đã duyệt đủ.
- Phân biệt năm báo cáo với ngày đăng tải; báo cáo 2025 có thể công bố năm 2026. Không suy kỳ từ thư mục upload.
- Phân biệt năm/quý/bán niên, hợp nhất/riêng lẻ/công ty mẹ, kiểm toán/soát xét/chưa kiểm toán, ngôn ngữ và báo cáo/giải trình/tổng quan.
- Không chọn ngày mới nhất đơn thuần khi có nhiều tài liệu cùng mục tiêu. Code chỉ ưu tiên một bản điều chỉnh có dấu hiệu rõ và ngày công bố sau các bản còn lại; nếu không xác định được thì trả trạng thái mơ hồ.
- Đọc tất cả trang PDF, không đặt danh sách trang hoặc tọa độ riêng theo công ty. Chỉ giữ sáu chỉ tiêu và evidence liên quan cho database.

## 3. Nghiên cứu nguồn thực trước khi triển khai

### 3.1. Vinamilk

Trang danh mục có liên kết PDF trong HTML trả về. Số trang nằm trong payload Next.js; adapter đọc chuỗi JSON, không thực thi JavaScript. Query page được kiểm tra từ thành phần phân trang của website; query năm được giữ khi chuyển trang. Nếu pageCount thiếu/mâu thuẫn, code dừng thay vì giả định độ phủ đầy đủ.

Danh mục gắn nhãn Q4 và trạng thái soát xét/kiểm toán dùng chung cho cả liên kết bản kiểm toán năm 2025. Code giữ nhãn gốc, chọn candidate phù hợp và yêu cầu xác minh kỳ năm trong PDF bằng OCR. Metadata danh mục chưa là kết luận về nội dung tài liệu.

### 3.2. Hòa Phát

Danh mục có phân trang, nhóm cha/con và liên kết tên tài liệu trùng với Download. Adapter đọc tên/ngày công bố trong item tương ứng, loại trùng liên kết và duyệt các trang quan sát được. Trong lần chạy thực đã đọc đủ 24 trang.

Gặp một PDF lịch sử được gắn metadata khác nhau ở nhiều trang. Code ghi nhận mâu thuẫn ngoài mục tiêu trong thống kê, không dùng nó để chọn/chặn báo cáo 2025. Nếu mâu thuẫn liên quan đến candidate mục tiêu, code dừng với lý do rõ.

### 3.3. Kiến trúc được chọn

Adapter giải quyết cấu trúc website; quy tắc lọc kỳ/phạm vi/kiểm toán/ngôn ngữ và lựa chọn phiên bản dùng chung. Nguồn mới cần đăng ký và có adapter tương thích, không cần điền lại URL PDF theo từng năm hoặc sửa số tài chính theo từng tài liệu. Hai nguồn đã kiểm chứng không chứng minh hỗ trợ mọi website.

| Báo cáo | Danh mục đăng ký | PDF gốc |
|---|---|---|
| VNM 2025 | [Danh mục chính thức](https://www.vinamilk.com.vn/investor/reports/financial) | [PDF](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/raw/ee996ffcb87f0699a59c20b102082666f6716fcf9be8ee314ad2de055f79c940.pdf) |
| HPG 2025 | [Danh mục chính thức](https://www.hoaphat.com.vn/quan-he-co-dong/bao-cao-tai-chinh) | [PDF](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/raw/f38c5f75becf7d3f145d27183eec81f119fd4f75e378b983a2763ddc3f7e0c07.pdf) |


## 4. Luồng: đầu vào, xử lý và đầu ra

| Bước | Đầu vào | Xử lý | Đầu ra |
|---|---|---|---|
| Discovery | Đích công ty/năm và cấu hình nguồn | Đọc HTML, nhận diện liên kết, duyệt phân trang, ghi độ phủ | Metadata candidate và quan sát HTTP |
| Lựa chọn | Candidate và tiêu chí | Loại ngoài phạm vi, phân biệt phiên bản; dừng nếu mơ hồ | Candidate được chọn và lý do |
| Tải/kiểm PDF | URL do discovery tìm | Kiểm host/redirect, giới hạn dung lượng, signature/structure/encryption và SHA-256 | PDF gốc và thông tin nguồn |
| Paddle | Toàn bộ trang PDF | Render 180 DPI; phát hiện vùng chữ, crop có đệm, lưu hình học/hash | Crop và metadata tạm |
| VietOCR | Crop do Paddle tạo | Đọc text tiếng Việt; chia dòng dài tại khoảng trắng; kiểm cache | Text/confidence/tọa độ tạm |
| Trích/chuẩn hóa | OCR toàn tài liệu | Kiểm ngữ cảnh; tìm bảng, đơn vị, cột, dòng; chuẩn hóa VND và kỳ | Sáu ứng viên kèm evidence |
| Persistence | Ứng viên và provenance | Giao dịch PostgreSQL; session mới đọc lại so giá trị/evidence | Database và CSV đọc lại |
| Cleanup | Lần lưu/đọc lại thành công | Xóa thư mục xử lý tạm trong workspace | PDF, dữ liệu cần thiết và log |

Điều phối Paddle tự chia toàn bộ PDF thành lô tối đa 10 trang, mỗi lô là tiến trình riêng nhằm giới hạn bộ nhớ; đây là kích thước xử lý, không là danh sách trang chọn thủ công. --detection-batch-pages thay kích thước lô. Metadata được gộp chỉ khi PDF/code/model/config/runtime khớp; bước lưu vẫn đòi đủ mọi trang. Lần chạy đơn tiến trình sau refactor đã gặp lỗi hết dung lượng tại trang 42; chưa lưu báo cáo thiếu trang vào database. Sau chia lô, VNM đã OCR đủ 63 trang nhưng bước lưu gặp lỗi trùng tên module/biến detection; lỗi xảy ra trước transaction. Đã sửa alias, bổ sung kiểm thử nhánh lưu thành công và chạy tiếp từ OCR có hash phù hợp; không sửa số đầu ra hoặc provenance cũ.

Paddle chỉ phát hiện/crop; text do VietOCR nhận diện. Không dùng text native PDF hoặc recognizer Paddle làm đầu ra OCR mới. PyMuPDF dùng để kiểm/render PDF.

Parser dùng tên/mã số chỉ tiêu, tiêu đề bảng và vị trí tương đối của cột. Đã xử lý mã trước/sau tên, mã gộp vào tên, tên xuống dòng, cột hiện tại bên phải và tiêu đề thuyết minh có lỗi OCR. Thiếu/mâu thuẫn ngữ cảnh, đơn vị, cột hoặc số giữ null/lý do; không thay số thiếu bằng 0.

## 5. Code sau tích hợp vào project

| File hiện hành | Vai trò |
|---|---|
| [models.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/src/financial_pipeline/collection/models.py) | Đích báo cáo, phân loại và chọn phiên bản. |
| [adapters.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/src/financial_pipeline/collection/adapters.py) | DOM danh mục VNM/HPG và phân trang. |
| [transport.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/src/financial_pipeline/collection/transport.py) | HTTP giới hạn dung lượng, timeout/retry và redirect. |
| [service.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/src/financial_pipeline/collection/service.py) | API collect_report: discovery → chọn → tải/kiểm PDF → lưu nguồn. |
| [cache.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/src/financial_pipeline/cache.py) | Kiểm điều kiện dùng lại detection/OCR. |
| [parser.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/src/financial_pipeline/extraction/parser.py) | Tìm bảng/cột/dòng, trích sáu chỉ tiêu, xác định kỳ và VND. |
| [report-sources.json](C:/Users/admin/Documents/GitHub/financial-analysis-platform/config/report-sources.json) | Cấu hình nguồn theo công ty, không đặt URL PDF. |
| [settings.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/src/financial_pipeline/settings.py) | Context cấu hình và kiểm đường dẫn thư mục tạm. |
| [pipeline.json](C:/Users/admin/Documents/GitHub/financial-analysis-platform/config/pipeline.json) | Workspace, interpreter, model/config, file database env và nguồn. |
| [repository.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/src/financial_pipeline/storage/repository.py) | Transaction, idempotency theo nội dung, Decimal và đọc lại bằng session mới. |
| [migrate.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/src/financial_pipeline/storage/migrate.py) | Áp dụng migration với engine/connection của caller. |
| [verify_pipeline.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/scripts/verify_pipeline.py) | Sinh kết quả kiểm thử và đối chiếu trực tiếp PostgreSQL với đầu ra/provenance. |
| [pyproject.toml](C:/Users/admin/Documents/GitHub/financial-analysis-platform/pyproject.toml) | Đóng gói src layout; cài editable từ project root. |
| [run_pipeline.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/scripts/run_pipeline.py) | Điều phối; collect-only, resume, keep-temporary. |
| [cli.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/src/financial_pipeline/cli.py) | CLI gọi collection service của src. |
| [detection.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/src/financial_pipeline/ocr/detection.py) | Runner render/Paddle/crop. |
| [recognition.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/src/financial_pipeline/ocr/recognition.py) | Runner VietOCR và cache vùng chữ. |
| [setup_local_database.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/scripts/setup_local_database.py) | Bootstrap PostgreSQL phát triển trên máy hiện tại; chạy rõ ràng ngoài pipeline. |
| [service.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/src/financial_pipeline/storage/service.py) | Kiểm OCR/provenance, gọi parser src, lưu/đọc lại/dọn tạm. |
| [models.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/src/financial_pipeline/storage/models.py) | ORM và ràng buộc. |
| [database.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/src/financial_pipeline/storage/database.py) | Factory Database; nhận URL/file env rõ ràng, không đọc env/mở engine khi import. |
| [001_collection_pipeline.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/src/financial_pipeline/storage/migrations/versions/001_collection_pipeline.py) | Migration schema bốn bảng. |
| [test_collection.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/tests/financial_pipeline/test_collection.py) | Kiểm thử collection và các lỗi nguồn. |
| [test_parser.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/tests/financial_pipeline/test_parser.py) | Kiểm thử parser trên bố cục giả lập. |
| [test_processing_cache.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/tests/financial_pipeline/test_processing_cache.py) | Kiểm thử tính hợp lệ cache. |
| [test_live_processing.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/tests/financial_pipeline/test_live_processing.py) | Ca opt-in trang PDF thật; mặc định skip. |
| [test_storage.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/tests/financial_pipeline/test_storage.py) | Kiểm thử PostgreSQL trong schema tạm. |

```text
src/financial_pipeline/
    __main__.py       # lệnh python -m financial_pipeline
    collection/
    extraction/
    ocr/             # detection.py, recognition.py
    storage/         # database, models, repository, service, migrations
    cache.py
    settings.py
    pipeline.py
    cli.py
config/              # pipeline.json, nguồn, cấu hình/model/package locks
scripts/             # CLI mỏng và bootstrap PostgreSQL local
pyproject.toml
tests/financial_pipeline/
var/                 # dữ liệu chạy, không là source code
    runtime/         # interpreter, weights, PostgreSQL, processing tạm
    data/
        raw/         # PDF gốc
        processed/   # số ứng viên, nguồn và CSV đọc lại PostgreSQL
        runs/        # nhật ký do pipeline sinh
```

Các runner cũ và db.py đã bỏ; không còn code nghiệp vụ ở workspace. Profile `config/pipeline.json` xác định workspace, hai interpreter, model directory/weights, config/lock, database env và source registry. Đổi nơi chạy bằng profile; không sửa các thuật toán. Dữ liệu và credentials vẫn ở runtime bị ignore, không đưa vào src.

API service: `detect_report(work_dir, settings, pages='all', dpi=180, append=False)`, `recognize_report(work_dir, settings, pages='all')`, `persist(source, rows, summary, sessions)`, `store_report(work_dir, settings, sessions, cleanup=False)`, `upgrade_schema(engine)`. Caller tạo Database bằng URL/file env và quản lý vòng đời bằng context manager. Migration giữ revision 001 và dùng connection do caller truyền; pipeline không tự tạo/reset cluster. File lock là đầu vào kiểm model; bước lưu không còn sửa lock để ghi kết quả smoke test.

Module được chuyển, không copy thành hai implementation. CLI/kiểm thử đã đổi import và cấu hình sang vị trí canonical. Hash collection/parser khớp byte với bản đã tạo các số trước chuyển. Import package từ ngoài repository cũng trỏ về src của project.

| Phần | Đã đưa src? | Mức sẵn sàng và việc tiếp theo |
|---|---|---|
| Collection | Có | Baseline cho hai nguồn đã kiểm chứng; thêm adapter/ca kiểm thử khi đăng ký nguồn mới |
| Parser/chuẩn hóa | Có | Baseline sáu chỉ tiêu và bố cục đã thử; cần đánh giá tài liệu chưa dùng để chỉnh rule |
| Cache | Có | Kiểm document, độ phủ, file hash, code/model/runtime; nâng cấp trên module hiện có |
| Runner Paddle/VietOCR | Có | detect_report/recognize_report nhận work_dir và settings; model nạp khi gọi; hai interpreter tách biệt qua profile |
| ORM/migration/persistence | Có | Database factory, session truyền vào repository/service; migration nhận engine/connection; giữ schema/lịch sử hiện có |
| API/giao diện/duyệt | Chưa | Ngoài phạm vi đã giao |

Đưa lõi vào src xác định nơi phát triển chính thức, không đồng nghĩa đã hỗ trợ mọi báo cáo hoặc hoàn thành sản phẩm. Code nằm trong working tree; chưa commit/push hay phát hành release trong phiên này.

## 6. Kết quả thực nghiệm

### 6.1. Độ phủ

| Báo cáo | Trang danh mục | URL PDF đã xem metadata | Candidate | Trang PDF OCR | Có giá trị / mục tiêu | Run database |
|---|---:|---:|---:|---:|---:|---:|
| VNM 2025 | 1/1 | 22 | 1 | 63/63 | 6/6 | 10 |
| HPG 2025 | 24/24 | 230 | 1 | 53/53 | 6/6 | 11 |


Số URL danh mục là metadata đã xem xét, không phải số PDF tải. Chỉ hai PDF đích được giữ trong raw, chống trùng theo nội dung. Có đủ sáu giá trị mỗi mẫu chưa là xác nhận độ đúng độc lập.

### 6.2. Các số hiện hành đọc từ PostgreSQL

| Chỉ tiêu | VNM 2025 — VND | Trang PDF | HPG 2025 — VND | Trang PDF |
|---|---:|---:|---:|---:|
| LNST tổng hợp nhất | 9.413.589.732.469 | 10 | 15.514.931.571.606 | 10 |
| CFO | 8.668.137.048.520 | 12 | 17.365.859.056.591 | 11 |
| Tiền và các khoản tương đương tiền | 1.794.879.718.871 | 7 | 8.300.890.304.205 | 7 |
| Tổng tài sản | 53.312.370.717.301 | 8 | 257.899.200.817.547 | 8 |
| Nợ phải trả | 18.829.355.431.194 | 9 | 126.679.189.940.972 | 9 |
| Vốn chủ sở hữu | 34.483.015.286.107 | 9 | 131.220.010.876.575 | 9 |


Đơn vị VND, số trang PDF bắt đầu từ 1. LNST là tổng LNST hợp nhất, không riêng phần cổ đông công ty mẹ. LNST/CFO là số cả năm; bốn chỉ tiêu bảng cân đối tại 31/12/2025. CAPEX, EPS/DPS và tiền chi cổ tức chưa được trích trong lát cắt này.

**Toàn bộ 12 số vẫn pending_review.** Chưa có người phê duyệt hoặc bộ số chuẩn độc lập. Run 10/11 là hai run hiện hành trong bảng; run 8/9 giữ là lịch sử trước refactor; database còn lịch sử. Không lấy tổng bản ghi lịch sử để báo đã hoàn thành cohort HPG/VNM/FPT 2023–2025.

### 6.3. Mốc chạy và việc chuyển src

| Lần chạy | Phạm vi | Thời điểm Việt Nam | Diễn giải |
|---|---|---|---|
| [Đầy đủ trước refactor](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/runs/20261012T083301940581Z/run.json) | Danh mục → PostgreSQL | 12/10/2026 15:33:01 → 12/10/2026 15:45:00 | OCR đủ hai PDF bằng runner workspace cũ. |
| [Resume trước refactor](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/runs/20261012T084925169013Z/run.json) | Danh mục → cache → PostgreSQL | 12/10/2026 15:49:25 → 12/10/2026 15:50:01 | Giữ run 8/9; cleanup thành công. |
| [Chuyển collection/parser](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/runs/20261012T091419788044Z/run.json) | Collection-only | 12/10/2026 16:14:19 → 12/10/2026 16:14:38 | Kiểm package và nguồn mới, chưa OCR toàn bộ. |
| [OCR VNM từ src](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/runs/20261012T101725639459Z/run.json) | 63 trang VNM | 12/10/2026 17:17:25 → 12/10/2026 17:28:24 | OCR đủ; bước lưu lỗi trùng tên detection; chưa ghi DB trong lần này. |
| [Hoàn tất từ src](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/runs/20261012T102858655786Z/run.json) | Danh mục → PostgreSQL | 12/10/2026 17:28:58 → 12/10/2026 17:36:52 | VNM dùng OCR hợp lệ từ lần trước; HPG OCR mới đủ 53 trang; lưu run 10/11. |
| [Resume và cleanup](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/runs/20261012T103656781982Z/run.json) | Danh mục → cache → PostgreSQL | 12/10/2026 17:36:56 → 12/10/2026 17:37:29 | Giữ run 10/11; dùng cache đủ hai PDF, dọn processing. |


Sau refactor đã OCR đủ 116 trang bằng service hiện hành trong src: VNM 63 trang được tạo ở lần batch rồi dùng lại đúng hash sau sửa bước lưu; HPG 53 trang được OCR mới trong lần hoàn tất. Lần resume cuối dùng cache 4361 vùng VNM và 4238 vùng HPG, không suy luận lại vùng nào, giữ run 10/11 và dọn processing. Thời gian log gồm network/I/O/cache và khởi tạo tiến trình; không là benchmark độ chính xác hoặc SLA.

Đã kiểm hash của detector/recognizer/parser, config và model, PDF gốc, 12 giá trị/evidence đọc trực tiếp PostgreSQL với CSV/candidates. Giá trị hai run mới không đổi so với run 8/9 trước refactor; không dùng việc khớp lịch sử làm phê duyệt độc lập. Không sửa số đầu ra hoặc đổi provenance của lịch sử để gắn nhãn code mới.

## 7. Kiểm thử và minh chứng

### 7.1. Hồi quy sau chuyển src

Kết quả hồi quy: **52 passed, 1 skipped, 0 failures, 0 errors**. Hai ca opt-in package/nguồn thực và OCR thật đều đạt; xem [live-tests.xml](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/verification/pipeline/live-tests.xml).

- Phân biệt năm báo cáo/năm upload, quý/bán niên/năm, phạm vi, assurance, ngôn ngữ và giải trình.
- Phân trang đủ, pageCount thiếu/quá giới hạn, HTML lặp giữa các trang và liên kết trùng.
- Không có candidate, nhiều phiên bản không rõ quan hệ, bản điều chỉnh rõ, metadata mâu thuẫn và lỗi HTTP.
- PDF giả HTML/hỏng, raw bị thay đổi, chống trùng và giữ phiên bản theo hash.
- Bố cục/mã dòng/cột/đơn vị thiếu; số âm, 0, null, số lớn; không lấy năm so sánh làm năm đích.
- Cache thiếu trang/chưa hoàn tất, ảnh/crop sửa, tham chiếu ngoài work, đổi code/model/runtime/DPI.
- PostgreSQL round-trip, idempotency, phân biệt refresh danh mục với đổi rule và rollback khi vi phạm ràng buộc. Chặn tập chỉ tiêu thiếu/trùng trước transaction; kiểm service lưu với OCR giả lập và PostgreSQL thật, xuất đúng bốn file và cleanup.
- Profile tại workspace khác; chặn processing/cleanup ngoài thư mục tạm; import service khi không có DATABASE_URL không tạo engine hoặc nạp model.

Kiểm thử lưu dùng schema tạm và số giả lập, không sửa số doanh nghiệp. Minh chứng: [tests.xml](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/verification/pipeline/tests.xml), [tests.log](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/verification/pipeline/tests.log), [test-summary.json](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/verification/pipeline/test-summary.json).

### 7.2. Trang PDF thật sau chuyển src

Đã nhận diện trang PDF 7 của VNM: lần đầu đọc 112 vùng; chạy lại cache 112 vùng. Ca mới kiểm thêm append detection trang 8, metadata giữ đủ trang 7/8. Detection chưa đủ tài liệu bị từ chối cache; lưu database bị chặn và số bản ghi không đổi. [Quan sát ca live](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/runs/live_processing_20261012T103737752226Z/observation.json).

Ca live kiểm recognition một trang và append detection thêm một trang; xác nhận cache, gộp độ phủ và từ chối lưu OCR thiếu trang. Thực nghiệm toàn tài liệu được ghi riêng tại mục 6.3.

### 7.3. Đối chiếu sau tích hợp

Đã đọc lại 12 bản ghi, so CSV/candidates.json, kiểm document/hash/công ty/năm và pending_review. Hash service/parser/config/model khớp code đang chạy; 12 giá trị không đổi so với lịch sử trước refactor. Tổng tài sản = nợ phải trả + vốn chủ sở hữu khớp ở cả hai doanh nghiệp; đẳng thức này không thay kiểm từng chữ/số trên PDF.

Minh chứng: [observation.json](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/verification/pipeline/observation.json). Chưa đo CER/WER, độ đúng từng chỉ tiêu trên tập độc lập hoặc đối chứng Tesseract trong luồng mới. Confidence VietOCR không được coi là tỷ lệ chính xác đã kiểm chứng.

## 8. File đầu ra, database và cleanup

| File | Nội dung | VNM | HPG |
|---|---|---|---|
| source.json | Nguồn, lựa chọn, độ phủ danh mục và hash. | [Mở](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/processed/VNM-2025-ee996ffcb87f/source.json) | [Mở](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/processed/HPG-2025-f38c5f75becf/source.json) |
| processing.json | Độ phủ OCR, bảng/ngữ cảnh và phiên bản code/model/config. | [Mở](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/processed/VNM-2025-ee996ffcb87f/processing.json) | [Mở](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/processed/HPG-2025-f38c5f75becf/processing.json) |
| candidates.json | Sáu số ứng viên, kỳ, đơn vị, trạng thái/evidence. | [Mở](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/processed/VNM-2025-ee996ffcb87f/candidates.json) | [Mở](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/processed/HPG-2025-f38c5f75becf/candidates.json) |
| database-readback.csv | Số đọc lại PostgreSQL, trang và run ID. | [Mở](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/processed/VNM-2025-ee996ffcb87f/database-readback.csv) | [Mở](C:/Users/admin/Documents/GitHub/financial-analysis-platform/var/data/processed/HPG-2025-f38c5f75becf/database-readback.csv) |


candidates.json giữ kỳ/ngày chốt, raw_value/raw_unit, số VND, trạng thái/lý do, trang/tọa độ, nhãn dòng/tiêu đề cột, model/config/confidence. Không đưa toàn bộ thuyết minh hoặc mọi số OCR vào database.

Bốn bảng: documents (đích), document_versions (PDF theo SHA-256), extraction_runs (lần trích/provenance), candidates (ứng viên). Giá trị NUMERIC(30,0), evidence JSONB. document_versions.source là nguồn ghi nhận đầu tiên; provenance.source của run hiện hành chứa discovery tương ứng. CSV là dữ liệu đọc lại, không là đầu vào điền số vào database.

Giữ PDF gốc, bốn file mỗi báo cáo, quan sát thu thập, log và môi trường/model/database cần chạy. Kiểm tra cuối xác nhận runtime/processing rỗng; workspace không giữ runner/ORM/config cũ hoặc bản implementation thứ hai. Ảnh/crop/OCR tạm và staging sau kiểm tra đã dọn. Không giữ thêm toàn bộ HTML danh mục hoặc tải 230 PDF ngoài mục tiêu. Luồng cũ dùng trang/bố cục cố định giữ trong lịch sử, không dùng làm luồng hiện hành.

data/runtime được ignore trong Git. Package src, cấu hình và test là code project; dữ liệu thực nghiệm/model/database không tự trở thành artifact đã commit. Chưa xác nhận sao lưu ngoài máy cho kết quả mới.

## 9. Thủ công, tự động và quy tắc xuyên suốt

| Phần việc | Cách thực hiện |
|---|---|
| Đăng ký URL danh mục, tên pháp lý, adapter | Cấu hình một lần theo công ty |
| Chọn công ty/năm | Người dùng cung cấp; không nhập từng URL PDF |
| Duyệt/lọc/chọn/tải/kiểm nguồn | Tự động; dừng khi không xác định được |
| Paddle/VietOCR, tìm bảng/cột/dòng, chuẩn hóa | Tự động |
| Lưu/đọc lại, cache và cleanup | Tự động |
| Viết/sửa code, bổ sung adapter/rule | Có Codex hỗ trợ; không gọi là người thực hiện tự viết toàn bộ |
| Điền/sửa trực tiếp số đầu ra | Không thực hiện; sửa code và chạy lại |
| Phê duyệt số đối chiếu PDF | Cần người thực hiện; chưa triển khai quy trình duyệt/công bố |

Quy tắc đã ghi vào [AGENTS.md](C:/Users/admin/Documents/GitHub/financial-analysis-platform/AGENTS.md): nghiên cứu nguồn/hợp đồng/ca biên/lỗi và tiêu chí kiểm chứng trước code; nâng cấp cùng module; không tạo bản thử mới mỗi phiên; không gọi cache là suy luận mới hoặc sửa kết quả để đạt mục tiêu.

## 10. Cách chạy tiếp và giới hạn

Package nhận cấu hình ngoài source; công ty/năm là đầu vào bắt buộc. Ví dụ khi đã cài package và đứng ở thư mục project:

```powershell
python -m pip install .
python -m financial_pipeline --config config/pipeline.json --ticker VNM --year 2025
python -m financial_pipeline --config config/pipeline.json --ticker VNM --ticker HPG --year 2025 --collect-only
python -m financial_pipeline --config config/pipeline.json --ticker VNM --ticker HPG --year 2025 --resume
```

Khi chạy ở thư mục khác, --config nhận đường dẫn tuyệt đối. Cần Python 3.12, dependencies của hai môi trường OCR, model đúng lock và PostgreSQL theo cấu hình. Package không tự tìm config dựa trên vị trí src. Scripts ở repo là công cụ phát triển/kiểm tra; package không gọi file script của repo để xử lý.

Đã build wheel, cài vào thư mục ngoài checkout, loại src gốc khỏi đường dẫn import và kiểm CLI, subprocess, ORM/OCR cùng migration đóng gói. Ca opt-in chạy collector VNM 2025 thật từ bản cài đặt này với cấu hình ngoài repo. Ca OCR sau sắp xếp lại kiểm trang 7 và append detection trang 8; dữ liệu PostgreSQL 12 chỉ tiêu được đối chiếu, không đổi.

Tên hiện hành theo chức năng: config/pipeline.json, src/financial_pipeline, var/data/raw, var/data/processed, var/data/verification/pipeline. Đã bỏ tên week1-demo khỏi nơi chạy hiện hành, đổi automatic thành processed và bỏ tên promotion khỏi thư mục kiểm chứng hiện hành. Chỉ chuyển vị trí file; không sửa số/provenance lịch sử. Báo cáo/kế hoạch cũ vẫn là lịch sử.

keep-temporary giữ ảnh/crop/OCR; mặc định dọn sau lưu/đọc lại thành công. Resume chỉ dùng cache hợp lệ; đã dọn tạm hoặc đổi code/model/runtime thì các bước tương ứng phải xử lý lại. Hai interpreter/model đã khóa phải sẵn có; môi trường vận hành còn trong workspace.

API dùng tiếp gồm collection/parser, OCR services và storage factory/repository/service nêu ở mục 5. Chạy với --config để thay workspace/model/interpreter/database env. Hai môi trường OCR phải được chuẩn bị theo package lock; PostgreSQL phải sẵn có. Pipeline áp dụng migration, không tự bootstrap server khi import hoặc chạy collection. scripts/setup_local_database.py là trợ giúp phát triển riêng trên máy hiện tại.

**Giới hạn:** hai nguồn và hai PDF đã kiểm chứng; các PDF cũng dùng để phát triển rule, chưa là tập độc lập. Parser dựa tên/mã số và kiểu tiêu đề/cột hiện có; crop chủ yếu cho tài liệu thẳng hàng. Chưa kiểm chứng mọi chế độ kế toán, trang xoay/scan kém, biểu diễn số/đa đơn vị khác hoặc kỳ tài chính khác năm dương lịch. Trường hợp không rõ giữ null/lý do.

**Đề xuất trao đổi tiếp, chưa tự tích hợp:** đối chiếu/phê duyệt 12 ứng viên; xác định tập độc lập và chỉ số độ đúng; chọn lát cắt API/giao diện UC-1. Mẫu mới, dữ liệu mới và công sức cần thống nhất, không mặc định mở đủ chín báo cáo trong phiên này.
