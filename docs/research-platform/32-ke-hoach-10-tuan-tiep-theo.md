# Kế hoạch 10 tuần tiếp theo — HPG, VNM, FPT và PaddleOCR

Cập nhật **11/10/2026**, kế hoạch **v6**, theo hạn còn **10 tuần** do người thực hiện cung cấp. **Tuần 1 ghép Paddle vào pipeline đã thử và làm UC-1 cơ bản; cuối tuần 4 demo UC-1/2/3; tuần 5 hoàn thiện ba doanh nghiệp.** Đây là tuần làm tiếp từ mốc hiện tại, không đếm lại tuần học kỳ. Chi tiết [tuần 1](33-ke-hoach-chi-tiet-tuan-01.md), [tuần 2](34-ke-hoach-chi-tiet-tuan-02.md), [sáu metrics kế thừa Báo cáo 2 và dữ liệu bổ sung](35-dac-ta-metrics-tu-bao-cao-02.md). Quyết định web thay thiết kế pilot: có API, frontend và migration; tăng dự toán, giữ ID task để truy vết, dùng khóa lưu v6 riêng.

Mốc hiện tại: thử công cụ/pipeline Tesseract trên một BCTC VNM quý I/2026, ba dòng × hai cột, 6/6 ô khớp đối chiếu thủ công; có thêm crawler và prototype tính toán. Điều này hỗ trợ tính khả thi ban đầu của pipeline, chưa chứng minh PaddleOCR, trích xuất tổng quát hoặc ứng dụng đã chạy. [Minh chứng công cụ](reports/dot-01-tuan-01-02/thu-nghiem-cong-cu.md).

Phạm vi: **HPG/VNM/FPT, BCTC năm 2023–2025, ưu tiên hợp nhất; chín báo cáo và 54 ô lõi**. [Quyết định stack](31-chot-pham-vi-va-stack-paddleocr.md), [manifest](../../config/pilot-scope.json), [SRS v3.3](22-srs-dac-ta-yeu-cau-phan-mem.md). React/TypeScript + FastAPI/Python 3.12 + PostgreSQL; pandas cho phân tích, PaddleOCR chính, Tesseract đối chứng. Không mở thêm doanh nghiệp, DuPont, ML, danh mục hoặc định giá.

## Cách dùng và ngân sách

[Checklist HTML đánh dấu/lưu tiến độ](checklist-10-tuan-v4.html) và [JSON kế hoạch](checklist-10-tuan-v4.json) được sinh từ cùng nguồn; giữ tên tệp để URL đang mở tiếp tục dùng được, nội dung hiện là v6. Tick phản ánh việc người dùng tự xác nhận; không tự nghiệm thu. Khi chuyển bản lưu v5: giữ ngày/nhật ký/giờ và tick bốn task không đổi W01-01/02/03, W02-02; các task phụ thuộc web/API/DB cần kiểm lại nên chưa chuyển tick. Bản v4 chỉ chuyển ngày/nhật ký/giờ. Bản lưu gốc vẫn giữ nguyên; có thể xuất JSON để đối chiếu.

**195 giờ dự toán**, khoảng **16–24 giờ/tuần**, đã gồm ghi báo cáo và phần dự phòng trong task. Quỹ giờ thực chưa được cung cấp; đây là ước lượng cần kiểm sau tuần 2, không phải cam kết đủ mọi nghĩa vụ trong 195 giờ và không cộng vào baseline 167 giờ/ước lượng 98–150 giờ cũ. Nếu quỹ thấp hơn, ưu tiên lỗi core, giữ demo bằng dữ liệu đã kiểm thủ công và hoãn UC-4; phần tự động chưa đạt vẫn báo chưa đạt. Không tự giảm nghĩa vụ M của SRS.

