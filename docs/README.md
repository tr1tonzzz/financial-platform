# Đề tài hiện hành và tài liệu triển khai

**Báo cáo 1 đang soạn:** [bối cảnh đề tài, hướng project và ví dụ Vinamilk quý I/2026](research-platform/reports/dot-01-tuan-01-02/bao-cao-01.md), kèm [phụ lục số liệu/phép tính](research-platform/reports/dot-01-tuan-01-02/vi-du-phan-tich-vnm.md). Theo yêu cầu hiện tại, chỉ làm tài liệu Markdown; chưa cần các bản xuất Word/slide/PDF.

**Nghiên cứu giá trị sử dụng 05/10/2026:** [vì sao liên kết BCTC với cổ tức có ích](research-platform/reports/dot-01-tuan-01-02/co-so-hoc-thuat-va-gia-tri-su-dung.md), có 10 nghiên cứu, tài liệu nghề nghiệp/pháp lý và ma trận câu hỏi người dùng → dữ liệu → kết quả → lợi ích. Phân biệt tác vụ pilot với đánh giá payout/FCFE cần thêm nguồn; chưa là phạm vi SRS mở rộng đã chốt.

**Hướng hiện hành cập nhật 05/10/2026:** Xây dựng hệ thống thu thập, chuẩn hóa và phân tích lợi nhuận, dòng tiền kinh doanh trong mối liên hệ với cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam. Lợi nhuận và khả năng chuyển thành tiền là trục, cổ tức là lớp đối chiếu. [SRS v3.1](research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md) đã tích hợp CR-PCD-01: tối thiểu một ca cầu nối CFO, mục tiêu1–3 sau gate; 83 mã yêu cầu/42 tình huống dự kiến. [Kế hoạch v3](research-platform/04-ke-hoach-13-tuan.md) và checklist cùng JSON có quỹ dự toán143+24=167 giờ; chưa xác nhận tăng thời gian thực. Quyết định giữ tên/extension chưa tích hợp ngày04/10 bên dưới được thay bằng cập nhật này. Chưa có phê duyệt giảng viên hoặc phần mềm hoàn chỉnh.

Hướng ban đầu ngày **03/10/2026**, cập nhật diễn đạt và chiều sâu ngày **05/10/2026**:
**Xây dựng hệ thống thu thập, chuẩn hóa và phân tích lợi nhuận, dòng tiền kinh doanh trong mối liên hệ với cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam.**

Project làm thu thập, kiểm định, phân tích mô tả và ứng dụng truy nguồn. Nghiên cứu lần hai ngày **04/10/2026** chốt giữ nền kiểm định/truy vết và vòng đời cổ tức; cập nhật 05/10 thêm cầu nối CFO theo ca. Hướng đồ án ưu tiên là đối chiếu phiên bản và ảnh hưởng tới kết quả; dự đoán là tùy chọn sau gate dữ liệu. Tên đăng ký/rubric cần trao đổi với giảng viên; sự lựa chọn của người thực hiện không được ghi thành phê duyệt của thầy.

## Tài liệu chính thức

[Bộ tài liệu hiện hành](research-platform/README.md) là đầu mối triển khai duy nhất.

