# Roadmap thực hiện BCTC–cổ tức Việt Nam trong 13 tuần

> **Trạng thái 03/10/2026 — hồ sơ khảo sát trước.** Project hiện hành tập trung thu thập, kiểm định và phân tích lợi nhuận–dòng tiền–cổ tức tiền mặt. Xem [SRS hiện hành](../research-platform/02-de-tai-va-srs.md) và [phương pháp thống nhất](../research-platform/11-phuong-phap-thu-thap-va-xu-ly.md). Các ngưỡng cảnh báo, dự báo, scope và lịch cũ bên dưới chỉ để tham khảo; không là yêu cầu MVP hiện hành.

Đây là kế hoạch hiện hành. Tên file có 16-tuan chỉ được giữ để tương thích liên kết.

Nguồn kế hoạch: [PP](PP-FDP-01.md). Yêu cầu: [SRS](SRS-FDP-01.md). Phương pháp: [Đề cương](../research-design.md).

## Các checkpoint

| Checkpoint | Tuần | Sản phẩm cần trình bày |
|---|---|---|
| 1 | 1–2 | Câu chuyện thực tế, 10 công ty pilot, nguồn/tài liệu thật, crawler tải raw có hash |
| 2 | 3–4 | Parser 6 chỉ tiêu, quy đổi đơn vị/kỳ/phạm vi, bộ đối chiếu và lỗi |
| 3 | 5–6 | Sự kiện cổ tức đúng trạng thái, chuỗi hoàn chỉnh một công ty |
| 4 | 7–8 | Dataset 30 công ty; quyết định mở 60–80 dựa trên thời gian review; bảng mẫu loại |
| 5 | 9–10 | Phân tích quan hệ, rule score, baseline và 3 case study |
| 6 | 11–12 | API/dashboard, kết quả kiểm thử và báo cáo; ML nếu đạt gate |
| 7 | 13 | Buffer, tái lập demo, slide và bảo vệ |

## Nội dung báo cáo mỗi checkpoint

- Mục tiêu và việc đã hoàn thành, kèm file/log/nguồn có thể kiểm tra.
- Độ phủ dữ liệu, lỗi còn mở và thời gian xử lý thủ công.
- Kết quả phân tích hoặc kiểm định mới; giới hạn của kết luận.
- Quyết định giảm/tăng phạm vi và công việc hai tuần tiếp theo.

Không trình bày mục tiêu chưa đo như kết quả. Tuần 1–2 cần dữ liệu thật sớm; tuần 9–10 dành cho phân tích, không dồn hết sang cuối kỳ.

## Mốc bắt buộc

Cuối tuần 2 tải được nguồn thật; cuối tuần 4 trích xuất và đối chiếu được; cuối tuần 6 có demo chuỗi hoàn chỉnh; cuối tuần 8 chốt dataset; cuối tuần 10 có phân tích và case study.

Thứ tự giảm phạm vi: nguồn thứ hai → OCR tổng quát → UI nâng cao → ML → chỉ tiêu mở rộng → giảm mục tiêu công ty về mức tối thiểu. Giữ truy vết, kiểm định, trạng thái thiếu và phân tích có bằng chứng.

## Công việc chi tiết

Thực hiện bảng từng tuần trong [PP](PP-FDP-01.md), kiểm tra [checklist](checklist-16-tuan-chi-tiet.md), bắt đầu bằng [kế hoạch tuần 1–2](tuan-1-2-chi-tiet-theo-ngay.md).