Mỗi tuần chia 4–5 buổi: đầu tuần chuẩn bị đúng phần cần, tái sử dụng công cụ đã thử; các buổi giữa viết/ghép code; cuối tuần kiểm luồng, lưu bằng chứng và giờ thật. Hạn/ngày cụ thể tính theo ngày bạn chọn trong HTML. Báo cáo định kỳ cuối tuần 2/4/6/8/10, thêm mốc kiểm tuần 5 theo yêu cầu. Mỗi tuần đều có gợi ý Word/slide để ghi kết quả khi làm; tuần lẻ có thể lưu nháp rồi gộp vào đợt hai tuần. Không phải tạo mười bộ Word/slide hoàn chỉnh hoặc báo cáo kết quả chưa chạy.

**Cách soạn:** Word giữ input→xử lý→output, code/run và số đo, khoảng 1–2 trang cho cập nhật tuần, gộp 3–5 trang nếu phù hợp đợt hai tuần. Slide dùng 4 ý cụ thể bên dưới, mỗi slide một ý, ưu tiên bảng/biểu đồ/demo; không lặp tổng quan đề tài hoặc giải thích lại công cụ đã kiểm. Các gợi ý là nội dung cần soạn, chưa tạo file .docx/.pptx.

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
| 1 | UC-1 cơ bản, thay Paddle vào pipeline đã thử | 24 | UC-1 |
| 2 | Củng cố UC-1, mở dữ liệu nhiều kỳ cho UC-2 | 22 | UC-1; chuẩn bị UC-2 |
| 3 | UC-2: biểu đồ, tỷ số và lưu phân tích | 18 | UC-2 |
| 4 | UC-3 và demo cơ bản ba UC đầu | 18 | UC-1/2/3 |
| 5 | Hoàn thiện ba công ty, kiểm chất lượng ba UC đầu | 20 | UC-1/2/3 |
| 6 | UC-5: thông báo và lịch sử cổ tức | 18 | UC-5 |
| 7 | UC-5: cơ sở tiền mặt và cầu nối CFO theo ca | 20 | UC-2/5 |
| 8 | UC-5: basis DPS, hồ sơ lưu và đo OCR | 20 | UC-5 |
| 9 | Ổn định hệ thống; UC-4 có điều kiện | 17 | Kiểm hệ thống; UC-4 sau gate |
| 10 | Nghiệm thu thử, đóng gói và báo cáo cuối | 18 | UC-1/2/3/5 và phần UC-4 đã làm |

## Công việc chi tiết

### Tuần 01 — UC-1 cơ bản, thay Paddle vào pipeline đã thử

**UC:** UC-1 · **Giờ dự toán:** 24

**Đầu vào:** Tận dụng tải PDF, pypdf và render Poppler đã thử; manifest HPG/VNM/FPT; ảnh VNM Q1/2026 chỉ dùng thử tích hợp OCR, không thay dữ liệu năm.

- [ ] **W01-01 — Thay bước Tesseract bằng adapter Paddle trong pipeline có sẵn.** (2 giờ)
  - Xong khi: Chỉ kiểm lại môi trường cần cho Paddle; dùng ảnh/render cũ, lưu engine/model/version/bbox/text/confidence và log. Không dành một tuần thử lại toàn bộ stack.
- [ ] **W01-02 — Nối manifest đã chốt vào ledger ứng dụng.** (1 giờ)
  - Xong khi: Có 9 report targets/54 ô đích với kỳ/scope/status; xác định các tài liệu theo nhóm trước tinh chỉnh parser. Không chọn lại doanh nghiệp.
- [ ] **W01-03 — Chọn một BCTC năm hợp nhất và đọc sáu ô tham chiếu.** (2 giờ)
  - Xong khi: Ưu tiên PDF FY2025 của HPG đã thu nếu còn tệp/hash đúng; nếu chọn VNM/FPT thì xác nhận nguồn. Có nhãn/cột/đơn vị/trang; quý 2026 không thay báo cáo năm.
- [ ] **W01-04 — Dựng FastAPI, schema PostgreSQL và luồng candidate→duyệt.** (10 giờ)
  - Xong khi: Có migration SQLAlchemy/Alembic, API truy vấn/review, NUMERIC và audit trong transaction; một báo cáo tạo sáu candidates hoặc lý do thiếu; chỉ số reviewed được cung cấp.
