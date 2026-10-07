# Đề tài và đặc tả hiện hành

**Cơ sở nhu cầu bổ sung 05/10/2026:** [nghiên cứu giá trị BCTC–cổ tức](reports/dot-01-tuan-01-02/co-so-hoc-thuat-va-gia-tri-su-dung.md) đưa ra câu hỏi người dùng U1–U6 cho pilot và U7–U8 mở rộng, căn cứ học thuật/nghề nghiệp, dữ liệu còn thiếu và cách đo lợi ích. [Báo cáo 1](reports/dot-01-tuan-01-02/bao-cao-01.md) đã gắn nhóm chức năng với các câu hỏi này. Mã U là ma trận giải thích trong báo cáo, không thay các mã yêu cầu/TC của SRS v3.1 hoặc tự mở rộng phạm vi đã dự toán.

## Bổ sung nhu cầu theo hướng kết hợp ngày 05/10/2026

Phiên bản nhu cầu 2.4; SRS v3.1 là nguồn yêu cầu hiện hành. Câu hỏi thêm: CFO khác lợi nhuận ở những dòng nào và phần nào chưa giải thích được? Người vận hành duyệt các dòng của BCLCTT gián tiếp; người đọc mở cầu nối LNTT→CFO cạnh LNST, đọc nguồn từng khoản rồi đối chiếu DPS theo năm lợi nhuận. Đây là phân rã số học, chưa là kết luận nhân quả. Tối thiểu một ca thật; 1–3 ca theo gate. P/US/PF/AN nền bên dưới giữ nguyên; E01–E10 và P01–P11 là bổ sung tại mục 15 SRS. Không nâng sáu chỉ tiêu toàn mẫu thành yêu cầu mọi dòng BCLCTT cho mọi công ty.

**Đặc tả triển khai cập nhật ngày 05/10/2026:** [SRS-FAP-01 v3.1](22-srs-dac-ta-yeu-cau-phan-mem.md) là nguồn yêu cầu chi tiết hiện hành, gồm FR/BR/DR/IR/NFR, use case và truy vết kiểm chứng; [bản Word](reports/SRS-FAP-01-v3.1.docx). Nội dung v2.3 bên dưới được giữ làm nguồn bài toán, P/US/PF/AN và ví dụ thiết kế. Khi có khác biệt về mức chi tiết/phạm vi, dùng v3.1; trạng thái vẫn là dự thảo chưa ghi nhận phê duyệt của giảng viên.

Phiên bản **2.3 ngày 04/10/2026**, giữ tên/phạm vi v2.2 sau nghiên cứu lần hai; làm rõ hủy đối tượng thực hiện quyền và đổi ưu tiên liên thông sang đối chiếu phiên bản/ảnh hưởng. Kế thừa câu chuyện người dùng, yêu cầu và tiêu chí nghiệm thu của v2.1. Tên:
**Xây dựng hệ thống thu thập, chuẩn hóa và phân tích lợi nhuận, dòng tiền kinh doanh trong mối liên hệ với cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam.**

### Trọng tâm triển khai và bảo vệ đã chốt ngày 04/10/2026

Đóng góp chính là quy trình thu thập tài liệu, trích xuất, lọc và làm sạch, chuẩn hóa, xử lý sự kiện cổ tức, kiểm định chất lượng và phân tích dữ liệu có truy vết. Giao diện phục vụ vận hành, tra cứu, kiểm tra nguồn và trình bày kết quả; độ phức tạp phát triển web không phải trọng tâm đề tài. Minh chứng đánh giá dựa trên bộ đối chiếu thủ công, độ đúng từng bước, lỗi nghiệp vụ, tính tái lập và công sức xử lý theo tài liệu đánh giá hiện hành.

Đây là việc xác định rõ trọng tâm đã có trong thiết kế, không thay đổi câu chuyện người dùng, sáu trường tài chính lõi, phạm vi pilot/đích có gate, quy tắc DPS công bố, kiến trúc hay các tiêu chí nghiệm thu. Nghiên cứu quan hệ lợi nhuận–CFO–DPS vẫn phục vụ lựa chọn dữ liệu và phân tích mô tả. Hướng dự đoán cho tốt nghiệp tiếp tục có điều kiện về dữ liệu, không trở thành yêu cầu project hiện tại.

**Kết quả nghiên cứu lần hai:** kiểm định có truy vết và vòng đời cổ tức là lõi. Đồ án ưu tiên đối chiếu phiên bản và giải thích ảnh hưởng tới ratios/aggregates/case; predictor là tùy chọn. [Quyết định và prior art](20-nghien-cuu-lan-hai-va-chot-de-tai.md). Word/slide xuất trước lượt này chưa chứa cập nhật v2.3.

