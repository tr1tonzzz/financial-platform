# CHECKLIST CHI TIẾT 16 TUẦN - FINANCIAL DATA PLATFORM

Tài liệu này là phiên bản phân rã cực kỳ chi tiết từ lộ trình 16 tuần ban đầu, được bổ sung các thông số kỹ thuật, tên bảng, tên API, và chỉ tiêu cụ thể từ SRS-FDP-01 và SDD-FDP-01. Sử dụng checklist này để theo dõi tiến độ hàng ngày/hàng tuần.

---

## CHECKPOINT 1 — Tuần 1–2: Xác định vấn đề & Học nền tảng

### Tuần 1: Thiết lập môi trường & Khảo sát cơ bản
- [ ] Cài đặt môi trường phát triển:
  - [ ] Python 3.11+
  - [ ] PostgreSQL 15+ (Khuyến nghị dùng Docker: `docker run --name postgres-db -e POSTGRES_PASSWORD=secret -p 5432:5432 -d postgres:15`)
  - [ ] VS Code và các extension cần thiết (Python, PostgreSQL, Prettier)
  - [ ] Git (Khởi tạo repository đồ án)
- [ ] Học/Ôn tập Python cơ bản (biến, dict/list, vòng lặp, đọc/ghi file).
- [ ] Nghiên cứu 4 sản phẩm tham khảo (Nasdaq Data Fabric, AlphaSense, Economatica, Polygon.io).
- [ ] Lập bảng so sánh 4 sản phẩm: tính năng, đối tượng người dùng, ưu/nhược điểm.
- [ ] Tải thử 1 file ZIP từ nguồn SEC Financial Statement Data Sets.
- [ ] Giải nén file ZIP, mở xem cấu trúc các file (`sub.txt`, `num.txt`, `tag.txt`, `pre.txt`) để hiểu sơ bộ định dạng TSV.

### Tuần 2: Phân tích dữ liệu bằng Pandas & Xác định Scope
- [ ] Học Pandas cơ bản (read_csv, DataFrame, filter, groupby).
- [ ] Viết Python script khảo sát dữ liệu SEC bằng Pandas:
  - [ ] Đọc file `num.txt` và in ra tổng số dòng.
  - [ ] Đọc file `sub.txt` và đếm số công ty phân biệt (`cik`).
  - [ ] Đếm số thẻ XBRL phân biệt (`tag`) trong `num.txt`.
- [ ] Soạn thảo Problem Statement, Product Vision, Target Users theo định dạng SRS.
- [ ] Xác định Scope rõ ràng:
  - [ ] Khẳng định Must Have: 30 công ty, 10 chỉ tiêu, Bitemporal, Benchmark hiệu năng, 12 quý.
  - [ ] Khẳng định Out of Scope (Không làm): Đăng nhập/Xác thực, Dữ liệu Việt Nam, Real-time, Streaming.

### Deliverables Checkpoint 1
- [ ] Script Python (`explore_sec.py`) chạy được và in ra thống kê.
- [ ] Slide thuyết trình Checkpoint 1 (7 slides: Tên đề tài, Problem Statement, Bảng so sánh 4 SP, Định vị SP, Scope, Demo script, Kế hoạch 16 tuần).
- [ ] Báo cáo Word Checkpoint 1 (7 phần theo mẫu).

---

## CHECKPOINT 2 — Tuần 3–4: Thiết kế dữ liệu & Kiến trúc

### Tuần 3: Chọn mẫu dữ liệu & Khởi tạo Database
- [ ] Học kết nối Python với PostgreSQL bằng `psycopg2` hoặc `SQLAlchemy`.
- [ ] Học sử dụng câu lệnh `COPY` của PostgreSQL để import dữ liệu tốc độ cao.
- [ ] Khảo sát và chốt danh sách **30 công ty (CIK)**:
  - [ ] Thuộc 3-4 ngành nghề khác nhau (Ví dụ: Tech, Finance, Retail).
  - [ ] Đảm bảo cả 30 công ty đều có đủ dữ liệu báo cáo trong 12 quý gần nhất.
  - [ ] Lưu danh sách 30 CIK này vào file `target_companies.csv`.
