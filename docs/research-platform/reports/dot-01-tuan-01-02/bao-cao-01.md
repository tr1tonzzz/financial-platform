# Báo cáo 1 — Nghiên cứu bối cảnh và đề xuất hướng đi project

**Đề tài:** Xây dựng hệ thống thu thập, chuẩn hóa và phân tích lợi nhuận, dòng tiền kinh doanh trong mối liên hệ với cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam.

**Ngày soạn:** 05/10/2026. **Cập nhật thử nghiệm:** 06/10/2026, mẫu Vinamilk quý I/2026. **Trạng thái:** bản thảo để trao đổi với giảng viên. Báo cáo tập trung vào nghiên cứu ban đầu và đề xuất sản phẩm; chưa xác nhận đã hoàn thành hai tuần triển khai hoặc có ứng dụng hoạt động.

## Tóm tắt đề xuất

Project đề xuất xây dựng hệ thống giúp người đọc trả lời: **mức cổ tức tiền mặt công bố có thể được hiểu thế nào trong bối cảnh lợi nhuận và khả năng tạo tiền của doanh nghiệp?** Người dùng xem lợi nhuận có đi cùng CFO không, khoản mục nào đóng góp vào khác biệt, cổ tức thuộc năm nào và bằng chứng nào hỗ trợ nhận xét. Hệ thống thu thập tài liệu công khai, chuẩn hóa dữ liệu, hỗ trợ duyệt số và trình bày câu trả lời mở lại được nguồn.

Lý do liên kết BCTC với cổ tức là để đối chiếu **kết quả kinh doanh, nguồn lực tài chính và quyết định phân phối**. Phân tích mức bao phủ cổ tức bằng lợi nhuận/dòng tiền tự do là một tác vụ trong tài liệu nghề nghiệp của [CFA Institute](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/analysis-of-dividends-and-share-repurchases). Project bắt đầu từ mô tả và đọc ca; đánh giá sâu khả năng duy trì cần thêm dữ liệu đầu tư, nghĩa vụ nợ và lợi nhuận giữ lại.