## 1 Bài toán và người dùng

Người đọc muốn thấy mức cổ tức công bố biến động cùng lợi nhuận và dòng tiền ra sao, với bằng chứng đúng doanh nghiệp/kỳ/phạm vi. Luồng sử dụng: chọn doanh nghiệp → xem mức đầy đủ → xem chuỗi năm và timeline → đọc chỉ số/case → mở trang nguồn. Người vận hành kiểm tra candidates, sự kiện điều chỉnh, năm lợi nhuận và sửa có audit.

Phân tích là lịch sử/mô tả, không xác suất duy trì cổ tức, đánh giá khả năng thanh toán pháp lý, nhân quả hoặc khuyến nghị mua bán.

### 1.1 Mục đích hệ thống

Hệ thống hỗ trợ người theo dõi doanh nghiệp niêm yết **đọc và đối chiếu lịch sử lợi nhuận sau thuế, dòng tiền kinh doanh và mức cổ tức tiền mặt được công bố cho từng năm lợi nhuận**. Người dùng cần biết lợi nhuận tăng có đi kèm CFO tăng hay không; cổ tức tăng, giữ nguyên hay giảm trong bối cảnh đó; và kết luận đang dựa trên tài liệu nào, có thiếu dữ liệu nào không.

Kết quả phục vụ bước tìm hiểu và lựa chọn trường hợp cần đọc sâu trước khi người dùng tự đánh giá doanh nghiệp. Người đọc không phải tự gom các PDF, nhập lại sáu chỉ tiêu, rà từng đợt cổ tức và tính lại mọi tỷ số mỗi lần có thông báo sửa đổi. Hiệu quả giảm công sức phải được đo, chưa coi là kết quả đã đạt.

### 1.2 Người dùng và nhu cầu

| Vai trò | Việc cần làm | Kết quả mong muốn |
|---|---|---|
| Người đọc chính: cá nhân theo dõi doanh nghiệp phi tài chính, có kiến thức tài chính cơ bản | Xem một doanh nghiệp qua nhiều năm, đối chiếu lợi nhuận–CFO–DPS, kiểm chứng điểm khác biệt | Bảng/biểu đồ đúng kỳ và phạm vi, số cụ thể, lý do thiếu hoặc không so sánh được, đường dẫn tới bằng chứng |
| Người nghiên cứu: sinh viên/người làm phân tích dữ liệu | Chọn tập quan sát hợp lệ, xem quan hệ mô tả và xuất kết quả để tái lập | Snapshot kèm nguồn, điều kiện lọc, số quan sát và công thức; ba case có thể kiểm tra |
| Người vận hành: người thực hiện đề tài | Thu tài liệu, duyệt kết quả trích, xử lý thiếu/trùng/sửa/hủy | Danh sách việc cần review và lịch sử trước–sau; số chưa duyệt không xuất thành kết quả chính thức |

Đây là các vai trò sử dụng, chưa yêu cầu tài khoản, phân quyền hoặc phục vụ nhiều người đồng thời trong MVP.

### 1.3 Câu chuyện nền cho project

**Tình huống giả định để thiết kế sản phẩm, chưa phải kết quả khảo sát người dùng:** Minh là người theo dõi cổ tức tiền mặt của một số doanh nghiệp phi tài chính. Minh thấy doanh nghiệp X báo lợi nhuận tăng và có thông báo cổ tức, nhưng muốn biết trong ba năm gần đây dòng tiền kinh doanh có cùng chiều với lợi nhuận không, và mức cổ tức công bố thay đổi ra sao. Minh cần hiểu số liệu trước khi lựa chọn doanh nghiệp để tìm hiểu sâu hơn.

Nếu làm thủ công, Minh phải mở BCTC từng năm, xác định đúng báo cáo hợp nhất hoặc cấp doanh nghiệp, tìm lợi nhuận và CFO, đổi đơn vị rồi nhập bảng. Sau đó Minh tìm các thông báo cổ tức: một thông báo có thể gộp hai năm lợi nhuận, một đợt có thể được đăng ở hai nơi, hoặc lịch/mức tiền có bản sửa. Nếu cộng theo năm đăng thông báo hoặc coi năm không tìm thấy thông báo là không chia cổ tức, Minh sẽ so sánh sai.

