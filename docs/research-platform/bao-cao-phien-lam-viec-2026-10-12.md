# Báo cáo phiên làm việc ngày 12/10/2026

## 1. Mục tiêu và phạm vi thực hiện

Triển khai lát cắt dữ liệu chạy được: **thu PDF → Paddle phát hiện/crop → VietOCR đọc tiếng Việt → trích sáu chỉ tiêu → chuẩn hóa → lưu PostgreSQL → đọc lại kiểm tra**. Mẫu thực hiện gồm hai báo cáo tài chính hợp nhất năm 2025: Vinamilk (VNM) và Hòa Phát (HPG).

Công việc nằm trong workspace riêng `workspace/week1-demo`. Phạm vi phiên này dừng ở database. API, giao diện, quy trình duyệt/công bố số liệu và các UC phân tích đầu tư chưa được triển khai trong lát cắt hiện hành. Sáu chỉ tiêu chưa bao gồm CAPEX hoặc tiền chi cổ tức.

Báo cáo Markdown này được soạn theo yêu cầu của người thực hiện. Các bảng số liệu, thống kê trang và liên kết đầu ra trong báo cáo được tạo bằng code từ file kết quả đã lưu. Nội dung diễn giải là tổng kết phiên làm việc, không thay thế bằng chứng thực nghiệm hoặc bộ số chuẩn độc lập.

## 2. Luồng đã triển khai

| Bước | Đầu vào | Xử lý | Đầu ra |
|---|---|---|---|
| Thu nguồn | Công ty, năm, tên pháp lý, URL PDF được cung cấp | Tải bằng HTTP, kiểm tra PDF, tính SHA-256 | PDF gốc và thông tin nguồn |
| Phát hiện/crop | Toàn bộ trang PDF | Render 180 DPI; Paddle `PP-OCRv5_mobile_det` phát hiện vùng chữ; crop có đệm | Ảnh crop và tọa độ tạm |
| OCR | Crop do Paddle tạo | VietOCR `vgg_seq2seq` chạy CPU; chia dòng dài tại khoảng trắng | Text, độ tin cậy và dấu vết xử lý tạm |
| Tìm dữ liệu | OCR của toàn bộ tài liệu | Kiểm tra công ty/kỳ/hợp nhất/kiểm toán; nhận diện bảng chính, đơn vị và cột kỳ hiện tại | Dòng chỉ tiêu kèm bằng chứng |
| Chuẩn hóa | Giá trị OCR và đơn vị bảng | Đọc dấu phân nhóm, số âm; chuyển sang VND; xác định kỳ hoặc ngày chốt | Sáu ứng viên mỗi báo cáo |
| Lưu và kiểm tra | Ứng viên cùng nguồn/provenance | Lưu giao dịch PostgreSQL; mở session mới đọc lại, so giá trị và evidence | Bản ghi database và CSV đọc lại |
| Dọn tạm | Lần lưu/đọc lại thành công | Xóa thư mục xử lý tạm trong phạm vi workspace | Giữ PDF, kết quả liên quan và log |

Parser hiện hành không đặt trước danh sách trang `1–15,22`, không dùng tọa độ pixel riêng cho VNM/HPG và không gắn số tài chính vào code. Code tìm bảng theo tiêu đề, nhận diện cột theo nhãn năm/ngày hoặc “Số cuối năm/Năm nay”, rồi tìm chỉ tiêu theo mã số và tên nghiệp vụ.

Các trường hợp được bổ sung trong phiên: mã số ở trước/sau tên chỉ tiêu; mã số gộp vào tên dòng; tên chỉ tiêu xuống dòng; cột hiện tại nằm bên phải; tiêu đề thuyết minh có lỗi OCR; dòng văn bản quá dài khi đưa vào recognizer.

Nếu thiếu/không rõ ngữ cảnh, bảng, đơn vị, cột hoặc giá trị, kết quả giữ `null` với lý do và trạng thái `missing_or_ambiguous`. Không thay số thiếu bằng 0. Giá trị trích được mang trạng thái `pending_review`.

## 3. Các file code và cấu hình

