# LỘ TRÌNH THỰC HIỆN ĐỒ ÁN — Financial Data Platform
## Chu kỳ báo cáo 2 tuần/lần — 16 tuần — 8 Checkpoint

**Nguyên tắc xuyên suốt:** Học kỳ này chỉ làm **Must Have + phần lõi của Should Have** trong SRS đã chốt (10 chỉ tiêu, 30 công ty, bitemporal, benchmark, API, dashboard core). Các phần còn lại — Screening đầy đủ, đối chiếu đa nguồn, mở rộng dữ liệu Việt Nam, authentication, caching, mở rộng số công ty/chỉ tiêu — dồn hết sang **Phần "Future Work — Đồ án tốt nghiệp"** ở cuối tài liệu, không động vào trong học kỳ này dù có dư thời gian giữa chừng.

Mỗi Checkpoint kết thúc bằng **1 slide thuyết trình + 1 báo cáo Word**, nộp cho giảng viên. Cấu trúc gợi ý cho từng loại tài liệu nằm ngay dưới mỗi Checkpoint để bạn không phải tự nghĩ lại format mỗi 2 tuần.

---

## CHECKPOINT 1 — Tuần 1–2: Xác định vấn đề & Học nền tảng

### Tuần 1
- Cài đặt môi trường: Python, PostgreSQL, VS Code, Git.
- Học Python cơ bản: biến, kiểu dữ liệu, list/dict, vòng lặp, hàm, đọc/ghi file.
- Nghiên cứu 4 sản phẩm tham khảo (Nasdaq Data Fabric, AlphaSense, Economatica, Polygon.io) — ghi chú vào bảng so sánh.
- Tải thử 1 file ZIP từ SEC Financial Statement Data Sets, chỉ giải nén xem thử cấu trúc file, chưa cần xử lý.

### Tuần 2
- Học Pandas cơ bản: đọc file, DataFrame, filter, groupby.
- Viết script nhỏ: đọc `num.txt` và `sub.txt` bằng Pandas, in ra số dòng, số công ty phân biệt (`cik`), số tag phân biệt.
- Xác định Problem Statement, Product Vision, Target Users (theo mẫu SRS Mục 1–2).
- Chốt scope học kỳ này: liệt kê rõ Must/Should Have sẽ làm và Could Have/Out of Scope sẽ **không** làm.

### Deliverable kỹ thuật
- Script khảo sát dữ liệu chạy được, in ra thống kê cơ bản của 1 quý dữ liệu SEC.
- Bảng so sánh 4 sản phẩm tham khảo.

### Slide (Checkpoint 1) — cấu trúc gợi ý
1. Tên đề tài, mục tiêu
2. Vấn đề (problem statement) — dữ liệu tài chính rời rạc, khó truy vấn, mất lịch sử khi có báo cáo điều chỉnh
3. Bảng so sánh 4 sản phẩm tham khảo + điểm học được / không copy
4. Định vị sản phẩm (1 câu) + đối tượng người dùng
5. Scope học kỳ này: Must/Should/Out of scope (nêu rõ phần nào để dành cho đồ án tốt nghiệp)
6. Demo nhỏ: kết quả script khảo sát dữ liệu (số dòng, số công ty, số tag)
7. Kế hoạch 16 tuần (tổng quan 1 slide)

### Báo cáo Word (Checkpoint 1) — cấu trúc gợi ý
1. Giới thiệu đề tài
2. Nghiên cứu thị trường (chi tiết bảng so sánh 4 sản phẩm)
3. Problem Statement & Product Vision
4. Đối tượng người dùng & Use case chính
5. Phạm vi đồ án (Scope) — bảng Must/Should/Could/Out of scope
6. Kết quả khảo sát dữ liệu ban đầu (số liệu + nhận xét về độ phức tạp của tag XBRL)
7. Kế hoạch tổng thể 16 tuần

### Definition of Done
Chạy được script đọc dữ liệu SEC bằng Pandas; có tài liệu scope đã chốt, không thay đổi giữa chừng trừ khi có lý do bắt buộc.

---

## CHECKPOINT 2 — Tuần 3–4: Thiết kế dữ liệu & Kiến trúc