Trong luồng sử dụng dự kiến, Minh chọn X và giai đoạn 2023–2025. Hệ thống hiển thị dữ liệu đã duyệt, phạm vi BCTC, độ đầy đủ theo năm và các đợt cổ tức. Minh xem hai đường lợi nhuận–CFO, tỷ số CFO/LNST và chuỗi DPS theo năm lợi nhuận; bấm vào một kết quả để xem công thức, số đầu vào và trang nguồn. Nếu năm 2025 chưa rà đủ thông báo, hệ thống ghi tổng phần đã quan sát và lý do thiếu, chưa kết luận cổ tức năm đó giảm. Minh xuất snapshot để ghi lại bằng chứng và những câu hỏi còn cần đọc sâu.

**Điểm kết thúc câu chuyện:** Minh trả lời được dữ liệu đã cho thấy điều gì, điều gì chưa thể kết luận và cần mở tài liệu nào để kiểm chứng. Việc mua/bán cổ phiếu và khẳng định doanh nghiệp sẽ tiếp tục trả cổ tức nằm ngoài kết quả của project.

### 1.4 Vấn đề thực tế và cách giải quyết trong phạm vi

| Mã | Vướng mắc trong công việc người dùng | Hệ thống xử lý | Bằng chứng nghiệm thu |
|---|---|---|---|
| P01 | Phải gom BCTC và thông báo cổ tức rời rạc rồi nhập tay | Thu nguồn, chuẩn hóa sáu chỉ tiêu, gom sự kiện theo doanh nghiệp/năm | PF02–PF03; log discovery và phép đo công sức so với quy trình nhập tay tương đương |
| P02 | Đọc lợi nhuận đơn lẻ nên không thấy CFO đang thấp, giảm hoặc âm | Đặt lợi nhuận và CFO cạnh nhau, hiển thị biến động và CFO/LNST có điều kiện | AN01–AN02; số tính tay khớp và nguồn của cả hai đại lượng mở được |
| P03 | Cộng sai cổ tức do nhiều đợt, khác năm lợi nhuận, đăng trùng hoặc điều chỉnh | Tách components, liên kết cùng đợt, dùng bản có hiệu lực và kiểm tra cơ sở cổ phiếu | AN04–AN05; notice hai năm, bản sửa và bản hủy cho tổng đúng |
| P04 | Nhầm thiếu dữ liệu thành 0 hoặc so sánh khác đơn vị/phạm vi | Hiển thị coverage/missing, kiểm tra kỳ–đơn vị–scope–basis trước phép tính | US01, US04; ca thiếu/chưa tương thích không tạo kết luận tăng/giảm |
| P05 | Không biết một tỷ số/nhận xét lấy từ đâu, khó kiểm tra hoặc làm lại | Truy ngược operands tới nguồn; lưu phiên bản, công thức và snapshot | US05, US07; 100% giá trị xuất bản truy nguồn được và snapshot cũ tái tính được |
| P06 | Khó tập hợp các trường hợp lợi nhuận, CFO và cổ tức biến động khác nhau | Biểu đồ và bộ lọc theo điều kiện số liệu để chọn case có bằng chứng | AN06–AN07; trả danh sách/case kèm n và phần thiếu, chưa suy nguyên nhân hoặc tương lai |

Các vấn đề trên là giả thuyết nhu cầu để xây sản phẩm. Khi pilot, ghi nhận quy trình của người dùng thử, lỗi thực tế và công sức; chưa khẳng định đã khảo sát hoặc đã chứng minh mức tiết kiệm.

## 2 Scope dữ liệu

Pilot 3 doanh nghiệp × 2023–2025 = 9 BCTC năm và các thông báo liên quan. Mục tiêu mở rộng 5–8 doanh nghiệp, 15–24 BCTC năm sau gate tuần 4. Sáu trường lõi: net_income_total, cfo, cash_equivalents, total_assets, total_liabilities, total_equity. EPS, LNST cổ đông mẹ, doanh thu, nợ vay, capex và ngắn hạn chỉ thêm nếu cần câu hỏi cụ thể và có dữ liệu đúng.

Ưu tiên phi tài chính, BCTC năm kiểm toán và series hợp nhất khi có. Báo cáo cấp doanh nghiệp phải được xác nhận; scope khác được tách cohort/series, không gộp tùy tiện. BCTC riêng công ty mẹ dùng làm bối cảnh khi thu được, không bắt buộc tải đôi toàn mẫu.

Đích cổ tức: **mức tiền mặt được công bố trên mỗi cổ phiếu và năm lợi nhuận**. Sự kiện có ngày công bố, chốt quyền, lịch thanh toán, trạng thái sửa/hủy. Paid confirmation là optional có bằng chứng; ngày thanh toán đã qua không đủ để gán paid. Một case 2026 có thể dùng chứng minh cập nhật.

## 3 Yêu cầu MVP

