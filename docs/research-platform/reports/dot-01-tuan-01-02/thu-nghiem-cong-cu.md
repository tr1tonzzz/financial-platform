# Thử nghiệm nhỏ: crawler → PDF → OCR → chỉ tiêu Vinamilk quý I/2026

Ngày chạy: **06/10/2026**. **Bổ sung cùng ngày:** cầu nối, ghép nguồn cổ tức và ý nghĩa đối với đề tài. Phụ lục của [báo cáo 1](bao-cao-01.md), đổi mẫu thử sang **BCTC hợp nhất quý I/2026 của Vinamilk (VNM)** theo yêu cầu. Đã chạy công cụ thực; đây là mẫu phát triển nhỏ, chưa là nghiệm thu hay đánh giá độ chính xác trên tập độc lập. Phần phân tích chính và [phụ lục phân tích](vi-du-phan-tich-vnm.md) nay dùng cùng mẫu Vinamilk này; cầu nối thành phần được đọc thủ công và kiểm tổng riêng.

## 1. Nguồn và câu hỏi thử nghiệm

Có thể tìm đúng báo cáo từ danh mục chính thức, tải PDF, trích LNST/CFO/tiền chi trả cổ tức và trả lời một câu hỏi phân tích sơ bộ không? Phần bổ sung còn thử tổ chức cầu nối và ghép một số thông báo cổ tức để kiểm việc liên kết dữ liệu giúp trả lời thêm câu hỏi nào; các bước đọc thành phần/thông báo hiện làm thủ công, chưa nằm trong crawler/OCR tự động.