- [ ] Định nghĩa chính xác **10 Canonical Metrics** (Theo SDD-FDP-01):
  - [ ] REVENUE (Doanh thu thuần)
  - [ ] NET_INCOME (Lợi nhuận ròng)
  - [ ] GROSS_PROFIT (Lợi nhuận gộp)
  - [ ] EPS (Lãi cơ bản trên cổ phiếu)
  - [ ] TOTAL_ASSETS (Tổng tài sản)
  - [ ] TOTAL_LIABILITIES (Tổng nợ phải trả)
  - [ ] TOTAL_EQUITY (Vốn chủ sở hữu)
  - [ ] OPERATING_CASH_FLOW (Dòng tiền HĐKD)
  - [ ] CAPEX (Chi đầu tư TSCĐ)
  - [ ] SHARES_OUTSTANDING (Số cổ phiếu lưu hành)

### Tuần 4: Thiết kế Database & Kiến trúc
- [ ] Vẽ ERD hoàn chỉnh bao gồm các bảng:
  - [ ] `company` (cik, name, sic_code, ...)
  - [ ] `metric_definition` (metric_id, code, display_name, ...)
  - [ ] `tag_mapping` (xbrl_tag, metric_id, priority)
  - [ ] `financial_fact` (Bảng bitemporal: cik, metric_id, period_end, value, filed_at, accession_no, ...)
  - [ ] `historical_price` (cik, trade_date, close_price)
  - [ ] `ingestion_log` (log_id, run_at, period, status, ...)
- [ ] Viết file migration SQL (`init_schema.sql`) để tạo cấu trúc schema trên PostgreSQL.
- [ ] Chạy file SQL vào DB thành công, không sinh lỗi.
- [ ] Vẽ sơ đồ kiến trúc hệ thống (High-level Architecture) bằng Mermaid.
- [ ] Viết tài liệu giải thích quyết định thiết kế (Decision Log):
  - [ ] Tại sao chọn thiết kế fact table (Long-format) thay vì bảng rộng (Wide-format)?
  - [ ] Tại sao cần Bitemporal (filed_at) để lưu lịch sử thay vì ghi đè?

### Deliverables Checkpoint 2
- [ ] Database Postgres đã được khởi tạo schema đầy đủ.
- [ ] File `target_companies.csv` chứa 30 CIK.
- [ ] Slide thuyết trình Checkpoint 2 (Kiến trúc, ERD, Giải thích quyết định thiết kế Fact Table + Bitemporal, Demo DB Schema).
- [ ] Báo cáo Word Checkpoint 2.

---

## CHECKPOINT 3 — Tuần 5–6: Vertical Slice (Bản chạy thông đầu tiên)

### Tuần 5: Ingestion & Standardization (Tối giản)
- [ ] Viết script Ingestion tối giản (`ingest_q1.py`):
  - [ ] Giải nén 1 file ZIP quý (VD: 2024Q1).
  - [ ] Nạp thô `sub.txt` và `num.txt` vào bảng Staging bằng lệnh `COPY`.
- [ ] Lập file `tag_mapping.csv` thủ công cho **3 chỉ tiêu** (REVENUE, NET_INCOME, TOTAL_ASSETS).
- [ ] Chạy script nạp thông tin mapping vào bảng `tag_mapping` và thông tin metric vào `metric_definition`.
- [ ] Lọc dữ liệu thô staging cho **3 CIK** đầu tiên trong danh sách.
- [ ] Viết script Standardization:
  - [ ] Join dữ liệu thô với `tag_mapping`.
  - [ ] Insert kết quả chuẩn hóa vào bảng chính `financial_fact`.

### Tuần 6: Khởi tạo Backend & API đầu tiên
- [ ] Cài đặt FastAPI và Uvicorn.
- [ ] Khởi tạo project backend cấu trúc chuẩn (routers, models, database).
- [ ] Cấu hình kết nối DB từ FastAPI (sử dụng connection pool).
- [ ] Viết 1 API Endpoint: `GET /companies/{cik}/financials`
  - [ ] Kết nối DB, query dữ liệu từ `financial_fact` cho CIK truyền vào.
  - [ ] Trả về JSON chuẩn `{ "data": {...}, "meta": {...} }`.
- [ ] Test API bằng Swagger UI (`http://localhost:8000/docs`) hoặc Postman.
- [ ] (Tùy chọn) Viết 1 file HTML/JS thuần gọi API hiển thị dữ liệu thô ra màn hình để chứng minh pipeline.