| File | Vai trò |
|---|---|
| [run_pipeline.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/scripts/run_pipeline.py) | Điều phối các bước; nhận đầu vào nguồn; ghi log và dừng khi bước xử lý lỗi. |
| [prepare_report.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/scripts/prepare_report.py) | Tải PDF từ URL được cung cấp, kiểm tra định dạng, tính SHA-256 và lưu thông tin nguồn. |
| [prepare_vietocr.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/scripts/prepare_vietocr.py) | Chuẩn bị model/config VietOCR; kiểm tra mã hash của model đã khóa. |
| [detect_regions.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/scripts/detect_regions.py) | Render toàn bộ trang, Paddle phát hiện vùng chữ, crop và lưu hình học vùng chữ. |
| [recognize_vietocr.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/scripts/recognize_vietocr.py) | VietOCR đọc crop; chia dòng quá dài tại khoảng trắng; sử dụng cache hợp lệ khi chạy tiếp. |
| [financial_parser.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/scripts/financial_parser.py) | Kiểm tra ngữ cảnh báo cáo; tìm bảng, đơn vị, cột và dòng chỉ tiêu; chuẩn hóa VND. |
| [setup_database.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/scripts/setup_database.py) | Chuẩn bị PostgreSQL cục bộ cho workspace. |
| [db.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/database/db.py) | Kết nối PostgreSQL và quản lý session. |
| [models.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/database/models.py) | Định nghĩa mô hình dữ liệu và ràng buộc. |
| [001_collection_pipeline.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/database/migrations/versions/001_collection_pipeline.py) | Tạo schema bằng Alembic. |
| [store_report.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/database/store_report.py) | Kiểm tra nguồn/độ đầy đủ OCR; lưu giao dịch, đọc lại đối chiếu, xuất kết quả và dọn file tạm. |
| [test_financial_parser.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/scripts/test_financial_parser.py) | Kiểm thử parser trên bố cục và dữ liệu giả lập. |
| [test_store_report.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/database/test_store_report.py) | Kiểm thử lưu PostgreSQL trong schema tạm, tách dữ liệu thực. |

Cấu hình đọc OCR được giữ tại [vietocr-inference.yml](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/config/vietocr-inference.yml). Các file khóa package và model trong [config](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/config) hỗ trợ kiểm tra môi trường/model; chúng không chứng minh chất lượng OCR.

## 4. Kết quả thực tế

### 4.1. Độ phủ và nhận diện bảng

| Báo cáo | Trang đã xử lý | Trang tự nhận diện là bảng chính | Số có giá trị / mục tiêu | Run database hiện hành |
|---|---:|---|---:|---:|
| VNM 2025 | 63/63 | 7, 8, 9, 10, 11, 12, 13, 14 | 6/6 | 4 |
| HPG 2025 | 53/53 | 7, 8, 9, 10, 11, 12 | 6/6 | 5 |


Các số trang trên là kết quả code tự tìm sau khi đọc toàn bộ PDF; không phải danh sách trang được người vận hành nhập. Ngữ cảnh công ty, báo cáo hợp nhất, kiểm toán, năm báo cáo và năm tài chính theo năm dương lịch đều qua kiểm tra bằng text OCR trên hai mẫu. Đây là kiểm tra tự động theo rule, chưa là phê duyệt độc lập của người dùng.

### 4.2. Sáu chỉ tiêu đọc lại từ PostgreSQL

| Chỉ tiêu | VNM 2025 (VND) | Trang PDF | HPG 2025 (VND) | Trang PDF |
|---|---:|---:|---:|---:|
| LNST toàn doanh nghiệp hợp nhất | 9.413.589.732.469 | 10 | 15.514.931.571.606 | 10 |
| Lưu chuyển tiền thuần từ HĐKD (CFO) | 8.668.137.048.520 | 12 | 17.365.859.056.591 | 11 |
| Tiền và tương đương tiền | 1.794.879.718.871 | 7 | 8.300.890.304.205 | 7 |
| Tổng tài sản | 53.312.370.717.301 | 8 | 257.899.200.817.547 | 8 |
| Nợ phải trả | 18.829.355.431.194 | 9 | 126.679.189.940.972 | 9 |
| Vốn chủ sở hữu | 34.483.015.286.107 | 9 | 131.220.010.876.575 | 9 |


Đơn vị: VND. Trang là số thứ tự trang PDF, bắt đầu từ 1. LNST ở đây là tổng LNST hợp nhất, không riêng phần thuộc cổ đông công ty mẹ. NI/CFO là số của cả năm; bốn chỉ tiêu bảng cân đối là số tại ngày 31/12/2025.

**Toàn bộ 12 số vẫn chờ duyệt.** Có đủ mục tiêu và đọc lại khớp database không có nghĩa là đã xác nhận OCR đúng 100% so với PDF.

### 4.3. File kết quả và chứng từ nguồn