| Mã | Chức năng | Nghiệm thu |
|---|---|---|
| PF01 | Công ty/kỳ/coverage | Expected ledger với lý do missing, trạng thái source/scope |
| PF02 | Tự thu BCTC và sự kiện | Ít nhất một adapter tự phát hiện danh mục BCTC và một luồng tự phát hiện thông báo cổ tức; seed danh mục/search hợp lệ, không seed từng file như bằng chứng tự phát hiện; fallback nhập ghi riêng |
| PF03 | Trích và chuẩn hóa | Sáu financial targets; event/components; raw value, unit, period, scope, source hash và locator |
| PF04 | Validation/review | Trước/sau/lý do, không xuất candidate chưa duyệt như fact đúng |
| PF05 | Lưu phiên bản | SQLite constraints/transaction; chạy lại không trùng; nguồn sửa có lịch sử |
| PF06 | Ghép doanh nghiệp–năm | DPS quan sát và trạng thái đủ dữ liệu riêng; năm lợi nhuận khác năm lịch; sửa/hủy không cộng trùng |
| PF07 | Phân tích mối quan hệ | Xu hướng, CFO/LNST hợp lệ, tiền/nợ trên tài sản, DPS biến động khi tương thích; số mẫu và giới hạn |
| PF08 | Dashboard/export | Timeline và chart, mở nguồn/operand, chất lượng, snapshot CSV/JSON |
| PF09 | Demo và đánh giá | File/thông báo mới qua luồng, lỗi được phát hiện, baseline/holdout và ba case |

Tự crawl cổ tức đầy đủ là gate chưa vượt, dù bốn thông báo mẫu đã trích được. Khi nguồn chỉ cho phép nhập có provenance, báo rõ tỷ lệ và hạn chế; không nghiệm thu PF02 như đã tự phát hiện. Không cần FastAPI/React hoặc nhiều người dùng trong MVP. Stack một app Python/Streamlit/SQLite.

### 3.1 Hệ thống phải phân tích cụ thể những gì

Các yêu cầu AN dưới đây cụ thể hóa PF06–PF08, dùng sáu trường lõi và sự kiện cổ tức đã nêu. Không thêm ML, giá thị trường, dữ liệu quý hoặc chỉ tiêu mở rộng thành nghĩa vụ MVP. Mọi kết quả phải kèm doanh nghiệp, kỳ, scope, đơn vị, snapshot và nguồn/operands; kết quả không tính được phải có lý do.

