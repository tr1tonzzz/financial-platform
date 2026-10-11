# Kế hoạch nghiên cứu sâu theo góp ý giảng viên

Ngày ghi nhận: **11/10/2026**. Nguồn góp ý: người thực hiện thuật lại buổi trình bày trước; chưa biết ngày buổi trình bày. Trạng thái: **đã lưu góp ý, rà soát nền hiện có và lập kế hoạch; chưa hoàn thành nghiên cứu sâu, benchmark PaddleOCR hoặc đánh giá người dùng**.

## 1. Mục tiêu và đầu ra cần đạt

Trọng tâm: chuyển từ “tổng hợp BCTC và cổ tức” sang **giúp người đầu tư cổ tức đánh giá cơ sở của khoản thu nhập tiền mặt, nhận diện điều cần kiểm tra và so sánh các lựa chọn bằng bằng chứng**. Đây là định hướng nghiên cứu, chưa là tuyên bố hệ thống đã cải thiện lợi nhuận đầu tư.

| Góp ý | Câu hỏi phải giải quyết | Sản phẩm nghiên cứu | Điều kiện hoàn thành |
|---|---|---|---|
| PaddleOCR có thể tốt hơn | Có giảm lỗi số liệu và công sức hiệu chỉnh trên PDF Việt Nam không? | Protocol, bộ đáp án, kết quả đối chứng, quyết định công cụ | Cùng mẫu/thiết bị; đo trích đúng trường và thời gian; giữ lỗi và trường thiếu |
| Vì sao bỏ cổ tức bằng cổ phiếu? | Giới hạn đối tượng nghiên cứu thế nào và gây sai lệch gì? | Luận chứng phạm vi, ca phản ví dụ, quy tắc dữ liệu | Phân biệt dòng tiền nhận được với biến động cơ sở trên mỗi cổ phiếu |
| Chức năng chưa giúp đầu tư rõ ràng | Người dùng làm tác vụ gì tốt hơn sau phân tích? | 3–5 UC nhỏ, dữ liệu, công thức, giao diện dự kiến và thí nghiệm | Mỗi UC có quyết định, đầu vào, xử lý, đầu ra và cách chấm |
| Thuật ngữ chưa chuẩn | Tên chức năng có diễn tả đúng tác vụ nghiệp vụ không? | Từ điển và danh sách vị trí cần sửa | Thuật ngữ đúng ngữ cảnh; không chỉ đổi từ cho trang trọng |
| Đẩy nhanh tiến độ | Kết quả chạy được gần nhất là gì? | Một lát cắt chức năng và hồ sơ minh chứng | Có luồng dữ liệu thật → phân tích → tra soát; ghi rõ phần thủ công |

Kết thúc nghiên cứu cần có khuyến nghị chọn **1 UC ưu tiên triển khai, tối đa 2 UC tiếp theo**, không chỉ danh sách ý tưởng. Lý do chọn phải xét giá trị quyết định, khả năng có dữ liệu, rủi ro diễn giải và giờ thực hiện.

## 2. Nền hiện có và khoảng trống

**Bổ sung sau khảo sát GitHub 11/10/2026:** [hồ sơ 9 dự án](../research-github-dividend/README.md) đã có đọc mã, phản hồi người dùng và 10 UC ứng viên. Đây là kết quả nhánh khảo sát dự án tương tự; nghiên cứu ca thật G02/G03, benchmark OCR và đánh giá người dùng vẫn chưa hoàn thành.

- [SRS v3.1](22-srs-dac-ta-yeu-cau-phan-mem.md) đã mô tả UC03 trích/chuẩn hóa, UC05 vòng đời cổ tức, UC06 phân tích và tối thiểu một ca cầu nối CFO. Đặc tả không chứng minh đã có ứng dụng tương ứng.
- [Nghiên cứu giá trị sử dụng 05/10](reports/dot-01-tuan-01-02/co-so-hoc-thuat-va-gia-tri-su-dung.md) đã có cơ sở học thuật/nghề nghiệp. Cần chuyển thành tác vụ ra quyết định và kiểm chứng, không viết lại tổng quan.
- [Thực nghiệm OCR 03/10](../research-recent-data/02-thu-nghiem-pdf-ocr.md) ghi 10 trang chọn thủ công, hai báo cáo, 11/12 ứng viên sáu chỉ tiêu khớp ảnh; còn một trường không trích được. Không có holdout độc lập hoặc số đo thời gian hiệu chỉnh.
- Mã có thể tái sử dụng: [probe_ocr.cjs](../../scripts/research/probe_ocr.cjs), [crawler](../../scripts/research/crawl_official_reports.py) và [thư mục demo OCR VNM](../../exports/vnm-ocr-demo/). Demo VNM tải URL định sẵn; không gọi đó là discovery đầy đủ. Các tệp demo hiện chưa được Git theo dõi tại thời điểm rà soát; minh chứng công cụ ở [báo cáo thực nghiệm](reports/dot-01-tuan-01-02/thu-nghiem-cong-cu.md).
- Chưa thấy bằng chứng benchmark PaddleOCR hoặc thí nghiệm cải thiện chất lượng quyết định trong các hồ sơ đã rà soát. Chưa xác nhận ứng dụng phân tích hoàn chỉnh.

