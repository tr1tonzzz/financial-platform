# Kế hoạch thực hiện UC-1, UC-2, UC-3, UC-5; UC-4 thực hiện sau

Ngày kiểm tra repository: **11/10/2026**. **Quyết định tiếp theo đã chốt:** mẫu HPG/VNM/FPT năm 2023–2025; OCR chính chuyển PaddleOCR. [Chi tiết và trạng thái triển khai](31-chot-pham-vi-va-stack-paddleocr.md). Quyết định ưu tiên của người thực hiện: tập trung khai thác dữ liệu, phân tích tài chính, so sánh và phân tích cổ tức trước; theo dõi doanh nghiệp thực hiện sau.

Trong tài liệu này, UC-1/2/3/5/4 là **UC-F01/02/03/05/04 trong [danh mục chức năng](27-yeu-cau-chuc-nang-va-vi-du.md)**. Không dùng số này thay cho BUC trong SRS: BUC-5 của SRS là lưu/tiếp tục phân tích, không phải phân tích cổ tức. Đây là kế hoạch triển khai các lát cắt được lựa chọn, chưa cam kết toàn bộ 38 chức năng nhỏ. [Dữ liệu cần thu thập](29-du-lieu-can-thu-thap-cho-uc-1-2-3-5.md) là tài liệu đi kèm.

## 1. Hiện đã làm được phần nào?

Đánh giá theo mã và kết quả thực nghiệm trong repository, không tính việc đã viết đặc tả thành tiến độ phần mềm. Thư mục `src` chưa có mã ứng dụng tại lần kiểm tra này. Chưa có bằng chứng nghiệm thu luồng giao diện, kho số liệu lịch sử đã duyệt hoặc hệ thống phục vụ người dùng hoàn chỉnh. Không suy ra tỷ lệ phần trăm hoàn thành khi chưa ước lượng khối lượng còn lại.

| Nhóm | Bằng chứng đã có | Chưa hoàn thành |
|---|---|---|
| UC-1 — Khai thác dữ liệu | Crawler tự phát hiện/tải 8 PDF FY2025/H1-2026 của HPG, DHG, VHC, HPA; lưu hash và metadata; lần chạy lại nhận 8 phản hồi 304. Có pipeline render/OCR và trích số VNM Q1/2026 | Chọn đúng bộ báo cáo 2023–2025, trích sáu trường ổn định qua nhiều mẫu, duyệt/lưu phiên bản, bảng tra cứu và xuất dữ liệu cho người dùng |
| UC-2 — Phân tích tài chính | Phép tính tăng trưởng LNST, biến động CFO, CFO/LNST cho VNM; cầu nối CFO nhập/đối chiếu thủ công ở VNM Q1/2026 và DHG FY2025, có số so sánh kỳ trước | Biểu đồ tương tác, bảng nhiều kỳ, công thức/nguồn từ điểm dữ liệu, lưu và mở lại lần phân tích; phân rã tự động nhiều mẫu chưa có |
| UC-3 — So sánh doanh nghiệp | Có đặc tả và nghiên cứu cách so sánh; các hàm nền có thể tái sử dụng | Chưa có bằng chứng mã ứng dụng chọn nhiều doanh nghiệp, kiểm tương thích rồi dựng bảng/biểu đồ so sánh |
| UC-5 — Phân tích cổ tức | Có ví dụ thông báo VNM/DHG; hàm kiểm CFO−CAPEX−khoản chi, hệ số bao phủ; quy tắc DPS tham chiếu/cơ sở cổ phiếu và làm tròn quyền | Lịch sử cổ tức đầy đủ từng năm, vòng đời sửa/hủy, nối vào dữ liệu tài chính, giao diện và chuỗi điều chỉnh DPS dựa trên sự kiện thực đầy đủ |
| UC-4 — Theo dõi doanh nghiệp | Crawler có nền nhận diện phiên bản tải về | Chưa có danh sách theo dõi/dòng cập nhật cho người dùng. Hoãn phần sản phẩm; vẫn giữ metadata/phiên bản làm nền cho các UC trước |

**Kết quả kiểm tra lại ngày 11/10:** 13 test crawler chạy qua bằng Python runtime đã có `pypdf/lxml`; 16 test Coverage/Basis chạy qua bằng Python mặc định. Đây là test prototype, không phải 29 tình huống nghiệm thu ứng dụng. Python mặc định thiếu `pypdf`, nên chưa chạy được test crawler trong môi trường đó. Bốn test screening lịch sử không được tính vào phạm vi hiện hành.

