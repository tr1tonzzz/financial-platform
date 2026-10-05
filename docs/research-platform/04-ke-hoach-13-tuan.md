# Kế hoạch thực hiện 13 tuần — v3 theo SRS v3.1

Cập nhật 05/10/2026 theo hướng lợi nhuận→chuyển thành tiền→đối chiếu cổ tức. CR-PCD-01/mục15 SRS thêm cầu nối LNTT→CFO tối thiểu một ca, mục tiêu1–3 theo gate; 83 mã yêu cầu/42 tình huống dự kiến. Giữ 78 việc, bổ sung tiêu chí cầu nối trong việc WNN-05. E05/E10 chỉ áp dụng khi có quyết định kích hoạt.

Quỹ nền143 giờ + cầu nối tối thiểu24 giờ =167 giờ dự toán (12–15giờ/tuần tùy tuần), chưa được người thực hiện xác nhận. Nghiên cứu ước lượng24–40 giờ;24 là mức thấp phải đo lại G4. Nếu thời gian thực chỉ10–12giờ/tuần thì cần phân bổ lại/lùi hạn hoặc CR giảm phạm vi, không coi quỹ mới nằm trong143giờ. Ưu tiên một ca trước mở5–8 doanh nghiệp; không đồng thời mở mọi chiều sâu. B5 là giờ thêm, không lấy dự phòng nền. Phần giả định nền bên dưới được giữ để đối chiếu.

Cập nhật 04/10/2026. Một người, 10–12 giờ/tuần; cơ sở 11 giờ × 13 = 143 giờ gồm học, code, kiểm, báo cáo và dự phòng. Tuần tính từ ngày bắt đầu thật, chưa mặc định đủ 13 tuần học kỳ. Các đầu ra là mục tiêu tương lai, không phải tiến độ đã đạt.

Nguồn đồng bộ: [SRS v3.1](22-srs-dac-ta-yeu-cau-phan-mem.md) → [JSON kế hoạch](checklist-13-tuan.json) → tài liệu này và [checklist HTML](checklist-13-tuan.html). Đọc [hướng dẫn bắt đầu/mẫu minh chứng](23-bat-dau-va-minh-chung-thuc-hien.md) trước buổi 1. Tài liệu 02 giữ P/US/PF/AN; kế hoạch 16 tuần/A1 cũ không áp dụng.

## 1. Kết quả rà soát và cách dùng

Bản trước có khung tuần/nhịp báo cáo nhưng thiếu phân bổ SRS, output paths, replay mọi kết quả, restore, benchmark và local safety; còn quy tắc/hướng tốt nghiệp cũ. V3 kế thừa các phần này, làm rõ freeze holdout trước đo. Version/cache nền làm từ tuần 2, tuần 10 hoàn thiện replay.

Mỗi tuần có đầu vào/phụ thuộc, 6 việc WNN-01…WNN-06, đầu ra, TC và tiêu chí xong. Làm theo thứ tự; ghi giờ/bằng chứng/lỗi cuối tuần. Phụ thuộc chưa đạt thì task liên quan pending, có thể làm việc độc lập. Báo cáo thật ở tuần 2/4/6/8/10/12; tuần 13 tổng kết theo mẫu trường. Không tạo bảy bộ tiến độ giả.

**Môi trường đã kiểm:** Python/venv hiện có 3.14.7, SRS chọn 3.12. Tuần 1 chuẩn bị interpreter/.venv-fap riêng hoặc xử lý CR trước freeze, không xóa venv cũ. src chưa có MVP, prototype chưa thu đủ 2023–2025. Module/file đầu ra dưới đây là vị trí dự kiến cần tạo khi làm.

## 2. Gate và ngân sách mở rộng

| Mốc | Điều kiện / quyết định | Khi chưa đạt |
|---|---|---|
| G2 cuối tuần 2 | Một issuer: danh mục→raw→candidate→review, rà discovery hai loại | Thử IR thay thế, ghi lỗi/assisted, xử lý tuần 3; assisted không pass FR04 |
| G4 cuối tuần 4 | Pilot 9 báo cáo/54 targets có ledger/review, effort và quyết định mẫu | Giữ 3 issuers, không mặc định mở 24 báo cáo |
| G8 đầu tuần 8 | Freeze scope/gold/split/config/hash, backup trước baseline | Chưa freeze thì chưa đo độc lập; ghi giới hạn |
| G11 cuối tuần 11 | Feature freeze, yêu cầu/TC có trạng thái và lỗi ưu tiên | Chỉ sửa lỗi/minh chứng; M chưa đạt cần sửa hoặc CR được chấp nhận |
| Cuối tuần 13 | Clean setup/bundle/replay/restore, báo cáo/deck/app thống nhất | Không gọi hoàn tất phép chưa chạy |

G4 ước lượng effort tăng thêm = BCTC thêm × phút xử lý/review + notices thêm × phút/notice + sửa adapter + rà coverage. Dùng mức cao đã quan sát. Quỹ dữ liệu mở rộng tối đa 6 giờ tuần 7 + ≤2 giờ dự phòng tuần 8 trước G8; không lấy giờ baseline/report/restore tăng mẫu. Vượt quỹ hoặc discovery còn lỗi thì giữ pilot. Giảm nghĩa vụ M cần CR, không tự đổi status thành pass.

TBD01 rubric/hạn/phê duyệt: tuần 1–2; TBD02 issuer/scope/nguồn/policy: trước G4; TBD03 gold/holdout/checker: trước G8; TBD04 máy/dependencies/ngưỡng: trước benchmark tuần 11; TBD05 mapping/basis/tolerance: trong pilot trước duyệt; TBD06 walkthrough/effort: thiết kế trước đo, kiểm tuần 5/12. Ghi decisions thật, chưa có phản hồi thì pending.

## 3. Tổng quan và giờ

Cột giờ: học / code / kiểm / báo cáo / dự phòng. Phát sinh phải ghi giờ thật và phân bổ lại tại gate.

| Tuần | Trọng tâm | Phụ thuộc | Giờ H/C/K/B/D | Báo cáo |
|---|---|---|---|---|
| 1 | Chuẩn bị môi trường, chốt pilot và đọc nguồn | Không | 2,5/5/1/1,5/1 +1 cầu nối | Nhật ký |
| 2 | Discovery và tải có kiểm soát; luồng nhỏ đầu tiên | 1 | 2,5/5/1/1,5/1 +1 cầu nối | Đợt 1 |
| 3 | Trích PDF/OCR và dựng pilot 9 báo cáo | 2 | 2,5/5/1/1,5/1 +1 cầu nối | Nhật ký |
| 4 | SQLite, validation, review và quyết định cỡ mẫu | 3 | 2/5/1,5/1,5/1 +2 cầu nối | Đợt 2 |
| 5 | Ứng dụng một doanh nghiệp và công thức lõi | 4 | 2,5/5/1/1,5/1 +3 cầu nối | Nhật ký |
| 6 | Vòng đời cổ tức, coverage và DPS năm | 4,5 | 2,5/5/1/1,5/1 +4 cầu nối | Đợt 3 |
| 7 | Dataset theo gate và chuẩn bị holdout | 6 | 2/5,5/1/1,5/1 +3 cầu nối | Nhật ký |
| 8 | Freeze holdout và đo chất lượng thực tế | 7 | 1/4/3/2/1 +2 cầu nối | Đợt 4 |
| 9 | Bộ lọc, Spearman và ba case thật | 5,6,8 | 2,5/5/1/1,5/1 +2 cầu nối | Nhật ký |
| 10 | Snapshot đầy đủ, replay offline và cập nhật | 2,4,6,9 | 2,5/5/1/1,5/1 +2 cầu nối | Đợt 5 |
| 11 | Khôi phục, hiệu năng, an toàn local và freeze | 8,10 | 1/3/4/2/1 +1 cầu nối | Nhật ký |
| 12 | Nghiệm thu thử, báo cáo và luyện bảo vệ | 9,10,11 | 1/1/2/6/1 +1 cầu nối | Đợt 6 |
| 13 | Môi trường sạch, đóng gói và nộp cuối | 12 | 0,5/2/3/3,5/2 +1 cầu nối | Cuối |

