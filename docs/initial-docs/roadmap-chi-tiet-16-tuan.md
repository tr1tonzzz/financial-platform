# ROADMAP CHI TIẾT TỪNG TUẦN
## Financial Data Platform — 16 tuần, báo cáo 2 tuần/lần

**Cách đọc tài liệu này:** mỗi tuần có danh sách công việc cụ thể (task-level, không phải mục tiêu chung chung). Mỗi Checkpoint (2 tuần) kết thúc bằng nội dung **chính xác** cần viết vào Slide và Word — không phải "viết báo cáo tiến độ" chung chung, mà là bảng/số liệu/hình cụ thể nào phải xuất hiện. Mọi mã FR/NFR/UC/TC tham chiếu tới SRS-FDP-01, SDD-FDP-01, TP-FDP-01.

---

# CHECKPOINT 1 (Tuần 1–2): Vấn đề, Scope, Nền tảng Python

## Tuần 1 — Khảo sát sản phẩm & Cài đặt môi trường

**Việc cần làm:**
- [ ] Cài Python 3.11+, kiểm tra `python --version` chạy đúng.
- [ ] Cài PostgreSQL 15+, tạo 1 database rỗng tên `fdp_dev`, kết nối thử bằng DBeaver/pgAdmin/psql.
- [ ] Cài VS Code + extension Python, Git.
- [ ] Tạo Git repository, viết `.gitignore` (loại `.env`, `__pycache__`, `node_modules`).
- [ ] Học Python: biến, kiểu dữ liệu (int/float/str/list/dict), câu lệnh if/else, vòng lặp for/while — làm 5-10 bài tập nhỏ (không cần chép vào báo cáo).
- [ ] Học Python: viết hàm (`def`), đọc/ghi file text cơ bản (`open()`, `read()`, `write()`).
- [ ] Truy cập trang SEC Financial Statement Data Sets, đọc tài liệu mô tả cấu trúc file (`sub.txt`, `num.txt`, `tag.txt`, `pre.txt`).
- [ ] Tải thử 1 file ZIP của 1 quý bất kỳ (VD: 2023q4), giải nén thủ công, mở bằng Excel/Notepad xem thử vài dòng.
- [ ] Nghiên cứu 4 sản phẩm tham khảo: với mỗi sản phẩm, ghi chú theo 3 câu hỏi — (1) sản phẩm lưu trữ dữ liệu gì, (2) cung cấp gì cho người dùng, (3) điểm nào có thể học/không nên học.

**Kỹ thuật cần nộp cuối tuần (không phải báo cáo, chỉ tự lưu lại):**
- File ghi chú so sánh 4 sản phẩm (bảng đơn giản).
- File ZIP đã giải nén, ghi chú số lượng file và kích thước.

## Tuần 2 — Pandas cơ bản & Chốt Scope

**Việc cần làm:**
- [ ] Học Pandas: `pd.read_csv()` / đọc file tab-delimited bằng `sep='\t'`, xem `.head()`, `.info()`, `.shape`.
- [ ] Học Pandas: lọc dữ liệu (`df[df['col'] == value]`), `.groupby()`, `.value_counts()`.
- [ ] Viết script `explore_data.py`: đọc `sub.txt` và `num.txt` của 1 quý bằng Pandas, in ra:
  - Tổng số dòng mỗi file
  - Số công ty phân biệt (`cik` duy nhất)
  - Số tag XBRL phân biệt trong `num.txt`
  - Top 10 tag xuất hiện nhiều nhất
- [ ] Chọn danh sách sơ bộ 30 công ty (CIK) từ 3–4 ngành khác nhau — ưu tiên công ty lớn, có lịch sử niêm yết lâu (dễ tìm restatement + đủ dữ liệu).
- [ ] Viết Problem Statement (2-3 câu), Product Vision (1 câu), Target Users (liệt kê 2-3 nhóm) — theo đúng khung SRS-FDP-01 Mục 1.2, 2.1, 2.3.
- [ ] Liệt kê rõ Must Have / Should Have / Could Have / Out of Scope cho học kỳ này — copy từ SRS-FDP-01 Mục 2.2 và điều chỉnh nếu cần, KHÔNG tự ý mở rộng thêm.
- [ ] Đọc lại toàn bộ SRS-FDP-01 một lượt, đánh dấu phần nào chưa hiểu để hỏi giảng viên tại buổi báo cáo.

**Deliverable kỹ thuật:**
- Script `explore_data.py` chạy được, có output thống kê rõ ràng.
- Danh sách 30 CIK đã chọn (lưu file `companies.csv`: cik, ticker, name, sic_code).

### 📊 NỘI DUNG SLIDE (Checkpoint 1) — 6-7 slide

1. **Tên đề tài + 1 câu định vị sản phẩm** (lấy nguyên văn từ SRS Mục 2.1).
2. **Vấn đề**: dữ liệu tài chính rời rạc, tag không đồng nhất, mất lịch sử khi có báo cáo điều chỉnh — nêu 1 ví dụ cụ thể tìm được khi khảo sát (VD: "chỉ tiêu Revenue có N tag khác nhau trong dữ liệu quý X").
3. **Bảng so sánh 4 sản phẩm tham khảo** (Nasdaq Data Fabric, AlphaSense, Economatica, Polygon.io) — cột: Data / Storage / Analytics / API / Điểm học được.
4. **Scope học kỳ này**: bảng Must/Should/Could/Out of Scope, có ghi chú rõ "phần nào để dành đồ án tốt nghiệp".
5. **Demo trực tiếp**: chạy `explore_data.py`, chiếu kết quả thống kê thật (số dòng, số công ty, số tag).
6. **Danh sách 30 công ty đã chọn** (bảng rút gọn, có thể chỉ hiện 10 dòng đầu + tổng số).
7. **Kế hoạch tổng quan 16 tuần** (1 slide dạng timeline, không cần chi tiết từng tuần).