**Cần đọc đúng bằng chứng OCR:** lần kiểm VNM 06/10 có 6/6 ô đúng, nhưng chỉ gồm ba dòng × hai cột của một PDF, dùng quy tắc theo trang/mẫu và đối chiếu thủ công cùng người thực hiện. Không phải sáu chỉ tiêu lõi, không phải benchmark độc lập. Khảo sát trước có 11/12 ô khớp ở hai báo cáo; hai tập kiểm khác nhau, không cộng thành tỷ lệ chính xác tổng quát. Chưa có thực nghiệm PaddleOCR đối chứng.

Minh chứng: [crawler](../research-crawl-methods/crawl-evidence.json), [OCR công cụ](reports/dot-01-tuan-01-02/thu-nghiem-cong-cu.md), [cầu nối DHG](../research-profit-cash-dividend/evidence/case-dhg-2025.json), [cầu nối VNM](../research-profit-cash-dividend/evidence/case-vnm-q1-2026.json), [prototype cổ tức](../research-dividend-functions/README.md), [kiểm kê/hash tại lần lập kế hoạch](evidence/uc-priority-audit-2026-10-11.json).

## 2. Thực hiện từng UC như thế nào?

**Kiến trúc thực hiện hiện hành:** React/TypeScript cho giao diện, FastAPI/Python cho API/nghiệp vụ, PostgreSQL cho kho số liệu; SQLAlchemy/Alembic cho transaction và migration. Giữ Python/Paddle/Poppler cho pipeline. [Stack và CR-WEB-01](31-chot-pham-vi-va-stack-paddleocr.md), [tuần 1](33-ke-hoach-chi-tiet-tuan-01.md), [tuần 2](34-ke-hoach-chi-tiet-tuan-02.md) thay lựa chọn pilot và giờ dự toán trước; đây là kế hoạch, chưa có web triển khai.

### UC-1 — Có dữ liệu dùng được, không chỉ có PDF

**Lát cắt đầu:** F01.1/.2/.4/.5/.6 và xuất bảng đơn giản của F01.3. Một doanh nghiệp, một báo cáo năm, sáu chỉ tiêu; sau đó mở thành ba năm và ba doanh nghiệp.

- **Đầu vào:** mã doanh nghiệp, kỳ, báo cáo đúng phạm vi, sáu chỉ tiêu cùng bằng chứng nguồn.
- **Xử lý:** xác nhận PDF → trích text nếu có, OCR nếu cần → tạo số liệu chờ duyệt → đối chiếu trang/cột/đơn vị → duyệt → lưu số chuẩn hóa cùng nguồn/phiên bản → phục vụ bảng dữ liệu.
- **Đầu ra:** người dùng chọn doanh nghiệp/kỳ, thấy số hoặc lý do thiếu, mở đúng trang nguồn, xuất CSV. Người vận hành có danh sách ô cần duyệt/sửa.
- **Mã tái sử dụng:** `crawl_official_reports.py` cho thu thập; `probe_vnm_q1.py`, `check_vnm_q1.py` và mẫu OCR trong `exports/vnm-ocr-demo` cho thực nghiệm. Không coi regex cố định theo trang VNM là bộ trích xuất chung.
- **Cần viết tiếp:** schema/migration PostgreSQL, parser theo nhãn/cột, services duyệt và REST API FastAPI; React gọi API để hiển thị bảng/nguồn/export. Không thay PostgreSQL bằng một file lưu tạm để báo đã hoàn thành kho dữ liệu; kiến trúc/schema hiện có mới là thiết kế.
- **Điều kiện xong:** lấy một ô đã duyệt từ bảng về đúng PDF/trang/cột; sửa ô tạo phiên bản mới và giữ bản cũ; ô thiếu không thành 0; xuất bảng giữ đơn vị/phạm vi. Có cả một ca hợp lệ và một ca thiếu/sai phạm vi để kiểm.

**Nghiên cứu còn thiếu:** mở cấu hình crawler cho FY2023/FY2024; xác định báo cáo hợp nhất/riêng lẻ và bản sửa; nhận diện cột hiện tại/so sánh, đơn vị và dấu âm; kiểm chứng PaddleOCR so với Tesseract. Nghiên cứu này cần kết thúc bằng fixture, mã hoặc bảng kết quả, không chỉ mô tả thuật toán.