## 3. Nhánh ưu tiên: chức năng phục vụ người đầu tư cổ tức

### 3.1. Giả thuyết nhu cầu và phương pháp nghiên cứu

Đối tượng giả định: nhà đầu tư cá nhân tìm thu nhập cổ tức tiền mặt từ doanh nghiệp phi tài chính. Cần kiểm tra lại qua tác vụ/phỏng vấn; chưa coi đây là phân khúc đã được xác nhận.

Nghiên cứu theo chuỗi: **quyết định → câu hỏi → bằng chứng → phép phân tích → hành động tiếp theo**. Đọc tài liệu nghề nghiệp và nghiên cứu liên quan theo từng câu hỏi; khảo sát sản phẩm hiện hành để xem cách giải quyết và khoảng trống, không suy đối thủ thiếu tính năng chỉ vì không thấy trên trang giới thiệu. Lưu URL, ngày truy cập, đoạn/mục hỗ trợ và mức bằng chứng: toàn văn, abstract, tài liệu sản phẩm hay ca tự tính.

Phỏng vấn/tác vụ thử: mục tiêu 3–5 người có kinh nghiệm đọc BCTC/đầu tư cổ tức, nếu tuyển được. Hỏi họ kiểm tra gì trước một thông báo cổ tức cao, từng nhầm gì và cần chứng cứ nào. Chưa liên hệ ai trong kế hoạch này. Nếu chưa có người, dùng ca chuyên môn được rà soát và ghi giới hạn, không gọi là xác nhận nhu cầu.

### 3.2. Các UC ứng viên cần nghiên cứu

Mã R-UC dưới đây là mã nghiên cứu, **không thay các mã UC trong SRS**. Đầu ra là hồ sơ hỗ trợ đánh giá; mức cổ tức cao không tự tạo thành lựa chọn đầu tư tốt.

| UC / quyết định người dùng | Đầu vào | Xử lý | Đầu ra cần thiết | Quan hệ phạm vi |
|---|---|---|---|---|
| R-UC01: Có nên tiếp tục thẩm định doanh nghiệp cho thu nhập cổ tức? | LNST, CFO, lịch sử DPS, coverage, scope/kỳ/version | Đối chiếu xu hướng lợi nhuận–tạo tiền–cổ tức; tìm năm lệch chiều; mở các dòng cầu nối liên quan | Hồ sơ có tín hiệu, lý do, trang nguồn và dữ kiện còn thiếu | Đào sâu UC06, FR25–29/31–32 và UC-E01/02; ứng viên làm trước |
| R-UC02: Cổ tức có được hỗ trợ bởi nguồn lực và nhu cầu sử dụng tiền? | Thêm chi đầu tư, tiền, vay/nợ đến hạn, báo cáo riêng và chứng cứ tổng cổ tức phù hợp | Phân tích khả năng bao phủ có điều kiện; đọc vốn lưu động và chi đầu tư; đối chiếu chủ thể phân phối | Bảng nguồn lực–nhu cầu tiền; vấn đề cần tra soát; kịch bản có giả định | Dữ liệu mới; lập đề xuất thay đổi nếu chọn |
| R-UC03: Cổ tức giảm hay chỉ thay đổi số lượng cổ phiếu? | DPS gốc, sự kiện cổ phiếu, tỷ lệ/ngày hiệu lực và lịch sử số lượng cổ phiếu | Kiểm tra cơ sở so sánh; lưu gốc và điều chỉnh theo quy tắc được kiểm chứng | Chuỗi DPS có cờ so sánh được; nguyên nhân khác biệt và bằng chứng | Nhánh bắt buộc nghiên cứu để bảo vệ luận chứng phạm vi; triển khai theo gate |
| R-UC04: Doanh nghiệp nào cần đọc trước trong danh sách theo dõi? | Hồ sơ cùng ngành/scope/kỳ/as_of, độ đầy đủ và tiêu chí người dùng | So sánh từng chiều; giải thích lý do đưa vào danh sách đọc sâu | Bảng so sánh kèm lý do, thiếu dữ liệu và nguồn; chưa dùng điểm tổng tùy ý | Tái dùng phân tích hiện có; tiêu chí/xếp hạng mới cần đánh giá |
| R-UC05: Khoản thu dự kiến thuộc năm nào, có thay lịch hoặc quyền không? | Notice/components, năm lợi nhuận, ngày đăng ký cuối cùng/lịch trả, bản sửa | Tách phần cổ tức đa năm; ghép vòng đời; tra soát trạng thái | Lịch dự kiến và bảng cổ tức theo năm lợi nhuận; phân biệt công bố/dự kiến/thực chi | Làm cụ thể UC05; không suy ngày dự kiến thành xác nhận đã nhận tiền |

