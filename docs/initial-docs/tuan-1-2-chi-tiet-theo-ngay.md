# CHI TIẾT THEO NGÀY — Tuần 1–2
## Financial Data Platform — Checkpoint 1

**Giả định:** mỗi ngày dành khoảng 2-3 giờ (buổi tối sau giờ học), cuối tuần có thể dành 4-5 giờ. Nếu học full-time cho đồ án, có thể gộp 2 ngày thành 1 và kết thúc sớm hơn.

---

## TUẦN 1

### Ngày 1 (Thứ 2) — Cài đặt môi trường
- [ ] Tải và cài Python 3.11+ (python.org), kiểm tra bằng `python --version` hoặc `python3 --version`.
- [ ] Cài VS Code, cài extension "Python" (Microsoft) và "Pylance".
- [ ] Cài Git, cấu hình `git config --global user.name` và `user.email`.
- [ ] Tạo tài khoản GitHub (nếu chưa có), tạo repository mới tên `financial-data-platform`.
- [ ] Clone repository về máy, tạo file `.gitignore` với nội dung tối thiểu: `__pycache__/`, `.env`, `venv/`, `node_modules/`, `*.pyc`.
- [ ] Tạo virtual environment: `python -m venv venv`, kích hoạt (`venv\Scripts\activate` trên Windows hoặc `source venv/bin/activate` trên Mac/Linux).
- [ ] Commit lần đầu: "Initial commit: project setup".

### Ngày 2 (Thứ 3) — Cài Database & Python cơ bản (phần 1)
- [ ] Tải và cài PostgreSQL 15+ (nhớ lưu lại mật khẩu superuser khi cài).
- [ ] Cài pgAdmin hoặc DBeaver (công cụ xem database bằng giao diện).
- [ ] Tạo 1 database mới tên `fdp_dev` qua pgAdmin/DBeaver.
- [ ] Thử kết nối, chạy câu lệnh `SELECT version();` để xác nhận PostgreSQL hoạt động (đây là SQL bạn đã biết, chỉ cần quen giao diện công cụ).
- [ ] Học Python: kiểu dữ liệu cơ bản — `int`, `float`, `str`, `bool`, `list`, `dict`. Viết 1 file `learn_basics.py` tự thực hành: tạo vài biến, in ra bằng `print()`, thử `type()`.
- [ ] Học Python: câu lệnh điều kiện `if/elif/else` — viết 1 hàm nhỏ tự luyện (VD: kiểm tra số chẵn/lẻ).

### Ngày 3 (Thứ 4) — Python cơ bản (phần 2): vòng lặp, hàm
- [ ] Học vòng lặp `for` và `while` — thực hành với `list` (VD: in ra bình phương từng số trong 1 danh sách).
- [ ] Học viết hàm (`def function_name(param):`), khái niệm return value.
- [ ] Học `dict` (key-value) — vì dữ liệu SEC sẽ ở dạng bảng, việc quen thao tác dict/list-of-dict rất cần thiết.
- [ ] Bài tập nhỏ tự luyện: viết hàm nhận vào 1 list số, trả về (min, max, trung bình) — không dùng thư viện, tự viết logic bằng vòng lặp (giúp hiểu bản chất trước khi dùng Pandas).
- [ ] Commit: "Learn Python basics".

### Ngày 4 (Thứ 5) — Đọc/ghi file & làm quen SEC
- [ ] Học đọc/ghi file text trong Python: `open()`, `.read()`, `.readlines()`, `with open(...) as f:`.
- [ ] Thực hành: tạo 1 file `.txt` bất kỳ (VD: danh sách tên), viết script đọc và in ra từng dòng.
- [ ] Truy cập trang SEC Financial Statement Data Sets (sec.gov/dera/data/financial-statement-data-sets), đọc phần mô tả cấu trúc dữ liệu (đọc kỹ, không cần hiểu hết ngay).
- [ ] Ghi chú lại (bằng tiếng Việt, ngôn ngữ của bạn): `sub.txt` chứa gì, `num.txt` chứa gì, `tag.txt` chứa gì — mỗi file 2-3 câu.