| Mã và câu hỏi người dùng | Đầu vào và phép xử lý | Đầu ra phải thấy | Điều kiện và giới hạn |
|---|---|---|---|
| AN01 — Lợi nhuận và CFO đã tăng/giảm thế nào qua các năm? | LNST tổng và CFO năm đã duyệt; tính mức và chênh lệch năm sau trừ năm trước; tăng trưởng LNST khi nền >0 | Bảng và hai đường cùng đơn vị; chênh lệch tiền và % LNST nếu hợp lệ; chỉ rõ năm lợi nhuận tăng nhưng CFO giảm/âm | Cùng scope, kỳ năm tương thích; thiếu năm thì để khoảng trống; nền LNST <=0 không xuất % tăng trưởng thông thường |
| AN02 — CFO bằng bao nhiêu lần lợi nhuận của cùng năm? | CFO / LNST tổng khi LNST >0 | Giá trị tỷ số từng năm, công thức, hai operands; diễn giải như “CFO bằng 0,33 lần LNST” hoặc “CFO âm trong khi LNST dương” | CFO âm vẫn tính được nếu LNST dương; LNST <=0 trả trạng thái không áp dụng cho cách diễn giải này; không suy gian lận, nguyên nhân CFO yếu hoặc chắc chắn cắt cổ tức |
| AN03 — Tiền và nợ phải trả chiếm bao nhiêu tổng tài sản? | Tiền và tương đương tiền / tổng tài sản; nợ phải trả / tổng tài sản; hiển thị VCSH trong bảng lõi và kiểm tra cân đối theo quy tắc validation | Hai tỷ lệ %, mức/chênh lệch theo năm để đọc bối cảnh cơ cấu tài chính; issue nếu cân đối không khớp tolerance đã chốt | Tài sản >0, cùng ngày/scope/đơn vị; nợ phải trả không gọi là nợ vay; các tỷ lệ này không chứng minh pháp nhân mẹ đủ tiền chia cổ tức |
| AN04 — Một năm lợi nhuận được công bố bao nhiêu đồng cổ tức tiền mặt trên mỗi cổ phiếu? | Tổng components active đã duyệt, rõ profit_year và cùng basis; rà coverage | Bảng năm lợi nhuận, các đợt thành phần, observed_dps; annual_announced_dps chỉ khi đủ; mức/chênh lệch và % DPS khi hợp lệ | Thiếu notice không là 0; năm chưa đủ không dùng để kết luận mức năm giảm; % chỉ khi nền >0 và cả hai năm đủ/comparable; basis chưa rõ thì giữ từng đợt, chặn tổng |
| AN05 — Lịch sử công bố và bản sửa ảnh hưởng dữ liệu thế nào? | Published/record/scheduled payment dates, relations sửa/hủy/đăng trùng và phiên bản nguồn | Timeline với trạng thái/lịch hiện hành, năm lợi nhuận của từng component và lịch sử thay đổi; tổng được cập nhật đúng | Sửa lịch không thêm DPS; sửa mức thay component cũ; hủy loại khỏi tổng active; ngày thanh toán qua không đổi thành xác nhận đã trả |
| AN06 — Cổ tức thay đổi cùng chiều hay khác chiều với lợi nhuận và CFO trong dữ liệu đã có? | Ghép doanh nghiệp–năm; đối chiếu mức và chênh lệch AN01 với AN04; bộ lọc “LNST tăng, CFO giảm” và “DPS giữ nguyên/tăng, LNST hoặc CFO giảm” | Các biểu đồ xếp theo cùng trục năm nhưng trục giá trị riêng cho VND và VND/cổ phiếu; danh sách trường hợp thỏa điều kiện, số quan sát hợp lệ/bị loại và lý do | Chỉ xét phần cần thiết đủ/comparable; bộ lọc là điều kiện quan sát, không điểm rủi ro; không chia CFO cho DPS hoặc suy quan hệ nhân quả |
| AN07 — Trên tập hợp lệ, các biến có quan hệ mô tả ra sao và có ngoại lệ nào? | Scatter và Spearman cho cặp biến được ghi rõ, chẳng hạn thay đổi % LNST và % DPS; xác định cohort/scope và snapshot trước khi tính | Hệ số nếu đủ điều kiện tính, n, tên hai biến/đơn vị, bộ lọc, danh sách phần loại; ba case có số liệu và nguồn | Mẫu <3 cặp hoặc một biến hằng thì không xuất hệ số; từ 3 cặp trở lên vẫn ghi mẫu nhỏ/phụ thuộc công ty, không coi là bằng chứng tin cậy; không gộp số tuyệt đối khác quy mô để kết luận chung |

Các điều kiện cụ thể và phép xử lý missing tuân theo [quy tắc ghép/phân tích](13-ghep-co-tuc-va-phan-tich.md). Ba case thật chỉ chọn sau khi đã kiểm chứng dữ liệu; nếu không có trường hợp đáp ứng một mẫu tình huống thì báo chưa tìm thấy, không tự tạo doanh nghiệp hoặc số liệu.

### 3.2 User stories và tiêu chí chấp nhận

User story mô tả nhu cầu theo vai trò; câu chuyện nền ở 1.3 giải thích vì sao các nhu cầu này phát sinh. Các câu “Khi–thì” dưới đây là hành vi phải kiểm tra khi triển khai, chưa phải chức năng đã hoàn thành.

**US01 — Xem đúng dữ liệu và độ đầy đủ (P04; PF01, PF03, PF08).** Là người đọc, tôi muốn chọn doanh nghiệp và giai đoạn để biết những năm/chỉ tiêu/đợt cổ tức nào đã có bằng chứng trước khi đọc kết quả phân tích.

- Khi chọn X, 2023–2025, thì thấy sáu trường lõi, scope và coverage riêng cho BCTC/cổ tức của từng năm.
- Khi một trường hoặc nguồn thiếu/chưa duyệt, thì thấy trạng thái và lý do; không hiển thị thành 0 hoặc tự lấp bằng năm khác.

**US02 — Đối chiếu lợi nhuận với CFO (P02; PF07–PF08; AN01–AN02).** Là người đọc, tôi muốn xem lợi nhuận và dòng tiền kinh doanh cạnh nhau để nhận ra những năm hai đại lượng biến động khác chiều.

- Khi dữ liệu cùng kỳ/scope đã duyệt, thì bảng, biểu đồ, chênh lệch và CFO/LNST khớp tính tay; CFO âm vẫn hiển thị đúng dấu.
- Khi LNST <=0 hoặc hai operands khác scope/kỳ, thì tỷ số không trả một giá trị thông thường và có lý do tương ứng.