- [ ] **W01-05 — Dựng web React/TypeScript gọi FastAPI: bảng, duyệt, nguồn và CSV.** (7 giờ)
  - Xong khi: Có loading/error/empty; chọn mã/năm và xem nguồn từng ô; API trả số tiền dạng chuỗi chính xác, export từ backend; browser không kết nối trực tiếp DB.
- [ ] **W01-06 — Kiểm luồng, lưu minh chứng và soạn phần Word/slide tuần 1.** (2 giờ)
  - Xong khi: Có run thật, ảnh bảng/nguồn và bảng lỗi; ghi mức tự động/assisted và giờ thực; slide demo UC-1, không trình bày lại tổng quan đề tài.

**Đầu ra cần lưu:**

- Paddle adapter và lock sau khi chạy qua, tái sử dụng render/download
- Một BCTC năm + sáu ô tham chiếu + DB/candidate/review mẫu
- Màn hình UC-1, CSV và week-01.md

**Tiêu chí chuyển mốc:** Cuối tuần 1 có UC-1 cơ bản cho một BCTC năm; Paddle là thay đổi trong luồng đã thử, không là một đợt nghiên cứu công cụ tách riêng.

**Khi vướng/chậm:** Timebox đổi Paddle khoảng 2 giờ ban đầu; nếu chưa chạy, ghi lỗi và xử lý trong giờ dự phòng/core, vẫn làm kho/bảng bằng số duyệt thủ công. Không báo số nhập tay là Paddle đã trích.

**Yêu cầu liên quan:** FR01, FR03, FR05, FR08, FR10, FR12, IR01, IR02, NFR07, NFR08, DR03, DR04, FR02, FR09, FR11, FR15, FR16, FR17, FR31, DR01, DR02, IR03, IR04.

**Ca kiểm cần thực hiện:** TC01, TC02, TC03, TC06, TC08, TC10, TC11, TC23, TC24. Đây là phân bổ kế hoạch, chưa phải kết quả pass.

**Gợi ý nội dung Word:**

1. UC-1 nhỏ: một BCTC năm, sáu trường kế thừa bảng dữ liệu Báo cáo 2, kỳ/scope. Mẫu thử cũ là ba dòng × hai cột; tải/đọc/render được tái sử dụng, chỉ thay engine OCR.
2. Luồng đã ghép: text/Paddle→candidate→duyệt→PostgreSQL→bảng/nguồn/CSV. Gắn ảnh bảng, một ô nguồn và log engine.
3. Bảng số ô đúng/sai/thiếu trước và sau duyệt nếu đã đo; lỗi còn lại, phần nhập tay và ba việc tuần 2. Chưa đo thì ghi chưa đo.

**Gợi ý slide ngắn:**

1. UC-1 tuần này: một báo cáo vào, bảng sáu chỉ tiêu có nguồn ra.
2. Một sơ đồ ngắn: pipeline cũ giữ lại, bước OCR đổi Paddle.
3. Ảnh hoặc demo trực tiếp bảng→ô số→trang nguồn→CSV.
4. Kết quả đã chạy, lỗi cần xử lý và đầu ra tuần 2.

**Demo:** Chọn báo cáo năm→xem một ô đã duyệt→mở trang/cột nguồn→xuất CSV; chỉ vị trí Paddle trong run log.

**Điểm trao đổi với thầy:** Luồng khai thác này đã đủ cơ bản cho UC-1 chưa; cần ưu tiên cải thiện trích số hay cách tra cứu nguồn?

### Tuần 02 — Củng cố UC-1, mở dữ liệu nhiều kỳ cho UC-2

**UC:** UC-1; chuẩn bị UC-2 · **Giờ dự toán:** 22

**Đầu vào:** UC-1 một báo cáo đã có từ tuần 1; lỗi thực và ledger mẫu chính.

- [ ] **W02-01 — Hoàn thiện schema, ràng buộc, transaction và revision từ DB tối thiểu.** (5 giờ)
  - Xong khi: Không dựng lại từ đầu; Alembic migration, NUMERIC/FK/unique, rollback và revision; pg_dump/pg_restore mẫu DB.
