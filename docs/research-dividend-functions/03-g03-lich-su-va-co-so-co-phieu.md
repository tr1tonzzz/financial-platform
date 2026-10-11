# G03 — Tra soát lịch sử cổ tức khi cơ sở cổ phiếu thay đổi

Thuộc BUC03; D05–D08. Nhu cầu: phân biệt DPS biến động do chính sách tiền mặt với biến động do số cổ phiếu tăng. Giá trị thực tế là giảm lỗi diễn giải lịch sử; phép tính trên một basis tham chiếu không tự phản ánh toàn bộ thu nhập, tổng lợi nhuận hay giá trị danh mục của nhà đầu tư.

## Giải thích phạm vi cổ tức cổ phiếu với giảng viên

Không cộng cổ tức cổ phiếu vào thu nhập tiền mặt vì người nhận có thêm cổ phiếu, chưa có khoản tiền nhận tại sự kiện; quy đổi thành tiền cần giá, thời điểm và giả định bán. Nhưng **không được bỏ sự kiện cổ phiếu khỏi kiểm tra cơ sở**: nó ảnh hưởng DPS, số cổ phiếu có quyền và tính so sánh. Phạm vi hợp lý là nghiên cứu tiền mặt, giữ sự kiện cổ phiếu làm dữ liệu điều chỉnh cơ sở. Thông báo phát hành từ vốn chủ sở hữu không phải lúc nào cũng mang tên “cổ tức cổ phiếu”; phải giữ loại sự kiện theo nguồn.

## Hai chế độ kết quả tách biệt

**A — lịch sử trên cơ sở tham chiếu:** lưu DPS gốc và basis gốc; chuyển sang một basis được chọn khi đã duyệt các sự kiện thích hợp trong khoảng. Nếu từ basis cũ sang mới số cổ phiếu tăng bởi hệ số F, `DPS_old_on_new_basis = DPS_old / F`. Chuỗi sự kiện hợp lệ có F bằng tích hệ số. Ví dụ giả lập 20% cổ phiếu miễn phí: 1.000 đồng/cổ phiếu cũ thành 833,333… trên basis mới; DPS mới=900 tương đương tăng 8% về tiền trên vị thế lý thuyết, dù DPS gốc giảm 10%. Không làm tròn đầu vào trước khi so sánh. Đây là phép chuẩn hóa có giả định không giao dịch, không cash-in-lieu và chưa xử lý phần lẻ theo tài khoản.

**B — mô phỏng quyền của vị thế:** cần số cổ phiếu đủ điều kiện ở từng sự kiện, quy tắc phần lẻ, sự kiện mua/bán hoặc xác nhận không giao dịch, thời điểm hạch toán và trạng thái quyền. Cổ phiếu mới được tính cho quyền tiền mặt sau chỉ khi có bằng chứng đủ điều kiện. `new_shares = floor(eligible_shares × ratio)` khi nguồn quy định hủy phần lẻ. Không lấy số nắm giữ hiện tại thay số có quyền lịch sử. Kết quả “dự kiến/mô phỏng”, không “đã nhận”. Chế độ B chưa là nghĩa vụ pilot D05–D08, chỉ dùng ví dụ độc lập để thấy giới hạn của A.

## Dữ liệu sự kiện và quy tắc

`corporate_action`: issuer_id; source_event_id; kind; raw_ratio/numerator/denominator; ratio_factor; announced_at; record_date; ex_date; credit_date; registration_date; trading_date; basis_effective_date; effective_date_evidence; rounding_rule; status; amends/cancels; source/locator/review. Mọi ngày chưa biết lưu null cùng reason. Ngày đăng ký cuối cùng, đăng ký bổ sung, hạch toán và bắt đầu giao dịch là các mốc khác nhau; không dùng một ngày làm tất cả.

Phiên bản đầu hỗ trợ phát hành cổ phiếu miễn phí tỷ lệ xác định và tách/gộp cổ phiếu đã kiểm chứng. Quyền mua trả tiền, ESOP, phát hành riêng lẻ, sáp nhập và chuyển đổi không mặc định là factor điều chỉnh DPS như cổ phiếu miễn phí. Chúng có thể tác động pha loãng nhưng cần mô hình riêng. Nếu một sự kiện không hỗ trợ nằm trong khoảng so sánh, chặn kết quả điều chỉnh của khoảng đó.

