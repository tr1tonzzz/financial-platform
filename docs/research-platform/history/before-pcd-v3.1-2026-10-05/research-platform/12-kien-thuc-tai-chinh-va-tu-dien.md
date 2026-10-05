# Kiến thức tài chính và từ điển dữ liệu lõi

Nếu chưa có nền tảng tài chính, đọc [tài liệu nhập môn bằng ví dụ dễ hiểu](18-nhap-mon-tai-chinh-cho-du-an.md) trước. Trang này giữ các định nghĩa trường và quy tắc dữ liệu dùng khi triển khai.

## 1 Sáu trường BCTC bắt buộc

| Code | Ý nghĩa | Nguồn/loại kỳ |
|---|---|---|
| net_income_total | LNST tổng của scope đang dùng | Kết quả kinh doanh, duration |
| cfo | Lưu chuyển tiền thuần từ hoạt động kinh doanh | Lưu chuyển tiền tệ, duration |
| cash_equivalents | Tiền và tương đương tiền | Cân đối, instant |
| total_assets | Tổng tài sản | Cân đối, instant |
| total_liabilities | Tổng nợ phải trả | Cân đối, instant |
| total_equity | Tổng VCSH | Cân đối, instant |

Dữ liệu monetary lưu VND integer/Decimal; raw unit/scale được giữ. PDF ghi nghìn/triệu đồng phải chuyển có bằng chứng. Nợ phải trả khác nợ vay; tiền khác lợi nhuận; CFO không phải chênh lệch tiền cuối kỳ.

Số năm là duration theo ngày bắt đầu/kết thúc thật; assets/cash là instant. Quý/bán niên 2026 nằm riêng series, không nhân bốn Q1 hoặc dùng CFO lũy kế chia LNST riêng quý. LNST tổng không thay bằng phần cổ đông mẹ khi tính CFO/LNST tổng.

## 2 Scope và diễn giải

Dùng hợp nhất làm series khi có; nếu chỉ báo cáo cấp doanh nghiệp thì xác nhận và đánh dấu entity. Riêng công ty mẹ là scope khác. Mỗi ratio lấy operands cùng document basis/period; cohort gộp phải tương thích và có số mẫu riêng. DHG trong phép thử trước là cấp doanh nghiệp, không tự gán consolidated để ghép cùng VNM.

CFO/lợi nhuận hợp nhất phản ánh nhóm, không trực tiếp là tiền có thể phân phối của pháp nhân mẹ. Muốn nghiên cứu nguồn tiền thực sự chi cổ tức ở mẹ, cần BCTC riêng, retained earnings, cash/debt/capex và điều kiện khác; phần này chưa là lời khẳng định của MVP.

EPS và LNST cổ đông mẹ có thể bổ sung. DPS/EPS chỉ là tỷ số tham khảo khi EPS tương thích profit_year/scope/share basis; EPS dùng số cổ phiếu bình quân còn DPS có cơ sở quyền riêng. Không gán phép tính đó thành tỷ lệ tổng tiền đã thực trả. Không nhân DPS với số cổ phiếu cuối năm để ước lượng tổng chi tiền như fact.

## 3 Từ điển sự kiện cổ tức

| Trường | Cách hiểu |
|---|---|
| issuer_id/ticker/isin | Pháp nhân và chứng khoán, mapping có hiệu lực |
| notice_id, notice_version_id | Danh tính thông báo và phiên bản nguồn |
| event_kind | cash_dividend, stock_dividend, amendment, cancellation hoặc other |
| published_at | Ngày/giờ hiển thị, timezone unknown khi nguồn không ghi |
| first_seen_at/checked_at | Mốc hệ thống đọc nguồn, không thay ngày công bố |
| record_date | Ngày đăng ký cuối cùng |
| scheduled_payment_date | Lịch thanh toán trong thông báo |
| confirmed_paid_at/evidence | Optional, chỉ có khi bằng chứng riêng xác nhận thực trả |
| dps_vnd/par_value/rate | Đồng/cổ phiếu; tỷ lệ trên mệnh giá lưu riêng |
| profit_year | Năm lợi nhuận nguồn nói rõ; không suy từ payment year |
| installment_kind | Tạm ứng/đợt/thanh toán còn lại/unknown theo nguồn |
| supersedes/cancels | Quan hệ điều chỉnh/hủy đã review |
| share_basis_id/action_status | Cơ sở cổ phiếu và trạng thái kiểm tra so sánh |
| review_status/source_locator | Candidate/reviewed và vị trí bằng chứng |

Status lifecycle proposed/approved/right_notice/amended/cancelled không đồng nghĩa paid. Nghị quyết thông qua kế hoạch là tài liệu đối chiếu, không cộng thêm như một đợt trả đã thông báo. Nguồn có dòng “tỷ lệ 25%” trên mệnh giá 10.000 đồng nghĩa 2.500 đồng/cổ phiếu, không yield 25% theo giá thị trường.

## 4 Năm lợi nhuận và ví dụ thật

[Thông báo VNM 187729](https://vsdc.vn/vi/ad1/187729) gộp 350 đồng thuộc 2024 và 2.500 đồng thuộc 2025. Một notice, hai components. Published/record/payment date giữ ở event, profit_year/dps giữ ở từng component. Không gán cả 2.850 vào 2025 và không cộng lại cùng event vì có hai route URL.

[Bốn ví dụ đã trích](../research-recent-data/dividend-event-examples.json) là mẫu development. Tổng phần đã quan sát chưa có nghĩa lịch sử đầy đủ. Ngày thanh toán đã qua vẫn giữ scheduled nếu chưa có payment confirmation.

## 5 Missing và tính đầy đủ

Financial missing không thay 0. Event chưa rõ năm → unallocated, không cố join. Năm không có notice → unknown/partial, không tự ghi không trả. Chỉ dùng explicit decision nguồn rõ để ghi declared_zero, giữ review và phạm vi thời gian.

Coverage có reviewed_complete_as_of_snapshot, partial, unknown; thêm not_applicable khi định nghĩa nghiệp vụ thật không áp dụng. Tính đủ gắn snapshot và bằng chứng rà nguồn/đối chiếu nghị quyết, không hứa không còn đính chính trong tương lai.

Split/cổ tức cổ phiếu/cổ phiếu thưởng có thể thay cơ sở DPS; lưu raw, ngày hiệu lực và mapping adjustment nếu kiểm chứng. Phát hành thêm không được tự chỉnh bằng một hệ số chung. Khi chưa xử lý, chặn so sánh DPS cần cùng basis.
