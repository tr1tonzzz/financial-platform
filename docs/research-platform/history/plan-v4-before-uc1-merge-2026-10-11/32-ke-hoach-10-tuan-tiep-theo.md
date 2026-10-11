# Kế hoạch 10 tuần tiếp theo — HPG, VNM, FPT và PaddleOCR

Cập nhật **11/10/2026**, kế hoạch **v4**, theo hạn còn **10 tuần** do người thực hiện cung cấp. **Cuối tuần 4 phải demo cơ bản UC-1/2/3; tuần 5 hoàn thiện trên ba doanh nghiệp và sửa lỗi.** Đây là tuần làm tiếp từ mốc hiện tại, không đếm lại tuần học kỳ hoặc giả định thực nghiệm quý đã hoàn thành UC-1.

Mốc hiện tại: thử công cụ/pipeline Tesseract trên một BCTC VNM quý I/2026, ba dòng × hai cột, 6/6 ô khớp đối chiếu thủ công; có thêm crawler và prototype tính toán. Điều này hỗ trợ tính khả thi ban đầu của pipeline, chưa chứng minh PaddleOCR, trích xuất tổng quát hoặc ứng dụng đã chạy. [Minh chứng công cụ](reports/dot-01-tuan-01-02/thu-nghiem-cong-cu.md).

Phạm vi: **HPG/VNM/FPT, BCTC năm 2023–2025, ưu tiên hợp nhất; chín báo cáo và 54 ô lõi**. [Quyết định stack](31-chot-pham-vi-va-stack-paddleocr.md), [manifest](../../config/pilot-scope.json), [SRS v3.3](22-srs-dac-ta-yeu-cau-phan-mem.md). Python 3.12/SQLite/pandas/Streamlit, PaddleOCR chính, Tesseract đối chứng. Không mở thêm doanh nghiệp, DuPont, ML, danh mục hoặc định giá.

## Cách dùng và ngân sách

[Checklist HTML đánh dấu/lưu tiến độ](checklist-10-tuan-v4.html) và [JSON kế hoạch](checklist-10-tuan-v4.json) được sinh từ cùng nguồn. Tick phản ánh việc người dùng tự xác nhận; không tự nghiệm thu. Tất cả việc tương lai mặc định trống; baseline đã chạy được ghi riêng. Bản cũ 13 tuần và bản lưu trình duyệt của nó giữ nguyên, không chuyển tick sang tiêu chí mới.

**178 giờ dự toán**, khoảng **16–20 giờ/tuần**, đã gồm ghi báo cáo và phần dự phòng trong task. Quỹ giờ thực chưa được cung cấp; đây là ước lượng cần kiểm sau tuần 2, không phải cam kết đủ mọi nghĩa vụ trong 178 giờ và không cộng vào baseline 167 giờ/ước lượng 98–150 giờ cũ. Nếu quỹ thấp hơn, ưu tiên lỗi core, giữ demo bằng dữ liệu đã kiểm thủ công và hoãn UC-4; phần tự động chưa đạt vẫn báo chưa đạt. Không tự giảm nghĩa vụ M của SRS.

Mỗi tuần chia 4–5 buổi: đầu tuần đọc/chuẩn bị đúng phần cần; các buổi giữa viết/ghép code; cuối tuần kiểm luồng, lưu bằng chứng và giờ thật. Hạn/ngày cụ thể tính theo ngày bạn chọn trong HTML. Báo cáo định kỳ cuối tuần 2/4/6/8/10, thêm mốc kiểm tuần 5 theo yêu cầu; không sinh báo cáo tiến độ giả trước khi làm.

Nơi lưu đầu ra đề xuất: `data-sets/fap/execution-v4/` cho PDF/ảnh/DB/kết quả, phải sao lưu riêng vì Git-ignore; `docs/research-platform/execution-v4/week-NN.md` cho nhật ký/minh chứng. Đường dẫn là mục tiêu tạo khi thực hiện, chưa có output không được tick.

## Mốc demo 4–5 tuần: thế nào là đủ cơ bản?

| UC | Demo cuối tuần 4 | Bổ sung tuần 5 |
|---|---|---|
| UC-1 | Chọn mã/năm, xem sáu chỉ tiêu đã duyệt hoặc lý do thiếu, truy xuất trang nguồn, xuất CSV; có luồng duyệt/sửa | Chọn được HPG/VNM/FPT; ledger chín báo cáo/54 ô được rà |
| UC-2 | Một công ty có bảng/biểu đồ nhiều kỳ, LNST/CFO, tỷ số có điều kiện; mở số nguồn, lưu nhận xét | Chạy trên phần dữ liệu đã duyệt của ba mã, sửa lỗi bộ chọn/đơn vị/thiếu |
| UC-3 | Chọn ít nhất hai công ty cùng năm/scope; xem bảng/biểu đồ cạnh nhau và tỷ số | So sánh nhóm ba mã, nhiều năm khi đủ nguồn; giải thích khác ngành |