### Tuần 3
- Học: kết nối Python–PostgreSQL (`psycopg2` hoặc `SQLAlchemy`), câu lệnh `COPY`, khái niệm transaction cơ bản.
- Khảo sát sâu hơn: chọn danh sách 30 công ty cụ thể (CIK) thuộc 3–4 ngành; kiểm tra các công ty này có đủ dữ liệu 12 quý gần nhất không.
- Xác định danh mục 10 chỉ tiêu canonical (theo SRS Mục 6.2), viết định nghĩa rõ từng chỉ tiêu.

### Tuần 4
- Thiết kế ERD đầy đủ (company, metric_definition, tag_mapping, financial_fact, historical_price, ingestion_log).
- Viết migration script tạo schema trong PostgreSQL.
- Vẽ kiến trúc hệ thống tổng thể (mermaid diagram theo SRS Mục 5).
- Viết tài liệu quyết định thiết kế: vì sao chọn long format/fact table thay vì bảng rộng; vì sao cần bitemporal.

### Deliverable kỹ thuật
- Database đã tạo schema đầy đủ, chạy migration không lỗi.
- Danh sách 30 công ty (CIK) đã chốt kèm lý do chọn.
- Danh mục 10 chỉ tiêu canonical có định nghĩa rõ ràng.

### Slide (Checkpoint 2)
1. Kiến trúc hệ thống tổng thể (mermaid diagram)
2. ERD (rút gọn, dễ nhìn)
3. Giải thích quyết định thiết kế: fact table + bitemporal là gì, vì sao chọn (so sánh nhanh với cách làm "bảng rộng" thông thường)
4. Danh sách 30 công ty + 10 chỉ tiêu đã chốt
5. Demo: schema đã chạy trên PostgreSQL (chạy `\d financial_fact` trực tiếp hoặc screenshot)

### Báo cáo Word (Checkpoint 2)
1. Thiết kế dữ liệu: ERD đầy đủ, giải thích từng bảng, từng field
2. Lý do lựa chọn kiến trúc bitemporal (so sánh ưu/nhược với cách lưu trữ ghi đè thông thường)
3. Kiến trúc hệ thống tổng thể, giải thích từng layer
4. Danh sách công ty & chỉ tiêu đã chốt + tiêu chí lựa chọn
5. Cập nhật tiến độ so với kế hoạch tuần 1-2

### Definition of Done
Database chạy đúng schema; có tài liệu ERD + kiến trúc hoàn chỉnh để dùng lại cho báo cáo cuối kỳ.

---

## CHECKPOINT 3 — Tuần 5–6: Vertical Slice (bản chạy thông đầu tiên)

### Tuần 5
- Viết script ingestion tối giản: tải 1 quý, nạp `sub.txt`/`num.txt` vào bảng staging bằng `COPY`.
- Viết bảng `tag_mapping` thủ công cho **3 chỉ tiêu** (Revenue, Net Income, Total Assets) áp dụng cho **3 công ty** trong danh sách 30.
- Viết script standardization: từ staging → tính ra giá trị 3 chỉtiêu cho 3 công ty, insert vào `financial_fact`.

### Tuần 6
- Học FastAPI cơ bản: tạo project, viết 1 endpoint `GET /companies/{cik}/financials`.
- Kết nối endpoint tới database, trả đúng dữ liệu 3 công ty đã nạp.
- Test bằng Swagger UI/Postman.
- (Không bắt buộc, làm nếu kịp) Dựng 1 trang React tối giản gọi API và hiển thị bảng số liệu thô.

### Deliverable kỹ thuật
- **Chuỗi end-to-end chạy thông:** file ZIP → staging → chuẩn hóa → database → API trả đúng dữ liệu.
- Đây là mốc kiểm soát quan trọng nhất của học kỳ.

### Slide (Checkpoint 3)
1. Nhắc lại kiến trúc, khoanh vùng phần đã chạy được (vertical slice) trên sơ đồ
2. Demo trực tiếp: gọi API, xem kết quả JSON trả về đúng số liệu 3 công ty
3. Khó khăn gặp phải khi học Python/FastAPI và cách giải quyết
4. Điều chỉnh kế hoạch (nếu có) cho các tuần tiếp theo

