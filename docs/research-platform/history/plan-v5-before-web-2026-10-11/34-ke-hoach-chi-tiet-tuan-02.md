# Kế hoạch chi tiết tuần 2 — hoàn thiện UC-1 nhiều kỳ

Ngày lập **11/10/2026**. Tiếp nối [tuần 1](33-ke-hoach-chi-tiet-tuan-01.md), theo [kế hoạch 10 tuần](32-ke-hoach-10-tuan-tiep-theo.md). **18 giờ dự toán**, không phải giờ đã thực hiện. Định nghĩa chỉ tiêu và căn cứ Báo cáo 2: [tài liệu 35](35-dac-ta-metrics-tu-bao-cao-02.md).

**Đích:** người theo dõi doanh nghiệp chọn một mã và 2023–2025, đọc bảng sáu chỉ tiêu, biết ô nào thiếu/đã sửa, xem định nghĩa và nguồn, xuất dữ liệu sử dụng cho UC-2. Thu thập/duyệt là phần vận hành phục vụ đầu ra này.

## 1. Phạm vi UC nhỏ và tiêu chí dùng được

| UC nhỏ | Tuần 2 làm gì? | Đầu ra người dùng kiểm được |
|---|---|---|
| F01.1 — Tra cứu doanh nghiệp | Chọn HPG/VNM/FPT, hiện tên và phạm vi; không làm tìm kiếm toàn thị trường | Chọn đúng mã; mã chưa có dữ liệu hiện lý do |
| F01.2 — Dữ liệu nhiều kỳ | Bảng sáu dòng × ba năm công ty đầu, chọn một/mọi năm trong phạm vi | Đổi giai đoạn đúng cột và nguồn, không dùng quý thay năm |
| F01.3 — Chọn/xuất dữ liệu | Chọn chỉ tiêu trong sáu trường và giai đoạn; xuất CSV dạng mỗi dòng một fact | CSV khớp bộ chọn, chứa thiếu/status/nguồn và revision |
| F01.4 — Định nghĩa/bằng chứng | Bấm ô → nghĩa chỉ tiêu, PDF/trang/cột, số gốc/đơn vị và lịch duyệt | Có thể kiểm ngược số hiển thị về đúng nguồn |
| F01.5 — Độ đầy đủ/phiên bản | Hiện 18 targets của ba năm, phân biệt đã duyệt/thiếu/chờ xử lý | Biết đang dùng bản nào và vì sao số chưa cung cấp |
| F01.6 — Nền dữ liệu | Parser khác bố cục, hàng đợi duyệt, revision và chạy lại an toàn | Sửa số có audit; tải/trích lại không nhân bản vô cớ |

Đây là lát cắt UC-1 đã chọn; chưa phải kho toàn bộ ba BCTC hoặc tất cả chức năng trong danh mục. Biểu đồ, công thức tỷ số và lưu nhận xét phân tích làm UC-2 ở tuần 3.

## 2. Điều kiện bắt đầu và thứ tự ưu tiên

Đầu vào cần có từ tuần 1: một PDF đúng năm/scope/hash, adapter Paddle hoặc lỗi còn mở, candidate/DB/review tối thiểu, bảng sáu trường và CSV. Nếu bảng/nguồn/CSV chưa đi hết luồng, sửa việc chặn trước khi mở ba năm; báo việc chuyển sang tuần 2 và giờ thực, không tick tuần 1 bằng kế hoạch.

Chọn công ty đầu theo nguồn năm và luồng đã làm ở tuần 1, ưu tiên tiếp tục cùng mã để giảm đổi bố cục. Chuẩn bị PDF 2023/2024/2025 của mã đó; một tài liệu công ty thứ hai làm ca thử bố cục. Dùng lại downloader/text/render; không tổ chức lại một đợt kiểm toàn bộ công nghệ.

## 3. Năm buổi thực hiện — 18 giờ

