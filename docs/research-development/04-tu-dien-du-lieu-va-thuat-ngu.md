# Từ điển dữ liệu và thuật ngữ dùng chung

Ngày: 03/10/2026. Quy tắc đề xuất chi tiết hóa [SDD](../initial-docs/SDD-FDP-01.md); không mô tả database đã triển khai.

## 1. Đơn vị quan sát và thời điểm

| Thuật ngữ/trường | Ý nghĩa và kiểm tra bắt buộc |
|---|---|
| `company_id` | Khóa doanh nghiệp ổn định; ticker có lịch sử hiệu lực |
| `firm_year` | Doanh nghiệp–năm tài chính; dành cho mô tả, không tự đồng nghĩa mẫu dự báo |
| `period_start`, `period_end` | Kỳ của dòng tiền/lợi nhuận; số dư tài sản/nợ tại period_end |
| `report_scope` | consolidated/separate; giữ tách biệt |
| `accounting_basis` | VAS/IFRS/other/unknown theo nguồn; bổ sung đề xuất từ khảo sát |
| `audit_status` | Có bằng chứng ý kiến kiểm toán, chưa rõ, chưa kiểm toán; chữ “annual” không chứng minh đã kiểm toán |
| `published_at` | Thời điểm công bố tài liệu xác minh được; khác ngày ký/kiểm toán và ngày tải |
| `available_at` | Thời điểm fact/version khả dụng công khai để mô phỏng dự báo |
| `retrieved_at` | Thời điểm hệ thống tải, lưu timezone |
| `cutoff_at` | Thời điểm chốt thông tin của một quan sát dự báo |
| `snapshot_at` | Mốc chốt dataset và đánh giá độ khép của outcome |

Lưu timestamp theo UTC và độ chính xác nguồn; hiển thị theo Asia/Saigon. Nguồn chỉ có ngày thì không tự bịa giờ giao dịch. Ngày audit không thay ngày khả dụng công khai.

## 2. Sáu facts lõi

| Code đề xuất | Khái niệm | Đơn vị chuẩn | Loại |
|---|---|---|---|
| `net_income_total` | LNST toàn nhóm nếu hợp nhất; LNST doanh nghiệp nếu riêng | VND | Flow năm |
| `cfo` | Lưu chuyển tiền thuần từ hoạt động kinh doanh, sau điều chỉnh nguồn | VND | Flow năm |
| `cash_equivalents` | Tiền và tương đương tiền; không cộng mọi tiền gửi/đầu tư | VND | Stock cuối kỳ |
| `total_assets` | Tổng tài sản | VND | Stock cuối kỳ |
| `total_liabilities` | Tổng nợ phải trả, bao gồm khoản không phải nợ vay | VND | Stock cuối kỳ |
| `total_equity` | Tổng vốn chủ sở hữu tương thích với tổng tài sản/nợ | VND | Stock cuối kỳ |

Mỗi fact có `raw_value`, `raw_unit`, `unit_multiplier`, `value_vnd`, nhãn gốc, trang/vùng, hash file, parser/mapping version, trạng thái review. Số tiền dùng Decimal/NUMERIC; ví dụ 1.250 triệu VND → 1.250.000.000 VND. Tách tiền mặt total khỏi các khoản dùng kỳ hạn dài hoặc chịu hạn chế theo thuyết minh.

## 3. Trạng thái thiếu và lỗi

| Trạng thái | Ví dụ | Xử lý |
|---|---|---|
| `not_disclosed` | Không có chỉ tiêu trong tài liệu đã rà | Missing có lý do |
| `source_missing` | Chưa tìm/tải được báo cáo | Missing, không phải 0 |
| `parse_failed` | Có nguồn nhưng đọc bảng thất bại | Review |
| `ambiguous` | Hai ứng viên khác nhau, thiếu đơn vị | Chặn ratio/nhãn liên quan |
| `not_applicable` | CFO/LNST khi LNST không dương | Trạng thái chỉ số, không phải fact 0 |
| `censored` | Outcome 12 tháng chưa khép | Không dùng train/test nhãn cuối |
| `unknown` | Cửa sổ khép nhưng bằng chứng cổ tức thiếu | Không gán omitted |

Không gộp “không áp dụng”, “thiếu” và “đã xác minh bằng 0”.

## 4. Sự kiện cổ tức

`event_id`: một quyền/đợt kinh tế; `event_version_id`: phiên bản lịch; `component_id`: phần DPS cho từng năm lợi nhuận; `dividend_type`: tiền/cổ phiếu/khác. Lưu `source_document_id`, `announced_at`, `record_date`, `ex_date` nếu nguồn xác minh, `scheduled_payment_date`, `confirmed_payment_date`, `cash_dps`, `profit_year`, `claim_type` và bằng chứng.

Phân biệt thời điểm thông báo quyền với lần công bố đầu tiên của doanh nghiệp. Nếu chưa tìm lần đầu, đặt `announcement_origin=vsdc_notice`, không tự coi là ngày thị trường biết đầu tiên. `scheduled` và `confirmed_paid` là hai mức bằng chứng khác nhau.

## 5. Công thức và domain

| Chỉ số | Công thức | Điều kiện |
|---|---|---|
| Chuyển hóa lợi nhuận | CFO/LNST | LNST > 0; xem riêng khi gần 0 |
| Tạo tiền so với tài sản cuối kỳ | CFO/A_end | A_end > 0; ghi đây là mẫu số cuối kỳ |
| Nợ phải trả/tài sản | L/A_end | A_end > 0 |
| Nợ phải trả/vốn | L/E | E > 0 |
| Tiền/nợ phải trả | Cash/L | L > 0; không gọi cash ratio chuẩn |
| Tiền/tài sản | Cash/A_end | A_end > 0 |
| DPS tiền | rate × nominal_value | rate dạng thập phân, mệnh giá xác minh |
| Mức giảm DPS | 1 − future_dps/past_dps | past_dps > 0, cùng cơ sở cổ phiếu và loại bằng chứng |
| Payout trên EPS | DPS/EPS | EPS > 0; cùng năm lợi nhuận, cơ sở cổ phiếu và phạm vi |
| Coverage tiền | CFO/cash_dividends_paid | Mẫu số > 0, cùng kỳ/phạm vi, bằng chứng thực trả |

Chi tiết FCFE, cash gap và điều kiện diễn giải ở [tài chính I2](i2-dong-tien-co-tuc/02-kien-thuc-tai-chinh.md). Các ngưỡng cảnh báo ở đề cương là giả định nghiên cứu.

## 6. Từ điển phiên bản nghiên cứu

`parser_version`, `mapping_version`, `label_version`, `rule_version`, `feature_version`, `split_version`, `snapshot_id` phải theo mọi kết quả. Sửa số tay tạo review_decision. Hồi cứu dùng bản sửa sau cutoff được ghi là descriptive-restated và không được lẫn với point-in-time prediction.