### Báo cáo Word (Checkpoint 3)
1. Mô tả kỹ thuật pipeline v0.1: từng bước ingestion → standardization → lưu trữ
2. Code snippet quan trọng (script nạp dữ liệu, script mapping, endpoint API)
3. Kết quả kiểm thử thủ công (input/output cụ thể)
4. Đánh giá: pipeline có sẵn sàng mở rộng lên 30 công ty × 10 chỉ tiêu không, cần sửa gì

### Definition of Done
Gọi API thật, nhận về dữ liệu thật đã đi qua toàn bộ pipeline — không phải dữ liệu giả lập hardcode.

**⚠️ Điểm kiểm soát cứng:** Nếu hết tuần 6 chưa đạt Definition of Done này, phải báo giảng viên ngay để cắt giảm scope (giảm số công ty hoặc số chỉ tiêu), không tiếp tục mở rộng khi nền chưa vững.

---

## CHECKPOINT 4 — Tuần 7–8: Mở rộng Ingestion & Chuẩn hóa toàn bộ

### Tuần 7
- Mở rộng `tag_mapping` cho đủ 10 chỉ tiêu canonical.
- Mở rộng ingestion nạp đủ 12 quý cho 30 công ty.
- Xử lý các trường hợp tag không map được — ghi log riêng, không làm crash pipeline.

### Tuần 8
- Viết script tính **coverage report**: % filing resolve được cho mỗi chỉ tiêu.
- Viết 3 rule validation (giá trị âm bất thường, duplicate, outlier) theo SRS FR-08.
- Chạy validation trên toàn bộ dữ liệu đã nạp, thống kê số bản ghi bị gắn cờ.

### Deliverable kỹ thuật
- Dataset đầy đủ: 30 công ty × 12 quý × 10 chỉ tiêu trong `financial_fact`.
- Bảng coverage report.
- Bảng thống kê dữ liệu bị flag kèm lý do.

### Slide (Checkpoint 4)
1. Số liệu tổng quan dataset đã nạp (số dòng, số công ty, số quý)
2. Bảng coverage report — chỉ tiêu nào tốt, chỉ tiêu nào yếu, vì sao
3. Ví dụ cụ thể 1-2 tag XBRL khó map và cách xử lý
4. Kết quả validation: bao nhiêu % dữ liệu sạch, bao nhiêu bị flag

### Báo cáo Word (Checkpoint 4)
1. Chi tiết cơ chế tag mapping (priority, cách xử lý xung đột)
2. Bảng coverage đầy đủ 10 chỉ tiêu + phân tích nguyên nhân chỉ tiêu có coverage thấp
3. Chi tiết 3 rule validation + ví dụ minh họa từng loại lỗi phát hiện được
4. Đánh giá chất lượng dữ liệu tổng thể, quyết định có cần giảm phạm vi công ty/chỉ tiêu không

### Definition of Done
Coverage đạt tối thiểu 70% cho ít nhất 6/10 chỉ tiêu (theo NFR-04 trong SRS); nếu không đạt, ghi rõ lý do và phương án xử lý trong báo cáo.

---

## CHECKPOINT 5 — Tuần 9–10: Bitemporal & Dữ liệu giá cổ phiếu

### Tuần 9
- Kiểm tra và đảm bảo cơ chế bitemporal hoạt động đúng: nạp thêm các filing có tính chất điều chỉnh (nếu công ty trong tập 30 có), giữ được nhiều `filed_at` cho cùng kỳ.
- Viết truy vấn point-in-time (`as_of`) theo đúng logic `DISTINCT ON` + `filed_at <=`.
- Chạy dò tìm và **liệt kê các trường hợp restatement thật** tìm được trong dataset.

### Tuần 10
- Viết script nạp dữ liệu giá cổ phiếu lịch sử (dùng thư viện `yfinance` hoặc nguồn tương đương) cho 30 công ty.
- Đo **benchmark baseline** (trước khi tối ưu): thời gian chạy 4 truy vấn đại diện (1 công ty 1 kỳ; chuỗi 12 quý; so sánh 5 công ty; toàn bộ 30 công ty) — chưa có index/materialized view.