- [ ] **W02-02 — Mở parser sáu trường cho báo cáo của các mã/kỳ tiếp theo.** (4 giờ)
  - Xong khi: Dùng fixture development; xử lý nhãn/cột/đơn vị khác mẫu đầu; một ô chưa trích được được giữ missing/ambiguous, không giả tự động.
- [ ] **W02-03 — Hoàn thiện hàng đợi duyệt và các kiểm tra số liệu.** (5 giờ)
  - Xong khi: React review gọi API; blocking không publish; warning có lý do; revision conflict HTTP 409, không ghi đè lần duyệt khác.
- [ ] **W02-04 — Bổ sung ba năm công ty đầu, bảng nhiều kỳ và CSV.** (5 giờ)
  - Xong khi: React giữ bộ chọn; FastAPI trả coverage/facts, CSV cùng bộ lọc; phân biệt current/comparative/revision và hiện thiếu rõ.
- [ ] **W02-05 — Kiểm tải lại, raw version và chạy tiếp sau lỗi.** (2 giờ)
  - Xong khi: 304/cùng hash không nhân raw; lỗi một file không phá file khác; nhập tay có acquisition_mode=assisted.
- [ ] **W02-06 — Báo cáo tiến độ đợt 1 và lưu demo UC-1.** (1 giờ)
  - Xong khi: Demo PDF→candidate→duyệt→bảng→nguồn→CSV; ghi đúng phần tự động/phần thủ công, giờ thực và lỗi.

**Đầu ra cần lưu:**

- DB/review đã củng cố và fixture bố cục khác
- Bảng nhiều kỳ của công ty đầu, CSV và audit
- week-02.md + ảnh/video ngắn/log chạy

**Tiêu chí chuyển mốc:** UC-1 ổn định hơn trên dữ liệu nhiều kỳ; có bộ số đã duyệt để tuần 3 làm UC-2, không đợi kiểm công cụ lại.

**Khi vướng/chậm:** Không đợi parser đạt độ chính xác cao ở mọi bố cục. Cho nhập/sửa có nguồn để hoàn thành luồng và đo công sức.

**Yêu cầu liên quan:** FR02, FR06, FR07, FR09, FR11, FR14, FR15, FR16, FR17, FR18, FR33, FR31, DR01, DR02, DR05, DR06, IR03, IR04, NFR01, NFR03, BR01, BR02, BR03, BR12.

**Ca kiểm cần thực hiện:** TC04, TC05, TC06, TC07, TC10, TC11, TC12, TC23, TC24, TC27. Đây là phân bổ kế hoạch, chưa phải kết quả pass.

**Gợi ý nội dung Word:**

1. Phần cải thiện so tuần 1: bố cục/kỳ nào đã xử lý; bảng ledger số báo cáo/ô đã duyệt và còn thiếu. Rà 18 targets của ba năm công ty đầu, không đồng nhất targets với số hợp lệ.
2. Một ca sai cột/đơn vị hoặc bản sửa: candidate→issue→sửa/duyệt→audit; kiểm chạy lại không nhân dữ liệu.
3. Bảng nhiều kỳ công ty đầu, định nghĩa sáu metrics từ Báo cáo 2 và dữ liệu dùng cho UC-2. Gộp tuần 1 vào báo cáo hai tuần; phần tự động và assisted ghi riêng.

**Gợi ý slide ngắn:**

1. UC-1 từ một báo cáo sang nhiều kỳ: kết quả tăng thêm.
2. Một lỗi dữ liệu thật và cách xử lý có audit.
3. Demo bảng nhiều kỳ→nguồn→xuất dữ liệu.
4. Coverage hiện tại và kế hoạch biểu đồ/tỷ số tuần 3.

**Demo:** Mở bảng ba năm; sửa một candidate có nguồn, kiểm bản trước/sau; chạy lại không nhân bản.