| Buổi | Giờ | Task 10 tuần | Việc cụ thể | Đầu ra cuối buổi |
|---|---:|---|---|---|
| 1 | 4 | W02-01 | Củng cố schema, khóa, transaction và revision | DB nâng cấp không mất nguồn/lịch sử; backup mở được |
| 2 | 4 | W02-02 | Mở parser sáu trường sang kỳ/bố cục khác | Candidates kèm lý do ambiguity; fixture phát triển có expected |
| 3 | 4 | W02-03 | Kiểm dữ liệu, hàng đợi duyệt và lịch sửa | Blocking không publish; duyệt/sửa/từ chối giữ audit |
| 4 | 3 | W02-04 | Chuỗi ba năm công ty đầu, bảng/bộ chọn/CSV | 18 targets được rà; dữ liệu đã duyệt sẵn cho UC-2 |
| 5 | 3 | W02-05 (2h), W02-06 (1h) | Tải/trích lại, resume, kiểm luồng và báo cáo | Log idempotency, demo UC-1 và nháp Word/slide đợt 1 |

### Buổi 1 — Kho dữ liệu giữ được ngữ cảnh

1. Sao lưu DB tuần 1; kiểm số candidate, facts và reviews trước sửa schema. Migration thất bại phải phục hồi được, không xóa DB làm lại để che mất lịch sử.
2. Tách doanh nghiệp/tài liệu/phiên bản/candidate/fact/review. Khóa nghiệp vụ của fact gồm mã, metric, loại kỳ, kỳ/ngày số dư, scope và revision; không chỉ dùng `(mã,năm)`.
3. Raw file nhận diện bằng SHA-256; cùng nội dung từ hai URL có thể giữ hai lần thu/nguồn nhưng không tạo hai PDF khác nhau. Hash mới tạo phiên bản tài liệu mới, chưa tự thành bản được duyệt hiện hành.
4. Một transaction lưu quyết định review cùng fact mới và lịch sử. Lỗi giữa chừng rollback; bản số trước vẫn truy xuất được.
5. Truy vấn bảng chính qua lớp repository, chỉ lấy bản reviewed đã được chọn. Nhiều bản mâu thuẫn chưa giải quyết trả trạng thái unresolved, không chọn bản mới nhất chỉ theo ngày tải.

**Kiểm nhỏ:** sửa một số giả định trong DB fixture, gây lỗi trước commit, đọc lại thấy bản cũ/audit không bị ghi nửa chừng. Fixture gắn nhãn, không sửa số doanh nghiệp để tạo minh chứng.

### Buổi 2 — Parser biết mình chưa chắc

1. Đọc header để xác nhận đơn vị, kỳ, phạm vi và cột; alias nhãn chỉ hỗ trợ tìm candidate. Không gán “2025” cho mọi số trong PDF 2025.
2. Chọn các dòng tổng đúng định nghĩa ở tài liệu 35. Phân biệt tổng LNST với phần cổ đông mẹ; tổng tiền/tương đương tiền với riêng tiền; tổng nợ phải trả với nợ vay.
3. Native text usable dùng nhánh text; scan dùng Paddle. Giữ cột/bbox để người duyệt kiểm, không chỉ tìm nhãn rồi lấy số gần nhất.
4. Khi nhiều nhãn/cột đều có vẻ hợp lệ, lưu candidates và `ambiguous` thay vì tự publish. Không đọc được ghi missing cùng nguyên nhân; không thay bằng 0.
5. Rà ít nhất một báo cáo/kỳ tiếp theo và một bố cục khác công ty đầu nếu nguồn có. Fixture ghi trang/cột/value/unit/period/scope expected, là tập phát triển; chưa dùng để khẳng định độ chính xác tổng quát.

**Đầu ra:** bảng lỗi theo nguyên nhân (nhãn, cột, dấu, đơn vị, kỳ/scope) và thời gian sửa; biết tự động trích được phần nào. Nếu còn nhiều lỗi, giới hạn parser theo bố cục có bằng chứng và cho review có nguồn để hoàn thành luồng.