### Deliverable kỹ thuật
- API `as_of` trả đúng kết quả khác nhau trước/sau ngày nộp báo cáo điều chỉnh.
- Danh sách các restatement phát hiện được (tên công ty, kỳ, giá trị trước/sau, ngày điều chỉnh).
- Dataset giá cổ phiếu đầy đủ.
- Bảng benchmark baseline.

### Slide (Checkpoint 5)
1. Giải thích khái niệm bitemporal bằng ví dụ trực quan: 1 công ty cụ thể, số liệu trước/sau điều chỉnh
2. Demo trực tiếp: gọi API với 2 giá trị `as_of` khác nhau, cho ra 2 kết quả khác nhau
3. Danh sách restatement tìm được (bảng ngắn gọn)
4. Bảng benchmark baseline — nêu rõ đây là "trước khi tối ưu", sẽ so sánh ở checkpoint sau

### Báo cáo Word (Checkpoint 5)
1. Giải thích chi tiết cơ chế bitemporal + câu lệnh SQL point-in-time
2. Toàn bộ danh sách restatement phát hiện được + phân tích (VD: restatement thường xảy ra ở loại chỉ tiêu nào)
3. Mô tả nguồn và cách nạp dữ liệu giá cổ phiếu
4. Bảng benchmark baseline đầy đủ (4 truy vấn, thời gian chạy, kèm `EXPLAIN` nếu có)

### Definition of Done
Tìm được tối thiểu 1 trường hợp restatement thật trong dataset (nếu không có, phải nêu rõ trong báo cáo và có phương án minh họa thay thế, ghi chú rõ là dữ liệu giả lập).

---

## CHECKPOINT 6 — Tuần 11–12: Tối ưu hiệu năng & Hoàn thiện API

### Tuần 11
- Thêm index cho `financial_fact` theo SRS Mục 6.1.
- Tạo materialized view `latest_metrics`.
- Đo lại benchmark (4 truy vấn giống Checkpoint 5) — **sau khi tối ưu**.
- Lưu kết quả `EXPLAIN ANALYZE` trước/sau để so sánh trực quan.

### Tuần 12
- Hoàn thiện toàn bộ endpoint còn lại trong SRS Mục 7 (`/compare`, `/trend`, `/prices`, `/metrics/coverage`, `/ingestion/logs`).
- Viết unit test cho các module chính (standardization, validation) bằng Pytest — tối thiểu 15 test case.
- Viết API test cho các endpoint (case hợp lệ + không hợp lệ).

### Deliverable kỹ thuật
- Bảng so sánh benchmark trước/sau tối ưu (tỷ lệ cải thiện %).
- API đầy đủ endpoint, có test pass.

### Slide (Checkpoint 6)
1. Bảng/biểu đồ so sánh benchmark trước/sau tối ưu — đây là slide quan trọng nhất của cả kỳ, nên trình bày rõ ràng (bar chart thời gian chạy)
2. Giải thích ngắn gọn: index/materialized view giúp gì (đọc query plan trước/sau)
3. Danh sách endpoint API hoàn chỉnh + demo nhanh qua Swagger
4. Kết quả test: số test case, tỷ lệ pass

### Báo cáo Word (Checkpoint 6)
1. Chi tiết các index/materialized view đã tạo + lý do
2. Bảng benchmark đầy đủ trước/sau, kèm `EXPLAIN ANALYZE` plan (chụp/paste)
3. Phân tích: truy vấn nào cải thiện nhiều nhất, vì sao
4. Danh sách API endpoint đầy đủ (bảng chuẩn OpenAPI-style)
5. Báo cáo kết quả unit test/API test

### Definition of Done
Có bằng chứng benchmark rõ ràng (số liệu trước/sau); toàn bộ API endpoint trong SRS đã hoạt động và có test.

---

## CHECKPOINT 7 — Tuần 13–14: Xây dựng Dashboard

### Tuần 13
- Dựng project React, gọi API thật (không mock data).
- Trang **Company Overview**: tìm kiếm công ty, hiển thị các chỉ tiêu chính + 2 chỉ số phái sinh (Revenue Growth, Profit Margin).
- Trang **Trend**: biểu đồ đường (Recharts) cho 1 chỉ tiêu theo 12 quý.
- Điều khiển **As-of date**: chọn ngày, gọi lại API, cập nhật số liệu — đây là phần trực quan hóa quan trọng nhất cho khái niệm bitemporal.