### 📄 NỘI DUNG BÁO CÁO WORD (Checkpoint 1) — theo mục

1. **Giới thiệu đề tài** (0.5 trang): tên đề tài, lý do chọn, bối cảnh.
2. **Nghiên cứu thị trường** (1-1.5 trang): phân tích chi tiết 4 sản phẩm tham khảo, bảng so sánh đầy đủ, phần "những gì nên học/không nên copy" (lấy và diễn giải lại từ nghiên cứu đã có).
3. **Problem Statement, Product Vision, Target Users** (0.5 trang) — copy nguyên từ SRS-FDP-01 Mục 1.2, 2.1, 2.3, có thể diễn giải thêm.
4. **Phạm vi đồ án** (0.5-1 trang): bảng Must/Should/Could/Out of Scope kèm giải thích ngắn vì sao mỗi mục được xếp vào nhóm đó.
5. **Kết quả khảo sát dữ liệu ban đầu** (0.5-1 trang): số liệu từ `explore_data.py` (số dòng, số công ty, số tag phân biệt, top 10 tag phổ biến) + nhận xét về độ phức tạp/hỗn loạn của dữ liệu XBRL thô (đây là bằng chứng cho thấy bài toán chuẩn hóa là có thật).
6. **Danh sách 30 công ty đã chọn** (phụ lục, dạng bảng đầy đủ).
7. **Kế hoạch tổng thể 16 tuần** (bảng tóm tắt theo Checkpoint, không cần chi tiết từng tuần trong báo cáo này).

**Định nghĩa hoàn thành (Definition of Done) Checkpoint 1:** Script khảo sát dữ liệu chạy được và cho ra số liệu thật; scope đã chốt bằng văn bản, không đổi trừ khi có lý do chính đáng được ghi vào Change Log của SRS.

---

# CHECKPOINT 2 (Tuần 3–4): Thiết kế Dữ liệu & Kiến trúc

## Tuần 3 — Kết nối Database & Xác định Chỉ tiêu

**Việc cần làm:**
- [ ] Học kết nối Python–PostgreSQL bằng `psycopg2` hoặc `SQLAlchemy`: viết được script connect, execute 1 câu `SELECT 1`.
- [ ] Học câu lệnh `CREATE TABLE`, `INSERT`, và đặc biệt `COPY` (khác `INSERT` ở tốc độ khi nạp dữ liệu lớn).
- [ ] Với 30 công ty đã chọn, kiểm tra thủ công (hoặc bằng script) xem mỗi công ty có đủ dữ liệu 12 quý gần nhất trong file SEC không — loại/thay công ty nào thiếu quá nhiều.
- [ ] Xác định chốt 10 chỉ tiêu canonical (dùng đúng danh sách ở SDD-FDP-01 Mục 3.5) — viết định nghĩa rõ ràng từng chỉ tiêu bằng tiếng Việt dễ hiểu (để dùng lại khi viết báo cáo).
- [ ] Với mỗi chỉ tiêu, tra cứu thử trong `tag.txt`/`num.txt` xem có những tag XBRL phổ biến nào tương ứng (ghi chú thủ công 3-5 tag mỗi chỉ tiêu để chuẩn bị cho `tag_mapping` ở tuần sau).

## Tuần 4 — ERD, Kiến trúc, Use Case

**Việc cần làm:**
- [ ] Vẽ lại ERD đầy đủ theo SDD-FDP-01 Mục 3.1 bằng công cụ (dbdiagram.io, draw.io, hoặc vẽ tay rồi chụp) — không copy nguyên bản mermaid, phải tự vẽ để hiểu.
- [ ] Viết migration script SQL tạo toàn bộ bảng: `company`, `metric_definition`, `tag_mapping`, `financial_fact`, `historical_price`, `ingestion_log`.
- [ ] Chạy migration trên database `fdp_dev`, kiểm tra bằng `\dt` (liệt kê bảng) và `\d financial_fact` (xem cấu trúc bảng).
- [ ] Insert thủ công 10 dòng vào `metric_definition` (10 chỉ tiêu canonical đã chốt).
- [ ] Vẽ lại Architecture Diagram (theo SDD Mục 2.2) — hiểu và giải thích được từng mũi tên nghĩa là gì.
- [ ] Vẽ Use Case Diagram (theo SRS Mục 2.7.1) — điều chỉnh nếu thấy actor/use case nào chưa phù hợp với thực tế đang làm.
- [ ] Viết tài liệu ngắn (nửa trang) giải thích: vì sao chọn fact table long-format thay vì bảng rộng (theo SDD Mục 2.4 — tự viết lại bằng lời của mình, không copy nguyên văn).

**Deliverable kỹ thuật:**
- Database `fdp_dev` có đủ 6 bảng đúng schema, chạy migration không lỗi.
- File `.sql` migration lưu trong Git.

### 📊 NỘI DUNG SLIDE (Checkpoint 2) — 6-7 slide