### Ngày 5 (Thứ 6) — Tải thử dữ liệu SEC
- [ ] Tải 1 file ZIP của 1 quý bất kỳ (khuyến nghị chọn quý gần đây, VD 2023q4, để dữ liệu đầy đủ).
- [ ] Giải nén thủ công (không cần code), xem các file bên trong bằng Excel hoặc Notepad++ (mở thử vài dòng đầu của `sub.txt` và `num.txt`).
- [ ] Ghi chú: mỗi dòng trong `num.txt` có những cột gì (adsh, tag, ddate, value...) — đối chiếu với mô tả đã đọc ở Ngày 4.
- [ ] Thử tìm thủ công (Ctrl+F trong Excel) 1 công ty quen thuộc (VD: tìm "Apple" trong `sub.txt`), ghi lại CIK của công ty đó.

### Ngày 6 (Thứ 7) — Nghiên cứu 4 sản phẩm tham khảo
- [ ] Đọc/tìm hiểu Nasdaq Data Fabric — ghi chú: sản phẩm cho ai dùng, lưu trữ/cung cấp gì.
- [ ] Đọc/tìm hiểu Polygon.io — chú ý cách họ thiết kế API (vào trang docs xem thử cấu trúc endpoint).
- [ ] Đọc/tìm hiểu Economatica — chú ý các tính năng screener, so sánh công ty.
- [ ] Đọc/tìm hiểu AlphaSense — chú ý đây là dạng search/AI trên tài liệu, khác hẳn 3 sản phẩm kia.
- [ ] Tổng hợp vào 1 bảng: mỗi sản phẩm — Data gì / Lưu trữ ra sao / Có Analytics không / Có API không / Điểm học được.

### Ngày 7 (Chủ nhật) — Nghỉ hoặc bù tiến độ
- [ ] Nếu đúng tiến độ: nghỉ ngơi, hoặc đọc thêm tài liệu Pandas để chuẩn bị tuần 2.
- [ ] Nếu trễ: dùng ngày này bù lại các việc chưa xong ở Ngày 1-6, ưu tiên xong phần cài đặt môi trường và bảng so sánh 4 sản phẩm trước khi sang tuần 2.

**Checklist cuối Tuần 1:**
- [ ] Môi trường Python + PostgreSQL + Git đã chạy được.
- [ ] Đã đọc và giải nén thử được 1 file ZIP từ SEC.
- [ ] Có bảng so sánh 4 sản phẩm tham khảo.
- [ ] Tự tin với: biến, if/else, vòng lặp, hàm, đọc file cơ bản trong Python.

---

## TUẦN 2

### Ngày 8 (Thứ 2) — Pandas cơ bản (phần 1)
- [ ] Cài Pandas: `pip install pandas`.
- [ ] Học đọc file bằng Pandas: `pd.read_csv('sub.txt', sep='\t')` (file SEC là tab-delimited, không phải comma).
- [ ] Thực hành các lệnh xem dữ liệu: `.head()`, `.shape`, `.info()`, `.columns`.
- [ ] Đọc thử `sub.txt` và `num.txt` của file đã tải ở Tuần 1, in ra `.head()` để xem có đọc đúng không.

### Ngày 9 (Thứ 3) — Pandas cơ bản (phần 2)
- [ ] Học lọc dữ liệu: `df[df['cik'] == '0000320193']` (lọc theo điều kiện).
- [ ] Học `.value_counts()` — dùng để đếm số lần xuất hiện (VD: đếm tag nào xuất hiện nhiều nhất trong `num.txt`).
- [ ] Học `.groupby()` cơ bản — VD: group theo `cik`, đếm số dòng mỗi công ty.
- [ ] Thực hành: dùng `.nunique()` đếm số công ty phân biệt, số tag phân biệt trong file đã tải.

### Ngày 10 (Thứ 4) — Viết script khảo sát dữ liệu
- [ ] Tạo file `explore_data.py` trong thư mục project.
- [ ] Viết code đọc `sub.txt`, `num.txt` bằng Pandas.
- [ ] In ra: tổng số dòng mỗi file, số `cik` phân biệt, số `tag` phân biệt trong `num.txt`.
- [ ] Thêm: `.value_counts().head(10)` để in ra Top 10 tag phổ biến nhất.
- [ ] Chạy thử, kiểm tra output có hợp lý không (số công ty phải khớp quy mô thực tế của 1 quý báo cáo SEC).
- [ ] Commit: "Add data exploration script".

