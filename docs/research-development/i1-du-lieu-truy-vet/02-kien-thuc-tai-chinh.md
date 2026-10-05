# I1 — Kiến thức tài chính để đọc và chuẩn hóa BCTC

Ngày: 03/10/2026. Mục đích: giúp parser nhận đúng đối tượng kinh tế, không chỉ nhận đúng chữ. Cần đọc trước [IT](03-ky-thuat-it.md).

## 1. Bốn nhóm báo cáo

| Thành phần | Loại thông tin | Sáu facts liên quan | Nhầm lẫn cần tránh |
|---|---|---|---|
| Bảng cân đối | Số dư tại một thời điểm | Tiền, tài sản, nợ phải trả, vốn | Lấy đầu kỳ thay cuối kỳ |
| Kết quả kinh doanh | Dòng lợi nhuận trong kỳ | LNST | Lấy lợi nhuận trước thuế hoặc phần công ty mẹ |
| Lưu chuyển tiền tệ | Thu/chi trong kỳ | CFO | Lấy tổng biến động tiền hoặc tiền trước thay đổi vốn lưu động |
| Thuyết minh | Giải thích đơn vị, chính sách và cấu phần | Xác nhận mọi facts | Bỏ qua tiền hạn chế, phân loại hoặc số sửa |

IAS 7 là nguồn học phân loại dòng tiền; cách ghi nhận thực tế phải theo báo cáo được thu thập. [IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows.html/).

## 2. Stock, flow và kỳ

Tiền/tài sản/nợ/vốn là stock cuối kỳ; LNST/CFO là flow của cả năm. CFO/tài sản cuối kỳ là chỉ số hợp lệ nếu đặt tên đúng. Khi muốn dùng tài sản bình quân, cần cả đầu và cuối kỳ tương thích: `A_avg=(A_begin+A_end)/2`; không đổi mẫu số giữa các công ty mà không ghi phiên bản.

Phân biệt quý đơn lẻ, lũy kế chín tháng và cả năm. Không cộng số lũy kế bốn quý để tạo năm. Dataset MVP chỉ dùng năm kiểm toán, tránh thêm bài toán quy đổi quý trước khi có nhu cầu.

## 3. Phạm vi và chuẩn mực

Hợp nhất phản ánh nhóm doanh nghiệp; riêng phản ánh pháp nhân công ty mẹ. Tổng LNST hợp nhất bao gồm phần cổ đông không kiểm soát, còn DPS công ty mẹ chi cho cổ đông công ty mẹ. Không dùng hai tử/mẫu số đó làm payout mà không xử lý phạm vi.

Vốn chủ sở hữu tổng hợp nhất phải tương thích đẳng thức tài sản = nợ + vốn; dùng vốn thuộc cổ đông công ty mẹ có thể tạo sai lệch do cổ đông không kiểm soát. IFRS/VAS có thể khác số liệu và cách phân loại; lưu `accounting_basis` và so sánh trong cùng basis. [Mẫu IFRS đã kiểm tra](../03-khao-sat-nguon-thuc-te.md).

## 4. Đơn vị, dấu và số so sánh

- “Triệu đồng” nhân 1.000.000; “nghìn đồng” nhân 1.000. Đơn vị áp dụng theo bảng, không mặc định toàn PDF.
- Số trong ngoặc thường thể hiện âm; dấu gạch cần xem quy ước nguồn, không tự coi mọi ô gạch là 0.
- Chỉ tiêu chi tiền có thể ghi âm theo dòng tiền; khi tính “số tiền chi”, đổi sang trị tuyệt đối sau khi định nghĩa dấu và giữ raw.
- Báo cáo 2024 có cột 2023 so sánh; cột đó có thể đã điều chỉnh. Không dùng nó thay phiên bản BCTC 2023 khả dụng ở cutoff quá khứ.
- Dấu chấm/phẩy phân cách tùy ngôn ngữ tài liệu; mẫu có thập phân cần parse theo quy ước nguồn.

## 5. Kiểm định nghiệp vụ

`residual = assets - liabilities - equity`. Dung sai từ đơn vị làm tròn: nếu từng số làm tròn tới u VND, ba số có sai khác tổng tối đa khoảng `1,5u` chỉ do làm tròn. Dùng giới hạn theo nguồn cộng một mức tương đối nhỏ nếu có lý do; không đặt dung sai lớn chỉ để hết lỗi.

Đẳng thức đúng vẫn có thể xảy ra khi cả ba số cùng sai đơn vị hoặc lấy nhầm năm. Bắt buộc kiểm tra metadata và nguồn độc lập. CFO có thể âm, LNST có thể âm và vốn có thể âm; dấu bất thường không tự chứng minh parser sai.

## 6. Bài tập cần hoàn thành

Đọc một BCTC, ghi sáu facts với nhãn/kỳ/đơn vị/trang; chỉ ra LNST công ty mẹ nếu có; phân biệt CFO với thay đổi tiền; tìm cơ sở kế toán và bằng chứng kiểm toán. Sau đó thử cố tình đổi cột năm hoặc hệ số đơn vị để xem validation nào phát hiện được.

Đầu ra là bảng đối chiếu đọc tay và danh sách lỗi; kiến thức chỉ được coi sẵn sàng khi người thực hiện giải thích được vì sao mỗi fact đúng phạm vi.