1. **Kiến trúc hệ thống tổng thể** (Architecture Diagram đã tự vẽ lại).
2. **Use Case Diagram** — giải thích 3 nhóm actor (End User, API Consumer, System Operator) và use case chính.
3. **ERD** (rút gọn, dễ nhìn — không cần hiện hết field, chỉ tên bảng + quan hệ).
4. **Giải thích thiết kế bitemporal**: dùng ví dụ trực quan — "nếu công ty X báo cáo lại Revenue quý Y, hệ thống lưu cả 2 giá trị thay vì ghi đè" (vẽ 1 hình minh họa đơn giản 2 dòng dữ liệu).
5. **Danh mục 10 chỉ tiêu canonical** + ví dụ 2-3 tag XBRL ánh xạ vào 1 chỉ tiêu.
6. **Demo**: chạy `\d financial_fact` trên psql, chiếu schema thật đã tạo.
7. Cập nhật tiến độ, vấn đề gặp phải khi học SQL nâng cao (nếu có).

### 📄 NỘI DUNG BÁO CÁO WORD (Checkpoint 2)

1. **Thiết kế dữ liệu** (1.5-2 trang): ERD đầy đủ + giải thích từng bảng, từng field quan trọng, quan hệ giữa các bảng.
2. **Lý do lựa chọn kiến trúc bitemporal** (1 trang): trình bày dạng so sánh — cách lưu ghi đè thông thường vs. cách lưu long-format giữ lịch sử, có bảng ưu/nhược điểm (tham khảo SDD Mục 2.4, viết lại bằng ngôn ngữ của bạn).
3. **Kiến trúc hệ thống tổng thể** (1 trang): giải thích từng thành phần (Ingestion, Standardization, Validation, Core Store, API, Dashboard) làm gì.
4. **Use Case Model** (0.5-1 trang): Use Case Diagram + bảng đặc tả rút gọn (actor, mô tả, luồng chính) cho 3-4 use case quan trọng nhất.
5. **Danh mục 10 chỉ tiêu canonical** (bảng, phụ lục).
6. **Danh sách 30 công ty final** (nếu có điều chỉnh so với Checkpoint 1, ghi rõ lý do đổi).

**Definition of Done Checkpoint 2:** Database chạy đúng schema; ERD, Architecture Diagram, Use Case Diagram đã hoàn chỉnh và tự giải thích được, không chỉ copy hình.

---

# CHECKPOINT 3 (Tuần 5–6): Vertical Slice — Chuỗi Chạy Thông Đầu Tiên

## Tuần 5 — Ingestion & Mapping tối giản (3 công ty, 3 chỉ tiêu)

**Việc cần làm:**
- [ ] Viết script `ingest.py`: tải 1 file ZIP theo tham số quý, giải nén vào thư mục `data/raw/{quarter}/`.
- [ ] Viết script tạo bảng staging (`staging_sub`, `staging_num`) — schema đơn giản, gần giống cấu trúc gốc của SEC.
- [ ] Dùng `COPY` (qua `psycopg2.copy_expert` hoặc tương đương) nạp `sub.txt`, `num.txt` vào staging.
- [ ] Kiểm tra: `SELECT COUNT(*)` staging phải khớp `wc -l` của file gốc (trừ dòng header).
- [ ] Chọn thủ công 3 công ty (CIK) trong danh sách 30, lọc riêng dữ liệu của 3 công ty này trong staging để test.
- [ ] Viết bảng `tag_mapping` thủ công cho 3 chỉ tiêu: `REVENUE`, `NET_INCOME`, `TOTAL_ASSETS` — tra cứu tag XBRL tương ứng đã ghi chú ở tuần 3, insert vào bảng `tag_mapping`.
- [ ] Viết script `standardize.py`: join `staging_num` với `tag_mapping`, tính giá trị theo `metric_id`, insert vào `financial_fact` (kèm `filed_at`, `accession_no` lấy từ `staging_sub`).
- [ ] Chạy thử toàn bộ cho 3 công ty, kiểm tra bằng `SELECT * FROM financial_fact` — đối chiếu vài giá trị với báo cáo tài chính thật của công ty đó (tra trên trang IR của công ty hoặc SEC EDGAR) để xác nhận đúng.

## Tuần 6 — API & Kiểm thử Vertical Slice

**Việc cần làm:**
- [ ] Học FastAPI cơ bản: tạo project, chạy `uvicorn main:app --reload`, viết route đơn giản trả JSON tĩnh.
- [ ] Viết endpoint thật: `GET /companies/{cik}/financials` — query từ `financial_fact`, trả JSON đúng 3 chỉ tiêu cho 1 công ty.
- [ ] Test bằng Swagger UI (`/docs` tự sinh của FastAPI) — gọi thử với 3 CIK đã nạp.
- [ ] Test bằng Postman: 1 case đúng (CIK tồn tại), 1 case sai (CIK không tồn tại) — kiểm tra hệ thống trả lỗi hợp lý, không crash (tương ứng TC-17 rút gọn).
- [ ] Viết lại toàn bộ pipeline thành 1 script duy nhất chạy tuần tự: `python run_pipeline.py --quarter=2023q4 --companies=3` để dễ demo.
- [ ] (Không bắt buộc, làm nếu còn thời gian) Dựng 1 trang React tối giản, gọi API, hiển thị bảng số liệu thô — không cần đẹp.
- [ ] Chạy lại toàn bộ pipeline 1 lần nữa từ đầu (xóa data, chạy lại) để chắc chắn không có bước nào làm thủ công mà quên ghi vào script.

**Deliverable kỹ thuật — đây là mốc quan trọng nhất học kỳ:**
- Lệnh `python run_pipeline.py` chạy từ đầu đến cuối, không cần can thiệp tay, kết thúc bằng việc gọi API thành công và nhận đúng dữ liệu 3 công ty.

### 📊 NỘI DUNG SLIDE (Checkpoint 3) — 5-6 slide

