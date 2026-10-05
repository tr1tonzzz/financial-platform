# Nhập môn tài chính để hiểu dữ liệu và các mối quan hệ trong dự án

Ngày cập nhật: **04/10/2026**.

Tài liệu dành cho người chưa có nền tảng tài chính, để hiểu những con số và quan hệ mà dự án lợi nhuận–dòng tiền–cổ tức sử dụng. Mục tiêu là đọc được một kết quả, hiểu nó nói lên điều gì và biết cần thêm bằng chứng nào trước khi kết luận sâu hơn.

Bạn có thể đọc mục 1–4 trước để hiểu nền tảng, mục 5–8 để hiểu các phép phân tích, rồi dùng ví dụ và câu hỏi cuối tài liệu để tự kiểm tra. Các chữ viết tắt đều được giải thích khi xuất hiện. **Số liệu của cửa hàng và doanh nghiệp X là giả định để học**, không phải kết quả thu thập của dự án; ví dụ VNM có nguồn riêng tại mục 6.

## 1 Hình dung một doanh nghiệp như một cửa hàng

Một cửa hàng cần tiền để mua hàng, có thể vay thêm, bán hàng cho khách và có người góp vốn làm chủ. Từ đó có ba câu hỏi khác nhau:

| Câu hỏi | Nội dung tài chính tương ứng |
|---|---|
| Trong năm, bán hàng và chịu chi phí như thế nào, cuối cùng lãi hay lỗ? | Kết quả kinh doanh và lợi nhuận |
| Trong năm, tiền thực sự vào/ra từ đâu? | Dòng tiền |
| Tại ngày cuối năm, đang có những tài sản gì, còn nghĩa vụ với ai và phần của chủ sở hữu là bao nhiêu? | Tình hình tài sản, nợ phải trả và vốn chủ sở hữu |