## 4. Công việc và tiêu chí từng tuần

### Tuần 01 — Chuẩn bị môi trường, chốt pilot và đọc nguồn

**Học đúng task:** Python file/dict/JSON, Git; sáu chỉ tiêu, flow/stock, scope và profit_year. Đọc tài liệu 18 theo phần cần dùng.

**Đích tuần:** Môi trường project được ghi phiên bản; một BCTC và một notice đọc tay, có ledger pilot và danh sách TBD.

**Đầu vào:** SRS v3.1; hướng dẫn bắt đầu ở tài liệu 23; các bằng chứng nghiên cứu hiện có, không phải app đã hoàn thành.

**Việc thực hiện:**

- **W01-01:** Kiểm tra Python: máy hiện có Python 3.14.7; chuẩn bị Python 3.12 theo SRS và môi trường .venv-fap riêng, ghi lệnh/phiên bản; không xóa venv cũ.
- **W01-02:** Chọn ba doanh nghiệp ứng viên phi tài chính; HPG/DHG/VHC là điểm xuất phát từ prototype, phải xác nhận BCTC 2023–2025, scope và nguồn cổ tức trước chốt. Ghi rubric/hạn thực/TBD01–TBD06.
- **W01-03:** Đọc một BCTC năm kiểm toán; nhập sáu targets với giá trị gốc, đơn vị, kỳ, scope, trang và locator; thiếu ghi missing, không thay 0.
- **W01-04:** Đọc một notice tiền mặt; tách profit_year/components, giữ published/first_seen/lịch trả khác nhau; paid chỉ khi có bằng chứng.
- **W01-05:** Tạo scope manifest 9 report targets và ledger 54 metric targets; tự viết JSON candidate và một quyết định review có trước–sau/lý do. Đây là nhập tay có nguồn. Bổ sung v3: Chọn ca cầu nối gián tiếp, đọc LNTT/rows/role/locator; phân biệt LNST và LNTT.
- **W01-06:** Lưu nhật ký, giờ thực và kiểm TC01/TC08 mức ban đầu; giải thích LNST khác CFO, năm lợi nhuận khác năm công bố; chuẩn bị danh sách câu hỏi cho thầy.

**Nhịp buổi đề xuất** (cộng giờ dự phòng của tuần):

- B1: 2,5 h học và kiểm môi trường, mở BCTC mẫu.
- B2: 3 h đọc/nhập BCTC và notice.
- B3: 3 h tạo manifest/ledger, review JSON và đối chiếu nguồn.
- B4: 1,5 h nhật ký, tự giải thích và câu hỏi phạm vi.
- B5: 1h bổ sung cầu nối — Chọn ca cầu nối gián tiếp, đọc LNTT/rows/role/locator; phân biệt LNST và LNTT.

**Đầu ra phải lưu** (từ repo, tạo khi làm):

- config/pilot.json; docs/research-platform/execution/environment.md, decisions.md (tạo khi thực hiện).
- data-sets/fap/pilot/{expected-reports.csv,expected-targets.csv,manual-gold.csv,manual-events.json,candidates.json,review-decisions.json}.
- docs/research-platform/execution/week-01.md với nguồn, lệnh thực chạy và điểm còn thiếu.
- docs/research-platform/execution/bridge-week-01.md: rows/manifest/expected-actual/giờ/decision phù hợp task (tạo khi làm).

**Yêu cầu SRS:** FR01, FR02, DR04, DR05, BR01, BR02, BR03, BR04, BR08, E01, E06.

**Kiểm chứng:** TC01, TC08, P04, P05; dùng input/expected mục 10 và 15 SRS, lưu actual/evidence.

**Xong khi:** Có 9 report targets/54 metric targets, một mẫu đọc tay truy nguồn được và môi trường Python đã xác nhận. Chưa có 3.12 thì bước môi trường pending, không nghiệm thu trên phiên bản khác âm thầm. Cầu nối: Chọn ca cầu nối gián tiếp, đọc LNTT/rows/role/locator; phân biệt LNST và LNTT. Chưa thực hiện ghi pending; E05/E10 chưa kích hoạt ghi not_applicable có quyết định.

### Tuần 02 — Discovery và tải có kiểm soát; luồng nhỏ đầu tiên

**Học đúng task:** HTTP, selector/urljoin, hash, status/error, retry và conditional GET; prototype còn filter FY2025/H1-2026.

**Đích tuần:** Danh mục tới raw thật; một BCTC và một notice tới dữ liệu đã đối chiếu, tách assisted khỏi discovery.

**Đầu vào:** Manifest tuần1; crawler và test offline hiện có; source policies chưa rõ phải kiểm.

**Việc thực hiện:**

- **W02-01:** Chạy regression crawler offline trước sửa; đọc classify/main, đưa issuer/year/window/budget ra config thay filter cố định. Không chạy lại script sinh bộ nghiên cứu để ghi đè tài liệu.
- **W02-02:** Hoàn thiện ít nhất một adapter BCTC tự phát hiện từ danh mục/search, phân trang có cap; lưu đường discovery và kiểm FY2023–2025 từ nội dung tài liệu.
- **W02-03:** Thử một adapter notice chính thức từ danh mục/search theo issuer/window; nếu VSDC không dùng được, thử IR hợp lệ. URL từng notice không chứng minh discovery.
- **W02-04:** Lưu raw/hash/version/HTTP validators và acquisition_mode; kiểm HTML giả PDF, timeout, 404/429/503, giới hạn file, retry/backoff/policy skip.
- **W02-05:** Kiểm 200/304/hash không đổi/hash đổi, cache lỗi và interruption/resume; dùng JSON review tuần1 cho luồng nhỏ trước khi SQLite tuần4; giữ raw cũ. Bổ sung v3: Chép/duyệt rows một ca DHG có source, subtotal/leaves; ghi giờ nhập và thiếu.
- **W02-06:** Lưu bằng chứng TC02–TC05, quyết định gate G2 và báo cáo đợt1. Nêu luồng nào tự phát hiện, luồng nào còn assisted và kế hoạch xử lý tuần3.