1. Nhắc lại Architecture Diagram, **khoanh vùng màu** phần đã chạy được (staging → standardize → DB → API).
2. **Demo trực tiếp** (quan trọng nhất buổi này): chạy `run_pipeline.py` trên máy thật, gọi API qua Swagger, chiếu kết quả JSON.
3. Đối chiếu 1 số liệu cụ thể trả về từ API với số liệu thật trên báo cáo tài chính công ty đó (chứng minh dữ liệu đúng, không chỉ chạy được).
4. Khó khăn gặp phải (VD: lỗi kết nối DB, lỗi parse tag) và cách giải quyết.
5. Kế hoạch mở rộng tuần 7-8 (từ 3 công ty lên 30, từ 3 chỉ tiêu lên 10).

### 📄 NỘI DUNG BÁO CÁO WORD (Checkpoint 3)

1. **Mô tả kỹ thuật pipeline v0.1** (1.5 trang): từng bước cụ thể — ingestion làm gì, standardization làm gì, lưu trữ ra sao — kèm sơ đồ (có thể dùng lại Sequence Diagram Ingestion ở SDD Mục 2.6.1, chú thích phần nào đã làm/chưa làm).
2. **Code snippet quan trọng** (1 trang): đoạn code `COPY` staging, đoạn code join `tag_mapping`, đoạn code endpoint API — có chú thích ngắn từng đoạn.
3. **Kết quả kiểm thử thủ công** (0.5 trang): bảng input/output cụ thể — CIK nào, chỉ tiêu nào, giá trị trả về, đối chiếu với nguồn thật.
4. **Đánh giá khả năng mở rộng** (0.5 trang): pipeline hiện tại có điểm nào cần sửa trước khi mở rộng lên 30 công ty × 10 chỉ tiêu (VD: cần xử lý case tag không map được, cần tối ưu tốc độ nạp).

**Definition of Done Checkpoint 3:** Gọi API thật nhận về dữ liệu đã đi qua toàn bộ pipeline, đối chiếu đúng với số liệu thật của công ty. **Đây là điểm kiểm soát cứng (Hard Gate M3) — nếu chưa đạt, báo giảng viên ngay để cắt giảm scope trước khi đi tiếp, theo PP-FDP-01 Mục 5 (R-04).**

---

# CHECKPOINT 4 (Tuần 7–8): Mở rộng Toàn bộ Dữ liệu

## Tuần 7 — Mở rộng Ingestion & Tag Mapping đầy đủ

**Việc cần làm:**
- [ ] Sửa `ingest.py` để chạy được cho nhiều quý liên tiếp (12 quý) bằng vòng lặp hoặc tham số danh sách quý.
- [ ] Chạy ingestion cho toàn bộ 12 quý, toàn bộ 30 công ty (không chỉ 3 công ty như Checkpoint 3) — theo dõi thời gian chạy, log lại nếu có quý nào lỗi tải.
- [ ] Mở rộng `tag_mapping` từ 3 chỉ tiêu lên đủ 10 chỉ tiêu: với mỗi chỉ tiêu còn lại (Gross Profit, EPS, Total Liabilities, Total Equity, Operating Cash Flow, Capex, Shares Outstanding), tra cứu tag XBRL phổ biến và thêm vào bảng mapping.
- [ ] Xử lý case một filing có nhiều tag cùng trỏ 1 chỉ tiêu: cài đặt cột `priority` trong logic standardize (nếu có nhiều giá trị, lấy theo priority thấp nhất/ưu tiên cao nhất).
- [ ] Xử lý case tag không map được: ghi vào bảng/file riêng (`unmapped_tags.csv`) thay vì bỏ qua âm thầm — để phân tích ở tuần 8.

## Tuần 8 — Coverage Report & Validation

**Việc cần làm:**
- [ ] Viết script `coverage_report.py`: với mỗi chỉ tiêu canonical, tính % số filing (trong 30 công ty × 12 quý) resolve được giá trị.
- [ ] Xuất coverage report ra bảng/file, sắp xếp từ chỉ tiêu coverage cao đến thấp — xác định chỉ tiêu nào đang yếu.
- [ ] Nếu có chỉ tiêu coverage quá thấp (<50%), quay lại `unmapped_tags.csv` xem tag nào phổ biến bị bỏ sót, bổ sung vào `tag_mapping`, chạy lại standardize.
- [ ] Viết 3 rule validation theo FR-08:
  - Rule 1: giá trị âm ở chỉ tiêu không cho phép âm (Total Assets, Revenue) → set `is_flagged=true`.
  - Rule 2: duplicate theo khóa `(cik, metric_id, period_end, filed_at, accession_no)` → phát hiện bằng `GROUP BY ... HAVING COUNT(*) > 1`.
  - Rule 3: giá trị lệch quá N lần so với trung vị lịch sử cùng công ty/chỉ tiêu (outlier) → tính bằng Pandas (`median()`, so sánh tỷ lệ).
- [ ] Chạy validation trên toàn bộ dữ liệu, cập nhật cột `is_flagged`, `flag_reason` trong `financial_fact`.
- [ ] Thống kê: bao nhiêu bản ghi bị flag theo từng rule, top 5 công ty/chỉ tiêu có nhiều bản ghi lỗi nhất.

**Deliverable kỹ thuật:**
- Dataset đầy đủ 30 công ty × 12 quý × 10 chỉ tiêu trong `financial_fact`.
- Coverage report hoàn chỉnh.
- Bảng thống kê dữ liệu bị flag.

### 📊 NỘI DUNG SLIDE (Checkpoint 4) — 6 slide

