# Kiến thức tài chính cần dùng khi lấy dữ liệu mới

> **Trạng thái 03/10/2026 — hồ sơ khảo sát trước.** Project hiện hành tập trung thu thập, kiểm định và phân tích lợi nhuận–dòng tiền–cổ tức tiền mặt. Xem [SRS hiện hành](../research-platform/02-de-tai-va-srs.md) và [phương pháp thống nhất](../research-platform/11-phuong-phap-thu-thap-va-xu-ly.md). Các ngưỡng cảnh báo, dự báo, scope và lịch cũ bên dưới chỉ để tham khảo; không là yêu cầu MVP hiện hành.

Phạm vi: áp dụng BCTC năm 2025 và các kỳ đầu 2026 vào đề tài hiện hành, ngày đánh giá 03/10/2026. Định nghĩa nghiên cứu chính nằm ở [research-design](../research-design.md); tài liệu này không tự thay thiết kế nhãn.

## 1. Năm, quý và lũy kế

Tài sản, tiền, nợ phải trả và vốn chủ sở hữu là **số tại ngày kết thúc kỳ**. LNST và CFO là **dòng phát sinh trong khoảng thời gian**. BCTC quý có thể trình bày LNST riêng quý và lũy kế trong cùng bảng; lưu chuyển tiền tệ thường trình bày từ đầu năm đến cuối kỳ. Phải lưu `period_start`, `period_end`, `duration_months`, `period_kind`, nhãn cột gốc.

- Q1: kỳ ba tháng thường cũng bằng lũy kế ba tháng, nhưng vẫn kiểm tra tiêu đề cột.
- H1: CFO sáu tháng phải đi cùng LNST sáu tháng khi tính CFO/LNST. Không lấy LNST riêng Q2 làm mẫu số cho CFO H1.
- CFO riêng Q2 có thể tính `CFO_H1 − CFO_Q1` khi cùng scope, đơn vị, chính sách và phiên bản có thể so sánh; gắn là số dẫn xuất, liên kết hai nguồn.
- Không cộng số dư tiền hay tài sản cuối quý để tạo số năm, không nhân bốn LNST Q1 để coi là LNST cả năm đã quan sát.

TTM tại 30/06/2026 cho một dòng phát sinh có thể tính `FY2025 + H1_2026 − H1_2025`. Công thức đòi hỏi đủ ba nguồn cùng cơ sở, phạm vi và comparability; không áp dụng cho số dư bảng cân đối. Chưa chạy tính TTM trong khảo sát này vì chưa chuẩn hóa đủ H1/2025. Dùng cột so sánh đã phân loại lại cần giữ phiên bản và ngày khả dụng; không đưa số điều chỉnh mới xuất hiện vào cutoff lịch sử cũ.

## 2. Phạm vi, cơ sở lập và mức bảo đảm

Ưu tiên hợp nhất theo SRS. Nếu doanh nghiệp công bố báo cáo cấp doanh nghiệp/riêng thì gắn loại rõ ràng, kiểm tra điều kiện đưa vào cohort. DHG FY2025 trong phép thử được đọc theo báo cáo cấp doanh nghiệp; VNM Q1/2026 là hợp nhất. Không ghép CFO riêng với LNST hợp nhất hoặc LNST của cổ đông công ty mẹ với vốn chủ sở hữu tổng mà không giải thích mục tiêu tỷ số.

Kiểm toán năm và soát xét giữa niên độ là hai mức bảo đảm khác nhau. VNM Q1/2026 có báo cáo soát xét; H1 của các công ty đã tải cũng có bản soát xét. Chỉ ghi `audited/reviewed/unaudited/unknown` sau đọc báo cáo liên quan, không suy từ kỳ, tên nhóm trên website hoặc ngôn ngữ. BCTC tiếng Anh VHC vẫn phải đọc cơ sở kế toán; không tự gán IFRS.

## 3. Sự kiện cổ tức đã thu thập

Bốn HTML đã tải và trích thành [dividend-event-examples.json](dividend-event-examples.json); tổng cộng năm thành phần theo năm lợi nhuận. Cùng agent đối chiếu với nội dung nguồn, chưa có chấm độc lập.