### Tuần 14
- Trang **Comparison**: chọn 2–5 công ty, hiển thị bảng so sánh song song các chỉ tiêu.
- (Chỉ làm nếu đúng tiến độ, không bắt buộc) Trang Screening đơn giản với 1-2 điều kiện lọc.
- Xử lý lỗi cơ bản trên UI (loading state, thông báo lỗi khi API fail).

### Deliverable kỹ thuật
- Dashboard chạy được, tích hợp thật với backend, tối thiểu 3 trang (Overview, Trend, Comparison).

### Slide (Checkpoint 7)
1. Demo trực tiếp dashboard: tìm công ty → xem overview → xem trend → gạt as-of date → so sánh 2-3 công ty
2. Đây là slide nên quay video demo dự phòng, tránh rủi ro demo lỗi trực tiếp
3. Những gì đã làm được / chưa làm được so với kế hoạch (Comparison, Screening)

### Báo cáo Word (Checkpoint 7)
1. Mô tả từng màn hình, luồng tương tác người dùng
2. Cách frontend gọi backend (danh sách API được dùng ở từng màn hình)
3. Screenshot các trang chính
4. Đánh giá UI/UX ở mức cơ bản (không cần sâu, chỉ cần nêu đã ưu tiên rõ ràng dữ liệu hơn thẩm mỹ)

### Definition of Done
Toàn bộ dashboard gọi dữ liệu thật từ API, không còn dữ liệu giả lập hardcode ở bất kỳ trang nào.

---

## CHECKPOINT 8 — Tuần 15–16: Hoàn thiện & Trình bày cuối kỳ

### Tuần 15
- Đóng gói toàn bộ hệ thống bằng Docker Compose, test chạy lại từ đầu trên trạng thái sạch (xóa container, chạy lại `docker-compose up`, kiểm tra tái lập được).
- Viết test tích hợp toàn luồng (ingestion → DB → API → UI).
- Hoàn thiện tài liệu: README, tài liệu kiến trúc, ERD final.

### Tuần 16
- Viết báo cáo cuối kỳ đầy đủ (tổng hợp toàn bộ 8 checkpoint).
- Làm slide trình bày cuối kỳ.
- Luyện tập demo tối thiểu 2 lần, chuẩn bị video demo dự phòng.
- Chuẩn bị trả lời các câu hỏi dự kiến từ hội đồng (đặc biệt về bitemporal và benchmark — đây là 2 phần khác biệt nhất của đồ án).

### Deliverable kỹ thuật (cuối kỳ)
- Hệ thống hoàn chỉnh, tái lập được bằng `docker-compose up`.
- Toàn bộ mã nguồn trên Git repository.
- Bảng benchmark, coverage report, danh sách restatement — đính kèm phụ lục báo cáo.

### Slide cuối kỳ — cấu trúc gợi ý (10-12 slide)
1. Giới thiệu đề tài, vấn đề giải quyết
2. Nghiên cứu sản phẩm tham khảo (rút gọn từ Checkpoint 1)
3. Kiến trúc hệ thống tổng thể
4. Data model (ERD) + giải thích bitemporal
5. Demo: point-in-time query (số liệu trước/sau restatement)
6. Demo: benchmark trước/sau tối ưu
7. Demo: dashboard (Overview → Trend → Comparison)
8. Kết quả đạt được so với scope đã cam kết (bảng Must/Should Have — cái nào làm, cái nào không)
9. Khó khăn & bài học kinh nghiệm
10. Hướng phát triển tiếp theo (đồ án tốt nghiệp)
11. Kết luận

