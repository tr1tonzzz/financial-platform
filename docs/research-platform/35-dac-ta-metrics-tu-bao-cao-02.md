# Chỉ tiêu và dữ liệu UC-1 — đối chiếu Báo cáo 2

Ngày lập: **11/10/2026**. Dùng cho [tuần 1](33-ke-hoach-chi-tiet-tuan-01.md), [tuần 2](34-ke-hoach-chi-tiet-tuan-02.md) và chuẩn bị UC-2. Đây là đặc tả triển khai, chưa phải kết quả ứng dụng đã chạy.

**Lưu và cung cấp dữ liệu theo kiến trúc web:** PostgreSQL lưu NUMERIC; Python dùng Decimal; API FastAPI trả số tiền dạng chuỗi/null; React hiển thị và xuất qua backend để giữ độ chính xác. Đổi stack không đổi định nghĩa sáu metrics hoặc tăng 54 targets. [Quyết định hiện hành](31-chot-pham-vi-va-stack-paddleocr.md).

## 1. Báo cáo đã xác định gì?

Nguồn tham chiếu: `Báo cáo 2.docx` do người thực hiện cung cấp. [Bản trích nội dung có SHA-256 và số khối](evidence/report-02-metrics-reference.json) ghi đường dẫn tệp gốc; khối 31 là bảng dữ liệu, khối 45–54 là thực nghiệm. Số khối là thứ tự phần tử trong nội dung Word, không phải số trang.

| Nội dung trong báo cáo | Cách sử dụng trong kế hoạch |
|---|---|
| Sáu số liệu nền: tổng LNST, CFO, tiền và tương đương tiền, tài sản, nợ phải trả, vốn chủ sở hữu | Giữ nguyên sáu trường lõi cho UC-1; không cần chọn lại financial metrics |
| Các dòng cầu nối CFO | Thu theo ca khi làm phân tích phân rã; chưa trích toàn bộ cho chín báo cáo ở tuần 1–2 |
| Dòng tiền chi cho chủ sở hữu | Lưu có dấu và nhãn gốc khi dùng ca đối chiếu tiền đã chi; khác DPS công bố |
| Thành phần thông báo cổ tức và năm lợi nhuận | UC-5; không lấy thông báo để điền vào dòng tiền chi trên BCLCTT |
| Nguồn, đơn vị, kỳ, phạm vi, duyệt và lịch sử | Phải xây cùng kho số liệu UC-1; không phải financial metrics mới |
| Tăng trưởng LNST, chênh lệch CFO, CFO/LNST | Kết quả tính từ số liệu đã duyệt; UC-2, không OCR thêm một dòng tỷ số |

**Điểm cần làm rõ khi báo cáo:** sáu ô đối chiếu ở thực nghiệm VNM là LNST/CFO/tiền chi cổ tức ở Q1/2026 và cột Q1/2025 đã phân loại lại. Đó là **ba chỉ tiêu × hai cột**; chưa phải sáu chỉ tiêu nền, chưa phải hai PDF độc lập, và là kết quả Tesseract được báo cáo, không phải Paddle. Dữ liệu quý này làm mẫu tích hợp, không thay bộ năm 2023–2025.

## 2. Từ điển sáu trường lõi

Mã dòng dưới đây chỉ là gợi ý tìm kiếm theo bố cục thông dụng; phải kiểm nhãn, header và cột thực tế. Không chọn số chỉ bằng mã dòng hoặc vị trí cố định.

| Mã trường | Nghĩa và mục đích đơn giản | Nơi tìm / gợi ý dòng | Loại kỳ và quy tắc chọn |
|---|---|---|---|
| `net_income_total` | Tổng lợi nhuận sau thuế; doanh nghiệp báo lãi hay lỗ trong năm | KQKD, “Lợi nhuận sau thuế thu nhập doanh nghiệp”, thường 60 | Dòng cả năm; tổng hợp nhất, không thay bằng LNST cổ đông công ty mẹ; có thể âm |
| `cfo` | Lưu chuyển tiền thuần từ hoạt động kinh doanh; hoạt động kinh doanh tạo hay dùng tiền | BCLCTT, thường 20 | Dòng cả năm, giữ dấu; không nhầm tiền trước thay đổi vốn lưu động với CFO cuối |
| `cash_equivalents` | Tiền và tương đương tiền tại cuối năm; bối cảnh lượng tiền đang có | Bảng cân đối, thường 110 | Số dư ngày cuối kỳ; không chỉ lấy dòng “Tiền” hoặc cộng trùng tổng và chi tiết |
| `total_assets` | Tổng tài sản; bối cảnh quy mô và mẫu số tỷ lệ | Bảng cân đối, thường 270 | Số dư cuối kỳ; không thay bằng tài sản ngắn hạn |
| `total_liabilities` | Tổng nợ phải trả; bối cảnh nguồn vốn từ nghĩa vụ phải trả | Bảng cân đối, thường 300 | Số dư cuối kỳ; không gọi là tổng nợ vay |
| `total_equity` | Tổng vốn chủ sở hữu; đối chiếu cân đối nguồn vốn | Bảng cân đối, thường 400 | Tổng vốn hợp nhất, gồm phần không kiểm soát khi báo cáo có; không lấy riêng vốn góp |