1. Số liệu tổng quan dataset: tổng số dòng `financial_fact`, số công ty, số quý, thời gian chạy ingestion toàn bộ.
2. **Bảng/biểu đồ coverage report** — 10 chỉ tiêu, coverage % từng chỉ tiêu (nên vẽ bar chart cho trực quan).
3. Ví dụ cụ thể: 1 tag khó map (VD: `RevenueFromContractWithCustomerExcludingAssessedTax`) và cách xử lý.
4. Kết quả validation: bao nhiêu % dữ liệu sạch / bị flag, breakdown theo 3 rule.
5. 1 ví dụ thực tế bản ghi bị flag (chụp màn hình dòng dữ liệu + lý do flag).
6. Đánh giá: dataset đã sẵn sàng cho phần bitemporal + benchmark ở Checkpoint 5-6 chưa.

### 📄 NỘI DUNG BÁO CÁO WORD (Checkpoint 4)

1. **Cơ chế tag mapping chi tiết** (1 trang): logic priority, cách xử lý xung đột nhiều tag, ví dụ minh họa bằng dữ liệu thật.
2. **Coverage report đầy đủ** (1 trang): bảng 10 dòng, % coverage, phân tích nguyên nhân với chỉ tiêu coverage thấp (nếu có).
3. **Chi tiết 3 rule validation** (1 trang): công thức/logic mỗi rule + ví dụ bản ghi thật bị phát hiện lỗi bởi từng rule.
4. **Đánh giá chất lượng dữ liệu tổng thể** (0.5 trang): đối chiếu với NFR-04 (coverage ≥70% cho ≥6/10 chỉ tiêu) — đạt hay chưa, nếu chưa thì phương án xử lý.
5. Cập nhật danh sách công ty (nếu có công ty bị loại do thiếu dữ liệu quá nhiều).

**Definition of Done Checkpoint 4:** Coverage đạt NFR-04; toàn bộ dữ liệu 30×12×10 đã nằm trong `financial_fact`, có gắn cờ chất lượng đầy đủ.

---

# CHECKPOINT 5 (Tuần 9–10): Bitemporal & Dữ liệu Giá

## Tuần 9 — Point-in-time Query & Restatement Detection

**Việc cần làm:**
- [ ] Kiểm tra trong dữ liệu 30 công ty đã nạp: tìm các trường hợp có từ 2 `accession_no` khác nhau cho cùng `(cik, metric_id, period_end)` — đây chính là dấu hiệu restatement.
- [ ] Nếu ít/không tìm thấy tự nhiên, thử mở rộng: tải thêm 1-2 quý cũ hơn để tăng khả năng bắt được restatement (các công ty lớn thường nộp lại báo cáo trong vòng 1 năm).
- [ ] Viết script `find_restatements.py`: liệt kê toàn bộ case restatement tìm được (company, metric, period, giá trị cũ, giá trị mới, ngày filed_at của mỗi lần).
- [ ] Cài index `idx_fact_filed_at` (SDD Mục 3.2) trên `financial_fact`.
- [ ] Viết endpoint `GET /companies/{cik}/financials?period=&as_of=` theo đúng SQL pattern ở SDD Mục 3.4 (`DISTINCT ON` + `filed_at <=`).
- [ ] Test thủ công: chọn 1 công ty có restatement, gọi API với 2 giá trị `as_of` (trước và sau ngày filed lần 2), xác nhận 2 kết quả khác nhau (tương ứng TC-19).
- [ ] Test case biên: gọi `as_of` trước cả ngày filing đầu tiên → xác nhận trả về rỗng có kiểm soát, không lỗi 500 (TC-20).

## Tuần 10 — Dữ liệu Giá Cổ phiếu & Benchmark Baseline

**Việc cần làm:**
- [ ] Học dùng thư viện lấy giá cổ phiếu lịch sử (`yfinance` hoặc tương đương) — test lấy giá 1 mã trong 1 khoảng ngày.
- [ ] Viết script `ingest_prices.py`: lấy giá đóng cửa lịch sử cho 30 công ty, khoảng thời gian khớp với 12 quý đã chọn, insert vào `historical_price`.
- [ ] Viết endpoint `GET /companies/{cik}/prices?from=&to=`.
- [ ] Xác định 4 truy vấn đại diện cho benchmark (theo TP-FDP-01 TC-26): (1) lấy 1 công ty 1 kỳ, (2) lấy chuỗi 12 quý 1 chỉ tiêu, (3) so sánh 5 công ty, (4) lọc toàn bộ 30 công ty theo 1 điều kiện.
- [ ] Viết script `benchmark.py`: chạy mỗi truy vấn N lần (VD: 10 lần), đo thời gian trung bình bằng `time.perf_counter()`.
- [ ] Chạy benchmark ở trạng thái **hiện tại (chưa có materialized view, chưa tối ưu)** — đây là baseline, lưu kết quả ra file/bảng.
- [ ] Chạy `EXPLAIN ANALYZE` cho từng truy vấn baseline, lưu lại text output.

**Deliverable kỹ thuật:**
- API `as_of` hoạt động đúng, có bằng chứng cụ thể (2 kết quả khác nhau).
- Danh sách restatement tìm được.
- Dữ liệu giá cổ phiếu đầy đủ 30 công ty.
- Bảng benchmark baseline + EXPLAIN ANALYZE.

### 📊 NỘI DUNG SLIDE (Checkpoint 5) — 6-7 slide

