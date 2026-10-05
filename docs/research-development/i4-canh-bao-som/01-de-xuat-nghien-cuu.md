# I4 — Nghiên cứu cảnh báo sớm có giải thích

Ngày: 03/10/2026. Rule score: P0/MVP. Logistic: P1 có điều kiện. Phục vụ RQ3.

## 1. Hướng đề xuất

Kiểm tra liệu tín hiệu BCTC đã biết tại cutoff có giúp nhận diện mức cổ tức giảm trong 12 tháng kế tiếp tốt hơn baseline lịch sử không. Bắt đầu với quy tắc dễ kiểm tra; logistic chỉ thêm khi dữ liệu/nhãn đủ.

Điểm cảnh báo 0–4 là độ nghiêm trọng theo rule, không là xác suất. Mô hình có predict_proba cũng cần đánh giá xác suất trước diễn giải cho người dùng.

## 2. Câu hỏi và giả thuyết

- I4-RQ1: rule score có phân biệt nhóm giảm/duy trì trên mẫu đủ điều kiện không?
- I4-RQ2: thêm CFO/nợ/tiền có cải thiện so với chỉ lịch sử chi trả?
- I4-RQ3: hiệu quả và tỷ lệ cảnh báo sai có thay đổi theo ngành/năm/basis?
- I4-RQ4: logistic cho xác suất có chất lượng hơn xác suất prevalence train không?

Đây là câu hỏi kiểm định, không cam kết kết quả. Nghiên cứu có thể kết luận tín hiệu yếu hoặc không đủ mẫu.

## 3. Ba tầng so sánh

| Tầng | Mô hình/baseline | Trạng thái |
|---|---|---|
| Lịch sử | Dự báo future_dps=past_dps; lớp maintained | Bắt buộc, có thể recall ca giảm bằng 0 |
| Quy tắc | Bốn tín hiệu theo đề cương; báo version bỏ tín hiệu trùng | MVP, ngưỡng thăm dò |
| Logistic | Ít feature lõi, regularization và split theo thời gian | Chỉ sau gate |

Xác suất prevalence train là baseline probabilistic riêng; baseline maintained không có xác suất có ý nghĩa nếu chỉ dùng lớp cứng.

## 4. Phạm vi và gate

Theo [đề cương](../../research-design.md): khoảng 200 mẫu đủ điều kiện, 40 ca giảm/ngừng trong train và ≥10 ca ở validation/test. Gate là vận hành thăm dò, không bảo đảm power hay đủ mẫu calibration. 30 công ty×5 năm tối đa 150 mẫu trước lọc, nên ML có thể không khả thi ở mức MVP tối thiểu.

Không random split để giải quyết thiếu ca; không thêm năm chưa khép; không đổi unknown thành maintained. Mở dữ liệu chỉ sau kiểm tra giờ và tiêu chuẩn nguồn.

## 5. Đóng góp và kết quả

Đóng góp là định nghĩa target đo được, chống leakage, so baseline trên cùng mẫu, và kiểm tra giải thích đúng số/nguồn. [Rudin](https://arxiv.org/abs/1811.10154) là lý do xem xét mô hình hiểu trực tiếp; không chứng minh lựa chọn này tự động dự báo tốt.

Nộp label/feature/split specifications, rule results, model report nếu có, bảng lỗi, ba case và giới hạn. Không đưa dự báo thành lời khuyên giao dịch hoặc khẳng định khả năng chi trả hợp pháp.

## 6. Tài liệu cần dùng

[Tài chính và nhãn](02-kien-thuc-tai-chinh.md), [IT rule/logistic](03-ky-thuat-it.md), [đánh giá ngoài mẫu](04-du-lieu-thi-nghiem-danh-gia.md), M01/T08–T11 trong [sổ nguồn](../02-so-tai-lieu-tham-khao.md).