**Điểm trao đổi với thầy:** Định nghĩa sáu trường, cách hiển thị thiếu và phạm vi báo cáo đã phù hợp chưa?

### Tuần 03 — UC-2: biểu đồ, tỷ số và lưu phân tích

**UC:** UC-2 · **Giờ dự toán:** 18

**Đầu vào:** Kho số đã duyệt; bổ sung hai năm còn lại của công ty đầu bằng nguồn đúng scope.

- [ ] **W03-01 — Viết engine delta/growth, CFO/LNST, tiền/tài sản và nợ phải trả/tài sản.** (4 giờ)
  - Xong khi: Chỉ dùng reviewed operands; nền tăng trưởng≤0, thiếu năm, assets≤0/cross-scope trả lý do; CFO âm được giữ.
- [ ] **W03-02 — Dựng bảng và biểu đồ LNST/CFO theo năm.** (5 giờ)
  - Xong khi: React vẽ từ API phân tích; nhãn/trục/đơn vị, không nối số thiếu; kiểm số chính xác ở bảng bên cạnh biểu đồ.
- [ ] **W03-03 — Gắn công thức, nguồn và lưu/mở lại lần phân tích.** (5 giờ)
  - Xong khi: API lưu/mở snapshot PostgreSQL; React mở operands/nguồn; bản dữ liệu mới không đổi snapshot đã lưu.
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

**Gợi ý nội dung Word:**

1. Câu hỏi người dùng: lợi nhuận tăng có đi cùng CFO không? Nêu kỳ/scope và các số đã duyệt.
2. Đầu vào→công thức có điều kiện→bảng/biểu đồ; một ca mẫu số 0/âm hoặc thiếu năm và cách hiển thị.
3. Một nhận xét từ số thật, nguồn operands, snapshot mở lại và giới hạn diễn giải; chuẩn bị dữ liệu so sánh.

**Gợi ý slide ngắn:**

1. UC-2 trả lời câu hỏi LNST–CFO của công ty nào/kỳ nào.
2. Biểu đồ thực tế và nhận xét ngắn gắn hai số.
3. Một tỷ số: công thức, nguồn và điều kiện không tính.
4. Demo lưu/mở lại; bước tiếp theo là so sánh công ty.

**Demo:** Chọn công ty/giai đoạn→xem biểu đồ→mở công thức/nguồn CFO-LNST→lưu và mở lại nhận xét.

**Điểm trao đổi với thầy:** Bảng/biểu đồ đã giúp đọc biến động rõ chưa; nên phân rã khoản nào khi CFO thay đổi?

### Tuần 04 — UC-3 và demo cơ bản ba UC đầu

**UC:** UC-1/2/3 · **Giờ dự toán:** 18

**Đầu vào:** UC-1/2 dùng được; số đã duyệt của doanh nghiệp thứ hai, tối thiểu một năm trùng với công ty đầu.

- [ ] **W04-01 — Thu và duyệt dữ liệu doanh nghiệp thứ hai.** (4 giờ)
  - Xong khi: Ít nhất một năm chung, sáu trường có số đã duyệt hoặc lý do thiếu; giữ scope cùng cơ sở.
- [ ] **W04-02 — Viết truy vấn và engine so sánh doanh nghiệp tự chọn.** (4 giờ)
  - Xong khi: Chọn hai mã/kỳ; chuẩn hóa đơn vị; tái dùng công thức UC-2; khác scope hoặc thiếu operand không tạo so sánh giả.
- [ ] **W04-03 — Dựng bảng/biểu đồ cạnh nhau và giải thích giới hạn.** (4 giờ)
  - Xong khi: React gọi API compare, đối chiếu LNST/CFO/tỷ số và nguồn; không xếp hạng/sàng lọc hay gọi nhóm khác ngành là benchmark ngành.
- [ ] **W04-04 — Nối luồng tra cứu→phân tích→so sánh→lưu/xuất.** (3 giờ)
  - Xong khi: React điều hướng ba UC, dùng chung bộ chọn và API; error/empty/loading không làm hiện dữ liệu kỳ cũ.
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

