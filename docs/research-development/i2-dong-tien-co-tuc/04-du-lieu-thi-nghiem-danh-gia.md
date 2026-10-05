# I2 — Thiết kế thí nghiệm quan hệ dòng tiền–cổ tức

Ngày: 03/10/2026. Chưa có kết quả định lượng trên cohort.

## 1. Dataset và câu hỏi chốt trước

Phân tích mô tả: 30 công ty × 2020–2024 tối đa 150 firm-year, scope/basis nhất quán, audit đủ bằng chứng. Dòng DPS theo profit_year chỉ gồm component xác định được năm. Nhãn giảm/duy trì dùng cửa sổ cutoff của I4 khi đánh giá kết quả tương lai; hai bảng phải báo cáo riêng.

Chốt ba quan hệ chính: CFO/LNST với ổn định chi trả; L/A với nhóm giảm; Cash/A với nhóm giảm. Quan hệ bổ sung là thăm dò và được đánh dấu để tránh nhiều kiểm định rồi chỉ chọn kết quả đẹp.

## 2. Phân tích mô tả bắt buộc

1. Báo cáo cohort theo ngành/năm, file audit, scope/basis và lý do loại.
2. Heatmap đủ sáu facts và độ phủ sự kiện; tách missing khỏi DPS 0 xác minh.
3. Median/IQR/min/max và phân bố ratio; số ca LNST≤0, vốn≤0, mẫu số gần 0.
4. Xu hướng CFO/LNST/DPS của từng case; tổng DPS theo profit_year và theo lịch không trộn.

Mỗi bảng tương quan có N theo cặp. Thêm bảng trên tập complete-case chung để xem thay đổi có phải do mẫu khác nhau; không tự impute để tăng N trong phân tích mô tả.

## 3. Tương quan và so sánh nhóm

Dùng Spearman cho liên hệ đơn điệu; biến hằng trả “không xác định”. Tài liệu [SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html) cảnh báo độ chính xác p-value ở mẫu nhỏ. Với panel, không hoán vị từng firm-year độc lập: ưu tiên effect size và bootstrap theo công ty; phép hoán vị nếu dùng phải tôn trọng cấu trúc cụm và giả định trao đổi được.

So nhóm reduced/omitted với maintained: chênh lệch median, số doanh nghiệp và số quan sát mỗi nhóm, interval cụm nếu đủ. Quan hệ có thể bị ngành, năm, quy mô, đầu tư hoặc sở hữu chi phối; chỉ thêm hồi quy kiểm soát khi dữ liệu đủ và mô hình không quá nhiều tham số.

Không dùng p<0,05 làm điều kiện duy nhất. Nếu làm nhiều kiểm định, báo toàn bộ và phương án kiểm soát đa kiểm định; ghi exploratory nếu không preregister. Không kết luận nhân quả.

## 4. Độ nhạy

| Thay đổi | Mục đích |
|---|---|
| CFO/LNST và CFO/A | Kiểm tra tác động lợi nhuận gần 0 |
| Bỏ từng công ty/ngành/năm | Phát hiện kết quả bị một nhóm chi phối |
| Chỉ facts có metadata đầy đủ | Kiểm tra chất lượng dữ liệu |
| Descriptive-restated vs phiên bản ban đầu | Đo ảnh hưởng sửa số; không trộn với forecast |
| Ngưỡng giảm 10/20/30% | Độ nhạy định nghĩa nhãn, chốt trước test |
| Chỉ nhãn announcement vs chỉ paid | Xem khác đích quan sát; không gộp hai loại |

Không loại outlier vì làm tương quan yếu. Nếu winsorize, giữ bản không cắt, ghi ngưỡng định trước và trình bày cả hai.

## 5. Ba case study cần chọn

Case A: dòng tiền yếu nhưng vẫn chi; case B: cổ tức giảm theo đúng loại bằng chứng; case C: cảnh báo sai hoặc ngược xu hướng nhóm. Chọn case sau thống kê nhưng ghi tiêu chí, tránh chỉ kể case ủng hộ giả thuyết.

Mỗi case gồm timeline BCTC/sự kiện, số liệu và nguồn, ratio đủ điều kiện, lý giải có thuyết minh/nghị quyết nếu có, giả thuyết khác và giới hạn. Chưa có case hoàn chỉnh; VNM/VSH khảo sát mới là đầu mối dữ liệu.

## 6. Kết quả và gate

Nộp báo cáo MD với cohort/mẫu số, biểu đồ, hệ số/effect size/interval, độ nhạy, ba case, câu hỏi chưa trả lời. Không đặt điều kiện “phải có tương quan mạnh” để hoàn thành. Nếu nhãn không đủ, chốt mô tả và ghi phần so nhóm/dự báo chưa kết luận theo đề cương.