**Nhịp buổi đề xuất** (cộng giờ dự phòng của tuần):

- B1: 2,5 h học HTTP, đọc prototype và chạy regression.
- B2: 3 h discovery BCTC/notice và config.
- B3: 3 h version/cache/resume, kiểm lỗi và luồng nhỏ.
- B4: 1,5 h báo cáo đợt1 và quyết định G2.
- B5: 1h bổ sung cầu nối — Chép/duyệt rows một ca DHG có source, subtotal/leaves; ghi giờ nhập và thiếu.

**Đầu ra phải lưu** (từ repo, tạo khi làm):

- data-sets/fap/runs/w02-<run_id>/ và raw/ có logs, hashes và config thực tế.
- docs/research-platform/execution/week-02.md; decisions.md ghi G2.
- docs/research-platform/reports/dot-01-tuan-01-02/{bao-cao.docx,tien-do.pptx,notes.md} chỉ tạo từ kết quả thật.
- docs/research-platform/execution/bridge-week-02.md: rows/manifest/expected-actual/giờ/decision phù hợp task (tạo khi làm).

**Yêu cầu SRS:** FR03, FR04, FR05, FR06, FR07, FR08, IR01, IR02, NFR07, BR06, E02, E09.

**Kiểm chứng:** TC02, TC03, TC04, TC05, P02, P11; dùng input/expected mục 10 và 15 SRS, lưu actual/evidence.

**Xong khi:** Có đường discovery thật cho mỗi loại nguồn hoặc ghi rõ loại chưa đạt; TC03–TC05 có expected/actual. Một cặp BCTC+notice có reviewed output/provenance JSON, không chỉ download. Cầu nối: Chép/duyệt rows một ca DHG có source, subtotal/leaves; ghi giờ nhập và thiếu. Chưa thực hiện ghi pending; E05/E10 chưa kích hoạt ghi not_applicable có quyết định.

**Gate:** G2: nguồn→raw→candidate→review chạy trên một issuer. Discovery notice chưa đạt phải có lỗi/nguồn thay thế/người phụ trách; assisted không pass FR04.

### Tuần 03 — Trích PDF/OCR và dựng pilot 9 báo cáo

**Học đúng task:** Text/layout/locator, OCR fallback, dấu âm, đơn vị, cột current/comparative và revision.

**Đích tuần:** 54 targets có candidate hoặc trạng thái thiếu; notices/components pilot có provenance.

**Đầu vào:** Collection tuần2, manifest9 reports; số nhập tay tuần1 làm development reference.

**Việc thực hiện:**

- **W03-01:** Thu BCTC năm2023–2025 của ba issuers; ghi mỗi report expected/published/found/downloaded/failed và lý do; xác nhận audited/scope từ tài liệu.
- **W03-02:** Trích text trước; chỉ OCR trang không đọc được. Ghi parser/OCR version, locator, raw value/unit, kỳ và scope cho từng candidate.
- **W03-03:** Chuẩn hóa six targets sang VND exact; giữ zero khác missing/ambiguous; kiểm dấu ngoặc, nghìn/triệu và LNST tổng khác cổ đông mẹ.
- **W03-04:** Trích nội dung chính notices thành components; năm lợi nhuận/basis chưa rõ giữ unresolved; published không bị thay bằng first_seen.
- **W03-05:** Dựng fixtures text/scan/current-comparative/scope/restated và notice hai năm; đối chiếu TC06–TC09. Không trộn fixture và case thật. Bổ sung v3: Thử extraction rows hoặc nhập tay có nhãn assisted; không thay discovery nền.
- **W03-06:** Ghi thiếu/sai, thời gian tự động và phút đọc/sửa riêng; lưu nhật ký tuần3 và hàng đợi review để tuần4 quyết định.

**Nhịp buổi đề xuất** (cộng giờ dự phòng của tuần):

- B1: 2,5 h học PDF/đơn vị và kiểm cột bằng tay.
- B2: 3 h financial extraction và OCR fallback.
- B3: 3 h event extraction/fixtures/provenance.
- B4: 1,5 h tổng hợp missing và effort.
- B5: 1h bổ sung cầu nối — Thử extraction rows hoặc nhập tay có nhãn assisted; không thay discovery nền.

**Đầu ra phải lưu** (từ repo, tạo khi làm):

- data-sets/fap/staging/{financial-candidates.json,event-candidates.json,issues.json} cùng provenance.
- data-sets/fap/evaluation/development/fixtures/ và effort.csv; ledger54 targets đầy đủ trạng thái.
- docs/research-platform/execution/week-03.md.
- docs/research-platform/execution/bridge-week-03.md: rows/manifest/expected-actual/giờ/decision phù hợp task (tạo khi làm).

**Yêu cầu SRS:** FR09, FR10, FR11, FR12, FR13, DR02, DR03, BR05, BR12, E01, E02.

**Kiểm chứng:** TC06, TC07, TC08, TC09, P04, P05; dùng input/expected mục 10 và 15 SRS, lưu actual/evidence.

**Xong khi:** Mỗi target có record/status; mọi candidate có raw version/locator và metadata bắt buộc hoặc issue blocking. TC06–TC09 có bằng chứng, không báo accuracy độc lập từ development. Cầu nối: Thử extraction rows hoặc nhập tay có nhãn assisted; không thay discovery nền. Chưa thực hiện ghi pending; E05/E10 chưa kích hoạt ghi not_applicable có quyết định.

### Tuần 04 — SQLite, validation, review và quyết định cỡ mẫu

**Học đúng task:** SQL keys/foreign keys, transaction, audit, revision và kiểm cân đối có tolerance.

**Đích tuần:** Reviewed store nhất quán; gate mở rộng dựa trên giờ thực của pilot.

**Đầu vào:** Candidates/raw/JSON audit từ tuần1–3; SRS data contracts; pilot ledger và effort.

**Việc thực hiện:**

- **W04-01:** Thiết kế ERD tối thiểu; triển khai SQLite gồm sources/versions, contexts, candidates/facts, events/components, coverage/issues/audit; nhập lại lịch sử JSON có provenance.
- **W04-02:** Thực hiện validation kỳ/unit/scope/nhãn và balance residual theo tolerance có version; thiếu operand trả not_checkable, không ép sửa số.
- **W04-03:** Tạo review tối thiểu xem nguồn cạnh số, approve/edit/reject; blocking không publish, warning cần lý do; audit trước–sau và operator local.
- **W04-04:** Kiểm transaction rollback, foreign keys, trùng logic/restated revisions và JOIN cardinality; pending/rejected không vào lớp phân tích chính thức.
- **W04-05:** Review pilot và coverage ledger; đo effort BCTC/notices/adapter; tính ngân sách mở rộng G4 và chốt3 hoặc5–8 issuers bằng decision record. Bổ sung v3: G4 đo công sức cầu nối; chốt quỹ167giờ hoặc CR/lùi hạn. Không tự giảm nghĩa vụ nền.
- **W04-06:** Chạy TC10–TC12/TC27, backup nhất quán đầu tiên; báo cáo đợt2 gồm ERD, lỗi, effort và CR nếu phải đổi yêu cầu discovery/phạm vi.

