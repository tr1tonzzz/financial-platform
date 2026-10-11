# Chốt phạm vi HPG–VNM–FPT và stack PaddleOCR

Quyết định của người thực hiện ngày **11/10/2026**: chọn **Hòa Phát (HPG), Vinamilk (VNM), FPT (FPT)**; chuyển công cụ OCR chính sang **PaddleOCR**. Quyết định này thay các phương án chưa chốt trong tài liệu 29/30 và lựa chọn Tesseract trong thiết kế trước. Không phải kết luận thực nghiệm rằng PaddleOCR đọc tốt hơn.

## 1. Phạm vi đã chốt

| Nội dung | Quyết định |
|---|---|
| Doanh nghiệp chính | HPG, VNM, FPT |
| Kỳ | Năm tài chính 2023, 2024, 2025 |
| Báo cáo | BCTC năm đã kiểm toán, ưu tiên và lập chuỗi hợp nhất; số riêng lẻ giữ thành chuỗi riêng nếu cần đọc bổ trợ |
| Khối lượng lõi | 9 báo cáo đích, 54 ô chỉ tiêu lõi; chưa tính dòng cầu nối/CAPEX/khoản chi/sự kiện cổ tức |
| Chức năng ưu tiên | UC-F01/02/03/05 trước, UC-F04 sau |
| Cổ tức | Phân tích tiền mặt; vẫn thu sự kiện cổ phiếu cần thiết để kiểm cơ sở DPS |
| Nguồn bổ trợ đã có | Ca DHG/VHC giữ làm minh chứng nghiên cứu lịch sử; không tính vào mẫu nghiệm thu chính |

Nhóm này phù hợp để kiểm luồng trên các doanh nghiệp có hoạt động khác nhau. Đây là nhóm doanh nghiệp do người dùng chọn, **không phải nhóm cùng ngành** hoặc mẫu đại diện toàn thị trường. Khi so sánh, kiểm kỳ/scope/đơn vị và giải thích giới hạn ngành. FPT cần đọc thay đổi phạm vi hợp nhất khi so lịch sử; HPG/FPT cần kiểm sự kiện vốn trước diễn giải DPS. Không tự dựng chuỗi điều chỉnh chỉ vì đã chọn mã.

[Manifest phạm vi](../../config/pilot-scope.json) ghi chín báo cáo cần thu, sáu chỉ tiêu và lựa chọn OCR. Đây là manifest kế hoạch, chưa được ứng dụng đọc và không đánh dấu các báo cáo đã thu/duyệt. Khi triển khai cần nối trạng thái thực từ ledger nguồn.

## 2. Stack đã chọn cho triển khai

**Quyết định kiến trúc tiếp ngày 11/10/2026:** người thực hiện yêu cầu giữ web React và PostgreSQL. Stack hiện hành là **React/TypeScript → REST API FastAPI/Python → PostgreSQL**. Phương án Streamlit/SQLite trước đó là thiết kế pilot đã được thay thế; không duy trì hai giao diện/hai database cho sản phẩm. Paddle vẫn là OCR chính. Quyết định này chưa có nghĩa các thành phần đã được cài hoặc ứng dụng đã chạy.

| Thành phần | Lựa chọn | Vai trò |
|---|---|---|
| Frontend | React + TypeScript, Vite | Web SPA: bộ chọn, bảng, biểu đồ, nguồn, màn hình duyệt; gọi API |
| Backend | FastAPI, Python 3.12, Windows local | REST API, nghiệp vụ dữ liệu/phân tích; dùng lại pipeline Python |
| Thu thập | HTTP + lxml, downloader có hash/phiên bản | Catalog BCTC, thông báo và tài liệu nguồn |
| PDF có text | pypdf/pdfplumber | Metadata, text/tọa độ; kiểm text có dùng được hay không |
| Render trang scan | Poppler | Chuyển trang cần đọc thành ảnh, giữ số trang/DPI |
| OCR chính | PaddleOCR dòng 3.x, engine PaddlePaddle, ưu tiên CPU | Nhận diện chữ/số và vị trí trên ảnh; chọn model hỗ trợ tiếng Việt |
| Database | PostgreSQL; SQLAlchemy + Alembic | Schema, transaction, revision và migration; NUMERIC cho số tiền |
| Tính toán | pandas, integer/Decimal | Công thức chạy ở backend trên dữ liệu đã duyệt |
| Tài liệu gốc | Thư mục raw theo SHA-256; metadata trong PostgreSQL | PDF/ảnh không nhét toàn bộ vào bảng số liệu; API phục vụ nguồn qua ID |
| Đối chứng OCR | Tesseract/Tesseract.js từ prototype cũ | Chỉ dùng đo so sánh; không là OCR mặc định của pipeline mới |

Đã chốt công nghệ và vai trò. **Chưa khóa phiên bản patch của PaddleOCR/PaddlePaddle hoặc model** trước khi kiểm cài đặt và chạy mẫu trên máy project. Khi smoke test qua, lưu phiên bản package, tên/hash model, cấu hình ngôn ngữ và thiết bị vào manifest/lock. Không dùng Python 3.14 mặc định của máy làm môi trường OCR đã được xác nhận; thiết kế giữ Python 3.12 riêng.

