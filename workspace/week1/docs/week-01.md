# Nhật ký tuần 1 — W01-03: một báo cáo năm, sáu ô tham chiếu

> Điều chỉnh theo yêu cầu tiếp ngày 11/10/2026: mẫu đầu chính chuyển sang **VNM 2025**, gộp buổi 1–2 và dùng PaddleOCR thật trong môi trường project. Hồ sơ HPG dưới đây giữ làm lịch sử nhập thủ công bằng xem ảnh Codex, **không đáp ứng quy trình OCR mới**, không tính thành minh chứng Paddle. Xem [nhật ký VNM 2025](vnm-2025.md).

Ngày thực hiện: **11/10/2026**. Kế hoạch hiện hành v6; hồ sơ đã chuyển vào `workspace/week1/` theo yêu cầu người thực hiện. Phạm vi lần này là phần **“Một báo cáo năm, sáu ô thật”** do người thực hiện yêu cầu. Chưa ghi tuần 1 hoàn thành.

**Kết quả:** đã xác minh một BCTC HPG năm 2025 hợp nhất, đã kiểm toán và nhập sáu ô tham chiếu có nguồn. Trạng thái `self_checked_reference`, dùng phát triển parser. Người thực hiện chưa duyệt; số fact được duyệt để cung cấp trên ứng dụng hiện là **0**. Đây là nhập thủ công từ ảnh PDF, chưa là kết quả PaddleOCR hoặc bộ gold độc lập.

## 1. Hồ sơ tài liệu đã kiểm

| Nội dung | Dữ kiện và bằng chứng trực tiếp |
|---|---|
| Pháp nhân | Công ty Cổ phần Tập đoàn Hòa Phát; bìa PDF trang 1 và header các bảng |
| Mã HPG | Thuyết minh thông tin khái quát, PDF trang 13 / trang in 11 xác nhận mã chứng khoán HPG |
| Kỳ | Năm kết thúc 31/12/2025 trên bìa/KQKD/LCTT; thuyết minh PDF trang 20 / trang in 18 xác nhận năm tài chính từ 01/01 tới 31/12 |
| Phạm vi | Hợp nhất; bìa, tên từng bảng và kiểm toán ghi Công ty cùng các công ty con |
| Kiểm toán | Báo cáo kiểm toán độc lập Deloitte, PDF trang 5–6 / trang in 3–4; chữ ký ngày 24/03/2026 |
| Đơn vị | VND trên từng bảng nguồn PDF trang 7–11; thuyết minh cơ sở lập báo cáo tại PDF trang 20 |
| Phương pháp LCTT | Gián tiếp, xác định từ bố cục lợi nhuận trước thuế và các điều chỉnh tại PDF trang 11 |
| Ngày thu ban đầu | `2026-10-03T04:23:32.844616+00:00`, tức 11:23:32 ngày 03/10/2026 tại Việt Nam; kế thừa manifest thực nghiệm cũ, không lấy thời gian sao chép hôm nay thay ngày thu |
| Ngày công bố | `null` / chưa xác định. Ngày ký kiểm toán, tên file và HTTP Last-Modified không được dùng thay ngày công bố |
| Tệp | 53 trang, 8.270.589 byte; PDF scan, kiểm pypdf thấy 0 trang có native text |
| SHA-256 | `f38c5f75becf7d3f145d27183eec81f119fd4f75e378b983a2763ddc3f7e0c07` |

[URL PDF chính thức](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/03/20260327-hpg-bctc-hop-nhat-nam-2025-sau-kiem-toan.pdf). Nguồn đang dùng là bản đã thu trong project; lần này không tải lại và chưa xác minh nguồn trực tuyến hiện có bản sửa mới hay chưa.

Giữ nguyên [PDF cũ](../../../data-sets/research-evidence/2026-10-03-recent/hpg-fy2025.pdf) và sao chép nguyên byte sang [PDF định danh bằng hash](../data/documents/f38c5f75becf7d3f145d27183eec81f119fd4f75e378b983a2763ddc3f7e0c07.pdf). Hash của cả hai đã kiểm khớp manifest thu cũ. [Hồ sơ nguồn](../data/source-manifest.json) giữ URL, hash, ngày thu, ngày ký và lý do ngày công bố để trống.