| File | Nội dung | VNM | HPG |
|---|---|---|---|
| `source.json` | URL, thời điểm tải, mã hash và vị trí PDF; thông tin đích công ty/năm. | [Mở](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/data/automatic/VNM-2025-ee996ffcb87f/source.json) | [Mở](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/data/automatic/HPG-2025-f38c5f75becf/source.json) |
| `processing.json` | Độ phủ trang, bảng tìm được, kiểm tra ngữ cảnh, config/package và mã hash code/model. | [Mở](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/data/automatic/VNM-2025-ee996ffcb87f/processing.json) | [Mở](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/data/automatic/HPG-2025-f38c5f75becf/processing.json) |
| `candidates.json` | Sáu số ứng viên, kỳ, đơn vị, trạng thái và bằng chứng OCR liên quan. | [Mở](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/data/automatic/VNM-2025-ee996ffcb87f/candidates.json) | [Mở](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/data/automatic/HPG-2025-f38c5f75becf/candidates.json) |
| `database-readback.csv` | Số và thông tin nguồn đọc lại từ PostgreSQL; mã lần trích. | [Mở](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/data/automatic/VNM-2025-ee996ffcb87f/database-readback.csv) | [Mở](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/data/automatic/HPG-2025-f38c5f75becf/database-readback.csv) |


