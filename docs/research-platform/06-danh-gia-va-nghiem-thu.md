# Protocol đánh giá và nghiệm thu

## Nghiệm thu bổ sung theo SRS v3.1

Giữ 73 yêu cầu/31 TC nền; thêm E01–E10 và P01–P11 tại mục 15 SRS, tổng 83 mã/42 tình huống dự kiến. E05/E10 chỉ vào mẫu số khi được kích hoạt. Tối thiểu một ca thật có context, reviewed leaves, residual/tolerance/completeness, nguồn mở được và replay. Kiểm double-count subtotal, dòng thiếu, sai dấu/đơn vị/scope, phương pháp trực tiếp/unknown, LNST khác LNTT, cổ tức đa năm và snapshot sau đổi mapping. [Input/expected P01–P11](../research-profit-cash-dividend/07-ke-hoach-thi-nghiem-va-kiem-thu.md).

Freeze gold theo dòng trước đo, tách lineage development/holdout. DHG đã dùng để thiết kế không là holdout độc lập. Báo trước/sau review, phút nhập/sửa và hình thức tự kiểm riêng; không gọi B2 là accuracy tự động. Quét 100% kết quả xuất bản có operands/source không có nghĩa trích được 100% targets. Nếu chưa có mẫu độc lập thì báo số đếm/case và giới hạn. Trạng thái ban đầu mọi test mới là not_run.

Thiết kế hiện hành ngày 03/10/2026, chưa có kết quả nghiệm thu. Đánh giá thu thập, trích/ghép dữ liệu và ứng dụng; không chấm predictor trong project.

## 1 Expected và holdout

Freeze issuer/year/scope, sáu financial targets/report, các fields/events/components gold và cửa sổ nguồn đã rà. Bốn notices mẫu và PDF dùng chỉnh parser thuộc development. Holdout dùng tài liệu/notices khác, tránh cùng notice route, bản dịch hoặc phiên bản gần giống ở hai tập. Gold có người khác kiểm tra nếu có; tự chấm phải nói rõ.

Scope mục tiêu 15–24 BCTC năm; gợi ý 5–8 tài liệu holdout ×6 targets =30–48 ô, cộng event holdout theo nguồn/kỳ đã chọn. Cỡ mẫu chốt sau pilot, không bảo đảm lực thống kê. Nếu ít hơn, báo mẫu nhỏ. Không bỏ target missing khỏi mẫu số.

## 2 Metrics riêng

| Lớp | Số đo |
|---|---|
| Discovery/selection | Expected đã công bố, coverage và precision đúng loại/kỳ/scope sau kiểm tra |
| Download/update | PDF/HTML hợp lệ, policy-skip/errors, bytes và phiên bản trước/sau/304 |
| Financial extraction | Joint metric/value/unit/period/scope, missing, lỗi trước/sau review |
| Events/components | Ticker/kind/DPS/profit_year/dates đúng joint, precision/recall theo gold |
| Lifecycle/aggregate | Trùng/sửa/hủy đúng, annual complete/partial/unknown và share comparability |
| Effort | Giây các bước, phút review tài liệu/notice, công sức sửa adapter |
| App | Truy ngược nguồn/operands, export tái lập, failure hiển thị rõ |

B0 text-only, B1 text + OCR fallback + parser cột, B2 B1 + validation/review. Không gọi B2 là accuracy tự động. Event parser có baseline một năm/notice để thấy lợi ích components nhưng không xuất baseline sai như dataset chính.

Financial VND integer dùng exact match; nguồn làm tròn thì tolerance công bố trước. Coverage có cả source failures và unknown. Báo tỷ lệ cùng số đếm/cỡ mẫu. Khi nói tiết kiệm công sức, cần đo nhập tay tương đương và giới hạn người đã nhớ số.

## 3 Tests nghiệp vụ

**Làm rõ sau nghiên cứu lần hai ngày 04/10/2026:** kiểm tra hủy ngày đăng ký/thông báo quyền không thành `declared_zero` hoặc hủy mọi quyết định cổ tức; bản thay thế chưa rõ giữ coverage partial/unknown. Nội dung hành chính/HTML sidebar thay không thêm DPS; sửa lịch giữ mức, sửa mức thay component có hiệu lực. Với cân đối tài sản–nợ phải trả–VCSH, chỉ kiểm tra cùng ngày/scope/unit, xét tolerance làm tròn đã chốt; thiếu operand trả không kiểm tra được, không tự suy pass. Đo precision/recall issues và công sức review riêng khỏi accuracy trích số. [Nguồn ca thật và quyết định](20-nghien-cuu-lan-hai-va-chot-de-tai.md).