**Nhịp buổi đề xuất** (cộng giờ dự phòng của tuần):

- B1: 2 h SQL/schema/tolerance.
- B2: 3 h storage, revision và review.
- B3: 3,5 h kiểm transaction, review pilot và effort.
- B4: 1,5 h báo cáo đợt2/G4.
- B5: 2h bổ sung cầu nối — G4 đo công sức cầu nối; chốt quỹ167giờ hoặc CR/lùi hạn. Không tự giảm nghĩa vụ nền.

**Đầu ra phải lưu** (từ repo, tạo khi làm):

- data-sets/fap/store/fap.sqlite; data-sets/fap/backup/g4/ (dùng backup API, không copy DB đang ghi).
- docs/research-platform/execution/{schema.md,week-04.md,decisions.md}; G4 scope/config version.
- docs/research-platform/reports/dot-02-tuan-03-04/ và test-results.csv cập nhật.
- docs/research-platform/execution/bridge-week-04.md: rows/manifest/expected-actual/giờ/decision phù hợp task (tạo khi làm).

**Yêu cầu SRS:** FR14, FR15, FR16, FR17, FR18, DR01, DR06, DR07, NFR03, BR09, BR10, E09.

**Kiểm chứng:** TC10, TC11, TC12, TC27, P11; dùng input/expected mục 10 và 15 SRS, lưu actual/evidence.

**Xong khi:** Reviewed facts có source/locator; audit và dữ liệu commit/rollback cùng nhau; TC10–TC12/TC27 có expected/actual. G4 ghi cỡ mẫu, chi phí, nguồn thiếu và giờ còn lại. Cầu nối: G4 đo công sức cầu nối; chốt quỹ167giờ hoặc CR/lùi hạn. Không tự giảm nghĩa vụ nền. Chưa thực hiện ghi pending; E05/E10 chưa kích hoạt ghi not_applicable có quyết định.

**Gate:** G4: chỉ mở rộng khi nguồn hai loại đã chạy, pilot xử lý được và ước lượng dữ liệu tăng thêm nằm trong quỹ6 h tuần7+≤2 h dự phòng tuần8; giữ giờ cho SRS còn lại.

### Tuần 05 — Ứng dụng một doanh nghiệp và công thức lõi

**Học đúng task:** pandas joins/groupby/cardinality, Streamlit và hàm tính thuần; operands/formula version.

**Đích tuần:** UI sáu chỉ tiêu, coverage và tỷ số có nguồn; kiểm được từ kết quả về raw.

**Đầu vào:** Reviewed SQLite tuần4; fixture SRS; schema và các rule scope/kỳ.

**Việc thực hiện:**

- **W05-01:** Tách lớp store/query, analytics và UI; chọn issuer/year/scope, mặc định dữ liệu reviewed và hiển thị as_of.
- **W05-02:** Hiển thị six metrics và LNST/CFO cùng đơn vị; missing tạo khoảng trống, không nối comparison qua năm thiếu.
- **W05-03:** Cài delta/growth LNST, CFO/LNST khi LNST>0, cash/assets và liabilities/assets khi assets>0; kiểm kỳ/scope trước tính.
- **W05-04:** Mỗi kết quả có formula/version, operands và snapshot context; bấm mở raw PDF trang/HTML locator, không chỉ URL hiện hành.
- **W05-05:** Chạy TC18/TC19/TC23 và walkthrough: đọc scope/unit/coverage, xem lý do null; VND và DPS có trục/nhãn riêng. Bổ sung v3: Thiết kế bridge tables/mapping/roles, review/audit; chọn cặp năm nếu đủ quỹ.
- **W05-06:** Ghi card công thức, đoạn JOIN tự giải thích và nhật ký tuần5; chưa gọi tổng DPS đủ khi lifecycle tuần6 chưa xong.

**Nhịp buổi đề xuất** (cộng giờ dự phòng của tuần):

- B1: 2,5 h pandas/Streamlit và công thức.
- B2: 3 h engine/query cùng test tính tay.
- B3: 3 h UI, missing/provenance và walkthrough.
- B4: 1,5 h ghi card module/ratio.
- B5: 3h bổ sung cầu nối — Thiết kế bridge tables/mapping/roles, review/audit; chọn cặp năm nếu đủ quỹ.

**Đầu ra phải lưu** (từ repo, tạo khi làm):

- src/fap/analytics/ và src/fap/ui/ (cấu trúc dự kiến, tạo khi code); config/version của formulas.
- data-sets/fap/evaluation/test-results.csv; ảnh/log walkthrough và operand checks.
- docs/research-platform/execution/week-05.md và hướng dẫn chạy app ban đầu.
- docs/research-platform/execution/bridge-week-05.md: rows/manifest/expected-actual/giờ/decision phù hợp task (tạo khi làm).

**Yêu cầu SRS:** FR25, FR26, FR27, FR31, FR32, IR03, NFR05, E02, E04, E05.

**Kiểm chứng:** TC18, TC19, TC23, P02, P03, P04, P06; dùng input/expected mục 10 và 15 SRS, lưu actual/evidence.

**Xong khi:** TC18/TC19 khớp tính tay, missing/cross-scope bị chặn; đi từ ratio tới cả operands/raw. UI không coi candidate là fact. Cầu nối: Thiết kế bridge tables/mapping/roles, review/audit; chọn cặp năm nếu đủ quỹ. Chưa thực hiện ghi pending; E05/E10 chưa kích hoạt ghi not_applicable có quyết định.

### Tuần 06 — Vòng đời cổ tức, coverage và DPS năm

**Học đúng task:** Event identity, policy/execution, amendments, basis và annual eligibility.

**Đích tuần:** Không đếm trùng, không gán hủy quyền thành0, chỉ so DPS năm đủ/comparable.

**Đầu vào:** Reviewed event candidates; UI tuần5; các ca thật development trong nghiên cứu20 và fixtures.

**Việc thực hiện:**

- **W06-01:** Triển khai notice/event/components và relations có bằng chứng review; hai routes/cùng đợt chỉ cộng một lần, hai đợt cùng ticker/ngày/DPS không tự merge.
- **W06-02:** Phân loại metadata/schedule/amount/rights cancellation/policy cancellation/unresolved; sửa lịch giữ DPS, sửa mức thay revision, hủy quyền giữ policy nếu nguồn không hủy policy.
- **W06-03:** Hiển thị timeline old/current và các ngày; scheduled không thành confirmed_paid khi ngày đã qua, xác nhận paid cần nguồn.
- **W06-04:** Review coverage theo sources/window/as_of; unresolved mới đưa complete về partial/unknown. observed_dps khác annual_announced_dps; missing không thành0.
- **W06-05:** Kiểm share basis trước cộng và growth; hai năm complete/comparable mới có annual delta/growth, baseline>0 cho growth; chặn CFO/DPS. Bổ sung v3: Tính cầu nối/residual/tolerance, kiểm ít nhất một ca thật; LNST riêng LNTT; trực tiếp/unknown bị chặn.
- **W06-06:** Chạy TC13–TC17/TC20; báo cáo đợt3 có ít nhất một duplicate, một amendment và một cancellation case đúng đối tượng.