Đây là demo chức năng, chưa là nghiệm thu toàn bộ SRS. Nhập tay/sửa số có nguồn để demo được chấp nhận nhưng phải hiện acquisition/review; không cộng vào độ chính xác tự động hoặc discovery. Chưa đủ dữ liệu phải báo độ đầy đủ chưa đạt, dù màn hình đã chạy.

## Tổng quan tuần

| Tuần | Trọng tâm | Giờ dự toán | Đầu ra chính |
|---|---|---:|---|
| 1 | PaddleOCR và một BCTC năm có nguồn | 16 | UC-1 |
| 2 | UC-1 chạy từ báo cáo đến bảng dữ liệu | 18 | UC-1 |
| 3 | UC-2: biểu đồ, tỷ số và lưu phân tích | 16 | UC-2 |
| 4 | UC-3 và demo cơ bản ba UC đầu | 16 | UC-1/2/3 |
| 5 | Hoàn thiện ba công ty, kiểm chất lượng ba UC đầu | 20 | UC-1/2/3 |
| 6 | UC-5: thông báo và lịch sử cổ tức | 18 | UC-5 |
| 7 | UC-5: cơ sở tiền mặt và cầu nối CFO theo ca | 20 | UC-2/5 |
| 8 | UC-5: basis DPS, hồ sơ lưu và đo OCR | 20 | UC-5 |
| 9 | Ổn định hệ thống; UC-4 có điều kiện | 16 | Kiểm hệ thống; UC-4 sau gate |
| 10 | Nghiệm thu thử, đóng gói và báo cáo cuối | 18 | UC-1/2/3/5 và phần UC-4 đã làm |

## Công việc chi tiết

### Tuần 01 — PaddleOCR và một BCTC năm có nguồn

**UC:** UC-1 · **Giờ dự toán:** 16

**Đầu vào:** Manifest HPG/VNM/FPT; ảnh/prototype VNM Q1/2026 là tài liệu phát triển, không phải dữ liệu năm.

- [ ] **W01-01 — Chuẩn bị Python 3.12 và môi trường riêng; cài PaddleOCR/PaddlePaddle CPU.** (4 giờ)
  - Xong khi: Chạy engine và OCR một ảnh thật; lưu phiên bản package/model/config, thời gian và lỗi; không đổi venv cũ.
- [ ] **W01-02 — Lập ledger 9 báo cáo và 54 ô, nối manifest đã chốt.** (2 giờ)
  - Xong khi: Mỗi mã/năm có scope/kỳ/status; ghi nơi lưu PDF và lý do thiếu; không đánh dấu đã thu từ manifest kế hoạch.
- [ ] **W01-03 — Thu một BCTC năm hợp nhất của mỗi mã; chọn một PDF để chạy đầu tiên.** (3 giờ)
  - Xong khi: Xác nhận bìa/header, kiểm toán, đơn vị, URL/hash; ghi assisted riêng nếu nguồn không tự phát hiện được.
- [ ] **W01-04 — Tạo adapter Paddle và chọn text hoặc OCR theo chất lượng trang.** (4 giờ)
  - Xong khi: Kết quả giữ trang/bbox/text/confidence/engine; parser chưa phải OCR. Chạy mẫu một trang mỗi mã, ghi rõ đã chạy/thiếu.
- [ ] **W01-05 — Đọc sáu ô tham chiếu của báo cáo đầu, chọn tập kiểm chưa dùng chỉnh parser.** (2 giờ)
  - Xong khi: Lưu nhãn/cột/đơn vị/scope và giá trị; phân nhóm tài liệu theo lineage trước khi tinh chỉnh; tự kiểm ghi rõ tự kiểm.
- [ ] **W01-06 — Ghi nhật ký tuần và chốt lát cắt UC-1/2/3 để demo tuần 4.** (1 giờ)
  - Xong khi: Có giờ thực, ảnh/log Paddle và đặc tả nhỏ đầu vào→xử lý→đầu ra; phần bổ sung danh mục ghi riêng với SRS.

**Đầu ra cần lưu:**

- environment.md và dependency/model lock sau khi chạy qua
- ledger-reports.csv, ledger-targets.csv, reference-facts.csv
- ocr-runs/ và ghi nhận tập development/holdout

**Tiêu chí chuyển mốc:** Paddle chạy được mẫu thật; có một BCTC năm đúng phạm vi và sáu ô tham chiếu. Chưa gọi bộ trích xuất tổng quát đã hoàn thành.

**Khi vướng/chậm:** Nếu cài Paddle lỗi: dùng tối đa hai buổi tập trung xử lý, ghi lỗi; vẫn dựng kho/UI bằng số nhập có nguồn. Không tự đổi lại engine hoặc gọi số nhập tay là OCR.

**Yêu cầu liên quan:** FR01, FR03, FR05, FR08, FR10, FR12, IR01, IR02, NFR07, NFR08, DR03, DR04.

**Ca kiểm cần thực hiện:** TC01, TC02, TC03, TC06, TC08. Đây là phân bổ kế hoạch, chưa phải kết quả pass.