### UC-2 — Hiểu xu hướng và lợi nhuận chuyển thành tiền thế nào

**Lát cắt đầu:** F02.1 + F02.4 + F02.8. Dùng sáu trường hiện có; phân rã F02.5 thực hiện theo một ca có dòng cấu thành được duyệt. F02.2/.3/.6/.7 chưa triển khai toàn bộ ở đợt đầu.

- **Đầu vào:** số liệu đã duyệt của một doanh nghiệp qua các kỳ tương thích.
- **Xử lý:** chọn giai đoạn → kiểm đơn vị/phạm vi/phiên bản → tính biến động, CFO/LNST, nợ phải trả/tài sản khi điều kiện hợp lệ → dựng bảng và biểu đồ → gắn công thức, nguồn và ghi chú.
- **Đầu ra:** biểu đồ LNST/CFO theo năm; bảng các tỷ số; người dùng chọn điểm để xem số gốc. Với cầu nối, hiển thị từng khoản đóng góp và phần sai lệch còn lại.
- **Cần viết tiếp:** hàm tính độc lập với giao diện; biểu đồ gắn dữ liệu nguồn; lưu bộ lựa chọn, phiên bản và nhận xét; mở lại đúng bối cảnh. Cầu nối dùng dòng cuối cùng, không cộng cả dòng tổng phụ lẫn dòng cấu thành.
- **Điều kiện xong:** người dùng trả lời “lợi nhuận tăng có đi cùng CFO không?” và kiểm được hai số nguồn; dữ liệu thiếu/denominator không hợp lệ không tạo kết quả giả; mở lại lần phân tích giữ bản dữ liệu đã dùng.

**Nghiên cứu còn thiếu:** quy tắc tăng trưởng khi năm gốc bằng 0/âm; cách trình bày CFO/LNST khi LNST không dương; bảo đảm đồ thị không nối qua kỳ thiếu như có số; từ điển dòng cầu nối theo mẫu. Muốn biên lợi nhuận cần thêm doanh thu; muốn DuPont phải thêm số dư đầu kỳ và các trường đúng chủ thể. Chỉ chọn mở rộng khi có câu hỏi người dùng cụ thể.

**Ví dụ sử dụng:** nhìn thấy LNST tăng trong khi CFO giảm, người dùng chọn năm đó, xem cầu nối và đọc thuyết minh khoản phải thu. Hệ thống giúp kiểm tra cơ sở của nhận xét, chưa tự kết luận doanh nghiệp tốt/xấu hoặc khuyến nghị mua/bán.

### UC-3 — Đối chiếu các doanh nghiệp do người dùng chọn

**Lát cắt đầu:** F03.1/.2/.3 với hai doanh nghiệp; F03.4 benchmark ngành để sau.

- **Đầu vào:** hai mã tự chọn, cùng kỳ và phạm vi phù hợp, các chỉ tiêu đã duyệt.
- **Xử lý:** kiểm tương thích → đưa đơn vị về cùng cơ sở → tính tỷ số bằng hàm của UC-2 → ghép bảng → vẽ các chuỗi và hiện thiếu dữ liệu.
- **Đầu ra:** bảng/biểu đồ cạnh nhau, công thức và nguồn từng số, ghi chú giới hạn so sánh. Không xếp hạng mã hay tự tìm doanh nghiệp đáp ứng điều kiện.
- **Cần viết tiếp:** truy vấn nhiều doanh nghiệp, kiểm phạm vi, bảng/biểu đồ so sánh, xuất/lưu nhóm đã chọn.
- **Điều kiện xong:** hai công ty cùng năm so được số và tỷ số; ca riêng lẻ–hợp nhất bị tách/không ghép vào một phép so sánh mặc định; doanh nghiệp thiếu CFO vẫn có dòng nhưng tỷ số để trống có lý do.

**Nghiên cứu còn thiếu:** chỉ tiêu nào có ý nghĩa giữa các ngành; cách xử lý khác năm tài chính; cách giải thích số tuyệt đối khác tỷ số. Ba doanh nghiệp khác ngành chỉ là nhóm người dùng chọn, không đại diện ngành. Cần mẫu/ngành đủ và chính sách chọn mẫu mới nghiên cứu benchmark.

### UC-5 — Đọc lịch sử cổ tức cùng cơ sở tài chính