**Nhịp buổi đề xuất** (cộng giờ dự phòng của tuần):

- B1: 2,5 h đọc notices và state/identity.
- B2: 3 h resolver/relations/coverage.
- B3: 3 h aggregate, basis và tests nghiệp vụ.
- B4: 1,5 h báo cáo đợt3.
- B5: 4h bổ sung cầu nối — Tính cầu nối/residual/tolerance, kiểm ít nhất một ca thật; LNST riêng LNTT; trực tiếp/unknown bị chặn.

**Đầu ra phải lưu** (từ repo, tạo khi làm):

- src/fap/events/ và coverage/aggregate rules; config rule versions.
- data-sets/fap/evaluation/test-results.csv, lifecycle fixture expected/actual và timeline evidence.
- docs/research-platform/execution/week-06.md; docs/research-platform/reports/dot-03-tuan-05-06/.
- docs/research-platform/execution/bridge-week-06.md: rows/manifest/expected-actual/giờ/decision phù hợp task (tạo khi làm).

**Yêu cầu SRS:** FR19, FR20, FR21, FR22, FR23, FR24, FR28, BR07, BR11, E03, E04, E06.

**Kiểm chứng:** TC13, TC14, TC15, TC16, TC17, TC20, P01, P02, P03, P04, P05, P09; dùng input/expected mục 10 và 15 SRS, lưu actual/evidence.

**Xong khi:** TC13–TC17/TC20 pass hoặc có lỗi cần sửa ghi rõ; annual null khi chưa đủ, cancellation không annual zero giả, paid không suy từ lịch. Cầu nối: Tính cầu nối/residual/tolerance, kiểm ít nhất một ca thật; LNST riêng LNTT; trực tiếp/unknown bị chặn. Chưa thực hiện ghi pending; E05/E10 chưa kích hoạt ghi not_applicable có quyết định.

### Tuần 07 — Dataset theo gate và chuẩn bị holdout

**Học đúng task:** Batch/resume, sampling, annotation, lineage leakage và expected denominator.

**Đích tuần:** Dataset theo G4; development/holdout manifest riêng và gold chưa dùng chỉnh parser.

**Đầu vào:** G4 scope, lifecycle đã kiểm tuần6, collection và review store.

**Việc thực hiện:**

- **W07-01:** Thu/review phần tăng thêm theo G4 trong quỹ dữ liệu đã chốt; đủ quỹ thì dừng ở pilot, ghi thiếu chứ không lấp0 hoặc bỏ mục khỏi ledger.
- **W07-02:** Rà coverage từng issuer/profit_year bằng nguồn/cửa sổ/as_of; remaining/unresolved được giữ, không coi đã thấy vài notices là complete.
- **W07-03:** Chọn holdout khác development; không chia route/bản dịch/revision gần giống cùng lineage sang hai tập; chưa chạy tuning trên holdout.
- **W07-04:** Tạo gold six targets/report và fields/components notice, ghi người annotate/check; nếu tự chấm nêu giới hạn. Mẫu mục tiêu5–8 tài liệu là có điều kiện theo G4.
- **W07-05:** Viết protocol metrics và effort trước đo, giữ missing trong denominator; đặt manifest/hash và kiểm TC26 phần split/annotation. Bổ sung v3: UI case/bridge/source và DPS profit_year, timeline riêng; thực chi chỉ khi E10 kích hoạt.
- **W07-06:** Lưu scope/gold backup và nhật ký tuần7; chuẩn bị G8 freeze đầu tuần8, không đợi chạy kết quả rồi đổi mẫu.

**Nhịp buổi đề xuất** (cộng giờ dự phòng của tuần):

- B1: 2 h học annotation/split và chốt danh sách.
- B2: 3 h thu/review mở rộng.
- B3: 3,5h review/coverage và gold/manifest.
- B4: 1,5 h ghi protocol và quyết định chuẩn bịG8.
- B5: 3h bổ sung cầu nối — UI case/bridge/source và DPS profit_year, timeline riêng; thực chi chỉ khi E10 kích hoạt.

**Đầu ra phải lưu** (từ repo, tạo khi làm):

- data-sets/fap/evaluation/{development,holdout}/manifest.json; gold-financial.csv, gold-events.json, protocol.json.
- data-sets/fap/backup/pre-g8/; ledger scope thực tế và effort.csv.
- docs/research-platform/execution/week-07.md; split rationale và selection limits.
- docs/research-platform/execution/bridge-week-07.md: rows/manifest/expected-actual/giờ/decision phù hợp task (tạo khi làm).

**Yêu cầu SRS:** FR07, FR24, FR36, DR07, NFR10, E07, E08, E10.

**Kiểm chứng:** TC05, TC17, TC26, P07, P08, P09, P10; dùng input/expected mục 10 và 15 SRS, lưu actual/evidence.

**Xong khi:** Có split manifest/hash/gold/protocol; holdout chưa dùng tune, gold checker/self-check rõ; mọi report/target thiếu vẫn nằm ledger. Cầu nối: UI case/bridge/source và DPS profit_year, timeline riêng; thực chi chỉ khi E10 kích hoạt. Chưa thực hiện ghi pending; E05/E10 chưa kích hoạt ghi not_applicable có quyết định.

### Tuần 08 — Freeze holdout và đo chất lượng thực tế

**Học đúng task:** Joint correctness, precision/recall, B0/B1/B2 và effort công bằng.

**Đích tuần:** Baseline/quality report có tử/mẫu số và dữ liệu trước/sau review tách rõ.

**Đầu vào:** Gold/protocol/split tuần7; pipeline versions; chưa tune holdout.

**Việc thực hiện:**

- **W08-01:** Đầu tuần ghi G8: đóng băng scope/gold/split/config/hash và backup trước khi đo; bổ sung mẫu sau freeze phải có version mới.
- **W08-02:** Chạy B0 text-only và B1 text+OCR/parser trên cùng targets; giữ run outputs/version trước review và đầy đủ missing.
- **W08-03:** Chấm financial joint metric/value/unit/period/scope và event/component joint fields, lifecycle/coverage; discovery khác extraction, assisted đếm riêng.
- **W08-04:** Review ra B2; đo giây tự động, phút review, effort sửa adapter và nhập tay tương đương; B2 không accuracy tự động.
- **W08-05:** Nếu sửa parser sau xem lỗi holdout, ghi holdout đó đã thành observed/development; đánh giá độc lập cần tập mới hoặc báo rõ không còn độc lập. Bổ sung v3: Freeze gold rows/lineage/mapping/formula, status và source hashes trước đo; DHG development không thành holdout.
- **W08-06:** Lưu TC26/NFR01 audit và báo cáo đợt4: số đúng/sai/thiếu, sample size, lỗi và giới hạn; không tick95% như đã cam kết.

**Nhịp buổi đề xuất** (cộng giờ dự phòng của tuần):

