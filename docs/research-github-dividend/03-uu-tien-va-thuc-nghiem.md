# Chọn chức năng để nghiên cứu bổ sung và kiểm chứng

Ngày 11/10/2026. Đây là đề nghị sau khảo sát GitHub, chưa phải thay đổi SRS đã chốt. Ước lượng là công sức một người, chưa đo trên triển khai thực; không cộng mặc định vào 167 giờ kế hoạch cũ.

## 1. Thứ tự đề nghị

| Mã | Giá trị quyết định | Nền dữ liệu | Thay đổi phạm vi | Đề nghị |
|---|---|---|---|---|
| G01 hồ sơ/sàng lọc có lý do | Chọn vấn đề và doanh nghiệp cần đọc sâu | Phần lớn đã đặc tả | Nhỏ cho hành vi, thêm lưu tiêu chí/ghi chú | Dùng làm cửa vào và demo gần nhất |
| G02 bao phủ tiền sau CAPEX/cổ tức | Thêm chiều thẩm định vượt biểu đồ LNST–CFO–DPS | Cần 2 dòng tiền mới đúng nghĩa | Vừa; mở E10/CAPEX | **Chức năng phân tích mới ưu tiên nghiên cứu/triển khai một ca** |
| G03 cơ sở cổ phiếu | Ngăn kết luận DPS sai, trả lời góp ý thầy | Cần sự kiện cổ phiếu | Vừa; thêm ledger/test | **Kiểm soát cần làm song hành** |
| G04 so sánh song song | Hiểu khác biệt giữa các ứng viên | Tái dùng nền sau G01/02 | Nhỏ nếu chỉ 2–3 mã | Làm sau ca phân tích hoạt động |
| G05 khoản thu theo quyền công bố | Lập kế hoạch thu nhập cá nhân | Thêm vị thế có quyền | Vừa | Ca mô phỏng có điều kiện sau gate |
| G06 tập trung nguồn thu | Hiểu phụ thuộc thu nhập | Phụ thuộc G05/ngành | Vừa | Để nhánh danh mục |
| G07 thay đổi ảnh hưởng hồ sơ | Giữ nhận định cập nhật | Có versions, thêm dependency | Vừa–lớn | Nhánh đồ án ưu tiên |
| G08 yield cao | Phân biệt tiền tăng với giá giảm | Cần giá lịch sử/as_of | Vừa–lớn | Sau gate giá |
| G09 kịch bản dòng tiền | Hiểu độ nhạy | Phụ thuộc G02 | Nhỏ sau G02 | Một kịch bản sau baseline |
| G10 thực nhận/đối soát | Kiểm khoản tiền của người dùng | Sổ tài khoản và quyền | Lớn | Tách khỏi MVP hiện tại |

Không xếp điểm 1–5 giả như kết quả định lượng đã khảo sát. Thứ tự dựa trên suy luận giá trị, phụ thuộc dữ liệu và độ phù hợp phạm vi; cần điều chỉnh bằng effort thật và tác vụ người dùng.

## 2. Luồng demo đề nghị

**Tác vụ:** “Tôi đang cân nhắc doanh nghiệp có lịch sử cổ tức tiền mặt. Tôi cần biết cơ sở tạo tiền của khoản chi này và có đang đọc sai lịch sử DPS không.”

1. Chọn một doanh nghiệp/năm và as_of; xem mức đủ dữ liệu, nguồn BCTC/notice và scope.
2. G01 nêu trường hợp cần tra soát: lợi nhuận/CFO lệch chiều, cổ tức giữ/tăng, hoặc dữ kiện chưa đủ. Người dùng mở hồ sơ thay vì tự dò tất cả đồ thị.
3. G02 đặt CFO cạnh CAPEX và cổ tức thực chi, hiện số dư, tỷ số và ý nghĩa có giới hạn; mở nguồn từng dòng.
4. Nếu có thay đổi cổ phiếu, G03 giải thích DPS gốc và cơ sở so sánh; thiếu chứng cứ thì khóa kết luận tăng/giảm qua điểm thay đổi.
5. Lưu kết luận thẩm định, dữ kiện còn thiếu và snapshot. Đầu ra có thể là “tiếp tục kiểm tiền tích lũy/nguồn vay/khả năng phân phối của mẹ”, không cần sinh một lời khuyên giao dịch.

