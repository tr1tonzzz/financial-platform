# Rà soát kiến trúc kỹ thuật

Trạng thái: định hướng nghiên cứu, chưa kiểm chứng bằng pilot.

Thiết kế hiện hành tại [SDD](../initial-docs/SDD-FDP-01.md). Chưa tuyên bố đã triển khai.

Rà pipeline nguồn → raw → extract → normalize → validate/review → dividends → dataset → analytics → API/dashboard.

Kiểm tra schema nguồn và bằng chứng, ngày khả dụng, phiên bản, dedupe sự kiện, nhật ký sửa và snapshot. Chọn công cụ từ loại tài liệu pilot, tránh thêm OCR/trình duyệt tự động trước khi đo nhu cầu.

Đầu ra tiếp theo: module cần viết, thứ tự, test tương ứng TP, ước lượng công sức và đề xuất sửa SDD có lý do.

