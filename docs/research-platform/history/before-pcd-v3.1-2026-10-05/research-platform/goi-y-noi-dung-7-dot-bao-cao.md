# Gợi ý nội dung cho bảy mốc báo cáo

Nhịp 03/10/2026: sáu đợt tiến độ hai tuần, một tổng kết tuần 13. Thiếu đầu ra thì báo nguyên nhân/kế hoạch, không điền tiến độ giả. Xem [khung chung](07-bao-cao-hang-tuan.md) và [mẫu điền](mau-bao-cao-hai-tuan.md).

## Đợt 1 — tuần 1–2: Đề tài và tính khả thi nguồn

Word:

- Tên/câu hỏi đề tài và phạm vi đã chọn; phần giảng viên cần góp ý.
- Bảng nguồn, một BCTC và thông báo nhiều năm đã đọc; sáu trường và DPS.
- Luồng tự tìm/tải, log thực tế, phần còn nhập tay và lỗi/policy.
- Kiến thức đã hiểu; gate discovery và ba đầu ra cho tuần 3–4.

Slide: Tên đề tài → mục tiêu hai tuần → nguồn/dữ liệu → pipeline → demo crawl → điều đã hiểu/giới hạn → kế hoạch và góp ý.

Demo/minh chứng: Danh mục IR tới file/raw; thông báo tách hai năm. Nếu tự tìm cổ tức chưa chạy, nói rõ.

Điểm trao đổi: Ngách và tiêu chí IT có phù hợp rubric? Scope/nguồn nào cần điều chỉnh?

## Đợt 2 — tuần 3–4: Pilot dữ liệu và quyết định phạm vi

Word:

- Ledger 3×3 năm: mong đợi/tìm/tải/trích/duyệt, scope và phần thiếu.
- Một lỗi OCR/cột/đơn vị với before–after và kiểm định.
- ERD/SQLite, review audit, components và coverage.
- Phút/report/notice và quyết định 5–8 công ty hoặc giữ pilot.

Slide: Mục tiêu pilot → bảng số thực → dữ liệu/coverage → OCR và schema → test/review → bài học → scope chốt.

Demo/minh chứng: Một candidate OCR tới reviewed fact, mở nguồn; sửa có audit.

Điểm trao đổi: Scope theo effort đã vừa sức chưa? Protocol đối chiếu cần bổ sung gì?

## Đợt 3 — tuần 5–6: Ứng dụng và vòng đời sự kiện

Word:

- UI/engine, bảng năm lợi nhuận và timeline; ratio có operands.
- Quy tắc route/trùng/nhiều năm/sửa/hủy và share basis.
- Tests nghiệp vụ và các lỗi được bắt; không gán missing bằng 0.
- Kiến thức JOIN/financial đã hiểu; kế hoạch dataset/holdout.

Slide: Kết quả ứng dụng → tiến độ → mô hình dữ liệu → event resolver → demo/tests → kiến thức và hạn chế → tuần 7–8.

Demo/minh chứng: Thông báo sửa lịch không tăng DPS; JOIN không nhân bản tài chính.

Điểm trao đổi: Quy tắc nghiệp vụ và bộ holdout có đủ đại diện các lỗi quan trọng?

## Đợt 4 — tuần 7–8: Đánh giá chất lượng và công sức

Word:

- Danh sách development/holdout, quy tắc tách và cách tạo gold.
- Bảng B0/B1/B2, joint correctness sáu targets và mẫu số/missing.
- Event/component/lifecycle/coverage metrics; effort và lỗi đại diện.
- Giới hạn tự chấm/mẫu nhỏ và việc sửa sau freeze.

Slide: Mục tiêu đánh giá → thiết kế mẫu → baseline → bảng kết quả → lỗi/demo → effort/giới hạn → quyết định tiếp.

Demo/minh chứng: Chạy một holdout hoặc mở log cố định; chỉ rõ B2 có người review.

Điểm trao đổi: Cách chấm và baseline hợp rubric? Có cần người đối chiếu độc lập?

## Đợt 5 — tuần 9–10: Phân tích và cập nhật dữ liệu

Word:

- Ba case lợi nhuận–CFO–DPS cùng snapshot/nguồn/coverage.
- Điều kiện ratio/growth và n nếu có Spearman; giới hạn quan hệ mô tả.
- Update/version/rerun, snapshot cũ và export tái lập.
- Ca 2026 nếu đã làm; phần còn thiếu và việc viết báo cáo.

Slide: Câu hỏi phân tích → coverage → case/biểu đồ → kỹ thuật snapshot → demo update → giới hạn diễn giải → viết báo cáo.

Demo/minh chứng: Một case truy ngược source, chạy lại không nhân bản và export.

Điểm trao đổi: Cách diễn giải case và giới hạn có phù hợp? Kết quả nào nên đưa vào báo cáo cuối?

## Đợt 6 — tuần 11–12: Hoàn thiện và chuẩn bị bảo vệ

Word:

- Bản mô tả kiến trúc/thuật toán, ERD và hướng dẫn chạy.
- Tổng hợp đóng góp IT, benchmark/case cùng scope thực đạt.
- Kết quả hai lượt demo, câu hỏi đã tự trả lời và lỗi còn lại.
- Checklist nộp cuối và hướng tốt nghiệp có gate dữ liệu.

Slide: Bài toán → phạm vi thực đạt → dữ liệu/kiến trúc → kỹ thuật chính → kết quả/demo → hạn chế → công việc nộp.

Demo/minh chứng: Luồng end-to-end, lỗi nguồn/sự kiện và một sửa code nhỏ tự giải thích.

Điểm trao đổi: Còn yêu cầu rubric hoặc minh chứng nào thiếu trước nộp?

## Tổng kết — tuần 13: Tổng kết và nộp cuối

Word:

- Bản cuối theo mẫu trường: bài toán, phương pháp, triển khai, đánh giá và kết luận.
- Manifest bundle, hướng dẫn chạy, số đo/snapshot nhất quán.
- Phần chưa hoàn thành, giới hạn và kế hoạch liên thông dự đoán.

Slide: Dùng deck bảo vệ cuối; chọn số liệu thật và demo đã tập.

Demo/minh chứng: Thử chạy gói nộp trong môi trường sạch; nêu đúng trạng thái nếu chưa thử.

Điểm trao đổi: Ghi phản hồi cuối thật và xác nhận danh mục nộp theo quy định.