R-UC01 có thể hoàn thành với ít dữ liệu bổ sung nhất, nhưng chỉ giúp **đặt câu hỏi thẩm định**. Muốn đánh giá khả năng duy trì cổ tức sâu hơn cần R-UC02; phải đo khả năng thu được dữ liệu trước khi cam kết.

### 3.3. Các phép phân tích và bẫy cần giải quyết

1. **Tính đều đặn của cổ tức:** số năm có cổ tức, biến động DPS và trạng thái năm chưa đủ thông báo. Chỉ ba năm là lịch sử ngắn; thiếu thông báo không phải không trả. Tách khoản thường xuyên và bất thường nếu chứng cứ cho phép.
2. **Lợi nhuận và tạo tiền:** CFO/LNST chỉ tính khi mẫu số có ý nghĩa; kèm số tuyệt đối và điều chỉnh vốn lưu động. CFO hợp nhất không tự là tiền công ty mẹ có quyền phân phối. Cầu nối giải thích đóng góp số học, không khẳng định nhân quả.
3. **Tỷ lệ chi trả:** nghiên cứu tổng cổ tức tiền mặt thuộc năm lợi nhuận / lợi nhuận phù hợp với cổ đông và chủ thể phân phối. DPS/EPS chỉ sử dụng sau khi kiểm tra cơ sở cổ phiếu, kỳ và EPS phù hợp; không nhân DPS với số cổ phiếu cuối năm tùy tiện để dựng tổng cổ tức.
4. **Bao phủ bằng tiền:** tách cổ tức công bố theo năm lợi nhuận khỏi tiền cổ tức thực chi trong năm. CFO / tiền cổ tức thực chi cùng chủ thể/kỳ là đối chiếu dòng tiền; không đồng nhất với khả năng bao phủ bằng dòng tiền tự do. Dòng “cổ tức, lợi nhuận đã trả” có thể gồm khoản phân phối khác, phải đọc thuyết minh.
5. **Chi đầu tư và nợ:** CFO − chi đầu tư tiền mặt là thước đo phải định nghĩa rõ, không mặc định là FCFE. Vay ròng, phân loại lãi vay, giao dịch đầu tư và nhu cầu duy trì/mở rộng phải được kiểm tra. Chưa có dữ liệu thì hiển thị “chưa đủ cơ sở đánh giá”.
6. **Tỷ suất cổ tức và tổng mức sinh lời:** cần giá, ngày định giá, sự kiện doanh nghiệp và giả định tái đầu tư/chi phí. Không gọi tỷ lệ cổ tức trên mệnh giá là tỷ suất cổ tức; đây là hướng mở rộng sau gate dữ liệu giá.
7. **Kịch bản:** nếu thử giảm CFO/tăng chi đầu tư thì ghi giả định người dùng chọn, không gọi là dự báo xác suất cắt cổ tức. Chưa có cơ sở để chọn ngưỡng “an toàn” chung hoặc tự xây điểm chất lượng đầu tư.

