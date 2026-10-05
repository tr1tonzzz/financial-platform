# Báo cáo 1 — Nghiên cứu bối cảnh và đề xuất hướng đi project

**Đề tài:** Xây dựng hệ thống thu thập, chuẩn hóa và phân tích lợi nhuận, dòng tiền kinh doanh trong mối liên hệ với cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam.

**Ngày soạn:** 05/10/2026. **Trạng thái:** bản thảo để trao đổi với giảng viên. Báo cáo tập trung vào nghiên cứu ban đầu và đề xuất sản phẩm; chưa xác nhận đã hoàn thành hai tuần triển khai hoặc có ứng dụng hoạt động.

## Tóm tắt đề xuất

Project đề xuất xây dựng một hệ thống giúp người đọc BCTC trả lời ba câu hỏi liên quan: doanh nghiệp tạo ra bao nhiêu lợi nhuận, hoạt động kinh doanh tạo ra bao nhiêu tiền, và cổ tức tiền mặt công bố thay đổi thế nào trong bối cảnh đó. Hệ thống thu thập tài liệu công khai, chuẩn hóa dữ liệu, hỗ trợ kiểm tra số liệu và trình bày kết quả có thể mở lại nguồn.

Ví dụ sơ bộ từ BCTC kiểm toán DHG năm 2025 cho thấy LNST tăng **9,43%** so với cột năm 2024, nhưng dòng tiền kinh doanh giảm **7,94%**. Đây là một tình huống cụ thể mà việc chỉ đọc lợi nhuận chưa phản ánh đầy đủ diễn biến tạo tiền. Cầu nối dòng tiền giúp người đọc đi thêm một bước: xem nhóm khoản mục nào đóng góp số học vào khác biệt này. Số liệu và cách tính được trình bày tại mục 5, từ [BCTC DHG 2025, trang PDF 10–11](https://dhgpharma.com.vn/sites/default/files/2026-03/DHG-Audited-FS-2025-VN.pdf#page=10).

Phạm vi ban đầu là 3 doanh nghiệp phi tài chính, dữ liệu năm 2023–2025 và ít nhất một ca cầu nối CFO. Trọng tâm project là xây dựng, kiểm tra và đánh giá hệ thống dữ liệu; chưa đặt mục tiêu dự báo cổ tức hoặc đưa ra khuyến nghị đầu tư.

## 1. Bối cảnh đề tài

### 1.1. Lợi nhuận và dòng tiền cho biết những mặt khác nhau

Lợi nhuận thể hiện kết quả kinh doanh theo ghi nhận kế toán. Dòng tiền thuần từ hoạt động kinh doanh, viết tắt **CFO**, thể hiện dòng tiền vào và ra của hoạt động kinh doanh trong kỳ. Hai đại lượng có liên hệ nhưng không nhất thiết biến động cùng chiều. Chẳng hạn, doanh thu bán chịu có thể được ghi nhận trước khi thu tiền; khấu hao là chi phí kế toán không tạo ra khoản chi tiền tương ứng trong kỳ.

Báo cáo lưu chuyển tiền tệ phân loại dòng tiền thành hoạt động kinh doanh, đầu tư và tài chính. Với phương pháp gián tiếp, lợi nhuận được điều chỉnh bởi các khoản phi tiền, khoản dồn tích và các khoản liên quan hoạt động đầu tư/tài chính để xác định dòng tiền kinh doanh. Đây là cơ sở khái niệm cho việc đọc cầu nối lợi nhuận–tiền; khi xử lý BCTC Việt Nam vẫn phải dùng đúng mẫu và quy tắc của tài liệu nguồn. [IFRS Foundation — giới thiệu IAS 7](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/).

Vì vậy, một câu hỏi phù hợp cho project là: **khi lợi nhuận tăng, tiền từ hoạt động kinh doanh có tăng tương ứng không, và nếu khác chiều thì nên đọc tiếp khoản mục nào?** Câu hỏi này hướng tới đối chiếu số liệu, chưa mặc định đánh giá doanh nghiệp tốt hay xấu.

### 1.2. Cổ tức là lớp thông tin phân phối cần ghép đúng

Khi đối chiếu kết quả kinh doanh với cổ tức, cần phân biệt năm lợi nhuận được chia với năm công bố và lịch thanh toán. Một thông báo có thể gồm các phần thuộc nhiều năm. Ví dụ, thông báo VNM ngày 02/10/2025 nêu mức 2.850 đồng/cổ phiếu, gồm 350 đồng thuộc phần còn lại năm 2024 và 2.500 đồng thuộc tạm ứng đợt 1 năm 2025. Nếu gán toàn bộ số tiền vào một năm chỉ dựa trên ngày đăng thông báo, bảng phân tích sẽ bị sai. [Thông báo VSDC về VNM](https://vsdc.vn/vi/ad1/187729).

Cổ tức tiền mặt công bố theo năm lợi nhuận là dữ liệu chính mà project muốn đối chiếu. Khoản tiền đã chi cho chủ sở hữu trong BCTC là một góc nhìn khác theo kỳ thực chi. Hai dữ liệu này cần giữ riêng; lịch thanh toán cũng chưa phải bằng chứng xác nhận đã trả.

### 1.3. Nguồn công khai tạo điều kiện triển khai, nhưng cần xử lý

Nguồn mục tiêu là trang quan hệ cổ đông của doanh nghiệp, BCTC năm kiểm toán và thông báo thực hiện quyền từ VSDC hoặc doanh nghiệp. Trường hợp DHG cho thấy có thể lấy tài liệu trực tiếp từ trang công bố chính thức để đọc các chỉ tiêu cần thiết. [Trang công bố BCTC DHG năm 2025](https://dhgpharma.com.vn/vi/co-dong/10533-bao-cao-tai-chinh-kiem-toan-nam-2025-va-giai-trinh-chenh-lech).

Tuy nhiên, có tài liệu công khai chưa đồng nghĩa có ngay một tập dữ liệu phân tích đúng. Người xử lý vẫn phải xác định kỳ báo cáo, đơn vị, phạm vi báo cáo, cột năm, các dòng cần lấy và tình trạng đầy đủ của lịch sử cổ tức. Bối cảnh này tạo ra một bài toán công nghệ thông tin cụ thể: đưa tài liệu rời rạc thành dữ liệu có cấu trúc và kết quả kiểm chứng được.

Các nguồn trên đủ để đặt bài toán và thử một ví dụ ban đầu. Báo cáo chưa phải tổng quan học thuật hệ thống, khảo sát người dùng hay bằng chứng về nhu cầu trả phí cho sản phẩm.

## 2. Project giải quyết vấn đề gì và vì sao cần thiết

Người dùng dự kiến là sinh viên, người nghiên cứu và người đọc BCTC cần theo dõi một số doanh nghiệp. Người vận hành hệ thống thu thập và duyệt dữ liệu; người đọc sử dụng bảng phân tích và mở nguồn để kiểm tra nhận xét.

Tình huống sử dụng giả định: một người đọc thấy doanh nghiệp công bố lợi nhuận tăng và muốn biết diễn biến này có đi cùng dòng tiền và cổ tức hay không. Khi tự làm, người đó phải tải từng BCTC, nhập số, đổi đơn vị, tìm các đợt cổ tức rồi ghép theo năm. Sau khi thấy biến động khác chiều, họ lại mở báo cáo để tìm khoản mục liên quan. Đây là tác vụ project muốn hỗ trợ.

| Vấn đề trong tác vụ | Hệ quả có thể gặp | Cách project hỗ trợ |
|---|---|---|
| Phải gom nhiều BCTC và thông báo | Lặp lại việc tìm tài liệu và nhập số | Thu thập theo danh mục, lưu nguồn cùng dữ liệu |
| Số ở các báo cáo có đơn vị, kỳ hoặc phạm vi khác nhau | So sánh hoặc tính tỷ số sai | Chuẩn hóa và kiểm tra trước khi tính |
| Chỉ nhìn lợi nhuận hoặc một tỷ số | Bỏ qua diễn biến CFO và khoản mục cần đọc tiếp | Hiển thị lợi nhuận–CFO và cầu nối theo ca |
| Cổ tức có nhiều đợt, nhiều năm hoặc bản sửa | Cộng trùng, gán sai năm lợi nhuận | Tách thành phần, liên kết bản sửa và giữ lịch sử |
| Chưa tìm thấy thông báo nhưng điền bằng 0 | Nhận xét sai rằng doanh nghiệp không chia hoặc cổ tức giảm | Hiển thị dữ liệu thiếu và mức đã rà nguồn |
| Kết quả chỉ là một bảng số không có nguồn | Khó kiểm tra hoặc làm lại khi tài liệu thay đổi | Lưu trang nguồn, số đầu vào, công thức và bản dữ liệu đã dùng |

Sự cần thiết của project nằm ở khả năng kết hợp **thu thập đúng, so sánh đúng và kiểm tra lại được** trong một luồng sử dụng. Có thể dùng bảng tính để tính các tỷ số; phần hệ thống cần chứng minh là hỗ trợ công việc gom nguồn, kiểm soát cách ghép và giữ bằng chứng khi dữ liệu cập nhật.

Lợi ích kỳ vọng là giảm thao tác lặp và giúp người đọc kiểm tra kết quả thuận tiện hơn. Chưa có phép đo để khẳng định tiết kiệm bao nhiêu thời gian; cần đánh giá trên cùng một tác vụ thủ công và tác vụ có hệ thống sau khi triển khai.

## 3. Hướng đi project được đề xuất

### 3.1. Mục tiêu và đầu ra

Đề xuất một hệ thống phân tích dữ liệu với câu chuyện sử dụng xuyên suốt:

**Chọn doanh nghiệp → xem lợi nhuận và CFO → đọc một ca biến động khác chiều → kiểm tra cầu nối và nguồn → đối chiếu cổ tức thuộc năm lợi nhuận → lưu kết quả phân tích.**

Đầu ra cuối project gồm ứng dụng chạy cục bộ, tập dữ liệu pilot có nguồn, ít nhất một ca cầu nối CFO kiểm tra được và hồ sơ đánh giá chất lượng/công sức. Đây là mục tiêu phát triển, chưa phải các đầu ra đã hoàn thành.

### 3.2. Phạm vi ban đầu

- Pilot 3 doanh nghiệp niêm yết **phi tài chính** × năm 2023–2025; danh sách cụ thể cần kiểm tra đủ nguồn trước khi chốt.
- Sáu chỉ tiêu BCTC lõi: tổng LNST, CFO, tiền và tương đương tiền, tổng tài sản, nợ phải trả và vốn chủ sở hữu.
- Thông báo cổ tức tiền mặt liên quan các năm lợi nhuận trong mẫu, kể cả thông báo đăng vào năm sau.
- Cầu nối từ lợi nhuận đến CFO cho ít nhất một ca có đủ dữ liệu; mục tiêu 1–3 ca nếu nguồn và công sức cho phép.
- Mở 5–8 doanh nghiệp chỉ sau đánh giá công sức; giữ rõ phạm vi riêng/hợp nhất và không trộn chúng trong một phép tính.

Ở giai đoạn project, chưa triển khai dự báo giá, khuyến nghị mua bán, chatbot tài chính hoặc crawl toàn thị trường. Nhánh tốt nghiệp ưu tiên nghiên cứu đối chiếu phiên bản nguồn và ảnh hưởng tới kết quả phân tích; dự đoán cổ tức chỉ là phương án sau khi có dữ liệu và thiết kế đánh giá phù hợp.

### 3.3. Cách triển khai sơ bộ

Luồng xử lý dự kiến là **tài liệu gốc → trích số → chuẩn hóa → kiểm tra và duyệt → lưu dữ liệu → phân tích và mở nguồn**. Báo cáo có văn bản dùng bộ đọc PDF; tài liệu scan thử OCR và đưa kết quả chưa chắc chắn vào hàng đợi duyệt. Cầu nối theo ca có thể nhập tay từ nguồn thật trong giai đoạn đầu, nhưng phải ghi rõ phần được hỗ trợ thủ công.

Stack dự kiến là Python cho thu thập/xử lý, SQLite cho lưu trữ và Streamlit cho giao diện. Tính toán dùng quy tắc xác định; chưa cần bổ sung AI để thực hiện các chức năng lõi. Chi tiết yêu cầu tham chiếu [SRS v3.1](../../22-srs-dac-ta-yeu-cau-phan-mem.md), còn báo cáo này chỉ trình bày hướng đi ở mức đề xuất.

## 4. Những chức năng dự kiến và lý do cần có

| Nhóm chức năng | Người dùng làm được gì | Vì sao cần |
|---|---|---|
| 1. Quản lý danh mục và nguồn | Chọn doanh nghiệp, năm, xem tài liệu đã có và còn thiếu | Giữ phạm vi pilot rõ ràng |
| 2. Thu thập tài liệu | Tìm/tải BCTC và thông báo, lưu ngày lấy và bản gốc | Giảm việc gom nguồn lặp lại, giữ bằng chứng |
| 3. Trích và chuẩn hóa dữ liệu | Lấy chỉ tiêu, đổi đơn vị, xác định đúng cột/kỳ/phạm vi | Tạo đầu vào có thể so sánh |
| 4. Kiểm tra và duyệt | Xem số cạnh nguồn, sửa lỗi có lịch sử; chặn phép tính thiếu dữ liệu | Kiểm soát lỗi PDF/OCR và nhập tay |
| 5. Quản lý sự kiện cổ tức | Tách phần theo năm lợi nhuận, xem các đợt, bản sửa và lịch | Tránh gán sai năm, trùng tiền hoặc suy lịch là thực trả |
| 6. Phân tích lợi nhuận–CFO–cổ tức | Xem biến động, tỷ số hợp lệ và ca khác chiều | Trả lời câu hỏi chính của đề tài |
| 7. Cầu nối CFO theo ca | Xem điểm đầu lợi nhuận, nhóm điều chỉnh và phần chưa khớp | Đi từ phát hiện khác biệt tới khoản mục cần đọc sâu |
| 8. Truy nguồn và lưu kết quả | Mở nguồn của số/công thức; lưu bộ dữ liệu cố định để tính lại | Làm kết quả có thể kiểm chứng sau cập nhật |

Đối với cầu nối gián tiếp của mẫu DHG, điểm đầu là **lợi nhuận trước thuế (LNTT)**. LNST vẫn được hiển thị riêng để so với CFO. Các dòng tổng trung gian chỉ dùng kiểm tra, không cộng lại cùng các dòng thành phần. Khi không đủ dữ liệu, hệ thống phải báo phần thiếu thay vì tự tạo một nguyên nhân giải thích.

Đóng góp công nghệ thông tin cần đánh giá gồm pipeline thu thập, chuẩn hóa có kiểm soát, mô hình dữ liệu cổ tức, truy nguồn và tái lập kết quả. Việc kết hợp lợi nhuận, dòng tiền và cổ tức chưa đủ để tự tuyên bố tính mới học thuật hoặc ưu thế so với mọi sản phẩm đang có.

## 5. Ví dụ phân tích thử từ BCTC DHG năm 2025

### 5.1. Nguồn và phạm vi minh họa

Ví dụ sử dụng **BCTC kiểm toán năm 2025 của Công ty Cổ phần Dược Hậu Giang**, công bố trên website doanh nghiệp. Bảng kết quả kinh doanh ở trang PDF 10/trang in 8; bảng lưu chuyển tiền tệ ở trang PDF 11/trang in 9. Đơn vị gốc là VND. Cột 2024 là cột so sánh trong bản báo cáo 2025, chưa phải một bản BCTC 2024 riêng được đối chiếu. [BCTC nguồn](https://dhgpharma.com.vn/sites/default/files/2026-03/DHG-Audited-FS-2025-VN.pdf#page=10).

Ví dụ được lập ban đầu từ số chép và đối chiếu thủ công. Sau đó đã chạy crawler, bộ đọc PDF và OCR để thử tái tạo bốn số LNST/CFO; kết quả và lỗi thực ở mục 5.6. Phần cầu nối/cổ tức vẫn dựa trên đối chiếu thủ công, chưa trích tự động đầy đủ hay đánh giá độc lập. Bảng dưới quy đổi sang tỷ đồng và làm tròn ba chữ số thập phân; phép tính dùng số VND gốc. Chi tiết tại [phụ lục ví dụ DHG](vi-du-phan-tich-dhg.md).

### 5.2. Lợi nhuận tăng trong khi CFO giảm

| Chỉ tiêu | 2024 — cột so sánh | 2025 | Thay đổi |
|---|---:|---:|---:|
| LNST, tỷ đồng | 778,920 | 852,354 | +73,434 tỷ; +9,43% |
| CFO, tỷ đồng | 1.317,583 | 1.212,968 | −104,616 tỷ; −7,94% |
| CFO/LNST, lần | 1,692 | 1,423 | Giảm khoảng 0,268 lần |

Tăng trưởng được tính bằng `(giá trị năm 2025 / giá trị cột 2024 − 1) × 100%`. Tỷ số CFO/LNST dùng hai chỉ tiêu cùng kỳ và phạm vi; LNST của cả hai cột đều dương.

Kết quả cho thấy doanh nghiệp có lợi nhuận tăng, nhưng tiền thuần từ hoạt động kinh doanh không tăng cùng chiều. CFO vẫn dương và lớn hơn LNST trong cả hai cột. Từ dữ liệu này chưa thể kết luận chất lượng lợi nhuận xấu hoặc khả năng chi trả cổ tức suy giảm; điều có thể làm là chọn ca để đọc tiếp BCLCTT.

### 5.3. Minh họa cầu nối ở mức nhóm khoản mục

| Thành phần cầu nối, tỷ đồng | 2024 — cột so sánh | 2025 | Đóng góp vào thay đổi CFO |
|---|---:|---:|---:|
| LNTT — điểm bắt đầu | 904,485 | 986,599 | +82,115 |
| Nhóm điều chỉnh dòng 02–06 | 60,779 | 64,554 | +3,775 |
| Nhóm thay đổi vốn lưu động dòng 09–12 | 517,633 | 344,523 | −173,110 |
| Lãi vay, thuế và chi khác HĐKD dòng 14, 15, 17 | −165,313 | −182,708 | −17,395 |
| **CFO — kết quả cộng** | **1.317,583** | **1.212,968** | **−104,616** |

Phép cộng từ các dòng VND gốc khớp CFO báo cáo của cả hai cột; phần chênh chưa khớp (**residual**) bằng 0. Nhóm vốn lưu động đóng góp −173,110 tỷ đồng vào thay đổi CFO, trong khi LNTT đóng góp dương. Điều này cho thấy nhận xét “CFO giảm do lợi nhuận giảm” không phù hợp với số liệu của ca này. Muốn giải thích nguyên nhân kinh doanh phía sau, cần đọc thêm thuyết minh và giải trình; báo cáo 1 dừng ở phân rã số học.

### 5.4. Liên hệ sơ bộ với góc dòng tiền chi cho chủ sở hữu

Dòng 36 của BCLCTT 2025 ghi **“Cổ tức, lợi nhuận đã trả cho chủ sở hữu”**, độ lớn khoảng **1.307,461 tỷ đồng**. So với CFO khoảng 1.212,968 tỷ đồng cùng kỳ, tỷ số CFO/độ lớn khoản chi này khoảng **0,928 lần**. Đây là đối chiếu hai dòng tiền trong kỳ từ [BCLCTT DHG, trang PDF 11](https://dhgpharma.com.vn/sites/default/files/2026-03/DHG-Audited-FS-2025-VN.pdf#page=11).

Khoản chi đó chưa được gán thành “cổ tức từ lợi nhuận năm 2025”. Ví dụ hiện chưa có lịch sử thông báo DHG đủ để lập chuỗi cổ tức công bố theo năm lợi nhuận; phần đó cần bổ sung sau. Tỷ số trên cũng chưa xác định nguồn riêng tài trợ cổ tức hoặc mức cổ tức tương lai.

### 5.5. Kết quả ví dụ minh họa cho sản phẩm

Trong giao diện dự kiến, người đọc sẽ thấy bảng LNST/CFO, chọn ca khác chiều, mở bảng cầu nối và bấm vào trang nguồn. Khi chuyển sang cổ tức, giao diện phân biệt mức công bố theo năm lợi nhuận với dòng tiền đã chi trong kỳ; phần chưa đủ dữ liệu được ghi rõ.

Ví dụ cho thấy có nguồn thật để thử câu hỏi phân tích và phép kiểm tra tổng. Thử nghiệm công cụ dưới đây bổ sung bằng chứng cho một đoạn pipeline nhỏ; chưa chứng minh độ chính xác tổng thể, độ phủ nhiều doanh nghiệp hay mức tiết kiệm thời gian.

### 5.6. Thử nghiệm công cụ để kiểm tra tính khả thi

Ngày 05/10/2026 đã chạy thử **crawler → đọc PDF → OCR hai trang → trích số → tính chỉ tiêu** trên chính báo cáo DHG dùng ở ví dụ. Phạm vi nhỏ giúp kiểm tra hướng triển khai mà chưa cần làm toàn bộ ứng dụng.

| Thử nghiệm | Kết quả thực |
|---|---|
| Crawler Python `urllib`/`lxml` trên một trang danh mục DHG | Tìm 12 liên kết PDF ứng viên, chọn và tải thành công hai kỳ FY2025/H1-2026; chạy lại nhận 2/2 HTTP 304 |
| Đọc bản FY2025 bằng `pypdf` | 12 trang đầu đều trả về 0 ký tự, gồm hai trang cần dùng; chuyển sang OCR |
| Poppler 220 DPI + Tesseract.js tiếng Việt/Anh | OCR được trang PDF 10–11, khoảng 7,413 giây nhận dạng hai trang, chưa tính khởi tạo và duyệt |
| Parser nhỏ tìm nhãn dòng, đọc hai cột VND | Sáu ô được đối chiếu: 5 đúng, 1 sai, 0 thiếu; bốn ô LNST/CFO đều khớp |
| Phân tích từ bốn ô LNST/CFO trích được | Tái tạo LNST +9,43%, CFO −7,94% và CFO/LNST 2025 khoảng 1,423 lần |

Lỗi thực nằm ở điều chỉnh tỷ giá năm 2025: OCR đọc **−246.438.677** thay vì **−246.436.677 VND**, lệch −2.000 đồng. Một số nhãn/mã dòng khác cũng bị đọc sai. Đây là lý do cần giữ trang nguồn, duyệt số và kiểm tổng, dù số OCR đã đúng định dạng.

Kết quả hỗ trợ tính khả thi ban đầu của luồng thu thập và trích ứng viên. Sáu ô là mẫu phát triển được đối chiếu cùng người; nhãn được chọn trước, trang/đơn vị/năm/scope còn kiểm thủ công. Chưa đo accuracy độc lập, chưa trích đủ sáu fact pilot hay toàn bộ cầu nối, và chưa thử crawler thông báo cổ tức. Cách chạy, phiên bản công cụ, số gốc, lỗi và log ở [phụ lục thử nghiệm công cụ](thu-nghiem-cong-cu.md).

## 6. Đánh giá ban đầu và bước tiếp theo

Hướng project có cơ sở để tiếp tục thử nghiệm: nguồn công khai cung cấp các bảng cần đọc; ca DHG minh họa lợi nhuận và CFO khác chiều; crawler/OCR đã chạy trên mẫu nhỏ và tái tạo được chỉ tiêu chính; thông báo VNM minh họa việc phải tách cổ tức theo năm. Lỗi OCR quan sát được cho thấy rủi ro công sức duyệt PDF, bên cạnh lịch sử cổ tức chưa đủ và khả năng ghép sai context. Vì vậy, nên hoàn thiện luồng nhỏ có review trước khi tăng số doanh nghiệp.

Ba đầu ra tiếp theo được đề xuất:

1. **Chốt danh mục pilot và bảng nguồn:** xác định 3 doanh nghiệp, nguồn BCTC 2023–2025, phạm vi báo cáo và nơi rà thông báo cổ tức; ghi rõ năm/tài liệu còn thiếu.
2. **Làm một luồng dữ liệu đến kết quả:** một BCTC và các thông báo của cùng doanh nghiệp đi tới số đã kiểm tra, bảng phân tích và nguồn mở được; ghi riêng tự động và nhập hỗ trợ.
3. **Thiết kế phép đánh giá:** lập bảng đối chiếu thủ công, nhóm lỗi cần kiểm và cách đo phút xử lý/review; dùng dữ liệu khác mẫu phát triển khi đánh giá độc lập.

Nội dung cần trao đổi với giảng viên là mức độ phù hợp của bài toán hệ thống dữ liệu, phạm vi pilot, chiều sâu cầu nối theo ca và tiêu chí nghiệm thu. Báo cáo chưa ghi nhận các nội dung này đã được phê duyệt.

## Tài liệu tham khảo và hồ sơ liên quan

- [IFRS Foundation — IAS 7](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/): nguồn khái niệm dòng tiền/phương pháp trình bày, không thay chế độ kế toán của BCTC Việt Nam.
- [DHG — trang công bố BCTC kiểm toán năm 2025](https://dhgpharma.com.vn/vi/co-dong/10533-bao-cao-tai-chinh-kiem-toan-nam-2025-va-giai-trinh-chenh-lech) và [PDF nguồn](https://dhgpharma.com.vn/sites/default/files/2026-03/DHG-Audited-FS-2025-VN.pdf): số liệu ví dụ tại trang PDF 10–11.
- [VSDC — thông báo VNM ngày 02/10/2025](https://vsdc.vn/vi/ad1/187729): ví dụ một thông báo gồm thành phần cổ tức của hai năm, tách biệt với ca tài chính DHG.
- [SRS v3.1](../../22-srs-dac-ta-yeu-cau-phan-mem.md) và [kế hoạch 13 tuần](../../04-ke-hoach-13-tuan.md): phạm vi/yêu cầu và lộ trình triển khai.
- [Phụ lục ví dụ DHG](vi-du-phan-tich-dhg.md): số gốc, phép tính và vị trí đối chiếu.
- [Phụ lục thử nghiệm công cụ](thu-nghiem-cong-cu.md): crawler, đọc PDF/OCR và đối chiếu sáu ô đã chạy thực ngày 05/10/2026.

Các trang DHG, IFRS và VSDC được mở kiểm tra ngày 05/10/2026. Các tài liệu trên được chọn để xác lập bài toán và minh họa ban đầu; báo cáo chưa thực hiện khảo sát toàn bộ sản phẩm hoặc tổng quan học thuật đầy đủ.