- [Danh mục BCTC Vinamilk](https://www.vinamilk.com.vn/investor/reports/financial): liên kết ghi ngày **29/04/2026**, kỳ Q1/2026, báo cáo hợp nhất.
- [PDF được liên kết từ danh mục](https://d8um25gjecm9v.cloudfront.net/cms/20260429_VNM_BCTC_DA_SOAT_XET_Q1_2026_HOP_NHAT_VN_d44326741a.pdf): Công ty CP Sữa Việt Nam và các công ty con; **71 trang**, đơn vị **VND**.
- Kỳ hiện tại: ba tháng kết thúc **31/03/2026**; cột so sánh: ba tháng kết thúc **31/03/2025**, ghi **đã phân loại lại**. Không coi cột này là bản Q1/2025 nguyên trạng tại thời điểm công bố năm 2025.
- Trạng thái kiểm tra từ tài liệu: **đã soát xét**, báo cáo KPMG số **25-01-00430-26-4**, ngày 29/04/2026, trang PDF 5–6. Không suy từ nhãn danh mục “Đã soát xét/kiểm toán” rằng đây là báo cáo kiểm toán năm.
- Ba trang thử OCR: PDF **12/13/14**, tương ứng trang in **11/12/13**. Chọn tổng LNST hợp nhất; không lấy LNST thuộc chủ sở hữu công ty mẹ để ghép với CFO hợp nhất.

Mẫu quý I/2026 phục vụ thử công cụ và ví dụ phân tích sơ bộ, **không đổi phạm vi pilot 2023–2025**. Không thường niên hóa số quý hoặc ghép chuỗi quý với năm. Bảng tham chiếu [VNM Q1/2026](../../../research-profit-cash-dividend/evidence/case-vnm-q1-2026.json) được đọc thủ công từ ảnh trang gốc bởi cùng người thực hiện, chưa có người kiểm độc lập.

## 2. Công cụ đã chạy

| Bước | Công cụ | Kết quả thực |
|---|---|---|
| Tìm nguồn | Python `urllib` + `lxml`, adapter nhỏ dùng lại client crawler trong repo | Một trang danh mục HTTP 200, **9 liên kết PDF ứng viên** trong HTML trả về; chọn đúng một báo cáo hợp nhất Q1/2026 |
| Tải và lưu dấu vết | HTTPS, kiểm `%PDF-`, SHA-256, lưu HTML/PDF/log | PDF HTTP 200, **3.839.441 byte**, lưu theo hash; chưa thử tải có điều kiện/304 với mẫu VNM |
| Trích lớp chữ | `pypdf` 6.10.0 | **71/71 trang trả 0 ký tự**; chuyển sang OCR cho ba trang chọn trước |
| Render | Poppler `pdftoppm`, 220 DPI | Render thành công trang PDF 12–14 |
| OCR | Tesseract.js 7.0.0, `vie` + `eng` | Trang 12: 993 ký tự, 1,523 giây; trang 13: 1.835 ký tự, 2,335 giây; trang 14: 1.394 ký tự, 2,169 giây |
| Trích ứng viên | Python tìm nhãn dòng, đọc hai cột số có dấu chấm và âm trong ngoặc | **6 đúng, 0 sai, 0 thiếu** trên sáu ô được chọn, so với tham chiếu đọc trang gốc |
| Tính sau đối chiếu | Python | LNST +54,87%; CFO tăng tuyệt đối 393,514 tỷ đồng, đổi từ âm sang dương; CFO/LNST Q1/2026 ≈ 0,110 lần |

Thời gian nhận dạng ba trang tổng **6,026 giây**, khởi tạo worker **1,044 giây**; chưa gồm tải, render và công sức duyệt. Confidence trang 12/13/14 là **88/91/87**, không phải tỷ lệ số đúng.

Crawler giới hạn **một trang danh mục và một PDF**, chỉ hai host được cho phép, tối thiểu một giây giữa request cùng host, giữ xác minh TLS, không gọi API hay duyệt toàn website. Website chính có robots cho phép đường dẫn danh mục. CDN trả **403 cho `robots.txt`**, vì vậy lần chạy mặc định dừng trước tải PDF; log lần này được giữ riêng. Lần thử tiếp dùng `--allow-unknown-robots` cho một tệp công khai được danh mục liên kết và tải thành công. Đây là trạng thái robots **chưa xác định**, không phải đã xác nhận cho phép trên CDN; tùy chọn không ghi đè quy tắc Disallow đã đọc được. Công cụ web cũng gặp 403, trong khi client Python nhận 200 ở danh mục và PDF: khả năng truy cập phụ thuộc client tại thời điểm chạy.

## 3. Số trích được và nhận xét minh họa

| Chỉ tiêu, VND | Q1/2026 | Q1/2025, đã phân loại lại | Vị trí | Đối chiếu |
|---|---:|---:|---|---|
| Tổng LNST hợp nhất | 2.458.221.002.532 | 1.587.273.268.054 | PDF 12, trang in 11 | Cả hai ô khớp |
| CFO | 269.326.997.516 | −124.187.023.735 | PDF 13, trang in 12, mã 20 | Cả hai ô khớp |
| Tiền chi trả cổ tức, dòng tiền âm | −55.837.540 | −1.044.977.722.500 | PDF 14, trang in 13, mã 36 | Cả hai ô khớp |

**Câu hỏi người dùng: lợi nhuận tăng có đi cùng dòng tiền kinh doanh tương ứng không?** LNST tăng **54,87%**, CFO đổi từ **−124,187 tỷ** sang **269,327 tỷ**. Tuy cải thiện, CFO/LNST chỉ khoảng **0,110 lần**, so với **−0,078 lần** ở cột so sánh. Vì CFO kỳ trước âm, dùng chênh lệch tuyệt đối **393,514 tỷ đồng**, không trình bày tăng trưởng CFO theo phần trăm dễ gây hiểu nhầm.

Nhận xét này dẫn người đọc tới báo cáo lưu chuyển tiền tệ thay vì chỉ nhìn LNST. Trang PDF 13 còn cho thấy chi thuế TNDN khoảng 1.579,997 tỷ đồng và biến động tồn kho/tài sản sinh học âm khoảng 1.036,623 tỷ đồng ở Q1/2026. Đây là số đọc lại thủ công để gợi ý khoản mục cần xem tiếp, **chưa phải cầu nối tự động hoặc kết luận nguyên nhân hoàn chỉnh**. Dòng tiền quý có thể chịu thời điểm thanh toán và mùa vụ; tỷ lệ thấp ở một quý chưa đủ gắn nhãn chất lượng lợi nhuận kém.

**Câu hỏi người dùng: lợi nhuận, dòng tiền và cổ tức có thể được đặt cạnh nhau không?** Có thể hiển thị cùng kỳ số chi trả cổ tức rất nhỏ năm 2026 so với cột 2025 để minh họa nhu cầu kiểm lịch trả và năm lợi nhuận. Mã 36 là **tiền đã chi trong kỳ của phạm vi hợp nhất**, không phải mức cổ tức công bố cho năm lợi nhuận 2026, DPS hay cam kết duy trì cổ tức. Đã bổ sung đối chiếu một số thông báo VSDC và thuyết minh ở mục 3.2 dưới đây; vẫn chưa xác định khoản chi 55.837.540 VND thuộc đợt/năm lợi nhuận nào hoặc giải thích đầy đủ chênh lệch thực chi. Không tính tỷ lệ CFO/chi cổ tức quý để suy khả năng chi trả bền vững khi mẫu số Q1/2026 quá nhỏ.

### 3.1. Bổ sung cầu nối: dữ liệu trích được có giúp giải thích CFO không?

Các dòng thành phần được đọc lại từ PDF 13/trang in 12, lưu vào `manual_bridge` của [hồ sơ VNM](../../../research-profit-cash-dividend/evidence/case-vnm-q1-2026.json). Sau đó cộng/kiểm bằng Python từ số VND gốc; không mô tả đây là cầu nối tự động từ OCR. Chi tiết từng dòng ở [phụ lục phân tích](vi-du-phan-tich-vnm.md).

| Thành phần, tỷ đồng | Q1/2025 — đã phân loại lại | Q1/2026 | Đóng góp vào ΔCFO |
|---|---:|---:|---:|
| LNTT, điểm đầu | 1.951,296 | 3.014,396 | +1.063,100 |
| Điều chỉnh 02–06 | 312,160 | 322,517 | +10,356 |
| Biến động vốn lưu động 09–12 | −985,146 | −962,842 | +22,304 |
| Chi phí đi vay đã trả, thuế, chi khác 14/15/17 | −1.402,497 | −2.104,744 | −702,246 |
| **CFO** | **−124,187** | **269,327** | **+393,514** |

Tổng khớp CFO cả hai quý, **residual = 0 VND**. Dòng 08 chỉ kiểm tổng trung gian, không cộng lại; hai dòng mã 02 và hai dòng mã 05 có nhãn khác nhau đều được giữ. Tổng các số làm tròn có thể lệch 0,001 tỷ; phép kiểm dùng VND gốc.

Tiền thuế TNDN đã nộp đóng góp **−648,134 tỷ** vào ΔCFO, là một phần bù trừ đáng kể mức tăng LNTT. Nhóm vốn lưu động cải thiện ròng **22,304 tỷ**, dù riêng phải thu đóng góp âm. Người đọc có thể xác định khoản mục cần xem tiếp thay vì chỉ nhận tỷ số 0,110 lần. Đây là **đóng góp số học**, chưa chứng minh nguyên nhân kinh doanh; tiền thuế nộp không đồng nhất chi phí thuế.

### 3.2. Bổ sung ghép dữ liệu cổ tức: vì sao phải thu thập ngoài BCTC?

Ba thông báo được tìm/đọc thủ công từ VSDC và tách thành phần vào `dividend_context` của hồ sơ VNM. Thuyết minh V.23 được đọc từ ảnh gốc PDF 60/trang in 59. Các bước này **không nằm trong số trang OCR hoặc ngân sách crawler BCTC ở mục 2**, chưa là thử crawler lịch sử cổ tức.

| Nguồn | Năm lợi nhuận và mức theo cổ phiếu | Lịch thanh toán | Kết quả đối chiếu |
|---|---|---|---|
| [VSDC 10/12/2024](https://vsdc.vn/vi/ad/177392) | Tạm ứng đợt 2 năm **2024**, 500 đồng | **28/02/2025**, thuộc Q1/2025 | Xác nhận một sự kiện có năm lợi nhuận khác năm thanh toán; ứng viên liên quan chi Q1/2025, chưa xác nhận toàn bộ dòng chi hợp nhất chỉ thuộc đợt này |
| [VSDC 02/10/2025](https://vsdc.vn/vi/ad1/187729) | **2024: 350 đồng**; **2025: 2.500 đồng** | **24/10/2025**, ngoài Q1/2026 | Tách hai thành phần, không gán toàn bộ 2.850 đồng cho năm 2025 hoặc chi Q1/2026 |
| [VSDC 17/06/2026](https://vsdc.vn/vi/ad/197038) | Phần còn lại năm **2025**, 1.850 đồng | **17/07/2026**, ngoài Q1/2026 | Bổ sung bối cảnh hồi cứu; thông báo công bố sau kỳ, không chứng minh đã chi trong Q1 |

[Thuyết minh V.23](https://d8um25gjecm9v.cloudfront.net/cms/20260429_VNM_BCTC_DA_SOAT_XET_Q1_2026_HOP_NHAT_VN_d44326741a.pdf#page=60) ghi ĐHĐCĐ ngày **22/04/2026** phê duyệt cổ tức năm 2025 **4.350 đồng/cổ phiếu**. Cộng đúng hai thành phần thuộc 2025: `2.500 + 1.850 = 4.350`, khớp mức phê duyệt. Nếu cộng cả phần 350 đồng của năm 2024, tổng sai thành **4.700 đồng/cổ phiếu**. Phép cộng được kiểm từ hồ sơ JSON; khớp mức phê duyệt chưa chứng minh lịch sử đã đầy đủ hoặc các khoản đã thực trả.

Như vậy, **chi Q1/2026 nhỏ không đủ kết luận giảm cổ tức năm 2025**: dòng tiền trong kỳ và mức theo năm lợi nhuận trả lời hai câu hỏi khác nhau. Chưa ghép được khoản chi **55.837.540 VND** vào sự kiện cụ thể; trạng thái được giữ là chưa xác định, không suy thành không có chính sách cổ tức hoặc gán vào năm lợi nhuận 2026.

Mốc phê duyệt 22/04/2026 sau cuối quý, dù được trình bày trong báo cáo phát hành 29/04/2026. Thông báo tháng 6 còn muộn hơn. Đây là đối chiếu hồi cứu tại **06/10/2026**; phân tích thông tin có sẵn ngày 31/03/2026 phải loại nguồn công bố sau mốc đó. Lịch trả là kế hoạch, BCLCTT là chi gộp; chưa có chứng từ đối soát từng giao dịch, và phạm vi hợp nhất không tự đồng nhất với quyền cổ tức công ty mẹ.

### 3.3. Kết quả phục vụ câu hỏi người dùng và tính cần thiết của đề tài

| Câu hỏi | Chỉ đọc một BCTC | Đầu ra dữ liệu liên kết cần có | Minh chứng ở thử nghiệm |
|---|---|---|---|
| Lợi nhuận tăng có đi cùng tạo tiền? | Có thể tự đọc hai bảng và tính | Chỉ tiêu đúng kỳ/scope, tỷ số, công thức, nguồn | LNST +54,87%, CFO/LNST ≈ 0,110 lần; cần xem tiếp |
| Khoản mục nào đóng góp vào CFO? | Cần tự nhóm/cộng dòng | Cầu nối, ΔCFO và residual | Cầu nối thủ công khớp, thuế đóng góp −648,134 tỷ |
| Chi cổ tức quý ít có nghĩa mức năm giảm? | Dòng chi không đủ lịch đợt và năm lợi nhuận | Chính sách theo năm đặt cạnh thực chi theo kỳ, trạng thái ghép | Mức 2025 phê duyệt 4.350 đồng, lịch đợt còn lại ngoài Q1; chi nhỏ Q1 chưa ghép |
| Một thông báo có hai năm thì cộng thế nào? | Cần tìm thêm thông báo và tự tách | Thành phần theo năm, kiểm tổng, ngày công bố/bản sửa | Tránh tổng sai 4.700 đồng thay vì 4.350 đồng cho 2025 |
| Tin số trích tự động đến đâu? | Cần kiểm ảnh nguồn và theo dõi sửa | Ứng viên, số duyệt, nguồn, lịch sửa và kiểm tổng | Sáu ô chọn trước khớp, ô khác sai 9 triệu đồng |

Người có chuyên môn vẫn có thể làm các bước này thủ công. Lý do xây hệ thống là tổ chức công việc lặp, giữ ngữ cảnh và hỗ trợ kiểm lại khi có nhiều kỳ/doanh nghiệp; **chưa đo được hệ thống nhanh hơn bao nhiêu**. Crawler/OCR tạo đầu vào, còn lợi ích đề tài nằm ở câu trả lời có số hỗ trợ, quy tắc ghép và bằng chứng mở lại được.

### 3.4. Điều đã minh họa và lợi ích còn phải đo

**Đã minh họa bằng tài liệu thật:** có thể thu thập/trích ứng viên trên mẫu; kết hợp lợi nhuận–CFO dẫn tới câu hỏi đọc sâu hơn; cầu nối kiểm được đóng góp; tách năm cổ tức tránh tổng sai; kiểm nguồn/tổng phát hiện lỗi OCR. Các kết quả hỗ trợ tính hợp lý của hướng đề tài, không đại diện tần suất vấn đề trên toàn thị trường.

**Còn phải đo:** thời gian toàn luồng so với nhập/ghép thủ công, số đúng/sai/thiếu trên tài liệu độc lập, phút duyệt, độ phủ thông báo/bản sửa, tỷ lệ trả lời đúng câu hỏi và khả năng tìm lại bằng chứng. Chưa có khảo sát nhu cầu, thử người dùng hoặc kết quả chứng minh quyết định đầu tư tốt hơn. Thiết kế đánh giá nằm ở mục 6 của [báo cáo 1](bao-cao-01.md).

## 4. Lỗi quan sát và giới hạn

Sáu ô được chọn khớp không có nghĩa toàn bộ OCR đúng. Ở trang PDF 13, OCR đọc “kinh doanh” thành “kinh donnh”, mã 11 thành 1, số thuế thành `(1.579.997498166)` mất dấu phân nhóm. Khi lập cầu nối thủ công cho ví dụ chính, đối chiếu thêm phát hiện dòng 12 cột Q1/2025 bị OCR đọc **−61.940.344.633** thay vì **−61.949.344.633 VND**, lệch **+9.000.000 VND**. Nếu dùng ô sai và giữ nguyên các dòng khác, tổng sẽ lệch CFO +9 triệu đồng. Ô này nằm ngoài sáu ô đã chọn, không được tính vào kết quả 6/6. Trang PDF 14 có nhãn tổng dòng tiền bị hỏng. Parser hiện chỉ tìm ba nhãn được chọn; nhãn CFO dùng phần đầu để chịu được lỗi ở dòng tiếp theo. Chưa trích tự động đủ cầu nối, chưa kiểm mọi mã dòng hoặc tự nhận diện năm, scope và đơn vị.

Giữ nguyên OCR gốc, lưu ứng viên và đối chiếu riêng. Bước đọc thủ công trang nguồn vẫn cần để xác nhận context và số. **6/6 ô của mẫu phát triển** chỉ hỗ trợ tiếp tục prototype; chưa có cơ sở công bố accuracy chung hoặc tiết kiệm thời gian người dùng. Thử nghiệm DHG ngày 05/10/2026 trước đó có một ô tỷ giá OCR sai 2.000 đồng; [log cũ](../../../../data-sets/research-evidence/2026-10-05-report-01/comparison.json) được giữ để không mất bằng chứng lỗi khi đổi mẫu.

## 5. Cách chạy lại và minh chứng

Môi trường dùng Python 3.12.14, `lxml` 6.1.1, `pypdf` 6.10.0, Node 24.19.0, Tesseract.js 7.0.0 và Poppler 26.07.0. Chạy từ gốc repo, điều chỉnh đường dẫn runtime theo máy. OCR cần dữ liệu ngôn ngữ hoặc cache.

```powershell
$evidenceDir = 'data-sets/research-evidence/2026-10-06-report-01-vnm-q1-2026'
$pdfRenderer = 'C:/path/to/poppler/pdftoppm.exe'
$ocrModule = 'C:/path/to/node_modules/tesseract.js'

# Mặc định dừng nếu robots không xác định; lần thử tệp công khai này dùng cờ ghi rõ trong log.
python scripts/research/probe_vnm_q1.py $evidenceDir --allow-unknown-robots
python scripts/research/check_vnm_q1.py prepare $evidenceDir --pdftoppm $pdfRenderer
node scripts/research/probe_ocr.cjs $ocrModule "$evidenceDir/page-jobs.json" "$evidenceDir/ocr"
python scripts/research/check_vnm_q1.py check $evidenceDir
```

Adapter chưa tổng quát hóa cho các quý/năm khác. Bộ kiểm tra dừng nếu hash PDF khác bảng tham chiếu; cần đọc lại trang và cập nhật tham chiếu thay vì mặc nhiên so dữ liệu mới. Chạy lại có thể thay đổi nguồn, số liên kết và thời gian; dùng thư mục mới để giữ log cũ.

- [Log chạy mặc định dừng tại robots CDN](../../../../data-sets/research-evidence/2026-10-06-report-01-vnm-q1-2026/source-probe-conservative.json).
- [Log thu thập và kiểm lớp chữ thành công](../../../../data-sets/research-evidence/2026-10-06-report-01-vnm-q1-2026/source-probe.json), [HTML danh mục](../../../../data-sets/research-evidence/2026-10-06-report-01-vnm-q1-2026/catalog.html).
- [Log OCR](../../../../data-sets/research-evidence/2026-10-06-report-01-vnm-q1-2026/ocr/ocr-run.json), văn bản trang [12](../../../../data-sets/research-evidence/2026-10-06-report-01-vnm-q1-2026/ocr/vnm-q1-2026-p12-ocr.txt), [13](../../../../data-sets/research-evidence/2026-10-06-report-01-vnm-q1-2026/ocr/vnm-q1-2026-p13-ocr.txt), [14](../../../../data-sets/research-evidence/2026-10-06-report-01-vnm-q1-2026/ocr/vnm-q1-2026-p14-ocr.txt).
- [Đối chiếu và phép tính](../../../../data-sets/research-evidence/2026-10-06-report-01-vnm-q1-2026/comparison.json), [tham chiếu đọc gốc](../../../research-profit-cash-dividend/evidence/case-vnm-q1-2026.json).
- [Hồ sơ cầu nối và sự kiện cổ tức](../../../research-profit-cash-dividend/evidence/case-vnm-q1-2026.json): các mục `manual_bridge`, `dividend_context`; ghi số nguồn, thành phần, mốc công bố, phép kiểm và phần chưa ghép. Các ảnh thuyết minh bổ sung phục vụ đọc thủ công, không thay log OCR ba trang.
- Script [tìm/tải VNM](../../../../scripts/research/probe_vnm_q1.py), [chuẩn bị/đối chiếu](../../../../scripts/research/check_vnm_q1.py), [OCR](../../../../scripts/research/probe_ocr.cjs).

SHA-256 PDF: `aa9e9d9a18fbbf05cc23c35b71a5dbae7a0a858a81727ff2e0d1c8ad047cb451`. Minh chứng kỹ thuật PDF/PNG/JSON/TXT nằm trong thư mục dữ liệu cục bộ; tài liệu báo cáo vẫn chỉ Markdown. Thư mục dữ liệu bị Git bỏ qua nên các liên kết minh chứng chỉ dùng được khi giữ kèm dữ liệu trên máy.
