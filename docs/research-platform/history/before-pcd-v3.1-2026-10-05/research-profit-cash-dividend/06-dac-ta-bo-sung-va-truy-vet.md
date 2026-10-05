# 06 — Đặc tả bổ sung và ma trận truy vết

Mã: **ADD-FAP-PCD-01 v1.0**, ngày 04/10/2026. Trạng thái đề xuất; **không thay SRS-FAP-01 v3.0**. Các yêu cầu bên dưới có hiệu lực nghiệm thu extension khi được đưa vào change record. Phần baseline vẫn áp dụng đầy đủ SRS cũ.

## 1. Những gì đã có trong SRS

| Năng lực | SRS v3.0 | Xử lý lần này |
|---|---|---|
| Thu thập, trích, chuẩn hóa, review | FR03–FR18 | Tái sử dụng, không ghi thành tính năng mới |
| Lifecycle, components, coverage | FR19–FR24 | Giữ contract, minh họa bằng VNM |
| LNST/CFO, tỷ số, DPS, chọn case | FR25–FR30 | Dùng làm đầu vào cho cầu nối |
| Truy nguồn/UI/export/replay | FR31–FR35 | Mở schema operands cho bridge |
| Đánh giá/case/backup | FR36–FR38 | Thêm test và công sức extension |

## 2. Yêu cầu extension

| ID | Yêu cầu kiểm chứng được | Mức đề xuất | Nghiệm thu |
|---|---|---|---|
| E01 | Nhận diện gián tiếp/trực tiếp/unknown, điểm bắt đầu, kỳ, scope, đơn vị cho ca | Must nếu nhận extension | Thiếu context không xuất bridge hoàn chỉnh |
| E02 | Lưu leaf/subtotal/total, group, raw label/code, value, locator và review cho từng dòng | Must | Có đủ lineage; subtotal không là operand cộng lần hai |
| E03 | Tính CFO từ start+leaves, residual và tolerance bằng số chính xác | Must | Đối chiếu ca thật và fixtures, không chia0/đổi dấu ngầm |
| E04 | Bridge thiếu dòng/khác scope trả status và lý do; không lấp phần thiếu bằng một nguyên nhân tự tạo | Must | Ca lỗi không được gắn reconciled_complete |
| E05 | So hai năm tương thích, phân rã delta CFO thành delta start/groups và delta residual | Should | Tổng đóng góp khớp delta CFO trong tolerance |
| E06 | Hiển thị LNST và điểm đầu LNTT riêng; cột so sánh có report version | Must | Người đọc nhận biết lợi nhuận nào đang ở cầu nối |
| E07 | Nối case với DPS profit_year và timeline, giữ coverage/basis/as_of | Must | Partial không thành annual đủ; scheduled không thành paid |
| E08 | Click kết quả cầu nối/case mở operands và nguồn; export/replay giữ mapping/formula version | Must | Replay không đổi sau chỉnh candidate/version mới |
| E09 | Đo thời gian nhập/review/correct từng ca và chất lượng trước–sau review | Must | Báo riêng tự động, hỗ trợ tay và tự đánh giá |
| E10 | Thêm góc CFO so với dòng chi cho chủ sở hữu cùng kỳ/scope | Could | Nhãn đúng BCLCTT; không gọi là payout profit_year |

Không đặt độ chính xác90–99% khi chưa pilot. Điều kiện chắc chắn cần có là 100% kết quả **được xuất bản** truy được operands/source hoặc được chặn rõ vì thiếu. Điều này không ngụ ý 100% targets trích được.

## 3. Use case chính

**UC-E01 — Duyệt một cầu nối:** người vận hành chọn report/period/scope; hệ thống đề xuất rows hoặc nhận chép tay; người vận hành xác nhận role/dấu/locator; validator kiểm subtotal và CFO; reviewer duyệt kèm lý do. Nếu thiếu, lưu partial và issue. Thành công khi có bridge result và audit trong cùng transaction, không phải khi residual tình cờ bằng0.

**UC-E02 — Đọc một case:** người dùng chọn snapshot/case; hệ thống hiện LNST/CFO, bridge, cổ tức profit_year; mở source của một khoản; xuất bản case. Nếu annual DPS chưa đủ, vẫn đọc bridge nhưng không có kết luận mức cổ tức cả năm.

**UC-E03 — Cập nhật:** tải phiên bản mới, review mapping/relation, tính snapshot mới, mở snapshot cũ và mới. Kết quả cũ không biến mất; không cần semantic impact engine tự động ở extension tối thiểu.

## 4. Truy vết nhu cầu → yêu cầu → kiểm tra

| Câu hỏi | Yêu cầu | Thiết kế | Kiểm tra trong07 |
|---|---|---|---|
| Vì sao CFO khác lợi nhuận? | E01–E04,E06 | bridge_mapper/validator | P01–P05,P09 |
| Dòng nào đóng góp vào thay đổi? | E05 | bridge_compare | P06 |
| Cổ tức đang được so theo góc nào? | E07,E10 | case_composer | P07,P08 |
| Số có kiểm chứng và tái lập không? | E02,E08 | operands/snapshot | P10 |
| Extension có đáng công không? | E09 | effort log, tác vụ | P11 |

## 5. Change record đề xuất

**CR-PCD-01:** thêm E01–E04,E06–E09 cho một ca trước; E05 cho cặp năm có dữ liệu; E10 tùy chọn. Lý do: tăng chiều sâu giải thích của đề tài kết hợp. Tác động: cần bridge tables, UI, tests, bộ gold theo dòng và quỹ giờ trong07. Baseline sáu facts/9 reports vẫn giữ. Nếu thời gian thiếu, ưu tiên baseline và giảm extension bằng change record.

Chủ sở hữu, người phê duyệt, ngày chấp nhận: **chưa xác nhận**. Không sửa trạng thái các tài liệu hiện hành thành approved từ nghiên cứu này. Sau khi chốt, cập nhật đồng bộ SRS, kế hoạch, checklist, mẫu báo cáo và bản Word tương ứng, thay vì duy trì hai bộ đặc tả có nghĩa vụ khác nhau.
