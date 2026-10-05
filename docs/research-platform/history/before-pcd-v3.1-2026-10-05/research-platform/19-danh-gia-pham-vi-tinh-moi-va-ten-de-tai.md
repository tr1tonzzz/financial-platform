# Đánh giá phạm vi tính mới và lựa chọn tên đề tài

Ngày khảo sát: **04/10/2026**. Đề tài đang dùng: **Xây dựng hệ thống thu thập, chuẩn hóa và phân tích dữ liệu lợi nhuận, dòng tiền kinh doanh và cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam.**

**Lượt nghiên cứu tiếp theo cùng ngày:** [nghiên cứu lần hai và quyết định cuối](20-nghien-cuu-lan-hai-va-chot-de-tai.md) giữ tên/phạm vi và ưu tiên đối chiếu phiên bản/ảnh hưởng cho đồ án. Phần dự đoán ở mục 6 dưới đây phản ánh hướng nối tiếp của lượt trước, nay giữ làm tùy chọn sau gate dữ liệu; không còn là hướng ưu tiên mặc định.

## 1 Kết luận để quyết định

**Đề tài không quá nhỏ để làm project CNTT có hệ thống phần mềm và kiểm định; có cơ sở phát triển lên đồ án.** Đánh giá này dựa trên phạm vi SRS: tự tìm/tải tài liệu, đọc PDF/OCR, chuẩn hóa, duyệt dữ liệu, ghép cổ tức theo năm lợi nhuận, xử lý phiên bản/sửa/hủy, phân tích và truy nguồn. Chưa có rubric của trường để kết luận chắc chắn đạt yêu cầu đồ án.

Người thực hiện xác nhận trong cuộc trao đổi ngày 04/10/2026 rằng đồ án được chấm chủ yếu theo hướng **xây dựng hệ thống phần mềm**. Vì vậy, ưu tiên hoàn thiện hệ thống, chất lượng xử lý và luồng sử dụng; không tự đặt yêu cầu phải phát minh mô hình AI mới để đề tài được xem là đủ lớn.

**Ý tưởng tài chính không hoàn toàn mới.** Nghiên cứu Việt Nam đã xét lợi nhuận/dòng tiền với chính sách cổ tức; thị trường đã có công cụ BCTC và lịch cổ tức. Hướng dự đoán giảm cổ tức cũng có dự án công khai ở thị trường khác. Do đó, cần trình bày phần triển khai và đánh giá của mình, không tuyên bố phát hiện quan hệ tài chính mới hoặc hệ thống đầu tiên.

**Điểm nhấn nên giữ:** dữ liệu tự thu từ tài liệu/công bố chính thức, ghép đúng năm và vòng đời sự kiện, xử lý thiếu/phạm vi/cơ sở cổ phiếu, kết quả có bằng chứng và tái lập được. Đây là định hướng đóng góp kỹ thuật cần chứng minh, chưa là kết quả đã đạt hoặc độc quyền khác biệt với mọi sản phẩm.

Không cần mở đề tài sang giá cổ phiếu, quản lý danh mục và hỏi đáp AI chỉ để tên trông lớn hơn. Cần làm sâu luồng dữ liệu và kiểm định trước khi mở phạm vi.

## 2 Có nhỏ quá hay không phụ thuộc vào sản phẩm thực hiện

| Cách thực hiện | Đánh giá phạm vi | Vì sao |
|---|---|---|
| Nhập tay vài bảng, tính tỷ số và vẽ biểu đồ | Dễ bị xem là mỏng cho đề tài hệ thống | Phần mềm ít xử lý dữ liệu thật, đóng góp kỹ thuật/kiểm định còn hạn chế |
| Gọi thư viện dữ liệu bên thứ ba rồi hiển thị kết quả | Có thể hữu ích nhưng cần đóng góp thêm rõ ràng | Truy xuất BCTC/sự kiện đã có công cụ; chưa chứng minh tự thu từ tài liệu gốc và xử lý lỗi nghiệp vụ |
| Hoàn thành pipeline và ứng dụng theo SRS, có dữ liệu thật và đánh giá | Có đủ chiều sâu để đề xuất làm project CNTT | Nhiều bài toán kỹ thuật liên kết; người dùng kiểm chứng được kết quả |
| Mở rộng lên đồ án với một câu hỏi và đánh giá mới, dữ liệu phù hợp | Có hướng phát triển, phải qua điều kiện khả thi | Đóng góp thêm nằm ở kỹ thuật dữ liệu/đánh giá hoặc dự báo đã kiểm định, không chỉ tăng số biểu đồ |

