# Tích hợp tự thu thập vào project BCTC–cổ tức

Định hướng hiện hành ngày 03/10/2026. [SRS](../research-platform/02-de-tai-va-srs.md) là nguồn phạm vi; [backlog](../research-platform/14-backlog-va-quyet-dinh.md) phân biệt thử nghiệm đã có và phần phải viết.

1. Tái sử dụng collector danh mục IR, bổ sung cấu hình 2023–2025 và đăng ký nguồn. Giữ hành vi mặc định bỏ qua policy chưa rõ.
2. Xây discovery thông báo VSDC/IR có phân trang, ngày truy cập và ledger kiểm tra phạm vi. Mẫu seed không thay discovery.
3. Downloader dùng chung: kiểm tra HTTP/type/PDF, giới hạn tần suất, conditional GET, hash, phiên bản bất biến.
4. PDF text trước, OCR vie+eng khi cần; lưu candidates và vị trí nguồn, trích sáu trường rồi kiểm định/duyệt.
5. HTML thông báo chính → sự kiện và components theo năm lợi nhuận; xử lý sửa/hủy, tránh đếm trùng, xác minh share basis và coverage.
6. SQLite → snapshot doanh nghiệp–năm → Streamlit, timeline, chỉ số mô tả và export.

Đóng góp IT được đánh giá bằng khả năng tự tìm tài liệu, tải lặp không nhân bản, độ đúng trên holdout, kiểm thử sự kiện nhiều năm/sửa/hủy/thiếu dữ liệu và truy vết trên demo. [Lịch 13 tuần](../research-platform/04-ke-hoach-13-tuan.md) dành thời gian học và báo cáo tuần; không có nhiệm vụ dự đoán trong MVP.
