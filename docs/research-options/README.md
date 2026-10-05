# Rà soát ý tưởng mới và lựa chọn đề tài

> **Trạng thái 03/10/2026 — hồ sơ khảo sát trước.** Project hiện hành tập trung thu thập, kiểm định và phân tích lợi nhuận–dòng tiền–cổ tức tiền mặt. Xem [SRS hiện hành](../research-platform/02-de-tai-va-srs.md) và [phương pháp thống nhất](../research-platform/11-phuong-phap-thu-thap-va-xu-ly.md). Các ngưỡng cảnh báo, dự báo, scope và lịch cũ bên dưới chỉ để tham khảo; không là yêu cầu MVP hiện hành.

Ngày rà soát: **03/10/2026**. Đây là kết luận thiết kế sau khi đọc tài liệu hiện hành và tra cứu bổ sung; chưa có kết quả thực nghiệm mới. Bộ này gồm **19 tài liệu Markdown**: trang so sánh này, bản chốt đề tài, sổ nguồn và bốn hồ sơ, mỗi hồ sơ bốn tài liệu riêng.

## 1. Kết luận lựa chọn

**Giữ đề tài BCTC–cổ tức tiền mặt Việt Nam. Ý tưởng đủ làm MVP và báo cáo nghiên cứu; chưa đủ bằng chứng để khẳng định khả thi trên toàn bộ mẫu hoặc có hiệu quả dự báo.** Không cần ghép tất cả hướng mới vào 13 tuần. Ưu tiên mở rộng cách giải thích lợi nhuận–dòng tiền trong các case study, nếu lấy được dữ liệu chi tiết.

Đọc [bản chốt đề tài](01-chot-y-tuong-de-tai.md) để biết tên chính thức, câu hỏi, phạm vi và kết quả cần nộp. [Sổ nguồn bổ sung](02-tai-lieu-va-co-so-lua-chon.md) ghi rõ phần đã đọc và phần chưa truy cập được.

## 2. Ý tưởng cũ và ý tưởng hiện hành khác nhau ở đâu?

[Ghi chú cũ](../report-docs/note.txt) mô tả tải dữ liệu SEC theo quý, mapping chỉ tiêu, kiểm tra chất lượng, lưu phiên bản, API, lọc/so sánh và đo hiệu năng. File không ghi tác giả; không đủ căn cứ coi mọi nội dung là lời thầy nói nguyên văn.

[SRS hiện hành](../initial-docs/SRS-FDP-01.md) đã chuyển bài toán sang BCTC và cổ tức Việt Nam. Có thể kế thừa staging, mapping, versioning và truy vấn theo thời điểm từ ghi chú cũ, nhưng phải thiết kế lại nguồn PDF/thông báo, đơn vị và ngữ nghĩa cổ tức. SEC là nguồn dữ liệu Mỹ; không dùng nó để thay dataset Việt Nam trong đề tài đã chốt.

Năm hồ sơ trong [bộ nghiên cứu trước](../research-development/README.md) chủ yếu là các thành phần của một hệ thống. Bốn hồ sơ dưới đây xét thêm câu hỏi nghiên cứu, cách diễn giải hoặc khả năng chuyển trọng tâm đề tài.

## 3. Bốn hướng có tiềm năng

| Hướng | Câu hỏi/đầu ra mới | Dữ liệu tăng thêm | Đánh giá phù hợp phạm vi hiện tại | Quyết định |
|---|---|---|---|---|
| N1. Giải thích lợi nhuận–dòng tiền | Vì sao có lãi nhưng tiền từ kinh doanh yếu? Phần nào đến từ vốn lưu động? | Các dòng điều chỉnh CFO; doanh thu, giá vốn, phải thu, tồn kho, phải trả | Gần bài toán lõi nhất; có thể làm ít case trước | Ưu tiên bổ sung có điều kiện |
| N2. Mô phỏng sức chịu đựng cổ tức | Sau cú giảm dòng tiền, đầu tư và trả nợ, còn bao nhiêu tiền nếu giữ mức chi trả? | CapEx tiền mặt, nợ gốc, vốn huy động, hạn chế sử dụng tiền, tổng tiền cổ tức | Demo rõ, nhưng dễ tạo cảm giác dự báo quá chắc chắn | Sau lõi dữ liệu; chỉ case có đủ đầu vào |
| N3. Công ty mẹ và hợp nhất | Tiền trong tập đoàn có phản ánh nguồn tiền ở đơn vị thực chi cổ tức không? | BCTC riêng và hợp nhất cùng kỳ; thuyết minh đầu tư, cổ tức nhận, hạn chế chuyển tiền | Có chiều sâu tài chính, chi phí đọc thuyết minh cao | Case chuyên sâu; không mở toàn mẫu |
| N4. Đối chiếu phiên bản BCTC | Số liệu của cùng kỳ thay đổi giữa các lần công bố như thế nào và ảnh hưởng chỉ số ra sao? | Cặp báo cáo gốc/điều chỉnh hoặc số so sánh kỳ sau; ngày công bố | Mạnh về kỹ thuật dữ liệu, ít phụ thuộc nhãn cổ tức | Hướng thay thế nếu nhãn cổ tức không đạt |