### Tuần 02 — UC-1 chạy từ báo cáo đến bảng dữ liệu

**UC:** UC-1 · **Giờ dự toán:** 18

**Đầu vào:** Một PDF năm, sáu ô tham chiếu, adapter OCR và metadata tuần 1.

- [ ] **W02-01 — Tạo SQLite cho tài liệu, candidate, số đã duyệt, audit và phiên bản.** (4 giờ)
  - Xong khi: Khóa/ràng buộc đúng; lưu số tiền integer/Decimal; sửa không xóa lịch sử; backup mẫu DB.
- [ ] **W02-02 — Ánh xạ sáu chỉ tiêu và chuẩn hóa dấu/đơn vị/cột.** (4 giờ)
  - Xong khi: Text/Paddle tạo candidate hoặc thiếu có lý do; không lấy LNST cổ đông mẹ thay tổng LNST; không đổi gạch mơ hồ thành 0.
- [ ] **W02-03 — Làm màn hình duyệt số cạnh trang nguồn.** (4 giờ)
  - Xong khi: Duyệt/sửa/từ chối có trước–sau/lý do; ô blocking hoặc thiếu nguồn không được xuất bản; transaction lỗi rollback.
- [ ] **W02-04 — Làm bảng chọn công ty/năm, xem sáu trường và xuất CSV.** (3 giờ)
  - Xong khi: Chọn được báo cáo đầu; mỗi ô đã duyệt truy xuất được nguồn; đơn vị/phạm vi/status rõ; CSV UTF-8 giữ null khác 0.
- [ ] **W02-05 — Kiểm tải lại, raw version và chạy tiếp sau lỗi.** (2 giờ)
  - Xong khi: 304/cùng hash không nhân raw; lỗi một file không phá file khác; nhập tay có acquisition_mode=assisted.
- [ ] **W02-06 — Báo cáo tiến độ đợt 1 và lưu demo UC-1.** (1 giờ)
  - Xong khi: Demo PDF→candidate→duyệt→bảng→nguồn→CSV; ghi đúng phần tự động/phần thủ công, giờ thực và lỗi.

**Đầu ra cần lưu:**

- DB pilot và bảng/review trong ứng dụng
- CSV đã duyệt và audit sửa một ô
- week-02.md + ảnh/video ngắn/log chạy

**Tiêu chí chuyển mốc:** Một báo cáo có luồng khai thác dùng được. Bảng không hiển thị candidate chưa duyệt như số chính thức.

**Khi vướng/chậm:** Không đợi parser đạt độ chính xác cao ở mọi bố cục. Cho nhập/sửa có nguồn để hoàn thành luồng và đo công sức.

**Yêu cầu liên quan:** FR02, FR06, FR07, FR09, FR11, FR14, FR15, FR16, FR17, FR18, FR33, FR31, DR01, DR02, DR05, DR06, IR03, IR04, NFR01, NFR03, BR01, BR02, BR03, BR12.

**Ca kiểm cần thực hiện:** TC04, TC05, TC06, TC07, TC10, TC11, TC12, TC23, TC24, TC27. Đây là phân bổ kế hoạch, chưa phải kết quả pass.

### Tuần 03 — UC-2: biểu đồ, tỷ số và lưu phân tích

**UC:** UC-2 · **Giờ dự toán:** 16

**Đầu vào:** Kho số đã duyệt; bổ sung hai năm còn lại của công ty đầu bằng nguồn đúng scope.

- [ ] **W03-01 — Viết engine delta/growth, CFO/LNST, tiền/tài sản và nợ phải trả/tài sản.** (4 giờ)
  - Xong khi: Chỉ dùng reviewed operands; nền tăng trưởng≤0, thiếu năm, assets≤0/cross-scope trả lý do; CFO âm được giữ.
- [ ] **W03-02 — Dựng bảng và biểu đồ LNST/CFO theo năm.** (4 giờ)
  - Xong khi: Có nhãn/trục/đơn vị; không nối qua số thiếu; đổi năm/mã cập nhật đúng cả bảng và biểu đồ.
- [ ] **W03-03 — Gắn công thức, nguồn và lưu/mở lại lần phân tích.** (4 giờ)
  - Xong khi: Chọn một kết quả mở operands; lưu mã/kỳ/scope/revision/ghi chú; dữ liệu mới không âm thầm thay bản đã lưu.
- [ ] **W03-04 — Xuất bảng và nhận xét cùng bối cảnh.** (2 giờ)
  - Xong khi: CSV/JSON có nguồn/phiên bản, null/status; roundtrip mở lại không mất tiếng Việt/dấu âm.
- [ ] **W03-05 — Kiểm ca thiếu và mẫu số không hợp lệ.** (1 giờ)
  - Xong khi: Có expected/actual cho các ca biên; số giả định chỉ làm fixture, tách khỏi case doanh nghiệp.
- [ ] **W03-06 — Demo câu hỏi lợi nhuận tăng có đi cùng CFO không.** (1 giờ)
  - Xong khi: Ghi một nhận xét từ dữ liệu thật, ít nhất hai số nguồn và giới hạn; lưu giờ thực.