**US03 — Xem cổ tức theo đúng năm lợi nhuận (P03; PF05–PF06, PF08; AN04–AN05).** Là người đọc, tôi muốn thấy từng đợt và tổng DPS có hiệu lực theo năm lợi nhuận để không cộng sai theo ngày đăng hoặc lịch thanh toán.

- Khi một thông báo gộp hai năm, thì từng component vào đúng năm; một đợt đăng ở hai nguồn chỉ cộng một lần sau review identity.
- Khi sửa lịch, tổng DPS giữ nguyên; khi sửa mức, component có hiệu lực thay đổi đúng và bản cũ vẫn xem được. Khi hủy, xác định rõ đối tượng bị hủy và quan hệ tới bản cũ; hủy ngày đăng ký/thông báo thực hiện quyền không tự gán DPS năm bằng 0, không tự hủy mọi quyết định cổ tức; nếu chưa rõ bản thay thế thì coverage cần review.
- Khi lịch thanh toán đã qua mà chưa có bằng chứng thực trả, thì trạng thái vẫn là lịch thanh toán/chưa xác nhận thực trả.

**US04 — So sánh trên dữ liệu đủ và tương thích (P04, P06; PF06–PF08; AN03–AN04, AN06).** Là người đọc, tôi muốn hệ thống kiểm tra điều kiện so sánh để biết kết luận nào có thể sử dụng và kết luận nào phải chờ thêm dữ liệu.

- Khi hai năm DPS đủ, cùng basis và nền dương, thì xem được chênh lệch/%; khi partial/unknown hoặc basis chưa xử lý, thì thấy lý do chặn so sánh annual.
- Khi lọc “LNST tăng, CFO giảm”, thì chỉ trả cặp năm có đủ hai biến cùng scope; lọc có DPS phải kiểm tra thêm annual coverage/basis và báo số bị loại.
- Khi tài sản <=0 hoặc khác ngày/scope, thì không xuất tỷ lệ tiền/tài sản hoặc nợ phải trả/tài sản như kết quả hợp lệ.

**US05 — Kiểm chứng một con số (P05; PF03, PF05, PF07–PF08).** Là người đọc, tôi muốn bấm một số hoặc nhận xét để mở bằng chứng và công thức, giúp tự kiểm tra kết quả.

- Khi mở một ratio, thì thấy công thức/phiên bản công thức, giá trị và IDs các operands, kỳ, scope, đơn vị, source version/hash và locator.
- Khi mở tổng DPS hoặc case, thì thấy components/nguồn đang có hiệu lực và trạng thái coverage; mở được tài liệu/URL nguồn và vị trí bằng chứng tương ứng.

**US06 — Duyệt và sửa dữ liệu có lịch sử (P01, P03–P04; PF02–PF05).** Là người vận hành, tôi muốn xử lý candidates và các issue để lỗi OCR/ghép không đi vào kết quả công bố.

- Khi collector/extractor tạo candidate chưa duyệt hoặc phát hiện thiếu kỳ/scope/đơn vị/năm lợi nhuận, thì đưa vào danh sách review; không xuất thành fact đã xác nhận.
- Khi sửa một giá trị/quan hệ sự kiện, thì lưu trước–sau, lý do, người duyệt và phiên bản trong transaction; rollback không để dữ liệu mới thiếu audit.
- Khi chạy lại cùng tài liệu/notice, thì không thêm trùng; nguồn đổi nội dung thì tạo phiên bản và giữ snapshot cũ.

**US07 — Xuất kết quả để làm lại (P05; PF05, PF08–PF09).** Là người nghiên cứu, tôi muốn xuất snapshot CSV/JSON kèm manifest để báo cáo và tái tính trên đúng tập dữ liệu đã dùng.

- Khi export, thì nhận dữ liệu cùng snapshot ID/as_of, filters, units/scopes, phiên bản/config công thức, nguồn/operands, coverage và phần missing/excluded.
- Khi tái tính bằng snapshot/config đó, thì khớp giá trị theo quy tắc tolerance đã công bố; nguồn cập nhật sau không đổi snapshot cũ.

**US08 — Đọc quan hệ mô tả và case (P06; PF07–PF09; AN06–AN07).** Là người nghiên cứu, tôi muốn xem mối quan hệ và ngoại lệ có bằng chứng để trình bày điều dữ liệu lịch sử cho thấy.

- Khi đủ điều kiện, thì scatter/hệ số có tên biến, bộ lọc, n và phần bị loại; nếu biến hằng hoặc <3 cặp thì trả lý do không tính.
- Khi đọc một trong ba case nghiệm thu, thì thấy facts, operands, timeline, coverage, snapshot, nguồn và giới hạn diễn giải; không nhận xác suất/khuyến nghị mua bán từ MVP.

