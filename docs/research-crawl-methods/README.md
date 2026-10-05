# Tự thu thập BCTC Việt Nam gần thời điểm hiện tại

Ngày khảo sát: **03/10/2026**. Áp dụng cho đề tài hiện hành: **Hệ thống thu thập và phân tích lợi nhuận, dòng tiền và cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam**.

**Kết luận: khả thi với danh sách doanh nghiệp và nguồn đã chọn.** Đã viết và chạy prototype tự đọc danh mục IR, tìm link, lọc tài liệu và tải PDF; không nhập sẵn URL từng PDF, không lấy số liệu từ dataset có sẵn. Thu được **8 BCTC mục tiêu của 4 doanh nghiệp: năm 2025 và bán niên 2026**, tổng **423 trang, 76.118.458 byte**. HPA bổ sung hai báo cáo chưa có trong khảo sát trước. Chạy lại kiểm tra trực tiếp nguồn, cả 8 file trả HTTP 304, kho vẫn có 8 URL và 8 phiên bản.

Đây là bằng chứng về **thu thập và cập nhật file**, chưa chứng minh trích tự động đủ sáu trường lõi đúng trên tám báo cáo. Trong mẫu mới, mỗi PDF được thử đọc 12 trang đầu bằng pypdf; **0/96 trang có trên 100 ký tự text**. Không được viết rằng toàn bộ 423 trang đã kiểm tra text hoặc rằng mọi BCTC Việt Nam đều là bản scan.

Các giới hạn cần đọc cùng kết quả: nguồn được chọn có chủ đích; adapter và classifier phát triển trên các danh mục này; chưa có holdout đo độ phủ toàn thị trường. Bốn file HPG/HPA dùng host `file.hoaphat.com.vn` có robots.txt trả 403: đã chạy chế độ thử hữu hạn, ghi rõ chính sách chưa xác định, không ghi là được robots cho phép. DHG/VHC có robots đọc được và không chặn đường dẫn đã chọn. Chế độ mặc định của script bỏ qua chính sách chưa xác định.

## Các phần nghiên cứu riêng

1. [Tính khả thi và lựa chọn nguồn](01-kha-thi-va-nguon.md).
2. [Kỹ thuật crawl HTTP, adapter và phân trang](02-ky-thuat-crawl-http-va-phan-trang.md).
3. [Kiến thức tài chính cần nhận diện khi thu thập](03-kien-thuc-tai-chinh-cho-crawler.md).
4. [Khảo sát PDF, OCR và trích xuất trước](04-pdf-ocr-va-trich-chin-truong.md).
5. [Cập nhật, phiên bản và truy vết](05-cap-nhat-phien-ban-va-truy-vet.md).
6. [Thực nghiệm, bằng chứng và chạy lại](06-thuc-nghiem-va-tai-lap.md).
7. [Kế hoạch tích hợp và đóng góp IT](07-ke-hoach-tich-hop-va-dong-gop-it.md).
8. [Lỗi đã gặp và giới hạn còn lại](08-nhat-ky-loi-va-gioi-han.md).

[Bằng chứng JSON](crawl-evidence.json) lưu hai lần chạy cuối, URL/hash/headers/robots và xác nhận trang đầu hai PDF HPA. [Prototype](../../scripts/research/crawl_official_reports.py) và [13 kiểm thử offline](../../scripts/research/test_crawl_official_reports.py) là mã khảo sát, chưa là module ứng dụng hoàn chỉnh.

## Quyết định cho project

Tự thu thập từ nguồn chính thức là năng lực lõi. [Phương pháp hiện hành](../research-platform/11-phuong-phap-thu-thap-va-xu-ly.md) thay các scope/trường đề xuất cũ: sáu chỉ tiêu tài chính, cổ tức công bố theo năm lợi nhuận và timeline riêng. Cổ tức là phần bắt buộc của project.

Pilot 3 công ty × 2023–2025, 9 PDF năm và thông báo liên quan. Gate tuần 4 quyết định mở rộng 5–8 công ty; một ca cập nhật 2026 là tùy chọn. Collector BCTC hiện có mới cấu hình năm 2025/bán niên 2026; phải bổ sung lựa chọn kỳ. Bốn thông báo cổ tức là mẫu seed, chưa chứng minh tự tìm đầy đủ lịch sử. Các con số thực nghiệm và JSON được giữ nguyên.