Tất cả lưu giá trị chuẩn hóa **VND**, nhưng giữ số và đơn vị nguyên bản. Hiển thị tỷ đồng là phép đổi phục vụ đọc, không thay số chính xác trong kho. Không áp quy tắc “mọi số âm là lỗi”: LNST, CFO và vốn có thể âm; trường hợp đáng kiểm được đưa sang duyệt có lý do.

**Ví dụ giả định:** PDF ghi đơn vị triệu đồng, CFO `(250)` → lưu `-250000000` VND; màn hình hiện `−0,250 tỷ đồng`. Dấu `—` chưa rõ ý nghĩa → để thiếu/mơ hồ; chỉ lưu 0 khi ngữ cảnh tài liệu xác nhận là 0.

## 3. Phần bổ sung thực sự cần thiết

Không bổ sung một loạt ROE, EPS, định giá vào hai tuần này. Cần bổ sung chi tiết dữ liệu để sáu trường dùng được:

| Bổ sung | Giải quyết điều gì? | Tác động công việc/phạm vi |
|---|---|---|
| Phân biệt số dư và số phát sinh; ngày cuối kỳ/khoảng kỳ | Không ghép tiền ngày 31/12 với CFO một quý như cùng một “năm” | Thêm metadata và kiểm tra; làm trong UC-1, không tăng 54 ô lõi |
| `column_role`, `reported_in_year`, `restatement_status` | Biết CFO 2024 lấy từ cột so sánh của báo cáo 2025 và có bị phân loại lại không | Thêm nguồn/cột/revision; tuần 2 |
| Phương pháp BCLCTT: trực tiếp/gián tiếp/chưa xác định | Chuẩn bị chọn ca cầu nối đúng bố cục | Metadata tài liệu, không yêu cầu trích các dòng cầu nối ngay |
| Định nghĩa và phiên bản quy tắc chuẩn hóa | Người dùng hiểu đúng “nợ phải trả” và kiểm lại phép đổi đơn vị | Từ điển + nguồn từng ô; tuần 1–2 |
| CAPEX, theo ca ở tuần 7 | Đọc CFO cùng nhu cầu đầu tư, như giới hạn đã nêu trong báo cáo | Dữ liệu điều kiện của kế hoạch G02 hiện có; không nâng thành trường lõi phải đủ ở chín báo cáo |

CAPEX cần xác định dòng chi mua sắm/xây dựng tài sản phù hợp, nhãn và phạm vi; giữ dòng gốc có dấu rồi tạo giá trị chi dương bằng quy tắc riêng. Không lấy toàn bộ dòng tiền đầu tư hoặc áp `abs()` cho mọi khoản. Dòng “cổ tức, lợi nhuận đã trả cho chủ sở hữu” có thể gộp khoản khác; chưa tách được thì dùng đúng nhãn khoản phân phối, không khẳng định là tiền cổ tức phổ thông.

**Quyết định phạm vi:** giữ manifest chín báo cáo/54 targets và SRS hiện hành. Tài liệu này làm rõ cách thực hiện, không thêm UC lớn hoặc nghĩa vụ trích toàn bộ BCTC. Doanh thu/ROE/EPS/thanh khoản chi tiết chỉ đưa vào sau khi chọn chức năng tương ứng và xác định nguồn, công sức, thay đổi SRS.

## 4. Hợp đồng dữ liệu cho một ô