**Đầu ra cần lưu:**

- Màn hình phân tích công ty đầu qua 2023–2025
- engine + fixture công thức và snapshot mẫu
- week-03.md

**Tiêu chí chuyển mốc:** UC-2 có bảng/biểu đồ và tỷ số thực dùng được; mở lại đúng bối cảnh. Chưa bắt buộc DuPont/doanh thu/biên lợi nhuận.

**Khi vướng/chậm:** Nếu chưa đủ ba năm: hiển thị phần đã duyệt, ghi missing. Không dùng quý 2026 để thay năm 2025.

**Yêu cầu liên quan:** FR25, FR26, FR27, FR32, FR34, FR35, BR11, DR08, NFR02, NFR05.

**Ca kiểm cần thực hiện:** TC18, TC19, TC21, TC23, TC24, TC25. Đây là phân bổ kế hoạch, chưa phải kết quả pass.

### Tuần 04 — UC-3 và demo cơ bản ba UC đầu

**UC:** UC-1/2/3 · **Giờ dự toán:** 16

**Đầu vào:** UC-1/2 dùng được; số đã duyệt của doanh nghiệp thứ hai, tối thiểu một năm trùng với công ty đầu.

- [ ] **W04-01 — Thu và duyệt dữ liệu doanh nghiệp thứ hai.** (4 giờ)
  - Xong khi: Ít nhất một năm chung, sáu trường có số đã duyệt hoặc lý do thiếu; giữ scope cùng cơ sở.
- [ ] **W04-02 — Viết truy vấn và engine so sánh doanh nghiệp tự chọn.** (4 giờ)
  - Xong khi: Chọn hai mã/kỳ; chuẩn hóa đơn vị; tái dùng công thức UC-2; khác scope hoặc thiếu operand không tạo so sánh giả.
- [ ] **W04-03 — Dựng bảng/biểu đồ cạnh nhau và giải thích giới hạn.** (3 giờ)
  - Xong khi: Đối chiếu LNST/CFO và tỷ số; mở nguồn từng mã; không xếp hạng/sàng lọc hoặc gọi nhóm khác ngành là benchmark ngành.
- [ ] **W04-04 — Nối luồng tra cứu→phân tích→so sánh→lưu/xuất.** (2 giờ)
  - Xong khi: Người dùng không cần chạy script riêng để chuyển giữa ba UC; bộ chọn giữ kỳ/scope rõ.
- [ ] **W04-05 — Chạy và ghi demo mốc 4 tuần; báo cáo đợt 2.** (2 giờ)
  - Xong khi: Ba tác vụ đi hết luồng, có file/run và dữ liệu thật; ghi phần assisted và danh sách lỗi; chưa tuyên bố nghiệm thu tất cả SRS.
- [ ] **W04-06 — Dự phòng sửa lỗi chặn demo.** (1 giờ)
  - Xong khi: Ưu tiên nguồn/đơn vị/bộ chọn/số sai; không thêm giao diện nâng cao hoặc chỉ tiêu ngoài lát cắt.

**Đầu ra cần lưu:**

- Ứng dụng demo UC-1/2/3
- demo-week-04.md với kịch bản và kết quả
- ảnh/CSV/snapshot của nhóm so sánh

**Tiêu chí chuyển mốc:** **Mốc bắt buộc:** cuối tuần 4 demo cơ bản UC-1/2/3; UC-1 truy số/nguồn, UC-2 có biểu đồ/tỷ số, UC-3 so ít nhất hai công ty.

**Khi vướng/chậm:** Nếu nguồn thứ hai chậm: ưu tiên nhập số đã đối chiếu thủ công có provenance, báo assisted. Nếu luồng còn lỗi, chuyển tuần 5 sửa ba UC đầu trước cổ tức.

**Yêu cầu liên quan:** FR32, FR31, IR03, NFR05, BR01.

**Ca kiểm cần thực hiện:** TC07, TC18, TC19, TC21, TC23. Đây là phân bổ kế hoạch, chưa phải kết quả pass.

### Tuần 05 — Hoàn thiện ba công ty, kiểm chất lượng ba UC đầu

**UC:** UC-1/2/3 · **Giờ dự toán:** 20

**Đầu vào:** Demo tuần 4 và danh sách lỗi; ledger chín báo cáo chính.

- [ ] **W05-01 — Thu/xác nhận chín BCTC HPG/VNM/FPT 2023–2025 và rà 54 targets.** (6 giờ)
  - Xong khi: Mọi target có trạng thái; cố gắng đủ số nhưng thiếu phải có lý do và báo độ đầy đủ chưa đạt; kiểm bản sửa/phạm vi FPT.
- [ ] **W05-02 — Sửa parser theo lỗi thật trên tập phát triển.** (3 giờ)
  - Xong khi: Lưu fixture/layout và lỗi trước–sau; không xem/chỉnh theo tập kiểm đã giữ riêng.
