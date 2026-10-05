# 04 — Nguồn dữ liệu, chuẩn hóa và chất lượng

## 1. Những gì đã có và chưa có

Theo [hồ sơ crawler](../research-crawl-methods/README.md), thử nghiệm trước thu 8 PDF của4 doanh nghiệp, tổng423 trang; chỉ96 trang đầu được thử text. Đây là kết quả cũ, không chạy lại trong lượt này. Theo [ledger OCR](../research-recent-data/ocr-core-check.json), bộ thử chọn12 targets của2 báo cáo có11 candidate khớp đối chiếu ảnh; chính người làm parser cũng chọn/duyệt mẫu. Không dùng 11/12 làm accuracy độc lập.

Trong lượt này đã đọc lại hai trang ảnh DHG và nội dung chính hai thông báo VNM trên web; đã kiểm tra được ca cầu nối ở cấp tài liệu. Chưa có chứng cứ đủ BCTC 2023–2025 và đầy đủ cổ tức cho3 doanh nghiệp. Không ngoại suy từ một ca thành khả năng tự động hóa hàng loạt.

## 2. Kế hoạch nguồn

| Nội dung | Nguồn ưu tiên | Nguồn hỗ trợ | Điều kiện |
|---|---|---|---|
| BCTC năm kiểm toán | IR doanh nghiệp và file chính thức | Hồ sơ công bố của sở | Xác nhận kỳ, scope, assurance, đơn vị, bản sửa |
| Nghị quyết phân phối | ĐHĐCĐ/HĐQT, IR | Công bố của sở | Kế hoạch/phê duyệt không tự là một đợt đã trả |
| Thực hiện quyền | VSDC, IR | Công bố của sở | Phân biệt notice, event, revision, component |
| Giải thích lợi nhuận/CFO | BCLCTT, thuyết minh, giải trình | Báo cáo thường niên | Tách phần số học và giải thích của ban điều hành |
| Số cổ phiếu và basis | Hồ sơ thực hiện quyền/corporate actions | Thuyết minh vốn/EPS | Không dùng một số cuối kỳ cho mọi đợt |

Ứng viên pilot: DHG cho cầu nối đã xem được; VNM cho sự kiện nhiều năm; doanh nghiệp thứ ba chọn sau kiểm tra nguồn đủ ba năm, ưu tiên đặc điểm khác. HPG/VHC là ứng viên từ khảo sát trước, không xem đã đạt pilot. Giữ scope nhất quán theo doanh nghiệp; không lấy riêng ở năm thiếu hợp nhất rồi nối thẳng.

Khóa mốc khảo sát tại04/10/2026; rà thông báo từ đầu2023 đến mốc này và bổ sung văn bản sớm hơn nếu cần quyết định/basis. Cổ tức FY2025 có thể xuất hiện trong2026. Không cam kết rằng tới mốc này mọi quyết định FY2025 đã khép. BCTC cả năm 2026 chưa là đầu vào năm đã hoàn tất đối với doanh nghiệp theo năm dương lịch.

## 3. Pipeline chuẩn hóa

1. Lập danh mục issuer/security/period/scope và expected documents trước thu thập.
2. Discovery từ trang danh mục; ghi route, phân trang, bộ lọc, giới hạn và chính sách nguồn. URL file nhập tay phải mang nhãn assisted.
3. Lưu raw bytes, URL, ngày truy xuất, hash và metadata công bố; URL không thay content identity.
4. Chọn PDF text hoặc OCR theo trang. Giữ ảnh/bbox và candidate, không ghi đè raw. Trang chính và cột so sánh có context riêng.
5. Chuẩn hóa dấu, phân cách, đơn vị về VND với số nguyên/Decimal; lưu raw token và unit. Gạch trống/không đọc được không thành0.
6. Map metric theo nhãn, mã dòng, loại báo cáo và chế độ; không dùng mã20 chung cho mọi bảng.
7. Kiểm tra công thức, kỳ, scope, provenance; lỗi blocking vào review. Confidence cao không thay reviewer cho context mơ hồ.
8. Duyệt facts và các relations sự kiện; tính aggregate chỉ từ versions đã duyệt. Freeze snapshot trước phân tích/đánh giá.

