# Khảo sát nhỏ nguồn và trích xuất đã thực hiện

Ngày kiểm tra: 03/10/2026. Mục đích: kiểm tra một đường tải và nhận diện lỗi ngữ nghĩa/bố cục trước pilot. **Đây chưa phải pilot 10 công ty, benchmark độc lập hay dataset nghiệm thu.**

**Bổ sung sau phép thử này, cùng ngày 03/10/2026:** [khảo sát dữ liệu 2025–2026](../research-recent-data/README.md) đã tải được HTML cổ tức ở host `vsdc.vn` và PDF HNX bằng curl Schannel có xác thực TLS. Kết quả bên dưới ở `vsd.vn` vẫn là kết quả của đường tải và môi trường đã thử trước đó; không còn nên dùng nó để kết luận chung rằng VSDC chưa có đường crawl local. Khảo sát mới còn kiểm tra 15 PDF và OCR, nhưng vẫn chưa đạt pilot 10 công ty.

## 1. Phương pháp và kết quả truy cập

Tìm nguồn chính thức bằng web; mở nội dung; thử tải bằng Python `urllib.request` với xác thực TLS; thử VSDC thêm bằng PowerShell `Invoke-WebRequest`; chỉ lưu file thành công. Không tắt xác thực TLS. Runtime Python 3.12.14 và pdfplumber 0.11.9 lấy từ bundle môi trường; đây là phiên bản thực chạy khảo sát, chưa phải dependency lock của dự án.

| Mẫu | Web | Tải local | Kết luận |
|---|---|---|---|
| [Vinamilk IFRS 2024](https://www.vinamilk.com.vn/bao-cao-thuong-nien/bao-cao/2024/doc/en/bctc-ifrs.pdf) | Fetch báo 403 | HTTP 200, PDF 133.468 bytes | Có file thật để thử đọc |
| [VNM VSDC 174349](https://www.vsd.vn/vi/ad1/174349) | Đọc được HTML | Lỗi xác thực TLS trong Python và kết nối SSL trong PowerShell | Đã đọc nghiệp vụ; chưa chứng minh crawler local |
| [VSH VSDC 174490](https://www.vsd.vn/vi/ad/174490) | Đọc được HTML | Lỗi TLS/SSL | Tương tự, cần xử lý đường truy cập hợp lệ trước crawl |
| FPT annual report 2024, URL trong sổ nguồn | Web open lỗi | HTTP 404 | Đường dẫn tìm kiếm có thể đã cũ |
| SDT VSDC 159639 | Chỉ search trả nội dung, open timeout | Lỗi TLS/SSL | Chưa dùng làm bằng chứng đã đọc trang gốc |

Không suy luận từ một lần tải thành công rằng site có API ổn định; cũng không coi lỗi TLS của môi trường này là nguồn vĩnh viễn không dùng được.

## 2. Hồ sơ PDF Vinamilk

- SHA-256: `aeb34a799f59755a211df3a295436685e9a4d5e1009237ea949e3fa2fc2b3ee3`.
- 3 trang PDF, mỗi trang là một spread hai trang in: 182–183, 184–185, 186–187.
- Phạm vi: hợp nhất; cơ sở ghi trên trang: IFRS; kỳ năm kết thúc 31/12/2024.
- Chưa có báo cáo kiểm toán trong file ba trang này; chưa xác minh ngày công bố ban đầu.
- Có text. `pdfplumber` thấy 2.150 / 1.772 / 2.749 ký tự ở ba trang; `find_tables()` mặc định trả 0 bảng mỗi trang.

Đã render cả ba trang bằng Poppler và xem hình. Trang dòng tiền vẫn mang tiêu đề trình bày về profit/loss, dù nội dung có operating/investing/financing cash flows. Đây là lỗi hoặc đặc điểm tiêu đề trong nguồn; parser cần đối chiếu nội dung bảng, giữ nhãn gốc và gắn cờ, không chỉ dựa vào tiêu đề.

## 3. Sáu giá trị đối chiếu

Giá trị dưới đây là **triệu VND**, cột 2024, IFRS hợp nhất. Sau khi tách nửa trang bằng `crop`, tìm dòng theo nhãn và parse số cột đầu, sáu ứng viên khớp với số đọc từ hình. Người tạo parser đồng thời đối chiếu, nên chưa có người chấm độc lập.

| Chỉ tiêu | Giá trị | Trang PDF / trang in | Vùng |
|---|---:|---|---|
| Tiền và tương đương tiền | 2.225.944 | 1 / 182 | Trái |
| Tổng tài sản | 56.993.245 | 1 / 182 | Trái |
| Nợ phải trả | 19.827.315 | 1 / 183 | Phải |
| Vốn chủ sở hữu tổng | 37.165.930 | 1 / 183 | Phải |
| LNST toàn nhóm | 8.686.245 | 2 / 184 | Trái |
| CFO | 9.770.587 | 3 / 186 | Trái |

Kiểm tra số học: `56.993.245 - 19.827.315 - 37.165.930 = 0` triệu VND. Đây là kiểm tra nhất quán, không chứng minh mọi fact đều đúng.

File nguồn và trace lưu local tại `data-sets/research-evidence/2026-10-03/`: `vnm-ifrs-2024.pdf`, `download-manifest.json`, `pdf-inspection.json`, `six-metric-probe.json`, ba text trang và ba PNG. Thư mục `data-sets/` đang được `.gitignore` loại; hồ sơ MD này giữ URL, hash, cách làm và kết quả để người đọc có thể tải lại. Raw không đi kèm khi chỉ clone repository.

## 4. Hai quan sát nghiệp vụ VSDC

**VNM:** thông báo cập nhật 30/08/2024, quyền 25/09/2024, lịch thanh toán 24/10/2024. Mệnh giá 10.000 đồng; tổng 24,5% = 2.450 đồng/cổ phiếu gồm 950 đồng cho năm 2023 và 1.500 đồng tạm ứng 2024. Một lịch thanh toán cần hai thành phần phân bổ profit_year. [Thông báo gốc](https://www.vsd.vn/vi/ad1/174349).

**VSH:** thông báo cập nhật 05/09/2024 sửa lịch thanh toán đợt 2 từ 03/10/2024 về 19/09/2024, tham chiếu quyền 29/12/2023. Đổi lịch theo hướng sớm hơn vẫn là amendment, không phải một cổ tức mới hay mặc nhiên là trì hoãn. [Thông báo gốc](https://www.vsd.vn/vi/ad/174490).

Hai trang chỉ xác nhận nội dung lịch công bố. Không dùng để gán `confirmed_paid` hoặc nhãn maintained/omitted.

## 5. Hệ quả cho thiết kế và nghiên cứu

1. Thêm `accounting_basis` vào metadata đề xuất và khóa tương thích phân tích; không ghép IFRS với VAS vì cùng ticker/năm.
2. Lưu cả trang PDF, trang in và vùng bằng chứng; parser trên spread cần tách vùng.
3. Benchmark ít nhất hai chiến lược text/coordinate; có text không bảo đảm table extraction mặc định hoạt động.
4. Sự kiện có bảng thành phần phân bổ và lịch sử amendment; giữ tổng lịch riêng để tránh cộng hai lần.
5. Kiểm tra đường crawl VSDC từ môi trường triển khai và chuỗi CA; chưa chọn nguồn chính chỉ từ kết quả web đọc được.

Các mục trên là đề xuất đào sâu SDD, chưa chỉnh schema phần mềm. Bước tiếp theo của nghiên cứu là mẫu nhiều công ty với BCTC năm kiểm toán đúng cohort.
