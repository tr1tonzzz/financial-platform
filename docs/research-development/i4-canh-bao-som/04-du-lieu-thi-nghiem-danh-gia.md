# I4 — Protocol đánh giá cảnh báo và dự báo

Ngày: 03/10/2026. Chưa chạy đánh giá RQ3.

## 1. Eligibility và thống kê trước mô hình

Lọc theo source/version hợp lệ tại cutoff, cùng scope/basis, cổ tức tiền past>0, cơ sở cổ phiếu so sánh được, outcome đã khép và bằng chứng nhãn đủ. Unknown/censored không tham gia metric phân loại cuối, nhưng báo số và lý do.

Lập flow count từ company/year thô → facts đủ → date đủ → past_dps dương → nhãn đủ → từng partition. Không dùng số firm-year lý thuyết làm số mẫu train.

## 2. Gate ML và mốc lịch

Gate theo đề cương: khoảng 200 mẫu đủ, train ≥40 ca dương, validation/test mỗi tập ≥10 ca dương. Sau gate vẫn kiểm tra đủ ca âm, số công ty, số năm và bất định. Nếu thiếu, đánh giá rule mô tả nếu nhãn đủ và ghi ML chưa khả thi.

Chọn validation_start/test_start từ lịch quan sát và khả năng khép outcome, trước xem metric. Ví dụ minh họa: train cutoff trước 2022 nhưng chỉ giữ outcome kết thúc trước 01/01/2022; validation cutoff 2022 nhưng cần outcome khép trước 01/01/2024; test cutoff từ 2024 và đủ cửa sổ tại snapshot. Đây là ví dụ cách purge, không phải split đã chốt; phải lập bảng số ca trước lựa chọn cuối.

## 3. Baselines và ablation

| So sánh | Mục đích |
|---|---|
| Maintained luôn / future_dps=past_dps | Mốc lịch sử bắt buộc |
| Xác suất prevalence train | Mốc Brier/AP probabilistic |
| Rule score 4 tín hiệu | Thiết kế MVP |
| Rule bỏ CFO<0 hoặc CFO/LNST | Kiểm tra tín hiệu trùng |
| Logistic chỉ lịch sử vs thêm BCTC | Đo giá trị bổ sung |

So trực tiếp trên **intersection** sample IDs đủ đầu vào cho mọi phương pháp đang so; báo thêm coverage của từng phương pháp trên toàn cohort để không che khả năng từ chối. Score rời rạc có thể xếp hạng cho PR, nhưng không dùng như xác suất để tính Brier.

## 4. Metrics

Confusion matrix, precision, recall, F1, tỷ lệ cảnh báo và số ca dương/âm. Test một lớp thì không diễn giải ranking metric như đánh giá phân biệt; mẫu quá ít ca thì ghi chưa đủ kết luận. Baseline accuracy cao khi ca giảm ít không chứng minh khả năng cảnh báo.

Dùng **Average Precision (AP)** với thư viện và định nghĩa ghi rõ; không gọi AP và diện tích PR tính hình thang là cùng phép tính. [Tài liệu average_precision_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html). Báo prevalence test để hiểu baseline ranking.

Với mô hình xác suất: `Brier=mean((p−y)^2)` cho binary target, cùng reliability diagram và số mẫu từng bin. [Tài liệu calibration](https://scikit-learn.org/stable/modules/calibration.html). Ít mẫu không ép fit thêm calibrator; dùng bins ít và báo độ bất định.

## 5. Chọn threshold và độ bất định

Threshold cảnh báo chọn trên validation với mục tiêu đã ghi, ví dụ cân bằng precision/recall hoặc giữ lượng review trong nguồn lực. Không chọn theo test. Rule threshold tài chính và label threshold là hai loại khác nhau, mỗi loại có version.

Bootstrap theo company để interval và chênh lệch metric paired trên cùng mẫu; mẫu có cả hai lớp trong replicate mới tính metric tương ứng, báo tỷ lệ replicate bị thiếu lớp. Mẫu nhỏ có interval rất rộng là kết quả phải nêu, không tăng số bootstrap để giả vờ thêm thông tin.

## 6. Phân tích lỗi

Rà false positive, false negative, một ca dòng tiền yếu vẫn duy trì và một ca giảm do yếu tố chưa đo. Check timeline, source quality, boundary payment, special dividend và basis. Giải thích từ bằng chứng; các lý do không có tài liệu chỉ ghi giả thuyết.

## 7. Hồ sơ nộp và kết luận được phép

Dataset/split manifest, feature/label/rule versions, baseline table, metric counts/interval, calibration nếu có, errors và runtime. Nếu không hơn baseline, kết luận dữ liệu/tín hiệu hiện tại chưa cho thấy cải thiện; không chuyển mục tiêu sau test để làm đẹp báo cáo.