[TT99/2025/TT-BTC có hiệu lực01/01/2026](https://congbao.chinhphu.vn/van-ban/thong-tu-so-99-2025-tt-btc-46529/59637.htm). Khi mở sang2026, dùng `accounting_regime`, `template_version`, `effective_period` trong mapping. Chưa đọc toàn bộ phụ lục nên không khẳng định mọi mã dòng thay thế tương ứng ra sao. Ca DHG2025 đã xem có mẫu theo TT200 in trên báo cáo.

## 4. Hợp đồng grain và ghép

Financial fact: `issuer + report_scope + period_start/end + metric + report_version + column_context`. Reviewed selection xác định đúng một fact active cho mỗi khóa ngữ nghĩa trong một snapshot; các revisions vẫn tồn tại.

Bridge line: `report_version + period + scope + line_id`, phân loại leaf/subtotal/total. Một dòng có nhiều nguồn chứng minh nhưng chỉ một operand trong phép cộng.

Dividend component: `security + event_id + component_id + revision`; profit_year có thể null. Hai component trong một notice không phải hai notices. Hai URL nói về cùng quyền không được cộng hai lần. Hai đợt khác nhau có cùng DPS/ngày không tự gộp.

Trước join: aggregate components hợp lệ thành một dòng `security + profit_year + basis + snapshot`. Sau đó join với **một** financial selection cùng issuer/FY. So số dòng firm-year trước–sau; nở dòng phải báo lỗi. Cần bảng mapping security–issuer có hiệu lực, tránh dựa duy nhất vào ticker.

## 5. Rủi ro chất lượng và cách xử lý

| Rủi ro | Bằng chứng/trạng thái | Tác động | Kiểm soát |
|---|---|---|---|
| Ghép theo năm thông báo | VNM notice2025 gồm profit_year2024 và2025 | Cao: sai kết quả cổ tức năm | Split components theo nội dung có nguồn |
| Cộng subtotal và children | DHG có dòng 08 và các dòng 01–06 | Cao: CFO tính bị nhân phần lợi nhuận | Kiểu line_role; cây phép tính |
| Thực chi khác năm lợi nhuận | Ngữ nghĩa BCLCTT và notice khác nhau | Cao: payout sai | Tách dataset và nhãn phân tích |
| Thiếu lịch sử sự kiện | Seed hiện có4 notices/2 issuers | Cao: gán zero hoặc tổng năm thiếu | Coverage ledger, annual=null khi partial |
| OCR sai dấu/cột | Hồ sơ cũ đã có field không trích được | Cao: đảo kết luận | Review ảnh, expected targets không bỏ missing |
| LNST mẹ/CFO tập đoàn | Rủi ro thiết kế, chưa audit toàn mẫu | Cao: tỷ số khác phạm vi | Khóa scope/metric, chặn phép tính |
| Selection bias | Pilot chọn có chủ đích từ nguồn truy cập được | Cao với suy rộng thị trường | Chỉ mô tả mẫu, ghi lý do chọn/loại |
| Thay mẫu kế toán | Metadata TT99, ca DHG mẫu TT200 | Trung bình trong2023–25, tăng khi mở2026 | Version mapping và holdout template mới |
| Publication thiếu timezone | Ledger notices giữ unknown | Cao nếu point-in-time | Không suy timestamp; date-only có chính sách cutoff |

Đây là rà soát rủi ro phục vụ thiết kế và kiểm tra nguồn chọn lọc, không phải kết quả audit toàn database. Mức độ tin cậy cao cho ca VNM/DHG đã đọc; coverage toàn mẫu và tỷ lệ lỗi thực tế còn chưa đo.

## 6. Gate công bố dữ liệu

Published facts phải có raw/version/locator/review. Cầu nối có thiếu line vẫn có thể hiển thị phần quan sát nhưng nhãn partial/not_reconciled rõ; không gọi số thiếu là nguyên nhân. Annual DPS chỉ đầy đủ trong tập nguồn/cửa sổ/as_of đã công bố, có bằng chứng kiểm tra, không là khẳng định tuyệt đối mọi thông báo trên Internet.

Giữ `observed_value`, `complete_value`, `status`, `reason`, `as_of` tách rời. Missing không bị loại âm thầm khỏi mẫu số chất lượng. Export phải giữ null và lý do, không xuất biểu đồ rồi đánh mất context.
