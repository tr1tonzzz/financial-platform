# TEST PLAN
## Financial Data Platform

**Document ID:** TP-FDP-01
**Version:** 1.0
**Tài liệu tham chiếu:** SRS-FDP-01, SDD-FDP-01
**Chuẩn tham chiếu:** cấu trúc theo IEEE 829 (Test Documentation)

---

## 1. Introduction

### 1.1 Purpose
Xác định phạm vi, phương pháp, tài nguyên và lịch trình kiểm thử cho hệ thống Financial Data Platform, đảm bảo mọi yêu cầu trong SRS-FDP-01 đều được kiểm chứng trước khi nghiệm thu.

### 1.2 Scope
Bao gồm: unit test, integration test, API test, kiểm thử thủ công UI, và benchmark hiệu năng (đo lường, không phải pass/fail nhị phân).

---

## 2. Test Strategy

| Loại kiểm thử | Mục tiêu | Công cụ | Mức độ tự động |
|---|---|---|---|
| Unit Test | Kiểm tra logic từng hàm/module độc lập (mapping, validation) | Pytest | Tự động |
| Integration Test | Kiểm tra luồng nhiều module phối hợp (ingestion → DB) | Pytest + test database riêng | Tự động |
| API Test | Kiểm tra từng endpoint, cả case hợp lệ/không hợp lệ | Pytest + FastAPI TestClient | Tự động |
| UI Test | Kiểm tra luồng tương tác người dùng trên dashboard | Thủ công theo checklist | Thủ công |
| Performance Benchmark | Đo thời gian thực thi truy vấn, không phải test đúng/sai | Script Python đo thời gian + `EXPLAIN ANALYZE` | Bán tự động |

### 2.1 Entry Criteria
- SRS-FDP-01 và SDD-FDP-01 đã hoàn thành ở mức đủ chi tiết cho module cần test.
- Môi trường test (database riêng, dữ liệu mẫu) đã sẵn sàng.

### 2.2 Exit Criteria
- 100% Must Have FR có tối thiểu 1 test case tương ứng và pass.
- NFR-04 (coverage ≥ 70% cho ≥ 6/10 chỉ tiêu) đạt trên dữ liệu thật.
- Benchmark FR-21/FR-22 có kết quả ghi nhận đầy đủ trước/sau tối ưu.

---

## 3. Test Environment
- Database test: PostgreSQL riêng biệt với database phát triển, seed bằng dữ liệu mẫu 1 quý, 3–5 công ty.
- Backend chạy ở chế độ test (`ENV=test`), dùng biến môi trường riêng.
- Dữ liệu test cho case lỗi: bộ dữ liệu giả lập có chèn sẵn giá trị âm bất thường, bản ghi trùng lặp, giá trị outlier (phục vụ FR-08).

---

## 4. Traceability Matrix (FR ↔ Test Case)

