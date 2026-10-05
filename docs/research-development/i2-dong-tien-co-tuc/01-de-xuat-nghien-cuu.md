# I2 — Nghiên cứu dòng tiền và tính ổn định cổ tức

Ngày: 03/10/2026. P0, lõi MVP/RQ2. Phụ thuộc facts I1 và sự kiện I3.

## 1. Câu chuyện và kết luận đề xuất

Doanh nghiệp báo lãi có thể thiếu tiền do phải thu, tồn kho, đầu tư hoặc trả nợ; doanh nghiệp dòng tiền yếu một năm vẫn có thể duy trì cổ tức nhờ tiền tích lũy. Cần phân tích nhiều dấu hiệu cùng lịch sử chi trả, không suy “LNST tăng → chắc chắn duy trì cổ tức”.

Nên bắt đầu với phân bố, xu hướng và so sánh nhóm; chỉ nâng lên hồi quy khi mẫu đủ. [Brav et al.](https://people.duke.edu/~charvey/Research/Published_Papers/P88_Payout_policy_in.pdf) là cơ sở lựa chọn biến nghiên cứu, chưa xác nhận quan hệ ở Việt Nam.

## 2. Câu hỏi nghiên cứu

| Câu hỏi | Biến giải thích | Kết quả cần quan sát |
|---|---|---|
| Tiền từ hoạt động kinh doanh có hỗ trợ lợi nhuận? | CFO/LNST, CFO/A | Lịch sử DPS và nhóm giảm/duy trì |
| Đòn bẩy và vùng đệm tiền liên hệ mức chi trả? | L/A, Cash/A, Cash/L | Chênh lệch nhóm và case ngoại lệ |
| Chi trả hiện tại có để lại dư địa sau đầu tư? | Payout, coverage, cash after CapEx | Chỉ phân tích tập mở rộng đủ đầu vào |
| Tín hiệu có khác theo ngành/năm? | Ngành, kỳ và basis | Phân tích độ nhạy, không suy rộng thiếu kiểm soát |

Giả thuyết là thăm dò: mức tạo tiền thấp và nghĩa vụ nợ cao có thể liên hệ mức chi trả kém ổn định. Chưa chỉ định dấu hệ số như kết quả đã biết.

## 3. Hai lớp phân tích

**Mô tả firm-year:** ghép DPS theo năm lợi nhuận khi nguồn cho biết; sự kiện không rõ năm được để riêng. Đây là tổng hợp lịch sử, được dùng dữ liệu đã biết ở snapshot.

**Liên hệ với kết quả tương lai:** dùng BCTC khả dụng tại cutoff và DPS cửa sổ kế tiếp đã khép. Phần này tuân thủ I4; không gọi việc so CFO 2024 với cổ tức profit_year 2024 đã biết về sau là dự báo tại đầu năm.

## 4. Tính mới cần chứng minh

Đóng góp đề xuất là kết nối facts tự thu thập với sự kiện đã phân bổ đúng, đo ảnh hưởng chất lượng dữ liệu lên kết luận và trình bày case có nguồn. Chưa xác minh mức mới học thuật so với toàn bộ nghiên cứu Việt Nam; cần rà soát bài thực nghiệm trong nước theo [quy trình đọc](../05-quy-trinh-nghien-cuu-va-lo-trinh-doc.md).

## 5. Sản phẩm và phạm vi

Dataset firm-year, heatmap missing, bảng chỉ số, phân bố/tương quan/so sánh nhóm, ít nhất ba case và dashboard đọc nguồn. FCFE/coverage mở rộng phụ thuộc dữ liệu, không bổ sung mặc định vào sáu facts nghiệm thu.

Chưa nghiên cứu định giá mục tiêu, khuyến nghị mua bán hay phản ứng giá thị trường. Dữ liệu 2020–2024 và 30 công ty tạo tối đa 150 firm-year trước loại mẫu, không bảo đảm đủ lực thống kê.

## 6. Tài liệu và bước tiếp

[Kiến thức tài chính](02-kien-thuc-tai-chinh.md), [IT phân tích](03-ky-thuat-it.md), [thiết kế thí nghiệm](04-du-lieu-thi-nghiem-danh-gia.md). Đọc F01–F05 và T07 trong [sổ nguồn](../02-so-tai-lieu-tham-khao.md). F04/F05 là nghiên cứu Việt Nam, cần đối chiếu target/specification trước chuyển biến sang bài toán này. Bước tiếp: chốt bảng biến, năm cổ tức và tiêu chí đủ dữ liệu trước tạo biểu đồ so sánh.
