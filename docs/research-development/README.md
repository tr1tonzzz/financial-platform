# Bộ nghiên cứu phát triển đề tài BCTC–cổ tức Việt Nam

> **Trạng thái 03/10/2026 — hồ sơ khảo sát trước.** Project hiện hành tập trung thu thập, kiểm định và phân tích lợi nhuận–dòng tiền–cổ tức tiền mặt. Xem [SRS hiện hành](../research-platform/02-de-tai-va-srs.md) và [phương pháp thống nhất](../research-platform/11-phuong-phap-thu-thap-va-xu-ly.md). Các ngưỡng cảnh báo, dự báo, scope và lịch cũ bên dưới chỉ để tham khảo; không là yêu cầu MVP hiện hành.

Ngày nghiên cứu: **03/10/2026**. Ngôn ngữ: tiếng Việt. Trạng thái: tổng hợp tài liệu đã đọc, khảo sát nhỏ đã thực hiện và thiết kế nghiên cứu đề xuất; chưa triển khai hệ thống hoặc hoàn thành pilot 10 doanh nghiệp.

## 1. Kết luận và cách sử dụng

Kết luận lựa chọn sau khi rà soát thêm ở [bản chốt đề tài](../research-options/01-chot-y-tuong-de-tai.md); [bốn hướng nghiên cứu bổ sung](../research-options/README.md) có tài liệu riêng. Bộ 27 file này tiếp tục đào sâu các thành phần của đề tài hiện hành.

Nên xây **dữ liệu có truy vết + vòng đời sự kiện cổ tức + phân tích dòng tiền** làm đóng góp chính. Cảnh báo theo quy tắc thuộc MVP; dự báo xác suất chỉ thực hiện khi nhãn và mẫu đạt gate hiện hành. Trợ lý hỏi đáp là hướng sau MVP.

Đọc [so sánh hướng phát triển](00-huong-phat-trien.md), [tổng quan nghiên cứu](01-tong-quan-tai-lieu.md) và [khảo sát nguồn thực tế](03-khao-sat-nguon-thuc-te.md) trước. Nguồn, mức độ đã đọc và giới hạn ở [sổ tài liệu tham khảo](02-so-tai-lieu-tham-khao.md).

Các tài liệu chính [SRS](../initial-docs/SRS-FDP-01.md), [đề cương](../research-design.md), [SDD](../initial-docs/SDD-FDP-01.md), [PP](../initial-docs/PP-FDP-01.md), [TP](../initial-docs/TP-FDP-01.md) tiếp tục quy định phạm vi. Bộ này đào sâu phương pháp và đề xuất mở rộng, không tự biến phần mở rộng thành yêu cầu nghiệm thu.

## 2. Hồ sơ riêng cho từng ý tưởng

Mỗi thư mục gồm bốn tài liệu: đề xuất nghiên cứu; kiến thức tài chính; kỹ thuật IT; thiết kế dữ liệu, thí nghiệm và đánh giá.

| Ý tưởng | Nghiên cứu | Tài chính | IT | Thí nghiệm |
|---|---|---|---|---|
| I1. Dữ liệu BCTC có truy vết | [Đề xuất](i1-du-lieu-truy-vet/01-de-xuat-nghien-cuu.md) | [Ngữ nghĩa BCTC](i1-du-lieu-truy-vet/02-kien-thuc-tai-chinh.md) | [Parser và provenance](i1-du-lieu-truy-vet/03-ky-thuat-it.md) | [Benchmark](i1-du-lieu-truy-vet/04-du-lieu-thi-nghiem-danh-gia.md) |
| I2. Dòng tiền và khả năng duy trì cổ tức | [Đề xuất](i2-dong-tien-co-tuc/01-de-xuat-nghien-cuu.md) | [Chỉ số và FCFE](i2-dong-tien-co-tuc/02-kien-thuc-tai-chinh.md) | [Phân tích và dashboard](i2-dong-tien-co-tuc/03-ky-thuat-it.md) | [Kiểm định quan hệ](i2-dong-tien-co-tuc/04-du-lieu-thi-nghiem-danh-gia.md) |
| I3. Vòng đời và chất lượng sự kiện cổ tức | [Đề xuất](i3-vong-doi-co-tuc/01-de-xuat-nghien-cuu.md) | [Ngày, quyền và DPS](i3-vong-doi-co-tuc/02-kien-thuc-tai-chinh.md) | [Phiên bản sự kiện](i3-vong-doi-co-tuc/03-ky-thuat-it.md) | [Đối chiếu thông báo](i3-vong-doi-co-tuc/04-du-lieu-thi-nghiem-danh-gia.md) |
| I4. Cảnh báo sớm có giải thích | [Đề xuất](i4-canh-bao-som/01-de-xuat-nghien-cuu.md) | [Nhãn và tín hiệu](i4-canh-bao-som/02-kien-thuc-tai-chinh.md) | [Rule score và logistic](i4-canh-bao-som/03-ky-thuat-it.md) | [Đánh giá theo thời gian](i4-canh-bao-som/04-du-lieu-thi-nghiem-danh-gia.md) |
| I5. Trợ lý tra cứu có dẫn nguồn | [Đề xuất](i5-tro-ly-co-dan-nguon/01-de-xuat-nghien-cuu.md) | [Giới hạn diễn giải](i5-tro-ly-co-dan-nguon/02-kien-thuc-tai-chinh.md) | [SQL, tìm kiếm và RAG](i5-tro-ly-co-dan-nguon/03-ky-thuat-it.md) | [Đánh giá câu trả lời](i5-tro-ly-co-dan-nguon/04-du-lieu-thi-nghiem-danh-gia.md) |

## 3. Kiến thức và quy tắc dùng chung

- [Từ điển dữ liệu, thuật ngữ và công thức](04-tu-dien-du-lieu-va-thuat-ngu.md).
- [Quy trình nghiên cứu, lựa chọn mẫu và lịch đọc](05-quy-trinh-nghien-cuu-va-lo-trinh-doc.md).

I1 và I3 là đầu vào của I2 và I4. I5 sử dụng kết quả đã duyệt của cả bốn hướng. Có thể đọc riêng từng hồ sơ, nhưng phải giữ các quy tắc chung về kỳ, phạm vi, đơn vị, thời điểm và nguồn.

## 4. Những gì đã và chưa thực hiện

Đã đọc các nguồn chính thức và một số phần của bài báo; đã tải một PDF doanh nghiệp, trích xuất sáu giá trị bằng cách tách nửa trang và đối chiếu hình ảnh. Đã đọc hai thông báo VSDC qua công cụ web. Chưa có crawler VSDC chạy thành công trên máy, chưa có dataset 30 công ty, chưa huấn luyện hoặc đánh giá mô hình, chưa có kết luận thực nghiệm về quan hệ BCTC–cổ tức.

**27 file Markdown** trong bộ này. Mọi tỷ lệ hiệu quả, quỹ giờ và ngưỡng chưa đo đều được ghi là mục tiêu hoặc giả định.