- [ ] **W05-03 — Mở so sánh cả ba mã và chuỗi nhiều năm.** (3 giờ)
  - Xong khi: Bảng/biểu đồ hiển thị đúng số/thiếu; không đổi kỳ hoặc scope âm thầm; nguồn từng ô truy được.
- [ ] **W05-04 — Freeze tập kiểm OCR/trích số và đo thử công sức.** (3 giờ)
  - Xong khi: 20–30 trang mục tiêu từ nhiều bố cục; ghi số trang/ô thực và lineage. Nếu chưa đủ mẫu, báo cỡ mẫu nhỏ thay vì nhân bản trang.
- [ ] **W05-05 — Sửa lỗi và rà yêu cầu cho UC-1/2/3.** (3 giờ)
  - Xong khi: Lập ma trận đã chạy/chưa chạy, các chức năng bổ sung F03 có tiêu chí riêng; không tự pass yêu cầu SRS bằng tick.
- [ ] **W05-06 — Chốt demo mốc 5 tuần và cập nhật kế hoạch bằng giờ thực.** (2 giờ)
  - Xong khi: Cả ba mã chọn được; phân tích/so sánh ổn định trên phần số đã duyệt; báo đủ/thiếu dữ liệu tách khỏi đủ chức năng.

**Đầu ra cần lưu:**

- ledger chín reports/54 ô đã rà và báo cáo coverage
- freeze-manifest.json + extraction-error-log.csv
- demo-week-05.md và requirement-status.csv

**Tiêu chí chuyển mốc:** **Mốc cam kết triển khai:** tuần 5 có bản cơ bản ba UC đầu cho HPG/VNM/FPT; lỗi dữ liệu/nguồn còn lại phải được công bố, không giả hoàn tất.

**Khi vướng/chậm:** Không mở thêm doanh nghiệp, doanh thu/DuPont hoặc benchmark ngành. Nếu chưa đạt, ưu tiên sửa và giảm phần UC-4 tùy chọn.

**Yêu cầu liên quan:** FR36, DR07, NFR10.

**Ca kiểm cần thực hiện:** TC01, TC07, TC12, TC26. Đây là phân bổ kế hoạch, chưa phải kết quả pass.

### Tuần 06 — UC-5: thông báo và lịch sử cổ tức

**UC:** UC-5 · **Giờ dự toán:** 18

**Đầu vào:** Kho ba công ty; nguồn IR/VSDC và notice mẫu lịch sử để phát triển.

- [ ] **W06-01 — Viết một adapter tự phát hiện notice theo doanh nghiệp/cửa sổ.** (5 giờ)
  - Xong khi: Có log từ catalog/search chính thức tới notice thật của mẫu; seed từng URL đếm assisted, không đạt FR04.
- [ ] **W06-02 — Trích và duyệt notice/components.** (3 giờ)
  - Xong khi: Tách đúng năm lợi nhuận/đợt, loại quyền, DPS, ngày; notice hỗn hợp không đẩy toàn bộ vào năm đăng.
- [ ] **W06-03 — Làm liên kết trùng, sửa và hủy đúng đối tượng.** (4 giờ)
  - Xong khi: Giữ old/current; sửa amount không cộng hai lần; hủy record notice không tự hủy chính sách/annual DPS.
- [ ] **W06-04 — Lập coverage từng mã/năm và tổng DPS có điều kiện.** (3 giờ)
  - Xong khi: Không tìm thấy khác 0; partial/unknown khác complete_as_of; chặn cộng khi basis chưa rõ.
- [ ] **W06-05 — Dựng timeline/bảng cổ tức và nguồn.** (2 giờ)
  - Xong khi: Tách lịch trả với xác nhận thực trả; FY2025 có thể có thông báo 2026; ngày đã qua không tự thành paid.
- [ ] **W06-06 — Báo cáo đợt 3 và ca notice hỗn hợp/sửa.** (1 giờ)
  - Xong khi: Một hồ sơ từ nguồn tới màn hình; ghi số notice đã rà, tự động/assisted và các mục unresolved.

**Đầu ra cần lưu:**

- notices/components/relations và coverage ledger
- màn hình lịch sử cổ tức có trạng thái
- week-06.md + fixture vòng đời

**Tiêu chí chuyển mốc:** UC-5 đọc được lịch sử quan sát, không giả đầy đủ; có discovery notice thật hoặc FR04 được báo chưa đạt.

**Khi vướng/chậm:** Nếu nguồn chặn: thử nguồn IR chính thức phù hợp; thu thủ công để demo nhưng báo thiếu FR04, không tự đổi nghĩa vụ nghiệm thu.

**Yêu cầu liên quan:** FR04, FR13, FR19, FR20, FR21, FR22, FR23, FR24, FR28, BR04, BR05, BR06, BR07, BR08, BR09, BR10, DR04, DR07.

**Ca kiểm cần thực hiện:** TC02, TC08, TC09, TC13, TC14, TC15, TC16, TC17, TC20. Đây là phân bổ kế hoạch, chưa phải kết quả pass.