### Buổi 3 — Kiểm và duyệt cạnh nguồn

| Kiểm | Xử lý đề xuất | Minh chứng cần lưu |
|---|---|---|
| Thiếu URL/hash/trang, unit hoặc scope chưa xác nhận | Chặn publish fact liên quan | Issue + ô không lên bảng reviewed |
| Kỳ/năm/cột không khớp target | Chặn, chọn lại kỳ/cột hoặc từ chối | Candidate cũ và lý do xử lý |
| Tài sản so với nợ phải trả + vốn | Warning, đối chiếu ba ô; không tự sửa số cho khớp | Residual và tolerance theo độ làm tròn nguồn |
| LNST/CFO âm hoặc lệch lớn | Giữ số có dấu; yêu cầu kiểm khi đáng nghi | Số gốc và lý do duyệt; không coi âm luôn là lỗi |
| Số so sánh khác báo cáo năm trước | Giữ cả hai, kiểm phân loại lại/bản sửa và quyết định dùng | Hai nguồn, revision và lý do lựa chọn |

Không đặt tolerance tiền tùy tiện để ép cân đối. Quy tắc/tolerance được lưu cùng kết quả kiểm; source rounding hoặc sai cột phải được phân biệt.

Màn hình vận hành có bộ lọc chưa duyệt/có issue, phần ảnh hoặc link đúng trang nguồn, số gốc/chuẩn hóa và ba hành động duyệt/sửa/từ chối. Sửa phải giữ trước–sau/lý do; không cho edit trực tiếp vào số chính thức. Missing ở ô khác không chặn toàn bảng: fact hợp lệ vẫn cung cấp, ô còn thiếu hiện lý do.

### Buổi 4 — Bảng nhiều kỳ để người dùng khai thác

1. Rà ba năm công ty đầu: mục tiêu 18 core targets. Có đủ PDF, đủ candidates, đủ reviewed facts là ba mức khác nhau; ghi riêng.
2. Bảng theo metric × năm, hiển thị VND hoặc tỷ đồng với nhãn rõ. Bộ chọn mã, năm và chỉ tiêu cập nhật đồng thời bảng/export; scope hiện cạnh tiêu đề.
3. Click ô → định nghĩa, giá trị chính xác VND, số gốc/unit, nhãn cột, bản tài liệu và audit. Bản so sánh/phân loại lại có nhãn ngay tại chi tiết ô.
4. Hiện coverage dạng “đã duyệt x/18; chờ duyệt y; thiếu z; unresolved u”, với các nhóm loại trừ nhau. Missing không tạo thanh biểu đồ 0 hoặc dòng CSV 0.
5. CSV UTF-8 gồm ticker, metric, period_kind, kỳ/ngày, scope, value_vnd, unit, status, reason, document_version_id, source_url, page, column, revision_id. Xuất cả targets thiếu của phạm vi đã chọn; mở lại kiểm tiếng Việt, dấu âm và số lớn không mất chính xác.

**Chuẩn bị UC-2:** truy vấn trả dữ liệu đã duyệt cùng status/nguồn cho chuỗi 2023–2025. Không tính growth/CFO-LNST ở lớp parser; tuần 3 dùng lớp phân tích riêng. Trường nào thiếu thì phép tính liên quan chưa thực hiện, không phải bỏ cả doanh nghiệp.

### Buổi 5 — Chạy lại, demo và báo cáo