**Lát cắt đầu:** F05.1/.2/.3/.4/.6; payout đầy đủ F05.5 để sau khi có số liệu đúng cổ đông/chủ thể.

- **Đầu vào:** thông báo/quyết định cổ tức, năm lợi nhuận, loại quyền, mức tiền trên cổ phiếu, ngày và trạng thái; CFO/CAPEX/khoản thực chi đúng kỳ/phạm vi; sự kiện thay đổi cơ sở cổ phiếu.
- **Xử lý:** tách thành phần nếu một thông báo liên quan nhiều năm → nối bản sửa/hủy → phân biệt công bố, lịch trả và thực chi → tổng hợp năm khi lịch sử đủ → tính kiểm bao phủ có điều kiện → kiểm basis DPS.
- **Đầu ra:** bảng lịch sử/sự kiện và biểu đồ tiền mặt theo năm khi có đủ cơ sở; bảng CFO−CAPEX−khoản chi và tỷ số bao phủ có công thức; DPS gốc, trạng thái có thể so sánh và chuỗi tham chiếu chỉ khi đủ bằng chứng; ghi chú có nguồn.
- **Mã tái sử dụng:** hàm `coverage`, `reference_dps`, `free_share_entitlement` trong `dividend_functions_probe.py`; parser ví dụ thông báo trong `extract_recent_dividend_examples.py`. Các hàm này nhận đầu vào đã ánh xạ/duyệt, chưa tự thu thập và ghép toàn bộ lịch sử.
- **Cần viết tiếp:** kho sự kiện, adapter nguồn cổ tức, duyệt năm lợi nhuận và trạng thái, đối chiếu bản sửa; nối kho số liệu UC-1 và hàm tính vào màn hình. Không lấy trị tuyệt đối mọi dòng đầu tư để thay CAPEX.
- **Điều kiện xong:** một thông báo hỗn hợp được tách đúng năm; bản sửa không bị tính hai lần; lịch thanh toán không gắn nhãn đã thực trả; thiếu năm/sự kiện không biến thành cổ tức bằng 0; một ca thiếu basis chặn chuỗi DPS điều chỉnh; G02 hiện đúng loại khoản chi.

**Nghiên cứu còn thiếu:** độ đầy đủ của lịch sử từng năm; tiền cổ tức công bố khác khoản chi trong BCTC; khoản chi gộp cho chủ sở hữu; ngày cơ sở cổ phiếu có hiệu lực; chuỗi chia tách/phát hành và giới hạn phép điều chỉnh. Trường hợp FPT hiện chưa đủ bằng chứng để dựng chuỗi DPS điều chỉnh hoàn chỉnh. CFO−CAPEX chưa mặc định là FCFE; hệ số bao phủ chưa chứng minh chính sách cổ tức tương lai.

**Ví dụ đã có trong prototype:** DHG FY2025 có CFO−CAPEX khoảng 1.181,83 tỷ đồng, thấp hơn khoản phân phối cho chủ sở hữu được ánh xạ; phần còn lại khoảng −125,63 tỷ, bao phủ khoảng 0,906. Đây là số của ca đã đối chiếu thủ công, không đồng nghĩa “cổ tức tiền mặt của cổ đông thường” nếu dòng nguồn gộp. Chức năng giúp người dùng đọc thêm cơ sở tài trợ khoản chi.

## 3. Lộ trình có đầu ra để bàn giao

**Lịch mới đã có theo hạn người thực hiện:** còn 10 tuần, demo cơ bản UC-1/2/3 cuối tuần 4 và hoàn thiện ba mã tuần 5. [Kế hoạch chi tiết v4](32-ke-hoach-10-tuan-tiep-theo.md), [checklist đánh dấu](checklist-10-tuan-v4.html). Các mốc/giờ dưới đây là phân tích trước lịch mới, không cộng vào dự toán v4.

Giữ thứ tự ưu tiên **1 → 2 → 3 → 5 → 4**. Không đợi thu đủ tất cả báo cáo mới làm màn hình phân tích: dùng dữ liệu mẫu đã duyệt, hiện rõ nguồn thủ công, rồi mở rộng corpus. Mỗi mốc là một lần demo có dữ liệu, mã và kết quả kiểm.

