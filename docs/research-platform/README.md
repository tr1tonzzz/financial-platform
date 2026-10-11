# Hệ thống phân tích lợi nhuận dòng tiền và cổ tức tiền mặt

**Phạm vi/stack hiện hành:** HPG/VNM/FPT, BCTC năm 2023–2025; OCR chính PaddleOCR. [Quyết định, manifest và trạng thái](31-chot-pham-vi-va-stack-paddleocr.md). Chưa có bằng chứng Paddle chạy trong project.

**Đánh giá sau bản vẽ 5 UC:** [chức năng đã hỗ trợ người đầu tư đến đâu?](37-danh-gia-muc-do-ho-tro-nha-dau-tu.md) phân biệt demo/danh mục/phạm vi thực hiện, chỉ rõ phần cần làm sâu trong UC-2/5, kèm dữ liệu, công sức và tác vụ kiểm chứng. [Nghiên cứu bổ sung 12 repo/32 tệp mã](../research-investor-support/README.md) chọn từ khảo sát 36 repo trước; chưa chạy platform nguồn. Các gói bổ sung chưa thay SRS hoặc lịch 195 giờ v6.

**Cập nhật mới nhất 11/10/2026:** đã loại A04 và các yêu cầu sàng lọc theo người thực hiện. [Yêu cầu chức năng v2.0](27-yeu-cau-chuc-nang-va-vi-du.md) tổ chức5 nhóm chính (khai thác, phân tích, so sánh, theo dõi, cổ tức) và2 hướng mở rộng (danh mục, kịch bản/định giá),38 chức năng nhỏ có mục đích/ví dụ. Người dùng chính là người theo dõi tài chính doanh nghiệp/đầu tư; thu/trích/duyệt là nền hỗ trợ.

**Nghiên cứu GitHub rộng:** [36 repository ưu tiên sao cao](../research-high-star-finance/README.md),25 repo ≥3.000 sao;35 README và mã chọn lọc17 repo,87 tệp nguồn/34 tham chiếu mã. [Bảng khảo sát](../research-high-star-finance/01-khao-sat-repository.md), [minh chứng](../research-high-star-finance/02-minh-chung-ma-va-bai-hoc.md), [khả thi/thứ tự](../research-high-star-finance/03-kha-thi-va-thu-tu-thuc-hien.md). Chưa cài/chạy các nền tảng nguồn.

**Đặc tả hiện hành:** [SRS v3.3 dự thảo](22-srs-dac-ta-yeu-cau-phan-mem.md) ghi CR-AN-03 tại mục18, rút FR29/FR30/D09/D10, còn91 yêu cầu/51 tình huống dự kiến;5BUC nền giữ truy vết. Các chức năng mới trong danh mục vẫn là ứng viên. Wordv3.1 và kế hoạch167 giờ là baseline trước cập nhật;64–98 giờ của CR-DIV-02 cũ cần tính lại. Chưa nghiệm thu ứng dụng hoặc phê duyệt giảng viên.

**Bằng chứng trước:** [G02/G03 và phần lưu hồ sơ](../research-dividend-functions/README.md) có ca DHG/FPT và20 tests prototype; screening G01 đã rút. [Hướng nền tảng dữ liệu](../research-financial-platform-direction/README.md) được kế thừa theo quyết định mới.

**Baseline hướng kết hợp ngày 05/10/2026 (được kế thừa trong v3.3):** Xây dựng hệ thống thu thập, chuẩn hóa và phân tích lợi nhuận, dòng tiền kinh doanh trong mối liên hệ với cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam. Lợi nhuận và khả năng chuyển thành tiền là trục, cổ tức là lớp đối chiếu. [SRS hiện hành kế thừa v3.1](22-srs-dac-ta-yeu-cau-phan-mem.md) đã tích hợp CR-PCD-01: tối thiểu một ca cầu nối CFO, mục tiêu1–3 sau gate; 83 mã yêu cầu/42 tình huống dự kiến. [Kế hoạch v3](04-ke-hoach-13-tuan.md) và checklist cùng JSON có quỹ dự toán143+24=167 giờ; chưa xác nhận tăng thời gian thực. Quyết định giữ tên/extension chưa tích hợp ngày04/10 bên dưới được thay bằng cập nhật này. Chưa có phê duyệt giảng viên hoặc phần mềm hoàn chỉnh.

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

[Yêu cầu chức năng — mục đích và ví dụ dễ hiểu](27-yeu-cau-chuc-nang-va-vi-du.md): tài liệu riêng tổ chức5 nhóm chính/2 hướng mở rộng→38 chức năng nhỏ; mục đích, ví dụ, dữ liệu và trạng thái.