- B1: 1 h freeze và ôn metrics.
- B2: 3 h chạy baseline/chấm.
- B3: 4 h đối chiếu/review/effort và lưu bằng chứng.
- B4: 2 h báo cáo đợt4.
- B5: 2h bổ sung cầu nối — Freeze gold rows/lineage/mapping/formula, status và source hashes trước đo; DHG development không thành holdout.

**Đầu ra phải lưu** (từ repo, tạo khi làm):

- data-sets/fap/evaluation/frozen-g8/{manifest.json,B0.json,B1.json,B2.json,metrics.json,effort.csv}.
- data-sets/fap/backup/g8/; docs/research-platform/execution/week-08.md.
- docs/research-platform/reports/dot-04-tuan-07-08/; actual gold/sample counts.
- docs/research-platform/execution/bridge-week-08.md: rows/manifest/expected-actual/giờ/decision phù hợp task (tạo khi làm).

**Yêu cầu SRS:** FR36, NFR01, NFR10, E02, E09.

**Kiểm chứng:** TC26, TC23, P11; dùng input/expected mục 10 và 15 SRS, lưu actual/evidence.

**Xong khi:** TC26 có manifest, expected/actual và công thức metric; xuất bản sau review quét provenance100%; tất cả số đếm gồm missing và đúng split status. Cầu nối: Freeze gold rows/lineage/mapping/formula, status và source hashes trước đo; DHG development không thành holdout. Chưa thực hiện ghi pending; E05/E10 chưa kích hoạt ghi not_applicable có quyết định.

**Gate:** G8: freeze trước benchmark; không mở issuer/chỉ tiêu mới sau gate nếu chưa có CR và quỹ thời gian.

### Tuần 09 — Bộ lọc, Spearman và ba case thật

**Học đúng task:** Quan hệ mô tả, ranks/ties/Spearman, mẫu lặp theo doanh nghiệp và giới hạn nhân quả.

**Đích tuần:** Bộ lọc đúng eligibility; ba case có nguồn, snapshot context và giới hạn.

**Đầu vào:** Reviewed dataset, metrics/limits tuần8; formulas và lifecycle tuần5–6.

**Việc thực hiện:**

- **W09-01:** Cài hai bộ lọc SRS: LNST tăng/CFO giảm; DPS giữ/tăng khi LNST hoặc CFO giảm, chỉ xét observations đủ/comparable.
- **W09-02:** Tạo scatter/Spearman với biến/bộ lọc/scope rõ; n<3 hoặc biến hằng không hệ số; ties đối chiếu reference fixture.
- **W09-03:** Hiển thị n, excluded và lý do; không dùng số tuyệt đối khác quy mô để tự suy kết luận chung hoặc CFO/DPS.
- **W09-04:** Chọn ba case thật từ nguồn đã kiểm: có thể khác mẫu tình huống mong đợi; không sửa số để có case hoặc dùng fixture giả.
- **W09-05:** Mỗi case ghi câu hỏi, bảng số, formulas/operands, coverage/basis, as_of, nguồn và phần chưa kết luận; tạo input manifest để tuần10 đóng snapshot. Bổ sung v3: Đo cầu nối trước/sau review và phút nhập/sửa; P06 chỉ khi E05 kích hoạt, số đếm/limits rõ.
- **W09-06:** Chạy TC21/TC22/TC28, tự trình bày một case2–3 phút và ghi nhật ký tuần9.

**Nhịp buổi đề xuất** (cộng giờ dự phòng của tuần):

- B1: 2,5 h học ranks/conditions, tính fixture bằng tay.
- B2: 3 h filters/scatter/Spearman và excluded.
- B3: 3 h chọn case/source/tests.
- B4: 1,5 h viết/giải thích case.
- B5: 2h bổ sung cầu nối — Đo cầu nối trước/sau review và phút nhập/sửa; P06 chỉ khi E05 kích hoạt, số đếm/limits rõ.

**Đầu ra phải lưu** (từ repo, tạo khi làm):

- src/fap/analytics/ filters/exploratory; data-sets/fap/evaluation/test-results.csv.
- docs/research-platform/execution/cases/{case-01.md,case-02.md,case-03.md}; input manifests có hash.
- docs/research-platform/execution/week-09.md.
- docs/research-platform/execution/bridge-week-09.md: rows/manifest/expected-actual/giờ/decision phù hợp task (tạo khi làm).

**Yêu cầu SRS:** FR29, FR30, FR37, E03, E04, E05, E09.

**Kiểm chứng:** TC21, TC22, TC28, P01, P03, P06, P11; dùng input/expected mục 10 và 15 SRS, lưu actual/evidence.

**Xong khi:** Ba case thật truy nguồn được; TC21/TC22/TC28 có expected/actual; không có hệ số giả khi thiếu/constant và không diễn giải nhân quả. Cầu nối: Đo cầu nối trước/sau review và phút nhập/sửa; P06 chỉ khi E05 kích hoạt, số đếm/limits rõ. Chưa thực hiện ghi pending; E05/E10 chưa kích hoạt ghi not_applicable có quyết định.

### Tuần 10 — Snapshot đầy đủ, replay offline và cập nhật

**Học đúng task:** Manifest/checksum/schema, formula version, immutable revisions và lỗi export.

**Đích tuần:** Gói CSV/JSON tự chứa inputs; replay toàn bộ kết quả cũ đúng sau cập nhật.

**Đầu vào:** Store revisions/raw, cases tuần9, formulas/coverage; conditional GET tuần2.

**Việc thực hiện:**

- **W10-01:** Thiết kế export schema_version, snapshot_id/as_of, inputs/revisions, formulas/config, scope/units, coverage và excluded; freeze tất cả số đầu vào.
- **W10-02:** Xuất CSV UTF-8/JSON/manifest/checksums và raw evidence khi được phép; evidence thiếu phải ghi incomplete, không mô tả gói đầy đủ.
- **W10-03:** Tạo replay offline bằng formula version đóng băng; so mọi kết quả tiền exact, ratios/growth sai số≤10^-9 trước rounding, không chỉ một ratio.
- **W10-04:** Tạo nguồn/review amendment mới rồi replay gói cũ; kiểm checksum hỏng, missing raw, formula version lạ; sources hiện hành không sửa snapshot cũ.
- **W10-05:** Kiểm UI run errors/import/export/path và resume; 304/cache/idempotency không regression. Case2026 chỉ thêm nếu đủ giờ, nguồn thật và không mở dữ liệu quý. Bổ sung v3: Export/replay bridge operands/mapping/source cố định sau đổi live data; source thiếu ghi incomplete.
- **W10-06:** Chạy TC24/TC25 và regression liên quan; gắn snapshot IDs vào ba case; báo cáo đợt5 có update/export/replay và giới hạn.

**Nhịp buổi đề xuất** (cộng giờ dự phòng của tuần):

- B1: 2,5 h schema/manifest và version semantics.
- B2: 3 h export/replay.
- B3: 3 h update/fault tests và gắn cases.
- B4: 1,5 h báo cáo đợt5.
- B5: 2h bổ sung cầu nối — Export/replay bridge operands/mapping/source cố định sau đổi live data; source thiếu ghi incomplete.

**Đầu ra phải lưu** (từ repo, tạo khi làm):