### Deliverables Checkpoint 3
- [ ] **End-to-End Pipeline chạy thông:** File ZIP -> Staging -> DB `financial_fact` -> FastAPI -> JSON response.
- [ ] Slide thuyết trình Checkpoint 3 (Sơ đồ vertical slice, Demo gọi API trực tiếp).
- [ ] Báo cáo Word Checkpoint 3 (Mô tả kỹ thuật pipeline v0.1).
- [ ] *Lưu ý Điểm chết:* Nếu API không trả ra dữ liệu thật (không hardcode), không được pass checkpoint này.

---

## CHECKPOINT 4 — Tuần 7–8: Mở rộng Ingestion & Chuẩn hóa toàn bộ

### Tuần 7: Mở rộng Dữ liệu (Scale up)
- [ ] Hoàn thiện `tag_mapping` cho đủ 10 chỉ tiêu. Xử lý các tag phức tạp/nhiều phiên bản của SEC.
- [ ] Chạy luồng Ingestion nạp đủ 12 quý dữ liệu (3 năm).
- [ ] Lọc và chuẩn hóa dữ liệu cho toàn bộ **30 công ty**.
- [ ] Xử lý exception trong pipeline: Các tag không map được phải được bỏ qua an toàn và ghi vào `ingestion_log` thay vì làm crash hệ thống.

### Tuần 8: Validation & Coverage
- [ ] Xây dựng tính năng tính Coverage:
  - [ ] Viết script/SQL tính tỷ lệ % filing giải quyết được thành công cho từng chỉ tiêu.
  - [ ] Viết API `GET /metrics/coverage` trả về báo cáo tỷ lệ.
- [ ] Viết Validation Rules (FR-08) chạy trên dữ liệu đã chuẩn hóa:
  - [ ] Rule 1: Dữ liệu âm bất hợp lý (Ví dụ: Doanh thu REVENUE < 0).
  - [ ] Rule 2: Phát hiện duplicate tags trong cùng một filing.
  - [ ] Rule 3: Outlier (Giá trị đột biến > 500% so với quý trước).
- [ ] Cập nhật DB: Gắn cờ `is_flagged = TRUE` và ghi `flag_reason` cho các bản ghi vi phạm (Không xóa data).
- [ ] Thống kê số lượng/tỷ lệ bản ghi bị gắn cờ.

### Deliverables Checkpoint 4
- [ ] DB `financial_fact` có đầy đủ data của 30 công ty x 12 quý x 10 chỉ tiêu.
- [ ] API Coverage report hoạt động.
- [ ] Slide Checkpoint 4 (Tổng quan dataset đã nạp, Bảng coverage, Kết quả chạy validation).
- [ ] Báo cáo Word Checkpoint 4 (Cơ chế mapping, Bảng coverage đầy đủ, Chi tiết 3 rules validation).

---

## CHECKPOINT 5 — Tuần 9–10: Bitemporal & Dữ liệu giá cổ phiếu

### Tuần 9: Triển khai Bitemporal Logic
- [ ] Khảo sát dữ liệu SEC để tìm ra các công ty có file điều chỉnh (Restatements) - 2 bản ghi cùng `cik`, `metric_id`, `period_end` nhưng khác `filed_at`.
- [ ] Đảm bảo script Ingestion nạp thành công các bản ghi điều chỉnh này, sinh ra nhiều dòng trên `financial_fact` thay vì ghi đè.
- [ ] Viết câu truy vấn Point-in-time SQL chuẩn:
  - Sử dụng `SELECT DISTINCT ON (cik, metric_id, period_end)`
  - Điều kiện `WHERE filed_at <= :as_of_date`
  - Sắp xếp `ORDER BY cik, metric_id, period_end, filed_at DESC`
- [ ] Cập nhật API `GET /companies/{cik}/financials` hỗ trợ query param `?as_of=YYYY-MM-DD`.
- [ ] Liệt kê danh sách các trường hợp Restatement thật tìm được trong DB (CIK, Kỳ, Giá trị cũ, Giá trị mới, Ngày nộp lại).