1. Tải lại cùng URL/nội dung: không nhân raw/candidate/fact ngoài chủ đích; ghi HTTP 304 nếu nguồn hỗ trợ, hoặc 200 cùng hash. Nguồn không hỗ trợ conditional request được ghi giới hạn.
2. Fixture raw mới: có document version mới, bản reviewed cũ vẫn truy được; chưa duyệt không tự thay bảng chính. Fixture lỗi một file: file khác vẫn xử lý và resume không tạo duplicates.
3. Demo người dùng: chọn mã/giai đoạn → bảng → một ô nguồn → một ô thiếu → chọn hai chỉ tiêu → CSV. Demo vận hành một lần sửa có audit và chạy lại.
4. Ghi thời gian thu, trích và duyệt riêng; candidate tự động đúng/sai/thiếu trước review riêng với facts sau review. Nếu chưa đo ghi chưa đo; không lấy 6/6 ô cũ làm số đo Paddle.
5. Điền nhật ký tuần 2 và [checklist](checklist-10-tuan-v4.html) bằng kết quả thật. Giờ soạn báo cáo 1h là nháp dựa trên minh chứng đã lưu, không cam kết hoàn thiện cả Word/PPT trong 1h.

## 4. Bộ kiểm tối thiểu

Các ca dưới đây là đề xuất kiểm cho lát cắt UC-1, không thay 51 ca SRS hoặc tự gán chúng đã pass.

| Ca | Input | Expected |
|---|---|---|
| U1-01 | PDF đúng mã/năm/scope có sáu số nguồn | Bảng khớp sáu số đã duyệt, từng ô về đúng nguồn |
| U1-02 | Nguồn đơn vị triệu, ngoặc âm | Chuẩn hóa chính xác, giữ dấu và raw unit |
| U1-03 | Có tổng LNST và LNST cổ đông mẹ | Trường `net_income_total` chọn tổng; không âm thầm thay bằng dòng mẹ |
| U1-04 | CFO 2024 trong cột so sánh PDF 2025 | Kỳ kinh tế 2024, tài liệu 2025, cột comparative; không nhân năm |
| U1-05 | Gạch/mất số/mơ hồ | Null + reason; khác số 0 đã xác nhận |
| U1-06 | Chưa duyệt/scope không rõ/nguồn không đủ | Không publish fact; có issue để xử lý |
| U1-07 | Sửa/duyệt hai lần, lỗi trước commit | Audit đủ và transaction rollback; không mất bản cũ |
| U1-08 | Lặp tải và trích cùng file | Raw/fact không nhân bản; run log ghi kết quả |
| U1-09 | Số so sánh đã phân loại lại khác bản năm trước | Hai nguồn giữ riêng; có lựa chọn revision có lý do |
| U1-10 | Chọn mã/năm/chỉ tiêu rồi CSV và reload app | File đúng bộ chọn, số/thiếu/tiếng Việt/nguồn không mất |

Đo expected/actual bằng dữ liệu nguồn thật cho ca bình thường, fixture gắn nhãn cho lỗi có chủ đích. Ca không có nguồn thật phải ghi fixture, không trình thành sự kiện doanh nghiệp đã xảy ra.

## 5. Hồ sơ đầu ra và điều kiện chuyển tuần 3

Các đường dẫn sau là **đích dự kiến**, chưa phải file đã có:

- `execution-v4/week-02.md`: task/giờ/run, phần đã chạy/chưa chạy, lỗi và việc chuyển tuần.
- `data-sets/fap/execution-v4/ledger-reports.csv`, `ledger-targets.csv`, `reference-facts.csv`: cập nhật nguồn/status; 18 targets công ty đầu đã rà, ledger toàn pilot vẫn 54.
- DB backup + schema/migration version + parser fixtures + review/error log + bộ kiểm expected/actual.
- CSV ba năm, ảnh bảng/nguồn/audit, log chạy lại và clip demo ngắn nếu cần; dữ liệu Git-ignore phải sao lưu riêng.

- [ ] W02-01: migration/transaction/revision không mất dữ liệu cũ.
- [ ] W02-02: parser thử trên kỳ/bố cục khác, ambiguity/missing có lý do.
- [ ] W02-03: số publish có đủ ngữ cảnh/nguồn, audit giữ trước–sau.
- [ ] W02-04: bảng ba năm và xuất bộ chọn hoạt động; công bố x/18 số đã duyệt.
- [ ] W02-05: chạy lại/resume/raw version có kiểm thực tế.
- [ ] W02-06: demo và nháp báo cáo ghi đúng kết quả.

