# N2 — Kiến thức tài chính và công thức kịch bản

Đây là công thức mô phỏng đề xuất, không phải dự báo hoặc xác định mức cổ tức tối đa được phép. [Đề xuất](01-de-xuat-nghien-cuu.md), [đánh giá](04-du-lieu-thi-nghiem-danh-gia.md).

## 1. Phân biệt các khoản tiền

CapEx tiền mặt là chi mua/xây dựng tài sản phục vụ đầu tư đã xác định; không thay bằng tăng giá trị tài sản cuối kỳ. Trả nợ gốc khác chi phí lãi vay; tổng nợ phải trả khác nợ vay. Vay mới là giả định/nguồn tài trợ cần ghi riêng, không mặc định doanh nghiệp luôn vay được.

Tiền và tương đương tiền cuối kỳ trước chưa chắc hoàn toàn tự do sử dụng. Chỉ trừ khoản hạn chế sử dụng xác định được và không nằm trong số dư đã loại trừ; thiếu thuyết minh thì trạng thái `availability_unknown`, không tự coi mọi tiền đều sẵn sàng phân phối.

[IAS 7 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows.html/) phân biệt hoạt động kinh doanh, đầu tư và tài trợ. Trong ứng dụng phải đọc cách phân loại thực tế của báo cáo; không áp một giả định chung về lãi vay/thuế/cổ tức cho mọi tài liệu.

## 2. Cân đối kịch bản cấp năm

Định nghĩa các khoản có dấu theo cùng một đơn vị/phạm vi:

```text
C_end = C_start_usable + CFO_scenario
        - capex_cash - debt_principal_paid + new_borrowing
        + other_net_cash - interest_outside_CFO - dividend_cash
headroom = C_end - assumed_minimum_cash
```

`other_net_cash` chỉ gồm dòng chưa nằm ở các hạng đã liệt kê, ví dụ thu thanh lý hay huy động vốn chủ sở hữu nếu đã xác định. Lãi vay/thuế đã nằm trong CFO không trừ lần nữa. Khi mô phỏng CFO tương lai, loại cổ tức chi trả ra khỏi CFO kịch bản nếu phương pháp gốc xếp khoản đó trong CFO; ghi phép điều chỉnh, sau đó mới trừ `dividend_cash` một lần. Cần cùng nguyên tắc cho khoản nhận cổ tức hoặc giao dịch đặc biệt nằm trong các dòng khác.

Nếu thay đổi vốn lưu động đã phản ánh trong CFO_scenario thì không trừ thêm biến động vốn lưu động. Thuế ngoài CFO, thuê tài sản, mua công ty và các khoản khác phải có vị trí riêng hoặc nằm duy nhất trong `other_net_cash`. Không ép phép tính giản lược này thành FCFE chuẩn hoặc mô hình đầy đủ khi thiếu thành phần.

## 3. Cú sốc và số tiền cổ tức

Với CFO cơ sở dương, có thể dùng `CFO_scenario = CFO_base × (1 − shock_rate)` cho cú giảm theo phần trăm. Với CFO không dương, dùng giảm tuyệt đối hoặc giả định riêng; nhân CFO âm với hệ số nhỏ hơn 1 sẽ làm ít âm hơn, không phải kịch bản xấu đi.

`dividend_cash = DPS × entitled_shares` chỉ khi biết số cổ phiếu được hưởng quyền đúng sự kiện. Không dùng số cổ phiếu bình quân tính EPS thay thế. Chi thực tế trên BCTC và số dự kiến theo thông báo phải được ghi hai loại khác nhau, tránh đếm lặp các đợt trong cùng kế hoạch.

## 4. Diễn giải

Headroom âm biểu thị thiếu tiền so với mức dự trữ giả định trong mô hình này. Headroom dương vẫn có thể đi cùng thiếu tiền tại ngày thanh toán. Dự trữ tối thiểu là giả định của scenario; không phải ngưỡng pháp lý hoặc quy tắc tối ưu đã chứng minh. Không gán xác suất cho kịch bản chưa có mô hình phân phối được kiểm định.
