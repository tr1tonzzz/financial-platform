# G02 — Phân tích bao phủ chi đầu tư và phân phối bằng tiền

Thuộc BUC02; D01–D04. Câu hỏi người dùng: “LNST và CFO có vẻ tốt, nhưng tiền tạo ra trong kỳ còn bao nhiêu sau chi đầu tư và phân phối cho chủ sở hữu?” Kết quả giúp quyết định đọc sâu lịch sử chi đầu tư, nguồn tiền tích lũy hoặc tài trợ; chưa chứng minh khả năng duy trì cổ tức tương lai.

## Định nghĩa và phạm vi

Chọn doanh nghiệp phi tài chính, năm đầy đủ, cùng chủ thể kế toán. CAPEX ở bản đầu là **tiền chi mua sắm/xây dựng TSCĐ và tài sản dài hạn khác theo dòng nguồn đã duyệt**; nếu dòng gộp rộng hơn CAPEX kinh tế thì ghi nguyên nhãn và `capex_definition`. Không dùng nguyên lưu chuyển đầu tư thuần làm CAPEX, vì còn tiền gửi, thu hồi cho vay và thanh lý tài sản. Không tự trừ thu thanh lý khỏi gross CAPEX nếu chưa chọn một định nghĩa khác có phiên bản.

D là tiền **thực chi trong năm tài chính**, không phải DPS công bố cho lợi nhuận năm đó. Nếu báo cáo ghi gộp cổ tức/lợi nhuận trả cho chủ sở hữu, metric là bao phủ **phân phối cho chủ sở hữu**, không giả làm tiền cổ tức cổ đông phổ thông. Công ty mẹ và hợp nhất có ranh giới tiền khác nhau; CFO hợp nhất không xác nhận tiền có thể chuyển lên công ty mẹ. Lưu nhãn `distribution_kind`, `reporting_scope`, `recipient_scope` và tình trạng tách khoản.

| Đầu vào | Hợp đồng tối thiểu |
|---|---|
| CFO | Giá trị signed VND, cả năm; fact reviewed |
| CAPEX | Độ lớn chi tiền không âm, tên dòng gốc, mã dòng nếu có, quy tắc sign/type đã duyệt |
| D | Độ lớn thực chi không âm, loại cổ tức hoặc phân phối gộp, cùng kỳ/scope |
| Metadata dùng chung | issuer_id, period_start/end, scope, unit, published_at/first_seen_at, revision, locator, reviewer, snapshot/as_of |
| Bổ sung để tra soát | Tiền đầu/cuối kỳ, vay/hoàn trả nợ, CFI/CFF và thuyết minh; thiếu không làm hỏng ba phép tính lõi |

Hai dòng tiền ra trong PDF thường âm; normalizer chuyển dấu theo mapping đã duyệt. `abs()` chung cho mọi số sẽ che lỗi nhận diện tiền thu. Chi âm theo giá trị magnitude nhập vào là lỗi dữ liệu. Hoàn nhập hoặc tiền thu mang ý nghĩa khác phải lập field/mapping riêng.

## Quy tắc tính và diễn giải

`cash_after_capex = CFO − CAPEX`.

`cash_after_capex_and_distribution = CFO − CAPEX − D`.

`coverage_cfo_to_investment_distribution = CFO / (CAPEX + D)` nếu mẫu số >0. Nếu tổng chi=0, hai số dư vẫn tính được nhưng tỷ số `not_applicable`. Thiếu hoặc khác kỳ/scope/đơn vị: metric tương ứng `not_computable` cùng reason; không điền 0. CFO âm vẫn tính signed. Không gọi CFO−CAPEX là FCFE: chưa xét vay ròng hay các điều chỉnh thích hợp.