1. Giải thích bitemporal bằng **1 ví dụ thật** tìm được: tên công ty, chỉ tiêu, giá trị trước/sau điều chỉnh, ngày công bố mỗi lần.
2. **Demo trực tiếp**: gọi API với 2 giá trị `as_of`, chiếu 2 response JSON khác nhau cạnh nhau.
3. Sequence Diagram luồng point-in-time (từ SDD Mục 2.6.2) — giải thích ngắn gọn.
4. Danh sách đầy đủ các restatement tìm được (bảng, có thể vài dòng).
5. Giới thiệu dữ liệu giá cổ phiếu đã nạp (số liệu tổng quan).
6. **Bảng benchmark baseline** — nêu rõ đây là "trước khi tối ưu", sẽ so sánh ở Checkpoint 6.
7. 1 slide `EXPLAIN ANALYZE` mẫu (chỉ 1 truy vấn tiêu biểu, không cần hết 4 truy vấn) — chỉ ra `Seq Scan` để tạo tương phản cho Checkpoint sau.

### 📄 NỘI DUNG BÁO CÁO WORD (Checkpoint 5)

1. **Cơ chế bitemporal chi tiết** (1 trang): câu lệnh SQL point-in-time đầy đủ, giải thích từng phần (`DISTINCT ON`, `filed_at <=`).
2. **Toàn bộ danh sách restatement** (1 trang, dạng bảng/phụ lục): company, metric, period, giá trị cũ/mới, ngày filed mỗi lần + 1-2 câu phân tích (VD: "restatement thường xảy ra ở chỉ tiêu X hơn Y").
3. **Mô tả nguồn và cách nạp dữ liệu giá cổ phiếu** (0.5 trang).
4. **Bảng benchmark baseline đầy đủ** (1 trang): 4 truy vấn, thời gian chạy (ms), kèm tóm tắt `EXPLAIN ANALYZE` (loại scan nào được dùng).
5. Kết quả test TC-19, TC-20 (input/output cụ thể).

**Definition of Done Checkpoint 5:** Tìm được tối thiểu 1 restatement thật; nếu không có, phải ghi rõ trong báo cáo và chuẩn bị phương án minh họa thay thế (dữ liệu giả lập có chú thích) theo đúng nguyên tắc trung thực học thuật.

---

# CHECKPOINT 6 (Tuần 11–12): Tối ưu Hiệu năng & API Hoàn chỉnh

## Tuần 11 — Tối ưu & Đo lại Benchmark

**Việc cần làm:**
- [ ] Tạo materialized view `mv_latest_metrics` theo đúng câu lệnh SDD Mục 3.3.
- [ ] Tạo index bổ sung cần thiết (`idx_fact_company_metric_period` nếu chưa có từ Checkpoint 2).
- [ ] Sửa endpoint `/compare` và `/screen` (nếu đã viết) để đọc từ `mv_latest_metrics` thay vì `financial_fact` trực tiếp.
- [ ] Chạy lại đúng 4 truy vấn benchmark của Checkpoint 5 (tuần 10), đo lại thời gian — **sau khi tối ưu**.
- [ ] Chạy lại `EXPLAIN ANALYZE` cho 4 truy vấn, so sánh loại scan trước/sau (`Seq Scan` → `Index Scan`/`Index Only Scan`).
- [ ] Tính tỷ lệ cải thiện (%) cho từng truy vấn, tổng hợp thành 1 bảng so sánh trước/sau.
- [ ] Viết lệnh refresh materialized view (`REFRESH MATERIALIZED VIEW mv_latest_metrics`) và quyết định thời điểm gọi (sau mỗi lần ingestion).

## Tuần 12 — Hoàn thiện API & Viết Test

**Việc cần làm:**
- [ ] Viết nốt các endpoint còn thiếu: `/trend`, `/compare`, `/screen`, `/metrics/coverage`, `/ingestion/logs`, `/health`.
- [ ] Viết response format thống nhất (`{data, meta}`) cho toàn bộ endpoint.
- [ ] Cài Pytest, viết unit test cho module standardization (map đúng tag → đúng metric), module validation (3 rule ở Checkpoint 4) — mục tiêu tối thiểu 15 test case theo NFR-06.
- [ ] Viết API test bằng `TestClient` của FastAPI cho từng endpoint — cả case hợp lệ và case lỗi (VD: CIK không tồn tại → 404, tham số sai định dạng → 400).
- [ ] Chạy toàn bộ test suite (`pytest`), sửa lỗi nếu có test fail.
- [ ] Cập nhật Traceability Matrix trong TP-FDP-01: đánh dấu Pass/Fail cho từng Test Case đã chạy được tới thời điểm này.

**Deliverable kỹ thuật:**
- Bảng benchmark trước/sau tối ưu hoàn chỉnh.
- API đầy đủ toàn bộ endpoint, có test pass.

### 📊 NỘI DUNG SLIDE (Checkpoint 6) — 6-7 slide — **slide quan trọng nhất cả kỳ**

1. **Biểu đồ cột so sánh benchmark trước/sau tối ưu** — 4 truy vấn, 2 cột mỗi truy vấn (trước/sau), có số ms và % cải thiện ghi rõ.
2. Giải thích ngắn gọn cơ chế: index giúp gì, materialized view giúp gì (1 câu mỗi cái, không sa vào lý thuyết).
3. So sánh trực quan `EXPLAIN ANALYZE` trước/sau cho truy vấn cải thiện nhiều nhất (VD: `Seq Scan cost=...` vs `Index Scan cost=...`).
4. Danh sách API endpoint hoàn chỉnh (bảng, demo nhanh qua Swagger).
5. Kết quả test: tổng số test case, số pass/fail, tỷ lệ.
6. Cập nhật Traceability Matrix (có thể chỉ hiện dòng đã Pass, rút gọn).

