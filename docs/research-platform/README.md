# Hệ thống phân tích lợi nhuận dòng tiền và cổ tức tiền mặt

**Hướng hiện hành cập nhật 05/10/2026:** Xây dựng hệ thống thu thập, chuẩn hóa và phân tích lợi nhuận, dòng tiền kinh doanh trong mối liên hệ với cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam. Lợi nhuận và khả năng chuyển thành tiền là trục, cổ tức là lớp đối chiếu. [SRS v3.1](22-srs-dac-ta-yeu-cau-phan-mem.md) đã tích hợp CR-PCD-01: tối thiểu một ca cầu nối CFO, mục tiêu1–3 sau gate; 83 mã yêu cầu/42 tình huống dự kiến. [Kế hoạch v3](04-ke-hoach-13-tuan.md) và checklist cùng JSON có quỹ dự toán143+24=167 giờ; chưa xác nhận tăng thời gian thực. Quyết định giữ tên/extension chưa tích hợp ngày04/10 bên dưới được thay bằng cập nhật này. Chưa có phê duyệt giảng viên hoặc phần mềm hoàn chỉnh.

**Hướng hiện hành cập nhật ngày 05/10/2026:**
**Xây dựng hệ thống thu thập, chuẩn hóa và phân tích lợi nhuận, dòng tiền kinh doanh trong mối liên hệ với cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam.**

Đây là hướng triển khai duy nhất. Năng lực phân tích BCTC có truy vết của A1 được tái sử dụng làm nền kỹ thuật cho ngách A2. Tên chính thức/rubric còn cần trao đổi với thầy; chưa có bằng chứng giảng viên đã phê duyệt.

## Phạm vi và quyết định chính

- Project: tự thu thập BCTC và thông báo cổ tức, trích/kiểm định/duyệt, ghép theo năm lợi nhuận, phân tích mô tả và ứng dụng truy nguồn.
- Đích dữ liệu cổ tức: **DPS tiền mặt được công bố**; ngày thanh toán theo lịch là trường riêng, xác nhận thực trả chỉ lưu khi có bằng chứng.
- Sáu trường BCTC lõi: LNST tổng, CFO, tiền và tương đương tiền, tổng tài sản, nợ phải trả, tổng VCSH. Doanh thu/EPS/phần LNST cổ đông mẹ/ngắn hạn là mở rộng có điều kiện.
- Pilot: 3 doanh nghiệp × 2023–2025 = 9 BCTC năm; chọn nguồn đủ rõ. Mục tiêu sau gate tuần 4: 5–8 doanh nghiệp, 15–24 BCTC năm. Cổ tức phải rà các đợt liên quan năm lợi nhuận, kể cả công bố ở năm khác.
- Ưu tiên doanh nghiệp phi tài chính; hợp nhất nếu có, cấp doanh nghiệp nếu thực sự không lập hợp nhất và đã xác nhận. Mỗi doanh nghiệp có series/scope riêng; không trộn scope trong tỷ số hoặc tương quan gộp.
- Một case cập nhật 2026 nếu đủ giờ; chưa cần mọi quý, giá thị trường, yield, TTM hoặc điểm bền vững tổng hợp.
- Chốt lại ngày **04/10/2026 sau nghiên cứu lần hai**: giữ nền pilot/sáu trường; cập nhật 05/10 dùng tên theo hướng kết hợp và thêm cầu nối CFO theo ca. Hướng đồ án ưu tiên là đối chiếu phiên bản/ảnh hưởng tới kết quả; dự đoán cổ tức là tùy chọn sau gate dữ liệu. Project hiện tại không cần ML/RAG.

Kế hoạch v3 giữ 13 tuần, dự toán 143 giờ nền + 24 giờ cầu nối = 167 giờ; phải đo/quyết định lại ở G4 vì quỹ 10–12 giờ/tuần trước đây chưa đủ cho toàn bộ phần thêm. Chưa gắn lịch học kỳ hoặc tự gửi báo cáo.

## Đọc theo thứ tự

[Nghiên cứu lần hai và quyết định cuối](20-nghien-cuu-lan-hai-va-chot-de-tai.md): đọc để biết phần giao nhau với prior art, tám nhánh và hướng chốt; [sổ 21 nguồn](21-so-nguon-nghien-cuu-lan-hai.md). Quyết định liên thông ở đây thay ưu tiên dự đoán trong hồ sơ khảo sát trước.

[Giải thích dễ hiểu các chức năng và dữ liệu cụ thể](17-giai-thich-chuc-nang-va-du-lieu.md): đọc trước nếu cần hình dung hệ thống làm gì, lấy số ở đâu và giải quyết vấn đề nào.

[Nhập môn tài chính cho người chưa có nền tảng](18-nhap-mon-tai-chinh-cho-du-an.md): giải thích ý nghĩa sáu chỉ tiêu, cổ tức, các tỷ số và quan hệ bằng ví dụ cửa hàng, có câu hỏi tự kiểm tra.

[Đánh giá phạm vi, tính mới và các tên đề xuất](19-danh-gia-pham-vi-tinh-moi-va-ten-de-tai.md): khảo sát ngày 04/10/2026, phân biệt đóng góp kỹ thuật với ý tưởng tài chính đã có; chưa tự đổi tên hiện hành.