1. [SRS-FAP-01 v3.1](research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md), [Word chỉnh sửa được](research-platform/reports/SRS-FAP-01-v3.1.docx); [bài toán và nhu cầu nền](research-platform/02-de-tai-va-srs.md).
2. [Phương pháp thu thập và xử lý đã thống nhất](research-platform/11-phuong-phap-thu-thap-va-xu-ly.md).
3. [Kiến thức tài chính và từ điển dữ liệu](research-platform/12-kien-thuc-tai-chinh-va-tu-dien.md).
4. [Thiết kế kỹ thuật dữ liệu](research-platform/03-kien-truc-va-du-lieu.md).
5. [Quy tắc ghép cổ tức và phân tích](research-platform/13-ghep-co-tuc-va-phan-tich.md).
6. [Kế hoạch 13 tuần](research-platform/04-ke-hoach-13-tuan.md).
7. [Đánh giá và nghiệm thu](research-platform/06-danh-gia-va-nghiem-thu.md).
8. [Báo cáo Word và slide](research-platform/07-bao-cao-hang-tuan.md).
9. [Backlog bắt đầu triển khai](research-platform/14-backlog-va-quyet-dinh.md).
10. [Ý tưởng, câu chuyện nền và nội dung trình bày với giảng viên](research-platform/16-y-tuong-va-cau-chuyen-nguoi-dung.md): mục đích, phân tích cụ thể, vấn đề thực tế và hướng tốt nghiệp; chi tiết yêu cầu và truy vết nghiệm thu trong SRS v3.0.
11. [Giải thích dễ hiểu các chức năng và dữ liệu cụ thể](research-platform/17-giai-thich-chuc-nang-va-du-lieu.md): từng chức năng có đầu vào, xử lý, đầu ra, vấn đề giải quyết và ví dụ xuyên suốt.
12. [Nhập môn tài chính để hiểu dữ liệu và quan hệ trong dự án](research-platform/18-nhap-mon-tai-chinh-cho-du-an.md): từ lợi nhuận–tiền–tài sản tới cổ tức và các tỷ số, dành cho người chưa có nền tảng tài chính.
13. [Đánh giá phạm vi, tính mới và lựa chọn tên đề tài](research-platform/19-danh-gia-pham-vi-tinh-moi-va-ten-de-tai.md): nguồn nghiên cứu/sản phẩm liên quan, chiều sâu project–đồ án và năm tên đề xuất.
14. [Nghiên cứu lần hai và chốt đề tài](research-platform/20-nghien-cuu-lan-hai-va-chot-de-tai.md): tám nhánh, ca nghiệp vụ thực tế, lựa chọn cuối và phạm vi project–đồ án; [sổ nguồn](research-platform/21-so-nguon-nghien-cuu-lan-hai.md) ghi rõ mức truy cập bằng chứng.

## Bằng chứng và hồ sơ tham khảo

- [Nghiên cứu kết hợp lợi nhuận–CFO trong mối liên hệ với cổ tức (04/10/2026)](research-profit-cash-dividend/README.md): đánh giá khả thi, cơ sở học thuật, nghiệp vụ, workflow, đặc tả bổ sung, kế hoạch/kiểm thử và ca thật DHG/VNM. Đây là cơ sở nghiên cứu cầu nối CFO đã tích hợp vào mục15 SRS v3.1.
- [Crawler BCTC](research-crawl-methods/README.md): prototype tìm/tải 8 PDF, cập nhật 304, 13 test; chưa là ứng dụng đầy đủ.
- [Nguồn và sự kiện gần hiện tại](research-recent-data/README.md): PDF/OCR và bốn thông báo cổ tức, chưa có lịch sử cổ tức đầy đủ.
- [Thiết kế phân tích hiện hành](research-design.md): chỉ mục phương pháp mới.
- [Nghiên cứu phát triển trước](research-development/README.md), [các phương án N1–N4](research-options/README.md), các hồ sơ trong initial-docs: tham khảo/lịch sử, không đưa ngưỡng cảnh báo hoặc dự báo cũ thành nghĩa vụ project.
- [Snapshot hướng sức khỏe tài chính A1](research-platform/history/a1-2026-10-03.zip): lưu quyết định trước, gồm Word/slide cũ.

Scope hiện hành: pilot 3 công ty × 3 năm; mục tiêu 5–8 công ty, 2023–2025 sau gate công sức. Sáu chỉ tiêu BCTC lõi và sự kiện cổ tức tiền mặt. Các mức 10 công ty/chín trường/ML trong tài liệu cũ không còn là cam kết hiện hành.

## Theo dõi thực hiện và báo cáo

Để bắt đầu: [Hướng dẫn buổi đầu/mẫu minh chứng](research-platform/23-bat-dau-va-minh-chung-thuc-hien.md) và [kế hoạch13tuần v3 theo SRS v3.0](research-platform/04-ke-hoach-13-tuan.md), đồng bộ với checklist dưới đây.

- [Checklist HTML 13 tuần](research-platform/checklist-13-tuan.html): đánh dấu, nhật ký, lưu trình duyệt, xuất/nhập JSON và ngày bắt đầu.
- [Khung Word/slide hai tuần](research-platform/07-bao-cao-hang-tuan.md), [gợi ý bảy mốc](research-platform/goi-y-noi-dung-7-dot-bao-cao.md), [mẫu điền](research-platform/mau-bao-cao-hai-tuan.md).
- [Một sách nền tảng và cách đọc](research-platform/15-sach-nen-tang-va-cach-doc.md).

Nhịp mới: cuối tuần 2/4/6/8/10/12 báo cáo; tuần 13 tổng kết. Nhật ký vẫn theo từng tuần.

[Nhật ký đổi hướng và quan hệ tài liệu](research-platform/25-nhat-ky-cap-nhat-huong-ket-hop.md): phạm vi thay đổi, giờ dự toán, bản lịch sử và các bản xuất cũ.