### Tuần 10: Giá cổ phiếu & Benchmark (Baseline)
- [ ] Sử dụng thư viện `yfinance` viết script tải dữ liệu giá cổ phiếu lịch sử (đóng cửa) của 30 công ty trong 3 năm qua.
- [ ] Nạp dữ liệu vào bảng `historical_price`.
- [ ] Xây dựng công cụ Benchmark (`benchmark.py`):
  - [ ] Truy vấn 1: Lấy tài chính 1 công ty, 1 kỳ, as-of hiện tại.
  - [ ] Truy vấn 2: Lấy toàn bộ 10 chỉ tiêu, 12 quý của 1 công ty.
  - [ ] Truy vấn 3: Lọc/So sánh 5 công ty ở 1 kỳ.
  - [ ] Truy vấn 4: Quét toàn bộ 30 công ty (Full scan).
- [ ] Chạy script Benchmark trên hệ thống **chưa có Index/Materialized View** (Lưu kết quả đo thời gian mili-giây).

### Deliverables Checkpoint 5
- [ ] API hỗ trợ `?as_of=` chạy đúng logic.
- [ ] Bảng lưu giá cổ phiếu đã có dữ liệu.
- [ ] Bảng kết quả Benchmark Baseline (Trước khi tối ưu).
- [ ] Slide Checkpoint 5 (Giải thích trực quan Bitemporal, Demo API as-of, Danh sách Restatements thật, Bảng Benchmark baseline).
- [ ] Báo cáo Word Checkpoint 5.

---

## CHECKPOINT 6 — Tuần 11–12: Tối ưu hiệu năng & Hoàn thiện API

### Tuần 11: Tối ưu hóa Database (Performance Tuning)
- [ ] Tạo các Indexes cần thiết trong PostgreSQL:
  - [ ] `CREATE INDEX idx_fact_company_metric_period ON financial_fact (cik, metric_id, period_end);`
  - [ ] `CREATE INDEX idx_fact_filed_at ON financial_fact (filed_at);`
- [ ] Tạo Materialized View để phục vụ bảng Overview/So sánh siêu tốc:
  - [ ] Viết script SQL `CREATE MATERIALIZED VIEW mv_latest_metrics AS...` (Lấy giá trị mới nhất `filed_at` loại bỏ các cờ lỗi).
  - [ ] Thêm index trên Materialized View.
- [ ] Chạy lại công cụ Benchmark (`benchmark.py`) với cùng 4 câu truy vấn ở Tuần 10.
- [ ] Chụp lại `EXPLAIN ANALYZE` của các câu truy vấn trước và sau khi tối ưu.
- [ ] Tính toán phần trăm (%) cải thiện thời gian phản hồi.

### Tuần 12: Hoàn thiện toàn bộ hệ thống Backend API
- [ ] Hoàn thành code cho tất cả các endpoint còn lại (Theo SRS/SDD):
  - [ ] `GET /companies` (Danh sách công ty)
  - [ ] `GET /companies/{cik}/trend?metric=...` (Xu hướng 1 chỉ tiêu)
  - [ ] `GET /companies/{cik}/prices?from=&to=` (Chuỗi giá cổ phiếu)
  - [ ] `POST /compare` (So sánh nhiều công ty)
  - [ ] `POST /screen` (Tính năng lọc, nếu thời gian cho phép)
  - [ ] `GET /ingestion/logs` (Danh sách logs nạp dữ liệu)
- [ ] Viết Unit Test bằng `pytest` cho module Standardization và Validation (Tối thiểu 15 Test cases).
- [ ] Viết API Test gọi giả lập các endpoint (Case 200 OK và Case 400 Bad Request).
- [ ] Chạy test suite và lưu report.

### Deliverables Checkpoint 6
- [ ] **Báo cáo Benchmark Trước/Sau tối ưu:** Bằng chứng định lượng quan trọng nhất của đồ án.
- [ ] API hoạt động đủ endpoint.
- [ ] Test coverage report (Pytest).
- [ ] Slide Checkpoint 6 (Biểu đồ so sánh thời gian truy vấn, EXPLAIN, Demo các APIs, Kết quả Unit Test).
- [ ] Báo cáo Word Checkpoint 6.

---

## CHECKPOINT 7 — Tuần 13–14: Xây dựng Dashboard

### Tuần 13: Giao diện Overview & Trend
- [ ] Khởi tạo React Project (`create-react-app` hoặc `vite`).
- [ ] Cài đặt thư viện: `axios` (gọi API), `recharts` (vẽ biểu đồ), `tailwindcss` hoặc component lib tùy chọn.
- [ ] Xây dựng Layout chung (Navbar, Sidebar tĩnh).
- [ ] Xây dựng Màn hình **Company Overview**:
  - [ ] Ô Search tìm công ty.
  - [ ] Hiển thị thông tin cơ bản: Tên, Ngành nghề.
  - [ ] Hiển thị Bảng Chỉ tiêu chính (10 metrics).
  - [ ] Tính toán 2 chỉ số phái sinh hiển thị nổi bật: Revenue Growth (%), Profit Margin (%).
  - [ ] **Đặc biệt:** Nút chọn `As-of Date` (Datepicker) -> Khi đổi ngày, gọi lại API và render lại số liệu.