**Gợi ý nội dung Word:**

1. Mốc demo ba UC: bảng từng UC gồm input, xử lý, output và đường dẫn minh chứng thực chạy.
2. Ca so sánh hai công ty cùng kỳ/scope: số tuyệt đối, tỷ số, biểu đồ và một trường hợp không đủ cơ sở.
3. Kết quả walkthrough, phần tự động/assisted, lỗi còn lại; tuần 5 mở HPG/VNM/FPT. So sánh khác ngành chưa là benchmark.

**Gợi ý slide ngắn:**

1. Mốc tuần 4: những phần UC-1/2/3 đã chạy.
2. UC-1/2: bảng có nguồn và biểu đồ một công ty.
3. UC-3: bảng/biểu đồ hai công ty, cùng kỳ/phạm vi.
4. Demo liên thông ba UC và lỗi cần sửa ở tuần 5.

**Demo:** Tra cứu một số→phân tích xu hướng→chọn công ty thứ hai→so sánh→nguồn→lưu/xuất.

**Điểm trao đổi với thầy:** Ba UC đầu đã thể hiện đúng hướng nền tảng dữ liệu hỗ trợ phân tích chưa; thao tác nào cần đơn giản hơn?

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

**Gợi ý nội dung Word:**

1. Ma trận HPG/VNM/FPT×2023–2025: chín reports/54 targets, số đã duyệt/thiếu và lý do; không chỉ báo số PDF tải được.
2. Các lỗi parser/bộ chọn/phạm vi đã sửa từ demo tuần 4; minh chứng so sánh ba công ty.
3. Giờ thu/duyệt thực, tập kiểm giữ riêng và quyết định giữ phạm vi; dữ liệu còn thiếu ảnh hưởng chỉ tiêu nào.

**Gợi ý slide ngắn:**

1. Ba công ty đã dùng được ở mức nào: bảng coverage.
2. Một thay đổi quan trọng so demo tuần 4.
3. Demo nhóm ba mã và chỉ rõ dữ liệu thiếu.
4. Điều kiện chuyển sang cổ tức; không mở thêm phạm vi.

**Demo:** Chuyển HPG/VNM/FPT và năm; so sánh nhóm; mở một số/thiếu có lý do; lưu cấu hình.

**Điểm trao đổi với thầy:** Phần core đã đủ để ưu tiên hồ sơ cổ tức chưa; cần sửa lỗi nào trước khi thêm UC-5?

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

**Gợi ý nội dung Word:**

1. Câu hỏi UC-5: mỗi khoản cổ tức thuộc năm lợi nhuận nào, ở trạng thái nào? Nêu nguồn và cửa sổ đã tra cứu.
2. Một notice hỗn hợp hoặc bản sửa: tách components/quan hệ old-current; phân biệt lịch trả và đã trả.
3. Timeline và coverage; annual DPS được tính/chặn thế nào; thiếu discovery FR04 hoặc phần assisted báo riêng.

**Gợi ý slide ngắn:**

1. UC-5: lịch sử cổ tức cần đọc theo năm lợi nhuận.
2. Một thông báo→components và trạng thái có nguồn.
3. Demo timeline/lịch sử và một ca sửa/hủy.
4. Dữ liệu chưa đủ và kế hoạch phân tích cơ sở tiền mặt.

**Demo:** Mở notice→thành phần theo năm→bản sửa nếu có→timeline; hiện nguyên nhân annual chưa được tính.

**Điểm trao đổi với thầy:** Cách phân biệt công bố/lịch trả/thực chi và độ đầy đủ lịch sử đã rõ chưa?

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

**Gợi ý nội dung Word:**

1. Ca thật trong ba mã: LNTT, các dòng cầu nối và CFO; nguồn từng dòng, subtotal/leaf và residual.
2. CFO−CAPEX−khoản chi: định nghĩa khoản chi, công thức, scope và số tiền; nguồn gộp phải gọi đúng tên.
3. Nhận xét/câu hỏi người dùng từ kết quả, giới hạn không suy FCFE hay cổ tức tương lai; điều kiện thiếu operands.