React/backend/database cũng khóa phiên bản theo môi trường chạy thật, không dùng phiên bản thử nghiệm làm baseline. React/Vite là lựa chọn thiết kế SPA với backend Python riêng, không phải yêu cầu phải dùng Next.js. [Tài liệu React](https://react.dev/learn/creating-a-react-app) mô tả các cách khởi tạo, gồm lựa chọn build tool khi tự tổ chức ứng dụng. Không xây thêm backend Node cho cùng nghiệp vụ.

Chạy local bằng ba thành phần: PostgreSQL, FastAPI và web React; có README/lệnh khởi chạy và biến môi trường mẫu. API và frontend bind localhost, CORS chỉ origin frontend được cấu hình theo [FastAPI](https://fastapi.tiangolo.com/tutorial/cors/). Tài khoản đọc/duyệt nhiều người và triển khai public chưa nằm trong lát cắt hai tuần; vai trò trên màn hình chưa được coi là cơ chế phân quyền production.

Backup dùng `pg_dump`/`pg_restore` cùng raw/config/migration; [tài liệu PostgreSQL](https://www.postgresql.org/docs/current/backup-dump.html) là căn cứ quy trình. Không sao chép thư mục data của DB đang chạy để thay backup. DB credentials nằm trong môi trường backend, không đưa vào frontend hoặc Git.

Tài liệu chính thức [cài PaddleOCR](https://www.paddleocr.ai/main/en/version3.x/installation.html) tách package OCR, nhóm khả năng bổ sung và inference engine; [pipeline OCR](https://www.paddleocr.ai/main/en/version3.x/pipeline_usage/OCR.html) liệt kê tiếng Việt (`vi`) và model hỗ trợ. Chọn general OCR trước; phân tích cấu trúc bảng bằng PP-Structure chỉ thêm nếu parser cần và có thực nghiệm. Không mặc định OCR trả ngay sáu chỉ tiêu đã chuẩn hóa.

## 3. Pipeline sau khi chuyển

PDF → kiểm text/tọa độ → nếu không dùng được thì render trang → PaddleOCR → chữ/số/vị trí/confidence → ánh xạ nhãn và cột → chuẩn hóa candidate → kiểm đơn vị/kỳ/scope/dấu → người vận hành duyệt → PostgreSQL → phân tích/biểu đồ.

Mỗi lần OCR lưu engine/package/model/config, trang, tọa độ, text thô, confidence, thời gian và lỗi. Confidence không thay kiểm đúng số. Giữ kết quả cũ dưới tên engine cũ để không biến phép đo Tesseract thành minh chứng Paddle.

## 4. Các bước thực hiện tiếp

1. Lập ledger thu báo cáo năm 2023–2025 cho HPG/VNM/FPT; xác nhận bìa/header và phiên bản. Không đổi mã trong crawler cũ rồi coi đã có adapter FPT.
2. Tạo môi trường Python 3.12 riêng, cài PaddleOCR/PaddlePaddle CPU tương thích; chạy kiểm engine và một ảnh thật từ mỗi mã; khóa phiên bản sau khi chạy qua.
3. Viết adapter Paddle trả kết quả chuẩn có trang/bbox/text/confidence; tách OCR khỏi parser nghiệp vụ. Tận dụng render/ảnh mẫu cũ, không ghi đè minh chứng Tesseract.
4. Đo đối chứng trên 20–30 trang đa dạng của ba doanh nghiệp; tách trang phát triển parser và trang kiểm. Báo đúng/sai/thiếu số, nhầm cột/đơn vị, thời gian và công sức duyệt.
5. Nối candidate vào UC-1, rồi chạy bảng/biểu đồ UC-2, so sánh UC-3 và hồ sơ cổ tức UC-5.

Benchmark dùng để đánh giá chất lượng và điều chỉnh pipeline sau lựa chọn của người thực hiện; **không là điều kiện xin lại quyền chuyển công cụ**. Nếu có lỗi tương thích hoặc chất lượng, ghi lỗi và xử lý/duyệt số, không tự tuyên bố đạt hoặc âm thầm thay engine.

## 5. Tác động và trạng thái

Số doanh nghiệp/năm/sáu chỉ tiêu không tăng, nên không thêm nghĩa vụ chức năng hoặc đổi ID SRS. Cập nhật phạm vi mục 1.3 và lựa chọn thiết kế mục 2.3 của SRS v3.3; giữ điều kiện OCR fallback và provenance. Nguồn FPT và sự kiện vốn làm phát sinh công việc kiểm adapter/basis cần đo lại. Cài đặt/adapter/benchmark là việc triển khai tiếp, chưa có bằng chứng Paddle chạy trong project tại thời điểm chốt này. Các prototype Tesseract và kết quả cũ vẫn là lịch sử thực nghiệm.