### Báo cáo Word cuối kỳ — cấu trúc gợi ý (theo chuẩn báo cáo đồ án)
1. Giới thiệu (Problem Statement, Product Vision, Target Users)
2. Nghiên cứu thị trường (4 sản phẩm tham khảo)
3. Yêu cầu hệ thống (Functional/Non-functional Requirements — lấy từ SRS)
4. Thiết kế hệ thống (Kiến trúc, ERD, giải thích bitemporal)
5. Công nghệ sử dụng và lý do lựa chọn
6. Triển khai (mô tả từng module: ingestion, standardization, validation, API, frontend)
7. Kết quả: coverage report, danh sách restatement, bảng benchmark trước/sau
8. Kiểm thử (unit test, integration test, kết quả)
9. Đánh giá kết quả đạt được so với scope ban đầu
10. Hạn chế của hệ thống hiện tại
11. Hướng phát triển (Mục "Future Work" bên dưới)
12. Kết luận
13. Phụ lục: code snippet quan trọng, ERD đầy đủ, danh sách API

### Definition of Done (cuối kỳ)
Toàn bộ Must Have trong SRS hoạt động; demo chạy được ít nhất 2 lần liên tiếp không lỗi; báo cáo và slide phản ánh đúng những gì đã làm, không phóng đại tính năng chưa hoàn thiện.

---

## Bảng tổng hợp tiến độ theo Checkpoint

| CP | Tuần | Trọng tâm | Deliverable chính |
|---|---|---|---|
| 1 | 1–2 | Vấn đề & Học nền tảng | Scope chốt, script khảo sát dữ liệu |
| 2 | 3–4 | Thiết kế dữ liệu | ERD, schema DB, kiến trúc |
| 3 | 5–6 | **Vertical Slice** | Pipeline end-to-end 3 công ty |
| 4 | 7–8 | Mở rộng dữ liệu | Dataset đầy đủ 30 công ty, coverage report |
| 5 | 9–10 | Bitemporal | As-of query, danh sách restatement |
| 6 | 11–12 | Tối ưu & API | Benchmark trước/sau, API đầy đủ |
| 7 | 13–14 | Dashboard | UI 3-4 trang, tích hợp thật |
| 8 | 15–16 | Hoàn thiện | Báo cáo, demo cuối kỳ |

---

## Future Work — Dành cho Đồ án Tốt nghiệp (KHÔNG làm trong học kỳ này)

Liệt kê rõ để tránh việc "tiện thể làm luôn" giữa kỳ làm lệch tiến độ:

- Mở rộng số lượng công ty (từ 30 lên hàng trăm/nghìn) và số chỉ tiêu canonical (từ 10 lên 20+).
- Basic Financial Screening đầy đủ với nhiều điều kiện kết hợp.
- Tích hợp thêm nguồn dữ liệu thứ hai (VD: vnstock cho thị trường Việt Nam) để đối chiếu đa nguồn.
- Cơ chế reconciliation khi hai nguồn dữ liệu cho kết quả khác nhau.
- Authentication/authorization đầy đủ, phân quyền người dùng.
- Caching layer (Redis) cho các truy vấn phổ biến.
- Mở rộng bộ benchmark (thêm nhiều loại truy vấn, thử nghiệm partitioning theo thời gian ở quy mô lớn hơn).
- Triển khai production thật (cloud hosting, CI/CD).
- Có thể cân nhắc TimescaleDB để so sánh hiệu năng với PostgreSQL thuần cho dữ liệu time-series.

*Ghi chú trong báo cáo cuối kỳ: nêu rõ đây là những hướng đã xác định nhưng chủ động không đưa vào scope học kỳ này để đảm bảo chất lượng và tính hoàn thiện của phần lõi (core Financial Data Platform).*

---

## Nguyên tắc quản lý rủi ro xuyên suốt lộ trình

1. Nếu một checkpoint không đạt Definition of Done, **báo ngay cho giảng viên tại buổi báo cáo đó**, đừng cố "gánh" sang checkpoint sau — rủi ro dồn cục ở cuối kỳ là nguyên nhân phổ biến nhất khiến đồ án dạng này thất bại.
2. Không bắt đầu bất kỳ hạng mục nào thuộc "Future Work" trước khi hoàn thành Must Have.
3. Mỗi checkpoint, dành ít nhất 30 phút so sánh lại tiến độ thực tế với bảng tổng hợp — nếu lệch quá 1 tuần, ưu tiên cắt giảm theo đúng thứ tự đã nêu trong SRS (Mục 9: cắt Screening → Comparison → giảm số công ty), không cắt bitemporal và benchmark.
