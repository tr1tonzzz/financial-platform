# PROJECT PLAN
## Financial Data Platform

**Document ID:** PP-FDP-01
**Version:** 1.0
**Tài liệu tham chiếu:** SRS-FDP-01, SDD-FDP-01, TP-FDP-01
**Chuẩn tham chiếu:** cấu trúc theo PMBOK (rút gọn cho đồ án học kỳ) — WBS, Schedule, Risk Register

---

## 1. Project Overview

| Mục | Nội dung |
|---|---|
| Tên dự án | Financial Data Platform |
| Người thực hiện | 1 sinh viên |
| Thời lượng | 16 tuần (1 học kỳ) |
| Hình thức báo cáo | Checkpoint 2 tuần/lần: Slide + Báo cáo Word |
| Ràng buộc năng lực | SQL: cơ bản · Python: mới bắt đầu · React: đã biết |
| Phạm vi tham chiếu | SRS-FDP-01 — chỉ thực hiện Must Have + phần lõi Should Have trong học kỳ này |

---

## 2. Work Breakdown Structure (WBS)

```
1. Khởi tạo & Nghiên cứu
   1.1 Nghiên cứu sản phẩm tham khảo
   1.2 Xác định Problem Statement, Scope
   1.3 Học Python nền tảng

2. Thiết kế
   2.1 Thiết kế ERD (SDD Mục 3)
   2.2 Thiết kế kiến trúc (SDD Mục 2)
   2.3 Setup schema database

3. Xây dựng Data Pipeline
   3.1 Ingestion module (FR-01–FR-04)
   3.2 Standardization module (FR-05–FR-07)
   3.3 Validation module (FR-08–FR-09)
   3.4 Bitemporal storage (FR-10–FR-11)

4. Xây dựng Backend & API
   4.1 API cơ bản (FR-12–FR-14, FR-16–FR-17)
   4.2 Point-in-time query (FR-15)
   4.3 Analytics endpoints (FR-18–FR-20)
   4.4 Tối ưu hiệu năng + Benchmark (FR-21–FR-22)

5. Xây dựng Frontend
   5.1 Company Overview + As-of control (FR-23, FR-27)
   5.2 Trend (FR-24)
   5.3 Comparison (FR-25)
   5.4 Screening (FR-26, nếu kịp)

6. Kiểm thử & Hoàn thiện
   6.1 Unit/Integration/API test (theo TP-FDP-01)
   6.2 Đóng gói Docker (NFR-08)
   6.3 Tài liệu hóa
   6.4 Báo cáo & Demo cuối kỳ
```

---

## 3. Schedule — 16 tuần / 8 Checkpoint

| CP | Tuần | WBS liên quan | Trọng tâm | Test Case chạy (theo TP-FDP-01) | Deliverable báo cáo |
|---|---|---|---|---|---|
| 1 | 1–2 | 1.1, 1.2, 1.3 | Vấn đề & học nền tảng | — | Slide + Word: Scope, nghiên cứu thị trường |
| 2 | 3–4 | 2.1, 2.2, 2.3 | Thiết kế dữ liệu & kiến trúc | — | Slide + Word: ERD, kiến trúc |
| 3 | 5–6 | 3.1 (rút gọn), 4.1 (rút gọn) | **Vertical Slice** | TC-01–TC-05 (rút gọn) | Slide + Word: demo end-to-end 3 công ty |
| 4 | 7–8 | 3.1, 3.2 | Mở rộng ingestion & chuẩn hóa | TC-01–TC-09 | Slide + Word: coverage report |
| 5 | 9–10 | 3.3, 3.4 | Validation & Bitemporal | TC-10–TC-15, TC-19, TC-20 | Slide + Word: as-of query, restatement list |
| 6 | 11–12 | 4.2, 4.3, 4.4 | API đầy đủ & Benchmark | TC-16–TC-27, TC-32, TC-33 | Slide + Word: bảng benchmark trước/sau |
| 7 | 13–14 | 5.1, 5.2, 5.3, (5.4) | Dashboard | TC-28–TC-31 | Slide + Word: demo dashboard |
| 8 | 15–16 | 6.1, 6.2, 6.3, 6.4 | Hoàn thiện & Demo cuối kỳ | TC-34–TC-36, toàn bộ regression | Báo cáo cuối kỳ đầy đủ + Slide cuối kỳ |

*Nội dung chi tiết từng tuần trong mỗi Checkpoint (task theo ngày, Definition of Done, cấu trúc slide/Word gợi ý) đã được lập ở tài liệu roadmap chi tiết đi kèm (`roadmap-16-tuan-checkpoint.md`) — Project Plan này giữ vai trò khung quản lý ở mức cao hơn, nối trực tiếp WBS với FR/Test Case để phục vụ truy vết.*

### 3.1 Milestone chính

