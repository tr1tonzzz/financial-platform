# Phụ lục báo cáo 1 — Ví dụ phân tích sơ bộ DHG

Ngày đối chiếu lại: **05/10/2026**. Phụ lục phục vụ [báo cáo 1](bao-cao-01.md), giữ số gốc để kiểm tra các bảng minh họa. Dữ liệu chép thủ công từ BCTC thật, chưa là gold kiểm độc lập. [Thử nghiệm công cụ](thu-nghiem-cong-cu.md) sau đó tái tạo được bốn số LNST/CFO bằng OCR/parser nhỏ; cầu nối và khoản chi chủ sở hữu trong phụ lục này vẫn dựa trên số đọc thủ công.

## 1. Tài liệu và vị trí nguồn

- Doanh nghiệp: Công ty Cổ phần Dược Hậu Giang, mã DHG.
- Tài liệu: BCTC cho năm tài chính kết thúc ngày 31/12/2025, bản kiểm toán được [doanh nghiệp công bố ngày 21/03/2026](https://dhgpharma.com.vn/vi/co-dong/10533-bao-cao-tai-chinh-kiem-toan-nam-2025-va-giai-trinh-chenh-lech).
- [BCTC PDF](https://dhgpharma.com.vn/sites/default/files/2026-03/DHG-Audited-FS-2025-VN.pdf#page=10): trang PDF 10/trang in 8 là B02-DN; trang PDF 11/trang in 9 là B03-DN.
- Đơn vị: VND. Cột “Năm nay” là 2025; “Năm trước” là số 2024 được trình bày trong cùng bản báo cáo 2025.
- Phạm vi giữ đúng tên báo cáo Công ty Cổ phần Dược Hậu Giang; chưa tự gán nhãn hợp nhất. Số 2024 không được coi là thông tin đã biết tại cuối năm 2024 trong nghiên cứu dự báo.
- Dữ liệu đối chiếu đã có trong repo: [bản chép VND và các dòng cầu nối](../../../research-profit-cash-dividend/evidence/case-dhg-2025.json). Lượt này mở lại ảnh trang nguồn và tính lại từ số VND.

## 2. Các số gốc dùng trong ví dụ

| Chỉ tiêu | Năm 2024 — cột so sánh, VND | Năm 2025, VND | Vị trí |
|---|---:|---:|---|
| LNTT | 904.484.566.816 | 986.599.267.177 | B02-DN mã 50; B03-DN mã 01 |
| LNST | 778.920.119.960 | 852.354.107.582 | B02-DN mã 60 |
| CFO | 1.317.583.405.328 | 1.212.967.705.385 | B03-DN mã 20 |
| Cổ tức, lợi nhuận đã trả cho chủ sở hữu — số có dấu | −980.595.532.500 | −1.307.460.710.000 | B03-DN mã 36 |

Dấu âm của dòng 36 biểu thị khoản chi. Khi tính tỷ số với độ lớn khoản chi, sử dụng trị tuyệt đối và giữ đúng nhãn. Dòng này chưa phải mức DPS hay tổng cổ tức công bố thuộc năm lợi nhuận 2025.

## 3. Phép tính và kết quả

| Phép tính | Cách tính từ VND gốc | Kết quả làm tròn |
|---|---|---:|
| ΔLNST | 852.354.107.582 − 778.920.119.960 | +73,434 tỷ đồng |
| Tăng trưởng LNST | (852.354.107.582 / 778.920.119.960 − 1) × 100% | +9,43% |
| ΔCFO | 1.212.967.705.385 − 1.317.583.405.328 | −104,616 tỷ đồng |
| Tăng trưởng CFO | (1.212.967.705.385 / 1.317.583.405.328 − 1) × 100% | −7,94% |
| CFO/LNST 2024 | 1.317.583.405.328 / 778.920.119.960 | 1,692 lần |
| CFO/LNST 2025 | 1.212.967.705.385 / 852.354.107.582 | 1,423 lần |
| Chênh lệch CFO/LNST | Tỷ số 2025 − tỷ số 2024, tính trước làm tròn | −0,268 lần |
| CFO/độ lớn chi cho chủ sở hữu 2025 | 1.212.967.705.385 / 1.307.460.710.000 | 0,928 lần |

Quy đổi tỷ đồng bằng `VND / 1.000.000.000`. Báo cáo dùng dấu chấm phân tách hàng nghìn và dấu phẩy thập phân. Chênh lệch tính từ số gốc nên đôi khi khác kết quả trừ hai tỷ số đã làm tròn trên màn hình.

## 4. Cầu nối theo nhóm và kiểm tra tổng

Nhóm được lập từ các dòng có dấu trong B03-DN. Dòng 08 là tổng trung gian trước thay đổi vốn lưu động, chỉ dùng đối chiếu; không cộng nó thêm lần nữa cùng điểm đầu và các dòng 02–06.

| Nhóm | Các mã dòng | 2024, VND | 2025, VND |
|---|---|---:|---:|
| LNTT — điểm đầu | 01 | 904.484.566.816 | 986.599.267.177 |
| Điều chỉnh trước vốn lưu động | 02, 03, 04, 05, 06 | 60.778.871.370 | 64.553.708.172 |
| Thay đổi vốn lưu động | 09, 10, 11, 12 | 517.633.154.221 | 344.523.224.177 |
| Lãi vay, thuế và chi khác HĐKD | 14, 15, 17 | −165.313.187.079 | −182.708.494.141 |
| **Tổng CFO tính** | Cộng bốn nhóm trên | **1.317.583.405.328** | **1.212.967.705.385** |
| **CFO báo cáo** | 20 | **1.317.583.405.328** | **1.212.967.705.385** |
| **Residual** | CFO báo cáo − CFO tính | **0** | **0** |

Kiểm tổng theo biến động: `82.114.700.361 + 3.774.836.802 − 173.109.930.044 − 17.395.307.062 = −104.615.699.943 VND`, khớp ΔCFO.

Nhận xét sơ bộ: nhóm thay đổi vốn lưu động có đóng góp âm lớn nhất trong bốn nhóm đối với ΔCFO. Đây là mô tả phân rã số học, chưa xác định nguyên nhân vận hành cụ thể. Residual bằng 0 cho biết phép cộng các dòng được chọn khớp số báo cáo; riêng kết quả này không chứng minh trích dữ liệu đầy đủ/đúng context trên mọi tài liệu.

## 5. Giới hạn sử dụng

Ví dụ chỉ có một doanh nghiệp và hai cột năm từ một phiên bản báo cáo. Nó phù hợp để minh họa bảng phân tích và cầu nối, chưa dùng suy quan hệ thống kê hoặc nhân quả giữa lợi nhuận, CFO và cổ tức.

Chưa rà đầy đủ các thông báo DHG để tính DPS theo năm lợi nhuận. Không ghép thông báo VNM trong phần bối cảnh của báo cáo với CFO của DHG. Không suy khoản chi chủ sở hữu năm 2025 là cổ tức từ lợi nhuận 2025, hoặc CFO thấp hơn khoản chi đó là mất khả năng chi trả.
