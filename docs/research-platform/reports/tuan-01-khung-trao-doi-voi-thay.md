# Khung trao đổi tuần 1 với giảng viên

Trạng thái: **bản chuẩn bị, chưa là báo cáo tiến độ đã hoàn thành**. Sinh viên: [điền]. Ngày trao đổi: [điền]. Thời gian thực làm: [điền]. Nguồn/bài tập: [bộ tuần 1](../24-tai-lieu-va-bai-tap-tuan-01.md).

## 1. Đề tài và mục tiêu dự kiến

**Xây dựng hệ thống thu thập, chuẩn hóa và phân tích dữ liệu lợi nhuận, dòng tiền kinh doanh và cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam.**

Hệ thống dự kiến hỗ trợ người dùng tra cứu số liệu có nguồn, so sánh lợi nhuận với dòng tiền, và xem các đợt cổ tức theo năm lợi nhuận. Trọng tâm kỹ thuật là dữ liệu đúng kỳ/đơn vị/phạm vi, sự kiện có vòng đời và kết quả có thể truy vết, tái lập. Tính khả thi tự động trên toàn bộ tập dữ liệu còn cần kiểm chứng.

## 2. Kiến thức nền đã học — sinh viên tự điền

| Nội dung | Diễn giải bằng lời của mình | Tài liệu đã đọc/trang | Tình trạng |
|---|---|---|---|
| Bảng cân đối và số tại thời điểm | [điền] | [điền] | chưa xác nhận |
| Kết quả kinh doanh và số cả kỳ | [điền] | [điền] | chưa xác nhận |
| CFO khác LNST | [điền] | [điền] | chưa xác nhận |
| Thuyết minh, đơn vị và phạm vi | [điền] | [điền] | chưa xác nhận |
| Năm lợi nhuận/ngày công bố/lịch trả | [điền] | [điền] | chưa xác nhận |

## 3. Minh họa dữ liệu thực tế

Mẫu trợ lý chuẩn bị gồm BCTC kiểm toán DHG 2024 và hai notice VSDC, có URL/trang trong bộ tuần 1. Sinh viên ghi ngày tự đối chiếu: [điền]; người kiểm độc lập nếu có: [điền, không có ghi self_check].

- Bảng sáu nhãn và nguồn: [đính kèm phần đã tự đối chiếu].
- Phép tính cân đối, CFO/LNST và nợ/tài sản: [ghi toán hạng, kết quả, điều kiện].
- Hai bản ghi cổ tức: [đính kèm]; không gán thực trả khi chỉ có lịch thanh toán.
- Quyết định ánh xạ nhãn “Tiền” vào schema: [pending hoặc quyết định kèm lý do].

## 4. Phân tích yêu cầu sơ bộ

| Nhu cầu | Khó khăn cần xử lý | Đầu ra dự kiến |
|---|---|---|
| Xem lợi nhuận và CFO cùng doanh nghiệp/năm | Sai cột, đơn vị, kỳ hoặc phạm vi | Bảng đã review, có locator nguồn |
| Xem cổ tức thuộc năm lợi nhuận | Nhiều đợt, khác năm công bố, có điều chỉnh | Sự kiện thành phần và tổng có điều kiện |
| Giải thích một tỷ số | Mẫu số không hợp lệ hoặc dữ liệu thiếu | Công thức, toán hạng, lý do không tính |
| Kiểm kết quả sau cập nhật nguồn | Phiên bản thay đổi | Bản gốc, lịch sử và snapshot tái lập |

Tham chiếu [SRS v3.0](../22-srs-dac-ta-yeu-cau-phan-mem.md). Đây là thiết kế dự kiến; đánh dấu chức năng đã chạy chỉ khi có minh chứng.

## 5. Phạm vi đề xuất và giới hạn

Pilot 3 doanh nghiệp phi tài chính × 2023–2025; HPG/DHG/VHC là ứng viên cần xác nhận. Đề xuất mở rộng bản cuối tới 8 doanh nghiệp, quyết định theo nguồn và effort tuần 4; kế hoạch hiện hành cho phép 5–8. Chưa xác nhận đủ 9 BCTC pilot/54 chỉ tiêu hoặc notices lịch sử.

Mẫu nhỏ phục vụ đánh giá hệ thống và phân tích khám phá; không suy rộng quan hệ tài chính ra toàn thị trường. ML chưa thuộc MVP bắt buộc.

## 6. Tiến độ thực và việc tiếp theo

| Công việc | Kết quả thật | Minh chứng | Vướng mắc |
|---|---|---|---|
| Môi trường Python 3.12 | [điền] | [lệnh/log] | [điền] |
| Đọc tay BCTC và notice | [điền] | [bảng/file] | [điền] |
| Scope manifest và ledger | [điền] | [file] | [điền] |
| JSON candidate và review | [điền] | [file/quyết định] | [điền] |
| TC01/TC08 mức ban đầu | [not_run/pass/fail/blocked] | [expected/actual] | [điền] |

Tuần 2 dự kiến hoàn thiện discovery có cấu hình, lưu nguồn/phiên bản và chạy một đường xử lý từ tài liệu gốc tới dữ liệu đã đối chiếu. Cập nhật thời lượng dựa trên nhật ký thật.

## 7. Ý kiến cần thầy xác nhận

Trọng tâm đánh giá hệ thống hay nghiên cứu thống kê: [điền]. Phạm vi dữ liệu: [điền]. Rubric và hạn nộp: [điền]. Yêu cầu gold/review/khảo sát người dùng: [điền]. Mẫu tài liệu và demo: [điền].

## 8. Kịch bản nói 3–5 phút

1. 45 giây: vấn đề người dùng và mục tiêu đề tài.
2. 60 giây: ba báo cáo và vì sao cần cả lợi nhuận lẫn CFO.
3. 90 giây: mở BCTC/notice thật, chỉ số/trang và việc tách năm lợi nhuận khỏi lịch trả.
4. 45 giây: cách hệ thống xử lý, giới hạn mẫu và phần chưa làm.
5. 60 giây: xin ý kiến về phạm vi, tiêu chí đánh giá và kế hoạch tuần tiếp theo.

Chỉ dùng “em đã” cho việc tự thực hiện, có file/log. Với bộ tài liệu được trợ lý chuẩn bị, mô tả đúng là “em có bộ nguồn và mẫu để đối chiếu”.