Đối với công ty cổ phần, phần sở hữu được chia thành các cổ phần; **cổ phiếu** thể hiện quyền sở hữu đó. **Cổ đông** là người sở hữu cổ phần. Doanh nghiệp có thể phân phối cổ tức cho cổ đông, nhưng có lợi nhuận không tự đồng nghĩa mọi lợi nhuận được trả ngay bằng tiền. [Investor.gov giải thích cổ phiếu và cổ tức](https://www.investor.gov/introduction-investing/investing-basics/investment-products/stocks).

Trong dự án, ta theo dõi **lợi nhuận sau thuế**, **dòng tiền kinh doanh** và **mức cổ tức tiền mặt công bố cho mỗi cổ phiếu**, cùng một số thông tin về tài sản và nguồn vốn.

## 2 Ví dụ quan trọng nhất là có lãi nhưng dòng tiền kinh doanh âm

### 2.1 Diễn biến của cửa hàng

Đơn vị là **triệu đồng**. Giả định cửa hàng mới mở, không có tiền đầu kỳ; bỏ qua các chi phí khác để dễ học. Khoản thuế 12 triệu là số giả định của ví dụ, không dùng để suy ra quy định thuế thực tế.

| Bước | Chuyện xảy ra | Tiền thực tế thay đổi | Ý nghĩa |
|---|---|---|---|
| 1 | Chủ góp 100, vay ngân hàng 60 | Tiền tăng 160 | Có vốn và khoản vay để hoạt động; tiền góp/vay không phải doanh thu bán hàng |
| 2 | Mua hàng 40 và trả tiền ngay | Tiền giảm 40 | Có hàng tồn kho; chưa bán nên chưa coi toàn bộ khoản mua này là giá vốn hàng đã bán |
| 3 | Bán hết số hàng với giá 100, mới thu được 30 | Tiền tăng 30; khách còn nợ 70 | Doanh thu ví dụ là 100, nhưng chỉ thu tiền 30 |
| 4 | Ghi nhận giá vốn số hàng đã bán là 40 | Không chi thêm lần nữa tại bước ghi giá vốn | Chi phí hàng bán là 40; khoản tiền mua đã ra ở bước 2 |
| 5 | Ghi nhận và trả thuế giả định 12 | Tiền giảm 12 | Lợi nhuận sau thuế còn 48 |

Ví dụ giả định việc bán hàng đã đủ điều kiện ghi nhận doanh thu. **Doanh thu** là giá trị bán hàng/dịch vụ được ghi nhận, không nhất thiết bằng tiền khách đã trả trong kỳ. **Giá vốn** là chi phí của phần hàng đã bán.

### 2.2 Ba kết quả khác nhau

| Đại lượng | Cách tính trong ví dụ | Kết quả |
|---|---|---|
| Lợi nhuận sau thuế, viết tắt LNST | 100 doanh thu − 40 giá vốn − 12 thuế | **48 triệu** |
| Dòng tiền thuần kinh doanh, viết tắt CFO | 30 thu từ khách − 40 trả mua hàng − 12 trả thuế | **−22 triệu** |
| Tiền cuối kỳ | 0 đầu kỳ + 100 góp vốn + 60 vay + 30 thu khách − 40 mua hàng − 12 thuế | **138 triệu** |

Bạn có thể thấy đồng thời **LNST dương 48**, **CFO âm 22** và **tiền cuối kỳ dương 138**. Chúng không mâu thuẫn: khách còn nợ tiền, còn số dư tiền đã được hỗ trợ bởi vốn góp và khoản vay.

### 2.3 Bảng tài sản và nguồn vốn vẫn khớp

Cuối kỳ, cửa hàng có tiền 138 và khoản phải thu khách hàng 70; tổng tài sản là **208**. Nợ ngân hàng là **60**. Vốn chủ sở hữu là vốn góp 100 cộng lợi nhuận giữ lại 48, bằng **148**. Giả định chưa phân phối lợi nhuận và không có thay đổi vốn khác.

**208 tài sản = 60 nợ phải trả + 148 vốn chủ sở hữu.**

Đây là ví dụ để hiểu cơ chế ghi nhận và luồng tiền. Khi đọc doanh nghiệp thật, lợi nhuận/CFO khác nhau còn có thể liên quan nhiều khoản khác; phải xem các dòng điều chỉnh và thuyết minh mới xác định được nguyên nhân.

## 3 Ba bảng báo cáo đang được dự án sử dụng

**Báo cáo tài chính**, viết tắt **BCTC**, là bộ thông tin kế toán về doanh nghiệp. Dự án lấy sáu số từ ba bảng chính sau:

| Bảng | Cách hình dung | Câu hỏi bảng trả lời | Số dự án lấy |
|---|---|---|---|
| Báo cáo kết quả hoạt động kinh doanh | Bộ phim về kết quả hoạt động trong một kỳ | Trong cả năm lãi/lỗ bao nhiêu? | LNST tổng |
| Báo cáo lưu chuyển tiền tệ | Bộ phim về tiền vào/ra trong một kỳ | Trong cả năm, tiền thay đổi từ các hoạt động nào? | CFO |
| Bảng cân đối kế toán | Bức ảnh chụp tại một ngày | Ngày đó có tài sản, nghĩa vụ và phần vốn chủ sở hữu bao nhiêu? | Tiền và tương đương tiền, tổng tài sản, tổng nợ phải trả, tổng VCSH |

Phân biệt **số trong kỳ** với **số tại một ngày** giúp tránh lấy CFO cả năm so với LNST một quý, hoặc lấy tài sản đầu năm khi cần cuối năm. [SEC trình bày sự khác nhau giữa các BCTC](https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements).

Ví dụ: “LNST năm 2024” thường mô tả một khoảng thời gian như 01/01–31/12/2024; “tiền tại 31/12/2024” là số dư ở ngày đó. Năm tài chính có thể khác năm dương lịch nên phải đọc ngày bắt đầu/kết thúc thật.

**Thuyết minh BCTC** là phần giải thích chi tiết: các khoản phải thu, hàng tồn kho, vay nợ, chính sách kế toán… Đây là nơi đọc sâu khi sáu số tổng chưa đủ giải thích một hiện tượng. Dự án không mặc định đã trích hết các chi tiết này.

## 4 Ý nghĩa của sáu dữ liệu tài chính lõi

### 4.1 LNST tổng là kết quả lãi hoặc lỗ sau thuế

**Hiểu đơn giản:** sau khi ghi nhận thu nhập và các chi phí liên quan, kể cả thuế, doanh nghiệp còn lãi/lỗ bao nhiêu trong kỳ. Đây là kết quả theo kế toán, chưa phải số tiền mới thu được.

**Trong dự án:** lấy dòng LNST tổng từ báo cáo kết quả kinh doanh. Dùng để đọc xu hướng, tính tỷ số với CFO và đối chiếu cổ tức.

**Đọc đúng:** LNST tăng từ 100 lên 120 tỷ nghĩa là lợi nhuận tăng 20 tỷ. Bạn chưa biết 20 tỷ tăng thêm đến từ bán hàng, khoản thu nhập khác hay thay đổi chi phí; muốn biết phải mở thêm báo cáo.

**Dễ nhầm:** doanh thu là giá trị bán hàng/dịch vụ; lợi nhuận là kết quả sau các chi phí. Doanh thu 100 không đồng nghĩa lãi 100, và LNST 100 không đồng nghĩa có thêm 100 tiền mặt.

### 4.2 CFO là dòng tiền thuần từ hoạt động kinh doanh

**Hiểu đơn giản:** tiền vào từ hoạt động kinh doanh trừ tiền ra thuộc hoạt động đó trong kỳ, theo cách phân loại trong BCTC. Từ “thuần” nói tới kết quả sau bù trừ, không phải tổng số tiền đã thu từ khách.

**CFO dương:** hoạt động kinh doanh tạo dòng tiền thuần dương trong kỳ. **CFO âm:** phần tiền ra của hoạt động kinh doanh lớn hơn phần tiền vào trong kỳ; chưa tự kết luận doanh nghiệp không còn tiền hoặc sẽ mất khả năng thanh toán.

Báo cáo lưu chuyển tiền tệ tách hoạt động **kinh doanh**, **đầu tư** và **tài chính**. Mua máy móc và nhận tiền vay minh họa vì sao tiền cuối kỳ còn chịu ảnh hưởng ngoài CFO. [IAS 7 giải thích ba nhóm dòng tiền](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/).

**Trong dự án:** đọc dòng CFO đã công bố, không tính CFO bằng tiền cuối năm trừ tiền đầu năm. Dự án cũng chưa lấy tất cả dòng tiền đầu tư/tài chính để phân tích chi tiết.

### 4.3 Tiền và tương đương tiền là số dư tại một ngày

**Hiểu đơn giản:** tiền và các khoản rất dễ chuyển thành một lượng tiền xác định, ít rủi ro biến động giá trị và có tính chất ngắn hạn phù hợp. Không tự coi mọi khoản đầu tư hoặc mọi tiền gửi là tương đương tiền. [Định nghĩa cash và cash equivalents trong IAS 7](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/).

**Trong dự án:** lấy tổng mục “Tiền và các khoản tương đương tiền” ở cuối năm. Dùng để tính tiền/tài sản và đọc bối cảnh số dư tiền.

**Đọc đúng:** số dư tiền tăng có thể đến từ kinh doanh, nhận tiền vay, góp vốn hoặc bán tài sản. Vì vậy “tiền tăng” chưa chứng minh “kinh doanh tạo tiền tốt hơn”. Cũng cần đọc thuyết minh nếu có hạn chế sử dụng tiền; số dư không tự đồng nghĩa mọi tiền đều sẵn sàng để chia cổ tức.

### 4.4 Tổng tài sản là các nguồn lực ghi nhận trên báo cáo

**Hiểu đơn giản:** tổng giá trị sổ sách của các nguồn lực doanh nghiệp kiểm soát và ghi nhận, chẳng hạn tiền, khoản phải thu, hàng tồn kho và máy móc. Tài sản không chỉ là tiền có thể lấy ra dùng ngay.

**Trong dự án:** lấy tổng tài sản cuối năm, dùng làm mẫu số cho tiền/tài sản và nợ phải trả/tài sản.

**Đọc đúng:** tài sản tăng có thể vì máy móc mới hoặc khách nợ nhiều hơn, chưa tự là dấu hiệu kinh doanh hiệu quả hơn. Giá trị sổ sách cũng không đồng nghĩa giá bán ngay hoặc giá trị thị trường của cả doanh nghiệp.

### 4.5 Nợ phải trả là toàn bộ nghĩa vụ được ghi nhận

**Hiểu đơn giản:** doanh nghiệp có các nghĩa vụ phải thực hiện với bên khác. Ngoài tiền vay còn có khoản phải trả nhà cung cấp, thuế phải nộp hoặc nghĩa vụ khác.

**Ví dụ giả định:** vay ngân hàng 40, chưa trả nhà cung cấp 50, thuế phải nộp 10 thì nợ phải trả là 100; nợ vay ngân hàng trong ví dụ chỉ là 40.

**Trong dự án:** lấy tổng nợ phải trả, tính nợ phải trả/tài sản. Chưa gọi kết quả đó là tỷ lệ nợ vay, và chưa suy áp lực trả nợ ngay khi chưa có kỳ hạn, lãi suất và cơ cấu nợ.

### 4.6 VCSH là phần còn lại về mặt kế toán của chủ sở hữu

**Vốn chủ sở hữu**, viết tắt **VCSH**, được hiểu qua đẳng thức:

**Tài sản = Nợ phải trả + VCSH**, hay **VCSH = Tài sản − Nợ phải trả**. [SEC giải thích đẳng thức cân đối](https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements).

**Ví dụ:** tài sản 1.000 tỷ, nợ phải trả 400 tỷ thì VCSH 600 tỷ. VCSH có thể bao gồm vốn góp, lợi nhuận chưa phân phối và các khoản vốn khác theo báo cáo; chưa phải 600 tỷ tiền sẵn trong tài khoản.

**Trong dự án:** VCSH là dữ liệu lõi để hiển thị và kiểm tra cân đối. Việc cân đối khớp hỗ trợ kiểm tra số liệu, nhưng không đảm bảo máy đọc đã chọn đúng năm/phạm vi/đơn vị. Dự án chưa mặc định tính tỷ suất sinh lời trên VCSH (ROE).

## 5 Vì sao lợi nhuận và CFO có thể khác nhau

### 5.1 Kế toán dồn tích là ghi nhận theo hoạt động chứ không chỉ theo tiền

Thuật ngữ **kế toán dồn tích** giúp giải thích ví dụ cửa hàng: có thể ghi doanh thu khi đã đáp ứng điều kiện ghi nhận, dù khách chưa trả hết tiền; có chi phí được ghi nhận ở kỳ này dù tiền ra ở thời điểm khác.

**Khoản phải thu** là khoản doanh nghiệp có quyền thu từ khách/bên khác theo nội dung báo cáo. **Khoản phải trả** là nghĩa vụ doanh nghiệp còn phải trả. **Hàng tồn kho** là hàng/nguyên vật liệu còn giữ cho hoạt động sản xuất kinh doanh.

Máy móc thường được sử dụng nhiều kỳ; **khấu hao** là phân bổ giá trị phải khấu hao trong thời gian sử dụng hữu ích, không phải mỗi kỳ lại mua một máy mới. Ví dụ giả định máy 100 triệu, không giá trị còn lại, dùng 5 năm và phân bổ đều: 20 triệu/năm. Số khấu hao ảnh hưởng chi phí nhưng không tự tạo dòng tiền chi mua máy mới 20 triệu trong năm đó. [IAS 16 định nghĩa khấu hao](https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2022/issued/part-a/ias-16-property-plant-and-equipment.pdf?bypass=onStep).

### 5.2 Những cơ chế có thể làm khác biệt

| Tình huống minh họa | Lợi nhuận và tiền có thể khác nhau thế nào | Cần kiểm tra thêm ở đâu |
|---|---|---|
| Bán chịu nhiều, chưa thu tiền | Ghi doanh thu/lợi nhuận nhưng chưa nhận đủ tiền | Khoản phải thu, thu tiền khách và thuyết minh |
| Mua thêm hàng dự trữ, đã trả tiền | Tiền ra trước khi toàn bộ hàng được bán và ghi giá vốn | Hàng tồn kho, tiền trả nhà cung cấp |
| Chưa trả tiền nhà cung cấp | Có thể ghi nhận chi phí/giá vốn trước thời điểm chi tiền | Khoản phải trả và dòng điều chỉnh liên quan |
| Có khấu hao | Chi phí làm giảm lợi nhuận, nhưng không phải tiền chi mua máy lặp lại trong kỳ | Tài sản cố định và dòng điều chỉnh CFO |
| Thu tiền khách nợ từ kỳ trước | Có tiền vào kỳ này dù doanh thu liên quan đã ghi kỳ trước | Biến động khoản phải thu và các khoản thu |

Đây là **những cơ chế có thể xảy ra**, không phải nguyên nhân đã được xác nhận cho một doanh nghiệp. Sáu số lõi cho thấy có khác biệt; muốn giải thích khác biệt phải thu thêm chi tiết. Báo cáo dòng tiền theo phương pháp gián tiếp điều chỉnh lợi nhuận cho khoản phi tiền tệ và chênh lệch thời điểm ghi nhận/thu chi. [IAS 7 mô tả phương pháp gián tiếp](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/).

## 6 Hiểu cổ tức và các dữ liệu sự kiện

### 6.1 Cổ tức tiền mặt và DPS

**Cổ tức tiền mặt** là khoản phân phối bằng tiền cho cổ đông theo quyền tương ứng. **DPS** viết tắt Dividend Per Share, trong dự án là mức tiền mặt **công bố cho một cổ phiếu** đủ điều kiện nhận quyền. DPS 1.500 đồng nghĩa là mức công bố 1.500 đồng/cổ phiếu.

Ví dụ giả định có 200 cổ phiếu đủ điều kiện nhận quyền với DPS 1.500: số tiền theo mức công bố là **200 × 1.500 = 300.000 đồng**, trước các khoản khấu trừ nếu có. Đây là phép giải thích quyền của người nắm giữ, không phải bằng chứng doanh nghiệp đã thực trả hay công thức lấy tổng tiền chi trả của toàn doanh nghiệp từ số cổ phiếu cuối năm.

**Cổ tức cổ phiếu** phân phối bằng cổ phiếu, không cộng vào DPS tiền mặt như một đợt tiền. Dự án theo dõi nó khi cần kiểm tra thay đổi cơ sở cổ phiếu.

Về bản chất, cổ tức là phân phối cho chủ sở hữu. Cổ tức tiền mặt thông thường không được coi là giá vốn/chi phí bán hàng để trừ lại khi tính LNST; cần phân biệt tạo lợi nhuận với quyết định phân phối lợi nhuận. Lợi nhuận giữ lại về kế toán cũng không tự là tiền còn trong ngân hàng.

### 6.2 Tỷ lệ cổ tức trên mệnh giá khác lợi suất theo giá thị trường

**Mệnh giá** là giá trị danh nghĩa được ghi cho cổ phiếu; **giá thị trường** là giá giao dịch, có thể khác mệnh giá.

Ví dụ giả định thông báo ghi 25% trên mệnh giá 10.000 đồng:

- DPS = 25% × 10.000 = **2.500 đồng/cổ phiếu**.
- Nếu dùng giá thị trường giả định 50.000 đồng, 2.500 / 50.000 = **5%**, là phép minh họa tỷ lệ tiền so với giá đó, chưa tính các yếu tố khác.

Vì vậy “cổ tức 25%” trong thông báo theo mệnh giá không có nghĩa người mua ở bất kỳ giá nào đều có lợi suất 25%. Dự án lõi thu DPS, tỷ lệ và mệnh giá; chưa thu giá thị trường để tính lợi suất cổ tức.

### 6.3 Năm lợi nhuận khác ngày công bố và ngày thanh toán

| Trường | Hiểu đơn giản | Cách dùng trong dự án |
|---|---|---|
| Năm lợi nhuận | Thông báo nói cổ tức thuộc năm nào | Ghép với BCTC năm tương ứng |
| Ngày công bố | Nguồn đăng thông báo vào lúc nào | Xếp lịch sử thông tin |
| Ngày đăng ký cuối cùng | Mốc lập danh sách người có quyền theo công bố | Xem sự kiện quyền; không suy rằng mua đúng ngày này luôn có quyền |
| Ngày thanh toán theo lịch | Ngày dự kiến/thông báo thực hiện thanh toán | Hiển thị lịch; chưa phải xác nhận thực trả |
| Tạm ứng/đợt/phần còn lại | Mức công bố thuộc giai đoạn nào trong việc chia cổ tức | Phân biệt và rà các đợt, tránh bỏ sót |
| Sửa/hủy | Nội dung nào thay thế hoặc loại bỏ thông báo trước | Chọn mức/lịch có hiệu lực và giữ lịch sử |

**Ví dụ thật để kiểm tra cách đọc:** VSDC đăng thông báo VNM ngày 02/10/2025, mệnh giá 10.000 đồng, tổng mức 2.850 đồng/cổ phiếu. Trong đó 350 đồng là phần còn lại của năm lợi nhuận 2024, còn 2.500 đồng là tạm ứng đợt 1 năm 2025; lịch thanh toán ghi 24/10/2025. Phải đưa hai phần vào đúng hai năm, không gán cả tổng vào 2025. [Thông báo gốc VSDC 187729](https://vsdc.vn/vi/ad1/187729).

Đó là mức trong **một thông báo**, chưa phải lịch sử năm đầy đủ. Ngày thanh toán trong thông báo, kể cả đã qua, chưa tự chứng minh thực trả; phải có bằng chứng xác nhận riêng để dùng trạng thái đó trong hệ thống.

### 6.4 Một năm có nhiều đợt và mỗi thông báo có thể thay đổi

Ví dụ giả định một năm có đợt 1 là 1.000, đợt 2 là 500 đồng/cổ phiếu, cùng cơ sở cổ phiếu. Tổng hai đợt có hiệu lực ban đầu là 1.500. Xét ba tình huống độc lập từ tổng ban đầu: nếu đợt 2 sửa còn 400, tổng là 1.400, không phải 1.900; nếu chỉ sửa lịch trả, tổng vẫn 1.500; nếu hủy đợt 2, phần có hiệu lực còn 1.000.

Phải phân biệt hai nguồn đăng cùng một đợt với hai đợt thật. Nghị quyết thông qua và thông báo quyền cùng đợt là bằng chứng khác nhau về một nội dung, không tự là hai khoản để cộng.

### 6.5 Cơ sở cổ phiếu có thể làm DPS thô thay đổi

Ví dụ giả định chỉ tách cổ phiếu theo tỷ lệ một thành hai: bạn có 100 cổ phiếu trước tách, thành 200 sau tách. DPS từ 2.000 xuống 1.000 đồng/cổ phiếu thì phép nhân lần lượt là **100 × 2.000 = 200 × 1.000 = 200.000 đồng**. Bạn chưa thể chỉ nhìn DPS giảm một nửa để nói số tiền tương ứng giảm một nửa.

Ví dụ chỉ minh họa thay đổi đơn vị cổ phiếu, chưa là quy tắc điều chỉnh chung cho mọi phát hành hoặc cổ tức cổ phiếu. Trong dữ liệu thật, phải xác định loại sự kiện, ngày hiệu lực và cơ sở quyền. Nếu chưa có điều chỉnh được kiểm chứng, hệ thống giữ từng mức gốc và chặn phép cộng/so sánh cần cùng cơ sở.

## 7 Ý nghĩa các tỷ số và quan hệ mà dự án phân tích

### 7.1 CFO chia cho LNST

**Công thức:** CFO / LNST tổng cùng kỳ và phạm vi. Dự án sử dụng khi **LNST >0**.

| Ví dụ giả định | Tỷ số | Cách nói phù hợp |
|---|---|---|
| CFO 90, LNST 100 | 0,90 lần | CFO tương đương 0,90 lần con số LNST trong kỳ |
| CFO 40, LNST 120 | Khoảng 0,33 lần | CFO thấp hơn LNST theo phép so sánh này |
| CFO 150, LNST 100 | 1,50 lần | CFO lớn hơn LNST; cần đọc thêm để biết cơ chế |
| CFO −10, LNST 80 | −0,125 lần | CFO âm trong khi doanh nghiệp ghi LNST dương |

Đây là phép đối chiếu **hai đại lượng tổng**, chưa phải theo dấu từng đồng lợi nhuận để xác định bao nhiêu đã thu tiền. Không có ngưỡng “luôn tốt” áp cho mọi ngành/kỳ; CFO/LNST <1 không tự chứng minh gian lận, >1 không tự chứng minh doanh nghiệp tốt.

Nếu LNST =0 thì không chia được. Nếu LNST âm, chia hai số vẫn có thể ra số dương nhưng dễ bị hiểu sai theo cách diễn giải trên; dự án trả trạng thái riêng và cho xem mức LNST/CFO thay vì xuất một tỷ số thông thường. LNST dương rất nhỏ cũng có thể làm tỷ số lớn, nên luôn đọc số gốc.

### 7.2 Tiền chia cho tổng tài sản

**Công thức:** tiền và tương đương tiền / tổng tài sản × 100%, tại cùng ngày, cùng phạm vi; tài sản >0.

Ví dụ 100 tỷ tiền trên 1.100 tỷ tài sản bằng khoảng **9,09%**. Có thể nói “tiền và tương đương tiền chiếm khoảng 9,09% giá trị tài sản ghi nhận tại ngày đó”. Không nói “9,09% đủ để trả mọi nghĩa vụ”: muốn nghiên cứu thanh khoản còn cần nợ ngắn hạn, thời hạn trả, khả năng thu tiền và thông tin khác.

Tỷ lệ giảm có thể vì tiền giảm, vì tài sản tăng hoặc cả hai. Dự án hiển thị cả tử số/mẫu số để không chỉ nhìn một phần trăm.

### 7.3 Nợ phải trả chia cho tổng tài sản

**Công thức:** tổng nợ phải trả / tổng tài sản × 100%, tại cùng ngày, cùng phạm vi; tài sản >0.

Ví dụ 550 tỷ nợ phải trả trên 1.100 tỷ tài sản là **50%**. Có thể nói “nợ phải trả bằng 50% tổng tài sản theo số ghi nhận”. Chưa biết bao nhiêu là vay chịu lãi, bao nhiêu là khoản phải trả hoạt động hoặc khoản đến hạn sớm.

Tỷ lệ tăng là bối cảnh cần đọc thêm cơ cấu nguồn vốn; chưa tự là điểm rủi ro hay kết luận mất khả năng thanh toán. Không đặt một ngưỡng chung như 50% để phân loại mọi doanh nghiệp an toàn/nguy hiểm.

### 7.4 Mức chênh lệch và phần trăm thay đổi

**Chênh lệch = số năm sau − số năm trước.** Khi nền năm trước dương và dữ liệu so sánh được: **% thay đổi = chênh lệch / số năm trước × 100%**.

Ví dụ LNST 100 lên 120 tỷ: tăng **20 tỷ**, tương ứng **20%**. DPS 1.000 lên 1.500: tăng **500 đồng/cổ phiếu**, tương ứng **50%**, nếu đã rà đủ và cùng cơ sở cổ phiếu.

Nền 0 làm phép chia không xác định. Nền âm có thể gây cách đọc sai; từ lỗ 100 xuống lỗ 50 là mức lỗ giảm, không đọc công thức growth thông thường thành “lợi nhuận giảm 50%”. Dự án ưu tiên hiển thị hai mức và chênh lệch khi nền không dương.

**Phần trăm khác điểm phần trăm:** nợ/tài sản từ 40% lên 50% là tăng **10 điểm phần trăm**; mức tăng tương đối của chính tỷ lệ là (50 − 40) / 40 = **25%**. Khi nói biến động tỷ lệ, cần ghi rõ đang dùng cách nào.

### 7.5 LNST CFO và DPS cùng chiều hoặc khác chiều

| Quan sát có thể gặp | Điều có thể nói | Câu hỏi cần đọc sâu |
|---|---|---|
| LNST tăng, CFO tăng, DPS tăng | Ba chỉ tiêu tăng trên phần dữ liệu so sánh được | Nguồn tăng trưởng và lịch sử này có ổn định không? |
| LNST tăng, CFO giảm/âm | Kết quả kế toán và dòng tiền kinh doanh đang khác chiều | Phải thu, hàng tồn kho, các điều chỉnh hoặc thời điểm thu chi thay đổi thế nào? |
| LNST hoặc CFO giảm, DPS giữ nguyên hoặc tăng | Mức cổ tức công bố chưa giảm cùng chỉ tiêu đang giảm | Có lợi nhuận tích lũy, nguồn tiền khác, chính sách chia hoặc phạm vi mẹ/nhóm nào cần xem? |
| LNST và CFO tăng, DPS giảm | Doanh nghiệp công bố mức thấp hơn dù hai chỉ tiêu tăng | Có kế hoạch đầu tư, thay đổi chính sách hoặc thay đổi cơ sở cổ phiếu không? |

Các câu hỏi cột cuối là **hướng kiểm tra**, không phải giải thích đã được xác nhận. Cổ tức có thể liên quan lợi nhuận tích lũy và lựa chọn phân phối, nên không buộc biến động một–một với LNST/CFO của cùng năm. Muốn kết luận nguyên nhân phải có dữ liệu và phương pháp khác ngoài biểu đồ ba đường.

### 7.6 Tương quan chỉ mô tả xu hướng trên mẫu

**Biểu đồ phân tán** đặt mỗi cặp số thành một điểm: chẳng hạn % thay đổi LNST trên trục ngang, % thay đổi DPS trên trục dọc. **Spearman** so sánh thứ hạng của hai biến: một biến xếp cao hơn có thường đi cùng biến kia xếp cao hơn hoặc thấp hơn không? Hệ số từ −1 tới +1 mô tả xu hướng ngược/cùng chiều đó. Gần 0 chưa có nghĩa hai biến hoàn toàn không liên quan theo mọi kiểu. [Tài liệu chính thức SciPy về Spearman](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html).

Dự án công bố tên biến, số cặp quan sát (**n**), phần bị loại và điều kiện lọc. Không xuất hệ số khi <3 cặp hoặc một biến hằng; đây là điều kiện hiển thị của dự án, chưa là ngưỡng đảm bảo độ tin cậy. Với ba năm và ít doanh nghiệp, phải giữ rõ giới hạn mẫu nhỏ và sự phụ thuộc giữa các năm của cùng công ty.

Thấy tương quan chưa chứng minh nguyên nhân: lợi nhuận và cổ tức có thể cùng chịu ảnh hưởng của yếu tố khác. Cũng chưa có nghĩa dự đoán được năm tiếp theo. Không gộp tùy tiện số tuyệt đối của công ty rất lớn và rất nhỏ để rút kết luận chung.

## 8 Điều kiện để đọc và so sánh đúng

### 8.1 Cùng đơn vị và đúng cột

“120.000 triệu đồng” là **120 tỷ đồng**, không phải 120.000 đồng. BCTC còn có cột năm hiện tại, cột năm trước và đôi khi số đã trình bày lại. Mỗi số phải đi cùng đơn vị, kỳ, cột và phiên bản nguồn.

Đơn vị LNST/CFO là đồng, DPS là đồng/cổ phiếu. **Không lấy CFO / DPS để gọi là khả năng trang trải cổ tức.** Nếu muốn so dòng tiền với tổng tiền phân phối cần thêm số tổng chi tương ứng, đúng khoảng thời gian và phạm vi; dự án chưa mặc định có số đó.

### 8.2 Cùng phạm vi báo cáo

**Hợp nhất** trình bày công ty mẹ và các công ty con như một thực thể kinh tế, có xử lý quan hệ nội bộ; **riêng** trình bày một pháp nhân với cách ghi nhận các khoản đầu tư tương ứng. [IFRS 10 giải thích phạm vi hợp nhất](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-10-consolidated-financial-statements/), [IAS 27 giải thích báo cáo riêng](https://www.ifrs.org/issued-standards/list-of-standards/ias-27-separate-financial-statements/).

Ví dụ giả định CFO hợp nhất 100 nhưng LNST riêng 20: chia ra 5 lần chưa có ý nghĩa tỷ số cùng phạm vi của dự án. Phải dùng CFO và LNST của cùng phạm vi.

**LNST tổng hợp nhất** còn cần phân biệt với **LNST thuộc cổ đông công ty mẹ**. Dự án dùng LNST tổng để đối chiếu CFO tổng. Tiền ở công ty con trong số hợp nhất không tự là tiền công ty mẹ sẵn để chia cho cổ đông mẹ; muốn nghiên cứu khả năng phân phối tại mẹ cần thêm BCTC riêng và các thông tin liên quan.

### 8.3 Cùng năm và đủ dữ liệu cổ tức

Một đợt thuộc năm lợi nhuận 2024 có thể đăng/thanh toán năm 2025. Bảng phân tích dùng năm lợi nhuận; lịch sự kiện dùng các ngày công bố/chốt quyền/thanh toán. Không đổi năm lợi nhuận theo ngày đăng.

| Trạng thái | Ý nghĩa | Cách đọc |
|---|---|---|
| Tổng phần đã quan sát | Cộng được các đợt hợp lệ đã tìm thấy | Chưa tự là tổng đủ của năm |
| Đủ tại mốc kiểm tra | Đã rà nguồn/đợt/sửa đổi với bằng chứng tại thời điểm chốt | Có thể dùng tổng năm khi các điều kiện khác cũng hợp lệ |
| Một phần/chưa xác định | Còn nguồn/đợt hoặc thông tin chưa kiểm tra xong | Chưa kết luận annual tăng/giảm |
| Có nguồn xác nhận không chia tiền mặt | Quyết định/nội dung rõ đã được duyệt | Có căn cứ ghi mức 0 trong phạm vi được xác nhận |

**Không tìm thấy thông báo khác với doanh nghiệp không chia cổ tức.** Một năm mới quan sát 1.000 so với năm trước đủ 1.500 chưa đủ để nói giảm 500: có thể còn đợt chưa tìm được.

### 8.4 Phân tích quá khứ khác dự đoán tại một thời điểm

Bảng lịch sử có thể ghép thông báo đến sau năm lợi nhuận để hiểu đầy đủ năm đó. Nhưng nếu muốn dự đoán tại ngày BCTC vừa công bố, không được dùng thông báo/bản sửa chưa xuất hiện vào ngày đó.

Ví dụ giả định dự đoán vào tháng 3 mà lấy thông báo tháng 10 làm đầu vào là dùng thông tin tương lai. Thuật ngữ **rò rỉ dữ liệu** chỉ lỗi khiến mô hình được “biết trước” điều lẽ ra chưa biết. Đây là lý do hướng tốt nghiệp cần quy tắc lập dữ liệu và đánh giá theo thời điểm riêng; project hiện tại chỉ mô tả lịch sử.

## 9 Ví dụ đọc kết quả của dự án theo ba năm

**Dữ liệu giả định của X**, cùng phạm vi, đã duyệt, cổ tức rà đủ và cùng cơ sở cổ phiếu:

| Năm | LNST | CFO | Tiền | Tài sản | Nợ phải trả | VCSH | DPS |
|---|---|---|---|---|---|---|---|
| 2023 | 100 | 90 | 120 | 1.000 | 400 | 600 | 1.000 |
| 2024 | 120 | 40 | 100 | 1.100 | 550 | 550 | 1.500 |
| 2025 | 80 | −10 | 70 | 1.200 | 660 | 540 | 1.400 |

Sáu cột tài chính tính bằng **tỷ đồng**, DPS bằng **đồng/cổ phiếu**. Đây là bộ số nhất quán với ví dụ trong SRS và tài liệu chức năng.

**Đọc năm 2024:** LNST tăng 20%, CFO giảm 50 tỷ; CFO/LNST từ 0,90 xuống khoảng 0,33 lần. DPS tăng 50%. Tiền/tài sản khoảng 9,09%; nợ phải trả/tài sản 50%.

Nhận xét phù hợp: “LNST và DPS công bố tăng trong khi CFO giảm. Cần mở dòng tiền/thuyết minh để tìm hiểu khác biệt; bộ số tổng chưa xác định nguyên nhân hay khả năng duy trì cổ tức.”

**Đọc năm 2025:** LNST giảm 40 tỷ, khoảng 33,33%; CFO âm 10 tỷ, CFO/LNST = −0,125 lần. Tiền/tài sản khoảng 5,83%, nợ phải trả/tài sản 55%. DPS giảm 100 đồng, khoảng 6,67%.

Nhận xét phù hợp: “Dữ liệu năm 2025 cho thấy LNST giảm, CFO âm và DPS công bố thấp hơn năm trước trên cùng cơ sở so sánh. Chưa đủ để kết luận biến nào gây ra biến nào hoặc dự đoán cổ tức năm sau.”

**Nếu cổ tức 2025 chưa rà đủ:** vẫn có thể đọc LNST/CFO nếu BCTC đủ, nhưng 1.400 chỉ là phần quan sát và câu “DPS năm giảm 6,67%” phải chờ. Độ đầy đủ cần kiểm tra riêng cho mỗi loại dữ liệu.

## 10 Thuật ngữ bổ trợ thường gặp nhưng chưa là dữ liệu lõi

Các khái niệm này giúp hiểu câu hỏi cần đọc thêm, **không tự mở rộng nghĩa vụ thu thập/phân tích của project**.

| Thuật ngữ | Hiểu đơn giản | Vì sao có thể cần về sau |
|---|---|---|
| Lợi nhuận chưa phân phối | Lợi nhuận kế toán tích lũy còn giữ lại theo báo cáo, chịu ảnh hưởng các phân phối/điều chỉnh | Hiểu bối cảnh phân phối; không phải số dư tiền |
| Nợ vay | Nghĩa vụ vay và các khoản liên quan theo định nghĩa đã xác nhận | Đọc chi phí lãi/kỳ hạn; chỉ là một phần nợ phải trả |
| Vốn lưu động | Trong cách gọi phổ biến là tài sản ngắn hạn trừ nợ ngắn hạn; phân tích kinh doanh có thể dùng định nghĩa vận hành khác | Định nghĩa phải chốt; khi giải thích CFO thường xem riêng phải thu, tồn kho, phải trả hoạt động |
| Thanh khoản | Khả năng có/thu xếp nguồn để đáp ứng nghĩa vụ khi đến hạn | Cần kỳ hạn và nguồn thu chi, không chỉ tiền/tài sản |
| Khấu hao | Phân bổ giá trị phải khấu hao của tài sản qua thời gian sử dụng | Giải thích một loại chi phí không có khoản chi mua mới tương ứng mỗi kỳ |
| Chi đầu tư, thường gọi capex | Chi để mua/xây/nâng cấp tài sản phục vụ hoạt động theo định nghĩa phân tích | Hiểu nhu cầu tiền đầu tư; chưa lấy từ sáu số tổng |
| Dòng tiền tự do, thường gọi FCF | Một cách đo tiền sau nhu cầu đầu tư; dạng đơn giản thường lấy CFO trừ capex, nhưng có nhiều định nghĩa | Phải xác định capex và phạm vi trước; không đồng nghĩa CFO |
| EPS | Lợi nhuận mỗi cổ phiếu, theo cách tính và cơ sở cổ phiếu của báo cáo | Cần lợi nhuận thuộc cổ đông phù hợp và số cổ phiếu bình quân; chưa là trường lõi |
| DPS/EPS | Phép so cổ tức mỗi cổ phiếu với lợi nhuận mỗi cổ phiếu | Cần cùng năm/basis phù hợp; chưa tự là tỷ lệ tổng tiền đã thực trả |
| ROE | Tỷ suất lợi nhuận trên VCSH theo định nghĩa đã chọn | Thường cần VCSH bình quân; không tự chia LNST cho VCSH cuối năm rồi gọi đúng mọi trường hợp |
| Số đã trình bày lại | Số kỳ trước được sửa/trình bày lại ở phiên bản báo cáo sau | Phải giữ nguồn/phiên bản và xác định dùng số nào |

## 11 Những câu dễ hiểu sai và cách nói chính xác hơn

| Câu dễ nhầm | Cách nói phù hợp với dữ liệu dự án |
|---|---|
| Có lãi 100 tỷ nghĩa là đã thu thêm 100 tỷ tiền | Có LNST 100 tỷ; xem CFO và các nhóm dòng tiền để đọc luồng tiền |
| CFO âm nghĩa là không còn tiền | CFO âm trong kỳ; số dư tiền còn phụ thuộc đầu kỳ và các nhóm dòng tiền khác |
| VCSH là tiền của chủ đang nằm trong ngân hàng | VCSH là phần còn lại về kế toán sau nợ, không phải số dư tiền |
| Nợ/tài sản 50% là nợ ngân hàng 50% | Tổng nợ phải trả bằng 50% tài sản; cần cơ cấu để biết phần nợ vay |
| CFO/LNST thấp chắc là gian lận | Hai đại lượng khác biệt; cần thêm bằng chứng để giải thích |
| Chia cổ tức 25% là lãi 25% trên giá mua | Phải xem tỷ lệ trên mệnh giá và giá mua/giá dùng để tính lợi suất |
| DPS giảm là cổ đông luôn nhận ít tiền hơn | Kiểm tra cơ sở cổ phiếu, số cổ phiếu đủ quyền và lịch sử đủ |
| Ngày trả đã qua nên doanh nghiệp đã trả | Đó là lịch công bố; xác nhận thực trả cần bằng chứng riêng |
| Không có thông báo trong dữ liệu nghĩa là không chia | Có thể thiếu nguồn/đợt; cần xác nhận rõ để ghi 0 |
| Tương quan cao nghĩa là CFO quyết định cổ tức | Có quan hệ mô tả trên mẫu; chưa chứng minh nhân quả |

## 12 Tự kiểm tra xem đã nắm được chưa

Thử trả lời trước khi đọc cột đáp án:

| Câu hỏi | Đáp án ngắn |
|---|---|
| Bán 100, mới thu 30 thì doanh thu có bắt buộc là 30 không? | Không; nếu đủ điều kiện ghi nhận, doanh thu có thể là 100, phần chưa thu là khoản phải thu |
| Có LNST dương và CFO âm cùng kỳ được không? | Được; ví dụ cửa hàng là LNST 48 và CFO −22 |
| CFO âm nhưng tiền cuối kỳ dương được không? | Được; còn tiền đầu kỳ, vốn góp, vay hoặc dòng tiền khác |
| Tài sản 1.000, nợ phải trả 400 thì VCSH bao nhiêu? | 600, theo đẳng thức cân đối |
| CFO 40, LNST 120 thì tỷ số nói được gì? | Khoảng 0,33 lần; chưa nói nguyên nhân khác biệt |
| Nợ/tài sản từ 40% lên 50% tăng mấy điểm phần trăm? | 10 điểm phần trăm; tăng tương đối của tỷ lệ là 25% |
| Cổ tức 25% trên mệnh giá 10.000 là DPS bao nhiêu? | 2.500 đồng/cổ phiếu |
| Notice đăng 2025 có phần thuộc lợi nhuận 2024 thì ghép năm nào? | Phần đó ghép BCTC/năm lợi nhuận 2024 |
| Năm trước đủ 1.500, năm nay mới tìm thấy 1.000 thì kết luận giảm được chưa? | Chưa, phải kiểm tra đã rà đủ và cùng cơ sở cổ phiếu |
| Có tương quan LNST–DPS thì đã có mô hình dự báo chưa? | Chưa; mô tả mẫu khác đánh giá dự báo tương lai |

## 13 Dùng tài liệu này cùng tài liệu chức năng

Sau khi hiểu khái niệm, đọc [giải thích chức năng và dữ liệu](17-giai-thich-chuc-nang-va-du-lieu.md) để gắn mỗi kiến thức với thao tác của hệ thống. Khi cần tên trường/điều kiện chính xác, dùng [từ điển dữ liệu](12-kien-thuc-tai-chinh-va-tu-dien.md), [quy tắc phân tích](13-ghep-co-tuc-va-phan-tich.md) và [SRS](02-de-tai-va-srs.md).

Nguồn quốc tế được dùng để học cơ chế và thuật ngữ; khi đọc dữ liệu Việt Nam vẫn phải theo nội dung, phạm vi và đơn vị của BCTC/thông báo thực tế. Tài liệu này không đặt thêm mô hình, chỉ tiêu hoặc chức năng ngoài phạm vi đã chốt.