Nguyên tắc: không sửa DPS gốc; parser cho tỷ lệ quyền giữ raw text; tránh nhầm 20:3 thành hệ số 20/3 (đúng tăng thêm 3/20, F=1,15); canceled không áp dụng; amended phải chọn revision hiệu lực; sự kiện pending/conflicting chặn so sánh. Bản công bố sau as_of không được đưa vào phân tích tại as_of cũ. Dữ liệu đã điều chỉnh từ vendor cần `basis=vendor_adjusted` và chính sách chuyển đổi riêng; không áp thêm factor lần hai. Không tự điều chỉnh EPS đã hồi tố.

## Ca Việt Nam — FPT 2025

[VSDC ngày 14/07/2025](https://vsdc.vn/vi/ad1/184974) ghi phát hành tăng vốn từ nguồn vốn chủ sở hữu, ngày đăng ký cuối cùng 22/07/2025, quyền 20:3, làm tròn xuống và hủy phần lẻ. Hệ số lý thuyết=1,15. Với 21 cổ phiếu đủ quyền, cổ phiếu thêm=floor(21×3/20)=3; tổng=24, thay vì 24,15 cổ phiếu lý thuyết. [Thông báo đăng ký bổ sung](https://vsdc.vn/vi/ad1/186572) là bằng chứng đăng ký, chưa tự xác nhận ngày có quyền tiền mặt trên từng tài khoản.

Hai thông báo tiền mặt gồm [còn lại năm 2024](https://vsdc.vn/vi/ad1/183589) và [tạm ứng đợt 1 năm 2025](https://vsdc.vn/vi/ad1/189195), mỗi đợt 1.000 đồng/cổ phiếu, thuộc hai năm lợi nhuận khác nhau. Đây là hai **đợt**, không đủ để suy tổng cổ tức năm 2024/2025 hoặc growth hàng năm. Theo giả định riêng rằng 24 cổ phiếu sau tăng vốn đều đủ quyền đợt sau và không giao dịch, khoản gộp của vị thế tăng từ 21.000 lên 24.000 đồng; đây là mô phỏng có điều kiện, chưa xác nhận thực nhận. Nguồn hiện có chưa đủ để tự chạy chuỗi entitlement thực tế. Trạng thái điều chỉnh basis phải yêu cầu người vận hành xác nhận bằng chứng, không suy từ thứ tự ngày công bố.

## Thiết kế và nghiệm thu

B03.4a nhập/duyệt ledger corporate action; B03.4b resolve chuỗi theo as_of; B03.4c kiểm basis interval và tính factor; B03.4d trả hai cột gốc/tham chiếu; B03.5 nêu phần biến động do basis với giả định. Chỉ tính annual growth khi FR28 về coverage/period vẫn đạt; việc biết factor không thay thế discovery đủ thông báo.

TC-D05: loại sự kiện, tỷ lệ 20:3, ngày riêng và phần lẻ từ nguồn. TC-D06: không sự kiện, một/nhiều sự kiện, gộp/tách, factor>0. TC-D07: canceled/amended/unresolved/unsupported, trùng mốc, thiếu ngày hoặc source basis chặn đúng; không double-adjust. TC-D08: giữ raw DPS, xuất factor chain và lý do; annual partial vẫn không được growth dù basis đã biết.

**Khả thi:** trung bình–cao với ledger thủ công và một loại phát hành miễn phí; thấp hơn nếu đòi tự xử lý mọi quyền và danh mục giao dịch. Ước tính 18–28 giờ cho pilot A với 1–2 ca, chưa gồm thu tự động ledger hoặc mô phỏng tài khoản B. Nếu thiếu bằng chứng basis, hiển thị lịch sử nguyên bản kèm cảnh báo chưa so sánh được; không ép ra tăng/giảm. Chức năng này là lý do bổ sung dữ liệu sự kiện cổ phiếu, không mở rộng thành phân tích mọi hình thức đầu tư.