**Chuyển UC-2 khi:** luồng bảng/nguồn/export ổn định và có ít nhất hai năm liền kề của công ty đầu với LNST/CFO đã duyệt, cùng scope. Đích mong muốn vẫn ba năm và sáu trường; thiếu số thì giới hạn phân tích nào chạy được và tiếp tục bổ sung. Không đợi parser tự động hoàn hảo; dữ liệu nhập/sửa có nguồn được dùng nhưng phải ghi rõ. Nếu chỉ có một năm, làm giao diện UC-2 trên phần có dữ liệu, chưa trình xu hướng nhiều năm là đã hoàn thành.

## 6. Nội dung Word và slide đợt hai tuần

**Word đề xuất 3–5 trang:** “Triển khai UC-1: khai thác dữ liệu tài chính có nguồn qua nhiều kỳ”. Dùng làm phần tiếp nối Báo cáo 2, không viết lại tổng quan đề tài.

1. **Phạm vi kế thừa (khoảng nửa trang):** sáu metrics từ bảng dữ liệu Báo cáo 2; mẫu thử cũ là ba dòng/hai kỳ; chọn báo cáo năm và đổi OCR sang Paddle. Bảng ngắn “đã có → bổ sung lần này”.
2. **Phân rã UC-1 (khoảng một trang):** bảng F01.1–F01.6, mỗi hàng input/xử lý/output/minh chứng; phần người dùng đặt trước phần vận hành.
3. **Cách thực hiện (khoảng một trang):** một sơ đồ tài liệu→candidate→review→fact→bảng/nguồn/CSV; một record thật đã ẩn thông tin không cần; cách lưu period/scope/đơn vị/revision. Trích đoạn code ngắn hoặc đường dẫn commit/run thực, chưa có không ghi đã viết.
4. **Thực nghiệm (khoảng một trang):** coverage report/targets/facts; bảng expected/actual một số ca kiểm; một lỗi thật và lần sửa có nguồn; thời gian trích/review nếu đo. Ảnh bảng nhiều kỳ và nguồn một ô.
5. **Giới hạn và bước kế tiếp (nửa trang):** phần assisted, bố cục chưa hỗ trợ, số còn thiếu; UC-2 sẽ làm biểu đồ LNST–CFO, tỷ số có điều kiện và lưu phân tích từ kho đã duyệt.

**Mẫu bảng kết quả để điền, không phải số đo:** mã/năm; PDF xác nhận; targets; candidates tự động đúng/sai/thiếu; facts reviewed; thời gian trích; thời gian duyệt; source/run. Đừng trộn accuracy của số máy trích với chất lượng số sau người sửa.

| Slide | Chỉ ghi phần cần đọc | Minh chứng/demo |
|---|---|---|
| 1 | UC-1 giúp chọn mã/kỳ → lấy bộ dữ liệu có nguồn; sáu chỉ tiêu kế thừa | Bảng input/output, đánh dấu chức năng đã chạy |
| 2 | Từ mẫu OCR cũ tới luồng ứng dụng; đổi Paddle tại bước OCR | Sơ đồ ngắn, engine/model/version đúng log |
| 3 | Bảng nhiều kỳ → chọn ô → nguồn → xuất | Demo trực tiếp, ảnh dự phòng |
| 4 | Coverage, một lỗi đã xử lý, ba việc UC-2 tuần 3 | Số đếm thật, một ảnh audit; không lặp sơ đồ |

**Demo 3–4 phút:** 2 phút người dùng khai thác bảng/nguồn/CSV; 1 phút duyệt/sửa; phần còn lại chỉ coverage và giới hạn. **Điểm trao đổi:** định nghĩa chỉ tiêu/cách trình bày nguồn đã rõ chưa; chuỗi dữ liệu hiện có đủ để bắt đầu phân tích LNST–CFO như dự kiến không?