| Nhóm | Trường cần có | Cách dùng |
|---|---|---|
| Định danh | `fact_id`, `ticker`, `metric_code`, `scope` | Chọn đúng doanh nghiệp/chỉ tiêu; scope chưa xác định không publish |
| Thời gian kinh tế | `fiscal_year`, `period_kind`, `period_start`, `period_end`, `as_of_date` | LNST/CFO dùng khoảng kỳ; số dư dùng ngày cuối kỳ; các trường không áp dụng để null |
| Nguồn tài liệu | `document_version_id`, `source_url`, `pdf_sha256`, `retrieved_at`, `published_at` | Ngày công bố chưa biết để null; ngày tải không thay ngày công bố |
| Vị trí | `pdf_page_index`, `printed_page_label`, `statement_type`, `row_label`, `row_code`, `column_label`, `column_role`, `bbox` | Index PDF từ 0, UI hiện trang PDF từ 1; nhãn trang in có thể khác; bbox null nếu chỉ định vị text |
| Giá trị | `raw_value`, `raw_unit`, `normalized_value_vnd`, `normalization_rule_version` | Decimal/integer; không float làm nguồn lưu tiền; missing có giá trị null và lý do |
| Ngữ cảnh phiên bản | `reported_in_year`, `restatement_status`, `revision_id` | Năm tài liệu khác năm của số; số gốc và số trình bày lại không ghi đè nhau |
| Xử lý | `extraction_method`, `engine_version`, `model_name`, `confidence`, `acquisition_mode`, `review_status`, `reason` | Phân biệt native text/Paddle/manual; confidence chỉ là thông tin OCR |

`acquisition_mode` mô tả cách lấy tài liệu (tự động/assisted), `extraction_method` mô tả cách lấy số; tải tự động không khiến số nhập tay thành trích tự động. Review lưu riêng người, thời điểm, số trước/sau và lý do. Một fact có thể tham chiếu nhiều lần duyệt; bảng chính chỉ đọc bản được duyệt đang được chọn.

**Ví dụ giả định:** CFO 2024 có trong PDF 2025, cột so sánh “2024 đã phân loại lại”: `fiscal_year=2024`, `reported_in_year=2025`, `column_role=comparative`, `restatement_status=reclassified`. Không tạo thêm một năm 2025 và không tự xóa CFO 2024 đã lưu từ PDF 2024. Khi chưa chọn được bản dùng hiện hành, hiển thị xung đột/chờ duyệt.

## 5. Những kết quả UC-2 được chuẩn bị, chưa tính trong UC-1

| Kết quả | Dữ liệu và quy tắc | Ví dụ giả định dễ hiểu |
|---|---|---|
| Chênh lệch LNST/CFO | Giá trị năm sau trừ năm trước; cùng scope/kỳ/đơn vị và phiên bản được chọn | CFO −20→40 tỷ: tăng 60 tỷ |
| Tăng trưởng LNST | `(NI_t−NI_t−1)/NI_t−1 × 100`; năm liền kề, nền dương và dữ liệu đã duyệt | 100→120 tỷ: tăng 20%; −20→40 thì giải thích chuyển lỗ sang lãi, không hiện “−300% tăng trưởng” |
| CFO/LNST | CFO chia tổng LNST khi LNST > 0 | 80/100=0,8 lần; CFO âm vẫn giữ kết quả âm |
| Tiền/tài sản | Tiền và tương đương tiền cuối kỳ / tài sản cùng ngày, assets > 0 | 50/500=10%; không suy đủ thanh khoản ngắn hạn |
| Nợ phải trả/tài sản | Tổng nợ phải trả / tài sản cùng ngày, assets > 0 | 300/500=60%; không đặt nhãn “nợ vay/tài sản” |
| Biểu đồ LNST–CFO | Chuỗi số đã duyệt, unit và nguồn; missing tạo khoảng trống | Nhìn năm lợi nhuận tăng nhưng CFO giảm để đọc thêm nguyên nhân |

Những tỷ số này cung cấp bối cảnh đọc tài chính; không kết luận cổ tức an toàn hoặc khuyến nghị mua/bán. DPS/năm lợi nhuận, tiền thực chi theo kỳ và basis cổ phiếu được quản lý riêng khi làm UC-5.

## 6. Dữ liệu tối thiểu qua hai tuần

- Tuần 1: một BCTC năm, sáu targets có giá trị đúng nguồn hoặc lý do thiếu; bảng/nguồn/CSV dùng được.
- Tuần 2: ưu tiên ba năm **một công ty đầu tiên** (18 targets); thử thêm một bố cục công ty thứ hai để phát hiện parser quá phụ thuộc mẫu. Không bắt buộc đủ chín PDF tuần 2.
- Chín báo cáo/54 targets vẫn là mục tiêu toàn pilot. Có 18 targets trong ledger không đồng nghĩa có 18 giá trị hợp lệ; báo số đã duyệt, missing và unresolved riêng.
- Cột so sánh có thể giúp đối chiếu và dựng chuỗi tạm thời nếu xác nhận đúng ngữ cảnh, nhưng không làm target PDF riêng của năm đó thành “đã thu”.