| Milestone | Tuần | Tiêu chí đạt |
|---|---|---|
| M1 — Scope Baseline | 2 | SRS-FDP-01 được xác nhận, không đổi Must Have sau mốc này |
| M2 — Design Baseline | 4 | SDD-FDP-01 được xác nhận |
| M3 — Vertical Slice | 6 | TC-01 đến TC-05 pass trên dữ liệu thật (không giả lập) |
| M4 — Data Platform hoàn chỉnh | 10 | NFR-04 đạt; FR-10, FR-11, FR-15 hoạt động đúng |
| M5 — Platform tối ưu hoàn chỉnh | 12 | FR-21, FR-22 có kết quả; toàn bộ API pass test |
| M6 — Sản phẩm hoàn chỉnh | 16 | Toàn bộ Must Have trong SRS đạt Definition of Done |

**Điểm kiểm soát cứng (Hard Gate):** Nếu M3 không đạt đúng hạn tuần 6, phải kích hoạt kịch bản cắt giảm scope tại Mục 5 trước khi tiếp tục.

---

## 4. Resource Plan
- Nhân lực: 1 sinh viên, ước lượng 15–20 giờ/tuần.
- Công cụ: máy cá nhân, Docker, PostgreSQL, VS Code — không phát sinh chi phí.
- Dữ liệu: SEC Financial Statement Data Sets — miễn phí, không giới hạn truy cập.

---

## 5. Risk Register

| ID | Rủi ro | Xác suất | Ảnh hưởng | Mitigation | Contingency | Kích hoạt khi |
|---|---|---|---|---|---|---|
| R-01 | Học Python chậm hơn dự kiến | Cao | Cao | Checkpoint 1 có deliverable cụ thể để đo tiến độ sớm | Giảm số chỉ tiêu canonical từ 10 xuống 5–6 | M3 trễ quá 1 tuần |
| R-02 | Tag XBRL không map hết (coverage thấp) | Cao | Trung bình | Chấp nhận ngưỡng NFR-04 = 70%, không cố map 100% | Loại chỉ tiêu có coverage quá thấp khỏi phạm vi Must Have | Coverage < 50% ở Checkpoint 4 |
| R-03 | Không tìm đủ trường hợp restatement thật trong 30 công ty | Trung bình | Trung bình | Chọn trước công ty có lịch sử niêm yết lâu năm | Minh họa bằng 1 case tạo giả lập có chú thích rõ trong báo cáo | Không tìm được case nào tới hết Checkpoint 5 |
| R-04 | Trễ Vertical Slice (M3) | Trung bình | Cao | Giới hạn vertical slice ở 3 công ty, 3 chỉ tiêu | Kích hoạt Hard Gate — báo giảng viên, cắt scope trước khi đi tiếp | Hết tuần 6 chưa qua TC-01–TC-05 |
| R-05 | Frontend tốn thời gian dù đã biết React | Thấp | Trung bình | Đã có buffer ở Checkpoint 7 | Cắt FR-26 (Screening UI) trước | Hết tuần 13 chưa xong Overview + Trend |
| R-06 | Thiếu thời gian tích hợp & viết báo cáo cuối kỳ | Trung bình | Cao | Viết tài liệu song song mỗi Checkpoint (không dồn cuối kỳ) | Dùng lại nội dung SRS/SDD/TP đã có sẵn làm khung báo cáo cuối kỳ | Không áp dụng — đã phòng ngừa cấu trúc từ đầu |

---

## 6. Scope Change Control

Mọi thay đổi FR/NFR trong SRS-FDP-01 sau Milestone M1 phải:
1. Ghi vào Change Log của SRS-FDP-01.
2. Đánh giá tác động tới WBS/Schedule ở tài liệu này.
3. Được xác nhận trong buổi báo cáo Checkpoint gần nhất.

**Thứ tự cắt giảm khi cần (tham chiếu SRS Mục 2.2, Feature priority):**
FR-26 (Screening UI) → FR-20 (Screening logic) → FR-19/FR-25 (Comparison) → giảm số công ty từ 30 xuống 15.
**Không cắt:** FR-10, FR-11, FR-15 (bitemporal) và FR-21, FR-22 (benchmark) — đây là các yêu cầu định vị giá trị cốt lõi của đồ án theo SRS Mục 2.1.

---

## 7. Deliverables Checklist (cuối dự án)

- [ ] SRS-FDP-01 (đã duyệt, có Change Log nếu có sửa)
- [ ] SDD-FDP-01
- [ ] TP-FDP-01 + kết quả chạy toàn bộ Test Case
- [ ] PP-FDP-01 (tài liệu này)
- [ ] Source code (Git repository)
- [ ] Docker Compose để tái lập hệ thống
- [ ] Coverage report, danh sách restatement, bảng benchmark (đính kèm phụ lục báo cáo cuối kỳ)
- [ ] Báo cáo cuối kỳ tổng hợp + Slide trình bày

---

## Change Log

| Version | Ngày | Nội dung thay đổi |
|---|---|---|
| 1.0 | | Bản phát hành đầu tiên, tách từ roadmap gộp trước đó |
