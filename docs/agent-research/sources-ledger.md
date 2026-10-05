# Sổ nguồn và bằng chứng

Chưa hoàn thành crawl pilot 10 doanh nghiệp. Ngày 03/10/2026 đã bổ sung khảo sát nhỏ và tổng quan tài liệu; trạng thái từng nguồn ở [sổ tham khảo](../research-development/02-so-tai-lieu-tham-khao.md), cách thực hiện và số liệu ở [khảo sát thực tế](../research-development/03-khao-sat-nguon-thuc-te.md).

| Nguồn/URL | Ngày kiểm tra | Phương pháp | Tài liệu/sự kiện lấy được | Lịch hay thực hiện? | Kết quả/giới hạn | File bằng chứng |
|---|---|---|---|---|---|---|
| [Vinamilk IFRS 2024](https://www.vinamilk.com.vn/bao-cao-thuong-nien/bao-cao/2024/doc/en/bctc-ifrs.pdf) | 03/10/2026 | Tải urllib HTTP 200, pdfplumber crop/text, render xem 3 trang | Sáu chỉ tiêu cột 2024 đã đối chiếu hình | Có dòng tổng chi cổ tức; chưa xác minh từng event | Một PDF IFRS, chưa rõ audit/available_at; không là cohort MVP | [Khảo sát](../research-development/03-khao-sat-nguon-thuc-te.md) |
| [VNM VSDC 174349](https://www.vsd.vn/vi/ad1/174349) | 03/10/2026 | Đọc HTML qua web | DPS và hai thành phần profit_year, lịch quyền/thanh toán | Lịch công bố | Tải local lỗi TLS; chưa xác nhận paid/coverage | [Khảo sát](../research-development/03-khao-sat-nguon-thuc-te.md) |
| [VSH VSDC 174490](https://www.vsd.vn/vi/ad/174490) | 03/10/2026 | Đọc HTML qua web | Amendment lịch thanh toán | Lịch công bố | Chưa đọc toàn chuỗi, local lỗi TLS | [Khảo sát](../research-development/03-khao-sat-nguon-thuc-te.md) |

Tài liệu học thuật ghi URL/DOI, nội dung liên quan đã đọc và phát biểu được hỗ trợ. URL xuất hiện trong hội thoại trước chưa tự động được coi là nguồn đã xác minh.

Nguồn F01–F05, M01–M03 và T01–T13 được ghi cùng mức độ đọc trong sổ tham khảo mới; F04/F05 nghiên cứu doanh nghiệp Việt Nam. Các URL FPT/HNX/SDT chưa truy cập đầy đủ được giữ là đầu mối, không đổi thành bằng chứng crawl thành công.