Số dư âm diễn giải: “CFO của kỳ này chưa bao phủ các khoản chi được chọn”; số dư không âm: “CFO bao phủ về mặt số học trong phạm vi các khoản đã chọn”. Không gán “an toàn”, “sắp cắt cổ tức”, “vay để trả cổ tức”. Tiền là nguồn lực chung; phép trừ không lần theo từng đồng tới mục đích sử dụng. Khi D=0 không có nghĩa chính sách không trả cổ tức, trừ khi nguồn và coverage cho biết điều đó riêng.

## Ca thực tế DHG năm 2025

Đã xem ảnh BCLCTT, PDF trang 11/in trang 9, đơn vị VND, B03-DN **phạm vi công ty**. Đây là đọc và đối chiếu thủ công trong nghiên cứu, chưa phải gold được người thứ hai duyệt. [BCTC kiểm toán DHG 2025](https://dhgpharma.com.vn/sites/default/files/2026-03/DHG-Audited-FS-2025-VN.pdf).

| Dòng / phép tính | 2025 (VND) | Cột so sánh 2024 (VND) |
|---|---:|---:|
| CFO — mã 20 | 1.212.967.705.385 | 1.317.583.405.328 |
| Tiền chi TSCĐ/TS dài hạn khác — magnitude mã 21 | 31.136.402.852 | 88.704.714.502 |
| Cổ tức/lợi nhuận đã trả chủ sở hữu — magnitude mã 36 | 1.307.460.710.000 | 980.595.532.500 |
| CFO sau hai khoản chi | −125.629.407.467 | 248.283.158.326 |
| CFO / tổng hai khoản chi | khoảng 0,9062 lần | khoảng 1,2322 lần |

2025 CFO dương nhưng số dư sau hai khoản chi âm; ca này minh chứng giá trị bổ sung của G02 so với chỉ nhìn CFO dương. Nó không chứng minh rủi ro cắt cổ tức: cần nhiều kỳ và bối cảnh khác. Không ghép dòng 36 vào profit_year=2025. Cột 2024 từ bản 2025 là comparative revision, không giả làm giá trị biết sẵn năm 2024. Nguồn/hash, inputs và kết quả tái tính lưu trong [evidence](evidence/real-cases.json).

## Các bước xây dựng

1. B02.4a: thêm hai field/mapping, nhập tay có nguồn cho một ca; dùng hàng đợi duyệt hiện hữu. Thu tự động hai trường là bước sau khi đo effort.
2. B02.4b: service nhận fact refs và snapshot; kiểm metadata; tính Decimal; trả value/status/reason/formula/version/operands, tách trạng thái từng metric.
3. B02.4c: màn hình bảng CFO → tiền sau chi đầu tư → tiền sau phân phối; hiển thị dòng nguồn, định nghĩa và dữ liệu còn thiếu. Nếu dùng biểu đồ phân bổ, không dựng sơ đồ khiến người đọc hiểu đã xác định nguồn tài trợ thực.
4. B02.5: mẫu câu cần tra soát có rule_id và operands; người dùng ghi câu hỏi, đọc thuyết minh và lưu hồ sơ BUC05.

## Kiểm chứng và khả thi

TC-D01: kiểm CAPEX/D với tên dòng, sign và loại khoản gộp; thông báo DPS không được dùng thay D. TC-D02: bảng năm/scope/unit lệch và missing chặn tính. TC-D03: số dư, mẫu số=0, CFO âm và Decimal đúng; ca DHG đối chiếu nguồn. TC-D04: mỗi kết quả dẫn tới operands, snapshot/version và nguồn; dòng gộp được giữ đúng nhãn khi xuất.

**Khả thi:** cao với nhập/duyệt có nguồn cho 1–3 ca; tự động mọi layout chưa có cơ sở. Ước tính 16–24 giờ bổ sung cho service/UI/test một ca, chưa gồm hoàn thiện hạ tầng nền; 1–2 giờ cho mỗi ca nguồn tương tự, dự toán cần đo thực tế. Điểm dừng: không xác minh được CAPEX/D cùng chủ thể thì vẫn cung cấp phân tích LNST/CFO, ghi G02 chưa đủ cơ sở. Không hạ chuẩn dữ liệu để có kết quả.
