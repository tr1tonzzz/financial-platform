# Quy trình nghiên cứu và lộ trình đọc

Ngày: 03/10/2026. Lịch chính ở [PP 13 tuần](../initial-docs/PP-FDP-01.md); phần này chỉ phân bổ nghiên cứu trong lịch đó.

## 1. Nguyên tắc chung

Chốt câu hỏi → kiểm chứng nguồn → định nghĩa biến → dựng mẫu đối chiếu → đóng băng protocol → chạy thí nghiệm → phân tích giới hạn → cập nhật tài liệu. Ghi thất bại và kết quả âm; không đổi nhãn hay loại outlier chỉ để nâng điểm.

Mỗi kết quả có một file MD riêng. Tên đề xuất: `results/i1-parser-benchmark-<snapshot>.md`, `results/i2-cashflow-association-<snapshot>.md`, `results/i3-event-reconciliation-<snapshot>.md`, `results/i4-temporal-evaluation-<snapshot>.md`, `results/i5-grounded-qa-<snapshot>.md`. Chỉ tạo hồ sơ kết quả khi đã chạy; hiện tại bốn file mỗi ý tưởng là protocol và tài liệu kiến thức.

## 2. Chọn mẫu pilot

Chọn 10 doanh nghiệp phi tài chính theo ít nhất ba nhóm ngành, khác kích thước và kiểu công bố. VNM/VSH là ứng viên dựa trên tài liệu vừa đọc, chưa phải danh sách mẫu đã chốt. Cần xác minh ngành và báo cáo kiểm toán trước chọn. Giữ nhật ký doanh nghiệp bị loại, lý do và thời gian thử nguồn.

Chọn mẫu dễ có PDF text là chiến lược khả thi, nhưng phải công bố thiên lệch. Với 30–80 công ty thuận tiện, kết luận chỉ áp dụng mẫu quan sát, không suy rộng toàn thị trường. Tránh chọn chỉ các doanh nghiệp vẫn còn niêm yết hoặc chỉ những doanh nghiệp đã biết giảm cổ tức mà không nêu cách lấy mẫu.

## 3. Lộ trình học và đầu ra

| Giai đoạn | Tài liệu cần đọc | Bài tập/đầu ra trong repo |
|---|---|---|
| Tuần 1–2 | I1 tài chính, I3 tài chính, F03, V02/V03 | Đọc tay 3 báo cáo và 5 thông báo; sổ URL, audit, kỳ/phạm vi |
| Tuần 3–4 | T01/T02/T04/T05, I1 IT/benchmark | Gold facts, mapping, bộ kiểm tra và bảng công sức |
| Tuần 5–6 | I3 IT/thí nghiệm, từ điển chung | Chuỗi phiên bản sự kiện; chốt loại nhãn sau pilot |
| Tuần 7–8 | F01/F02/F04/F05, I2 tài chính/phương pháp | Snapshot mô tả, danh sách missing, công thức đủ điều kiện |
| Tuần 9–10 | T07–T11, M01, I4 | Báo cáo quan hệ, ba case, đánh giá rule score; gate ML |
| Tuần 11–13 | T13 và protocol tái lập | API/demo, hướng dẫn, báo cáo kết quả/giới hạn |
| Sau MVP | M02/M03/T12, toàn bộ I5 | Benchmark tìm kiếm rồi đánh giá RAG |

Không cần học FCFE, OCR, LLM và mọi mô hình ngay tuần đầu. FCFE đòi hỏi dữ liệu mở rộng; OCR chỉ khi scan ảnh hưởng cohort; ML chỉ khi nhãn đủ; RAG sau dữ liệu ổn định.

## 4. Hồ sơ một thí nghiệm

Ghi: câu hỏi, giả thuyết, dữ liệu/tiêu chí loại, đơn vị quan sát, baseline, phép xử lý, cấu hình/seed/phiên bản, metric/mẫu số, kết quả thực tế, độ bất định, chi phí thao tác, lỗi và kết luận được phép. Link raw bằng hash/locator, không chỉ ghi ticker.

Tách development/evaluation của parser và training/validation/test của dự báo. Dataset dùng phát triển mapping không trở thành gold độc lập chỉ vì đổi tên file. Nếu chỉ một người đọc gold, ghi hạn chế và đọc lại ngẫu nhiên sau một khoảng thời gian.

## 5. Đóng băng và rà soát

Trước khi chạy final test, chốt cohort, ngưỡng nhãn, rule version, metric, splitter và cách xử lý missing. Giữ test để đánh giá một lần của cấu hình chốt; nếu phát hiện lỗi dữ liệu, tạo snapshot mới, nêu thay đổi và báo cáo cả ảnh hưởng. Không chọn phiên bản có kết quả đẹp nhất mà bỏ những lần sửa khác.

## 6. Gate thực hiện

I1/I3 trước, I2 sau. I4 ML theo gate hiện hành: khoảng 200 mẫu đủ điều kiện, 40 ca dương trong train, ít nhất 10 ở validation và test; đây là gate vận hành, không bảo đảm power. I5 cần facts đã duyệt và nguồn retrievable; thiếu nền dữ liệu thì dừng ở tìm kiếm có nguồn.

Ước lượng mở rộng bằng `số báo cáo còn lại × phút tải/parser/review đã đo + số thông báo × phút đối chiếu + thời gian viết/kiểm thử`, giữ 20% dự phòng theo PP. Không ghi các ước lượng thành giờ thực tế.