### Tuần 07 — UC-5: cơ sở tiền mặt và cầu nối CFO theo ca

**UC:** UC-2/5 · **Giờ dự toán:** 20

**Đầu vào:** Một BCTC của HPG/VNM/FPT có operands G02/cầu nối đọc được; không dùng DHG thay case nghiệm thu chính.

- [ ] **W07-01 — Đọc/duyệt CAPEX và khoản phân phối chủ sở hữu cho một ca.** (4 giờ)
  - Xong khi: Cùng kỳ/scope/unit với CFO; lưu nhãn nguồn và loại khoản chi gộp/tách; không abs mọi dòng đầu tư.
- [ ] **W07-02 — Làm cầu nối LNTT→CFO từ các dòng cấu thành.** (6 giờ)
  - Xong khi: Một ca thật; leaf chỉ cộng một lần, subtotal chỉ kiểm; có residual/tolerance và nguồn từng dòng. Hai kỳ chỉ thêm khi đủ.
- [ ] **W07-03 — Ghép hàm bao phủ CFO−CAPEX và các khoản chi.** (4 giờ)
  - Xong khi: Có công thức/operands/điều kiện; CFO âm giữ dấu; chi=0 chặn tỷ số; không gọi kết quả là FCFE.
- [ ] **W07-04 — Dựng biểu đồ cầu nối và bảng bao phủ có nguồn.** (3 giờ)
  - Xong khi: Người dùng hiểu khoản nào đóng góp CFO và khoản chi được bao phủ thế nào; khoản gộp không hiện thành cổ tức thường đã tách.
- [ ] **W07-05 — Kiểm thiếu/sai dấu/sai kỳ và snapshot kết quả.** (2 giờ)
  - Xong khi: Ca thiếu trả lý do; fixture tách ca thật; xuất/mở lại giữ operand/formula version.
- [ ] **W07-06 — Ghi nhận xét đầu tư có căn cứ và giới hạn.** (1 giờ)
  - Xong khi: Lưu câu hỏi cần đọc thêm với số/nguồn; không suy khả năng trả cổ tức tương lai từ một tỷ số.

**Đầu ra cần lưu:**

- bridge-lines.csv và cầu nối có residual
- G02 case có operands và định nghĩa khoản chi
- week-07.md + snapshot

**Tiêu chí chuyển mốc:** Ít nhất một ca mẫu chính có cầu nối và bao phủ chạy được; không ép khớp bằng dòng bù. Nhiều ca/E05/E10 chỉ khi đủ thời gian và quyết định kích hoạt.

**Khi vướng/chậm:** Nếu không đủ dòng phân rã: ghi unresolved và tiếp tục đọc một báo cáo khác trong ba mã; không dùng sáu số tổng để dựng phân rã giả.

**Yêu cầu liên quan:** E01, E02, E03, E04, E05, E06, E07, E08, E09, E10, D01, D02, D03, D04, D11.

**Ca kiểm cần thực hiện:** P01, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, TC-D01, TC-D02, TC-D03, TC-D04, TC-D11. Đây là phân bổ kế hoạch, chưa phải kết quả pass.

### Tuần 08 — UC-5: basis DPS, hồ sơ lưu và đo OCR

**UC:** UC-5 · **Giờ dự toán:** 20

**Đầu vào:** Ledger sự kiện, ca tiền mặt/cầu nối, tập kiểm đã freeze tuần 5.

- [ ] **W08-01 — Thu/duyệt sự kiện vốn cần cho HPG/FPT và trạng thái basis VNM.** (5 giờ)
  - Xong khi: Loại/tỷ lệ/ngày hiệu lực có nguồn; không suy ngày basis từ ngày record hoặc coi mọi phát hành là split.
- [ ] **W08-02 — Ghép điều chỉnh DPS và chặn khi chưa đủ cơ sở.** (3 giờ)
  - Xong khi: Giữ DPS gốc; chỉ chain hợp lệ; unsupported/unresolved/tương lai bị chặn; chưa đủ dữ liệu vẫn là đầu ra hợp lệ có lý do.
- [ ] **W08-03 — Dựng lịch sử cổ tức và biểu đồ có trạng thái so sánh.** (3 giờ)
  - Xong khi: Annual/growth chỉ khi coverage và basis đủ; không cộng cổ tức cổ phiếu vào thu nhập tiền mặt.
- [ ] **W08-04 — Lưu hồ sơ nhận xét/câu hỏi, xuất và replay offline.** (3 giờ)
  - Xong khi: Bối cảnh/nguồn/version/checksum đầy đủ; sửa dữ liệu không thay snapshot cũ; gói hỏng báo lỗi.
- [ ] **W08-05 — Đo Paddle/Tesseract và B0/B1/B2 trên tập kiểm đã giữ.** (4 giờ)
  - Xong khi: Cùng trang/ô; ghi đúng/sai/thiếu metric-value-unit-period-scope và thời gian/công sức; chỉ có một người thì ghi tự kiểm.
