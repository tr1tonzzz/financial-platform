# Khả thi thu thập dữ liệu gần hiện tại: 2025–2026

> **Trạng thái 03/10/2026 — hồ sơ khảo sát trước.** Project hiện hành tập trung thu thập, kiểm định và phân tích lợi nhuận–dòng tiền–cổ tức tiền mặt. Xem [SRS hiện hành](../research-platform/02-de-tai-va-srs.md) và [phương pháp thống nhất](../research-platform/11-phuong-phap-thu-thap-va-xu-ly.md). Các ngưỡng cảnh báo, dự báo, scope và lịch cũ bên dưới chỉ để tham khảo; không là yêu cầu MVP hiện hành.

Ngày khảo sát: **03/10/2026**. Đối tượng: BCTC và cổ tức tiền mặt của doanh nghiệp Việt Nam trong đề tài [đã chốt](../research-options/01-chot-y-tuong-de-tai.md). Đây là khảo sát nguồn và thử nghiệm trích xuất nhỏ, chưa phải pilot 10 công ty hay dataset nghiệm thu.

## Kết luận để quyết định

**Có cơ sở thực tế để bổ sung BCTC năm 2025, quý I và bán niên 2026 cho project.** Đã tải 15 PDF thật, tổng 804 trang, thuộc DHG, HPG, VHC, VNM và VHE. VHC có cả tiếng Việt và tiếng Anh nên số file không phải số quan sát độc lập. Danh mục của REE và FPT cũng truy cập được, nhưng chưa tải các PDF được phát hiện vì đường dẫn bị loại theo robots đã đọc.

Điểm nghẽn chính là chuẩn hóa và kiểm tra dữ liệu: 12/15 PDF có **0 trang với hơn 100 ký tự text trích được**. Một PDF có text nhưng mã chữ bị lỗi. Vì vậy, phương án chỉ tải PDF rồi dùng regex trên text sẽ bỏ sót nhiều báo cáo mới. OCR đã chạy trên 10 trang lựa chọn của hai báo cáo; bộ tìm dòng đơn giản khớp 11/12 số đã đối chiếu từ ảnh, thiếu một dòng nợ phải trả. Sau đối chiếu ảnh có đủ sáu chỉ tiêu của mỗi báo cáo. Đây không phải độ chính xác độc lập hay kết quả toàn bộ pipeline.

Thông báo cổ tức tải được bằng HTML từ VSDC, gồm bốn thông báo của hai công ty. Chưa kiểm tra đủ lịch sử để khẳng định tổng cổ tức năm hoặc xác nhận thực trả.

| Dữ liệu | Tính khả thi tại ngày khảo sát | Cách đưa vào đề tài |
|---|---|---|
| BCTC năm 2025 | Đã tải bản kiểm toán của HPG, DHG, VHC và bản hợp nhất năm của VHE | Mở rộng phân tích năm sau khi chuẩn hóa và kiểm tra từng công ty |
| Quý I/2026 | Đã tải HPG, DHG, VHC, VNM | Lớp cập nhật; giữ mức bảo đảm của từng báo cáo |
| Bán niên 2026 | Đã tải báo cáo soát xét HPG, DHG, VHC, VNM | Ưu tiên cho cập nhật gần hiện tại; tách khỏi dữ liệu năm |
| Quý III/2026 | Kỳ vừa kết thúc Ti30/09; khảo sát này chưa thu thập | Gắn trạng thái chưa kiểm chứng, chưa đưa vào cam kết độ phủ |
| Năm 2026 | Chưa kết thúc đối với doanh nghiệp có năm tài chính theo năm dương lịch | Chưa có đủ cơ sở dùng BCTC cả năm đã kiểm toán |
| Cổ tức thuộc năm lợi nhuận 2025 | Đã tải và tách được thông báo 2025–2026 | Lưu sự kiện, năm lợi nhuận, các mốc thời gian; kiểm tra đầy đủ trước tổng hợp |
| Nhãn cắt giảm trong 12 tháng sau BCTC công bố năm 2026 | Nhiều cửa sổ còn mở | Đánh dấu bị kiểm duyệt theo thời gian, không ép nhãn 0 |

## Đề xuất phạm vi

Giữ tên đề tài và MVP hiện hành. Dùng 2020–2024 làm phần lịch sử ban đầu; bổ sung **năm 2025 có điều kiện theo độ phủ và công sức pilot**. Đưa quý I và bán niên 2026 thành lớp phân tích cập nhật cho các công ty đã qua kiểm tra. Không tăng ngay nghĩa vụ phủ 30 công ty × tất cả quý, không lấy vài PDF thành công làm bằng chứng cho cả thị trường.

Như vậy, dữ liệu mới hỗ trợ phân tích lợi nhuận–dòng tiền, khả năng duy trì cổ tức và trình diễn tính cập nhật của hệ thống. Việc huấn luyện/đánh giá cảnh báo vẫn dùng mẫu có thông tin và nhãn hợp lệ theo [research-design](../research-design.md); nhãn tương lai chưa trưởng thành phải loại khỏi đánh giá hoặc xử lý theo thiết kế kiểm duyệt phù hợp.

## Các tài liệu riêng

1. [Nguồn, ngày công bố và kết quả truy cập](01-nguon-va-truy-cap.md).
2. [Thử nghiệm PDF, OCR và đối chiếu sáu chỉ tiêu](02-thu-nghiem-pdf-ocr.md).
3. [Kiến thức tài chính: kỳ báo cáo, cổ tức và thời điểm dự báo](03-ky-tai-chinh-co-tuc-va-nhan.md).
4. [Kỹ thuật IT: crawler, OCR, kiểm định và cập nhật](04-thiet-ke-crawl-va-chuan-hoa.md).
5. [Pilot, công sức và cách tái lập](05-pilot-va-tai-lap.md).

Bằng chứng có thể đọc bằng máy: [manifest truy cập](download-evidence.json), [đối chiếu OCR](ocr-core-check.json), [sự kiện cổ tức](dividend-event-examples.json), [tổng số đo](probe-summary.json). PDF/HTML/ảnh/OCR gốc nằm tại `data-sets/research-evidence/2026-10-03-recent/`, hiện bị Git ignore; các MD và JSON là phần có thể chia sẻ qua repository. Không ghi rằng raw evidence đã được commit.