- data-sets/fap/snapshots/<snapshot_id>/ có CSV/JSON/manifest/checksums và evidence status.
- data-sets/fap/evaluation/replay-comparison.json, test-results.csv; run logs before/after.
- docs/research-platform/execution/week-10.md; docs/research-platform/reports/dot-05-tuan-09-10/.
- docs/research-platform/execution/bridge-week-10.md: rows/manifest/expected-actual/giờ/decision phù hợp task (tạo khi làm).

**Yêu cầu SRS:** FR33, FR34, FR35, DR08, IR04, NFR02, E08.

**Kiểm chứng:** TC24, TC25, TC04, TC05, P10; dùng input/expected mục 10 và 15 SRS, lưu actual/evidence.

**Xong khi:** TC24/TC25 pass cho toàn bộ derived outputs; gói hỏng/version lạ bị từ chối rõ; snapshot cũ khớp sau source/review update và offline. Cầu nối: Export/replay bridge operands/mapping/source cố định sau đổi live data; source thiếu ghi incomplete. Chưa thực hiện ghi pending; E05/E10 chưa kích hoạt ghi not_applicable có quyết định.

### Tuần 11 — Khôi phục, hiệu năng, an toàn local và freeze

**Học đúng task:** SQLite backup API, dependency locks, measurement và local input boundaries.

**Đích tuần:** README chạy thật, restore sạch, benchmark và toàn bộ yêu cầu có trạng thái.

**Đầu vào:** Snapshot/replay tuần10; TC catalog/SRS matrix; máy benchmark và dependencies đã ghi.

**Việc thực hiện:**

- **W11-01:** Làm backup nhất quán database/raw/config/snapshots; restore sang thư mục sạch, kiểm hashes/revisions/references và replay ít nhất một snapshot.
- **W11-02:** Đo TC30 trên máy ghi cấu hình:24 reports/144 targets/≤200 notices,20 thao tác warm cache, p95≤3 s; dữ liệu benchmark giả phải gắn synthetic, tách khỏi gold/case.
- **W11-03:** Kiểm localhost listener, HTML không execute, path traversal và log/export không secrets; TC31 không pass chỉ nhờ một checkbox UI.
- **W11-04:** Ghi module/adapter/parser/rule/formula versions và khóa dependency; README setup/collect/extract/review/export/replay/evaluate/backup/restore thực chạy.
- **W11-05:** Đối chiếu 83 mã yêu cầu/42 tình huống: pass/fail/not_run, đường bằng chứng; fix thiếu hoặc CR được chấp nhận, không tự xóa yêu cầu để làm tỷ lệ đẹp. Bổ sung v3: Regression bridge và snapshot/restore; tổng kết trạng thái E/P, C có quyết định áp dụng.
- **W11-06:** Ghi G11 feature freeze, danh sách lỗi phải sửa và bản nháp báo cáo kỹ thuật/ERD; chỉ sửa lỗi/phần còn thiếu, không mở ML/API ngoài scope.

**Nhịp buổi đề xuất** (cộng giờ dự phòng của tuần):

- B1: 1 h backup/measurement checklist.
- B2: 3 h restore/config/README và sửa lỗi.
- B3: 4 h restore, perf, safety và rà matrix.
- B4: 2 h bản nháp/G11.
- B5: 1h bổ sung cầu nối — Regression bridge và snapshot/restore; tổng kết trạng thái E/P, C có quyết định áp dụng.

**Đầu ra phải lưu** (từ repo, tạo khi làm):

- data-sets/fap/backup/g11/ và restore-check/; restore/benchmark/security evidence.
- README chạy app; dependency lock; docs/research-platform/execution/requirements-status.csv và test-results.csv.
- docs/research-platform/execution/week-11.md; docs/research-platform/reports/draft-final/ từ artifact thực tế.
- docs/research-platform/execution/bridge-week-11.md: rows/manifest/expected-actual/giờ/decision phù hợp task (tạo khi làm).

**Yêu cầu SRS:** FR38, IR05, NFR04, NFR06, NFR08, NFR09, E01, E02, E03, E04, E05, E06, E07, E08, E09, E10.

**Kiểm chứng:** TC29, TC30, TC31, P01, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11; dùng input/expected mục 10 và 15 SRS, lưu actual/evidence.

**Xong khi:** TC29/TC30/TC31 có logs/results; restore/replay thực chạy; mọi yêu cầu/TC có trạng thái và link bằng chứng. Chưa đạt không gọi đã nghiệm thu. Cầu nối: Regression bridge và snapshot/restore; tổng kết trạng thái E/P, C có quyết định áp dụng. Chưa thực hiện ghi pending; E05/E10 chưa kích hoạt ghi not_applicable có quyết định.

**Gate:** G11: freeze tính năng, chỉ xử lý lỗi và minh chứng còn thiếu; điểm M chưa pass cần kế hoạch sửa hoặc change record hợp lệ.

### Tuần 12 — Nghiệm thu thử, báo cáo và luyện bảo vệ

**Học đúng task:** Trình bày input→xử lý→output, dữ liệu→bằng chứng→giới hạn; tự sửa code.

**Đích tuần:** Hai lượt demo8–12 phút, báo cáo/deck thống nhất cùng snapshot và trạng thái SRS.

**Đầu vào:** Feature-frozen app, README/quality/tests/cases và actual requirement status tuần11.

**Việc thực hiện:**

- **W12-01:** Nghiệm thu thử UC01–UC08: walkthrough luồng thật success+failure+review+amendment+export/replay; quét provenance và eligibility published set.
- **W12-02:** Tạo báo cáo cuối theo rubric thực tế, slide và notes từ kết quả thật; tên/scope/sample size/metrics/limitations khớp SRS và snapshot.
- **W12-03:** Luyện hai demo8–12 phút; một lượt ưu tiên reviewer kiểm nguồn, một lượt lỗi nguồn/hủy quyền/restore; ghi thời gian và lỗi vấp.
- **W12-04:** Tự sửa một hàm/truy vấn nhỏ, dự đoán output rồi test; giải thích automatic/assisted/OCR/review/DPS công bố/paid và coverage.
- **W12-05:** Chuẩn bị bản offline/snapshot/log fallback; sửa lỗi nghiêm trọng, chạy lại tests bị ảnh hưởng, cập nhật requirement status và phản hồi thật. Bổ sung v3: Báo cáo/demo tối thiểu một ca cầu nối thật và một ca thiếu dòng; ghi effort/giới hạn.
- **W12-06:** Báo cáo đợt6 và checklist nộp; nhánh tốt nghiệp ưu tiên version/impact, predictor chỉ tùy chọn có gate riêng.

**Nhịp buổi đề xuất** (cộng giờ dự phòng của tuần):

- B1: 1 h ôn điểm yếu/câu hỏi.
- B2: 2 h sửa lỗi và nghiệm thu thử.
- B3: 3 h hai lượt demo/tự sửa code.
- B4: 4 h báo cáo đợt6 và hoàn thiện deck.
- B5: 1h bổ sung cầu nối — Báo cáo/demo tối thiểu một ca cầu nối thật và một ca thiếu dòng; ghi effort/giới hạn.