1. [Quyết định chọn ngách](01-so-sanh-va-quyet-dinh.md).
2. [SRS-FAP-01 v3.1 đầy đủ](22-srs-dac-ta-yeu-cau-phan-mem.md), [bản Word](reports/SRS-FAP-01-v3.1.docx); [bài toán và nhu cầu P/US/PF/AN](02-de-tai-va-srs.md), [ý tưởng để trình bày](16-y-tuong-va-cau-chuyen-nguoi-dung.md).
3. [Phương pháp thu thập và xử lý](11-phuong-phap-thu-thap-va-xu-ly.md).
4. [Tài chính và từ điển](12-kien-thuc-tai-chinh-va-tu-dien.md).
5. [Kiến trúc và schema](03-kien-truc-va-du-lieu.md).
6. [Ghép sự kiện và phân tích](13-ghep-co-tuc-va-phan-tich.md).
7. [Kế hoạch học/làm](04-ke-hoach-13-tuan.md), [lộ trình học](05-lo-trinh-hoc.md).
8. [Đánh giá](06-danh-gia-va-nghiem-thu.md), [báo cáo tuần](07-bao-cao-hang-tuan.md).
9. [Bảo vệ](08-chuan-bi-bao-ve.md), [tốt nghiệp](09-lien-thong-tot-nghiep.md).
10. [Sổ nguồn](10-so-nguon.md), [backlog và quyết định](14-backlog-va-quyet-dinh.md).

[Các bản Word và slide](reports/README.md): SRS Word v3.0 đồng bộ với đặc tả mới; báo cáo đề xuất/slide cũ chưa được tái tạo.

## Bằng chứng đã có

Crawler mới tự phát hiện/tải 8 PDF năm 2025/bán niên 2026 của HPG, DHG, VHC, HPA; chạy lại 8 phản hồi 304; 13 test offline pass. Có 4 file dùng host robots trả 403, ghi rõ bounded probe, không đánh dấu Allow. Khảo sát OCR cũ đối chiếu sáu trường ở hai PDF, chưa gold độc lập. Bốn HTML cổ tức VNM/DHG có năm thành phần năm lợi nhuận; chưa chứng minh lịch sử năm đủ hoặc đã thực trả.

Chưa có ứng dụng hoàn chỉnh, dataset lịch sử ghép đầy đủ hoặc benchmark độc lập. Prototype chưa tự thu 2023–2024; cần mở cấu hình kỳ và adapter cổ tức. Đọc [bằng chứng crawl](../research-crawl-methods/README.md) và [sự kiện](../research-recent-data/dividend-event-examples.json).

## Tài liệu các hướng đã khảo sát

Hồ sơ A1–A7 trong ideas là thư viện tham khảo. [A2](ideas/a2-bctc-co-tuc/01-y-tuong-va-kha-thi.md) là hướng chọn; các hướng khác không triển khai song song. Bản A1 trước được giữ ở [snapshot lịch sử](history/a1-2026-10-03.zip). Quy tắc MVP mới nằm trong bộ này; các ngưỡng cảnh báo/nhãn dự báo 12 tháng của tài liệu cũ không tự áp dụng.

## Theo dõi thực hiện và báo cáo

[Bộ tài liệu và bài tập tuần 1](24-tai-lieu-va-bai-tap-tuan-01.md): thứ tự đọc, nguồn chính thức, BCTC/notice DHG mẫu và [khung trao đổi với thầy](reports/tuan-01-khung-trao-doi-voi-thay.md). Mẫu chuẩn bị chưa là tiến độ đã hoàn thành.

**Bắt đầu làm theo:** [Hướng dẫn buổi đầu và mẫu minh chứng](23-bat-dau-va-minh-chung-thuc-hien.md) → [kế hoạch13tuần v3](04-ke-hoach-13-tuan.md) → [checklist v3](checklist-13-tuan.html). Kế hoạch đã phân bổ83 mã yêu cầu/42 tình huống SRS v3.1, 78việc/167giờ dự toán, outputs/gates và việc restore/performance/safety; các module/output là mục tiêu cần thực hiện, chưa có app hoàn chỉnh.

- [Checklist HTML 13 tuần](checklist-13-tuan.html): đánh dấu, nhật ký, lưu trình duyệt, xuất/nhập JSON và ngày bắt đầu.
- [Khung Word/slide hai tuần](07-bao-cao-hang-tuan.md), [gợi ý bảy mốc](goi-y-noi-dung-7-dot-bao-cao.md), [mẫu điền](mau-bao-cao-hai-tuan.md).
- [Một sách nền tảng và cách đọc](15-sach-nen-tang-va-cach-doc.md).

Nhịp mới: cuối tuần 2/4/6/8/10/12 báo cáo; tuần 13 tổng kết. Nhật ký vẫn theo từng tuần.

[Nhật ký đổi hướng và quan hệ tài liệu](25-nhat-ky-cap-nhat-huong-ket-hop.md): phạm vi thay đổi, giờ dự toán, bản lịch sử và các bản xuất cũ.
