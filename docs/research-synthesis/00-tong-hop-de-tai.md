# Tổng hợp đề tài BCTC–cổ tức tiền mặt Việt Nam

## Đề tài hiện hành

**Hệ thống thu thập, chuẩn hóa và phân tích dữ liệu BCTC–cổ tức tiền mặt Việt Nam để đánh giá khả năng duy trì cổ tức và nghiên cứu cảnh báo sớm rủi ro cắt giảm.**

Câu chuyện: doanh nghiệp có lãi chưa chắc tạo đủ tiền để duy trì cổ tức. Người đọc cần nối BCTC với các đợt cổ tức và hiểu tín hiệu dòng tiền/nợ, trong khi dữ liệu phân tán và nhiều PDF.

## Làm gì và để làm gì?

Tự thu thập tài liệu Việt Nam → trích xuất số liệu có nguồn → kiểm định → nối sự kiện cổ tức → phân tích quan hệ → tạo cảnh báo có giải thích → cung cấp truy vấn và dashboard.

Trọng tâm: kỹ thuật dữ liệu và phân tích dữ liệu tài chính. Sản phẩm học thuật là dataset có chất lượng đo được và kết quả phân tích có bằng chứng.

## Phạm vi thống nhất

Pilot 10 công ty phi tài chính; MVP tối thiểu 30, mục tiêu 60–80 khi quỹ giờ cho phép. Giai đoạn mô tả 2020–2024; thêm 2025 có điều kiện. Sáu chỉ tiêu lõi: LNST, CFO, tiền, tài sản, nợ phải trả, vốn chủ sở hữu.

Nguồn là công bố và IR Việt Nam, lựa chọn sau pilot. Không mặc định crawler đã khả thi hoặc lịch thanh toán là đã trả. Thiếu sự kiện phải giữ unknown nếu chưa xác minh.

Phân tích CFO/LNST, CFO/tài sản, tiền/nợ phải trả và đòn bẩy; payout/coverage mở rộng khi đủ đầu vào. Rule score là MVP; ML chỉ khi đủ mẫu và nhãn.

## Bộ tài liệu để triển khai

- [SRS: yêu cầu](../initial-docs/SRS-FDP-01.md).
- [Đề cương: giả thuyết, nhãn và phương pháp](../research-design.md).
- [SDD: kiến trúc và schema](../initial-docs/SDD-FDP-01.md).
- [PP: kế hoạch 13 tuần](../initial-docs/PP-FDP-01.md).
- [TP: kiểm thử và đánh giá](../initial-docs/TP-FDP-01.md).

Bộ trên là nguồn quyết định phạm vi. Bản tổng hợp này không định nghĩa yêu cầu riêng.