Ngách nghiệp vụ tập trung không đồng nghĩa hệ thống ít việc. Ví dụ một thông báo cổ tức gộp hai năm, được đăng ở hai nơi và có bản sửa đã cần mô hình sự kiện, liên kết nguồn, trạng thái có hiệu lực, tính tổng và lịch sử. Đọc đúng sáu số từ PDF ảnh còn cần xác định kỳ, đơn vị, phạm vi và vị trí bằng chứng.

### 2.1 Những phần đủ tạo chiều sâu cho project hiện tại

| Phần phải xây dựng | Vấn đề kỹ thuật phải xử lý | Bằng chứng để bảo vệ |
|---|---|---|
| Thu thập tự động | Danh mục, phân trang, nhận diện loại/kỳ, tải lỗi, cập nhật nguồn | Log tự phát hiện BCTC và cổ tức; phần nhập hỗ trợ đếm riêng |
| Trích/chuẩn hóa | PDF chữ/ảnh, OCR, nhầm cột, nghìn/triệu, dấu âm | Số gốc và số chuẩn; đối chiếu trước/sau review trên tập đã chốt |
| Mô hình tài chính/sự kiện | Kỳ–phạm vi, một notice nhiều năm, nhiều nguồn cùng đợt, sửa/hủy | Schema, ca khó có nguồn, aggregate đúng và tests nghiệp vụ |
| Chất lượng/phiên bản | Thiếu khác 0, chưa duyệt khác đã xác nhận, nguồn sửa không mất bản cũ | Coverage, audit, snapshot trước/sau, chạy lại không trùng |
| Phân tích/ứng dụng | Điều kiện tính, truy ngược số đầu vào, đọc cùng/khác chiều | Bảng/chart/timeline, ba case thật, export tái tính được |
| Đánh giá giá trị sử dụng | Tự động đúng bao nhiêu, còn sửa tay bao nhiêu, có giảm công sức không | Baseline text-only/OCR/review; chất lượng, độ phủ, thời gian và nhiệm vụ người dùng nếu có |

Các thư viện PDF/OCR, database hoặc dashboard không tự là đóng góp. Đóng góp nằm ở cách tổ chức, xử lý các ca thật và số đo cho thấy luồng làm đúng đến đâu.

### 2.2 Nhận định thẳng về cỡ dữ liệu

Pilot 3 doanh nghiệp × 3 năm là bước kiểm tra khả thi, chưa là quy mô cuối cùng. Mục tiêu hiện hành 5–8 doanh nghiệp, 15–24 BCTC năm là mẫu nhỏ về thống kê, nhưng có thể dùng để đánh giá một project phần mềm nếu phân biệt dữ liệu phát triển, dữ liệu đánh giá và ca khó.

**Không dùng 15–24 quan sát để hứa khám phá quan hệ phổ quát, nhân quả hoặc mô hình dự đoán đáng tin cậy.** Đánh giá extraction có thể xét nhiều ô/chỉ tiêu và trường sự kiện, nhưng số ô trích không tự biến thành từng ấy quan sát độc lập cho nghiên cứu tài chính. Nhãn dự báo cần nhiều kỳ/doanh nghiệp hơn, đủ trường hợp giảm, độ đầy đủ và cửa sổ kết quả đã khép.

Đây là đánh giá phương pháp cho phạm vi của bạn, không phải một ngưỡng số công ty được trường quy định.

## 3 Đã có ai nghiên cứu vấn đề tài chính này chưa

**Có.** Các nguồn dưới đây là bài trên trang tạp chí/nhà xuất bản hoặc đại học. Trong lượt này đã đọc metadata và abstract; chưa tái lập mô hình, kiểm định dữ liệu hay đánh giá toàn bộ phương pháp của bài.