Luồng này dùng nền thu thập/chuẩn hóa để thực hiện tác vụ tài chính cụ thể. Năng lực kỹ thuật vẫn cần hoàn thiện; hồ sơ đầu tư không che thiếu discovery, review hoặc dữ liệu.

## 3. Việc có thể thực hiện theo lát cắt nhỏ

| Việc | Phụ thuộc | Giờ giả định | Bằng chứng xong |
|---|---|---:|---|
| A. Chọn một ca trong DHG/VNM hoặc mẫu pilot có đủ dòng chi | PDF kiểm toán và scope phù hợp | 3–5 | Bảng dòng nguồn, locator, nghĩa CAPEX/cổ tức; ghi phần gộp/thiếu |
| B. Chốt quy tắc G02 và tự tính đối chiếu | A đủ dữ liệu | 2–3 | Baseline, dấu/đơn vị, trường hợp không áp dụng và đáp án |
| C. Dựng đầu ra G02 nối hồ sơ G01 trong stack hiện hành | B và nền data/review của project | 6–10 | Một ca chạy được tới tra soát/snapshot; nguồn thủ công có nhãn |
| D. Một ca cổ tức cổ phiếu thật để chốt basis G03 | Notice tỷ lệ/ngày quyền/hiệu lực | 3–5 | Timeline, DPS gốc/quy đổi và ca thiếu bị chặn |
| E. Tác vụ thử A/B và ghi sai sót | Ca C/D, tuyển được người | 3–5 | Kết quả từng ca/người và giới hạn |

Khoảng tổng 17–28 giờ **không tính xây lại toàn nền ứng dụng**, triển khai ledger corporate actions tổng quát hoặc benchmark OCR. Nếu nền chưa có, C phải ước lượng lại, không dùng khoảng này làm cam kết hoàn thành hệ thống.

Gate sau A: nếu không tách được tiền cổ tức thì demo đúng nhãn “chi phân phối cho chủ sở hữu” hoặc chọn ca khác; chưa gọi bao phủ cổ tức phổ thông. Gate sau D: nếu chưa đủ nguồn thì giữ cảnh báo basis và không tính chuỗi điều chỉnh giả. Gate sau E: chỉ chọn mở rộng khi chất lượng tác vụ/công sức có bằng chứng.

## 4. Thiết kế đánh giá gắn với quyết định

Baseline A là cùng dữ liệu trong PDF và bảng/biểu đồ tổng hợp; phương án B có hồ sơ UC. Hai bộ ca tương đương, đổi thứ tự để giảm nhớ đáp án. Mục tiêu 3–5 người thử nếu tuyển được, không tự liên hệ hay báo có người đã thử.

| Tác vụ | Ca thử quan trọng | Đáp án/chỉ số |
|---|---|---|
| Đọc cơ sở cổ tức | CFO/LNST cao nhưng CAPEX+D vượt CFO | Nhận ra thiếu bao phủ kỳ; không suy chắc chắn cắt cổ tức |
| Đọc lịch sử DPS | Có sự kiện tăng số cổ phiếu giữa hai lần quyền | Chỉ ra basis, phân biệt DPS giảm với tiền vị thế gốc |
| Chọn doanh nghiệp để đọc | Một mã đủ dữ liệu, một mã thiếu CAPEX/notice | Không coi thiếu là đạt; biết tài liệu cần lấy thêm |
| Đọc lịch trả | Notice hai profit_year, lịch sửa, chưa chứng cứ thực chi | Không tính trùng và không kết luận đã nhận |
| So sánh doanh nghiệp | CFO/net income đối nghịch bao phủ tiền | Giải thích trade-off bằng dữ kiện, không chọn chỉ tỷ số cao nhất |