Đây là đánh giá định tính về sự phù hợp và phụ thuộc dữ liệu, không phải điểm số thị trường hay số giờ đã đo. N2/N3/N4 phát triển các khả năng vốn đã được nhắc trong bộ trước thành bài toán và protocol riêng; không tuyên bố chúng mới hoàn toàn. N1 mở thêm lớp giải thích vốn lưu động so với sáu chỉ tiêu lõi.

## 4. Hồ sơ riêng cho từng hướng

| Hướng | Đề xuất nghiên cứu | Tài chính | Kỹ thuật IT | Dữ liệu và đánh giá |
|---|---|---|---|---|
| N1 | [Đề xuất](n1-loi-nhuan-dong-tien/01-de-xuat-nghien-cuu.md) | [Kiến thức](n1-loi-nhuan-dong-tien/02-kien-thuc-tai-chinh.md) | [Thiết kế](n1-loi-nhuan-dong-tien/03-ky-thuat-it.md) | [Protocol](n1-loi-nhuan-dong-tien/04-du-lieu-thi-nghiem-danh-gia.md) |
| N2 | [Đề xuất](n2-kich-ban-co-tuc/01-de-xuat-nghien-cuu.md) | [Kiến thức](n2-kich-ban-co-tuc/02-kien-thuc-tai-chinh.md) | [Thiết kế](n2-kich-ban-co-tuc/03-ky-thuat-it.md) | [Protocol](n2-kich-ban-co-tuc/04-du-lieu-thi-nghiem-danh-gia.md) |
| N3 | [Đề xuất](n3-cong-ty-me-hop-nhat/01-de-xuat-nghien-cuu.md) | [Kiến thức](n3-cong-ty-me-hop-nhat/02-kien-thuc-tai-chinh.md) | [Thiết kế](n3-cong-ty-me-hop-nhat/03-ky-thuat-it.md) | [Protocol](n3-cong-ty-me-hop-nhat/04-du-lieu-thi-nghiem-danh-gia.md) |
| N4 | [Đề xuất](n4-phien-ban-bctc/01-de-xuat-nghien-cuu.md) | [Kiến thức](n4-phien-ban-bctc/02-kien-thuc-tai-chinh.md) | [Thiết kế](n4-phien-ban-bctc/03-ky-thuat-it.md) | [Protocol](n4-phien-ban-bctc/04-du-lieu-thi-nghiem-danh-gia.md) |

## 5. Vì sao chưa chọn đề tài khác?

N1 có thể thành đề tài riêng về khả năng chuyển lợi nhuận thành tiền, nhưng chưa có bằng chứng lợi ích lớn hơn việc giữ cổ tức làm câu chuyện ứng dụng. N4 là phương án thay thế rõ nhất: hệ thống chuẩn hóa và đối chiếu phiên bản BCTC Việt Nam có truy vết. Nó vẫn cần nguồn báo cáo và benchmark, không tự dễ chỉ vì bỏ nhãn cổ tức.

Chưa ưu tiên giá cổ phiếu/phản ứng thị trường, phân tích cảm xúc tin tức hoặc chatbot làm trọng tâm: các hướng này thêm nguồn, nhãn và protocol khác trong khi pipeline lõi chưa được chứng minh. Chưa có nghiên cứu đủ rộng để kết luận các hướng đó kém tiềm năng nói chung.

## 6. Quyết định sau pilot

1. Thực hiện pilot 10 doanh nghiệp theo kế hoạch hiện hành; đo khả năng tải, độ phủ, độ đúng và công sức review.
2. Chốt nhãn cổ tức được công bố hay thực trả dựa trên bằng chứng; thiếu thông báo không đồng nghĩa không trả. Nếu thiếu bằng chứng xác định giảm/ngừng, chỉ báo cáo phần phân tích đủ điều kiện và hạn chế của RQ3.
3. Giữ lõi nếu có thể tạo mẫu phân tích hợp lệ. Chỉ triển khai ML theo gate trong [đề cương](../research-design.md); không lấy tổng số doanh nghiệp–năm làm số mẫu đủ nhãn.
4. N1 chỉ bổ sung cho case có dòng CFO chi tiết và nguồn đủ rõ. Nếu làm thành tính năng bắt buộc, phải cập nhật SRS, SDD, PP và TP cùng nhau.
5. Nếu nhãn cổ tức không thể xây dựng đáng tin cậy dù đã khảo sát nguồn bổ sung, dùng báo cáo pilot để cân nhắc N4 và trao đổi đổi trọng tâm. Chưa đổi đề tài trong lượt nghiên cứu này.

Mọi hướng mở rộng phải nằm trong phần công sức còn lại đã đo, thay thế một phần công việc khác hoặc được chuyển sang giai đoạn sau. Không cộng bốn hồ sơ vào lịch MVP hiện hành.