### 3.3 Kịch bản minh họa có kết quả kiểm tra được

**Toàn bộ số dưới đây là giả định của doanh nghiệp X, chỉ làm fixture thiết kế/nghiệm thu.** Không dùng chúng làm case thực nghiệm hoặc bằng chứng đã có dữ liệu thị trường. Giả định ba BCTC cùng scope, tất cả số đã duyệt và cổ tức đủ trên cùng basis tại snapshot.

| Năm lợi nhuận | LNST (tỷ VND) | CFO (tỷ VND) | Tiền (tỷ VND) | Tài sản (tỷ VND) | Nợ phải trả (tỷ VND) | VCSH (tỷ VND) | DPS công bố đủ (VND/cổ phiếu) |
|---|---|---|---|---|---|---|---|
| 2023 | 100 | 90 | 120 | 1.000 | 400 | 600 | 1.000 |
| 2024 | 120 | 40 | 100 | 1.100 | 550 | 550 | 1.500 |
| 2025 | 80 | -10 | 70 | 1.200 | 660 | 540 | 1.400 |

Kết quả mong đợi:

1. Năm 2024: LNST tăng 20 tỷ, tương ứng 20%; CFO giảm 50 tỷ; CFO/LNST = 1/3, hiển thị khoảng 0,33 lần, giảm từ 0,90 lần năm 2023. DPS tăng 500 đồng, tương ứng 50%. Hệ thống mô tả “LNST và DPS tăng trong khi CFO giảm”, chưa kết luận vì sao hoặc cổ tức có bền vững không.
2. Năm 2025: LNST giảm 40 tỷ; CFO âm 10 tỷ; CFO/LNST = -0,125 lần. Tiền/tài sản khoảng 5,83%; nợ phải trả/tài sản 55%. DPS giảm 100 đồng, khoảng 6,67%. Hệ thống trình bày các biến đồng thời, chưa kết luận biến nào gây ra biến nào.
3. Một notice đăng năm 2026 gồm 350 đồng thuộc 2024 và 1.000 đồng thuộc 2025: phân bổ đúng hai năm. Các components khác là 1.150 đồng thuộc 2024 và 400 đồng thuộc 2025, nên tổng tương ứng 1.500/1.400. Giả định component 2025 ban đầu 500 đồng được sửa thành 400: bản cũ không được cộng thêm; sửa lịch tiếp theo giữ tổng 1.400.
4. Biến thể thiếu dữ liệu: nếu chưa xác nhận độ đầy đủ năm 2025 nhưng đã quan sát 1.400 đồng, chỉ hiển thị observed_dps = 1.400 với partial; annual_announced_dps và % thay đổi annual chưa tính. Không xuất câu “cổ tức 2025 giảm 6,67%”.
5. Biến thể LNST =0 hoặc âm: CFO/LNST theo AN02 trả trạng thái riêng. Biến thể basis chưa rõ: không cộng các components khác basis thành tổng dù có đủ notice.

Giá trị lưu/tính dùng độ chính xác gốc; số làm tròn trên màn hình phải ghi quy tắc. Fixture giúp kiểm tra phép tính và luồng lỗi; nghiệm thu dữ liệu thật vẫn theo [protocol đánh giá](06-danh-gia-va-nghiem-thu.md).

## 4 Đóng góp IT

Adapter/rate-limit/retry/conditional GET, xử lý PDF scan, parser metadata và bảng, event identity/lifecycle, mô hình nhiều thành phần năm lợi nhuận, coverage và review audit, phép tính có operands, UI truy vết và kiểm thử. Đo chất lượng dữ liệu và công sức là bằng chứng chính. Rubric của trường vẫn cần đối chiếu; không chỉ dùng tên thư viện để kết luận đạt IT.

## 5 Câu hỏi và gate

RQ1: Collector chọn đúng/tải được bao nhiêu tài liệu và sự kiện đã công bố trên expected set?
RQ2: Text-only so OCR/parser/review cải thiện đúng joint và công sức thế nào?
RQ3: Chuỗi lợi nhuận–CFO–DPS có những quan hệ/ngoại lệ mô tả nào trên mẫu đủ dữ liệu?
RQ4: Kết quả có tái tính và truy nguồn/phiên bản được không?

100% giá trị xuất bản có provenance, kỳ/unit/scope; tổng DPS năm chỉ được gọi đầy đủ khi ledger được review. Gate tuần 4 quyết định scope; tuần 8 freeze holdout. Ngưỡng accuracy mục tiêu thăm dò 95% trước review cần chấm trên target đã freeze, không phải kết quả đạt. Thống kê nhỏ không trở thành bằng chứng nhân quả.