- [ ] **W08-06 — Báo cáo đợt 4 và freeze chức năng ưu tiên.** (2 giờ)
  - Xong khi: Demo UC-1/2/3/5; bảng actual/pass/fail/not_run; kết quả OCR không khẳng định tăng lợi nhuận đầu tư.

**Đầu ra cần lưu:**

- corporate-action ledger và raw/reference DPS
- dossier + export/replay bundle
- ocr-evaluation.csv, report-week-08.md

**Tiêu chí chuyển mốc:** Bốn UC ưu tiên có luồng dùng được, kể cả trạng thái chưa đủ dữ liệu; công bố phần chưa đạt SRS. Freeze feature trước tuần 9.

**Khi vướng/chậm:** Không đủ basis thì chặn điều chỉnh; không dựng số giả để demo. Nếu core còn lỗi, tuần 9 không làm UC-4.

**Yêu cầu liên quan:** D05, D06, D07, D08, D11, D12, FR34, FR35, FR36, NFR02, NFR10.

**Ca kiểm cần thực hiện:** TC-D05, TC-D06, TC-D07, TC-D08, TC-D11, TC-D12, TC16, TC20, TC24, TC25, TC26. Đây là phân bổ kế hoạch, chưa phải kết quả pass.

### Tuần 09 — Ổn định hệ thống; UC-4 có điều kiện

**UC:** Kiểm hệ thống; UC-4 sau gate · **Giờ dự toán:** 16

**Đầu vào:** Feature freeze tuần 8; ma trận các yêu cầu còn thiếu và bộ demo bốn UC.

- [ ] **W09-01 — Rà toàn bộ yêu cầu/ca kiểm hiện hành và sửa lỗi trọng yếu.** (3 giờ)
  - Xong khi: 91 mã/51 TC có owner/mốc/status/evidence; yêu cầu chưa đạt giữ fail/not_run hoặc có CR, không đổi thành pass.
- [ ] **W09-02 — Backup/restore DB, raw, config và snapshots vào thư mục sạch.** (4 giờ)
  - Xong khi: Hash/reference/revision khớp, replay ít nhất một snapshot; thử lỗi transaction và không nhân dữ liệu khi resume.
- [ ] **W09-03 — Đo hiệu năng và kiểm an toàn local theo SRS.** (3 giờ)
  - Xong khi: TC30 đúng bộ tải chuẩn, TC31 localhost/path/HTML/log; dữ liệu tạo kiểm tải ghi synthetic, không tính thành mẫu nghiên cứu mới.
- [ ] **W09-04 — Nếu gate đạt: danh sách theo dõi và công bố mới tối thiểu.** (3 giờ)
  - Xong khi: Doanh nghiệp tự chọn; xem cập nhật/old-new và mở phân tích. Không sàng lọc hoặc cảnh báo tiêu chí. Nếu core lỗi, dành giờ sửa core và ghi UC-4 hoãn.
- [ ] **W09-05 — Walkthrough tác vụ với người dùng hoặc ghi rõ tự đánh giá.** (2 giờ)
  - Xong khi: Đo tìm số/nguồn, LNST–CFO, so sánh và cổ tức; giờ/lỗi đọc PDF thủ công làm đối chứng tác vụ.
- [ ] **W09-06 — Nhật ký tuần và danh sách lỗi cuối.** (1 giờ)
  - Xong khi: Chốt lỗi phải sửa trước nộp, dữ liệu nào chưa đủ và UC-4 có làm/hoãn; không thêm hướng ML/định giá.

**Đầu ra cần lưu:**

- restore-check.json và yêu cầu/TC có bằng chứng
- performance/local-check logs + walkthrough.md
- UC-4 tối thiểu hoặc quyết định hoãn có lý do

**Tiêu chí chuyển mốc:** Luồng ưu tiên ổn định và restore/replay kiểm được. UC-4 không được lấy giờ sửa lỗi dữ liệu/tính toán để kịp thêm tính năng.

**Khi vướng/chậm:** TC30 là kiểm tải khác bộ pilot chín báo cáo; nếu chưa đủ bộ theo SRS phải ghi chưa đạt, hoặc lập CR phù hợp, không báo phép đo chín PDF là TC30 pass.

**Yêu cầu liên quan:** FR38, IR05, NFR03, NFR04, NFR06, NFR09, NFR05, NFR10.

**Ca kiểm cần thực hiện:** TC05, TC11, TC25, TC27, TC29, TC30, TC31. Đây là phân bổ kế hoạch, chưa phải kết quả pass.

### Tuần 10 — Nghiệm thu thử, đóng gói và báo cáo cuối

**UC:** UC-1/2/3/5 và phần UC-4 đã làm · **Giờ dự toán:** 18

**Đầu vào:** Ứng dụng freeze, hồ sơ đo, danh sách lỗi, raw/DB và snapshots.

- [ ] **W10-01 — Sửa lỗi chặn sử dụng và chạy lại các ca bị ảnh hưởng.** (4 giờ)
  - Xong khi: Số/nguồn đúng, không mất audit/snapshot; không mở thêm chức năng.