| Thông báo chính thức | Công bố | Chốt quyền | Thanh toán theo lịch | DPS và năm lợi nhuận |
|---|---|---|---|---|
| [VNM 187729](https://vsdc.vn/vi/ad1/187729) | 02/10/2025 | 17/10/2025 | 24/10/2025 | 2.850 đồng = 350 thuộc 2024 + 2.500 tạm ứng 2025 |
| [VNM 197038](https://vsdc.vn/vi/ad1/197038) | 17/06/2026 | 29/06/2026 | 17/07/2026 | 1.850 đồng, phần còn lại 2025 |
| [DHG 195056](https://vsdc.vn/vi/ad1/195056) | 29/04/2026 | 12/05/2026 | 28/05/2026 | 5.000 đồng, đợt 1 của 2025 |
| [DHG 199544](https://vsdc.vn/vi/ad1/199544) | 21/08/2026 | 15/09/2026 | 30/09/2026 | 5.000 đồng, đợt cuối của 2025 |

Không gán toàn bộ 2.850 đồng của thông báo VNM vào năm 2025 hoặc năm thanh toán mà bỏ mất ý nghĩa năm lợi nhuận. Mệnh giá trong bốn thông báo là 10.000 đồng; tỷ lệ phần trăm tính trên mệnh giá, không phải dividend yield theo giá thị trường. Giữ DPS gốc là đơn vị đồng/cổ phiếu; nếu dùng tỷ lệ phải lưu mệnh giá và cách chuyển đổi.

Tổng các thành phần thuộc 2025 đã quan sát là VNM 4.350 đồng và DHG 10.000 đồng/cổ phiếu. Đây chỉ là **tổng từ các thông báo đã thu thập**, không đủ bằng chứng xác nhận đầy đủ lịch sử năm, thực trả hoặc sự so sánh đã điều chỉnh thay đổi số cổ phiếu. Chỉ cần thiếu một thông báo điều chỉnh/hủy là phép tổng có thể sai.

`announcement/published`, `record_date`, `scheduled_payment_date` và `confirmed_paid_at` phải tách riêng. Bốn sự kiện đang giữ `paid_status=scheduled`, `confirmed_paid_at=null`, kể cả ngày thanh toán đã qua. Không tìm thấy xác nhận không được tự biến thành “đã trả” hoặc “không trả”. Ngày hiển thị có giờ nhưng nguồn không ghi timezone nên JSON giữ `displayed_timezone=null`.

Khoản “cổ tức, lợi nhuận đã trả cho chủ sở hữu” trên báo cáo lưu chuyển tiền tệ là dòng tiền trong kỳ, có thể thuộc lợi nhuận các năm trước và có phạm vi khác DPS cho cổ đông phổ thông. Không đồng nhất khoản đó với tổng DPS theo năm lợi nhuận. Dùng cho phân tích sức chịu đựng dòng tiền chỉ khi định nghĩa mẫu số phù hợp và có nguồn.

## 4. Dữ liệu gần hiện tại và cửa sổ nhãn tương lai

Thiết kế hiện hành dùng cutoff là thời điểm BCTC năm khả dụng; outcome là 12 tháng sau cutoff. Ví dụ mốc đóng cửa sổ, lấy ngày trên danh mục làm minh họa, chưa chứng minh ngày công bố sớm nhất:

| Feature mới | Cutoff minh họa | Cửa sổ 12 tháng kết thúc | Tại 03/10/2026 |
|---|---|---|---|
| DHG FY2025 | 21/03/2026 | 21/03/2027 | Chưa khép |
| HPG FY2025 | 27/03/2026 | 27/03/2027 | Chưa khép |
| VNM Q1/2026, nếu nghiên cứu thiết kế quý riêng | 29/04/2026 | 29/04/2027 | Chưa khép |
| VNM H1/2026, nếu nghiên cứu thiết kế giữa năm riêng | 30/07/2026 | 30/07/2027 | Chưa khép |

DPS thuộc năm lợi nhuận 2025 có thể đã có thông báo gần đầy đủ nhưng không đồng nghĩa nhãn **12 tháng sau BCTC công bố năm 2026** đã trưởng thành. Nếu gắn nhãn theo năm lợi nhuận thay vì cửa sổ thời gian, đó là bài toán khác cần sửa protocol, không dùng chung hai định nghĩa.

Theo thiết kế hiện hành, các mẫu chưa khép phải `censored`, các mẫu không chứng minh đủ độ phủ là `unknown`. Không đưa chúng vào test như nhãn “duy trì cổ tức”. Quý không được tự biến thành bốn mẫu độc lập dùng cùng một nhãn năm; cửa sổ trùng nhau dễ gây rò rỉ. Trước khi thử mô hình quý cần protocol mới, chia theo cutoff, purge cửa sổ outcome và chốt cách nhóm doanh nghiệp.

Nếu pilot chủ yếu thu được thông báo và lịch, research-design đã cho phép chọn đích **giảm mức cổ tức tiền mặt được công bố** theo `announced_at` và DPS thông báo. Cần ghi quyết định, đổi tên kết quả và kiểm tra đủ cửa sổ; không gọi đó là giảm tiền đã thực trả. Phương án này phù hợp loại nguồn đã tải, nhưng khảo sát bốn thông báo hiện tại chưa đủ để tự chốt đích dự báo hoặc nghiệm thu nhãn.

## 5. Hướng phát triển được dữ liệu mới hỗ trợ

N1 lợi nhuận–dòng tiền: báo cáo chính có dòng vốn lưu động, nhưng cần mở rộng trích xuất phải thu/tồn kho và biến động dòng tiền ngoài sáu chỉ tiêu. N2 mô phỏng cổ tức: cần capex, nợ vay/đáo hạn và dòng cổ tức, không thay nợ vay bằng tổng nợ phải trả. N3 riêng–hợp nhất: phải thu được cả hai bộ cùng kỳ. N4 phiên bản: phải giữ bản gốc và điều chỉnh cùng ngày công bố. Khảo sát này chứng minh nguồn mới tồn tại và trích số lõi được; chưa chứng minh đủ dữ liệu cho cả bốn mở rộng. Xem [hồ sơ N1–N4](../research-options/README.md).