**Đầu ra phải lưu** (từ repo, tạo khi làm):

- docs/research-platform/reports/dot-06-tuan-11-12/; draft final report/deck/notes với snapshot IDs.
- data-sets/fap/evaluation/acceptance-rehearsal/; requirements-status.csv và test-results.csv.
- docs/research-platform/execution/week-12.md, demo-script.md và issue list.
- docs/research-platform/execution/bridge-week-12.md: rows/manifest/expected-actual/giờ/decision phù hợp task (tạo khi làm).

**Yêu cầu SRS:** NFR01, NFR05, FR31, FR37, E07, E09.

**Kiểm chứng:** TC23, TC28, TC31, P03, P11; dùng input/expected mục 10 và 15 SRS, lưu actual/evidence.

**Xong khi:** Hai lượt demo ghi nhận thật, E2 E đủ provenance/missing/lifecycle/replay; rubric/requirement gaps ghi rõ, không bỏ qua phần chưa làm. Cầu nối: Báo cáo/demo tối thiểu một ca cầu nối thật và một ca thiếu dòng; ghi effort/giới hạn. Chưa thực hiện ghi pending; E05/E10 chưa kích hoạt ghi not_applicable có quyết định.

### Tuần 13 — Môi trường sạch, đóng gói và nộp cuối

**Học đúng task:** Ôn hạn chế và quy trình tái lập; chỉ sửa lỗi còn lại.

**Đích tuần:** Bundle nhất quán, có manifest/checksum và người khác đọc hướng dẫn có thể chạy.

**Đầu vào:** App đã freeze, final drafts, accepted CR/TBD và bundle manifest dự kiến.

**Việc thực hiện:**

- **W13-01:** Sửa lỗi ưu tiên theo phản hồi thật, chạy regression bị ảnh hưởng; không thêm tính năng lớn hoặc đổi mẫu đánh giá âm thầm.
- **W13-02:** Dựng môi trường sạch theo README; chạy offline demo/replay/restore và các TC hồi quy cần thiết; lưu lệnh, phiên bản và kết quả thật.
- **W13-03:** Đóng bundle code/config/dependency locks/raw được phép/manifest/snapshots/tests/evaluation; giữ hashes, không đưa venv hoặc secrets vào gói.
- **W13-04:** Đối chiếu báo cáo/deck/source/app: cùng tên/scope/số đếm/metrics/snapshot; kiểm các paths và links thực tồn tại.
- **W13-05:** Rà 83 mã yêu cầu và 42 tình huống với bằng chứng cuối; yêu cầu M chưa pass phải ghi rõ và xử lý theo change/acceptance thực tế, không tick nhờ kế hoạch. Bổ sung v3: Bàn giao rows/source/snapshot/mapping và quyết định gate; đối chiếu SRS3.1, không coi tick là pass.
- **W13-06:** Hoàn thiện reports/tong-ket-tuan-13/ theo danh mục nộp thực tế; nêu phần đạt/chưa đạt và hướng version-impact có gate riêng.

**Nhịp buổi đề xuất** (cộng giờ dự phòng của tuần):

- B1: 0,5 h ôn điểm yếu.
- B2: 2 h sửa lỗi/package.
- B3: 3 h clean setup/replay/regression.
- B4: 3,5 h final report/deck và kiểm gói.
- B5: 1h bổ sung cầu nối — Bàn giao rows/source/snapshot/mapping và quyết định gate; đối chiếu SRS3.1, không coi tick là pass.

**Đầu ra phải lưu** (từ repo, tạo khi làm):

- data-sets/fap/submission/<date>/ có bundle manifest/checksums, README và final snapshot.
- docs/research-platform/reports/tong-ket-tuan-13/; requirements-status.csv/test-results.csv cuối.
- docs/research-platform/execution/week-13.md và quyết định cuối thực tế.
- docs/research-platform/execution/bridge-week-13.md: rows/manifest/expected-actual/giờ/decision phù hợp task (tạo khi làm).

**Yêu cầu SRS:** IR05, NFR02, NFR09, NFR10, E08, E09.

**Kiểm chứng:** TC25, TC26, TC29, P10, P11; dùng input/expected mục 10 và 15 SRS, lưu actual/evidence.

**Xong khi:** Gói sạch chạy được có log; yêu cầu/TC trạng thái đúng bằng chứng; Word/deck/app thống nhất. Chưa chạy clean setup thì không tick hoàn tất. Cầu nối: Bàn giao rows/source/snapshot/mapping và quyết định gate; đối chiếu SRS3.1, không coi tick là pass. Chưa thực hiện ghi pending; E05/E10 chưa kích hoạt ghi not_applicable có quyết định.

## 5. Thiếu thời gian và xử lý vướng

167 giờ (143 nền + 24 cầu nối) là dự toán, chưa chứng minh mọi adapter/layout làm kịp. Lỗi quá một buổi phải lưu raw/run, thu nhỏ một tài liệu, ghi giờ/decision. Giữ review/provenance/missing/lifecycle/snapshot/restore; giảm issuers trước khi bỏ lõi. Assisted không thay discovery trong nghiệm thu. Không có case mong đợi thì chọn case thật khác.

Nếu chỉ còn 8–10 tuần với 10–12 giờ/tuần: tuần 1 gộp môi trường/đọc/discovery; tuần 2–3 pilot/extract/store/review/G4; tuần 4 analytics/lifecycle; tuần 5 gold/freeze; tuần 6 đo/cases; tuần 7 snapshot/restore/local checks; tuần 8 nghiệm thu/report/package; tuần 9–10 nếu có là buffer. Chỉ 3 issuers, không mở 5–8. Giữ TC bắt buộc áp dụng, tính lại giờ/CR trước nhận lịch ngắn. Dưới 8 tuần hoặc <6–7 giờ/tuần cần lập ngân sách theo hạn thật, chưa cam kết lịch này khả thi.

## 6. Theo dõi và mở rộng

Kế hoạch phủ 83 mã yêu cầu và 42 tình huống; phân bổ tuần không phải pass. Kiểm khi module xong, hồi quy khi rule/input/store đổi. Tuần 11–13 tổng hợp status với bằng chứng, không suy từ tick. Mẫu hồ sơ ở [23](23-bat-dau-va-minh-chung-thuc-hien.md).

Đồ án ưu tiên version/impact; project giữ lineage làm nền, chưa bắt buộc semantic diff engine đầy đủ. Predictor tùy chọn sau gate riêng, không task 13 tuần. [Báo cáo hai tuần](07-bao-cao-hang-tuan.md), [lộ trình học](05-lo-trinh-hoc.md) và [tài chính](18-nhap-mon-tai-chinh-cho-du-an.md) đi cùng kế hoạch.

Checklist v3 giữ bản lưu v1/v2, chuyển start/notes, không tự áp tick vì tiêu chí đã đổi. Nguồn là JSON, sửa rồi chạy build_weekly_checklist.py để sinh Markdown/HTML. Bản trước trong history/before-pcd-v3.1-2026-10-05. Các đường dẫn/module dự kiến chưa phải artifact đã xây.