**Gợi ý slide ngắn:**

1. Vấn đề ca thật: lợi nhuận và tiền thay đổi ra sao.
2. Biểu đồ cầu nối CFO với khoản đóng góp chính.
3. Bảng bao phủ khoản chi, công thức và nhãn khoản chi.
4. Demo truy nguồn; điều kết quả cho phép và chưa cho phép kết luận.

**Demo:** Chọn ca→cầu nối CFO→một dòng nguồn→bao phủ→operands→lưu câu hỏi đọc thêm.

**Điểm trao đổi với thầy:** Cách giải thích cơ sở tiền mặt của khoản phân phối đã đúng nghiệp vụ và hữu ích chưa?

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

**Gợi ý nội dung Word:**

1. Sự kiện vốn và basis DPS: DPS gốc/chuỗi tham chiếu được phép tính, nguồn ngày hiệu lực, ca bị chặn.
2. Kết quả OCR cùng tập trang/ô: đúng/sai/thiếu, nhầm cột/đơn vị, thời gian; B0/B1/B2 và tự/độc lập kiểm khai rõ.
3. Hồ sơ UC-5 xuất/replay, ma trận bốn UC ưu tiên, phần còn thiếu và quyết định feature freeze.

**Gợi ý slide ngắn:**

1. Vì sao vẫn giữ sự kiện cổ phiếu trong phân tích tiền mặt.
2. DPS gốc/tham chiếu hoặc lý do chặn từ một ca có nguồn.
3. Kết quả Paddle–Tesseract bằng số đếm và giới hạn mẫu.
4. Demo hồ sơ cổ tức lưu/mở lại; trạng thái core trước tuần 9.

**Demo:** Xem basis của một chuỗi→kết quả hoặc lý do chặn→hồ sơ→export→replay đúng phiên bản.

**Điểm trao đổi với thầy:** Điều kiện so sánh DPS và thiết kế đo OCR đã đủ thuyết phục; phần nào cần công bố giới hạn rõ hơn?

### Tuần 09 — Ổn định hệ thống; UC-4 có điều kiện

**UC:** Kiểm hệ thống; UC-4 sau gate · **Giờ dự toán:** 17

**Đầu vào:** Feature freeze tuần 8; ma trận các yêu cầu còn thiếu và bộ demo bốn UC.

- [ ] **W09-01 — Rà toàn bộ yêu cầu/ca kiểm hiện hành và sửa lỗi trọng yếu.** (3 giờ)
  - Xong khi: 91 mã/51 TC có owner/mốc/status/evidence; yêu cầu chưa đạt giữ fail/not_run hoặc có CR, không đổi thành pass.
- [ ] **W09-02 — Backup/restore DB, raw, config và snapshots vào thư mục sạch.** (5 giờ)
  - Xong khi: pg_dump/pg_restore cùng raw/config/migration; hash/revision khớp và replay snapshot; không copy data directory đang chạy làm backup.
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

**Gợi ý nội dung Word:**

1. Kiểm backup→restore→replay: file/hash/revision và kết quả thật; hiệu năng ghi đúng cấu hình/bộ kiểm.
2. Walkthrough tác vụ: thời gian/lỗi với đọc PDF thủ công, người thử và giới hạn mẫu; không khẳng định tăng lợi nhuận đầu tư.
3. UC-4 có làm/hoãn theo gate; nếu làm, mô tả danh sách tự chọn/công bố/old-new; danh sách lỗi trước nộp.

**Gợi ý slide ngắn:**

1. Core ổn định: những kiểm tra đã chạy và còn thiếu.
2. Minh chứng restore/replay hoặc kết quả hiệu năng.
3. Walkthrough và UC-4 tối thiểu nếu đã làm.
4. Các lỗi cuối và quyết định ưu tiên trước nộp.

**Demo:** Restore một gói→mở snapshot; nếu UC-4 đã chạy thì mở cập nhật sang phân tích, nếu chưa thì báo hoãn.