Cơ sở nghề nghiệp ban đầu: CFA đưa bao phủ cổ tức theo lợi nhuận/dòng tiền tự do và khả năng duy trì vào nội dung phân tích. Đây là căn cứ chọn câu hỏi, không chứng minh hiệu quả sản phẩm. [CFA, Analysis of Dividends and Share Repurchases](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/analysis-of-dividends-and-share-repurchases). Phân biệt CFO, FCFF và FCFE theo [CFA, Free Cash Flow Valuation](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/free-cash-flow-valuation).

### 3.4. Thiết kế kiểm chứng chất lượng quyết định

So sánh A: đọc PDF/thông báo và bảng tổng hợp đơn thuần; B: cùng dữ liệu với hồ sơ phân tích và tra soát của UC. Chọn ca đủ dữ liệu, ca thiếu, ca lợi nhuận/CFO lệch chiều, ca nhiều năm cổ tức và ca có biến động cổ phiếu; không chỉ chọn ví dụ thuận lợi.

- Đáp án chuẩn gồm kết luận được phép, dữ kiện bắt buộc phải kiểm tra, lỗi diễn giải và nguồn. Nhờ người có chuyên môn rà soát nếu có; nếu chỉ người thực hiện tự chấm, ghi rõ tính độc lập còn hạn chế.
- Dùng hai bộ ca tương đương và đổi thứ tự A/B giữa người thử để giảm hiệu ứng nhớ/học. Không cho một người đọc đúng cùng ca hai lần rồi quy mọi cải thiện cho hệ thống.
- Chấm tỷ lệ nhận diện đúng vấn đề, bỏ sót dữ kiện quan trọng, kết luận sai do năm/scope/số cổ phiếu, khả năng viện dẫn chứng cứ và thời gian hoàn thành. Mức tự tin chỉ là số đo phụ; tự tin cao hơn không mặc định tốt hơn.
- Báo từng ca và từng người, cùng lỗi còn lại. Mẫu 3–5 người chỉ là đánh giá thử; không suy hiệu quả toàn thị trường.
- Tiêu chí chọn UC: chất lượng trả lời tăng hoặc sai sót trọng yếu giảm, có lý do từ chứng cứ; không chỉ nhanh hơn. Mức cải thiện mục tiêu phải chốt trước thử sau khi biết baseline, không chọn sau khi thấy kết quả.
- “Tăng lợi nhuận đầu tư” là giả thuyết dài hạn riêng. Nếu sau này backtest phải có dữ liệu tại thời điểm quyết định, tránh nhìn trước/sống sót, xử lý sự kiện, chi phí và benchmark; không dùng dữ liệu hiện tại thay lịch sử để chứng minh hiệu quả.

## 4. Cổ tức bằng cổ phiếu: luận chứng và phương án xử lý

Luận chứng khởi đầu: đề tài tập trung dòng tiền cổ tức nên cổ tức bằng cổ phiếu không được cộng vào tiền cổ tức nhận được. CFA phân biệt phân phối tiền mặt với stock dividends/splits. [Nguồn nghề nghiệp](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/analysis-of-dividends-and-share-repurchases). Việc giới hạn chỉ tiêu tiền mặt không đủ để kết luận các sự kiện thay đổi số cổ phiếu có thể bị bỏ khỏi dữ liệu.

**Phản ví dụ giả lập để thiết kế test, chưa là ca doanh nghiệp thật:** nhà đầu tư có 100 cổ phiếu; nhận cổ tức bằng cổ phiếu 20%, sau đó nắm 120 cổ phiếu. Nếu DPS tiền mặt giảm từ 1.000 xuống 900 đồng, nhìn DPS gốc sẽ thấy giảm 10%; giả sử toàn bộ 120 cổ phiếu đều có quyền nhận ở lần sau thì tổng khoản nhận tăng từ 100.000 lên 108.000 đồng. Kết quả phụ thuộc trình tự/ngày quyền, làm tròn và quyền hưởng thực tế; ví dụ chưa tính giá, thuế hoặc phí.