Normalize: dấu ngoặc âm, nghìn/triệu, gạch/ô trống. Period/scope: YTD vs riêng quý, hợp nhất/riêng, số so sánh. Event: notice hai năm, hai route, hai nguồn cùng đợt, hai đợt cùng số; sửa lịch không thêm DPS; sửa mức/hủy giữ lịch sử; thiếu notice không là 0; share basis chưa rõ chặn tổng/growth. JOIN không nhân bản facts theo số components.

Store: keys/transaction/audit/rollback, chạy lại không trùng và snapshot cũ còn nguyên khi bản mới tới. Collector: HTML giả PDF, timeout/404/policy/redirect/corrupt cache. E2E: BCTC + notice thật tới review/aggregate/chart/export và mở nguồn ngược.

## 4 Nghiệm thu và bằng chứng trước

100% số xuất bản có source hash/version/locator/kỳ/unit/scope, active components/coverage. Ba case có dữ liệu và giới hạn; ERD/architecture, test/benchmark, README chạy, báo cáo Word/slide và demo tự giải thích/sửa nhỏ. Một luồng discovery BCTC và một luồng discovery event phải có log; manual fallback đếm riêng.

Crawler đã có 8 PDF/4 issuer/7 HTML và 8 ×304, 13 test offline; đây là development, không accuracy thị trường hoặc dataset ghép hoàn chỉnh. [Bằng chứng](../research-crawl-methods/crawl-evidence.json) không đổi số sau đổi scope. Numeric OCR cũ 11/12 chỉ mẫu sáu trường, không independent gold.

Tương quan/case không được nghiệm thu như mô hình dự đoán. Rubric trường chưa có nên phải đối chiếu với thầy, đặc biệt yêu cầu AI nếu thật sự bắt buộc.

## 5 Đối chiếu bài toán người dùng với nghiệm thu SRS v2.1

[SRS v2.1](02-de-tai-va-srs.md) cụ thể hóa PF01–PF09 bằng P01–P06, AN01–AN07 và US01–US08. Khi nghiệm thu, ghi input/snapshot, expected/actual, pass/fail và nguồn bằng chứng cho từng nhóm dưới đây; chưa tick hoàn thành chỉ vì đã có tài liệu.

| Nhóm | Yêu cầu đối chiếu | Bằng chứng cần có |
|---|---|---|
| Dữ liệu/coverage | US01, US04; P01, P04 | Chọn doanh nghiệp/giai đoạn; bảng đủ/thiếu/chưa duyệt riêng BCTC và cổ tức; scope/kỳ/đơn vị/basis sai phải hiện lý do |
| Phân tích cụ thể | US02, US04, US08; AN01–AN03, AN06–AN07 | Tính tay đối chiếu mức/chênh lệch/% và ratio; bộ lọc khác chiều; scatter/hệ số kèm n/excluded; biến hằng hoặc <3 cặp không tính hệ số |
| Ghép và vòng đời cổ tức | US03–US04; AN04–AN05 | Notice hai năm, đăng trùng, sửa lịch/mức/hủy; coverage partial và basis chưa rõ chặn annual/growth; lịch đã qua không tự gán paid |
| Review/provenance | US05–US06; P03–P05 | Candidate chưa duyệt không xuất thành fact; audit trước–sau/lý do; 100% giá trị xuất bản mở được operands/components và nguồn/locator |
| Tái lập và báo cáo | US07–US08; P05–P06 | Export kèm manifest/config/coverage; tái tính snapshot cũ khớp sau cập nhật; ba case thật có bằng chứng và giới hạn |

Fixture giả định ở mục 3.3 SRS kiểm tra phép tính và hành vi. Giữ fixture tách khỏi gold/holdout và ba case dữ liệu thật. Nếu chưa tìm được một kiểu case trong nguồn thật, ghi rõ rồi chọn case khác có giá trị kiểm chứng; không đổi số giả định thành kết quả thu thập.

Đánh giá lợi ích P01 bằng thời gian/công sức gom tài liệu, nhập tay và kiểm chứng trên cùng tập đầu vào so với pipeline gồm cả review. Với người dùng thử nếu có, giao câu hỏi cụ thể: nhận ra năm LNST tăng nhưng CFO giảm, tìm tổng DPS đúng và mở nguồn, phân biệt thiếu dữ liệu với 0. Ghi tỷ lệ hoàn thành, lỗi hiểu kết quả, thời gian, số người và giới hạn tự đánh giá. Đây là protocol đề xuất, chưa có kết quả hoặc cam kết tiết kiệm bao nhiêu phần trăm.

GUS01 thuộc hướng tốt nghiệp, không đưa vào mẫu số nghiệm thu chức năng của project. Việc phê duyệt đề tài vẫn cần đối chiếu yêu cầu giảng viên.