[Nghiên cứu lần hai và quyết định cuối](20-nghien-cuu-lan-hai-va-chot-de-tai.md): đọc để biết phần giao nhau với prior art, tám nhánh và hướng chốt; [sổ 21 nguồn](21-so-nguon-nghien-cuu-lan-hai.md). Quyết định liên thông ở đây thay ưu tiên dự đoán trong hồ sơ khảo sát trước.

[Giải thích dễ hiểu các chức năng và dữ liệu cụ thể](17-giai-thich-chuc-nang-va-du-lieu.md): đọc trước nếu cần hình dung hệ thống làm gì, lấy số ở đâu và giải quyết vấn đề nào.

[Nhập môn tài chính cho người chưa có nền tảng](18-nhap-mon-tai-chinh-cho-du-an.md): giải thích ý nghĩa sáu chỉ tiêu, cổ tức, các tỷ số và quan hệ bằng ví dụ cửa hàng, có câu hỏi tự kiểm tra.

[Đánh giá phạm vi, tính mới và các tên đề xuất](19-danh-gia-pham-vi-tinh-moi-va-ten-de-tai.md): khảo sát ngày 04/10/2026, phân biệt đóng góp kỹ thuật với ý tưởng tài chính đã có; chưa tự đổi tên hiện hành.

1. [Quyết định chọn ngách](01-so-sanh-va-quyet-dinh.md).
2. [SRS-FAP-01 v3.3 hiện hành](22-srs-dac-ta-yeu-cau-phan-mem.md), [bản Word](reports/SRS-FAP-01-v3.1.docx); [bài toán và nhu cầu P/US/PF/AN](02-de-tai-va-srs.md), [ý tưởng để trình bày](16-y-tuong-va-cau-chuyen-nguoi-dung.md).
3. [Phương pháp thu thập và xử lý](11-phuong-phap-thu-thap-va-xu-ly.md).
4. [Tài chính và từ điển](12-kien-thuc-tai-chinh-va-tu-dien.md).
5. [Kiến trúc và schema](03-kien-truc-va-du-lieu.md).
6. [Ghép sự kiện và phân tích](13-ghep-co-tuc-va-phan-tich.md).
7. [Kế hoạch học/làm](04-ke-hoach-13-tuan.md), [lộ trình học](05-lo-trinh-hoc.md).
8. [Đánh giá](06-danh-gia-va-nghiem-thu.md), [báo cáo tuần](07-bao-cao-hang-tuan.md).
9. [Bảo vệ](08-chuan-bi-bao-ve.md), [tốt nghiệp](09-lien-thong-tot-nghiep.md).
10. [Sổ nguồn](10-so-nguon.md), [backlog và quyết định](14-backlog-va-quyet-dinh.md).

[Các bản Word và slide](reports/README.md): Word v3.1 là bản lưu trước CR-DIV-02/CR-AN-03, chưa đồng bộ SRS v3.3; báo cáo đề xuất/slide cũ chưa được tái tạo.

## Bằng chứng đã có

[Danh sách doanh nghiệp đã khảo sát](30-danh-sach-doanh-nghiep-de-chon-pham-vi.md): chín ứng viên, nguồn chính thức và giới hạn so sánh; quyết định sau khảo sát đã chốt HPG/VNM/FPT tại tài liệu 31.

**Kiểm tiến độ và kế hoạch mới 11/10:** [UC-F01/02/03/05 trước, UC-F04 sau](28-ke-hoach-thuc-hien-uc-1-2-3-5.md), kèm [danh mục dữ liệu cần thu](29-du-lieu-can-thu-thap-cho-uc-1-2-3-5.md). Có crawler/OCR/phép tính prototype; chưa có mã ứng dụng trong `src`. Lập mốc demo từ dữ liệu đã duyệt, bảng/biểu đồ, so sánh đến hồ sơ cổ tức; không tick tiến độ chỉ vì đã có đặc tả.

Crawler mới tự phát hiện/tải 8 PDF năm 2025/bán niên 2026 của HPG, DHG, VHC, HPA; chạy lại 8 phản hồi 304; 13 test offline pass. Có 4 file dùng host robots trả 403, ghi rõ bounded probe, không đánh dấu Allow. Khảo sát OCR cũ đối chiếu sáu trường ở hai PDF, chưa gold độc lập. Bốn HTML cổ tức VNM/DHG có năm thành phần năm lợi nhuận; chưa chứng minh lịch sử năm đủ hoặc đã thực trả.

Chưa có ứng dụng hoàn chỉnh, dataset lịch sử ghép đầy đủ hoặc benchmark độc lập. Prototype chưa tự thu 2023–2024; cần mở cấu hình kỳ và adapter cổ tức. Đọc [bằng chứng crawl](../research-crawl-methods/README.md) và [sự kiện](../research-recent-data/dividend-event-examples.json).

