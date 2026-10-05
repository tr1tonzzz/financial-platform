# Thử nghiệm nhỏ: crawler → PDF → OCR → chỉ tiêu DHG

Ngày chạy: **05/10/2026**. Phụ lục của [báo cáo 1](bao-cao-01.md). Đây là thử nghiệm công cụ thực trên mẫu phát triển, đủ để minh họa tính khả thi ban đầu; chưa là nghiệm thu hệ thống hay đo độ chính xác trên dữ liệu độc lập.

## 1. Câu hỏi và phạm vi

Có thể tự tìm/tải BCTC từ website doanh nghiệp, lấy số từ hai trang báo cáo và tính lại ví dụ LNST/CFO không? Nếu PDF không có lớp chữ dùng được, OCR có hỗ trợ không và có lỗi gì?

Crawler được giới hạn ở **một trang danh mục DHG, tối đa hai PDF**, không duyệt toàn website. Mẫu phân tích là [BCTC kiểm toán DHG năm 2025](https://dhgpharma.com.vn/sites/default/files/2026-03/DHG-Audited-FS-2025-VN.pdf), trang PDF 10–11; bản bán niên 2026 chỉ được tải để thử thu thập, không đưa vào phép so sánh năm. Hai cột năm nay/năm trước tương ứng 2025/2024; đơn vị VND và phạm vi Công ty CP Dược Hậu Giang được kiểm tra thủ công từ nguồn.

Sáu ô đối chiếu gồm LNST, CFO và điều chỉnh tỷ giá, mỗi khoản hai năm. Bảng tham chiếu là số đã chép/đọc thủ công trong [hồ sơ ca DHG](../../../research-profit-cash-dividend/evidence/case-dhg-2025.json). Người thực hiện cũng đọc lại trang gốc để xác nhận lỗi OCR. Đây là đối chiếu cùng người trên mẫu phát triển, chưa có người kiểm độc lập.

## 2. Công cụ đã chạy và kết quả

| Bước | Công cụ | Kết quả quan sát |
|---|---|---|
| Tìm và tải | Python `urllib` + `lxml`, script crawler có sẵn trong repo | Trang danh mục HTTP 200, 12 liên kết PDF ứng viên; bộ lọc chọn hai kỳ FY-2025/H1-2026 và tải được cả hai |
| Kiểm tra nguồn/version | SHA-256, lưu HTML/PDF/log, yêu cầu HTTP có điều kiện | Hai PDF lưu thành công; chạy lại cùng cấu hình nhận **2/2 HTTP 304**, tái sử dụng bản cục bộ đã kiểm hash |
| Đọc lớp chữ | `pypdf` | PDF FY2025 có 40 trang; **12/12 trang đầu trả về 0 ký tự**, gồm trang 10–11. Chưa kiểm lớp chữ toàn bộ 40 trang |
| Chuyển trang thành ảnh | Poppler `pdftoppm`, 220 DPI | Render thành công hai trang PDF 10 và 11 |
| Nhận dạng chữ | Tesseract.js, `vie` + `eng` | Trang 10: 2.000 ký tự, 3,175 giây; trang 11: 2.772 ký tự, 4,238 giây |
| Trích số từ OCR | Script Python nhỏ, tìm nhãn dòng và hai số VND | Có ứng viên cho cả sáu ô; **5 đúng, 1 sai, 0 thiếu** so với tham chiếu |
| Tính chỉ tiêu | Python từ bốn số LNST/CFO trích được | LNST +9,43%; CFO −7,94%; CFO/LNST 2025 = 1,423 lần, cột 2024 = 1,692 lần |

Crawler kiểm `robots.txt` và nhận kết quả cho phép đối với các URL đã truy cập; giới hạn host DHG, tối thiểu một giây giữa request, không bật tùy chọn thử khi robots không rõ. Thử nghiệm chỉ xác nhận adapter và trang danh mục này tại thời điểm chạy, chưa xác nhận mọi kỳ hoặc mọi website.

Tổng thời gian nhận dạng hai trang khoảng **7,413 giây**, cộng khởi tạo worker **1,383 giây**. Đây là thời gian công cụ trên máy hiện tại, chưa gồm toàn bộ tải/render/đối chiếu và chưa đo thời gian người duyệt. Confidence OCR trang 10/11 lần lượt 87/89 **không phải tỷ lệ số liệu đúng**.

## 3. Số trích được và lỗi thực

| Trường | Năm | Số OCR/parser, VND | Tham chiếu, VND | Kết quả |
|---|---:|---:|---:|---|
| LNST | 2025 | 852.354.107.582 | 852.354.107.582 | Khớp |
| LNST | 2024 | 778.920.119.960 | 778.920.119.960 | Khớp |
| CFO | 2025 | 1.212.967.705.385 | 1.212.967.705.385 | Khớp |
| CFO | 2024 | 1.317.583.405.328 | 1.317.583.405.328 | Khớp |
| Điều chỉnh tỷ giá, dòng 04 | 2025 | −246.438.677 | −246.436.677 | **Sai −2.000** |
| Điều chỉnh tỷ giá, dòng 04 | 2024 | 324.569.255 | 324.569.255 | Khớp |

OCR nhận `6` thành `8` trong số âm năm 2025. Parser vẫn nhận đây là một số hợp lệ, cho thấy kiểm tra định dạng không đủ để phát hiện lỗi. Nếu chỉ thay ô này vào cầu nối thủ công đã khớp và giữ nguyên các ô khác, tổng sẽ lệch CFO −2.000 VND. Đây là phép minh họa ảnh hưởng lỗi, **chưa phải cầu nối trích tự động toàn bộ**.

Văn bản OCR còn đọc mã dòng `01` thành `07` và làm hỏng dòng tổng trước thay đổi vốn lưu động. Script nhỏ hiện tìm ba nhãn được chọn, giữ dấu âm ngoặc và đọc hai cột có dấu chấm phân nhóm; chưa kiểm tự động tất cả mã dòng, đơn vị, năm và scope. Vì vậy, sáu ứng viên chưa được coi là sáu fact đã duyệt. Không sửa văn bản OCR gốc để che lỗi; kết quả đối chiếu được lưu riêng.

## 4. Cách chạy lại

Chạy từ thư mục gốc repo. Môi trường đã dùng: Python **3.12.14**, `lxml` **6.1.1**, `pypdf` **6.10.0**, Node **24.19.0**, Tesseract.js **7.0.0**, Poppler **26.07.0**. Đặt ba biến PowerShell `$pdfRenderer`, `$ocrModule`, `$evidenceDir` theo máy; module OCR cần truy cập được dữ liệu ngôn ngữ lần đầu hoặc đã có cache.

```powershell
$evidenceDir = 'data-sets/research-evidence/2026-10-05-report-01'
$pdfRenderer = 'C:/path/to/poppler/pdftoppm.exe'
$ocrModule = 'C:/path/to/node_modules/tesseract.js'

python scripts/research/crawl_official_reports.py $evidenceDir --companies DHG --max-pages 1 --max-pdfs-per-company 2
python scripts/research/probe_report01.py prepare $evidenceDir --pdftoppm $pdfRenderer
node scripts/research/probe_ocr.cjs $ocrModule "$evidenceDir/page-jobs.json" "$evidenceDir/ocr"
python scripts/research/probe_report01.py check $evidenceDir
```

Lần đầu ở thư mục trống tải PDF; lần sau có thể nhận 304 nếu nguồn không đổi. Website, nội dung và OCR có thể thay đổi: không bảo đảm mọi lần chạy có đúng số ứng viên hoặc thời gian như lần đã ghi. `page-jobs.json` được tạo lại với đường dẫn ảnh trên máy đang chạy.

Minh chứng lần chạy này:

- [Crawler lần đầu](../../../../data-sets/research-evidence/2026-10-05-report-01/run-20261005T050125032756Z.json) và [lần kiểm tra lại](../../../../data-sets/research-evidence/2026-10-05-report-01/run-20261005T050405747233Z.json).
- [Đọc PDF và phiên bản môi trường](../../../../data-sets/research-evidence/2026-10-05-report-01/pdf-probe.json), hash FY2025 `abaaac8d3813329db1987e769f325fbee7b8c4776b4205b26a4673f95b589973` khớp bản dùng cho ví dụ thủ công.
- [Log OCR](../../../../data-sets/research-evidence/2026-10-05-report-01/ocr/ocr-run.json), văn bản [trang 10](../../../../data-sets/research-evidence/2026-10-05-report-01/ocr/dhg-fy2025-p10-ocr.txt) và [trang 11](../../../../data-sets/research-evidence/2026-10-05-report-01/ocr/dhg-fy2025-p11-ocr.txt).
- [Đối chiếu sáu ô và chỉ tiêu từ OCR](../../../../data-sets/research-evidence/2026-10-05-report-01/comparison.json).
- Script [crawler](../../../../scripts/research/crawl_official_reports.py), [OCR](../../../../scripts/research/probe_ocr.cjs), [chuẩn bị và đối chiếu](../../../../scripts/research/probe_report01.py).

## 5. Ý nghĩa đối với hướng project

Mẫu nhỏ đã chạy được đoạn **tìm nguồn → tải → thử đọc PDF → OCR → trích ứng viên → đối chiếu → tính chỉ tiêu**, không chỉ đọc số thủ công. Kết quả 4/4 ô LNST/CFO khớp hỗ trợ tiếp tục làm prototype. Lỗi tỷ giá và lỗi mã dòng hỗ trợ yêu cầu giữ nguồn, duyệt số và kiểm tổng; chưa có cơ sở bỏ bước kiểm soát.

Để giữ báo cáo 1 gọn, chưa cần thử nhiều bộ OCR hoặc xây crawler tổng quát. Bước tiếp theo nên thử một PDF có lớp chữ dùng được và một tài liệu khác mẫu phát triển, đo số đúng/sai/thiếu cùng phút duyệt. Cổ tức, sáu fact đầy đủ của pilot, nhiều doanh nghiệp và giao diện review vẫn là phần cần triển khai. Báo cáo trình bày bằng Markdown; PDF/ảnh/JSON/TXT trong thư mục dữ liệu chỉ là nguồn và minh chứng kỹ thuật.
