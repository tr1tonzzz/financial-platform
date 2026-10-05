# Thử nghiệm PDF và OCR trên báo cáo mới

Ngày chạy: 03/10/2026. Báo cáo số đo từ [manifest](download-evidence.json), [summary](probe-summary.json) và [đối chiếu](ocr-core-check.json). Chưa tạo bộ chấm độc lập.

## 1. Tải và kiểm tra lớp text

`pdfplumber 0.11.9` trích text mọi trang. Quy ước thống kê `text_pages`: số trang có hơn 100 ký tự trích được. Vì vậy “0 trang text” trong bảng không khẳng định tuyệt đối mọi trang không có bất kỳ ký tự nào; nó cho thấy không có lớp chữ đủ dùng theo phép kiểm tra này.

| ID tài liệu | Kỳ / ngôn ngữ | Trang PDF | Trang text |
|---|---|---:|---:|
| hpg-fy2025 | Năm 2025 / VN | 53 | 0 |
| hpg-q12026 | Q1/2026 / VN | 37 | 37 |
| hpg-h12026 | H1/2026 / VN | 67 | 0 |
| dhg-fy2025 | Năm 2025 / VN | 40 | 0 |
| dhg-q12026 | Q1/2026 / VN | 36 | 0 |
| dhg-h12026 | H1/2026 / VN | 45 | 0 |
| vhc-fy2025 | Năm 2025 / VN | 64 | 0 |
| vhc-q12026 | Q1/2026 / VN | 46 | 0 |
| vhc-h12026 | H1/2026 / VN | 65 | 0 |
| vhc-fy2025-en | Năm 2025 / EN | 64 | 0 |
| vhc-q12026-en | Q1/2026 / EN | 44 | 0 |
| vhc-h12026-en | H1/2026 / EN | 65 | 18 |
| vnm-q12026 | Q1/2026 / VN | 71 | 0 |
| vnm-h12026 | H1/2026 / VN | 72 | 0 |
| hnx-vhe-fy2025-curl | Năm 2025 / VN | 35 | 35 |
| **Tổng** | **15 file, 5 công ty** | **804** | **90** |

HPG Q1 có text nhưng nhiều chữ/số bị mã hóa lỗi, nên 37 trang text không đồng nghĩa đã đọc chính xác. VHC H1 tiếng Anh có lớp text ở một phần báo cáo, các phần khác cần OCR; tiếng Anh không tự đồng nghĩa IFRS. Cần đọc cơ sở lập báo cáo. Các bản EN/VN là ứng viên đối chiếu, phải kiểm tra cùng kỳ, scope và phiên bản trước ghép.

## 2. OCR thực chạy

Đã chọn và xem ảnh 10 trang chứa bảng chính của hai PDF: DHG FY2025, trang PDF 7–11; VNM Q1/2026, trang PDF 7, 9, 10, 11, 13. Poppler render 220 dpi; Tesseract.js 7.0.0, tiếng Việt và tiếng Anh, một worker dùng lại; Node thực chạy 24.15.0. Thư viện đã có trong runtime, không cài thêm gói mới.

- Khởi tạo OCR: 1,111 giây.
- Nhận dạng 10 ảnh: 29,785 giây; trung vị 2,803 giây/trang.
- Số đo không bao gồm toàn bộ thời gian tải, render, chọn trang, dựng bảng, sửa lỗi và duyệt số.
- Confidence của OCR trên mẫu khoảng 82–91; đây là điểm của engine, không phải tỷ lệ giá trị tài chính đúng.

Tesseract.js đọc ảnh, không trực tiếp đọc PDF; cần render trước. `pdfplumber` phù hợp PDF có text và không cung cấp OCR sẵn. [Tài liệu Tesseract.js](https://github.com/naptha/tesseract.js), [tài liệu pdfplumber](https://github.com/jsvine/pdfplumber).

## 3. Sáu số đã đối chiếu từ ảnh

**Đơn vị VND**, giữ nguyên số nguyên. DHG: báo cáo cấp doanh nghiệp theo mẫu B01-DN, không gán là hợp nhất; VNM: hợp nhất. Hai cột là hai công ty và hai kỳ khác nhau, không dùng bảng này để so sánh hiệu quả kinh doanh trực tiếp.

| Chỉ tiêu | DHG FY2025 | Trang PDF / in | VNM Q1/2026 | Trang PDF / in |
|---|---:|---|---:|---|
| Tiền và tương đương tiền | 129.895.664.996 | 7 / 5 | 2.077.596.293.461 | 7 / 6 |
| Tổng tài sản | 5.173.881.628.997 | 8 / 6 | 55.429.011.127.169 | 9 / 8 |
| Nợ phải trả | 1.036.616.453.045 | 9 / 7 | 18.740.931.850.130 | 10 / 9 |
| Vốn chủ sở hữu tổng | 4.137.265.175.952 | 9 / 7 | 36.688.079.277.039 | 10 / 9 |
| LNST tổng | 852.354.107.582 | 10 / 8 | 2.458.221.002.532 | 11 / 10 |
| CFO | 1.212.967.705.385 | 11 / 9 | 269.326.997.516 | 13 / 12 |

Nguồn gốc: [DHG BCTC kiểm toán 2025](https://dhgpharma.com.vn/sites/default/files/2026-03/DHG-Audited-FS-2025-VN.pdf), [VNM BCTC soát xét Q1/2026 hợp nhất](https://d8um25gjecm9v.cloudfront.net/cms/20260429_VNM_BCTC_DA_SOAT_XET_Q1_2026_HOP_NHAT_VN_d44326741a.pdf). File gốc và ảnh theo ID có trong thư mục raw evidence.

`Tài sản − Nợ phải trả − VCSH = 0` cho cả hai bộ giá trị sau đối chiếu. Đẳng thức là kiểm tra nhất quán, chưa đủ đảm bảo đúng kỳ, đúng cột hoặc đúng đơn vị.

## 4. Lỗi thực tế và giới hạn

Bộ trích thử tìm nhãn theo regex trong text OCR rồi lấy số ở dòng gần đó. **11/12 ứng viên khớp ảnh; trường nợ phải trả VNM không tìm được ứng viên.** Số 18.740.931.850.130 được đọc và xác nhận từ ảnh, không phải giá trị mà bộ regex đã tự lấy thành công. Kết quả được giữ nguyên trong JSON, không chỉnh quy tắc sau khi xem đáp án rồi công bố lại là độ chính xác 100%.

Người chọn trang, viết parser và đối chiếu là cùng agent. Chỉ có hai báo cáo, trang được chọn thủ công, không đo thất bại khi tự tìm trang, không có holdout, không đo thời gian review. Chưa đủ suy rộng 11/12 sang dataset. Các dòng ngoài sáu chỉ tiêu vẫn có lỗi OCR, nên không tự suy mọi số trong bảng đều đúng.

Nên thử parser có tọa độ cột, mã dòng và từ điển nhãn nhiều phiên bản; giữ raw text/bounding box và cờ missing. Mã tổng tài sản quan sát giữa DHG FY2025 và VNM Q1/2026 khác nhau, nên không hard-code một mã cho mọi năm. Xem [thiết kế IT](04-thiet-ke-crawl-va-chuan-hoa.md).