| Công trình | Nội dung đã kiểm tra | Liên quan đến đề tài | Khác biệt cần giữ rõ |
|---|---|---|---|
| Pascal Alphonse và Quoc Trung Tran, *A Two-Step Approach to Investigate Dividend Policy: Evidence from Vietnamese Stock Market*, 2014, DOI 10.5539/ijef.v6n3p16 | Abstract xét quyết định có chia và mức chia; có biến lợi nhuận và dòng tiền tự do | Quan hệ tài chính và việc chia cổ tức ở Việt Nam đã được nghiên cứu | Phân tích kinh tế lượng; không phải bằng chứng về pipeline tự đọc PDF/ghép notice của project. [Nguồn nhà xuất bản](https://www.ccsenet.org/journal/index.php/ijef/article/view/32728) |
| Do Thi Van Trang, *Determinants of Dividend Payout Policy A Case of Nonfinancial Listed Companies in Vietnam*, 2016 | Abstract nêu 156 công ty, giai đoạn 2009–2014; xét FCF, lợi nhuận, thanh khoản, đòn bẩy và biến khác | Trùng đối tượng doanh nghiệp phi tài chính Việt Nam và nhiều nhóm biến liên quan | Tỷ lệ chi trả và nghiên cứu yếu tố khác tổng DPS công bố theo năm lợi nhuận. [Nguồn VNU](https://js.vnu.edu.vn/EAB/article/view/4059) |
| Chau Anh Vu, *The impact of the free cash flow and the firm’s life cycle on dividend policy: Evidence from Vietnam’s listed firms*, 2023, DOI 10.22144/ctu.jen.2023.026 | Abstract nêu 110 công ty HOSE, 2014–2020; FCF, vòng đời, dividend payout ratio; FEM/REM/GMM | Dòng tiền và cổ tức không phải quan hệ mới tại Việt Nam | FCF không đồng nhất CFO; công trình nghiên cứu chính sách chi trả, không tự tái lập bằng CFO/LNST và DPS của project. [Nguồn CTU](https://ctujs.ctu.edu.vn/index.php/ctujs/article/view/583) |
| Nguyen Do Quyen và Bui Quang Huy, *Factors affecting firm’s propensity to pay dividends: Evidence from Vietnam’s listed companies*, 2016 | Abstract xét xu hướng có chia cổ tức của công ty phi tài chính HOSE, 2009–2015 | Ngay câu hỏi có/không chia ở Việt Nam cũng đã có nghiên cứu | Không đồng nghĩa đã xây hệ thống tương tự toàn bộ đề tài. [Nguồn FTU](https://jiem.ftu.edu.vn/index.php/jiem/article/view/154) |

Không dùng kết quả tổng hợp của các bài để kết luận một doanh nghiệp cụ thể sẽ giảm cổ tức. Chúng phục vụ phần nghiên cứu liên quan và xác định phạm vi đóng góp của mình.

## 4 Đã có phần mềm hoặc dự án gần ý tưởng chưa

**Có các chức năng và dự án gần.** Việc kiểm tra dưới đây dựa trên tài liệu công khai, chưa đăng nhập tài khoản trả phí, chạy thư viện hoặc benchmark phần mềm.

| Công cụ/dự án | Điều đã quan sát công khai | Phần giao nhau với đề tài | Giới hạn kết luận |
|---|---|---|---|
| VietstockFinance | Trang doanh nghiệp có mục BCTC/tài liệu cổ đông và lịch cổ tức/phát hành thêm | Hồ sơ doanh nghiệp, BCTC, sự kiện cổ tức | Chưa kiểm tra toàn bộ logic ghép/phiên bản và chức năng trong tài khoản; không khẳng định họ thiếu truy vết. [Trang VNM](https://finance.vietstock.vn/VNM-ctcp-sua-viet-nam.htm) |
| FiinTrade | Tài liệu hướng dẫn công khai mô tả biểu đồ doanh thu/lợi nhuận/dòng tiền và sự kiện BCTC/cổ tức | Dashboard tài chính và sự kiện doanh nghiệp | Tài liệu 2021 là bằng chứng chức năng đã có, chưa là khảo sát toàn bộ phiên bản hiện tại; mở PDF không ổn định trong lượt này, dùng mô tả được chỉ mục trên nguồn chính thức. [Hướng dẫn 07/2021](https://web.fiintrade.vn/upload/docs/FiinTrade-Tai-lieu-huong-dan-su-dung-072021.pdf) |
| Vnstock | README gốc có truy xuất/chuẩn hóa nguồn bên thứ ba, BCTC gồm cân đối, kết quả kinh doanh, dòng tiền; sự kiện doanh nghiệp | Phần thu/truy xuất và chuẩn hóa dữ liệu Việt Nam | Chưa chạy/kiểm tra chất lượng hay toàn bộ dữ liệu sự kiện. Phiên bản hiện tại là mã nguồn công khai theo giấy phép riêng, không tự gắn nhãn nguồn mở cho mọi phiên bản. [Repository gốc](https://github.com/thinh-vu/vnstock) |
| CoTuc | Trang công khai hiển thị lịch sự kiện và loại cổ tức tiền mặt/cổ phiếu | Theo dõi sự kiện cổ tức Việt Nam | Chưa kiểm chứng lịch sử đầy đủ, phương pháp thu nguồn hoặc chất lượng; không sử dụng số trang này làm gold. [Trang sản phẩm](https://cotuc.vn/en) |
| DataCore-VietNam/vn-corporate-actions | README có sổ sự kiện, cổ tức tiền mặt/cổ phiếu, chia tách và điều chỉnh chuỗi giá | Xử lý corporate actions/cơ sở cổ phiếu có tiền lệ mã nguồn công khai | Trọng tâm là điều chỉnh giá/khối lượng; chưa kiểm tra code và không mặc định cơ chế điều chỉnh giá dùng nguyên cho tổng DPS. [Repository](https://github.com/DataCore-VietNam/vn-corporate-actions) |
| Research-SLIIT, project 2025/26 | Trang nhóm mô tả nền tảng thị trường Colombo, luồng tài liệu/ETL và thành phần dự đoán giảm cổ tức bằng Logistic Regression | Hướng tốt nghiệp thu dữ liệu và dự đoán giảm cổ tức cũng có dự án gần ở thị trường khác | Đây là mô tả do nhóm công bố, chưa chạy code/tái lập; số accuracy/AUC họ nêu không dùng làm bằng chứng hiệu quả đã xác minh. [Trang nhóm dự án](https://github.com/Research-SLIIT) |

Như vậy, “website có dữ liệu tài chính và cổ tức”, “crawler”, “dashboard”, “xử lý sự kiện” hay “thêm ML dự đoán cổ tức” đều không đủ để tuyên bố mới toàn cầu. Vẫn có thể xây một hệ thống độc lập cho phạm vi cụ thể và chứng minh chất lượng bằng thực nghiệm.

## 5 Phần nào có thể là đóng góp của bạn

### 5.1 Phân biệt ba nghĩa của tính mới

| Nghĩa | Đánh giá hiện tại |
|---|---|
| Ý tưởng tài chính chưa ai biết | Không: đã có nghiên cứu liên quan |
| Chưa ai từng có phần mềm cùng nhóm chức năng | Không: có BCTC/lịch cổ tức, công cụ dữ liệu và dự án gần |
| Công trình do bạn tự thiết kế/triển khai/đánh giá, có khác biệt được chứng minh trong phạm vi | Có thể đạt, nhưng phải nộp artifact và so sánh cụ thể; chưa chứng minh bằng tên đề tài |

Một tổ hợp xử lý nguồn Việt Nam có kiểm định có thể là đóng góp ứng dụng/kỹ thuật của đồ án. Đây là nhận định chuyên môn, không thay tiêu chí tính mới của giảng viên. Nếu trường bắt buộc phương pháp nghiên cứu mới, chỉ tích hợp các thư viện và làm ứng dụng chưa đủ để bảo đảm yêu cầu đó.

### 5.2 Những điểm nên đưa vào câu hỏi đánh giá

| Điểm nhấn dự kiến | Câu hỏi cần kiểm tra | So sánh có thể thực hiện |
|---|---|---|
| Trích đúng từ tài liệu gốc Việt Nam | Đúng chỉ tiêu/giá trị/đơn vị/kỳ/phạm vi bao nhiêu; còn sửa tay bao nhiêu? | Text-only so text+OCR/parser, trước/sau review; cùng tập đã chốt |
| Ghép cổ tức theo năm lợi nhuận | Tách nhiều năm/đợt và xử lý sửa/hủy tốt hơn phép cộng đơn giản thế nào? | Baseline gán theo năm thông báo/cộng notices so mô hình components/lifecycle, trên gold |
| Ngăn kết luận khi dữ liệu chưa đủ | Thiếu notice, khác scope hoặc basis gây sai kết quả gì nếu bỏ kiểm tra? | Ca thiếu/trùng/sửa/basis trước/sau validation; không xuất baseline sai thành dữ liệu chính |
| Truy nguồn và giữ phiên bản | Có tái tính snapshot và kiểm chứng từng operand được không? | Nguồn thay đổi, bản sửa tới, snapshot cũ giữ nguyên; kiểm tra 100% số xuất bản |
| Hữu ích với người đọc | Tìm năm khác chiều, tổng DPS đúng, mở nguồn nhanh/ít lỗi hơn nhập tay không? | Nhiệm vụ cùng đầu vào, tính cả công sức review, số người thử và giới hạn |

Các câu hỏi này bám công việc thật và tạo bằng chứng IT. Chưa được gọi là phương pháp mới trên thế giới; cần đối chiếu thêm prior art cụ thể nếu muốn nâng tuyên bố.

### 5.3 Một cách diễn đạt với giảng viên

> Quan hệ lợi nhuận, dòng tiền và cổ tức đã có nghiên cứu, và thị trường cũng có phần mềm dữ liệu tài chính. Đề tài của em tập trung xây dựng và kiểm định một hệ thống tự thu dữ liệu từ BCTC/công bố chính thức, chuẩn hóa và ghép cổ tức theo đúng năm lợi nhuận, xử lý thiếu/trùng/sửa/hủy, cho phép truy nguồn và tái lập kết quả. Em chứng minh đóng góp qua độ đúng, độ phủ, công sức review, các ca khó và luồng người dùng. Phần dự đoán là bước nối tiếp khi dữ liệu và đánh giá theo thời gian đủ điều kiện.

Đây là cách trình bày phạm vi đóng góp, không phải khẳng định thầy đã phê duyệt hay hệ thống đã triển khai xong.

## 6 Phát triển lên đồ án theo hướng nào

**Sau nghiên cứu lần hai, hướng ưu tiên là đối chiếu phiên bản và ảnh hưởng tới kết quả**, xem [hướng tốt nghiệp hiện hành](09-lien-thong-tot-nghiep.md). Phân tích dự đoán giảm/không giảm bên dưới lưu lại phương án đã nghiên cứu, chỉ mở khi đủ dữ liệu theo thời điểm và quỹ giờ.

Đây là hướng phát triển dự kiến đã ghi trong hồ sơ, **không phải điều kiện bắt buộc suy ra từ việc chấm đồ án hệ thống phần mềm**. Theo hướng chấm người thực hiện xác nhận, có thể trao đổi với thầy về việc làm sâu hệ thống thu thập/cập nhật, kiểm soát chất lượng, ghép sự kiện và truy vết, với đánh giá mới có ý nghĩa. Không tự đồng nhất “phát triển lên đồ án” với “phải thêm ML”.

| Giai đoạn | Đầu ra | Điều kiện để đi tiếp |
|---|---|---|
| Project | Pipeline, facts/events đã duyệt, coverage, phiên bản, phân tích lịch sử và app có truy vết | Chạy thực tế, quality/effort được đo; không chỉ có tài liệu |
| Pilot tốt nghiệp | Mở lịch sử/doanh nghiệp, kiểm tra ngày thông tin khả dụng, nhãn và phân bố lớp | Cửa sổ kết quả khép, đủ coverage/basis và đủ trường hợp giảm cho đánh giá có ý nghĩa |
| Đồ án dự đoán | Định nghĩa target/cutoff/ngưỡng trước test; baseline, mô hình, tách thời gian và ứng dụng giải thích | So với baseline trên tập chưa dùng chỉnh mô hình; báo kết quả yếu nếu yếu; không hứa accuracy trước dữ liệu |

Chỉ tăng số công ty hoặc thêm mô hình theo tên thư viện chưa đủ tạo đóng góp mới. Cần xác định câu hỏi đánh giá mới, xử lý rò rỉ thông tin, chất lượng nhãn và giới hạn. Trước mắt chưa đổi mục tiêu hồi cứu theo năm lợi nhuận thành dự đoán cửa sổ 12 tháng trong project.

Nếu pilot cho thấy dữ liệu dự đoán không đủ, có thể trao đổi với thầy về đồ án tập trung vào chất lượng dữ liệu/ghép sự kiện/phiên bản, với benchmark và cải tiến kỹ thuật cụ thể. Đây là phương án cần thống nhất lại, chưa tự thay hướng đã chọn và chưa coi project hiện tại tự động đủ cho đồ án.

## 7 Đánh giá tên đang dùng

Tên hiện tại mô tả đúng một bài toán tập trung. Điểm cần chỉnh không phải “làm cho lớn” mà là làm rõ:

1. **Dòng tiền** trong phần lõi là **dòng tiền kinh doanh**, không phải phân tích toàn bộ dòng tiền đầu tư/tài chính.
2. **Cổ tức** là **mức tiền mặt công bố**, chưa mặc định tổng tiền thực trả hoặc khả năng pháp lý chi trả.
3. Cụm **“phân tích mối quan hệ”** dễ khiến người đọc chờ nghiên cứu tài chính với mẫu lớn; tên nhấn vào hệ thống dữ liệu phù hợp hơn nếu phần chính là project CNTT.
4. “Doanh nghiệp niêm yết Việt Nam” nêu đối tượng, không có nghĩa đã phủ toàn thị trường; proposal/SRS phải ghi mẫu và kỳ cụ thể.

Tên không cần chứa tất cả chi tiết: abstract và SRS ghi sáu trường lõi, pilot, độ phủ, phạm vi mô tả và đường phát triển. Tránh dùng “AI”, “dự báo”, “tính bền vững” hoặc “tối ưu đầu tư” khi chưa có chức năng/đánh giá tương ứng.

## 8 Các tên để lựa chọn

Các tên N01–N05 dưới đây lưu lại các phương án đã nghiên cứu. **Ngày 04/10/2026, người thực hiện yêu cầu chốt tên theo hướng lấy thu thập, xử lý và phân tích dữ liệu làm trọng tâm. Tên chính thức:** Xây dựng hệ thống thu thập, chuẩn hóa và phân tích dữ liệu lợi nhuận, dòng tiền kinh doanh và cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam. Đây là phương án cụ thể hóa N02 bằng việc bổ sung “chuẩn hóa”; SRS v2.2 và các tài liệu nguồn đã được đồng bộ.

| Mã | Tên đề xuất | Phù hợp khi | Lưu ý |
|---|---|---|---|
| **N01 — ưu tiên đề xuất** | **Xây dựng hệ thống thu thập, chuẩn hóa và phân tích dữ liệu báo cáo tài chính và cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam** | Muốn tên nhấn đóng góp hệ thống và để lại không gian phát triển | Abstract phải nói rõ phân tích LNST–CFO–DPS, chưa hứa phân tích toàn bộ BCTC |
| **N02 — gần tên hiện tại nhất** | **Xây dựng hệ thống thu thập và phân tích dữ liệu lợi nhuận, dòng tiền kinh doanh và cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam** | Muốn giữ ngách rõ, đổi ít và dùng từ chính xác hơn | Phù hợp trực tiếp sáu trường lõi và phân tích hiện hành |
| **N03 — nhấn bằng chứng dữ liệu** | **Xây dựng hệ thống dữ liệu có truy vết phục vụ phân tích lợi nhuận, dòng tiền kinh doanh và cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam** | Muốn tập trung vào nguồn, phiên bản, chất lượng và tái lập | Cần demo truy ngược số/công thức/đợt tới nguồn, không chỉ có URL chung |
| **N04 — nhấn nhu cầu người đọc** | **Xây dựng hệ thống hỗ trợ phân tích cổ tức tiền mặt dựa trên lợi nhuận và dòng tiền kinh doanh của doanh nghiệp niêm yết Việt Nam** | Muốn người nghe hiểu mục đích nghiệp vụ ngay | Chưa đồng nghĩa hệ thống quyết định cổ tức bền vững hoặc cho lời khuyên đầu tư |
| **N05 — giữ cách gọi quan hệ** | **Xây dựng hệ thống thu thập và phân tích mối quan hệ giữa lợi nhuận, dòng tiền kinh doanh và cổ tức tiền mặt công bố của doanh nghiệp niêm yết Việt Nam** | Thầy muốn tên nêu quan hệ nghiên cứu cụ thể | Ghi rõ phân tích mô tả trên mẫu nhỏ, chưa suy nhân quả |

**Đề xuất trước khi chốt tên (giữ để đối chiếu):** N01 nếu muốn tên hệ thống dễ liên thông và thể hiện rõ công việc dữ liệu; N02 nếu ưu tiên tên phản ánh chính xác ngách hiện tại. N03 phù hợp khi truy vết/phiên bản là phần kỹ thuật bạn sẽ làm sâu nhất. Không cần thêm nhiều nhóm chức năng chỉ để đáp ứng một tên rộng hơn.

Tên riêng có thể dùng **khi bước sang đồ án và đã vượt gate dữ liệu**:

- **Xây dựng hệ thống phân tích và dự đoán biến động mức cổ tức tiền mặt công bố của doanh nghiệp niêm yết Việt Nam dựa trên dữ liệu tài chính.**
- Nếu target chốt cụ thể là lớp giảm: **Xây dựng hệ thống hỗ trợ dự đoán giảm mức cổ tức tiền mặt công bố của doanh nghiệp niêm yết Việt Nam dựa trên lợi nhuận và dòng tiền kinh doanh.**

Đây là tên tương lai có điều kiện, chưa dùng như cam kết predictor của project. Nếu mô hình cần nhiều đặc trưng ngoài LNST/CFO, tên “dữ liệu tài chính” phù hợp hơn việc giữ chỉ hai nhóm biến.

## 9 Phạm vi tra cứu và điều chưa xác minh

Đã tra cứu theo các nhóm: dividend policy/profitability/free cash flow ở Việt Nam; phần mềm BCTC và lịch cổ tức; thư viện/corporate actions; dự án dự đoán giảm cổ tức; cụm tên tiếng Việt và đồ án liên quan. Ưu tiên nguồn tạp chí/nhà xuất bản/đại học, tài liệu sản phẩm và repository gốc.

Trong tập kết quả đã kiểm tra **chưa xác định một đồ án Việt Nam công khai trùng toàn bộ tên, phạm vi SRS và cách triển khai của bạn**. Điều đó không chứng minh chưa ai làm: đồ án có thể không công khai, không được lập chỉ mục, mang tên khác hoặc có chức năng nằm trong sản phẩm trả phí. Không dùng kết quả tìm tên nguyên văn để kết luận tính mới.

Chưa thực hiện tổng quan hệ thống toàn bộ tài liệu, khảo sát sản phẩm trả phí, thử nghiệm đối thủ hoặc tìm trong kho đồ án nội bộ của trường. Abstract cho thấy tồn tại nghiên cứu liên quan, chưa đủ để nói mình đã đọc/tái lập toàn bộ bài. Repository tự mô tả một chức năng là bằng chứng có công bố chức năng, chưa là benchmark độc lập.

Đã được người thực hiện xác nhận hướng **xây dựng hệ thống phần mềm**, nhưng chưa nhận rubric chi tiết ngành/trường, số thành viên và lịch thực tế. Kết luận “không quá nhỏ” dựa trên hướng đó và độ sâu SRS; giảng viên quyết định phạm vi chấp nhận. Tài liệu này bổ sung bằng chứng lựa chọn tên/phạm vi, không tự thay đổi tên đã chốt hay mở nghĩa vụ triển khai.