- [ ] **W10-02 — Chạy từ môi trường sạch theo README.** (3 giờ)
  - Xong khi: Khôi phục dependency/model/config, có hướng dẫn nguồn/model offline nếu cần; một người khác hoặc tự chạy mới ghi rõ.
- [ ] **W10-03 — Xuất ba case thật của mẫu chính.** (3 giờ)
  - Xong khi: Mỗi case có số/nguồn/phạm vi/coverage/giới hạn và câu hỏi người dùng; không bắt buộc cả ba đều ra kết quả điều chỉnh DPS.
- [ ] **W10-04 — Tổng hợp đánh giá và ma trận nghiệm thu.** (3 giờ)
  - Xong khi: Tách tự động/review/assisted, số đếm/tỷ lệ/giờ; tất cả M được báo pass/fail/not_run hoặc CR, không gọi hoàn tất nếu còn thiếu.
- [ ] **W10-05 — Viết báo cáo cuối và chuẩn bị demo ngắn theo UC.** (4 giờ)
  - Xong khi: Phân rã đầu vào→xử lý→đầu ra→minh chứng; ít lý thuyết tổng quan; báo giới hạn và chức năng đề xuất tách đã chạy.
- [ ] **W10-06 — Đóng gói, sao lưu và kiểm tệp nộp cuối.** (1 giờ)
  - Xong khi: MD/app/evidence thống nhất; có danh sách file/hash và bản lưu tiến độ; dự phòng lỗi nộp.

**Đầu ra cần lưu:**

- release bundle + README + backup
- ba case và acceptance-status.csv
- báo cáo cuối Markdown, kịch bản demo; bản xuất theo yêu cầu trường khi cần

**Tiêu chí chuyển mốc:** Bộ bàn giao chạy/tái lập được và báo đúng phần đã đạt/chưa đạt. Không dùng số tick checklist làm tỷ lệ chất lượng đồ án.

**Khi vướng/chậm:** Nếu còn yêu cầu M chưa đạt, báo thiếu và hướng xử lý/CR cho thầy; không tự giảm yêu cầu hoặc hứa đầy đủ.

**Yêu cầu liên quan:** FR37, FR38, FR36, IR05, NFR01, NFR02, NFR09, NFR10.

**Ca kiểm cần thực hiện:** TC23, TC24, TC25, TC26, TC28, TC29. Đây là phân bổ kế hoạch, chưa phải kết quả pass.

## Đánh giá và kiểm soát phạm vi

Kế hoạch phân bổ 91 yêu cầu hiện hành/51 ca kiểm SRS; không tái đưa FR29/FR30/D09/D10 hoặc sàng lọc dưới tên cảnh báo. Phần bổ sung tương tác biểu đồ/so sánh nhóm F03 có tiêu chí riêng trong tuần 1/4/5, chưa biến toàn danh mục 38 chức năng thành phạm vi nghiệm thu. E05/E10/nhiều ca và các yêu cầu D có điều kiện phải ghi trạng thái kích hoạt/not_applicable có lý do, không mặc định đã đạt.

Freeze lineage trước đo: bản dịch/cột so sánh/bản sửa gần giống không nằm hai phía development/holdout. Cỡ pilot nhỏ thì báo số đếm thật và giới hạn; người tự xây gold phải ghi tự kiểm. Không gọi tập đã chỉnh parser để khớp là tập kiểm độc lập. Đo Paddle–Tesseract trên cùng trang/ô và khai cấu hình; không đổi quyết định OCR thành tuyên bố ưu thế chưa đo.

TC30 yêu cầu bộ tải 24 báo cáo/144 targets/≤200 notices theo SRS, khác mẫu nghiên cứu chín báo cáo. Có thể chuẩn bị bộ kiểm tải riêng nhưng phải ghi nguồn/synthetic, không nhân bản thành corpus nghiên cứu. Không đủ đúng bộ kiểm thì TC30 chưa đạt hoặc cần CR; không báo đo pilot nhỏ là đạt TC30.

Mỗi task chỉ tick khi có đầu ra và bằng chứng đúng tiêu chí. Mỗi TC ghi input/expected/actual, code/config version, pass/fail/not_run, người/ngày và đường dẫn. Nhật ký mỗi tuần: giờ thực, file/run, số đã duyệt/thiếu, lỗi và việc chuyển tuần. Tuần 9 làm UC-4 chỉ khi lỗi core đã xử lý; nếu chưa đạt, dùng giờ đó sửa UC-1/2/3/5 và ghi UC-4 hoãn.

Kết thúc tuần 10: tổng hợp phần đã chạy, phần chưa đạt và dữ liệu chưa đầy đủ. Tất cả yêu cầu M phải có bằng chứng đạt hoặc change record được chấp nhận; checklist/tài liệu không thay nghiệm thu. Trình bày theo UC nhỏ, đầu vào→xử lý→đầu ra→minh chứng; ưu tiên demo và số đo thay tổng quan lý thuyết.