## 2. Sáu ô đã nhập

**Đơn vị gốc và chuẩn hóa: VND**, dấu chấm trong số gốc là phân cách hàng nghìn. CSV lưu số chuẩn hóa nguyên, không dấu phân cách; không dùng float. Trang PDF dưới đây tính từ **1**; JSON/CSV lưu `pdf_page_index` từ **0**. Cột chọn là cột hiện tại, không lấy số 2024 thay số 2025.

| Chỉ tiêu / mã trường | Số gốc VND | Dòng | Trang PDF / trang in | Cột gốc | Thời gian kinh tế |
|---|---:|---|---|---|---|
| Tổng LNST / `net_income_total` | 15.514.931.571.606 | 60 | 10 / 8 | Năm nay | 01/01–31/12/2025 |
| CFO / `cfo` | 17.365.859.056.591 | 20 | 11 / 9 | Năm nay | 01/01–31/12/2025 |
| Tiền và tương đương tiền / `cash_equivalents` | 8.300.890.304.205 | 110 | 7 / 5 | Số cuối năm | Số dư 31/12/2025 |
| Tổng tài sản / `total_assets` | 257.899.200.817.547 | 270 | 8 / 6 | Số cuối năm | Số dư 31/12/2025 |
| Tổng nợ phải trả / `total_liabilities` | 126.679.189.940.972 | 300 | 9 / 7 | Số cuối năm | Số dư 31/12/2025 |
| Tổng vốn chủ sở hữu / `total_equity` | 131.220.010.876.575 | 400 | 9 / 7 | Số cuối năm | Số dư 31/12/2025 |

Tên nhãn nguyên bản, mã dòng, đơn vị, kỳ/ngày số dư, nhãn cột so sánh, trang, ảnh nguồn và lý do chọn từng dòng có tại [bản nhập tham chiếu JSON](hpg-2025-reference-input.json) và [reference-facts.csv](../data/reference-facts.csv). Cả sáu xác định được nên không có ô thiếu/mơ hồ trong bộ này. `bbox`, confidence, engine/model để null vì chưa chạy OCR hoặc đo tọa độ.

- LNST là dòng 60 hợp nhất, **không** dùng dòng 61 của công ty mẹ (15.453.174.006.223 VND).
- CFO là dòng 20 sau biến động vốn lưu động, **không** dùng dòng 08 (28.627.072.820.572 VND).
- Tiền là tổng dòng 110, gồm cả 111 và 112, không chỉ tiền dòng 111.
- Nợ là dòng 300, không thay bằng các dòng vay 320/338.
- Vốn chủ là tổng hợp nhất dòng 400, có phần lợi ích cổ đông không kiểm soát 429, không lấy riêng vốn góp 411.

Ảnh nguồn đã đọc ở 110 DPI và đối chiếu số lần hai ở 180 DPI: [tiền](../data/evidence/HPG-2025/detail-07.png), [tài sản](../data/evidence/HPG-2025/detail-08.png), [nợ/vốn](../data/evidence/HPG-2025/detail-09.png), [LNST](../data/evidence/HPG-2025/detail-10.png), [CFO](../data/evidence/HPG-2025/detail-11.png).

## 3. Cột so sánh và kiểm chéo

KQKD/LCTT ghi “Năm trước”; phía tài sản ghi “Số đầu năm”; phía nợ/vốn tại PDF trang 9 ghi **“Số đầu năm (Trình bày lại)”**. Giữ nguyên từng nhãn, không gắn trạng thái trình bày lại của cột so sánh cho số 2025. Thuyết minh PDF trang 20 / trang in 18 ghi **phân loại lại** 54 tỷ VND giữa chi phí phải trả dài hạn 333 và dự phòng phải trả dài hạn 342. Chưa nhập các ô 2024 vào sáu targets 2025.

Kiểm số học từ các dòng nguồn cùng cột hiện tại:

| Phép kiểm | Kết quả VND | Kết quả kiểm |
|---|---:|---|
| Tiền 111 + tương đương tiền 112 | 4.602.047.650.138 + 3.698.842.654.067 = 8.300.890.304.205 | Khớp 110 |
| Tài sản ngắn hạn 100 + dài hạn 200 | 103.659.402.759.724 + 154.239.798.057.823 = 257.899.200.817.547 | Khớp 270 |
| Nợ ngắn hạn 310 + dài hạn 330 | 94.186.268.324.508 + 32.492.921.616.464 = 126.679.189.940.972 | Khớp 300 |
| LNST công ty mẹ 61 + cổ đông không kiểm soát 62 | 15.453.174.006.223 + 61.757.565.383 = 15.514.931.571.606 | Khớp 60 |
| Nợ 300 + vốn chủ 400 | 126.679.189.940.972 + 131.220.010.876.575 = 257.899.200.817.547 | Khớp tài sản 270 |

CFO đối chiếu trực tiếp nhãn, dòng 20, cột và đơn vị; chưa cộng lại toàn bộ các dòng cầu nối CFO. Các phép kiểm trên là kiểm nhất quán trong cùng báo cáo, không phải kiểm độc lập độ chính xác OCR.

## 4. Phân nhóm phát triển/kiểm

Đăng ký tài liệu này là `development`, family `HPG-consolidated-FY2025`, `independent_test_eligible=false`. Khi có bản dịch, bản sửa hoặc bản gần trùng, phải giữ cùng family và development. Số so sánh 2024 đã nhìn trong PDF này không được chuyển thành một mẫu kiểm độc lập. Một hash khác không tự làm tài liệu độc lập; phải kiểm quan hệ nội dung trước khi chia tập. Chưa xây tập kiểm độc lập trong lần này.

## 5. Minh chứng chạy và giới hạn

Đã chạy [script đóng gói tham chiếu](../scripts/prepare_reference_facts.py) với đầu vào JSON nói trên bằng Python bundled. Script chỉ đóng gói số nhập, kiểm chuẩn hóa/hash và đọc lại CSV, không phải parser PDF hoặc bước duyệt DB.

```text
python workspace/week1/scripts/prepare_reference_facts.py workspace/week1/docs/hpg-2025-reference-input.json
```

[Log kiểm](../data/reference-validation.json): hash PDF gốc/bản lưu khớp; 6 dòng; năm phép đối chiếu số học khớp; CSV UTF-8 BOM đọc lại giữ nguyên **tất cả trường**, gồm số tiền chính xác và các trường null thành ô trống. [Bản log lưu cùng tài liệu](hpg-2025-reference-validation.json) lưu lần chạy để theo dõi bằng Git.

Poppler có cảnh báo font Symbol/ArialUnicode khi render bìa, mục lục và các trang đầu; đã đọc ảnh thực tế, các nhãn/số cần dùng ở trang bảng rõ. pypdf đọc PDF nhưng không có native text. Chưa cài thêm package vào venv project, chưa smoke test Paddle hoặc khóa model.

| Hạng mục tuần 1 | Trạng thái sau lần này |
|---|---|
| W01-03 chọn báo cáo và nhập sáu tham chiếu | Đã thực hiện; tự kiểm, chưa duyệt độc lập |
| W01-01 Paddle | Chưa thực hiện trong lần này |
| W01-02 ledger 9 báo cáo / 54 targets | Chưa nối ledger trong lần này; nguồn metadata mới chỉ một báo cáo |
| W01-04 PostgreSQL / candidate / review | Chưa thực hiện |
| W01-05 React / truy nguồn / xuất từ DB | Chưa thực hiện; CSV tham chiếu này chưa là export của ứng dụng |
| W01-06 kiểm luồng web / demo | Chưa thực hiện |

Giờ công của người thực hiện: **chưa ghi nhận**, không lấy 2 giờ dự toán buổi 2 thành giờ thực. Không tự tick checklist cả tuần hoặc soạn Word/slide.

Việc tiếp theo trong lát cắt UC-1: dùng sáu tham chiếu này để tạo candidate có provenance, xây kho PostgreSQL và luồng duyệt. Tích hợp Paddle trên ảnh nguồn riêng, đo đối chiếu với tham chiếu này và giữ nhãn manual/Paddle rõ ràng.

`data-sets/` bị Git-ignore: PDF, ảnh và CSV phải sao lưu riêng. JSON nhập và nhật ký trong thư mục docs có thể theo dõi bằng Git; chúng không thay thế bản sao lưu PDF.