| Mốc | Việc thực hiện | Đầu ra và điều kiện chuyển mốc | Ước lượng ban đầu* |
|---|---|---|---|
| M0 | Chốt mẫu, lập manifest; chọn một BCTC năm và định nghĩa sáu trường; chốt schema ô số/nguồn | Có tài liệu tải được, đúng phạm vi, sáu ô tham chiếu và danh sách thiếu | 6–10 giờ |
| M1 — UC-1 | Trích/duyệt/lưu và dựng bảng một công ty; truy xuất nguồn, xuất CSV | Chạy từ PDF đến bảng sử dụng được; có ca sửa và thiếu | 20–30 giờ |
| M2 — UC-2 | Biểu đồ/tỷ số, công thức, chọn điểm nguồn, lưu/mở lại; mở dữ liệu ba năm của công ty đầu | Demo trả lời câu hỏi LNST–CFO qua các kỳ; kiểm lại phép tính từ số đã duyệt | 16–24 giờ |
| M3 — UC-3 | Thêm doanh nghiệp thứ hai, chọn nhóm, bảng/biểu đồ cùng kỳ | Một phép so sánh hợp lệ và một ca bị ngăn vì phạm vi không tương thích | 12–20 giờ |
| M4 — UC-5 | Ledger sự kiện; lịch sử tiền mặt; G02; trạng thái basis/G03; ghi chú | Một hồ sơ cổ tức truy được nguồn, xử lý bản sửa và thiếu basis; không giả định lịch sử đầy đủ | 24–36 giờ |
| M5 | Mở pilot ba doanh nghiệp × ba năm; cầu nối theo ca; kiểm luồng, đo tác vụ và sửa lỗi | 9 báo cáo đích/54 ô lõi được kiểm kê; mọi ô có số đã duyệt hoặc lý do thiếu; kết quả và hạn chế được báo cáo | 20–30 giờ |
| M6 — UC-4 | Danh sách tự chọn, công bố mới, đối chiếu bản cập nhật và tiếp tục phân tích | Chỉ bắt đầu sau luồng 1/2/3/5 ổn định; dự toán riêng | Chưa cộng |

*M0–M5: **98–150 giờ xây dựng/ghép luồng và kiểm pilot**, là ước lượng kế hoạch chưa được đo, không phải tiến độ thực tế hoặc toàn bộ ngân sách đồ án. Chưa bao gồm thời gian thu thập/duyệt corpus lịch sử diện rộng, benchmark OCR, giao diện nâng cao, benchmark ngành, ba BCTC đầy đủ, ML, định giá hoặc UC-4. Sau M1 ghi giờ thực trích/duyệt một báo cáo và điều chỉnh M2–M5. Không cộng cơ học vào baseline 167 giờ hay dự toán 64–98 giờ cũ vì có công việc trùng nhau. Chưa biết quỹ giờ/hạn nộp nên chưa gắn tuần lịch cụ thể.

**Ba việc tiếp theo:** (1) xác nhận một PDF năm của HPG/VNM/FPT và sáu ô lõi, cài/chạy mẫu Paddle trong môi trường Python 3.12; (2) tạo kho số đã duyệt và màn hình bảng có nguồn; (3) dựng biểu đồ LNST/CFO, rồi mở rộng ba năm và thêm hai mã còn lại. Ca DHG/VHC giữ làm nghiên cứu trước, không thay mẫu chính đã chốt.

## 4. Nghiên cứu cần kết thúc bằng kết quả gì?