Chấm: tỷ lệ nhận diện đúng vấn đề; lỗi kết luận thiếu căn cứ; dữ kiện trọng yếu bị bỏ sót; truy đúng nguồn; thời gian tác vụ. Hỏi người thử hành động tiếp theo, không hỏi chung “thấy tiện không” rồi dùng làm chứng minh giá trị. Người rà đáp án nên độc lập nếu có thể; người thực hiện tự chấm phải ghi giới hạn.

## 5. Ca số học đã làm trong khảo sát

Đã tính độc lập và lưu [JSON](illustrative-cases.json). Không chạy mã repository; không dùng số doanh nghiệp thật.

| Ca | Kết quả | Điều minh họa |
|---|---|---|
| CFO=120, CAPEX=80, D=60 | coverage 0,857; số dư −20 | CFO/LNST tốt chưa đủ để nói khoản chi được bao phủ |
| CFO=95, CAPEX=20, D=40 | coverage 1,583; số dư 35 | Phải xét nhu cầu sử dụng tiền, không chỉ chuyển đổi lợi nhuận |
| 100×1.000 → 120×900 | 100.000→108.000; +8% | DPS gốc giảm 10% nhưng khoản thu vị thế gốc tăng trong giả định quyền đủ |
| DPS=1.000, giá 20.000→10.000 | yield 5%→10% | Yield tăng không tự là cổ tức tăng |
| Thu nhập A/B=75/25; A giảm 50% | Tổng còn 62,5; giảm 37,5% | Mức tập trung thu nhập quyết định độ nhạy của khoản thu |
| Điểm yếu tố payout=100, streak=0; bỏ các yếu tố còn lại | Công thức trọng số minh họa tăng từ 30 lên 75 | Không nên để thiếu dữ liệu tạo vẻ an toàn hơn; không phải đánh giá cổ phiếu thật |

Ca cuối là tính riêng phép trung bình trọng số dựa trên cấu trúc trọng số đã đọc ở SALARY, giả định các yếu tố bỏ đi trước đó bằng 0. Không chứng minh dự án nguồn luôn cho điểm sai hoặc mọi dữ liệu thiếu đều tăng điểm.

## 6. Đề nghị thay đổi phạm vi để trao đổi với thầy

- Giữ thu thập, chuẩn hóa, truy nguồn, lifecycle và sáu chỉ tiêu làm nền.
- Thêm **một ca phân tích dòng tiền sau chi đầu tư/chi phân phối** có kiểm chứng; mục tiêu mở tổng quát chỉ sau gate nguồn/công sức. Tách capability phần mềm với việc nhập dòng bổ sung thủ công.
- Lưu sự kiện cổ phiếu tối thiểu hoặc đánh dấu chuỗi không so sánh được khi chưa xử lý. Đây là cách giải thích đúng giới hạn tiền mặt, không mở sang phân tích mọi corporate action ngay.
- Đưa kết quả vào **hồ sơ thẩm định** với câu hỏi, chứng cứ, phần thiếu và hành động cần nghiên cứu. Không tự thiết kế “điểm an toàn” chỉ để tạo cảm giác chức năng đầu tư.
- Lập CR, dictionary, acceptance tests và cập nhật bản nguồn Markdown của SRS khi chọn triển khai. Chưa sửa bản Word/slide hoặc nghiệm thu chỉ vì khảo sát GitHub xong.

Nội dung trao đổi trọng tâm: “Em bổ sung UC kiểm tra phần tiền kinh doanh sau chi đầu tư và phân phối, có nguồn từng dòng; đồng thời kiểm cơ sở cổ phiếu để không đọc sai tăng/giảm cổ tức. Em sẽ đo khả năng nhận diện đúng vấn đề bằng tác vụ so với bảng tổng hợp.” Đây là cách mô tả hướng làm, không phải lời tuyên bố đã xây xong.