## Tài liệu các hướng đã khảo sát

Hồ sơ A1–A7 trong ideas là thư viện tham khảo. [A2](ideas/a2-bctc-co-tuc/01-y-tuong-va-kha-thi.md) là hướng chọn; các hướng khác không triển khai song song. Bản A1 trước được giữ ở [snapshot lịch sử](history/a1-2026-10-03.zip). Quy tắc MVP mới nằm trong bộ này; các ngưỡng cảnh báo/nhãn dự báo 12 tháng của tài liệu cũ không tự áp dụng.

## Theo dõi thực hiện và báo cáo

**Thiết kế trước năm UC:** [màn hình và luồng sử dụng](36-thiet-ke-man-hinh-5-uc.md), [bản xem tương tác](../design-5-uc/index.html). Có 10 màn hình minh họa; Figma tạo tệp nhưng canvas bị chặn bởi hạn mức Starter, bộ SVG được cung cấp để nhập chỉnh sửa.

**Chi tiết UC-1 theo Báo cáo 2:** [tuần 1 — một báo cáo và tích hợp Paddle](33-ke-hoach-chi-tiet-tuan-01.md), [tuần 2 — kho nhiều kỳ, duyệt và phiên bản](34-ke-hoach-chi-tiet-tuan-02.md), [từ điển sáu metrics và dữ liệu bổ sung](35-dac-ta-metrics-tu-bao-cao-02.md). Có phân rã F01.1–F01.6, nhiệm vụ từng buổi, bộ kiểm và nội dung Word/slide; đây là kế hoạch, chưa là kết quả triển khai.

**Điều chỉnh hiện hành v6:** [tuần này làm UC-1 cơ bản và ghép Paddle](33-ke-hoach-chi-tiet-tuan-01.md), tái sử dụng tải/text/render đã thử. [Kế hoạch 10 tuần](32-ke-hoach-10-tuan-tiep-theo.md) và [HTML đang dùng](checklist-10-tuan-v4.html) có gợi ý Word/slide/demo cho cả 10 tuần; giữ tên file v4 nhưng nội dung đã cập nhật v6.

**Lịch thực hiện hiện hành:** [10 tuần tiếp theo v6](32-ke-hoach-10-tuan-tiep-theo.md), [checklist HTML mới](checklist-10-tuan-v4.html). Demo cơ bản UC-1/2/3 cuối tuần 4, hoàn thiện ba mã tuần 5; UC-5 tuần 6–8, UC-4 có điều kiện tuần 9. Kế hoạch/checklist 13 tuần bên dưới giữ làm lịch sử, không là lịch tiếp theo và không chuyển tick tự động.

[Bộ tài liệu và bài tập tuần 1](24-tai-lieu-va-bai-tap-tuan-01.md): thứ tự đọc, nguồn chính thức, BCTC/notice DHG mẫu và [khung trao đổi với thầy](reports/tuan-01-khung-trao-doi-voi-thay.md). Mẫu chuẩn bị chưa là tiến độ đã hoàn thành.

**Bắt đầu làm theo:** [kế hoạch 10 tuần v6](32-ke-hoach-10-tuan-tiep-theo.md) → [checklist HTML hiện hành](checklist-10-tuan-v4.html). [Hướng dẫn minh chứng](23-bat-dau-va-minh-chung-thuc-hien.md) còn dùng làm mẫu. [Kế hoạch13 tuần v3](04-ke-hoach-13-tuan.md)/[checklist v3](checklist-13-tuan.html) giữ baseline lịch sử 83 mã/42 TC/167 giờ; chưa có app hoàn chỉnh.

- [Checklist HTML 13 tuần](checklist-13-tuan.html): đánh dấu, nhật ký, lưu trình duyệt, xuất/nhập JSON và ngày bắt đầu.
- [Khung Word/slide hai tuần](07-bao-cao-hang-tuan.md), [gợi ý bảy mốc](goi-y-noi-dung-7-dot-bao-cao.md), [mẫu điền](mau-bao-cao-hai-tuan.md).
- [Một sách nền tảng và cách đọc](15-sach-nen-tang-va-cach-doc.md).

Nhịp mới: cuối tuần 2/4/6/8/10/12 báo cáo; tuần 13 tổng kết. Nhật ký vẫn theo từng tuần.

[Nhật ký đổi hướng và quan hệ tài liệu](25-nhat-ky-cap-nhat-huong-ket-hop.md): phạm vi thay đổi, giờ dự toán, bản lịch sử và các bản xuất cũ.