### Ngày 11 (Thứ 5) — Chọn danh sách 30 công ty
- [ ] Xác định 3-4 ngành muốn đưa vào (VD: Technology, Retail, Energy, Banking) — nên chọn ngành có đặc điểm báo cáo tài chính khác nhau rõ rệt để so sánh sau này thú vị hơn.
- [ ] Với mỗi ngành, chọn 7-8 công ty lớn, quen thuộc (dễ tra cứu đối chiếu số liệu thật sau này, dễ có restatement vì lịch sử niêm yết lâu).
- [ ] Tra CIK của từng công ty (tìm trên SEC EDGAR company search hoặc trong `sub.txt` đã tải).
- [ ] Lưu danh sách vào file `companies.csv` với cột: `cik, ticker, name, sic_code`.
- [ ] Dùng script đã viết ở Ngày 10, lọc thử xem 30 công ty này có xuất hiện đủ trong file quý đã tải không (kiểm tra nhanh bằng `.isin()`).

### Ngày 12 (Thứ 6) — Viết Problem Statement & Scope
- [ ] Viết Problem Statement: 2-3 câu mô tả vấn đề (dựa trên những gì đã học ở Tuần 1 về sự rời rạc/hỗn loạn của dữ liệu tài chính thô).
- [ ] Viết Product Vision: 1 câu định vị sản phẩm.
- [ ] Liệt kê Target Users: 2-3 nhóm.
- [ ] Đối chiếu với bảng Must/Should/Could/Out of Scope đã có sẵn trong SRS-FDP-01 — đọc kỹ, xác nhận có đồng ý với scope này không, ghi chú nếu muốn điều chỉnh gì để trao đổi với giảng viên.

### Ngày 13 (Thứ 7) — Chuẩn bị Slide & Word Checkpoint 1
- [ ] Viết Slide theo cấu trúc đã định (7 slide: đề tài, vấn đề, bảng so sánh, scope, demo, danh sách công ty, kế hoạch tổng quan).
- [ ] Chèn số liệu thật từ `explore_data.py` vào slide (không dùng số liệu giả định).
- [ ] Viết bản nháp báo cáo Word (các mục 1-4 trước, mục 5-7 hoàn thiện sau khi có kết quả cuối).
- [ ] Chuẩn bị chạy thử demo script trên máy sẽ dùng để báo cáo (đảm bảo không lỗi môi trường vào phút chót).

### Ngày 14 (Chủ nhật) — Rà soát & Nộp
- [ ] Đọc lại toàn bộ Slide + Word, kiểm tra số liệu nhất quán giữa 2 tài liệu.
- [ ] Chạy thử lại `explore_data.py` lần cuối để chắc chắn demo không lỗi.
- [ ] Commit toàn bộ code + tài liệu lên Git.
- [ ] Chuẩn bị câu hỏi muốn hỏi giảng viên (nếu scope có điểm chưa chắc chắn).

**Checklist cuối Tuần 2 (= cuối Checkpoint 1):**
- [ ] `explore_data.py` chạy hoàn chỉnh, có số liệu thật.
- [ ] File `companies.csv` với 30 công ty đã chọn.
- [ ] Problem Statement, Scope đã chốt bằng văn bản.
- [ ] Slide + Word đã sẵn sàng nộp/trình bày.

---

## Mẹo giữ tiến độ cho 2 tuần này
- Đừng cố "học hết Python" trước khi bắt tay vào dữ liệu thật — học tới đâu dùng tới đó là đủ. Mục tiêu Tuần 1-2 không phải giỏi Python, mà là **đủ Python để đọc được dữ liệu SEC bằng Pandas**.
- Nếu Ngày 1-2 mất nhiều thời gian hơn dự kiến do lỗi cài đặt (rất phổ biến, đặc biệt với PostgreSQL trên Windows), đừng hoảng — đây là chuyện bình thường, dùng ngày Chủ nhật (Ngày 7) để bù, không cần báo giảng viên vì đây chưa phải Hard Gate.
- Nếu tới Ngày 10 mà chưa chạy được `explore_data.py`, đây là tín hiệu cần xem lại: có thể đang học Python quá sâu (VD: học OOP, decorator) trong khi chưa cần — quay lại đúng phạm vi "biến, vòng lặp, hàm, đọc file, Pandas cơ bản" là đủ cho Checkpoint 1.