| FR | Mô tả ngắn | Test Case ID | Loại test | Kết quả mong đợi |
|---|---|---|---|---|
| FR-01 | Tải dữ liệu nguồn | TC-01 | Integration | File ZIP tải và giải nén thành công với tham số quý hợp lệ |
| FR-01 | — | TC-02 | Integration | Xử lý đúng khi tham số quý không hợp lệ (báo lỗi rõ ràng, không crash) |
| FR-02 | Nạp staging | TC-03 | Integration | Số dòng staging = số dòng file nguồn |
| FR-03 | Idempotent | TC-04 | Integration | Chạy ingestion 2 lần → số dòng không đổi sau lần 2 |
| FR-04 | Ghi log | TC-05 | Unit | Bảng `ingestion_log` có bản ghi mới sau mỗi lần chạy, đúng field |
| FR-05 | Danh mục canonical | TC-06 | Unit | Bảng `metric_definition` có đủ 10 chỉ tiêu đã định nghĩa |
| FR-06 | Ánh xạ tag | TC-07 | Unit | Với input có 2 tag cùng nghĩa, output chỉ có 1 giá trị theo đúng priority |
| FR-06 | — | TC-08 | Unit | Với tag không có trong mapping, hệ thống bỏ qua có kiểm soát, không crash |
| FR-07 | Coverage report | TC-09 | Integration | Coverage tính đúng theo công thức (số filing resolve / tổng filing) |
| FR-08 | Rule validation | TC-10 | Unit | Giá trị âm ở chỉ tiêu không cho phép âm → bị gắn cờ |
| FR-08 | — | TC-11 | Unit | Bản ghi trùng khóa → bị phát hiện |
| FR-08 | — | TC-12 | Unit | Giá trị lệch > ngưỡng so với trung vị lịch sử → bị gắn cờ outlier |
| FR-09 | Gắn cờ không xóa | TC-13 | Integration | Bản ghi vi phạm vẫn tồn tại trong DB, có `is_flagged=true` và `flag_reason` |
| FR-10 | Bitemporal | TC-14 | Integration | Nạp 2 filing cùng kỳ khác `filed_at` → cả 2 bản ghi cùng tồn tại |
| FR-11 | Truy vết nguồn | TC-15 | Unit | Mỗi fact có `accession_no` hợp lệ, không rỗng |
| FR-12 | Tìm kiếm company | TC-16 | API | `GET /companies?search=apple` trả đúng kết quả liên quan |
| FR-13 | Company profile | TC-17 | API | `GET /companies/{cik}` với CIK hợp lệ trả đủ thông tin; CIK không tồn tại → 404 |
| FR-14 | Financials mới nhất | TC-18 | API | Trả đúng giá trị `filed_at` lớn nhất cho mỗi chỉ tiêu |
| FR-15 | Point-in-time | TC-19 | API | Với 2 giá trị `as_of` khác nhau bao quanh ngày điều chỉnh → 2 kết quả khác nhau |
| FR-15 | — | TC-20 | API | `as_of` trước ngày filing đầu tiên → trả rỗng có kiểm soát, không lỗi 500 |
| FR-16 | Trend | TC-21 | API | Trả đủ chuỗi giá trị theo đúng thứ tự thời gian |
| FR-17 | Giá lịch sử | TC-22 | API | Trả đúng khoảng `from`–`to` |
| FR-18 | Overview | TC-23 | Integration | Chỉ số phái sinh (Revenue Growth, Profit Margin) tính đúng theo công thức |
| FR-19 | Comparison | TC-24 | API | `POST /compare` với 2–5 CIK trả đúng cấu trúc, đúng giá trị |
| FR-20 | Screening | TC-25 | API | Điều kiện đơn (VD: ROE > 15) trả đúng tập company thỏa mãn |
| FR-21 | Benchmark | TC-26 | Performance | Script benchmark chạy và xuất được bảng thời gian trước/sau tối ưu |
| FR-22 | Query plan | TC-27 | Performance | `EXPLAIN ANALYZE` được lưu lại đầy đủ cho từng truy vấn benchmark |
| FR-23 | UI Overview | TC-28 | Manual UI | Tìm kiếm → xem overview đúng dữ liệu từ API |
| FR-24 | UI Trend | TC-29 | Manual UI | Biểu đồ hiển thị đúng số điểm dữ liệu |
| FR-25 | UI Comparison | TC-30 | Manual UI | Chọn/bỏ chọn company cập nhật đúng bảng so sánh |
| FR-27 | UI As-of | TC-31 | Manual UI | Thay đổi as-of date → số liệu trên UI cập nhật đúng theo TC-19 |
| NFR-01 | Hiệu năng truy vấn đơn | TC-32 | Performance | Thời gian phản hồi < 300ms trên dữ liệu tham chiếu |
| NFR-02 | Hiệu năng screening | TC-33 | Performance | Thời gian phản hồi < 1s sau tối ưu |
| NFR-03 | Reliability ingestion | TC-34 | Integration | Ngắt kết nối giữa chừng khi ingestion → dữ liệu cũ không bị hỏng |
| NFR-04 | Data quality | TC-35 | Integration | Coverage ≥ 70% cho ≥ 6/10 chỉ tiêu trên dữ liệu thật |
| NFR-08 | Reproducibility | TC-36 | Integration | `docker-compose up` từ trạng thái sạch → hệ thống chạy đúng |

*Nguyên tắc: mỗi FR/NFR bắt buộc có ít nhất 1 dòng trong bảng này. Không có yêu cầu nào trong SRS được coi là "đã kiểm thử" nếu không xuất hiện ở đây.*

---

## 5. Test Case Detail Template

Mỗi Test Case trong bảng trên khi triển khai thực tế cần được viết chi tiết theo mẫu:

```
Test Case ID: TC-XX
Liên quan đến: FR-XX
Mục tiêu:
Điều kiện tiên quyết:
Bước thực hiện:
  1. ...
  2. ...
Dữ liệu đầu vào:
Kết quả mong đợi:
Kết quả thực tế: [điền khi chạy]
Trạng thái: Pass / Fail
```

---

## 6. Risk-based Test Prioritization

| Mức ưu tiên | Nhóm Test Case | Lý do |
|---|---|---|
| Cao | TC-14, TC-19, TC-20 (bitemporal) | Đây là phần logic phức tạp nhất, sai sót khó phát hiện bằng mắt |
| Cao | TC-26, TC-27, TC-32, TC-33 (benchmark) | Là bằng chứng định lượng cốt lõi của đồ án |
| Trung bình | TC-07, TC-08, TC-09 (mapping/coverage) | Ảnh hưởng trực tiếp chất lượng dữ liệu nhưng dễ phát hiện lỗi qua coverage report |
| Thấp | TC-28 → TC-31 (UI thủ công) | Ảnh hưởng trải nghiệm, không ảnh hưởng tính đúng đắn dữ liệu |

---

## 7. Test Schedule
Việc thực thi Test Case gắn với từng Checkpoint trong PP-FDP-01 — không dồn toàn bộ kiểm thử vào cuối kỳ. Tham chiếu PP-FDP-01, Mục 3 để biết Test Case nào chạy ở Checkpoint nào.

---

## Change Log

| Version | Ngày | Nội dung thay đổi |
|---|---|---|
| 1.0 | | Bản phát hành đầu tiên |
