# I4 — Kỹ thuật IT: rule engine và mô hình theo thời điểm

Ngày: 03/10/2026. Thiết kế, chưa huấn luyện mô hình.

## 1. Point-in-time dataset

Một row gồm company/cutoff, feature values/status/fact versions, past_dps và event versions, outcome_end, future_dps/label/evidence, snapshot và config versions. Có thể có nhiều cutoff cho cùng công ty; khóa không chỉ company-year.

Chọn facts có available_at≤cutoff, cùng kỳ/scope/basis; feature tăng nợ/giảm tiền cần năm trước hợp lệ. Không dùng số so sánh đã sửa trong báo cáo công bố sau cutoff. Không dùng tổng DPS tương lai, trạng thái cuối tại snapshot hoặc future-derived coverage làm feature.

## 2. Rule engine

Rule config có input domains, threshold, trọng số, version và mô tả. Output từng rule: fired/not_fired/not_applicable/missing cùng số thực tế, threshold và fact_ids. Score tổng chỉ xuất khi policy đủ dữ liệu/domain được đáp ứng.

Lưu explanation có cấu trúc rồi render thành văn bản, ví dụ “CFO/LNST=0,42, thấp hơn ngưỡng thăm dò 0,5”; không cần LLM để viết lời giải thích phép so sánh. Thiếu data khác score=0. Không chia score cho số rule có dữ liệu mà vẫn dùng nhãn ngưỡng của score đầy đủ.

## 3. Logistic baseline

Đầu tiên chỉ dùng ít feature: CFO/A, L/A, Cash/A và lịch sử DPS đã biết; thử CFO/LNST trên tập domain hợp lệ riêng. Feature list và regularization chọn trên train/validation. Chuẩn hóa scale và xử lý missing nằm trong Pipeline; không impute trước split. [Hướng dẫn leakage](https://scikit-learn.org/stable/common_pitfalls.html).

Nếu class_weight được thử, ghi cấu hình và xem ảnh hưởng calibration. Không cần SMOTE ở baseline; nếu thử oversampling chỉ trên train trong từng fold, không đưa dữ liệu nhân tạo vào test. Với ít ca dương, ưu tiên ít tham số và báo bất ổn hệ số.

## 4. Splitter theo lịch

```text
train: cutoff < validation_start AND outcome_end < validation_start
validation: cutoff trong khoảng validation
            AND outcome_end < test_start
test: cutoff >= test_start AND outcome_end <= snapshot_at
```

Thêm kiểm tra nhãn train/validation thực sự có thể biết trước mốc kế tiếp, theo loại chứng cứ; outcome_end sớm nhưng bằng chứng chưa công khai vẫn không đủ. Nhóm cùng cutoff/day vào cùng partition khi ngày nguồn không có giờ.

[TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) không tự xử lý panel, ngày không đều và horizon nhãn. Viết splitter theo timestamp/period, không coi gap 12 dòng là 12 tháng.

## 5. Giải thích và lưu kết quả

Logistic: hiển thị feature, giá trị/scale, hệ số và contribution trên log-odds, cùng intercept/version. Contribution không là xác suất độc lập hay tác động nhân quả. Nếu sau này có model phức tạp và SHAP, cần tài liệu/benchmark riêng; chưa cần cho MVP.

Lưu model config, feature schema, train range, label/split versions, thresholds, metric output, seed/runtime và snapshot hash. Chưa cần model registry dịch vụ; thư mục artifact có manifest đủ để chạy lại.

## 6. Kiểm thử trọng yếu

Fact published sau cutoff bị loại; amendment future không thành feature; future_end chồng validation bị loại khỏi train; LNST âm không tạo ratio hợp lệ; thiếu năm trước không tạo delta=0; test không fit imputer/scaler; cùng sample IDs giữa baseline/rule/logistic khi so trực tiếp.

Kỹ năng cần học: classification logistic, loss/regularization, Pipeline, thresholding, date-based evaluation, calibration. [Protocol](04-du-lieu-thi-nghiem-danh-gia.md) quy định metric và gate.