Ví dụ sơ bộ từ **BCTC hợp nhất đã soát xét quý I/2026 của Vinamilk** cho thấy tổng LNST tăng **54,87%** so với cột quý I/2025 đã phân loại lại; CFO cải thiện từ âm sang dương nhưng chỉ bằng **0,110 lần LNST** ở quý I/2026. Cầu nối giúp xem khoản mục nào đóng góp số học vào diễn biến tạo tiền, còn dòng chi trả cổ tức đặt ra nhu cầu kiểm lịch trả và năm lợi nhuận. Số liệu, phép tính và giới hạn được trình bày tại mục 5, từ [BCTC Vinamilk, trang PDF 12–14](https://d8um25gjecm9v.cloudfront.net/cms/20260429_VNM_BCTC_DA_SOAT_XET_Q1_2026_HOP_NHAT_VN_d44326741a.pdf#page=12).

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

Nguồn mục tiêu là trang quan hệ cổ đông của doanh nghiệp, BCTC năm kiểm toán và thông báo thực hiện quyền từ VSDC hoặc doanh nghiệp. Trường hợp Vinamilk cho thấy có thể tìm tài liệu từ danh mục chính thức và tải PDF được liên kết để đọc các chỉ tiêu cần thiết. [Danh mục BCTC Vinamilk](https://www.vinamilk.com.vn/investor/reports/financial). Mẫu quý ở mục 5 phục vụ minh họa; nguồn mục tiêu của pilot vẫn là báo cáo năm.

Tuy nhiên, có tài liệu công khai chưa đồng nghĩa có ngay một tập dữ liệu phân tích đúng. Người xử lý vẫn phải xác định kỳ báo cáo, đơn vị, phạm vi báo cáo, cột năm, các dòng cần lấy và tình trạng đầy đủ của lịch sử cổ tức. Bối cảnh này tạo ra một bài toán công nghệ thông tin cụ thể: đưa tài liệu rời rạc thành dữ liệu có cấu trúc và kết quả kiểm chứng được.

Đã bổ sung rà soát có mục tiêu gồm 10 nghiên cứu học thuật và tài liệu nghề nghiệp/pháp lý, với kết quả, phạm vi và mức đọc tại [cơ sở học thuật và giá trị sử dụng](co-so-hoc-thuat-va-gia-tri-su-dung.md). Rà soát này chưa là tổng quan hệ thống, khảo sát người dùng hay bằng chứng nhu cầu trả phí.

### 1.4. Bằng chứng cho việc nghiên cứu BCTC trong mối liên hệ với cổ tức

**Lợi nhuận cần được đọc cùng thành phần tạo tiền.** Sloan (1996) nghiên cứu vai trò tiền/dồn tích đối với độ bền của lợi nhuận. Đây là cơ sở để project hỗ trợ phát hiện ca khác chiều và đọc cầu nối, không lấy một tỷ số làm kết luận chất lượng lợi nhuận. [Sloan (1996), abstract tác giả](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2598).

**Cổ tức là quyết định có bối cảnh, không tự suy từ LNST năm nay.** Khoản 2 Điều 135 bản hợp nhất Luật Doanh nghiệp 2025 liên hệ việc phân phối với lợi nhuận đã thực hiện/giữ lại và nghĩa vụ tài chính/thanh toán sau phân phối. [Công báo — Điều 135](https://congbao.cdnchinhphu.vn/CongBaoCP/VanBan/2025/8/45865/58269-1-20251105-110667-vbhn-vpqh.pdf#page=93). Hệ thống dùng thông tin này để định hướng đọc dữ liệu, chưa là bộ kiểm điều kiện pháp lý.

**CFO và cổ tức không nhất thiết thay đổi ngay cùng nhau.** Khảo sát Brav và cộng sự (2005) ghi nhận xu hướng duy trì cổ tức và vai trò lợi nhuận bền vững. Skinner và Soltes (2011) ghi nhận quan hệ giữa việc trả cổ tức và độ bền lợi nhuận trong mẫu nghiên cứu. Điều này hỗ trợ xem chuỗi nhiều kỳ, nhưng không chứng minh trả cổ tức gây ra lợi nhuận tốt. [Brav et al. (2005)](https://people.duke.edu/~charvey/Research/Published_Papers/P88_Payout_policy_in.pdf), [Skinner & Soltes (2011)](https://link.springer.com/article/10.1007/s11142-009-9113-8).

**Bằng chứng Việt Nam cho thấy quan hệ cần được kiểm theo định nghĩa và mẫu.** Alphonse và Tran (2014) tách quyết định có chia/mức chia và báo quan hệ FCF/tài sản–payout âm trong abstract. Chau Anh Vu (2023), mẫu 110 công ty HOSE giai đoạn 2014–2020, báo hệ số FCF–payout dương ở Bảng 8. Không chuyển một trong hai thành quy luật “CFO cao thì cổ tức cao”: FCF không đồng nghĩa CFO, và thiết kế nghiên cứu khác nhau. [Alphonse & Tran (2014)](https://www.ccsenet.org/journal/index.php/ijef/article/view/32728), [Vu (2023), Bảng 1/8](https://ctujs.ctu.edu.vn/index.php/ctujs/article/download/583/643).

Các tài liệu hỗ trợ tính hợp lý của câu hỏi phân tích; hiệu quả công cụ đối với người dùng vẫn cần đo. Bằng chứng bổ sung về tích lũy, độ ổn định và tín hiệu cổ tức được tổng hợp dưới đây.

### 1.5. Chính sách cổ tức cần được đặt trong bối cảnh nhiều kỳ

| Nghiên cứu | Kết quả liên quan | Ý nghĩa đối với hướng project |
|---|---|---|
| [DeAngelo, DeAngelo & Stulz (2006)](https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/0/30211/files/2016/05/Dividend-policy-and-the-earned-contributed-capital-1mhbg83.pdf) | Trong mẫu công ty công nghiệp Mỹ 1973–2002, tỷ trọng lợi nhuận giữ lại trong vốn liên quan tới quyết định trả cổ tức | Xem bối cảnh tích lũy; tổng vốn chủ sở hữu và tiền cuối kỳ không thay thế lợi nhuận giữ lại |
| [Chay & Suh (2009)](https://www.sciencedirect.com/science/article/pii/S0304405X09000415) | Mẫu hơn 5.000 công ty thuộc bảy nước, 1994–2005: bất định dòng tiền liên quan âm với mức và xác suất trả cổ tức | Cần lịch sử khi đọc khả năng duy trì; biến đại diện chính trong nghiên cứu là biến động lợi suất, không phải CFO ba năm |
| [Grullon et al. (2005)](https://www.jstor.org/stable/10.1086/431438) | Sau kiểm soát tính phi tuyến của lợi nhuận, thay đổi cổ tức không cải thiện dự báo lợi nhuận ngoài mẫu | Không suy cổ tức tăng thành lợi nhuận tương lai chắc chắn tăng |
| [Ham, Kaplan & Leary (2020)](https://profiles.wustl.edu/en/publications/do-dividends-convey-information-about-future-earnings/) | Với phương pháp/cửa sổ thời gian khác, thay đổi cổ tức chứa thông tin về thay đổi thu nhập kinh tế bền vững | Quan hệ có giá trị nghiên cứu nhưng nhạy với định nghĩa và thời điểm; chưa là mô hình dự báo cho Việt Nam |
| [Ham, Kaplan & Utke (2023; online 2021)](https://link.springer.com/article/10.1007/s11142-021-09642-4) | Dữ liệu Mỹ 1988–2017 cho thấy cổ tức liên quan cách thị trường tiếp nhận thông tin lợi nhuận, có khác biệt theo tiền dự trữ và khả năng cắt cổ tức | Cổ tức bổ sung bối cảnh thông tin; cần đọc đặc điểm từng doanh nghiệp thay vì áp dụng nhận xét đồng nhất |

Các kết quả khác hướng cho thấy đề tài nên cung cấp dữ liệu và câu trả lời có điều kiện. Mức cổ tức thấp có thể dẫn tới câu hỏi về nhu cầu tái đầu tư; mức cao có thể dẫn tới câu hỏi về tích lũy và sức ép tiền. Đây là hướng đọc tiếp, chưa là nguyên nhân đã được xác nhận cho từng doanh nghiệp. Với pilot 3 doanh nghiệp × 3 năm, project đánh giá hệ thống hỗ trợ phân tích, chưa kiểm chứng quy luật nhân quả của thị trường.

Mức tiếp cận nguồn cũng khác nhau: đã đọc các phần chọn lọc trong PDF Brav, DeAngelo và Vu; Sloan, Alphonse–Tran, Grullon và Ham–Kaplan–Leary chủ yếu dựa trên abstract/metadata; Skinner–Soltes dựa trên nội dung công khai; Ham–Kaplan–Utke đọc abstract, mở đầu và mẫu. Chay–Suh đọc nội dung abstract/giới thiệu từ kết quả nhà xuất bản, mở trực tiếp gặp lỗi. Chưa tái lập mô hình nào. Chi tiết mức đọc được giữ trong phụ lục nghiên cứu.

### 1.6. Vì sao CFO chưa đủ để kết luận về khả năng duy trì cổ tức?

CFO phản ánh tiền thuần từ kinh doanh, nhưng doanh nghiệp còn nhu cầu đầu tư và tài trợ. CFA Institute phân biệt dòng tiền tự do cho doanh nghiệp (**FCFF**) và dòng tiền tự do cho cổ đông (**FCFE**); tính từ CFO cần các điều chỉnh đầu tư tài sản và vay ròng/phân loại phù hợp. [CFA Institute — Free Cash Flow Valuation](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/free-cash-flow-valuation).

Vì vậy, việc so CFO với tiền đã chi cho chủ sở hữu có ích để chọn ca cần đọc sâu. Để hiểu nền tảng phân phối còn phải xem tiền đầu kỳ, lợi nhuận tích lũy, chi đầu tư, nguồn tài trợ và nghĩa vụ đến hạn. Nếu chỉ có sáu chỉ tiêu lõi, hệ thống trả lời về xu hướng và bối cảnh ban đầu; chưa xác định cổ tức tối đa, nguồn riêng tài trợ cổ tức hoặc mức an toàn của khoản phân phối.

## 2. Project giải quyết vấn đề gì và vì sao cần thiết

Người dùng chính dự kiến là người đọc BCTC theo dõi một số doanh nghiệp và sinh viên/người nghiên cứu cần phân tích có dẫn nguồn. Người vận hành thu thập và duyệt dữ liệu phục vụ các tác vụ đó. Nhu cầu/ưu tiên hiện được đề xuất từ tài liệu và ca nguồn, chưa được xác nhận bằng phỏng vấn.

Tình huống sử dụng giả định: một người đọc thấy doanh nghiệp công bố lợi nhuận tăng và muốn biết diễn biến này có đi cùng dòng tiền và cổ tức hay không. Khi tự làm, người đó phải tải từng BCTC, nhập số, đổi đơn vị, tìm các đợt cổ tức rồi ghép theo năm. Sau khi thấy biến động khác chiều, họ lại mở báo cáo để tìm khoản mục liên quan. Đây là tác vụ project muốn hỗ trợ.

### 2.1. Câu hỏi người dùng và lợi ích của câu trả lời

| Câu hỏi cần trả lời | Kết quả project phải cung cấp | Lợi ích với người đọc |
|---|---|---|
| U1. Lợi nhuận tăng có đi cùng CFO không? | Số/thay đổi cùng kỳ, tỷ số phù hợp và ca khác chiều | Chọn ca cần đọc sâu, tránh chỉ nhìn LNST |
| U2. Khoản mục nào đóng góp vào chênh lệch? | Cầu nối theo ca, đóng góp/residual và trang nguồn | Tìm đúng khoản mục để đọc giải trình tiếp |
| U3. Cổ tức tiền mặt này thuộc lợi nhuận năm nào, tổng đã xác nhận bao nhiêu? | DPS từng thành phần/năm, bản sửa và mức đầy đủ nguồn | Tránh gán sai năm hoặc cộng trùng |
| U4. Khoản chi cho chủ sở hữu trong kỳ lớn thế nào so với CFO? | So sánh hai dòng tiền đúng scope/kỳ trên ca có nguồn | Xác định trường hợp cần đọc tiếp bối cảnh tiền; chưa kết luận khả năng chi trả |
| U5. Cổ tức thay đổi trong bối cảnh lợi nhuận/CFO nào? | Chuỗi theo năm lợi nhuận, biến động và phần thiếu | Theo dõi chính sách và đặt câu hỏi khi các chỉ tiêu khác chiều |
| U6. Có thể kiểm lại số và nhận xét này không? | Nguồn từng số, trạng thái duyệt, công thức và version | Trích dẫn, phát hiện lỗi và tái lập kết quả |

Payout ratio, đánh giá tiền sau đầu tư/trả nợ và khả năng duy trì sâu hơn là câu hỏi mở rộng khi có thêm dữ liệu; không mặc định sáu chỉ tiêu lõi trả lời được toàn bộ. Bảng chi tiết dữ liệu/điều kiện cho U1–U8 tại [phụ lục nghiên cứu](co-so-hoc-thuat-va-gia-tri-su-dung.md).

### 2.2. Vấn đề dữ liệu cản trở các câu trả lời

| Vấn đề trong tác vụ | Hệ quả có thể gặp | Cách project hỗ trợ |
|---|---|---|
| Phải gom nhiều BCTC và thông báo | Lặp lại việc tìm tài liệu và nhập số | Thu thập theo danh mục, lưu nguồn cùng dữ liệu |
| Số ở các báo cáo có đơn vị, kỳ hoặc phạm vi khác nhau | So sánh hoặc tính tỷ số sai | Chuẩn hóa và kiểm tra trước khi tính |
| Chỉ nhìn lợi nhuận hoặc một tỷ số | Bỏ qua diễn biến CFO và khoản mục cần đọc tiếp | Hiển thị lợi nhuận–CFO và cầu nối theo ca |
| Cổ tức có nhiều đợt, nhiều năm hoặc bản sửa | Cộng trùng, gán sai năm lợi nhuận | Tách thành phần, liên kết bản sửa và giữ lịch sử |
| Chưa tìm thấy thông báo nhưng điền bằng 0 | Nhận xét sai rằng doanh nghiệp không chia hoặc cổ tức giảm | Hiển thị dữ liệu thiếu và mức đã rà nguồn |
| Kết quả chỉ là một bảng số không có nguồn | Khó kiểm tra hoặc làm lại khi tài liệu thay đổi | Lưu trang nguồn, số đầu vào, công thức và bản dữ liệu đã dùng |

Sự cần thiết của project nằm ở khả năng kết hợp **thu thập đúng, so sánh đúng và kiểm tra lại được** trong một luồng sử dụng. Có thể dùng bảng tính để tính các tỷ số; phần hệ thống cần chứng minh là hỗ trợ công việc gom nguồn, kiểm soát cách ghép và giữ bằng chứng khi dữ liệu cập nhật.

Lợi ích cần kiểm là giảm công sức gom nguồn, giảm lỗi ghép năm/scope và giúp xác định đúng khoản mục/nguồn nhanh hơn. So sánh tác vụ đọc tay với dùng hệ thống bằng thời gian, số câu trả lời đúng, lỗi đúng/sai/thiếu và khả năng mở đúng nguồn. Riêng cầu nối, so bảng tỷ số đơn thuần với bảng tỷ số có cầu nối để đo giá trị bổ sung. Chưa có phép đo tiết kiệm thời gian hoặc cải thiện quyết định đầu tư; xem thiết kế đánh giá trong phụ lục.

### 2.3. Ý nghĩa của việc khai thác dữ liệu đối với người sử dụng

**Đối với người theo dõi doanh nghiệp**, kết quả phân tích giúp xác định điều cần tìm hiểu trước khi hình thành nhận xét. Thay vì dừng ở “LNST tăng” hoặc “cổ tức cao”, người đọc có thể kiểm tra tiền tạo ra từ kinh doanh, xác định khoản mục đóng góp vào biến động và xem chính sách phân phối có liên tục qua các kỳ đã rà hay không. Đầu ra mong muốn là một câu trả lời kèm số, nguồn và vấn đề cần đọc tiếp.

**Đối với sinh viên và người nghiên cứu**, dữ liệu đúng năm lợi nhuận, phạm vi và phiên bản giúp lập bảng mô tả có thể kiểm lại. Điều này đặc biệt cần khi một thông báo gồm nhiều năm, bản sửa thay mức chia hoặc BCTC có cột so sánh. Người dùng có thể trích dẫn nguồn và tái lập phép tính; tập pilot chưa đủ cho kết luận thống kê toàn thị trường.

**Đối với người thu thập và duyệt dữ liệu**, pipeline giữ tài liệu gốc, ứng viên trích xuất và sửa đổi giúp xử lý lỗi có hệ thống. Thử nghiệm OCR Vinamilk cho thấy ngoài sáu ô được chọn khớp nguồn, vẫn có lỗi nhãn, mã dòng và dấu phân nhóm ở các dòng khác. Giá trị dự kiến của tự động hóa là giảm thao tác lặp trong khi giữ khả năng kiểm soát; công sức duyệt phải được tính vào đánh giá lợi ích.

Ba lợi ích trên là mục tiêu sản phẩm được suy ra từ tác vụ và bằng chứng đã nghiên cứu. Chúng cần được kiểm bằng người dùng/tác vụ thực; chưa có số đo chứng minh tiết kiệm bao nhiêu thời gian hoặc cải thiện lợi nhuận đầu tư.

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

Sáu fact lõi hỗ trợ U1 và bối cảnh tài chính. U2 cần thêm các dòng cầu nối, U4 cần dòng tiền chi theo ca; U3/U5 cần sự kiện cổ tức đã duyệt. Chưa có lợi nhuận giữ lại, CAPEX, lịch nợ hoặc lợi nhuận phù hợp cổ đông thì không tự tính payout/FCFE hay gắn nhãn “cổ tức an toàn”. Các biến mở rộng trong tài liệu nghiên cứu chưa được biến thành cam kết phạm vi mới.

### 3.3. Cách triển khai sơ bộ

Luồng xử lý dự kiến là **tài liệu gốc → trích số → chuẩn hóa → kiểm tra và duyệt → lưu dữ liệu → phân tích và mở nguồn**. Báo cáo có văn bản dùng bộ đọc PDF; tài liệu scan thử OCR và đưa kết quả chưa chắc chắn vào hàng đợi duyệt. Cầu nối theo ca có thể nhập tay từ nguồn thật trong giai đoạn đầu, nhưng phải ghi rõ phần được hỗ trợ thủ công.

Stack dự kiến là Python cho thu thập/xử lý, SQLite cho lưu trữ và Streamlit cho giao diện. Tính toán dùng quy tắc xác định; chưa cần bổ sung AI để thực hiện các chức năng lõi. Chi tiết yêu cầu tham chiếu [SRS v3.1](../../22-srs-dac-ta-yeu-cau-phan-mem.md), còn báo cáo này chỉ trình bày hướng đi ở mức đề xuất.

### 3.4. Quy tắc khai thác để trả lời đúng câu hỏi

Hệ thống giữ hai phép đối chiếu riêng. **Góc chính sách** ghép BCTC năm `t` với các thành phần cổ tức thuộc lợi nhuận năm `t`, dù thông báo hoặc thanh toán ở năm sau. **Góc tiền trong kỳ** ghép CFO với khoản tiền chi trong cùng kỳ và phạm vi báo cáo. Khoản chi trong BCLCTT không tự được gán thành cổ tức từ lợi nhuận năm đó.

| Dữ liệu/chỉ tiêu | Quy tắc áp dụng |
|---|---|
| LNST và CFO | So cùng kỳ, đơn vị và phạm vi; tỷ số với mẫu số âm/0/gần 0 cần giải thích hoặc thay bằng số tuyệt đối |
| DPS — cổ tức tiền mặt trên mỗi cổ phiếu | Tổng thành phần hợp lệ theo năm lợi nhuận, xử lý bản sửa/thay thế; ghi “tổng đã xác nhận” khi chưa đủ nguồn |
| Tiền chi chủ sở hữu | Giữ nguyên nhãn, kỳ và scope của dòng tiền; tỷ số với CFO là mô tả thu–chi, chưa là payout ratio |
| Payout ratio — tỷ lệ phân phối lợi nhuận | Chỉ tính khi có cổ tức và lợi nhuận phù hợp cùng năm/quyền lợi; hoặc DPS/EPS đã kiểm cùng cơ sở cổ phiếu |
| FCFE và bối cảnh sau đầu tư/trả nợ | Cần thêm dữ liệu có định nghĩa phù hợp; không tự thay FCFE bằng CFO hoặc CFO trừ toàn bộ dòng tiền đầu tư |
| Tình trạng cổ tức | Phân biệt chưa tìm thấy, có quyết định không chia, tạm ứng, lịch thanh toán và bằng chứng thực chi; thiếu nguồn không điền bằng 0 |

BCTC riêng và hợp nhất phải được tách. Khi phân tích cổ tức của pháp nhân niêm yết, chưa thể coi toàn bộ lợi nhuận hoặc tiền của nhóm công ty là nguồn sẵn dùng tại công ty mẹ. Nếu thiếu hồ sơ phân phối và thuyết minh phù hợp, hệ thống ghi rõ giới hạn. Pilot phục vụ phân tích hồi cứu; nếu nghiên cứu quyết định tại ngày công bố, cần thêm ngày thông tin có thể biết để tránh dùng BCTC công bố sau sự kiện như thông tin đã có trước đó.

## 4. Những chức năng dự kiến và lý do cần có

| Nhóm chức năng | Người dùng làm được gì | Câu hỏi phục vụ/lý do |
|---|---|---|
| 1. Quản lý danh mục và nguồn | Chọn doanh nghiệp, năm, xem tài liệu đã có và còn thiếu | U3/U6: biết câu trả lời có đủ nguồn không |
| 2. Thu thập tài liệu | Tìm/tải BCTC và thông báo, lưu ngày lấy và bản gốc | Đầu vào U1–U6: giảm gom nguồn lặp lại, giữ bằng chứng |
| 3. Trích và chuẩn hóa dữ liệu | Lấy chỉ tiêu, đổi đơn vị, xác định đúng cột/kỳ/phạm vi | U1/U4/U5: so sánh đúng ngữ cảnh |
| 4. Kiểm tra và duyệt | Xem số cạnh nguồn, sửa lỗi có lịch sử; chặn phép tính thiếu dữ liệu | U6: kiểm soát lỗi PDF/OCR và nhập tay |
| 5. Quản lý sự kiện cổ tức | Tách phần theo năm lợi nhuận, xem các đợt, bản sửa và lịch | U3/U5: tránh gán sai năm, trùng tiền hoặc suy lịch là thực trả |
| 6. Phân tích lợi nhuận–CFO–cổ tức | Xem biến động, tỷ số hợp lệ và ca khác chiều | U1/U4/U5: mô tả kết quả, tạo tiền và phân phối |
| 7. Cầu nối CFO theo ca | Xem điểm đầu lợi nhuận, nhóm điều chỉnh và phần chưa khớp | U2: xác định khoản mục đóng góp, cần đọc tiếp |
| 8. Truy nguồn và lưu kết quả | Mở nguồn số/công thức; lưu dữ liệu để tính lại | U6: kiểm chứng và tái lập sau cập nhật |

Đối với cầu nối gián tiếp của mẫu Vinamilk, điểm đầu là **lợi nhuận trước thuế (LNTT)**. LNST vẫn được hiển thị riêng để so với CFO. Các dòng tổng trung gian chỉ dùng kiểm tra, không cộng lại cùng các dòng thành phần. Khi không đủ dữ liệu, hệ thống phải báo phần thiếu thay vì tự tạo một nguyên nhân giải thích.

Đóng góp công nghệ thông tin cần đánh giá gồm pipeline thu thập, chuẩn hóa có kiểm soát, mô hình dữ liệu cổ tức, truy nguồn và tái lập kết quả. Việc kết hợp lợi nhuận, dòng tiền và cổ tức chưa đủ để tự tuyên bố tính mới học thuật hoặc ưu thế so với mọi sản phẩm đang có.

## 5. Ví dụ phân tích thử từ BCTC Vinamilk quý I/2026

### 5.1. Nguồn và phạm vi minh họa

Ví dụ sử dụng **BCTC hợp nhất đã soát xét quý I/2026 của Công ty CP Sữa Việt Nam và các công ty con (VNM)**, được [danh mục chính thức Vinamilk](https://www.vinamilk.com.vn/investor/reports/financial) liên kết ngày 29/04/2026. [PDF nguồn](https://d8um25gjecm9v.cloudfront.net/cms/20260429_VNM_BCTC_DA_SOAT_XET_Q1_2026_HOP_NHAT_VN_d44326741a.pdf) có 71 trang; báo cáo soát xét KPMG ở trang PDF 5–6. Tổng LNST ở PDF 12/trang in 11, CFO và cầu nối ở PDF 13/trang in 12, chi trả cổ tức ở PDF 14/trang in 13. Đơn vị gốc **VND**; hai cột đều là giai đoạn ba tháng kết thúc 31/03, năm 2026 và năm 2025. Cột 2025 ghi **đã phân loại lại**, chưa phải bản Q1/2025 nguyên trạng tại thời điểm công bố năm trước.

Sáu ô LNST/CFO/chi cổ tức đã được trích bằng OCR/parser nhỏ và đối chiếu trang gốc. Các dòng thành phần cầu nối được đọc, duyệt thủ công và kiểm tổng bằng Python, **chưa trích tự động đầy đủ hoặc kiểm độc lập**. LNST dùng tổng hợp nhất, không dùng phần thuộc chủ sở hữu công ty mẹ để ghép với CFO hợp nhất. Bảng quy đổi sang tỷ đồng, làm tròn ba chữ số; phép tính dùng số VND gốc trong [phụ lục Vinamilk](vi-du-phan-tich-vnm.md).

Mẫu quý I/2026 phù hợp để minh họa câu hỏi và tính khả thi của công cụ, không thay phạm vi pilot dữ liệu năm 2023–2025. Không nhân bốn số quý, không ghép chuỗi quý với năm và không dùng một quý để kết luận khả năng duy trì cổ tức.

### 5.2. Lợi nhuận tăng, CFO cải thiện nhưng còn thấp so với lợi nhuận

| Chỉ tiêu | Q1/2025 — đã phân loại lại | Q1/2026 | Thay đổi |
|---|---:|---:|---:|
| Tổng LNST hợp nhất, tỷ đồng | 1.587,273 | 2.458,221 | +870,948 tỷ; +54,87% |
| CFO, tỷ đồng | −124,187 | 269,327 | +393,514 tỷ; chuyển từ âm sang dương |
| CFO/LNST, lần | −0,078 | 0,110 | Tăng khoảng 0,188 lần |

Tăng trưởng LNST bằng `(LNST Q1/2026 / LNST cột Q1/2025 − 1) × 100%`; tỷ số CFO/LNST dùng cùng kỳ/phạm vi và LNST dương. Vì CFO kỳ trước âm, báo **chênh lệch tuyệt đối**, không diễn giải tốc độ tăng trưởng phần trăm CFO.

CFO cùng cải thiện với lợi nhuận nhưng số tiền thuần kinh doanh trong quý I/2026 nhỏ hơn nhiều tổng LNST. Người đọc cần xem khoản điều chỉnh, vốn lưu động và thời điểm chi tiền; tỷ số 0,110 lần tự nó chưa chứng minh chất lượng lợi nhuận kém. Báo cáo quý có thể chịu mùa vụ và lịch thanh toán, nên cần chuỗi nhiều kỳ cùng thuyết minh để đánh giá tiếp.

### 5.3. Cầu nối LNTT → CFO và đóng góp vào chênh lệch

| Thành phần cầu nối, tỷ đồng | Q1/2025 — đã phân loại lại | Q1/2026 | Đóng góp vào ΔCFO |
|---|---:|---:|---:|
| LNTT — điểm bắt đầu, dòng 01 | 1.951,296 | 3.014,396 | +1.063,100 |
| Điều chỉnh dòng 02–06 | 312,160 | 322,517 | +10,356 |
| Biến động vốn lưu động dòng 09–12 | −985,146 | −962,842 | +22,304 |
| Chi phí đi vay đã trả, thuế và chi khác HĐKD, dòng 14/15/17 | −1.402,497 | −2.104,744 | −702,246 |
| **CFO — kết quả cộng** | **−124,187** | **269,327** | **+393,514** |

Tổng từ số VND gốc khớp CFO cả hai cột, **residual = 0**. Dòng 08 là tổng trung gian dùng kiểm tra, không cộng lại cùng thành phần. Báo cáo có hai dòng mã 02 và hai dòng mã 05 với nhãn khác nhau; đều phải giữ trong phép cộng, không loại trùng chỉ theo mã dòng.

LNTT đóng góp +1.063,100 tỷ vào ΔCFO, trong khi nhóm các khoản chi tiền 14/15/17 đóng góp −702,246 tỷ. Trong nhóm này, **thuế TNDN đã nộp** tăng về độ lớn từ 931,863 tỷ lên 1.579,997 tỷ, đóng góp **−648,134 tỷ** vào chênh lệch CFO. Đây là tiền thuế nộp trong kỳ, không đồng nhất với chi phí thuế trên báo cáo kết quả kinh doanh.

Nhóm vốn lưu động vẫn âm ở cả hai quý nhưng cải thiện ròng **22,304 tỷ**. Biến động phải thu đóng góp **−1.044,004 tỷ** vào ΔCFO, được bù một phần bởi tồn kho/tài sản sinh học **+372,763 tỷ** và phải trả/nợ phải trả khác **+757,746 tỷ**; chi phí chờ phân bổ đóng góp **−64,201 tỷ**. Vì vậy, không thể nhìn riêng dòng phải thu rồi kết luận toàn bộ vốn lưu động làm CFO giảm so với kỳ trước. Đây là phân rã số học; nguyên nhân như chính sách tín dụng, tiến độ mua hàng hoặc lịch nộp thuế cần kiểm thuyết minh, chưa được xác nhận trong ví dụ nhỏ.

### 5.4. Đặt tiền chi cổ tức cạnh lợi nhuận và CFO

Dòng 36 **“Tiền chi trả cổ tức”** của [BCLCTT, trang PDF 14](https://d8um25gjecm9v.cloudfront.net/cms/20260429_VNM_BCTC_DA_SOAT_XET_Q1_2026_HOP_NHAT_VN_d44326741a.pdf#page=14) ghi **−55.837.540 VND** ở Q1/2026, tương đương khoảng **55,838 triệu đồng**, so với **−1.044.977.722.500 VND**, khoảng **1.044,978 tỷ đồng**, ở cột Q1/2025. Giữ dấu âm để mô tả dòng chi; không nhầm 55,838 triệu thành tỷ đồng.

LNST tăng không đồng nghĩa tiền cổ tức chi trong cùng quý cũng tăng. Khoản chi Q1/2026 rất nhỏ trong khi Q1/2025 lớn hơn nhiều đặt ra câu hỏi về **lịch thanh toán, nghĩa vụ còn lại và năm lợi nhuận của từng đợt**. Chưa đọc đủ thông báo/thuyết minh để giải thích chênh lệch này; không gọi đây là giảm chính sách cổ tức hoặc xác định khoản nhỏ là thanh toán đợt nào. Không dùng CFO/chi cổ tức Q1/2026 với mẫu số nhỏ để kết luận mức bao phủ bền vững.

[Thông báo VSDC về VNM năm 2025](https://vsdc.vn/vi/ad1/187729) minh họa quy tắc cần có: mức 2.850 đồng/cổ phiếu gồm 350 đồng thuộc lợi nhuận 2024 và 2.500 đồng tạm ứng lợi nhuận 2025, lịch trả 24/10/2025. Dù cùng doanh nghiệp, **thông báo này không được ghép thành khoản chi Q1/2026**: lịch công bố không phải bằng chứng thực trả trong quý, và năm lợi nhuận khác năm thanh toán. Để trả lời chính sách theo năm, hệ thống cần lập lịch sử thông báo, tách thành phần rồi đối chiếu thực chi và phạm vi hợp nhất.

### 5.4.1. Thử ghép thông báo → năm lợi nhuận → lịch trả → chi trong kỳ

Để kiểm ý nghĩa của việc liên kết dữ liệu, rà có mục tiêu thêm ba thông báo VSDC và thuyết minh cổ tức của chính báo cáo Vinamilk. Đây là hồ sơ ghép thủ công một số sự kiện, **chưa phải lịch sử đầy đủ hoặc đối soát giao dịch**.

| Nguồn thông báo | Thành phần theo năm lợi nhuận | Lịch thanh toán | Đối chiếu với BCTC quý |
|---|---|---|---|
| [VSDC, 10/12/2024](https://vsdc.vn/vi/ad/177392) | Tạm ứng đợt 2 năm **2024**, 500 đồng/cổ phiếu | **28/02/2025**, trong Q1/2025 | Là ứng viên giải thích dòng chi 1.044,978 tỷ ở cột Q1/2025; thông báo xác nhận năm/lịch, chưa chứng minh toàn bộ dòng hợp nhất chỉ thuộc đợt này |
| [VSDC, 02/10/2025](https://vsdc.vn/vi/ad1/187729) | 350 đồng cho **2024** và 2.500 đồng cho **2025** | **24/10/2025**, ngoài Q1/2026 | Phải tách hai thành phần; không gán cả 2.850 đồng cho năm 2025 hoặc ghép thành chi Q1/2026 |
| [VSDC, 17/06/2026](https://vsdc.vn/vi/ad/197038) | Phần còn lại năm **2025**, 1.850 đồng/cổ phiếu | **17/07/2026**, ngoài Q1/2026 | Sự kiện bổ sung khi nghiên cứu ngày 06/10/2026, không phải thông tin đã biết cuối Q1 hoặc bằng chứng đã chi trong Q1 |

[Thuyết minh V.23, PDF 60/trang in 59](https://d8um25gjecm9v.cloudfront.net/cms/20260429_VNM_BCTC_DA_SOAT_XET_Q1_2026_HOP_NHAT_VN_d44326741a.pdf#page=60) ghi ĐHĐCĐ ngày **22/04/2026** phê duyệt mức cổ tức năm 2025 là **4.350 đồng/cổ phiếu**. Hai thành phần năm 2025 được chọn ở trên cộng `2.500 + 1.850 = 4.350`, **khớp mức phê duyệt**; phần 350 đồng thuộc năm 2024 được loại khỏi tổng năm 2025. Nếu gán toàn bộ thông báo tháng 10/2025 cho năm 2025 rồi cộng 1.850 đồng, tổng sai thành **4.700 đồng**, cao hơn 350 đồng/cổ phiếu. Đây là một phép kiểm thực cho quy tắc chuẩn hóa năm lợi nhuận; khớp tổng không thay thế việc rà mọi bản sửa hoặc xác nhận thực trả.

Có hai đầu ra tách biệt: **chính sách theo năm lợi nhuận** có mức 2025 được phê duyệt 4.350 đồng/cổ phiếu; **dòng tiền thực chi theo kỳ** ghi 55,838 triệu đồng ở Q1/2026. Vì vậy, khoản chi quý nhỏ không đủ kết luận doanh nghiệp cắt cổ tức năm 2025. Tuy nhiên, chưa xác định khoản 55.837.540 VND thuộc đợt nào hoặc chủ thể nào trong phạm vi hợp nhất; hệ thống phải để **chưa ghép được**, không tự gán.

Mốc phê duyệt 22/04/2026 nằm **sau cuối quý** và đã được trình bày trong báo cáo phát hành 29/04/2026; thông báo tháng 6 còn muộn hơn. Ví dụ này dùng góc nhìn nghiên cứu hồi cứu ngày 06/10/2026. Nếu phân tích thông tin có sẵn tại 31/03/2026, phải loại các nguồn công bố sau ngày đó. Lịch trả là bằng chứng kế hoạch thực hiện quyền, BCLCTT là bằng chứng chi gộp; chưa có chứng từ để xác nhận từng giao dịch.

**Vấn đề đề tài giải quyết:** dữ liệu tài chính đơn lẻ không chứa đủ năm lợi nhuận/lịch đợt; thông báo đơn lẻ không mô tả đủ dòng tiền kinh doanh hay thực chi gộp. Thu thập cả hai, tách thành phần, lưu ngày công bố và kiểm tổng giúp người đọc tránh diễn giải sai chính sách, đồng thời biết trường hợp nào còn thiếu bằng chứng. Việc ghép theo năm không làm cho cổ tức và CFO trở thành quan hệ nhân quả, cũng không đủ để dự báo cổ tức.

### 5.5. Kết quả ví dụ minh họa cho sản phẩm

Người dùng có thể nhận câu trả lời: **“Lợi nhuận và CFO cùng cải thiện, nhưng CFO quý I/2026 còn thấp so với LNST; tăng LNTT được bù trừ bởi các khoản chi tiền, nổi bật là thuế đã nộp. Tiền cổ tức chi trong quý nhỏ, cần kiểm lịch trả và năm lợi nhuận trước khi diễn giải chính sách.”** Mỗi nhận xét có bảng số, dòng đóng góp, trang nguồn và phần chưa biết.

Giao diện dự kiến cho phép mở bảng LNST/CFO, cầu nối, trang gốc và lịch cổ tức, phân biệt số đã chi với mức công bố. Ví dụ có ích ở việc chọn câu hỏi cần đọc tiếp và kiểm lại bằng chứng; chưa chứng minh độ chính xác tổng thể, độ phủ toàn thị trường hoặc mức tiết kiệm thời gian.

### 5.6. Thử nghiệm công cụ để kiểm tra tính khả thi

Ngày **06/10/2026**, phụ lục thử nghiệm đổi sang **BCTC hợp nhất quý I/2026 của Vinamilk**, đã soát xét, để chạy luồng **crawler → PDF → OCR ba trang → trích ứng viên → đối chiếu → tính chỉ tiêu**. Mục 5.1–5.5 dùng cùng báo cáo này để phân tích sơ bộ; mẫu quý không đổi phạm vi pilot dữ liệu năm 2023–2025.

| Thử nghiệm | Kết quả thực |
|---|---|
| Crawler Python `urllib`/`lxml` trên danh mục Vinamilk | HTML HTTP 200, 9 liên kết PDF ứng viên; chọn và tải một bản hợp nhất Q1/2026, PDF HTTP 200 |
| Đọc PDF bằng `pypdf` | 71/71 trang trả 0 ký tự; chọn OCR trang PDF 12–14 |
| Poppler 220 DPI + Tesseract.js tiếng Việt/Anh | OCR ba trang khoảng 6,026 giây, chưa gồm khởi tạo 1,044 giây, tải/render/duyệt |
| Parser nhỏ và đối chiếu trang gốc | Sáu ô LNST/CFO/chi trả cổ tức, mỗi khoản hai quý: 6 đúng, 0 sai, 0 thiếu trên mẫu phát triển |
| Phân tích sơ bộ | LNST +54,87%; CFO từ −124,187 tỷ lên 269,327 tỷ; CFO/LNST Q1/2026 ≈ 0,110 lần |

Nguồn là [PDF được danh mục Vinamilk liên kết](https://d8um25gjecm9v.cloudfront.net/cms/20260429_VNM_BCTC_DA_SOAT_XET_Q1_2026_HOP_NHAT_VN_d44326741a.pdf). Cột Q1/2025 trong bản này ghi **đã phân loại lại**. Tổng LNST và CFO cùng phạm vi hợp nhất. Lợi nhuận tăng nhưng mức chuyển thành dòng tiền trong quý còn thấp là một gợi ý đọc tiếp vốn lưu động và lịch thanh toán; chưa đủ kết luận chất lượng lợi nhuận hay khả năng duy trì cổ tức. Dòng 36 là tiền chi trả cổ tức trong kỳ, chưa ghép thông báo để xác định năm lợi nhuận.

Crawler mặc định dừng vì robots CDN trả 403; lần thử tiếp dùng cờ riêng cho một PDF công khai được danh mục liên kết, có ghi log trạng thái chưa xác định. Không mô tả kết quả này là robots CDN đã cho phép hoặc crawler VNM vận hành hoàn toàn tự động. OCR còn lỗi nhãn, mã dòng và số ngoài sáu ô được chọn. Kết quả 6/6 là đối chiếu cùng người trên mẫu phát triển; context và trang vẫn kiểm thủ công, chưa đo accuracy độc lập hay thời gian tiết kiệm. [Phụ lục thử nghiệm](thu-nghiem-cong-cu.md) có số gốc, cách chạy, log và giới hạn; giữ cả log DHG trước đó với lỗi tỷ giá 2.000 đồng.

### 5.7. Ví dụ đã trả lời câu hỏi người dùng đến đâu?

| Câu hỏi | Câu trả lời từ mẫu hiện có | Giá trị sử dụng và phần còn thiếu |
|---|---|---|
| U1 — LNST có đi cùng CFO? | VNM: LNST +54,87%; CFO âm chuyển dương, CFO/LNST Q1/2026 ≈ 0,110 lần | Xem mức tạo tiền và chuỗi nhiều kỳ, chưa gắn nhãn chất lượng lợi nhuận |
| U2 — Khoản mục nào đóng góp? | LNTT +1.063,100 tỷ; nhóm chi tiền −702,246 tỷ, trong đó thuế −648,134 tỷ; vốn lưu động +22,304 tỷ vào ΔCFO | Đọc tiếp lịch thanh toán/thuyết minh; cầu nối thủ công khớp tổng, chưa xác định nguyên nhân kinh doanh |
| U3/U5 — Cổ tức theo năm và bối cảnh thay đổi? | 2.500 + 1.850 = 4.350 đồng cho năm 2025, khớp thuyết minh; 350 đồng thuộc 2024; lịch trả tháng 7/2026 ngoài Q1 | Tránh tổng sai 4.700 đồng và diễn giải chi quý nhỏ là cắt cổ tức; chưa ghép khoản 55,838 triệu vào đợt cụ thể |
| U4 — Chi trong kỳ so với CFO? | CFO Q1/2026 ≈ 269,327 tỷ; tiền chi cổ tức ≈ 55,838 triệu; cột Q1/2025 chi ≈ 1.044,978 tỷ | Đặt câu hỏi lịch trả; không dùng mẫu số nhỏ và một quý để kết luận bền vững |
| U6 — Kiểm lại bằng chứng? | Có số VND gốc, trang PDF, log OCR/đối chiếu sáu ô, cầu nối và công thức kiểm tổng | Minh chứng cục bộ; thao tác trên giao diện hoàn chỉnh và đáp án độc lập chưa được đánh giá |

Ví dụ cho thấy một đầu ra hữu ích gồm **nhận xét → số hỗ trợ → khoản mục liên quan → nguồn → điều chưa biết**. Thu thập và OCR tạo đầu vào; giá trị sử dụng nằm ở việc chuyển đầu vào đã kiểm thành câu trả lời đúng ngữ cảnh.

### 5.8. Đọc BCTC đơn lẻ trả lời được gì, hệ thống bổ sung điều gì?

Đây là so sánh **khả năng trả lời từ các nguồn và đầu ra đề xuất**, chưa là thử nghiệm người dùng hoặc khẳng định người đọc thủ công không thể làm được. Một người có chuyên môn vẫn có thể tự ghép nguồn; hệ thống cần chứng minh giảm công việc lặp và hỗ trợ kiểm lại khi mở rộng nhiều kỳ/doanh nghiệp.

| Câu hỏi người dùng | Chỉ có một BCTC và đọc thủ công | Đầu ra hệ thống cần cung cấp | Bằng chứng ví dụ và phần cần đánh giá |
|---|---|---|---|
| Lợi nhuận tăng có đi cùng tiền kinh doanh? | Có thể đọc hai bảng và tự tính tỷ số | Bảng cùng kỳ/scope, công thức và trang nguồn | Đã tính LNST +54,87%, CFO/LNST 0,110 lần; cần đo thời gian và lỗi context trên mẫu mới |
| Vì sao CFO không tương ứng mức tăng lợi nhuận? | Có các dòng, cần tự nhóm và cộng | Cầu nối, đóng góp vào ΔCFO, residual và dòng nguồn | Cầu nối khớp; thuế đóng góp −648,134 tỷ; chưa đo lợi ích so với đọc bảng thông thường |
| Cổ tức chi ít trong quý có nghĩa giảm mức cổ tức năm? | Dòng chi không đủ lịch đợt/năm lợi nhuận; thuyết minh có mức phê duyệt nhưng chưa đủ lịch thực hiện | Chính sách theo năm đặt cạnh dòng chi theo kỳ, ghi trạng thái ghép | 2025 phê duyệt 4.350 đồng, lịch đợt cuối tháng 7/2026; khoản chi nhỏ Q1 còn chưa ghép |
| Một đợt chứa hai năm lợi nhuận thì tổng năm tính thế nào? | Cần tìm thông báo ngoài BCTC và tự tách | Thành phần sự kiện, năm lợi nhuận, tổng và kiểm chéo | Tách 350/2.500 đồng tránh tổng 2025 sai 4.700 đồng; cần kiểm lịch sử/bản sửa đầy đủ |
| Có thể tin số tự động trích không? | Có thể đối chiếu trang gốc, nhưng cần theo dõi riêng số đã sửa | Ứng viên, số duyệt, lịch sửa, nguồn và kiểm tổng | OCR dòng 12 lệch 9 triệu; giữ bản gốc và số đọc lại, chưa có accuracy độc lập |

Mỗi chức năng phải dẫn tới một câu trả lời hoặc giảm một loại lỗi cụ thể. Crawler/OCR cung cấp đầu vào; đóng góp sản phẩm nằm ở dữ liệu đúng ngữ cảnh, phép kiểm và bằng chứng mở lại được. Ví dụ cho thấy **lý do cần tổ chức và liên kết dữ liệu**, chưa chứng minh tự động hóa luôn nhanh hơn hoặc mọi nhà đầu tư đều cần cùng một cách phân tích.

## 6. Đánh giá giá trị đề tài và bước tiếp theo

### 6.1. Cơ sở hiện có và đóng góp dự kiến

Hướng project có cơ sở để tiếp tục thử nghiệm: nguồn công khai cung cấp các bảng cần đọc; ca VNM minh họa lợi nhuận tăng nhưng CFO còn thấp tương đối và có cầu nối kiểm tổng; crawler/OCR đã chạy trên mẫu nhỏ và tái tạo được chỉ tiêu chính; thông báo VNM minh họa việc phải tách cổ tức theo năm. Lỗi OCR quan sát được cho thấy rủi ro công sức duyệt PDF, bên cạnh lịch sử cổ tức chưa đủ và khả năng ghép sai context. Vì vậy, nên hoàn thiện luồng nhỏ có review trước khi tăng số doanh nghiệp.

Cơ sở học thuật và nghề nghiệp hỗ trợ việc đặt BCTC cạnh chính sách cổ tức; đóng góp project cần chứng minh là **chất lượng dữ liệu, khả năng trả lời tác vụ, truy nguồn và công sức xử lý**. Việc kết hợp các dữ liệu này đã tồn tại trong nghiên cứu, nên chưa tự là tính mới. Ba câu hỏi nghiên cứu phù hợp là: pipeline tạo dữ liệu đúng với chất lượng/công sức nào; cầu nối có giúp trả lời đúng khoản mục hơn bảng tỷ số; và quy tắc năm/phiên bản/độ đầy đủ làm thay đổi kết quả mô tả thế nào.

### 6.1.1. Tính cần thiết đã được hỗ trợ đến mức nào?

Cơ sở học thuật ở mục 1 giải thích vì sao xem lợi nhuận, dòng tiền và cổ tức cùng nhau là một tác vụ hợp lý. Ca Vinamilk bổ sung **bằng chứng tình huống về vấn đề dữ liệu và câu hỏi phân tích**, không đại diện tần suất vấn đề trên toàn thị trường.

| Luận điểm | Bằng chứng đã có | Lợi ích dự kiến còn phải đo |
|---|---|---|
| Lợi nhuận đơn lẻ chưa trả lời đủ về tạo tiền | LNST tăng mạnh, CFO còn thấp tương đối; cầu nối cho biết phần bù trừ | Người dùng nhận xét đúng và tìm khoản mục nhanh hơn hay không |
| Thời điểm chi không đồng nhất năm lợi nhuận | Cổ tức năm 2024 có lịch trả trong Q1/2025; đợt còn lại năm 2025 có lịch tháng 7/2026 | Tỷ lệ ghép năm/kỳ đúng và lỗi diễn giải giảm khi dùng hệ thống |
| Chuẩn hóa sự kiện ảnh hưởng kết quả | Tách thông báo hai năm cho tổng 2025 là 4.350 thay vì 4.700 đồng/cổ phiếu | Độ phủ, xử lý bản sửa/trùng và tổng đúng trên nhiều doanh nghiệp |
| Trích xuất cần kiểm soát chất lượng | Sáu ô chọn trước khớp, nhưng một ô khác lệch 9 triệu đồng và có lỗi mã dòng | Số đúng/sai/thiếu trên tập độc lập, số lỗi còn lọt sau duyệt |
| Truy nguồn giúp kiểm chứng nhận xét | Số gốc, công thức, cầu nối và nguồn thông báo đã lưu | Thời gian tìm nguồn/tái lập; công sức toàn luồng so với làm thủ công |

**Kết luận phù hợp cho báo cáo 1:** có cơ sở đề xuất một hệ thống thu thập–chuẩn hóa–phân tích có kiểm soát, vì việc liên kết nguồn trả lời thêm câu hỏi và tránh các lỗi diễn giải được minh họa bằng tài liệu thật. Chưa có bằng chứng để công bố tiết kiệm bao nhiêu thời gian, độ chính xác chung, chất lượng quyết định đầu tư tăng hoặc ưu thế so với mọi công cụ hiện có. Các lợi ích đó là giả thuyết đánh giá của project, không phải kết quả đã đạt.

### 6.2. Cách kiểm chứng lợi ích với người dùng

| Tác vụ | Cách so sánh | Bằng chứng cần đo |
|---|---|---|
| Trả lời U1 từ một BCTC mới | Đọc/nhập tay và dùng hệ thống | Phút hoàn thành; số/năm/scope đúng; nhận xét và phần thiếu được nêu đúng |
| Tìm khoản mục đóng góp U2 | Bảng tỷ số và bảng tỷ số kèm cầu nối | Khoản mục/đóng góp/residual đúng; thời gian mở được nguồn |
| Ghép cổ tức U3/U5 | Ghép theo năm công bố và ghép theo năm lợi nhuận/bản sửa | Thành phần gán đúng; lỗi cộng trùng; tổng năm sai; phân biệt thiếu với 0 |
| Kiểm lại nhận xét U6 | Bảng số đơn lẻ và dữ liệu có nguồn/công thức | Mở đúng trang; tái lập đúng phép tính; phát hiện ô OCR sai |

Đánh giá cần tài liệu khác mẫu phát triển, đáp án được kiểm độc lập và tác vụ tương đương. Nếu cùng người làm hai cách, đổi thứ tự hoặc ca để giảm tác động học trước. Báo thời gian cả thu thập–trích–duyệt và số đúng/sai/thiếu; giây OCR riêng không đại diện mức tiết kiệm công việc. Đây là thiết kế đánh giá đề xuất, chưa có kết quả thử người dùng.

### 6.3. Bước tiếp theo

Ba đầu ra tiếp theo được đề xuất:

1. **Chốt danh mục pilot và bảng nguồn:** xác định 3 doanh nghiệp, nguồn BCTC 2023–2025, phạm vi báo cáo và nơi rà thông báo cổ tức; ghi rõ năm/tài liệu còn thiếu.
2. **Làm một luồng dữ liệu đến kết quả:** một BCTC và các thông báo của cùng doanh nghiệp đi tới số đã kiểm tra, bảng phân tích và nguồn mở được; ghi riêng tự động và nhập hỗ trợ.
3. **Thiết kế phép đánh giá:** lập bảng đối chiếu thủ công, nhóm lỗi cần kiểm và cách đo phút xử lý/review; dùng dữ liệu khác mẫu phát triển khi đánh giá độc lập.

Nội dung cần trao đổi với giảng viên là mức độ phù hợp của bài toán hệ thống dữ liệu, phạm vi pilot, chiều sâu cầu nối theo ca và tiêu chí nghiệm thu. Báo cáo chưa ghi nhận các nội dung này đã được phê duyệt.

## Tài liệu tham khảo và hồ sơ liên quan

### Nguồn học thuật, nghề nghiệp và tài liệu gốc

Nguồn học thuật được kiểm tra ngày 05/10/2026; BCTC/thông báo bổ sung cho ca Vinamilk được kiểm tra ngày 06/10/2026. Mức tiếp cận được ghi để phân biệt kết quả đã đọc với phần chưa kiểm toàn văn; chưa tái lập mô hình nào. Rà soát có mục tiêu phục vụ lựa chọn bài toán, chưa là tổng quan hệ thống hay khảo sát toàn bộ sản phẩm.

| ID | Thông tin trích dẫn | Nguồn trực tiếp/mức tiếp cận |
|---|---|---|
| S1 | Sloan, R. G. (1996). *Do Stock Prices Fully Reflect Information in Accruals and Cash Flows About Future Earnings?* The Accounting Review, 71(3), 289–315 | [Abstract tác giả trên SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2598); không có PDF tải trực tiếp ở trang này |
| S2 | Brav, A., Graham, J. R., Harvey, C. R., & Michaely, R. (2005). *Payout Policy in the 21st Century.* Journal of Financial Economics, 77, 483–527. DOI: 10.1016/j.jfineco.2004.07.004 | [PDF trên website tác giả tại Duke](https://people.duke.edu/~charvey/Research/Published_Papers/P88_Payout_policy_in.pdf), đọc các phần đã nêu |
| S3 | DeAngelo, H., DeAngelo, L., & Stulz, R. M. (2006). *Dividend Policy and the Earned/Contributed Capital Mix: A Test of the Life-Cycle Theory.* Journal of Financial Economics, 81(2), 227–254. DOI: 10.1016/j.jfineco.2005.07.005 | [PDF trên hạ tầng Ohio State](https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/0/30211/files/2016/05/Dividend-policy-and-the-earned-contributed-capital-1mhbg83.pdf) |
| S4 | Chay, J. B., & Suh, J. (2009). *Payout Policy and Cash-Flow Uncertainty.* Journal of Financial Economics, 93(1), 88–107. DOI: 10.1016/j.jfineco.2008.12.001 | [Trang nhà xuất bản](https://www.sciencedirect.com/science/article/pii/S0304405X09000415); nội dung abstract/giới thiệu đọc được từ kết quả tìm kiếm, mở trực tiếp lỗi ở lượt này |
| S5 | Skinner, D. J., & Soltes, E. (2011). *What Do Dividends Tell Us About Earnings Quality?* Review of Accounting Studies, 16, 1–28. DOI: 10.1007/s11142-009-9113-8 | [Springer](https://link.springer.com/article/10.1007/s11142-009-9113-8), abstract/ghi chú công khai; năm online 2009, năm số tạp chí 2011 |
| S6 | Alphonse, P., & Tran, Q. T. (2014). *A Two-Step Approach to Investigate Dividend Policy: Evidence from Vietnamese Stock Market.* International Journal of Economics and Finance, 6(3), 16. DOI: 10.5539/ijef.v6n3p16 | [Trang tạp chí](https://www.ccsenet.org/journal/index.php/ijef/article/view/32728); abstract đọc được, PDF lỗi, chưa xác nhận trang kết thúc |
| S7 | Chau Anh Vu (2023). *The Impact of the Free Cash Flow and the Firm’s Life Cycle on Dividend Policy: Evidence from Vietnam’s Listed Firms.* CTU Journal of Innovation and Sustainable Development, 15(2), 116–125. DOI: 10.22144/ctu.jen.2023.026 | [PDF tạp chí](https://ctujs.ctu.edu.vn/index.php/ctujs/article/download/583/643), phần đã nêu ở mục 3; ghi tên theo đầu PDF |
| S8 | Grullon, G., Michaely, R., Benartzi, S., & Thaler, R. H. (2005). *Dividend Changes Do Not Signal Changes in Future Profitability.* The Journal of Business, 78(5), 1659–1682. DOI: 10.1086/431438 | [Abstract nhà xuất bản trên JSTOR](https://www.jstor.org/stable/10.1086/431438) |
| S9 | Ham, C. G., Kaplan, Z. R., & Leary, M. T. (2020). *Do Dividends Convey Information About Future Earnings?* Journal of Financial Economics, 136(2), 547–570. DOI: 10.1016/j.jfineco.2019.10.006 | [Hồ sơ nghiên cứu WashU](https://profiles.wustl.edu/en/publications/do-dividends-convey-information-about-future-earnings/), abstract/metadata; không coi bản working paper 2018 là bản xuất bản 2020 |
| S10 | Ham, C. G., Kaplan, Z. R., & Utke, S. (2023). *Attention to Dividends, Inattention to Earnings?* Review of Accounting Studies, 28, 265–306. DOI: 10.1007/s11142-021-09642-4 | [Springer, open access](https://link.springer.com/article/10.1007/s11142-021-09642-4), các phần đã nêu; online 2021 |
| P1 | CFA Institute (2026). *Analysis of Dividends and Share Repurchases* | [Refresher reading chính thức](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/analysis-of-dividends-and-share-repurchases); mục tiêu học/tóm tắt, không phải nghiên cứu nhu cầu thị trường |
| P2 | CFA Institute (2026). *Free Cash Flow Valuation* | [Refresher reading chính thức](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/free-cash-flow-valuation); định nghĩa/công thức trong tóm tắt |
| P3 | IFRS Foundation. *IAS 7 — Statement of Cash Flows* | [Trang About](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/); cơ sở khái niệm, không thay chế độ kế toán của BCTC Việt Nam |
| P4 | Văn phòng Quốc hội (2025). Bản hợp nhất Luật Doanh nghiệp 67/VBHN-VPQH, ngày 15/08/2025, khoản 2 Điều 135 | [Metadata Công báo](https://congbao.chinhphu.vn/van-ban/van-ban-hop-nhat-so-67-vbhn-vpqh-45865.htm), [PDF phần Điều 135](https://congbao.cdnchinhphu.vn/CongBaoCP/VanBan/2025/8/45865/58269-1-20251105-110667-vbhn-vpqh.pdf#page=93); dùng làm căn cứ bối cảnh, không xây bộ kiểm pháp lý |
| E1 | VSDC (02/10/2025). VNM: Chi trả cổ tức còn lại năm 2024 và tạm ứng đợt 1/2025 bằng tiền mặt | [Thông báo trực tiếp](https://vsdc.vn/vi/ad1/187729), đã đọc thành phần/năm/lịch trả; không là xác nhận thực chi |
| E2 | Vinamilk (2026). BCTC hợp nhất đã soát xét quý I/2026, cột so sánh Q1/2025 đã phân loại lại | [PDF từ danh mục doanh nghiệp](https://d8um25gjecm9v.cloudfront.net/cms/20260429_VNM_BCTC_DA_SOAT_XET_Q1_2026_HOP_NHAT_VN_d44326741a.pdf#page=12), kiểm ngày 06/10/2026; số/trang và phép tính tại [phụ lục Vinamilk](vi-du-phan-tich-vnm.md) |
| E3 | VSDC (2024; 2026). Thông báo tạm ứng đợt 2 năm 2024 và trả phần còn lại năm 2025 của VNM | [Thông báo 10/12/2024](https://vsdc.vn/vi/ad/177392), [thông báo 17/06/2026](https://vsdc.vn/vi/ad/197038); kiểm 06/10/2026, đọc năm lợi nhuận, DPS và lịch trả; không coi lịch là xác nhận thực chi |

### Hồ sơ dự án và phụ lục

- [SRS v3.1](../../22-srs-dac-ta-yeu-cau-phan-mem.md) và [kế hoạch 13 tuần](../../04-ke-hoach-13-tuan.md): phạm vi/yêu cầu và lộ trình triển khai.
- [Phụ lục ví dụ Vinamilk](vi-du-phan-tich-vnm.md): số gốc, phép tính và vị trí đối chiếu.
- [Phụ lục thử nghiệm công cụ](thu-nghiem-cong-cu.md): mẫu Vinamilk hợp nhất Q1/2026, crawler, PDF/OCR ba trang và đối chiếu sáu ô đã chạy thực ngày 06/10/2026.
- [Cơ sở học thuật và giá trị sử dụng](co-so-hoc-thuat-va-gia-tri-su-dung.md): 10 nghiên cứu, tài liệu nghề nghiệp/pháp lý, câu hỏi U1–U8 và cách đánh giá lợi ích; kèm mức tiếp cận của từng nguồn.