Trong trường hợp tỷ lệ 20% đơn giản và đã xác định mốc hiệu lực, DPS lịch sử 1.000 đồng trên cơ sở cổ phiếu cũ tương đương khoảng 833,33 đồng trên cơ sở mới. Đây là phép quy đổi thiết kế cho ca đơn giản, không phải quy tắc chung cho phát hành quyền mua, thưởng cổ phiếu, ESOP, mua cổ phiếu quỹ hoặc mọi sự kiện doanh nghiệp. [Investor.gov mô tả tác động chia tách tới số cổ phiếu và DPS](https://www.investor.gov/introduction-investing/investing-basics/glossary/stock-split); nguồn này giải thích khái niệm, không thay quy tắc Việt Nam. [IAS 33](https://www.ifrs.org/issued-standards/list-of-standards/ias-33-earnings-per-share/) là đầu mối nghiên cứu EPS, không tự áp dụng cơ chế EPS cho DPS.

Ba phương án cần đánh giá bằng ca thật:

| Phương án | Lợi ích | Giới hạn | Quyết định nghiên cứu |
|---|---|---|---|
| Chỉ tiền mặt, không theo dõi sự kiện cổ phiếu | Ít công sức | Không bảo đảm so sánh DPS/EPS hay tiền nhận trên vị thế giữ lâu dài | Chỉ chấp nhận nếu đánh dấu không so sánh được/loại ca và công khai giới hạn |
| Tiền mặt là chỉ tiêu chính; lưu sự kiện cổ phiếu tối thiểu | Giữ trọng tâm, kiểm soát sai lệch | Cần nguồn tỷ lệ/ngày/trạng thái và quy tắc điều chỉnh | Hướng ưu tiên để kiểm chứng tính khả thi |
| Phân tích đầy đủ tổng mức sinh lời | Trả lời câu hỏi đầu tư rộng hơn | Cần giá, quyền, tái đầu tư, chi phí, nhiều dữ liệu mới | Nghiên cứu sau; chưa tích hợp vào MVP |

Việc tiếp theo: tìm một ca thật có cổ tức bằng cổ phiếu và tiền mặt; đọc nghị quyết/thông báo của doanh nghiệp/VSDC; lập timeline quyền và lượng cổ phiếu; so kết luận dùng DPS gốc với cơ sở điều chỉnh. Ghi thêm các sự kiện không phải cổ tức để không nhầm bản chất. Hồ sơ cần nêu rõ bỏ phần nào, giữ dữ liệu gì, câu hỏi nào vẫn trả lời được và câu hỏi nào phải từ chối.

## 5. Kiểm chứng PaddleOCR so với Tesseract

Tài liệu chính thức có mô hình nhận dạng đa ngôn ngữ hỗ trợ tiếng Việt (`vi`, nhóm Latin). Điều đó xác nhận có ứng viên kỹ thuật, chưa xác nhận đọc BCTC của project tốt hơn. [PaddleOCR multilingual](https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/version3.x/algorithm/PP-OCRv5/PP-OCRv5_multi_languages.en.md). Tesseract có hướng dẫn về chất lượng ảnh và phân đoạn trang; baseline cần được cấu hình hợp lý. [Tesseract ImproveQuality](https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html).

Protocol dự kiến:

1. Tái sử dụng 10 trang đã thử để kiểm tra cài đặt và phát triển; **không gọi chúng là holdout mới**. Chọn thêm 12–20 trang từ tài liệu chưa dùng chỉnh quy tắc, tách theo tài liệu để tránh hai trang cùng mẫu rơi vào cả hai nhóm. Bao gồm bảng nhiều cột, âm/ngoặc, dấu phân cách, đơn vị và dấu/chữ ký nếu có.
2. Lập manifest PDF/hash/trang/DPI và đáp án kiểm bằng ảnh: kỳ, scope, đơn vị, nhãn/mã dòng, cột và số đúng. Giữ cùng ảnh đầu vào; thử 220/300 DPI chỉ trên nhóm phát triển rồi khóa cấu hình trước holdout.
3. So Tesseract.js 7.0.0 hiện có với PaddleOCR nhận dạng Việt phù hợp. Ghi phiên bản wrapper/engine, model/hash, CPU/GPU, tham số, tiền xử lý, RAM và thời gian tải/khởi tạo riêng. Kết luận về cấu hình này; chưa suy mọi bản Tesseract đều kém hơn.
4. Hai phép đo tách biệt: (a) OCR số/nhãn và tọa độ so đáp án; (b) toàn luồng trích trường với cùng bộ chuẩn hóa/định nghĩa trường. Nếu đổi cả parser hoặc thêm bộ phân tích layout/bảng, báo thành thí nghiệm riêng, không quy toàn bộ lợi ích cho OCR.
5. Chỉ tiêu chính: số trường trích đúng / **toàn bộ trường kỳ vọng**; chính xác giá trị+kỳ+cột+đơn vị; lỗi âm, lệch cột và thiếu số. Chỉ tiêu phụ: CER, thời gian/trang, thời gian hiệu chỉnh, RAM và lỗi cài/chạy. Confidence không phải độ chính xác thực đo; có thể đo CER trên nhóm nhãn được gán đáp án đầy đủ để giảm công sức.
6. Chấm cặp trên cùng trang/trường, báo kết quả theo từng loại bảng/tài liệu và tổng; không xem các trường cùng PDF là mẫu độc lập khi diễn giải độ tin cậy. Nếu hiệu chỉnh do cùng người làm, đổi thứ tự và ẩn tên engine khi khả thi.
7. Chỉ đề nghị thay công cụ khi giảm lỗi nghiệp vụ hoặc công sức hiệu chỉnh, không tăng lỗi trọng yếu, và chạy ổn trên máy mục tiêu. Nếu lợi ích chưa rõ, giữ baseline và thử thêm mẫu theo lỗi thực tế. PDF có lớp chữ dùng được vẫn ưu tiên trích trực tiếp.

Sản phẩm: manifest, gold, cấu hình, raw output, bảng lỗi, số đo và ghi chú quyết định. Chuẩn bị và chạy thử 2–3 trang là mốc đầu; benchmark đầy đủ là việc tiếp theo, không cam kết xong chỉ trong thời gian khảo sát.

## 6. Thuật ngữ nghiệp vụ

| Cách nói hiện tại | Cách dùng phù hợp | Khi nào sử dụng |
|---|---|---|
| Mở được nguồn | Truy xuất chứng từ nguồn / xem tài liệu gốc | Chỉ mở đúng tài liệu/trang chứa số |
| Mở nguồn để kiểm tra | Tra soát số liệu với chứng từ nguồn | Có kiểm tra sai lệch, xác minh kỳ/cột/đơn vị và ghi kết quả |
| So số | Đối chiếu số liệu | So hai giá trị hoặc kiểm quan hệ số học |
| Lấy dữ liệu | Thu thập / trích xuất dữ liệu | Thu tài liệu khác trích trường trong tài liệu |
| Gom cổ tức | Tổng hợp cổ tức tiền mặt theo năm lợi nhuận | Đã tách thành phần và loại trùng/sửa/hủy đúng |
| Cổ tức 20% | Tỷ lệ cổ tức tiền mặt trên mệnh giá hoặc tỷ lệ cổ tức bằng cổ phiếu | Phải nói loại quyền và cơ sở tỷ lệ |
| Tiền cổ tức đã nhận | Cổ tức công bố / lịch thanh toán dự kiến / thực chi có chứng cứ | Chọn theo bằng chứng, không gọi dự kiến là thực nhận |
| Cổ tức tốt/an toàn | Cơ sở đánh giá khả năng duy trì cổ tức; vấn đề cần thẩm định | Phân tích có điều kiện, tránh nhãn không có chuẩn đánh giá |
| Giải thích CFO giảm | Phân rã đóng góp vào biến động CFO | Phân rã số học; kết luận nguyên nhân kinh tế cần chứng cứ thêm |

Rà soát trước báo cáo, slide và nhãn giao diện đang dùng. Không sửa toàn bộ hồ sơ lịch sử hoặc thay “mở nguồn” bằng “tra soát” khi chức năng chỉ mở PDF.

## 7. Nhịp thực hiện để tăng tốc

Đề xuất đợt đầu **12–18/10/2026**, dự toán **15 giờ**, chưa xác nhận quỹ giờ thực tế hoặc ngày hẹn với giảng viên. Đây là kế hoạch nghiên cứu ngắn hạn bổ sung backlog hiện hành, không thay lịch nghiệm thu 13 tuần; các giờ chuyển từ việc tổng quan/soạn lại tài liệu phải được ghi vào nhật ký, không mặc định có thêm quỹ giờ.

| Mốc dự kiến | Việc | Giờ | Đầu ra kiểm được |
|---|---|---:|---|
| 12/10 | Rà UC hiện tại, chọn câu hỏi ưu tiên và nguồn theo câu hỏi | 2 | Ma trận dữ liệu đã có/thiếu; đề cương R-UC01/02 |
| 13–14/10 | Nghiên cứu nghiệp vụ và tính các ca lợi nhuận–CFO–cổ tức | 4 | 2 ca đối chiếu, công thức/nguồn và giới hạn; chưa gắn nhãn hiệu quả đầu tư |
| 15/10 | Nghiên cứu ca cổ tức bằng cổ phiếu; kiểm cơ sở DPS | 3 | 1 ca thật hoặc ghi rõ thiếu nguồn; đề nghị phương án phạm vi |
| 16/10 | Chuẩn bị OCR đối chứng; cài/cấu hình và chạy thử 2–3 trang | 3 | Nhật ký khả thi, manifest ban đầu và cấu hình; không là benchmark cuối |
| 17/10 | Chốt UC ưu tiên và protocol tác vụ A/B | 2 | Đặc tả UC nhỏ, tiêu chí, rubric và dữ liệu còn thiếu |
| 18/10 | Tổng hợp quyết định nghiên cứu và nội dung trao đổi | 1 | 1 trang đề nghị, thuật ngữ thống nhất, backlog triển khai |

Nếu chỉ có 10–12 giờ, ưu tiên 8 giờ cho chức năng, 3 giờ cho cổ tức cổ phiếu, 1 giờ cho protocol OCR; lùi chạy Paddle sang đợt tiếp theo và ghi phần chưa làm. Không giảm chất lượng bằng cách biến nghiên cứu chưa chạy thành kết quả.

Đợt kế tiếp dự kiến 19–25/10: dựng lát cắt R-UC01 bằng dữ liệu đã duyệt, hoàn thành benchmark OCR theo thời gian thực đo và thực hiện tác vụ A/B khi có người thử. Ước lượng lại cuối đợt đầu; không coi đây là cam kết đã có người dùng hoặc mọi tính năng hoàn thành trong một tuần.

Gate: cuối ngày nghiên cứu thứ hai phải biết dữ liệu nào đủ để làm UC01; cuối đợt đầu phải chọn được UC và có đề nghị giữ/giảm/mở rộng dữ liệu. Nếu R-UC02 thiếu nguồn, tiếp tục làm UC01 và ghi rõ câu hỏi khả năng duy trì chưa giải quyết hết. Không tăng số công ty đồng thời với tăng chiều sâu.

## 8. Checklist bàn giao và quyết định phạm vi

- [x] Lưu nguyên ý góp ý và cập nhật hướng dẫn project.
- [x] Rà soát tài liệu/mã hiện có và kiểm tra nguồn chính thức ban đầu.
- [x] Lập kế hoạch có UC, phép kiểm chứng, đầu ra, giờ dự toán và gate.
- [ ] Hoàn thành hồ sơ nghiên cứu chức năng và lựa chọn UC bằng chứng cứ.
- [ ] Hoàn thành ca thật cổ tức bằng cổ phiếu và đề nghị cách kiểm soát DPS.
- [ ] Hoàn thành benchmark PaddleOCR–Tesseract trên holdout.
- [ ] Chạy lát cắt chức năng với dữ liệu thật và lưu minh chứng.
- [ ] Thử tác vụ người dùng hoặc ghi rõ vì sao chưa làm được.
- [ ] Lập change record cho dữ liệu/chức năng vượt SRS; đồng bộ tài liệu được chọn triển khai.

Mỗi hồ sơ tiếp theo ghi: câu hỏi, nguồn/phần đã đọc, kết quả ca, giả thuyết còn mở, quyết định đề nghị và thời gian thực tế. Không tick việc chỉ vì đã viết kế hoạch. Khi trao đổi với thầy: nêu một vấn đề đầu tư cụ thể → chạy một UC → mở chứng cứ → trình bày giới hạn → đề nghị bước tiếp theo.

## Cập nhật 11/10/2026 — nghiên cứu triển khai và UC lớn

[Bộ ba chức năng](../research-dividend-functions/README.md) đã có đặc tả G02/G03/G01, kiến trúc, dự toán, ca DHG/FPT và 20 tests prototype. [SRS3.2](22-srs-dac-ta-yeu-cau-phan-mem.md) nhóm lại 5 BUC, giữ UC cũ là phân rã và thêm12 D/12 TC-D. GitHub thêm3 repo, tổng12. Tiếp theo triển khai lát dọc nguồn→duyệt→metric→dossier; chốt quỹ giờ/pilot trước nghiệm thu. Chưa có application acceptance, gold độc lập hay OCR đối chứng. Kế hoạch167 giờ cũ chưa bao gồm64–98 giờ bổ sung dự toán.