### 📄 NỘI DUNG BÁO CÁO WORD (Checkpoint 6)

1. **Chi tiết các biện pháp tối ưu** (1 trang): index đã tạo, materialized view, câu lệnh SQL cụ thể.
2. **Bảng benchmark đầy đủ trước/sau** (1 trang): 4 truy vấn × (thời gian trước, thời gian sau, % cải thiện) + `EXPLAIN ANALYZE` đầy đủ (phụ lục nếu dài).
3. **Phân tích kết quả** (0.5 trang): truy vấn nào cải thiện nhiều nhất/ít nhất, vì sao (liên hệ tới loại scan, kích thước dữ liệu quét).
4. **Danh sách API endpoint đầy đủ** (bảng chuẩn, giống OpenAPI spec).
5. **Báo cáo kết quả test** (0.5 trang): số lượng test case theo từng loại (unit/integration/API), tỷ lệ pass, các lỗi đã sửa trong quá trình test.

**Definition of Done Checkpoint 6:** Có bằng chứng benchmark rõ ràng bằng số liệu thật; toàn bộ endpoint trong SRS hoạt động và có test pass.

---

# CHECKPOINT 7 (Tuần 13–14): Xây dựng Dashboard

## Tuần 13 — Company Overview & Trend

**Việc cần làm:**
- [ ] Dựng project React (Vite hoặc Create React App), cài Recharts, cài axios/fetch để gọi API.
- [ ] Viết component tìm kiếm công ty, gọi `GET /companies?search=`.
- [ ] Viết trang **Company Overview**: hiển thị 10 chỉ tiêu chính + 2 chỉ số phái sinh (Revenue Growth YoY, Net Profit Margin — tính ở frontend hoặc lấy từ API `/companies/{cik}/financials`).
- [ ] Viết trang **Trend**: dropdown chọn 1 chỉ tiêu, gọi `GET /trend`, vẽ biểu đồ đường bằng Recharts.
- [ ] Viết control **As-of date** (input type="date"): khi đổi giá trị, gọi lại API `/financials?as_of=`, cập nhật số liệu hiển thị trên Overview — đây là phần trực quan hóa quan trọng nhất cho bitemporal.
- [ ] Test thủ công: chọn công ty có restatement đã tìm được ở Checkpoint 5, gạt as-of qua lại, xác nhận số liệu đổi đúng.

## Tuần 14 — Comparison & Hoàn thiện UI

**Việc cần làm:**
- [ ] Viết trang **Comparison**: cho phép chọn 2-5 công ty (multi-select), chọn chỉ tiêu, gọi `POST /compare`, hiển thị bảng song song.
- [ ] (Chỉ làm nếu đúng tiến độ) Viết trang **Screening** đơn giản: form nhập 1-2 điều kiện, gọi `POST /screen`, hiển thị bảng kết quả.
- [ ] Xử lý loading state (spinner/skeleton khi đang gọi API) và error state (thông báo khi API lỗi) cho toàn bộ trang.
- [ ] Kiểm tra responsive cơ bản (không cần hỗ trợ mobile, chỉ cần không vỡ layout ở màn hình desktop thường dùng).
- [ ] Review lại toàn bộ luồng UI theo checklist UC-01 → UC-06 trong SRS, đảm bảo mỗi Use Case đều thao tác được trên UI thật.

**Deliverable kỹ thuật:**
- Dashboard chạy được, tối thiểu 3 trang (Overview, Trend, Comparison) tích hợp thật với backend, không còn dữ liệu giả lập hardcode.

### 📊 NỘI DUNG SLIDE (Checkpoint 7) — 5-6 slide

1. Demo trực tiếp toàn bộ luồng: tìm công ty → overview → trend → **gạt as-of date (điểm nhấn)** → chọn thêm công ty → so sánh.
2. Nên có video quay sẵn luồng demo này làm dự phòng ngay từ bây giờ (theo TP-FDP-01 Mục 7.2), không đợi tới cuối kỳ.
3. Ảnh chụp màn hình từng trang chính (phòng khi demo trực tiếp có sự cố mạng buổi báo cáo).
4. Những gì đã làm được/chưa làm được so với kế hoạch (đặc biệt nêu rõ nếu Screening chưa kịp làm).

### 📄 NỘI DUNG BÁO CÁO WORD (Checkpoint 7)

1. **Mô tả từng màn hình** (1 trang): luồng tương tác, API được gọi ở mỗi màn hình (liên hệ UC-01 → UC-06).
2. **Screenshot các trang chính** (phụ lục).
3. **Đánh giá UI/UX ở mức cơ bản** (0.5 trang): nêu rõ đã ưu tiên tính đúng của dữ liệu hơn thẩm mỹ giao diện, đúng định vị sản phẩm ở SRS.
4. Cập nhật tiến độ Must/Should/Could Have — mục nào chắc chắn hoàn thành, mục nào có nguy cơ không kịp.

**Definition of Done Checkpoint 7:** Toàn bộ dashboard gọi dữ liệu thật, không có màn hình nào dùng dữ liệu hardcode.

---

# CHECKPOINT 8 (Tuần 15–16): Hoàn thiện & Trình bày Cuối kỳ

## Tuần 15 — Đóng gói, Kiểm thử Tích hợp, Chuẩn bị Dự phòng

