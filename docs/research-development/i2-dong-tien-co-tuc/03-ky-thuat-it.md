# I2 — Kỹ thuật IT: bảng phân tích, thống kê và dashboard

Ngày: 03/10/2026. Thiết kế đề xuất; cần facts đã duyệt của I1.

## 1. Analytics mart

Bảng `firm_year_metrics` khóa theo snapshot/company/year/scope/basis. Lưu giá trị, trạng thái, fact_ids, công thức, denominator policy và metric_version. Bảng DPS profit_year chỉ ghép component có năm được nguồn nêu; phần không rõ năm có bảng riêng.

Đề xuất lưu facts dạng long để provenance/version rõ; pivot thành wide khi phân tích. Không pivot trước xử lý conflict/version vì có thể vô tình lấy trung bình hai báo cáo.

## 2. Hàm tính chỉ số có trạng thái

```text
ratio(numerator, denominator, compatibility_rules)
→ {value, status, reason, input_fact_ids, formula_version}
```

Domain rule kiểm tra scope/basis/kỳ, mẫu số và độ đầy đủ. Khi LNST≤0, CFO/LNST trả not_applicable kèm lý do; CFO âm vẫn là fact hợp lệ. Không dùng `fillna(0)` trước tính ratio. Numeric facts chính xác; chuyển float chỉ ở bước thống kê và lưu độ làm tròn hiển thị.

## 3. Thống kê cần học

Python/pandas: join/pivot/groupby; SciPy: phân bố, hạng và kiểm tra; matplotlib/Plotly: xu hướng và biểu đồ missing. [SciPy spearmanr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html) hỗ trợ hệ số hạng; phải tự ghi số quan sát thực tế theo cặp biến.

Pipeline phân tích tạo bảng machine-readable và báo cáo MD: phân bố → mức thiếu → tương quan → chênh lệch nhóm → độ nhạy → case. Code phân tích đọc snapshot cố định, tránh truy vấn dữ liệu đang thay đổi giữa hai biểu đồ.

## 4. Độ bất định với panel

Bootstrap đề xuất: lấy mẫu **company_id** có hoàn lại, giữ toàn bộ năm của mỗi công ty được lấy, tính statistic mỗi lần; ghi seed/số lần và tỷ lệ lần không đủ hai nhóm. Công ty được lấy hai lần phải có bootstrap_id khác để không bị dedupe mất.

Cách này giữ phụ thuộc theo công ty nhưng chưa xử lý mọi cú sốc chung theo năm. Chỉ có năm năm quan sát, thêm kiểm tra bỏ từng năm/ngành và báo giới hạn; không gọi bootstrap cụm là giải pháp cho mọi phụ thuộc.

## 5. API và giao diện tối thiểu

API trả metric/value/status, formula, source facts, snapshot, scope/basis và thời điểm. Dùng [FastAPI response model](https://fastapi.tiangolo.com/tutorial/response-model/) để kiểm tra cấu trúc response; không coi schema validation là kiểm chứng tài chính.

Ba vùng dashboard: xu hướng CFO/LNST/DPS; tỷ số và mức thiếu; danh sách sự kiện và liên kết nguồn. Không đặt số tiền tuyệt đối và tỷ số khác đơn vị trên cùng trục mà không giải thích. Vẽ khoảng trống cho missing, không nối thành đường bằng 0.

Chọn một giao diện theo SDD: Streamlit ở pilot hoặc React cho MVP; tránh duy trì cả hai lâu dài. Chart thể hiện data_status và cho mở đúng trang nguồn.

## 6. Chất lượng và tái lập

Kiểm tra join không tăng số dòng; ratio domain; event component không cộng hai lần; kết quả sort ổn định; ba case tìm lại nguồn; chart/API cùng snapshot. Hướng dẫn chạy phân tích từ raw/snapshot và manifest, không chỉ nộp notebook đã bấm chạy.

Protocol phương pháp tại [thí nghiệm I2](04-du-lieu-thi-nghiem-danh-gia.md); công thức tài chính tại [kiến thức I2](02-kien-thuc-tai-chinh.md).