Phương pháp chi tiết: [thu thập/xử lý](11-phuong-phap-thu-thap-va-xu-ly.md), [ghép/phân tích](13-ghep-co-tuc-va-phan-tich.md).

## 6 Câu chuyện và mục đích dự kiến cho đồ án tốt nghiệp

**Ưu tiên cập nhật sau nghiên cứu lần hai:** người vận hành nhận tài liệu/thông báo mới, muốn biết số/trường nào thay đổi, kết quả nào bị ảnh hưởng và giữ được snapshot cũ. Nhánh đối chiếu phiên bản/ảnh hưởng được chọn trước predictor; protocol và gate trong [hướng tốt nghiệp](09-lien-thong-tot-nghiep.md). Câu chuyện GUS01 bên dưới được giữ làm **phương án dự đoán tùy chọn**, không là lộ trình bắt buộc hay tiêu chí nghiệm thu project.

**Cần xác định trước để định hướng dữ liệu, chưa đưa vào nghiệm thu project.** Câu chuyện nền: sau khi sử dụng dữ liệu lịch sử, Minh lập danh sách doanh nghiệp cần theo dõi ở thời điểm một BCTC năm vừa được công bố. Minh muốn biết doanh nghiệp nào cần ưu tiên kiểm tra khả năng mức cổ tức công bố sắp tới giảm so với giai đoạn trước, thay vì đọc sâu mọi doanh nghiệp như nhau. Minh cần tín hiệu kèm dữ liệu đã biết tại thời điểm đánh giá, giới hạn và bằng chứng kiểm định để quyết định thứ tự đọc tài liệu.

**GUS01 — Ưu tiên theo dõi khả năng giảm mức cổ tức công bố.** Là người theo dõi cổ tức, tôi muốn nhận một ước lượng/tín hiệu về việc DPS công bố trong 12 tháng sau cutoff giảm so với cửa sổ trước, để chọn doanh nghiệp cần đọc sâu; tôi muốn biết ước lượng dựa trên thông tin nào và được đánh giá ra sao.

- Đầu vào dự kiến: BCTC, lịch sử công bố cổ tức và các đặc trưng đã khả dụng tại cutoff; không dùng bản sửa hoặc sự kiện tương lai để tạo feature lịch sử.
- Đầu ra dự kiến: trạng thái “giảm” hoặc “không giảm” theo protocol đã chốt, hoặc “không đủ điều kiện đánh giá”; xác suất chỉ hiển thị khi mô hình đã được đánh giá và hiệu chỉnh phù hợp. “Không giảm” bao gồm duy trì/tăng, không gọi tất cả là giữ nguyên.
- Chấp nhận trong tốt nghiệp: target/cửa sổ/ngưỡng giảm chốt trước test; nhãn đủ coverage/basis và cửa sổ trưởng thành; tách thời gian; so baseline; công bố số mẫu, precision/recall/F1/PR-AUC của lớp giảm và giới hạn. Không đủ dữ liệu thì báo chưa đánh giá được, không giả tạo predictor.
- Vấn đề muốn giải quyết: sắp thứ tự kiểm tra sâu từ danh sách theo dõi; lợi ích này còn cần đánh giá với người dùng và kết quả mô hình, không tự suy từ chỉ số kỹ thuật.

Project chuẩn bị nguồn/phiên bản, published_at và first_seen_at riêng, facts/events/coverage/snapshots để kiểm tra tính khả dụng của dữ liệu cho hướng này. Phân tích hồi cứu theo profit_year không được dùng nguyên trạng như bộ dự báo tại cutoff. Định nghĩa chi tiết và điều kiện mở rộng nằm ở [hướng tốt nghiệp](09-lien-thong-tot-nghiep.md).

## 7 Dùng SRS khi trình bày ý tưởng

Trình bày theo thứ tự **câu chuyện Minh → vấn đề P01–P06 → mục đích → câu hỏi AN01–AN07 và một kết quả minh họa → luồng sản phẩm/user stories → giới hạn project và câu chuyện tốt nghiệp → cách nghiệm thu**. Không chỉ liệt kê “crawl dữ liệu”, “phân tích BCTC”, “dashboard” hoặc tên thư viện.

[Tài liệu trình bày ý tưởng và câu chuyện người dùng](16-y-tuong-va-cau-chuyen-nguoi-dung.md) cung cấp bản ngắn để nói với giảng viên. Các yêu cầu/tiêu chí chi tiết trong SRS này là đầu mối đối chiếu; ghi nhận phản hồi của thầy rồi cập nhật phạm vi, không tự coi bản viết là phê duyệt.