**Việc cần làm:**
- [ ] Viết `Dockerfile` cho backend, `Dockerfile` cho frontend (hoặc build tĩnh serve qua nginx), viết `docker-compose.yml` gộp cả 3 service (postgres, backend, frontend).
- [ ] Test: xóa toàn bộ container/volume, chạy `docker-compose up` từ đầu, kiểm tra hệ thống lên đúng (NFR-08, TC-36).
- [ ] Viết script seed dữ liệu từ file backup (không phải chạy lại ingestion từ SEC) để khởi động nhanh khi demo.
- [ ] Xuất file backup dữ liệu (`pg_dump`) sau khi đã có dữ liệu đầy đủ và sạch, lưu kèm source code (theo TP-FDP-01 Mục 7.1).
- [ ] Test TC-37: ngắt mạng, restore từ backup, chạy thử toàn bộ UC-01 → UC-06 — xác nhận hoạt động không cần internet.
- [ ] Viết integration test cuối: 1 script chạy toàn luồng từ ingestion (dùng dữ liệu mẫu nhỏ) → DB → gọi API → nhận đúng kết quả.
- [ ] Hoàn thiện README: hướng dẫn cài đặt, chạy, seed dữ liệu, chạy test.
- [ ] Quay video demo dự phòng (3-5 phút) theo đúng kịch bản sẽ trình bày.
- [ ] (Tùy chọn, nếu còn thời gian) Deploy backend lên Render, frontend lên Vercel theo TP-FDP-01 Mục 7.3.

## Tuần 16 — Báo cáo Cuối kỳ & Luyện Demo

**Việc cần làm:**
- [ ] Tổng hợp toàn bộ nội dung 8 Checkpoint thành báo cáo cuối kỳ hoàn chỉnh (dùng lại SRS/SDD/TP/PP làm khung, không viết lại từ đầu).
- [ ] Viết phần "Hạn chế của hệ thống" trung thực (VD: coverage chưa đạt 100%, Screening chưa hoàn thiện nếu vậy).
- [ ] Viết phần "Hướng phát triển" dựa trên mục Future Work đã xác định từ trước.
- [ ] Làm slide cuối kỳ (10-12 slide) theo cấu trúc đã thống nhất trước đó.
- [ ] Luyện demo tối thiểu 2 lần liên tiếp không lỗi, bấm đúng thứ tự kịch bản.
- [ ] Kiểm tra checklist trước ngày bảo vệ (TP-FDP-01 Mục 7.4): file backup, video, sạc pin, cổng kết nối.
- [ ] Chuẩn bị trả lời câu hỏi dự kiến: "Vì sao chọn bitemporal thay vì lưu thông thường?", "Benchmark đo như thế nào, có đáng tin không?", "Phần nào để dành đồ án tốt nghiệp và vì sao?".

### 📊 NỘI DUNG SLIDE CUỐI KỲ (10-12 slide)

1. Giới thiệu đề tài, vấn đề giải quyết
2. Nghiên cứu sản phẩm tham khảo (rút gọn)
3. Kiến trúc hệ thống + Use Case tổng quan
4. ERD + giải thích bitemporal
5. Demo: point-in-time query (số liệu trước/sau restatement thật)
6. Demo: benchmark trước/sau tối ưu
7. Demo: dashboard (Overview → Trend → As-of → Comparison)
8. Kết quả đạt được so với scope cam kết (bảng Must/Should Have — cái nào làm, cái nào không, vì sao)
9. Kết quả test (số test case, tỷ lệ pass) + kế hoạch dự phòng demo
10. Khó khăn & bài học kinh nghiệm
11. Hướng phát triển (đồ án tốt nghiệp)
12. Kết luận + Cảm ơn

### 📄 NỘI DUNG BÁO CÁO WORD CUỐI KỲ

Tổng hợp đầy đủ theo cấu trúc chuẩn (Giới thiệu → Nghiên cứu → Yêu cầu → Thiết kế → Công nghệ → Triển khai → Kết quả → Kiểm thử → Đánh giá → Hạn chế → Hướng phát triển → Kết luận → Phụ lục), lấy trực tiếp nội dung đã viết ở 7 Checkpoint trước, không viết mới từ đầu — chỉ cần biên tập lại cho mạch lạc và bổ sung phần Kết luận/Đánh giá tổng thể.

**Definition of Done Checkpoint 8 (cuối kỳ):** Toàn bộ Must Have hoạt động; demo chạy được 2 lần liên tiếp không lỗi; có phương án dự phòng đầy đủ (backup data, video); báo cáo phản ánh đúng thực tế đã làm.

---

## Bảng tổng hợp nhanh (dùng để tự theo dõi tiến độ)

| Tuần | Việc trọng tâm nhất trong tuần |
|---|---|
| 1 | Cài môi trường + học Python cơ bản + khảo sát 4 sản phẩm |
| 2 | Pandas cơ bản + khảo sát dữ liệu SEC + chốt scope |
| 3 | Kết nối DB + chốt 10 chỉ tiêu |
| 4 | ERD + migration + Use Case Diagram |
| 5 | Ingestion + mapping 3 chỉ tiêu cho 3 công ty |
| 6 | **API đầu tiên chạy thông — Hard Gate** |
| 7 | Mở rộng ingestion 30 công ty × 12 quý |
| 8 | Coverage report + validation |
| 9 | Point-in-time query + tìm restatement |
| 10 | Dữ liệu giá + benchmark baseline |
| 11 | Index + materialized view + benchmark sau tối ưu |
| 12 | Hoàn thiện API + unit/API test |
| 13 | Dashboard: Overview + Trend + As-of |
| 14 | Dashboard: Comparison (+ Screening nếu kịp) |
| 15 | Docker + backup + video dự phòng |
| 16 | Báo cáo cuối kỳ + luyện demo |
