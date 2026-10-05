# I3 — Dữ liệu đối chiếu và đánh giá vòng đời cổ tức

Ngày: 03/10/2026. Protocol, chưa có benchmark 20 thông báo.

## 1. Bộ đối chiếu cần xây

Ít nhất 20 thông báo thật theo TP, gồm cash, stock, tạm ứng, nhiều năm lợi nhuận và amendment. Cần đủ chuỗi liên quan để biết thông báo nào cùng event; số event có thể nhỏ hơn số notice. Tăng mẫu nếu 20 notices không đủ loại lỗi.

Gold do đọc tay ghi notice_id/hash/URL, ngày công khai, company, loại quyền, số tham chiếu, event_id, DPS/components, record/schedule, claim_type và trạng thái bằng chứng. Giữ “chưa xác định” ở gold khi chuỗi nguồn thiếu; không ép tất cả field có đáp án.

## 2. Baseline và thí nghiệm

| Mã | Baseline | Phương án đề xuất | Đầu ra |
|---|---|---|---|
| E1 | Mỗi notice là event | Registry có ghép tham chiếu/amendment | Số duplicate và sai tổng DPS |
| E2 | Gom theo năm đăng tin | Component theo profit_year xác minh | Số firm-year bị sửa và phần không phân bổ |
| E3 | Qua lịch thì paid | Paid chỉ khi đủ bằng chứng | Số nhãn bị gán vượt nguồn; baseline là lỗi minh họa |
| E4 | Một lịch cuối | Version theo cutoff | Mẫu dùng lịch tương lai và sửa nhãn |

E3 chỉ dùng để đo/giải thích hậu quả trong thí nghiệm; không đưa cách gán sai vào dataset sản phẩm.

## 3. Chỉ số

- Field accuracy: đúng DPS, loại, ngày, năm/components trong tổng field có gold xác định.
- Pair precision/recall: trên cặp notices được đánh dấu cùng event; báo cả false merge và false split.
- DPS absolute error và tỷ lệ company-year tổng đúng trên tập gold đủ chuỗi.
- Số event/firm-year/labels thay đổi giữa baseline và proposed, chia cho tổng được so sánh.
- Coverage xác minh lịch và coverage bằng chứng paid báo riêng; tỷ lệ unknown/censored và lý do.
- Phút đọc/ghép một chuỗi và số chuỗi cần quyết định thủ công.

Pair accuracy có thể cao do rất nhiều cặp không liên quan; không dùng một mình. Đánh giá paid precision phải dựa chứng cứ chứ không chỉ khớp nguồn lịch.

## 4. Cửa sổ và coverage

Tại cutoff, past `(cutoff−12 tháng, cutoff]`; future `(cutoff, cutoff+12 tháng]`, quy ước ngày/giờ theo độ chính xác nguồn. Paid target dùng confirmed_payment_date; announcement target dùng ngày công bố xác minh của event, với quy tắc amendment đã chốt.

Sự kiện thiếu ngày chính xác gần biên cửa sổ phải giữ ambiguous/unknown hoặc phân tích độ nhạy, không tự đặt ngày giữa tháng. Future chưa khép ở snapshot → censored. Future khép nhưng nguồn chưa rà đủ → unknown, không omitted.

Chọn announcement target cần chốt cách sửa/hủy: cùng event không cộng lại mỗi amendment; ghi rõ lấy mức công bố ban đầu hay mức hợp lệ cuối trong cửa sổ, và giữ mọi phiên bản. Không dùng diễn giải “thực trả” cho target này.

## 5. Các ca phải thử

Một lịch gộp nhiều profit_year; amendment dời sớm; amendment dời muộn nhiều lần; cash đổi/hủy; cổ phiếu kèm cash; hai đợt cùng ngày; notice thiếu tham chiếu; split làm DPS kém so sánh; BCTC ghi tổng chi nhưng không có ngày event; nguồn dừng giữa cửa sổ.

Đối chiếu không đủ bằng chứng phải tạo kết quả unknown; đây là hành vi đúng, không phải lỗi benchmark.

## 6. Quyết định sau pilot

Ghi tỷ lệ cửa sổ có paid evidence và announcement evidence, chi phí đối chiếu và phạm vi chưa rà. Quyết định target dựa khả năng đo, không chọn target vì cho mô hình điểm cao. Cập nhật đề cương, label_version và sổ quyết định trước final test.

Sản phẩm cuối: event/component registry, coverage ledger, bảng lỗi/ảnh hưởng và báo cáo MD. Hai notices khảo sát hiện tại mới kiểm tra cấu trúc, chưa đủ bất cứ metric tổng quát nào ở trên.