- [ ] Xây dựng Màn hình **Trend**:
  - [ ] Vẽ biểu đồ Line chart 12 quý cho một chỉ tiêu được chọn.

### Tuần 14: Giao diện So sánh & Tinh chỉnh
- [ ] Xây dựng Màn hình **Comparison**:
  - [ ] Combobox cho phép chọn 2 đến 5 công ty.
  - [ ] Bảng so sánh song song các chỉ tiêu của các công ty trong quý gần nhất.
- [ ] Xử lý UI States: Loading spinners, Thông báo lỗi (VD: "Không có dữ liệu cho thời điểm này").
- [ ] (Tùy chọn) Xây dựng màn hình Screening (Lọc công ty theo điều kiện).
- [ ] Tích hợp API thật 100%, xóa bỏ hoàn toàn dữ liệu Mock.

### Deliverables Checkpoint 7
- [ ] Mã nguồn React Frontend hoạt động trơn tru.
- [ ] Frontend kết nối thành công với Backend FastAPI.
- [ ] Slide Checkpoint 7 (Video Demo Dashboard, Trình bày UI flow).
- [ ] Báo cáo Word Checkpoint 7 (Mô tả giao diện, luồng gọi API, Screenshots).

---

## CHECKPOINT 8 — Tuần 15–16: Hoàn thiện & Trình bày cuối kỳ

### Tuần 15: Đóng gói & Triển khai
- [ ] Viết file `docker-compose.yml` định nghĩa 3 services: `postgres`, `backend`, `frontend`.
- [ ] Tạo `Dockerfile` riêng cho Backend và Frontend.
- [ ] Kiểm thử khả năng tái lập (Reproducibility):
  - [ ] `docker-compose down -v` (Xóa toàn bộ DB rác).
  - [ ] `docker-compose up -d --build` (Khởi động hệ thống sạch).
  - [ ] Chạy script Ingestion nạp dữ liệu từ đầu, đảm bảo luồng thông suốt không cần can thiệp thủ công.
- [ ] Cập nhật/Review lại tài liệu Markdown trong repository (README.md, SDD, SRS).

### Tuần 16: Chuẩn bị Báo cáo & Thuyết trình
- [ ] Soạn Báo cáo Word cuối kỳ (Theo cấu trúc 13 phần định sẵn, ghép nội dung từ CP1-CP7).
- [ ] Thiết kế Slide cuối kỳ (10-12 slides). Tập trung vào:
  - [ ] Kiến trúc hệ thống
  - [ ] Cách Bitemporal hoạt động
  - [ ] Hiệu quả của Performance Tuning (Benchmark)
- [ ] Ghi hình 1 Video Demo dự phòng dài 3-5 phút (Điểm qua Overview -> Trend -> Đổi As-of date -> Compare).
- [ ] Chuẩn bị kịch bản trả lời phản biện:
  - Câu hỏi dự kiến: *Sự khác nhau giữa Bitemporal Fact Table và bảng lưu đè?*
  - Câu hỏi dự kiến: *Materialized View giúp ích gì cho Performance? Có nhược điểm gì?*
- [ ] Đẩy source code version cuối cùng lên GitHub.
- [ ] Báo cáo tổng kết đồ án với giảng viên.

### Deliverables Cuối Kỳ
- [ ] Toàn bộ Source Code đóng gói Docker.
- [ ] Báo cáo Word Final.
- [ ] Slide Final & Video dự phòng.
- [ ] Passed hệ thống!

---
*Ghi chú: Toàn bộ các hạng mục mở rộng (Thêm công ty, Authen/Author, Cache Redis, CI/CD, dữ liệu Việt Nam) thuộc về "Future Work" hoặc Đồ án Tốt nghiệp, **TUYỆT ĐỐI KHÔNG** dành thời gian làm trong học kỳ này nếu các Checkpoint chính (Must Have) chưa đạt Definition of Done.*