| Báo cáo | PDF gốc lưu cục bộ | URL nguồn |
|---|---|---|
| VNM 2025 | [PDF](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/data/raw/ee996ffcb87f0699a59c20b102082666f6716fcf9be8ee314ad2de055f79c940.pdf) | [Nguồn PDF](https://d8um25gjecm9v.cloudfront.net/cms/20260227_BCTC_KIEM_TOAN_2025_HOP_NHAT_VN_94f1e76e45.pdf) |
| HPG 2025 | [PDF](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/data/raw/f38c5f75becf7d3f145d27183eec81f119fd4f75e378b983a2763ddc3f7e0c07.pdf) | [Nguồn PDF](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/03/20260327-hpg-bctc-hop-nhat-nam-2025-sau-kiem-toan.pdf) |


`candidates.json` giữ giá trị OCR gốc, đơn vị, trang, tọa độ vùng số, nhãn dòng, tiêu đề cột hiện tại/so sánh, thông tin model và độ tin cậy. Chỉ giữ evidence liên quan đến chỉ tiêu; không xuất toàn bộ nội dung thuyết minh vào database.

Database có bốn bảng: `documents` (đích công ty/năm/phạm vi), `document_versions` (phiên bản PDF và nguồn), `extraction_runs` (lần trích và provenance), `candidates` (sáu ứng viên/lần trích). Giá trị dùng `NUMERIC(30,0)`; evidence dùng JSONB. CSV là bản xuất đọc lại, không phải nơi nhập số vào database. Database có các lần trích lịch sử; 12 số trong bảng thuộc hai run hiện hành nêu trên, không phải tổng số bản ghi toàn database.

### 4.4. Cách hiểu lần chạy cuối

Lần điều phối cuối bắt đầu 12/10/2026 12:34:02, hoàn tất 12/10/2026 12:34:19 (giờ Việt Nam), dùng `--resume`; [run.json](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/data/runs/20261012T053402375825Z/run.json) ghi `completed: true`.

PDF và kết quả detection được tái sử dụng từ các bước đã chạy trước đó. Recognizer được gọi lại nhưng dùng cache đã kiểm tra: VNM 4361 vùng, HPG 4238 vùng; lần điều phối cuối không suy luận lại vùng nào. Vì vậy thời gian của lần chạy cuối không đại diện cho thời gian tải/render/Paddle/VietOCR từ đầu trên 116 trang. Không dùng mốc này để công bố hiệu năng OCR.

## 5. Phân biệt thủ công và tự động

| Phần việc | Hiện trạng |
|---|---|
| Chọn doanh nghiệp, năm, URL và tên pháp lý dự kiến | Do người vận hành cung cấp/đặt trong đầu vào; chưa tự khám phá mọi báo cáo từ Internet |
| Tải PDF từ URL đã cung cấp | Tự động |
| Xác định trang cần đọc | Tự động đọc tất cả trang; không yêu cầu chọn trang bằng tay |
| Paddle crop, VietOCR, tìm bảng/cột/dòng, chuẩn hóa | Tự động theo code/rule |
| Viết/sửa code và rule xử lý | Có Codex hỗ trợ; không gọi là code do người thực hiện tự viết hoàn toàn |
| Điền hoặc sửa trực tiếp số liệu đầu ra | Không thực hiện; sửa code rồi chạy lại |
| Lưu database, đọc lại, xuất kết quả và dọn tạm | Tự động |
| Đối chiếu độc lập với PDF và phê duyệt | Cần người duyệt; chưa hoàn thành |

## 6. Kiểm tra đã thực hiện

Trong phiên, lệnh pytest trên hai file kiểm thử hiện hành cho kết quả **8 passed**: sáu ca parser và hai ca PostgreSQL. Kết quả này đã quan sát trong đầu ra lệnh; chưa có file log pytest riêng được giữ trong lần chạy pipeline cuối.

Các kiểm tra gồm: biến đổi vị trí mã dòng/kích thước ảnh; cột hiện tại bên phải; mã dòng gộp và tên xuống dòng; phân biệt năm báo cáo với năm so sánh; loại thuyết minh/đoạn nhắc đến bảng; không coi dấu gạch hoặc số không rõ là 0; lưu số âm, null, 0 và số lớn chính xác; tái lưu cùng nội dung không nhân bản run; hoàn tác toàn giao dịch khi vi phạm ràng buộc.

Kiểm thử PostgreSQL dùng schema tạm và số giả lập, không sửa số liệu doanh nghiệp thực. Ngoài ra, hai run thực được đọc lại bằng session mới và so giá trị/evidence; gọi lưu lại từ kết quả đã giữ trả về cùng run hiện hành.

Kiểm tra đẳng thức kế toán trên số đọc lại:

- VNM: tổng tài sản = nợ phải trả + vốn chủ sở hữu: **khớp**.
- HPG: tổng tài sản = nợ phải trả + vốn chủ sở hữu: **khớp**.

Các kiểm tra này hỗ trợ phát hiện lỗi parser/persistence. Chưa có đo CER/WER, sai số từng chỉ tiêu so với bộ số chuẩn độc lập hoặc đối chứng Tesseract trong luồng mới. Độ tin cậy VietOCR không được coi là tỷ lệ chính xác đã kiểm chứng.

## 7. Dữ liệu giữ lại và dọn dẹp

- Giữ hai PDF gốc trong [data/raw](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/data/raw) để truy xuất chứng từ nguồn và chạy lại.
- Giữ bốn file kết quả mỗi báo cáo, log điều phối, database cùng model/môi trường cần vận hành.
- Hai thư mục xử lý tạm của luồng mới đã được pipeline xóa sau lưu/đọc lại thành công; ảnh trang, crop và OCR toàn bộ trang không còn trong các thư mục tạm này.
- Code và dữ liệu của luồng cũ dùng trang/bố cục cố định được chuyển sang [fixed-page-pipeline](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/history/week1-over-scope-2026-10-12/fixed-page-pipeline). Đây là dữ liệu lịch sử, chưa bị xóa hết; không dùng làm kết quả hiện hành.
- Các thư mục `data/` và `runtime/` của workspace được ignore trong Git. Kết quả hiện nằm cục bộ; chưa có xác nhận sao lưu ngoài máy cho hai run mới.

Để chạy lại luồng chính, dùng interpreter inference của workspace để chạy [run_pipeline.py](C:/Users/admin/Documents/GitHub/financial-analysis-platform/workspace/week1-demo/scripts/run_pipeline.py). Chạy mặc định xử lý hai nguồn 2025 đã chọn và dọn tạm sau thành công. `--keep-temporary` giữ ảnh/crop/OCR để kiểm tra. `--resume` tái sử dụng dữ liệu tạm khi còn; sau khi đã dọn tạm, một lần chạy tiếp cần xử lý lại các bước tương ứng.

## 8. Giới hạn và nội dung trao đổi tiếp

**Đã triển khai:** đọc toàn bộ hai báo cáo, tự tìm bảng/cột/dòng theo nội dung, trích sáu chỉ tiêu, chuẩn hóa, lưu PostgreSQL và xuất số đọc lại có nguồn.

**Chưa được chứng minh:** khả năng áp dụng cho mọi báo cáo. Parser vẫn dựa trên danh mục tên bảng, tên chỉ tiêu, mã số kế toán và giả định tài liệu tiếng Việt, hợp nhất, năm tài chính theo năm dương lịch. Hai báo cáo đã dùng để phát triển rule; chưa phải tập kiểm thử độc lập. Chưa đánh giá trang xoay, scan kém, bố cục hoặc chế độ kế toán khác, kỳ tài chính khác năm dương lịch. Khi gặp trường hợp mới, có thể cần bổ sung rule dùng chung; không điền giá trị tài chính theo từng công ty.

**Đề xuất trao đổi, chưa tự triển khai:** (1) người thực hiện đối chiếu/phê duyệt 12 ứng viên; (2) xác định cách đánh giá parser trên tài liệu chưa dùng để chỉnh rule và đo độ đúng; (3) sau khi nền dữ liệu ổn định, quyết định lát cắt API/giao diện phục vụ UC-1. Mẫu/năm mới, bộ số chuẩn, dữ liệu bổ sung và công sức cho các bước này cần được thống nhất trước khi tích hợp.