**Điểm trao đổi với thầy:** Những giới hạn nào cần ghi vào báo cáo cuối; còn lỗi nào chặn nghiệm thu?

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

**Gợi ý nội dung Word:**

1. Kết quả theo UC: chỉ phần đã chạy, đầu vào/xử lý/đầu ra và ba case HPG/VNM/FPT có bằng chứng.
2. Phương pháp và kết quả kiểm: coverage, OCR, công sức, replay/restore và pass/fail/not_run từng yêu cầu; giả định/tập kiểm riêng.
3. Hướng dẫn chạy, phạm vi/giới hạn, chức năng hoãn và nghiên cứu tốt nghiệp đề xuất; không lặp toàn bộ thư viện khảo sát.

**Gợi ý slide ngắn:**

1. Kết quả sản phẩm và phạm vi đã chốt.
2. Demo UC-1→UC-2→UC-3 trên dữ liệu thật.
3. Demo UC-5: lịch sử, cơ sở tiền mặt/basis và nguồn.
4. Một bảng số đo chính; giới hạn/chưa đạt và hướng tiếp theo.

**Demo:** Kịch bản liền mạch 5–7 phút với dữ liệu đã lưu; có bản backup và ảnh/log thật nếu nguồn mạng không sẵn.

**Điểm trao đổi với thầy:** Xác nhận kết quả, phạm vi chưa đạt và phần nên phát triển tiếp; không tự ghi đã được thầy phê duyệt.

## Đánh giá và kiểm soát phạm vi

Kế hoạch phân bổ 91 yêu cầu hiện hành/51 ca kiểm SRS; không tái đưa FR29/FR30/D09/D10 hoặc sàng lọc dưới tên cảnh báo. Phần bổ sung tương tác biểu đồ/so sánh nhóm F03 có tiêu chí riêng trong tuần 1/4/5, chưa biến toàn danh mục 38 chức năng thành phạm vi nghiệm thu. E05/E10/nhiều ca và các yêu cầu D có điều kiện phải ghi trạng thái kích hoạt/not_applicable có lý do, không mặc định đã đạt.

Freeze lineage trước đo: bản dịch/cột so sánh/bản sửa gần giống không nằm hai phía development/holdout. Cỡ pilot nhỏ thì báo số đếm thật và giới hạn; người tự xây gold phải ghi tự kiểm. Không gọi tập đã chỉnh parser để khớp là tập kiểm độc lập. Đo Paddle–Tesseract trên cùng trang/ô và khai cấu hình; không đổi quyết định OCR thành tuyên bố ưu thế chưa đo.

TC30 yêu cầu bộ tải 24 báo cáo/144 targets/≤200 notices theo SRS, khác mẫu nghiên cứu chín báo cáo. Có thể chuẩn bị bộ kiểm tải riêng nhưng phải ghi nguồn/synthetic, không nhân bản thành corpus nghiên cứu. Không đủ đúng bộ kiểm thì TC30 chưa đạt hoặc cần CR; không báo đo pilot nhỏ là đạt TC30.

Mỗi task chỉ tick khi có đầu ra và bằng chứng đúng tiêu chí. Mỗi TC ghi input/expected/actual, code/config version, pass/fail/not_run, người/ngày và đường dẫn. Nhật ký mỗi tuần: giờ thực, file/run, số đã duyệt/thiếu, lỗi và việc chuyển tuần. Tuần 9 làm UC-4 chỉ khi lỗi core đã xử lý; nếu chưa đạt, dùng giờ đó sửa UC-1/2/3/5 và ghi UC-4 hoãn.

Kết thúc tuần 10: tổng hợp phần đã chạy, phần chưa đạt và dữ liệu chưa đầy đủ. Tất cả yêu cầu M phải có bằng chứng đạt hoặc change record được chấp nhận; checklist/tài liệu không thay nghiệm thu. Trình bày theo UC nhỏ, đầu vào→xử lý→đầu ra→minh chứng; ưu tiên demo và số đo thay tổng quan lý thuyết.