| Vấn đề cần nghiên cứu | Cách kiểm | Đầu ra bắt buộc / quyết định |
|---|---|---|
| Nguồn lịch sử | Kiểm catalog chính thức và trang bìa PDF 2023–2025; ghi tải thành công/thất bại và bản sửa | Manifest, hash, scope xác nhận; chọn mẫu theo nguồn có thật |
| PaddleOCR có tốt hơn không? | Cùng bộ trang và cùng ô tham chiếu; mẫu có dấu âm, đơn vị, cột so sánh, scan khác chất lượng; tách phần dùng chỉnh parser và phần kiểm | Bảng đúng/sai/thiếu theo ô số và ngữ cảnh, thời gian, cấu hình/phiên bản; đã chọn Paddle theo người thực hiện; kết quả dùng đánh giá chất lượng và điều chỉnh pipeline |
| Trích số tổng quát | Chạy parser trên bố cục khác VNM, đối chiếu nhãn+cột+đơn vị; giữ candidate khi mơ hồ | Fixture và lỗi thực; không kết luận từ 6 ô một mẫu |
| Công thức phân tích | Ghi điều kiện từng tỷ số, ca mẫu số 0/âm, thiếu kỳ và khác scope | Từ điển công thức và kiểm kết quả, giải thích được trên giao diện |
| Cầu nối CFO | Duyệt dòng cuối, kiểm tổng phụ, kiểm tổng CFO, so đóng góp hai kỳ | Một ca chạy được, residual hiển thị; không ép khớp bằng dòng bù |
| Cổ tức/basis | Đối chiếu notice, nghị quyết, BCTC và sự kiện vốn; kiểm bản sửa/hủy và mốc thời gian | Ledger có nguồn; chính sách đầy đủ năm; ca không đủ dữ liệu được giữ nguyên trạng thái |
| Người dùng thực sự được hỗ trợ gì? | Làm ba tác vụ: tìm số và nguồn; giải thích LNST–CFO; đối chiếu khoản chi cổ tức. So thời gian và lỗi với đọc PDF/Excel thủ công | Nhật ký tác vụ và kết quả có mẫu; phân biệt kiểm nội bộ với thử cùng người dùng khác |

Khung OCR đề xuất: 20–30 trang đa dạng; liệt kê chính xác số ô trước khi chạy và giữ một phần chưa dùng điều chỉnh parser. Đây là thiết kế thử nghiệm, chưa có kết quả. Tesseract hiện được thử qua Tesseract.js; khi so với Paddle cần nói rõ đang so cả pipeline nào, CPU/phần cứng nào và chi phí chuẩn bị. Không gọi tập cùng người làm đối chiếu là gold độc lập.

Đo giá trị sử dụng bằng khả năng hoàn thành tác vụ, độ đúng, thời gian tra cứu/đối chiếu và khả năng truy nguồn. Chưa dùng lợi suất đầu tư làm chỉ tiêu thành công khi chưa có thử nghiệm đầu tư phù hợp. Dự đoán bằng học máy là nhánh tốt nghiệp sau gate dữ liệu; pilot 9 quan sát công ty–năm không đủ để mặc định huấn luyện một mô hình đáng tin cậy.

## 5. Tác động tới SRS và tài liệu

- Giữ [SRS v3.3](22-srs-dac-ta-yeu-cau-phan-mem.md), ID truy vết và các yêu cầu đã rút. Quyết định ưu tiên không tự duyệt mọi chức năng bổ sung.
- Trước M2/M3, đặc tả phần bổ sung chọn điểm biểu đồ, so sánh nhiều công ty và lưu cấu hình: đầu vào, xử lý, đầu ra, ca kiểm và tác động giờ/dữ liệu. Sáu trường nền đủ cho lát cắt đầu; không tự thêm doanh thu vào tiêu chí pilot cũ.
- Trước M4, nối D01–D08/D11–D12 vào ứng dụng; ghi rõ chức năng nào được triển khai và chức năng nào chỉ có prototype. Không triển khai D09/D10 đã rút.
- Kế hoạch 13 tuần/checklist cũ là baseline lịch sử; không tự tick hoàn thành từ nghiên cứu/test hàm. Dùng các mốc trên để tái lập lịch khi có giờ thực và hạn nộp.
- UC-4 hoãn giao diện theo dõi, không hoãn lưu nguồn, thời điểm và phiên bản cần cho tính đúng của UC-1/2/3/5.

## 6. Nguồn dữ liệu kiểm tra tại lần lập kế hoạch

Catalog [HPG](https://www.hoaphat.com.vn/quan-he-co-dong/bao-cao-tai-chinh), [DHG](https://dhgpharma.com.vn/vi/bao-cao-tai-chinh), [VHC](https://www.vinhhoan.com/investors-2/) và thông báo [VNM tại VSDC](https://vsdc.vn/vi/ad1/197038) đã được đọc lại ngày 11/10. Catalog VHC có tài liệu nhiều năm nhưng còn phải kiểm PDF để xác nhận đúng kỳ/scope. Công cụ đọc web nhận 403 ở catalog VNM tại lần này, trong khi prototype 06/10 đã tải được một báo cáo quý; khả năng truy cập hiện tại không được suy từ lần tải cũ. Khi nguồn không đọc được, ghi trạng thái và dùng tài liệu nguồn chính thức đã lưu/thu thủ công có provenance, không giả lập tải thành công.
