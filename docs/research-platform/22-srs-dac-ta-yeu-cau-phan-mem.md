# ĐẶC TẢ YÊU CẦU PHẦN MỀM — SRS-FAP-01

**Xây dựng hệ thống thu thập, chuẩn hóa và phân tích lợi nhuận, dòng tiền kinh doanh trong mối liên hệ với cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam.**

Phiên bản 3.3 • Ngày 11/10/2026 • Trạng thái: dự thảo cơ sở yêu cầu để rà soát và triển khai.

## 0. Kiểm soát tài liệu

| Thuộc tính | Giá trị |
|---|---|
| Mã tài liệu / hệ thống | SRS-FAP-01 / Financial Analysis Platform (FAP) |
| Nguồn chuẩn để sửa | Tệp Markdown này; Word v3.1 là bản lưu trước CR-DIV-02, chưa đồng bộ v3.3 |
| Người soạn | Trợ lý Codex, dựa trên nghiên cứu và quyết định trong repository |
| Chủ sở hữu yêu cầu | Sinh viên thực hiện đề tài; họ tên chưa cung cấp |
| Người rà soát / phê duyệt | Sinh viên và giảng viên hướng dẫn; chưa ghi nhận phê duyệt |
| Phạm vi hiệu lực | Lịch làm tiếp còn 10 tuần theo người thực hiện, kế hoạch v4; baseline 13 tuần giữ lịch sử; các mở rộng tốt nghiệp không thuộc nghiệm thu MVP |
| Quan hệ tài liệu | Kế thừa v3.1/CR-PCD-01, v3.2/CR-DIV-02; CR-AN-03 rút sàng lọc tại mục18; UC nền mục3/5, phân rã mục17; danh mục sản phẩm UC-F tại tài liệu27 |

| Phiên bản | Ngày | Thay đổi |
|---|---|---|
| 2.3 | 04/10/2026 | Chốt phạm vi sau nghiên cứu lần hai; làm rõ hủy quyền và hướng mở rộng |
| 3.0 | 04/10/2026 | Bổ sung yêu cầu định danh, use case, hợp đồng dữ liệu, phi chức năng, phép kiểm chứng và ma trận truy vết |
| 3.3 | 11/10/2026 | Rút FR29/FR30/D09/D10 và ba TC theo yêu cầu người thực hiện; định hướng người theo dõi tài chính/đầu tư; giữ ID còn lại, 91 yêu cầu/51 TC dự kiến; UC-F mới là ứng viên |
| 3.2 | 11/10/2026 | Tổ chức 5 BUC; giữ FR/UC phân rã; thêm 12 D/12 TC-D cho G02/G03/G01 theo ca pilot; chưa phê duyệt hoặc tích hợp ứng dụng |
| 3.1 | 05/10/2026 | Tích hợp hướng kết hợp theo yêu cầu cập nhật tài liệu của người thực hiện: cầu nối CFO theo ca, E01–E10/P01–P11; giữ 73 yêu cầu và 31 TC nền |

**Cơ sở và giới hạn của đánh giá “đủ”:** đã có bài toán, người dùng, phạm vi, sáu chỉ tiêu, nguồn thử, quy tắc cổ tức, kiến trúc dự kiến và protocol đánh giá. Các thông tin này đủ để lập SRS có thể rà soát và triển khai. Chưa có bộ gold hoàn chỉnh, kiểm chứng discovery cổ tức trên toàn pilot, rubric chính thức của trường hay nghiệm thu người dùng. Mục 12 ghi cách đóng từng điểm mở; tài liệu này không tuyên bố các chức năng đã được xây dựng.

Tài liệu tham chiếu ISO/IEC/IEEE 29148:2018 cho kỹ nghệ yêu cầu và hướng dẫn công khai NASA về yêu cầu kiểm chứng được, định danh và truy vết. Chưa đối chiếu từng điều khoản của toàn văn tiêu chuẩn có bản quyền; đây không phải tuyên bố chứng nhận hoặc tuân thủ đầy đủ. Cấu trúc được điều chỉnh cho project một người, có xử lý dữ liệu và phần mềm.

## 1. Giới thiệu

### 1.1. Mục đích và đối tượng đọc

SRS xác định hành vi, dữ liệu, giao diện, chất lượng và bằng chứng nghiệm thu của FAP. Sinh viên dùng để thiết kế và chia việc; giảng viên dùng để rà soát phạm vi; người kiểm thử dùng để dựng đầu vào và đối chiếu kết quả. SRS mô tả điều hệ thống phải thực hiện; tên module ở ma trận là phân bổ dự kiến, không phải thiết kế code đã hoàn thành.

### 1.2. Mục tiêu sản phẩm

Người dùng chính là người theo dõi tài chính doanh nghiệp và người đầu tư. FAP lấy lợi nhuận và khả năng chuyển thành tiền làm trục, đối chiếu với chính sách cổ tức tiền mặt. Tối thiểu một ca có cầu nối LNTT→CFO với operands và residual được duyệt theo mục 15. FAP giúp người đọc đối chiếu lịch sử lợi nhuận sau thuế (LNST), dòng tiền kinh doanh (CFO) và cổ tức tiền mặt công bố theo năm lợi nhuận, đồng thời tra soát được bằng chứng của từng số. Người vận hành thu nguồn, duyệt kết quả trích, xử lý bản sửa và xuất snapshot tái lập. CR-DIV-02 bổ sung tác vụ thẩm định: xem bao phủ tiền mặt, kiểm cơ sở lịch sử DPS, lưu nhận xét và hồ sơ câu hỏi/bằng chứng; phần sàng lọc đã rút theo CR-AN-03. Hiệu quả tiết kiệm công sức là đối tượng đo thử, chưa phải kết quả đã chứng minh.

### 1.3. Phạm vi và giới hạn

MVP sử dụng BCTC năm kiểm toán, ưu tiên hợp nhất, của doanh nghiệp niêm yết phi tài chính Việt Nam. Pilot gồm 3 doanh nghiệp × năm tài chính 2023–2025 = 9 BCTC năm và các thông báo cổ tức liên quan. Mở rộng 5–8 doanh nghiệp, 15–24 BCTC sau quyết định tuần 4 dựa trên dữ liệu và công sức. Đây là cỡ mẫu mục tiêu, không bảo đảm lực thống kê.

**Chốt mẫu ngày 11/10/2026 theo người thực hiện:** Hòa Phát (HPG), Vinamilk (VNM), FPT (FPT). Nhóm này không phải benchmark cùng ngành. Ca DHG/VHC đã có là minh chứng nghiên cứu bổ trợ, không thay báo cáo đích của mẫu chính. [Manifest phạm vi](../../config/pilot-scope.json) và [quyết định stack](31-chot-pham-vi-va-stack-paddleocr.md) chưa xác nhận bộ dữ liệu đã thu/duyệt hoàn chỉnh.

Sáu trường tài chính bắt buộc cho toàn mẫu; LNTT và các dòng cầu nối chỉ bổ sung cho ca chọn, không nâng mọi báo cáo thành bộ trường mở rộng. Sáu trường: net_income_total, cfo, cash_equivalents, total_assets, total_liabilities, total_equity. Cổ tức được biểu diễn theo thông báo, đợt thực hiện quyền và thành phần năm lợi nhuận. Giá thị trường, dividend yield, danh mục vị thế, backtest, dự đoán, chatbot, điểm sức khỏe tổng hợp, dữ liệu quý và toàn thị trường nằm ngoài MVP. CR-DIV-02 bổ sung phân tích bao phủ tiền mặt, cơ sở cổ phiếu và hồ sơ thẩm định theo ca có điều kiện; không mở hai trường tiền mặt cho mọi BCTC hoặc mọi loại corporate action. Không suy nhân quả, gian lận, khả năng thanh toán pháp lý hay khuyến nghị mua bán từ các tỷ số mô tả.

### 1.4. Quy ước đặc tả

“Phải” là nghĩa vụ nghiệm thu; “nên” là khuyến nghị. M là bắt buộc trong MVP; C là bắt buộc nếu điều kiện ghi tại yêu cầu được kích hoạt. FR: chức năng; BR: nghiệp vụ; DR: dữ liệu; IR: giao diện; NFR: phi chức năng; UC: use case; TC: tình huống kiểm chứng; TBD: điểm mở. Số hiển thị đã làm tròn khác với số lưu/tính gốc. Mọi yêu cầu ở mục 5–9 và mục 15–16 là dự kiến phải thực hiện, trạng thái ban đầu “chưa kiểm chứng”.

Tham chiếu P01–P06 (vấn đề), US01–US08 (nhu cầu), PF01–PF09 (nhóm năng lực phân rã kế thừa), AN01–AN07 (phân tích) giữ nguyên nghĩa tại tài liệu 02. Một TC có thể kiểm chứng nhiều yêu cầu; ma trận không thay thế hồ sơ expected/actual và bằng chứng khi chạy thử.

### 1.5. Tài liệu nguồn

| Mã | Tài liệu | Vai trò |
|---|---|---|
| S01 | [Đề tài và nhu cầu v2.4](02-de-tai-va-srs.md) | P, US, PF, AN và ví dụ giả định |
| S02 | [Nghiên cứu lần hai](20-nghien-cuu-lan-hai-va-chot-de-tai.md), [sổ nguồn](21-so-nguon-nghien-cuu-lan-hai.md) | Phạm vi chốt và ca thông báo thực tế |
| S03 | [Phương pháp thu thập](11-phuong-phap-thu-thap-va-xu-ly.md) | Discovery, HTTP, PDF, OCR |
| S04 | [Từ điển tài chính](12-kien-thuc-tai-chinh-va-tu-dien.md) | Nghĩa chỉ tiêu, kỳ, đơn vị, phạm vi |
| S05 | [Ghép cổ tức và phân tích](13-ghep-co-tuc-va-phan-tich.md) | Năm lợi nhuận, coverage, basis và vòng đời |
| S06 | [Protocol đánh giá](06-danh-gia-va-nghiem-thu.md) | Gold, holdout, metric và nghiệm thu |
| S07 | [Kiến trúc và dữ liệu](03-kien-truc-va-du-lieu.md) | Ràng buộc môi trường triển khai |
| S09 | [Nghiên cứu triển khai ba chức năng](../research-dividend-functions/README.md) | G02/G03/G01, BUC01–05, CR-DIV-02 và nguồn GitHub/Việt Nam |
| S08 | [Kế hoạch 13 tuần](04-ke-hoach-13-tuan.md) | Các mốc và gate |
| R01 | [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) | Tham chiếu kỹ nghệ yêu cầu; trang giới thiệu công khai |
| R02 | [NASA: How to Write a Good Requirement](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/) | Cách viết yêu cầu rõ và kiểm chứng được |
| R03 | [NASA: Requirements Verification Matrix](https://www.nasa.gov/reference/appendix-d-requirements-verification-matrix/) | Định danh và truy vết kiểm chứng |

Các nguồn trực tuyến được kiểm tra ngày 04/10/2026. Quy tắc nghiệp vụ chi tiết dựa trên S02–S05, không coi nguồn hướng dẫn SRS là quy định tài chính.

## 2. Mô tả tổng thể

### 2.1. Bối cảnh và ranh giới

Nguồn công khai chính thức → phát hiện/tải → tài liệu bất biến → trích candidates → validation và review → facts/components đã duyệt → ghép theo doanh nghiệp/năm → phân tích → UI và snapshot. Thu thập phụ thuộc mạng và nguồn bên ngoài; xem dữ liệu đã lưu, review, tính và replay snapshot phải thực hiện được offline.

Các tác nhân ngoài gồm website quan hệ nhà đầu tư/công bố chính thức, VSDC hoặc nguồn thông báo quyền chính thức, người vận hành và người đọc. Tài liệu PDF/HTML là đầu vào; CSV, JSON và gói snapshot là đầu ra. Nguồn không phải database nội bộ của FAP. Hệ thống không đặt lệnh, gửi email hay tự xuất bản dữ liệu ra dịch vụ ngoài.

### 2.2. Người dùng

| Vai trò | Năng lực / nhu cầu | Quyền trong MVP |
|---|---|---|
| Người theo dõi tài chính/đầu tư | Xem doanh nghiệp quan tâm qua thời gian, đối chiếu tài chính/cổ tức và kiểm nguồn | Tra cứu, phân tích, đối chiếu dữ liệu đã chọn, lưu/xuất snapshot |
| Người nghiên cứu | Chọn tập dữ liệu để đối chiếu, đọc giới hạn, tái tính | Chọn doanh nghiệp/kỳ, xem missing, xuất và replay; không sàng lọc ứng viên |
| Người vận hành | Nhận diện chỉ tiêu và tài liệu; duyệt/sửa có lý do | Cấu hình nguồn, thu thập, review, cập nhật, sao lưu |

Đây là vai trò sử dụng trong một ứng dụng local do một người vận hành. Chọn màn hình/vai trò không phải cơ chế xác thực hoặc RBAC. Đưa lên mạng hoặc nhiều người cùng ghi cần đặc tả bảo mật và đồng thời riêng trước triển khai.

### 2.3. Môi trường và ràng buộc thiết kế

Một ứng dụng web React/TypeScript, REST API FastAPI/Python 3.12, PostgreSQL và pandas; HTTP/lxml cho nguồn, pypdf/pdfplumber cho PDF có text, Poppler render và **PaddleOCR/PaddlePaddle CPU cho OCR fallback** theo quyết định người thực hiện ngày 11/10/2026. Tesseract giữ làm đối chứng; chưa có thực nghiệm chứng minh Paddle tốt hơn trên corpus project. Phụ thuộc/model và cấu hình phải được khóa theo phiên bản triển khai thực tế sau smoke test. Môi trường nghiệm thu chính là Windows local; React và FastAPI là lựa chọn kiến trúc hiện hành; cloud, GPU và server nhiều người dùng chưa bắt buộc. Có thể thay thư viện tương đương bằng quyết định thiết kế nếu vẫn đạt toàn bộ yêu cầu và cập nhật manifest.

Ngân sách baseline v3.1: 13 tuần, 143 giờ nền + 24 giờ cầu nối dự toán; CR-DIV-02 trước đây ước tính thêm 64–98 giờ với giả định hạ tầng nền đã chạy, chưa cộng vào lịch/checklist; cần tính lại sau CR-AN-03; quỹ thực cần chốt tại G4/mục 15. Thay đổi cỡ mẫu/chỉ tiêu phải ghi change record ở mục 12; không âm thầm mở rộng MVP.

### 2.4. Giả định và phụ thuộc

**Lịch mới theo hạn người thực hiện:** [kế hoạch 10 tuần v6](32-ke-hoach-10-tuan-tiep-theo.md) thay phân bổ tuần của baseline cũ: tuần 4 demo cơ bản UC-F01/02/03, tuần 5 rà dữ liệu ba mã, tuần 8 freeze core/tập đo, tuần 10 bàn giao. Mốc lịch này không giảm các nghĩa vụ M hoặc biến việc nhập tay thành discovery đạt FR04; phải báo trạng thái nghiệm thu thật. Ngày bắt đầu chọn trong checklist, quỹ giờ thực chưa xác nhận.

Có ít nhất một luồng danh mục BCTC và một luồng thông báo quyền cho phép tự phát hiện trong pilot. Có người vận hành duyệt chỉ tiêu và giải quyết mâu thuẫn nguồn. Không giả định HTML/PDF có cấu trúc cố định, notice luôn chỉ có một năm, mọi năm đều có cổ tức, hay nguồn chính thức luôn không sai. Dữ liệu lịch sử có thể được công bố hoặc sửa sau năm tài chính. Tình trạng quyền truy cập nguồn và bộ doanh nghiệp phải được xác nhận tại gate tuần 4.

## 3. Nhu cầu và các luồng sử dụng

### 3.1. Danh mục nhu cầu kế thừa

| Nhu cầu | Kết quả cần có |
|---|---|
| US01 | Dữ liệu sáu chỉ tiêu và độ đầy đủ từng doanh nghiệp/năm |
| US02 | LNST, CFO, chênh lệch và CFO/LNST đúng điều kiện |
| US03 | Các đợt và tổng DPS công bố đúng năm lợi nhuận, đúng bản có hiệu lực |
| US04 | Chỉ so sánh cùng kỳ/scope/đơn vị/basis, nêu lý do khi bị chặn |
| US05 | Truy ngược số liệu, công thức và nguồn |
| US06 | Review/sửa có audit trước–sau và lý do |
| US07 | Snapshot xuất ra và tái tính được |
| US08 | Đọc/đối chiếu dữ liệu doanh nghiệp người dùng chọn và ba case thật có giới hạn; phần lọc trường hợp/khám phá đã rút tại mục18 |

### 3.2. UC nghiệp vụ cấp hệ thống

Năm BUC dưới đây nhóm nghĩa vụ đang đặc tả để truy vết. Danh mục sản phẩm theo mục tiêu người dùng được tổ chức UC lớn→nhỏ tại [tài liệu27](27-yeu-cau-chuc-nang-va-vi-du.md), gồm năm nhóm chính và hai hướng mở rộng; không tự tích hợp mọi ứng viên vào MVP. Thu thập, trích xuất, chuẩn hóa, duyệt và tra soát nguồn là các luồng phân rã/năng lực dùng chung; không là năm sản phẩm độc lập. UC01–UC08 cũ được giữ nguyên tại mục 17 để truy vết kỹ thuật. Chi tiết đầu vào, luồng, ngoại lệ và phân rã tại [cấu trúc UC](../research-dividend-functions/01-uc-lon-va-phan-ra.md).

### 3.3. BUC01 — Khai thác và quản lý dữ liệu doanh nghiệp

Tác nhân chính: người theo dõi tài chính/đầu tư; người vận hành hỗ trợ nguồn và duyệt. Đầu vào: doanh nghiệp/kỳ/chỉ tiêu người đọc chọn, nguồn và tài liệu. Luồng: thiết lập ledger → thu/cập nhật → trích/chuẩn hóa → kiểm tra/duyệt → công bố dữ liệu có provenance và coverage. Đầu ra: hồ sơ dữ liệu sử dụng được hoặc thiếu có lý do. Ngoại lệ nguồn/OCR/kỳ/scope mơ hồ giữ pending; không xuất bản dữ liệu chưa duyệt. Phân rã: UC01–UC04 và UC08; FR01–FR18/FR33/FR36–FR38. Năng lực nhập/duyệt trường mới tái dùng luồng này.

### 3.4. BUC02 — Phân tích tài chính và nền tảng tiền mặt

Tác nhân: người đọc/nghiên cứu. Đầu vào: facts đã duyệt cùng kỳ/scope và snapshot; dòng cầu nối/CAPEX/phân phối khi ca tương ứng được chọn. Luồng: kiểm điều kiện → đối chiếu LNST/CFO → xem cầu nối → tính tiền sau chi đầu tư/phân phối → tra soát operands. Đầu ra: số liệu, giới hạn và vấn đề cần đọc sâu. Thiếu trường mở rộng chỉ chặn metric phụ thuộc, không chặn các phân tích nền. Phân rã: phần tiền mặt UC06, UC-E01–03; FR25–27, E01–10, D01–04 có điều kiện. Không suy bền vững tương lai hoặc nguồn tài trợ chỉ từ số dư.

### 3.5. BUC03 — Phân tích lịch sử chính sách và quyền cổ tức

Tác nhân: người đọc và người vận hành khi duyệt sự kiện. Đầu vào: notices/components, revisions, coverage và ledger cổ phiếu nếu chọn G03. Luồng: giải quyết vòng đời → tổng năm lợi nhuận → kiểm basis → xem DPS gốc và tham chiếu khi hợp lệ → đọc lịch và lý do biến động. Đầu ra: lịch sử so sánh được hoặc trạng thái chưa đủ cơ sở. Canceled/partial/unresolved không được suy annual=0 hoặc growth. Phân rã: UC05 và phần DPS UC06; FR19–24/FR28, D05–08 có điều kiện. Sự kiện cổ phiếu phục vụ kiểm cơ sở, không cộng vào tiền thu.

### 3.6. BUC04 — Đối chiếu dữ liệu tài chính doanh nghiệp

Tác nhân: người theo dõi tài chính/đầu tư. Đầu vào: doanh nghiệp/kỳ/scope do người dùng chọn và snapshot. Luồng: chọn dữ liệu → kiểm tương thích/độ đầy đủ → xem bảng, tỷ số và biểu đồ đã đặc tả → đối chiếu số/nguồn. Đầu ra: dữ liệu có cùng cơ sở hoặc trạng thái chưa đủ cơ sở. Phân rã: phần chọn/đối chiếu UC06; FR32 dùng kết quả FR25–28. FR29/30 và D09/10 đã rút. Bảng nhiều doanh nghiệp/benchmark ngành trong UC-F03 là ứng viên bổ sung, chưa thành yêu cầu mới chỉ bởi đổi tên BUC.

### 3.7. BUC05 — Lưu và tiếp tục phân tích

Tác nhân: người theo dõi tài chính/đầu tư. Đầu vào: kết quả BUC02–04, bối cảnh phân tích và ghi chú. Luồng: tạo hồ sơ → tra soát bằng chứng → ghi luận điểm/câu hỏi → freeze → xuất/replay. Đầu ra: hồ sơ kiểm lại được sau cập nhật nguồn. Phân rã: tra soát UC06 và UC07; FR31/FR34–35, D11–12. Ghi chú người dùng tách facts được duyệt. Phát hiện ảnh hưởng tự động hoặc lịch thu nhập theo vị thế là ứng viên sau pilot, chưa thuộc CR này.

## 4. Quy tắc nghiệp vụ

**BR01 — Kỳ và phạm vi.** Phép ghép/so sánh phải dùng cùng doanh nghiệp, scope và kỳ năm tương thích; stock metrics cùng ngày kết thúc, flow metrics cùng khoảng kỳ. consolidated và entity-only thuộc series khác. Không ghép số riêng công ty mẹ với CFO hợp nhất. Kiểm chứng: TC07, TC18–TC20.

**BR02 — LNST và CFO.** net_income_total là LNST toàn doanh nghiệp/nhóm trong báo cáo, không tự thay bằng LNST cổ đông mẹ. cfo là lưu chuyển tiền thuần từ hoạt động kinh doanh, có thể âm. Tỷ số CFO/LNST chỉ có giá trị khi LNST>0 và operands hợp lệ; không chặn CFO âm. Kiểm chứng: TC06, TC18.

**BR03 — Thiếu không phải 0.** missing, ambiguous, rejected, pending_review phải có trạng thái và lý do; không impute thành 0. Giá trị 0 là số có bằng chứng. “Không tìm thấy notice” khác “doanh nghiệp công bố không chia”. Kiểm chứng: TC06, TC17, TC21.

**BR04 — Năm lợi nhuận cổ tức.** Component phải gắn profit_year theo văn bản; không dùng năm đăng/chốt/thanh toán thay thế. Notice gộp hai năm phải tách hai components, không nhân đôi tổng notice. Kiểm chứng: TC09, TC13.

**BR05 — Đơn vị và cơ sở cổ phiếu.** Số tài chính chuẩn hóa sang VND; DPS dùng VND/cổ phiếu. Tỷ lệ % chỉ đổi ra DPS nếu mệnh giá/cơ sở được nguồn xác nhận. Chỉ tổng/so DPS khi share basis tương thích đã được duyệt; basis unknown chặn tổng, basis thay đổi chặn growth trừ khi có điều chỉnh được chứng minh và lưu phương pháp. Không tự áp split factor cho mọi phát hành. Kiểm chứng: TC06, TC09, TC16.

**BR06 — Không đếm trùng.** Raw duplicates, nhiều routes hoặc nhiều nguồn của cùng notice/đợt không tạo nhiều khoản DPS. Các đợt khác nhau có cùng ticker/ngày/DPS không đủ để tự gộp. Identity mơ hồ cần review. Kiểm chứng: TC04, TC13.

**BR07 — Sửa và hủy đúng đối tượng.** Sửa hành chính/schedule không thay DPS; sửa amount thay component cũ có hiệu lực, không cộng cả hai. Hủy ngày quyền/notice thực hiện quyền không tự hủy chính sách cổ tức hoặc gán annual DPS=0. Policy cancellation chỉ ghi khi văn bản xác định rõ đối tượng. Khi chưa biết bản thay thế, phải giữ coverage chưa hoàn chỉnh. Kiểm chứng: TC14–TC15.

**BR08 — Công bố khác đã trả.** scheduled_payment_date là lịch dự kiến. confirmed_paid chỉ được ghi với tài liệu xác nhận đã thanh toán gắn nguồn và phạm vi; ngày đã qua không đủ. published_at lấy từ nguồn, first_seen_at do collector ghi; không thay nhau. Kiểm chứng: TC08, TC15.

**BR09 — Coverage theo thời điểm.** complete_as_of nghĩa là người vận hành đã rà ledger theo các nguồn/cửa sổ khai báo tới as_of, giải quyết các khoản mơ hồ và duyệt basis; không bảo đảm không có công bố/sửa tương lai. partial khi biết thiếu/unresolved; unknown khi chưa đủ cơ sở rà; not_applicable chỉ có lý do nghiệp vụ thực sự, không dùng cho năm chưa tìm thấy notice. Kiểm chứng: TC17, TC24.

**BR10 — Tổng DPS năm.** observed_dps chỉ cộng components công bố có hiệu lực đã duyệt và basis tương thích trong phần quan sát; nếu không đủ điều kiện cộng, trả null và danh sách components. annual_announced_dps chỉ có giá trị khi complete_as_of và basis tương thích; 0 chỉ khi reviewed declared_zero có bằng chứng bao phủ năm, không mâu thuẫn khoản active. Các quyền bị hủy chưa rõ thay thế không bị xóa khỏi lịch sử hoặc tự làm policy amount biến mất; tổng annual phải bị chặn khi coverage chưa rõ. Kiểm chứng: TC16–TC17.

**BR11 — Phép tính mô tả.** Delta=x_t−x_(t−1); growth=(x_t−x_(t−1))/x_(t−1)×100 chỉ khi nền>0, kỳ liền nhau và comparable. Growth DPS còn cần hai năm complete_as_of. cash/assets và liabilities/assets yêu cầu assets>0. Không tính CFO/DPS vì khác đơn vị. Kiểm chứng: TC18–TC21.

**BR12 — Xung đột và số so sánh.** Khi nguồn mới sửa số lịch sử hoặc số so sánh khác bản gốc, phải giữ cả revision và chọn revision theo bằng chứng duyệt trong snapshot. Không chọn “last write wins”, không ghép tự động một phần số restated với phần còn lại bản gốc mà bỏ kiểm scope/kỳ/revision. Kiểm chứng: TC07, TC12, TC25.

## 5. Yêu cầu chức năng theo UC lớn

Giữ mã yêu cầu nền để truy vết; FR29/FR30 đã rút, FR32 cập nhật tham chiếu theo CR-AN-03. E01–E10 tại mục15; D01–D08/D11–D12 tại mục16, D09/D10 đã rút. Truy vết cũ ở mục 11 dùng UC phân rã tại mục 17.

### 5.1. BUC01 — Khai thác và quản lý dữ liệu doanh nghiệp

**FR01 [M] — Tập dữ liệu dự kiến.** Hệ thống phải lưu doanh nghiệp, năm, scope ưu tiên, sáu targets và cửa sổ nguồn/as_of thành manifest phạm vi có phiên bản. **Chấp nhận:** TC01; tạo pilot cho 3 doanh nghiệp ×3 năm phải có 9 report targets và 54 financial targets, chưa suy target đã được công bố. Nguồn: S01, PF01, US01.

**FR02 [M] — Ledger đầy đủ.** Hệ thống phải hiển thị trạng thái và lý do từng report/target cùng coverage cổ tức riêng từng doanh nghiệp/năm. **Chấp nhận:** TC01, TC17; mục chưa thu/chưa duyệt xuất missing/pending thay vì 0. Nguồn: S01, PF01, US01.

**FR03 [M] — Discovery BCTC.** Hệ thống phải có ít nhất một adapter tự phát hiện link BCTC từ danh mục/search chính thức có phân trang hoặc cửa sổ cấu hình. **Chấp nhận:** TC02; log từ seed danh mục tới một tài liệu thật thuộc pilot; danh sách seed từng PDF không được tính là discovery. Nguồn: S03, PF02.

**FR04 [M] — Discovery cổ tức.** Hệ thống phải có ít nhất một luồng tự phát hiện thông báo cổ tức từ danh mục/search chính thức trong phạm vi pilot. **Chấp nhận:** TC02; log đầu vào danh mục, cửa sổ/phân trang và notice phát hiện thật; nhập từng notice được báo riêng. Nguồn: S03, PF02.

**FR05 [M] — Tải có kiểm tra.** Hệ thống phải kiểm status, định dạng thực, dung lượng và hash trước khi nhận raw artifact. **Chấp nhận:** TC03; HTML giả PDF, file lỗi và quá giới hạn không được nhận là PDF hợp lệ; log có lý do. Giới hạn vận hành ở mục 9. Nguồn: S03, PF02.

**FR06 [M] — Cập nhật bất biến.** Hệ thống phải dùng validator HTTP khi có và phân biệt raw theo content hash để giữ phiên bản cũ, tránh tạo bản mới cho nội dung không đổi. **Chấp nhận:** TC04; 304 không tạo raw version; 200 cùng hash không tạo bản trùng; 200 khác hash tạo version mới có quan hệ và thời gian. Nguồn: S03, PF05.

**FR07 [M] — Chạy lại và tiếp tục.** Hệ thống phải ghi trạng thái theo tài liệu và tiếp tục phần chưa hoàn thành sau lỗi mà không nhân bản dữ liệu đã commit. **Chấp nhận:** TC05; ngắt sau tải/giữa xử lý, chạy lại giữ đúng một raw/fact revision theo khóa và ghi lần thử. Nguồn: S03, PF02, PF05.

**FR08 [M] — Nhập hỗ trợ.** Hệ thống phải nhận file/URL do người vận hành cung cấp, yêu cầu metadata/provenance và gắn acquisition_mode=assisted. **Chấp nhận:** TC05; assisted không tăng số discovery tự động trong báo cáo; file không đủ metadata giữ pending. Nguồn: S03, PF02.

**FR09 [M] — Sáu financial candidates.** Hệ thống phải trích sáu targets từ PDF có text và ghi candidate hoặc trạng thái thiếu cho từng target. **Chấp nhận:** TC06–TC07; dấu âm, đơn vị, cột năm hiện tại/số so sánh và scope được đối chiếu; không bỏ missing khỏi mẫu số đánh giá. Nguồn: S04, PF03, US01.

**FR10 [M] — OCR fallback.** Hệ thống phải hỗ trợ OCR trang scan/không có text sử dụng được và ghi phương thức trích, trang và lỗi. **Chấp nhận:** TC06; fixture scan kích hoạt fallback, candidate có nhãn OCR; OCR không thành công đi review/nhập có nguồn. Không cam kết OCR mọi layout. Nguồn: S03, PF03.

**FR11 [M] — Chuẩn hóa giá trị.** Hệ thống phải lưu raw text/value/unit và giá trị VND cùng quy tắc chuyển đổi, giữ riêng missing và zero. **Chấp nhận:** TC06; 1.200 triệu thành 1.200.000.000 VND, (50) triệu thành −50.000.000 VND; gạch mơ hồ không thành 0. Nguồn: S04, PF03, US04.

**FR12 [M] — Provenance candidate.** Hệ thống phải gắn mỗi candidate với source version/hash, trang hoặc HTML locator, kỳ, scope và parser/OCR version. **Chấp nhận:** TC08, TC23; mở được vùng/trang nguồn của candidate; thiếu locator/metadata bắt buộc thì chặn duyệt. Nguồn: S03, PF03, US05.

**FR13 [M] — Notice và components.** Hệ thống phải trích ticker, loại sự kiện, raw DPS/basis, profit_year và các ngày thành notice/components có provenance. **Chấp nhận:** TC09; notice 2 năm tạo 2 components đúng năm, tổng bằng mức notice khi đủ basis; field không rõ giữ unresolved. Nguồn: S05, PF03, US03.

**FR14 [M] — Issues validation.** Hệ thống phải tạo issue có rule_id, mức blocking/warning, operands, kết quả và lý do cho các kiểm tra metadata, unit, period, scope, cân đối và lifecycle. **Chấp nhận:** TC10; assets≠liabilities+equity ngoài tolerance sinh issue; thiếu operand trả not_checkable; không tự suy pass. Nguồn: S04, S06, PF04.

**FR15 [M] — Hàng đợi review.** Hệ thống phải cho xem candidate/issue cạnh nguồn và duyệt, sửa hoặc từ chối. **Chấp nhận:** TC10; candidate blocking không vào facts đã duyệt; warning chỉ được chấp nhận với lý do; quyết định từ chối vẫn có lịch sử. Nguồn: S01, PF04, US06.

**FR16 [M] — Audit quyết định.** Hệ thống phải lưu người vận hành local, thời gian UTC, trước–sau, lý do, nguồn và đối tượng của mỗi lần duyệt/sửa/từ chối/link sự kiện. **Chấp nhận:** TC11; sửa hai lần hiển thị đủ chuỗi, không ghi đè audit; identity local không được mô tả là xác thực danh tính. Nguồn: S01, PF04, US06.

**FR17 [M] — Xuất bản nhất quán.** Hệ thống phải commit dữ liệu đã duyệt và audit liên quan trong một transaction; lớp phân tích mặc định chỉ đọc dữ liệu reviewed. **Chấp nhận:** TC11, TC27; lỗi giữa commit rollback toàn bộ; pending/rejected không xuất trên bảng/CSV kết quả chính thức. Nguồn: S07, PF05, US06.

**FR18 [M] — Xử lý revision mâu thuẫn.** Hệ thống phải giữ nhiều revisions và yêu cầu review chọn revision có hiệu lực khi cùng khóa logic khác số/kỳ/scope. **Chấp nhận:** TC12; nguồn sửa lịch sử không xóa bản gốc; snapshot mới dùng revision được duyệt, snapshot cũ dùng revision cũ. Nguồn: S02, PF05, US05.

**FR33 [M] — Thông báo lỗi vận hành.** Hệ thống phải hiển thị run status, issue và hành động có thể thực hiện cho lỗi download/parser/review/export. **Chấp nhận:** TC03, TC05, TC24; lỗi tài liệu A không làm mất kết quả B; UI không báo thành công khi export/review thất bại. Nguồn: S03, PF08.

**FR36 [M] — Hồ sơ đánh giá.** Hệ thống phải xuất hoặc cung cấp script sinh báo cáo từ gold/holdout freeze cho discovery, extraction, lifecycle, review và effort. **Chấp nhận:** TC26; có tử/mẫu số, missing, development/holdout split, tự/độc lập kiểm gold và B0/B1/B2 riêng. Nguồn: S06, PF09.

**FR37 [M] — Ba case dữ liệu thật.** Hệ thống phải cho xuất ba case đã kiểm chứng, mỗi case có giá trị, nguồn, snapshot và giới hạn. **Chấp nhận:** TC28; không dùng fixture giả định; nếu không có kiểu case mong đợi, chọn case khác thật và ghi rõ. Nguồn: S06, AN07, US08.

**FR38 [M] — Sao lưu/khôi phục.** Hệ thống phải có quy trình/script backup nhất quán PostgreSQL, raw, config và manifests, cùng lệnh khôi phục được tài liệu hóa. **Chấp nhận:** TC29; khôi phục ở thư mục sạch khớp hashes/số revisions và replay thành công ít nhất một snapshot. Nguồn: S07, PF05, US07.

### 5.2. BUC02 — Phân tích tài chính và nền tảng tiền mặt

**FR25 [M] — LNST/CFO theo năm.** Hệ thống phải hiển thị mức, delta LNST/CFO và growth LNST theo BR01, BR11. **Chấp nhận:** TC18; năm bị thiếu không nối phép so sánh như hai kỳ liền nhau; nền LNST≤0 không có growth thông thường. Nguồn: S01, PF07, AN01.

**FR26 [M] — CFO/LNST.** Hệ thống phải tính CFO/LNST cho operands đã duyệt, cùng kỳ/scope và LNST>0, kèm công thức và lý do khi không hợp lệ. **Chấp nhận:** TC18; CFO=−10 và LNST=80 cho −0,125; LNST=0/âm trả not_applicable. Nguồn: S01, AN02, US02.

**FR27 [M] — Cơ cấu tiền/nợ.** Hệ thống phải tính cash_equivalents/assets và liabilities/assets khi assets>0 và operands cùng ngày/scope. **Chấp nhận:** TC19; trả phần trăm đúng; total_liabilities hiển thị “nợ phải trả”, không “nợ vay”; operands thiếu/cross-scope bị chặn. Nguồn: S04, AN03.

Bổ sung theo ca: E01–E10 và D01–D04; CAPEX/thực chi không mặc định là trường bắt buộc mọi BCTC.

### 5.3. BUC03 — Phân tích lịch sử chính sách và quyền cổ tức

**FR19 [M] — Identity và liên kết.** Hệ thống phải lưu các quan hệ same_notice/same_event/amends/cancels cùng bằng chứng review. **Chấp nhận:** TC13; 2 routes và 2 nguồn cùng đợt cộng một lần; 2 đợt thật cùng ticker/ngày/mức vẫn giữ riêng khi identity khác. Nguồn: S05, PF05, US03.

**FR20 [M] — Phân loại bản sửa.** Hệ thống phải phân biệt metadata, schedule, amount, rights cancellation, policy cancellation và unresolved để tính hiệu lực theo BR07. **Chấp nhận:** TC14–TC15; sửa lịch giữ DPS, sửa amount thay khoản, hủy quyền không làm annual=0. Nguồn: S02, PF06, US03.

**FR21 [M] — Timeline sự kiện.** Hệ thống phải hiển thị published_at, first_seen_at, record_date, scheduled_payment_date và chuỗi sửa/hủy trên timeline. **Chấp nhận:** TC08, TC14; ngày thiếu để trống có lý do; timezone ngày công bố không rõ được ghi unknown; bản cũ xem được. Nguồn: S05, PF08, AN05.

**FR22 [M] — Trạng thái thanh toán.** Hệ thống phải giữ thông báo/lịch khác confirmed_paid và chỉ cho ghi confirmed_paid nếu kèm nguồn xác nhận. **Chấp nhận:** TC15; lịch đã qua vẫn không thành paid; confirmed_paid không nguồn bị chặn. Nguồn: S05, US03.

**FR23 [M] — Tổng hợp theo năm lợi nhuận.** Hệ thống phải trả components, observed_dps, annual_announced_dps và trạng thái eligibility theo BR04–BR10. **Chấp nhận:** TC16–TC17; notice hai năm vào đúng năm, basis unknown trả null aggregate, partial không có annual tổng đầy đủ. Nguồn: S05, PF06, AN04.

**FR24 [M] — Review coverage.** Hệ thống phải lưu as_of, tập nguồn/cửa sổ đã rà, người duyệt, lý do và trạng thái coverage từng doanh nghiệp/profit_year. **Chấp nhận:** TC17; chỉ chuyển complete_as_of khi ledger đã rà và không còn unresolved ảnh hưởng; update làm phát sinh unresolved phải đưa coverage hiện hành về partial/unknown. Nguồn: S05, US01, US03.

**FR28 [M] — Biến động DPS.** Hệ thống phải tính delta/growth DPS năm chỉ khi cả hai năm complete_as_of và basis/period compatible; growth cần nền>0. **Chấp nhận:** TC20; partial không kết luận DPS năm giảm; baseline zero có delta nếu hợp lệ, growth null có lý do. Nguồn: S05, AN04, US04.

Bổ sung theo ca: D05–D08 cho ledger sự kiện và cơ sở tham chiếu; không thay điều kiện coverage FR28.

### 5.4. BUC04 — Đối chiếu dữ liệu tài chính doanh nghiệp



**FR32 [M] — Tra cứu và biểu đồ.** Hệ thống phải cho chọn doanh nghiệp/năm/scope, xem sáu chỉ tiêu, coverage, timeline và các phân tích FR25–FR28. **Chấp nhận:** TC21, TC23; VND và VND/cổ phiếu có nhãn/trục riêng; missing để khoảng trống và giải thích. Nguồn: S01, PF08, US01–US04.

Chọn doanh nghiệp/kỳ để tra cứu vẫn thuộc FR32. Không có nghĩa vụ tìm trường hợp, scatter/Spearman hoặc đánh giá tiêu chí; mã đã rút được lưu tại mục18.

### 5.5. BUC05 — Lưu và tiếp tục phân tích

**FR31 [M] — Truy vết phép tính.** Hệ thống phải cho mở formula_id/version, operands hoặc components, snapshot_id và nguồn của mỗi kết quả tính. **Chấp nhận:** TC23; đi từ tỷ số/tổng DPS tới toàn bộ số đầu vào và raw locator; không có kết quả xuất bản mồ côi. Nguồn: S01, US05, PF08.

**FR34 [M] — Export snapshot.** Hệ thống phải xuất CSV/JSON và manifest chứa dữ liệu đóng băng, revisions, coverage, formula/config, filters, n/excluded và checksum. **Chấp nhận:** TC24; đọc lại đủ dữ liệu để replay offline và xác định nguồn; định dạng chi tiết ở IR04/DR08. Nguồn: S01, US07.

**FR35 [M] — Replay.** Hệ thống phải tái tính snapshot cũ bằng dữ liệu/công thức đóng băng và kiểm tính toàn vẹn trước replay. **Chấp nhận:** TC25; update nguồn hiện hành không đổi kết quả cũ; gói thiếu/hỏng/version không hỗ trợ trả lỗi rõ. Nguồn: S01, US07.

Bổ sung theo pilot: D11–D12 cho ghi chú/tác vụ và hồ sơ đóng băng.

## 6. Yêu cầu dữ liệu

### 6.1. Thực thể và khóa logic

| Thực thể | Định danh / nội dung chính |
|---|---|
| Issuer | issuer_id ổn định; ticker, tên, exchange, khoảng hiệu lực alias; đổi ticker không đổi lịch sử issuer |
| SourceArtifact / RawVersion | artifact_id và version_id; URL/routes, content_hash, loại, size, fetched_at, HTTP validators, acquisition_mode, raw path |
| ReportContext | issuer, period_start/end, fiscal_year, scope, currency, audited flag, revision và tài liệu |
| Candidate / FinancialFact | candidate_id/fact_revision_id; metric, raw/normalized value, trạng thái, provenance và review |
| Notice / DividendEvent | notice_version_id/event_id; issuer, loại, ngày, đối tượng quyền/chính sách, quan hệ amendments/cancellations |
| DividendComponent | component_revision_id; event, profit_year, DPS raw/normalized, basis_id, effective state, sources |
| CoverageLedger | issuer/year/scope hoặc profit_year; expected/observed, status, sources/window, as_of, decision |
| ValidationIssue / ReviewDecision | rule_id, target, severity, status; operator, before/after, reason, recorded_at |
| DerivedResult / Snapshot | result_id/snapshot_id; formula version, input revisions, scope/config/coverage, excluded, hash |

Đây là hợp đồng dữ liệu logic. ERD vật lý, index và bảng triển khai được thiết kế sau SRS. Một event có nhiều notices/versions và nhiều components; một notice có thể liên quan nhiều năm. Không join facts với components trước khi tổng hợp rồi làm nhân bản financial rows.

### 6.2. Từ điển sáu chỉ tiêu

| Metric key | Nghĩa và loại kỳ | Đơn vị chuẩn |
|---|---|---|
| net_income_total | LNST tổng của scope báo cáo; flow trong năm | VND |
| cfo | Lưu chuyển tiền thuần từ hoạt động kinh doanh; flow trong năm, có thể âm | VND |
| cash_equivalents | Tiền và tương đương tiền; stock cuối kỳ | VND |
| total_assets | Tổng tài sản; stock cuối kỳ | VND |
| total_liabilities | Tổng nợ phải trả, không đồng nghĩa nợ vay; stock cuối kỳ | VND |
| total_equity | Tổng vốn chủ sở hữu của scope báo cáo; stock cuối kỳ | VND |

Không gọi cfo là CFO chức danh trong UI. Fiscal year có period_start/end thật, không giả định mọi doanh nghiệp đều có năm kết thúc 31/12. Tập pilot ưu tiên năm trọn vẹn tương thích; kỳ ngắn/chuyển niên độ chỉ lưu riêng, không so trực tiếp bằng growth năm.

### 6.3. Hợp đồng bắt buộc

**DR01 [M] — Định danh và toàn vẹn.** Dữ liệu phải có khóa ổn định và ràng buộc tham chiếu; một logical financial key gồm issuer, metric, period, scope, revision, không chỉ ticker/year. **Chấp nhận:** TC12, TC27; khóa ngoại lỗi bị từ chối; cập nhật ticker không mất lineage; duplicate không nhân rows. Nguồn: S07, PF05.

**DR02 [M] — Giá trị và đơn vị.** Giá trị chuẩn VND phải dùng integer hoặc decimal exact có phạm vi lưu đủ, không dùng floating point để giữ số gốc. Raw value/unit, currency và quy tắc đổi phải còn truy cập được; rounding chỉ tại trình bày. **Chấp nhận:** TC06, TC18; normalize/replay exact VND, không mất dấu/độ lớn. Nguồn: S04, PF03.

**DR03 [M] — Metadata và locator.** Mỗi fact/component đã duyệt phải có issuer, period/profit_year, scope hoặc basis tương ứng, unit, raw version/hash và locator. PDF dùng số trang 1-based và bbox hoặc vùng/bảng/nhãn đủ tìm; HTML dùng selector/đoạn trích và raw HTML version. **Chấp nhận:** TC08, TC23; kiểm 100% bản xuất bản không thiếu các trường áp dụng. Nguồn: S03, US05.

**DR04 [M] — Thời gian.** Thời gian hệ thống phải lưu UTC có timezone; ngày nghiệp vụ chỉ ngày giữ ISO YYYY-MM-DD. published_at phải giữ độ chính xác và timezone gốc hoặc unknown; first_seen_at không thay published_at. **Chấp nhận:** TC08; ngày không rõ giờ không bị thêm giờ giả; as_of/recorded_at phân biệt. Nguồn: S05, AN05.

**DR05 [M] — Trạng thái có lý do.** Null phải kèm status/reason ở fact, aggregate và kết quả; zero phải có nguồn. Coverage gồm complete_as_of, partial, unknown, not_applicable, không đồng nhất với extraction accuracy. **Chấp nhận:** TC17, TC21; CSV/JSON giữ null/status; không đổi null thành 0 khi đọc lại. Nguồn: S05, US01.

**DR06 [M] — Revision và audit bất biến.** Raw versions, revisions đã dùng trong snapshot, review history và relations đã công bố phải được giữ qua cập nhật; correction tạo revision/decision mới. **Chấp nhận:** TC11–TC12, TC25; snapshot cũ còn references hợp lệ sau hai lần sửa. Nguồn: S07, US06–US07.

**DR07 [M] — Coverage evidence.** Ledger phải lưu tập nguồn, cửa sổ đã rà, expected items biết được, unresolved items, as_of và người quyết định. **Chấp nhận:** TC17; người kiểm tra giải thích được vì sao complete hoặc partial; không dùng kết quả crawler không thấy link để chứng minh không chia. Nguồn: S05, US03.

**DR08 [M] — Gói snapshot.** Snapshot phải tự chứa inputs đã duyệt để tái tính và manifest chỉ tới raw evidence đã lưu; gói export phải gồm raw evidence liên quan khi nguồn cho phép sao chép, nếu không thì gói được ghi evidence_incomplete cùng lý do. **Chấp nhận:** TC24–TC25; replay offline đủ số đầu vào; gói incomplete không được mô tả là đầy đủ bằng chứng. Nguồn: S01, US07.

### 6.4. Trạng thái và chuyển trạng thái

| Đối tượng | Trạng thái / chuyển hợp lệ | Điều kiện |
|---|---|---|
| Candidate | extracted → validated → pending_review → approved/rejected | Blocking issues giải quyết trước approved; sửa tạo revision |
| Financial fact | reviewed → superseded trong hiện hành | Bản cũ giữ cho snapshot; reviewed fact khác candidate |
| Event/component | proposed → reviewed active / superseded / execution_cancelled / policy_cancelled / unresolved | Phải biết đối tượng và bằng chứng; policy và execution là hai chiều khác nhau |
| Coverage | unknown → partial → complete_as_of; complete_as_of → partial khi có unresolved mới | Mỗi quyết định có as_of và audit; old snapshot không bị đổi |
| Run item | pending → running → success/failed/skipped; failed → retry | Retry idempotent; skipped có policy/reason |

Payment evidence là thuộc tính riêng với not_confirmed/confirmed_paid, không phải tự động bước tiếp theo của scheduled. Với notice hủy quyền, component policy công bố vẫn được giữ theo bằng chứng; eligibility annual bị chặn khi chưa xác định quan hệ thay thế. Từ “active” trên UI phải nói rõ active policy hay active execution.

### 6.5. Quy tắc precision và cân đối

Số VND sau quy đổi đối chiếu exact với nguồn. Khi nguồn làm tròn, giá trị báo cáo được giữ đúng theo đơn vị công bố; không phục hồi số lẻ không có bằng chứng. Cân đối kiểm residual=assets−liabilities−equity. Tolerance mặc định cho ba số cùng rounding quantum q là 1,5q; nếu các quantum khác nhau, tolerance=0,5(q_assets+q_liabilities+q_equity). Chỉ áp dụng khi xác định được làm tròn gần nhất; rounding mode không rõ phải ghi tolerance policy thủ công có lý do, không tự xác nhận pass. Mọi tolerance và phiên bản rule lưu trong config/snapshot. Không sửa số để ép cân đối.

Quy tắc 1,5q là lựa chọn kỹ thuật đề xuất cho pilot, không ngưỡng kế toán pháp định. Giá trị hiển thị mặc định: VND theo đơn vị chọn và ghi nhãn, tỷ số 4 chữ số thập phân, phần trăm 2 chữ số; export giữ precision tính gốc hoặc serialized decimal và rounding policy. So replay yêu cầu giá trị tiền exact; ratios/growth absolute error≤10^-9 trước rounding khi cùng phiên bản công thức.

## 7. Yêu cầu giao diện bên ngoài

**IR01 [M] — Giao diện nguồn HTTP.** Adapter phải khai báo nguồn/domain, seed danh mục, cửa sổ, pagination, timeout/retry/delay và trạng thái policy; log URL cuối và HTTP status mà không lưu secret. **Chấp nhận:** TC02–TC05; audit đường discovery và lỗi đủ tái kiểm. Nguồn: S03, PF02.

**IR02 [M] — Nhập PDF/HTML.** Đầu vào phải được kiểm định dạng/nội dung, gắn raw artifact và không tự chạy script/macro từ tài liệu. **Chấp nhận:** TC03, TC05; HTML lưu để phân tích, không execute trong UI; file nhập lỗi có thông báo. Nguồn: S03, PF03.

**IR03 [M] — UI tiếng Việt.** UI phải có các màn hình dataset/coverage, runs, review, company analysis, evidence và snapshots; nhãn nghĩa tài chính tiếng Việt, không chỉ key kỹ thuật. **Chấp nhận:** TC21, TC23; người đọc chọn tập, nhận biết thiếu dữ liệu và mở nguồn qua luồng UC06; biểu đồ có đơn vị/scope/as_of. Nguồn: S01, PF08.

**IR04 [M] — Export machine-readable.** CSV phải dùng UTF-8 và schema ghi trong manifest; null được biểu diễn nhất quán cùng status. JSON phải có schema_version, snapshot_id, generated_at, as_of, data_scope, inputs, formulas, config, coverage, exclusions và checksums. **Chấp nhận:** TC24; roundtrip Unicode/âm/zero/null đúng, không chỉ xuất ảnh/chart. Nguồn: S01, US07.

**IR05 [M] — Giao diện chạy và cấu hình.** Phải có lệnh hoặc màn hình cho collect, extract, review, export/replay, evaluate và backup/restore, cùng README khởi chạy và cấu hình nguồn/mẫu. **Chấp nhận:** TC26, TC29; thực hiện từ thư mục sạch theo README, không sửa code để đổi issuer/year hoặc delay. Thiết kế web dùng REST API FastAPI; CLI giữ cho xử lý theo lô và tái lập thực nghiệm. Nguồn: S07, PF09.

## 8. Yêu cầu phi chức năng

**NFR01 [M] — Tính đúng và truy vết.** 100% giá trị tài chính/DPS/derived được xuất bản trong tập nghiệm thu phải có nguồn và operands/metadata bắt buộc theo DR03; mọi phép tính phải đạt expected ở bộ TC nghiệp vụ. **Kiểm chứng:** TC23, TC26; kiểm toàn bộ published targets và fixtures, ghi lỗi thay vì bỏ targets lỗi. Đây là chuẩn xuất bản sau review, không cam kết 100% extraction tự động. Nguồn: S06, P05.

**NFR02 [M] — Tính tái lập.** Replay cùng snapshot/formula version phải cho cùng inputs/coverage và kết quả trong precision mục 6.5 dù dữ liệu hiện hành đã cập nhật. **Kiểm chứng:** TC25; so mọi kết quả trước/sau update, không chỉ một biểu đồ. Nguồn: S06, US07.

**NFR03 [M] — Khả năng chịu lỗi.** Một tài liệu lỗi không được làm hỏng dữ liệu đã commit của tài liệu khác; interruption phải khôi phục bằng retry theo FR07 và transaction. **Kiểm chứng:** TC05, TC27; fault injection trước/sau commit và cache lỗi. Không cam kết tránh mất điện ở phần chưa commit. Nguồn: S03, S07.

**NFR04 [M] — Hiệu năng local.** Trên máy nghiệm thu được ghi cấu hình, với bộ 24 BCTC, 144 financial targets và tối đa 200 notices đã lưu, p95 thời gian đổi bộ lọc và hiển thị bảng/phân tích từ cache phải≤3 giây trong 20 thao tác sau warmup. **Kiểm chứng:** TC30; không tính network/OCR vào UI latency; ghi mọi lần đo. Ngưỡng này kế thừa đề xuất v3.0, cần xác nhận máy trước đo. Nguồn: S08, US01, TBD04.

**NFR05 [M] — Minh bạch sử dụng.** Trong kịch bản xem một doanh nghiệp, người dùng phải nhìn thấy scope, đơn vị, as_of và trạng thái đầy đủ ngay ở bảng/kết quả; nguyên nhân null phải mở được từ kết quả. **Kiểm chứng:** TC21, TC23; checklist UI và ít nhất một lượt walkthrough có ghi người thực hiện; nếu tự đánh giá phải ghi rõ. Nguồn: S01, US01, US04.

**NFR06 [M] — An toàn nguồn và vận hành.** Mặc định ứng dụng phải bind localhost, không thực thi nội dung tài liệu, không nhận path traversal khi export/import, và không ghi credentials vào log/gói xuất. **Kiểm chứng:** TC31; cấu hình chạy và input path/HTML bất thường bị xử lý; địa chỉ listen được kiểm. Đây là phạm vi local, chưa đủ cho triển khai public. Nguồn: S07, IR02.

**NFR07 [M] — Thu thập có kiểm soát.** Collector phải dùng timeout, backoff/retry có giới hạn và delay/rate limit theo cấu hình, ghi policy skip khi nguồn không cho phép và không vòng lặp vô hạn. **Kiểm chứng:** TC03, TC05; lỗi 429/503 và policy block có log, dừng đúng cap. Nguồn: S03, PF02.

**NFR08 [M] — Bảo trì và chẩn đoán.** Adapter, parser, validation rules và công thức phải có version nhận diện, log rule/source errors và cấu hình tách khỏi dữ liệu; đổi một adapter không cần viết lại module phân tích. **Kiểm chứng:** TC08, TC26; inspection cấu trúc/config và manifest xác định version dùng cho mỗi output. Nguồn: S03, S07.

**NFR09 [M] — Khôi phục và lưu giữ.** Backup phải gồm database/raw/config/snapshots nhất quán; revisions và bằng chứng đang được snapshot tham chiếu không được tự xóa. **Kiểm chứng:** TC29; restore và checksum/replay đúng. Chưa đặt thời gian phục hồi/RPO số học vì local một người; mỗi mốc freeze phải có backup. Nguồn: S07, US07.

**NFR10 [M] — Đánh giá trung thực.** Báo cáo phải tách discovery/download/extraction tự động/review/aggregate, báo cả số đếm và tỷ lệ, cả missing và công sức; không dùng số mẫu development hoặc B2 sau review như accuracy tự động độc lập. **Kiểm chứng:** TC26, TC28; kiểm manifest split, công thức metric và cách diễn giải case. Ngưỡng 95% trước review chỉ mục tiêu thăm dò, không phải cổng chấp nhận đã chốt. Nguồn: S06, PF09.

## 9. Các giá trị vận hành đề xuất

| Tham số | Mặc định kế thừa v3.0 | Cách xử lý |
|---|---|---|
| HTTP connect/read timeout | 10 / 60 giây | Cấu hình từng nguồn; quá hạn ghi failed |
| Retry transient error | Tối đa 3 lần retry sau lần đầu | Backoff 2, 4, 8 giây hoặc Retry-After trong giới hạn run; không retry vô hạn |
| Delay giữa request cùng nguồn | Tối thiểu 2 giây | Nguồn có yêu cầu chặt hơn dùng giá trị chặt hơn |
| Raw file tối đa | 100 MiB/file | Streaming cap; quá cap cần cấu hình có lý do, chưa tải thành công |
| Discovery cap | 100 trang/run/nguồn | Chạm cap ghi incomplete, không kết luận coverage complete |
| Số financial targets | 6/report | Missing vẫn giữ trong denominator |
| UI benchmark | 24 báo cáo, 144 targets, ≤200 notices | Chỉ bộ dữ liệu local đã lưu; không cap kho dữ liệu bằng benchmark |
| Bản backup | Tại mỗi freeze mẫu/snapshot nghiệm thu | Đường dẫn/manifest và checksum ghi trong hồ sơ |

Các giá trị mới là cấu hình đề xuất, không kết quả đo hoặc đòi hỏi của ISO. Nếu pilot cho thấy không phù hợp, thay bằng change record trước freeze nghiệm thu. Run phải ghi config thực tế. Cần báo incomplete khi hết cap/window còn nghi ngờ thiếu nguồn.

## 10. Kiểm chứng và nghiệm thu

### 10.1. Phương pháp và cổng chấp nhận

T=Test có expected/actual; D=Demonstration luồng sử dụng; I=Inspection tài liệu/schema/UI/log; A=Analysis đối chiếu dữ liệu/metric. Các TC dưới đây là kế hoạch kiểm chứng, chưa phải test đã chạy. TC fixture kiểm quy tắc, tài liệu thật kiểm khả năng hoạt động; hai loại phải tách trong báo cáo.

Cổng nghiệm thu: (1) tất cả yêu cầu M có hồ sơ pass hoặc change record được chấp nhận thay đổi phạm vi; (2) pilot 9 báo cáo và ledger 54 targets đã được rà, missing được báo đúng; (3) có discovery tự động thật cho cả BCTC và cổ tức, manual fallback đếm riêng; (4) 100% số xuất bản có provenance, phép tính/lifecycle fixtures pass; (5) export/replay/restore qua kiểm chứng; (6) gold/holdout và công sức có báo cáo; (7) ba case thật, README và demo. Pilot đủ 9 reports không đồng nghĩa đủ mọi field/notice. Không nghiệm thu complete_as_of nếu còn unresolved ảnh hưởng.

Nếu gate tuần 4 không đạt discovery cổ tức, đây là thiếu yêu cầu FR04 cần đổi phạm vi có ghi nhận, không được tự đánh dấu pass bằng nhập tay. Kết quả extraction thấp phải được công bố và xử lý trong review; SRS không đưa một ngưỡng phần trăm chưa có pilot thành cam kết chất lượng tự động.

### 10.2. Danh mục tình huống kiểm chứng

| TC / phương pháp | Đầu vào và kết quả bắt buộc |
|---|---|
| TC01 — T/I | 3 issuers×3 năm: 9 report targets/54 metric targets; thiếu/chưa duyệt có trạng thái; thay scope tạo manifest mới |
| TC02 — D/I | Một seed danh mục BCTC và một seed danh mục notices thật: log phân trang/cửa sổ tới tài liệu thuộc pilot; seed từng file đếm assisted |
| TC03 — T | HTTP timeout/404/429/503, HTML giả PDF, PDF hỏng/quá100MiB, policy block: đúng failed/skipped, retry cap, không raw hợp lệ giả |
| TC04 — T | 200→304→200 cùng hash→200 khác hash và hai URL cùng content: số versions/relations đúng, raw trước không đổi |
| TC05 — T | Ngắt run sau tải, lỗi cache, resume và assisted import: dữ liệu không nhân bản, failed thử lại, policy/config có log |
| TC06 — T/A | PDF text+scan, ngoặc âm, triệu/nghìn, zero/gạch/missing: đúng value/unit/status và OCR provenance |
| TC07 — T/A | Bảng current/comparative, riêng/hợp nhất, năm ngắn/restated: chọn đúng context hoặc ambiguous; không mix revision/scope |
| TC08 — T/I | Kiểm locator/hash/version/parser và ngày chỉ-date/timezone unknown/first_seen: không thêm metadata giả; thiếu provenance chặn publish |
| TC09 — T/A | Notice 950 cho FY2023 +1500 cho FY2024: hai components tổng2450; % thiếu mệnh giá/basis hoặc profit_year chưa rõ bị chặn |
| TC10 — T | Cân đối đúng/lệch/thiếu operand/rounding unknown; blocking vs warning: issue đúng rule/tolerance, missing trả not_checkable |
| TC11 — T/I | Duyệt/sửa/từ chối 2 lần và lỗi commit: đủ audit trước–sau, pending không xuất, rollback không dữ liệu nửa chừng |
| TC12 — T | Hai facts cùng khóa khác giá trị/restated, alias ticker, source mới: revisions giữ riêng, reviewed selection rõ, snapshot cũ không đổi |
| TC13 — T/A | 2 routes/2 sources cùng đợt và 2 đợt thật cùng ticker/ngày/DPS: duplicate không cộng hai lần; distinct không tự gộp |
| TC14 — T/A | Sửa metadata/schedule và amount: DPS giữ hoặc thay đúng loại, timeline giữ old/current; không cộng bản cũ+mới |
| TC15 — T/A | Hủy record notice, policy cancellation có nguồn, payment date đã qua/paid có nguồn: đúng đối tượng, không annual zero giả hoặc paid giả |
| TC16 — T | Basis compatible/unknown/changed, components nhiều năm: tổng chỉ khi hợp lệ, không CFO/DPS hoặc tự split-adjust |
| TC17 — T/I | complete_as_of/partial/unknown/declared_zero/not_applicable, unresolved mới: annual null khi thiếu; zero phải có nguồn; coverage có ledger |
| TC18 — T/A | LNST/CFO 100/90→120/40→80/−10 cùng scope: delta LNST20,−40; growth20%,−33,333…%; CFO/LNST0,9;1/3;−0,125. Nền≤0/missing bị chặn đúng |
| TC19 — T/A | Cash70/assets1200; liabilities660/assets1200: 5,833…% và55%; assets≤0/cross-scope/thiếu operand không giá trị |
| TC20 — T | DPS1000→1500→1400 complete/basis phù hợp: growth50%,−6,666…%; đổi năm thành partial hoặc basis unknown chặn annual comparison |
| TC21 — T/D | Chọn doanh nghiệp/năm/scope trên fixture đủ/thiếu: bảng và biểu đồ dùng đúng dữ liệu, đơn vị riêng; missing có lý do/khoảng trống, không thành zero; đổi bộ chọn không trộn kỳ/scope |
| TC23 — D/I | Chọn ratio/tổng DPS/case bất kỳ trong published set: mở toàn bộ operands/components/raw locators; quét100% provenance không mồ côi |
| TC24 — T/I | Export UTF-8 với tiếng Việt/âm/zero/null/partial và raw evidence: manifest/schema/checksum đầy đủ; roundtrip đúng; gói thiếu bằng chứng gắn incomplete |
| TC25 — T | Export snapshot→update amount/fact→replay offline: kết quả cũ exact VND, ratios/growth tolerance10^-9; checksum sai/version lạ báo lỗi |
| TC26 — A/I | Gold freeze, development/holdout tách theo artifact lineage, B0/B1/B2: đúng tử/mẫu/missing/joint metrics và log effort; tự kiểm được khai báo |
| TC27 — T | Fault injection giữa transaction, foreign key sai và duplicate logical keys: rollback/ràng buộc đúng, không nhân fact khi join components |
| TC28 — D/A | Ba case từ tài liệu thật: có số, nguồn, scope/as_of/coverage và giới hạn; không gọi fixture là dữ liệu thu thập hoặc suy nhân quả |
| TC29 — T/D | Backup→restore thư mục sạch: DB/raw/config hashes và references đúng, replay ít nhất1 snapshot; README đủ thực hiện |
| TC30 — T/A | Bộ24 reports/144 targets/≤200 notices,20 thao tác warm cache: p95≤3s; ghi máy/phiên bản/phép đo và không trộn network/OCR |
| TC31 — T/I | Kiểm localhost, HTML không execute, export/import path traversal và secret log: bị chặn/ẩn phù hợp, không public listener mặc định |

TC18–TC21 là số giả định để kiểm phép tính, không phải kết quả doanh nghiệp. Ca thật VNM nhiều năm, VC7 sửa lịch và SVC hủy quyền trong S02 có thể dùng development/demonstration; không đưa bản gần giống của chúng vào holdout rồi gọi độc lập.

### 10.3. Thiết kế đo chất lượng dữ liệu

Freeze issuer/year/scope, raw versions, expected targets và notice/component gold trước đo. Tách development và holdout theo lineage; bản dịch/route/bản sửa gần giống không nằm hai phía. Mục tiêu holdout sau mở rộng là 5–8 tài liệu×6 targets=30–48 ô và notices khác development; cỡ mẫu thật chốt tại TBD03, mẫu nhỏ phải nêu giới hạn. Nếu chỉ còn pilot nhỏ, báo toàn bộ số đếm và hình thức kiểm, không giả lực thống kê.

Financial joint-correct phải đúng đồng thời metric/value/unit/period/scope; denominator gồm targets missing. Event/component joint-correct phải đúng fields gold tương ứng; precision/recall theo ledger đã rà. Discovery precision/coverage báo trên expected đã công bố có xác nhận, khác extraction. B0=text-only; B1=text+OCR/parser; B2=B1+review. Đo cả lỗi trước và sau review, phút review/tài liệu, effort sửa adapter và nhập tay tương đương. Không coi B2 là accuracy tự động.

Hồ sơ mỗi TC/yêu cầu gồm: id, manifest đầu vào, phiên bản code/config, expected, actual, phương pháp, pass/fail/not_run, người/ngày chạy và đường dẫn bằng chứng. SRS hôm nay chỉ kiểm chất lượng tài liệu và truy vết, không xác nhận app pass TC.

## 11. Ma trận truy vết

Các mã BR là ràng buộc nghiệp vụ được kiểm chứng qua FR/DR liên quan. Ma trận dưới đây bao phủ mọi yêu cầu FR, DR, IR, NFR; mỗi dòng có nguồn nhu cầu, luồng, khối dự kiến và TC. Chưa phân bổ tên file code vì kiến trúc chi tiết có thể thay đổi.

| Yêu cầu | Nguồn / nghiệp vụ | UC | Khối dự kiến | Kiểm chứng |
|---|---|---|---|---|
| FR01 | S01/PF01/US01 | UC01 | Catalog | TC01 |
| FR02 | S01/US01/BR03,BR09 | UC01,UC06 | Coverage | TC01,TC17 |
| FR03 | S03/PF02 | UC02 | Collector | TC02 |
| FR04 | S03/PF02 | UC02 | Collector | TC02 |
| FR05 | S03/PF02 | UC02 | Collector | TC03 |
| FR06 | S03/PF05/BR06 | UC02 | Raw store | TC04 |
| FR07 | S03/PF05 | UC02 | Run manager | TC05 |
| FR08 | S03/PF02 | UC02 | Import | TC05 |
| FR09 | S04/PF03/BR01,BR02 | UC03 | Extractor | TC06,TC07 |
| FR10 | S03/PF03 | UC03 | OCR | TC06 |
| FR11 | S04/US04/BR03,BR05 | UC03 | Normalizer | TC06 |
| FR12 | S03/US05 | UC03,UC04 | Provenance | TC08,TC23 |
| FR13 | S05/US03/BR04,BR05 | UC03 | Event parser | TC09 |
| FR14 | S04,S06/PF04/BR01 | UC03,UC04 | Validator | TC10 |
| FR15 | S01/US06 | UC04 | Review UI | TC10 |
| FR16 | S01/US06 | UC04,UC05 | Audit | TC11 |
| FR17 | S07/US06 | UC04 | Store | TC11,TC27 |
| FR18 | S02/US05/BR12 | UC04 | Revision | TC12 |
| FR19 | S05/US03/BR06 | UC05 | Event identity | TC13 |
| FR20 | S02/US03/BR07 | UC05 | Lifecycle | TC14,TC15 |
| FR21 | S05/AN05/BR08 | UC05,UC06 | Timeline | TC08,TC14 |
| FR22 | S05/US03/BR08 | UC05 | Payment evidence | TC15 |
| FR23 | S05/AN04/BR04,BR05,BR10 | UC05,UC06 | Aggregate | TC16,TC17 |
| FR24 | S05/US01/BR09 | UC05 | Coverage | TC17 |
| FR25 | S01/AN01/BR01,BR11 | UC06 | Analytics | TC18 |
| FR26 | S01/AN02/BR02 | UC06 | Analytics | TC18 |
| FR27 | S04/AN03/BR01,BR11 | UC06 | Analytics | TC19 |
| FR28 | S05/AN04/BR05,BR11 | UC06 | Analytics | TC20 |
| FR31 | S01/US05 | UC06 | Evidence UI | TC23 |
| FR32 | S01/US01–US04/PF08 | UC06 | Dashboard | TC21,TC23 |
| FR33 | S03/PF08 | UC02,UC07 | Run UI | TC03,TC05,TC24 |
| FR34 | S01/US07 | UC07 | Export | TC24 |
| FR35 | S01/US07/BR12 | UC07 | Replay | TC25 |
| FR36 | S06/PF09 | UC08 | Evaluation | TC26 |
| FR37 | S06/US08 | UC08 | Case report | TC28 |
| FR38 | S07/US07 | UC08 | Backup | TC29 |
| DR01 | S07/PF05/BR12 | UC01,UC04 | Schema | TC12,TC27 |
| DR02 | S04/PF03/BR05 | UC03,UC06 | Numeric types | TC06,TC18 |
| DR03 | S03/US05 | UC03,UC06 | Provenance | TC08,TC23 |
| DR04 | S05/AN05/BR08 | UC02,UC05 | Time model | TC08 |
| DR05 | S05/US01/BR03,BR09 | UC05,UC06 | Status model | TC17,TC21 |
| DR06 | S07/US06–US07/BR12 | UC04,UC07 | Revision store | TC11,TC12,TC25 |
| DR07 | S05/US03/BR09 | UC05 | Ledger | TC17 |
| DR08 | S01/US07 | UC07 | Snapshot schema | TC24,TC25 |
| IR01 | S03/PF02 | UC02 | HTTP adapter | TC02,TC03,TC04,TC05 |
| IR02 | S03/PF03 | UC02,UC03 | Import boundary | TC03,TC05 |
| IR03 | S01/PF08 | UC06 | UI | TC21,TC23 |
| IR04 | S01/US07 | UC07 | Export schema | TC24 |
| IR05 | S07/PF09 | UC02,UC08 | CLI/config | TC26,TC29 |
| NFR01 | S06/P05 | UC03,UC06 | Quality gate | TC23,TC26 |
| NFR02 | S06/US07 | UC07 | Replay | TC25 |
| NFR03 | S03,S07 | UC02,UC04 | Reliability | TC05,TC27 |
| NFR04 | S08/US01/TBD04 | UC06 | Performance | TC30 |
| NFR05 | S01/US01,US04 | UC06 | Usability | TC21,TC23 |
| NFR06 | S07/IR02 | UC02,UC07 | Local safety | TC31 |
| NFR07 | S03/PF02 | UC02 | HTTP policy | TC03,TC05 |
| NFR08 | S03,S07 | UC03,UC08 | Config/version | TC08,TC26 |
| NFR09 | S07/US07 | UC08 | Backup | TC29 |
| NFR10 | S06/PF09 | UC08 | Evaluation | TC26,TC28 |

## 12. Điểm mở và quản lý thay đổi

### 12.1. Các điểm cần xác nhận

| Mã | Điểm mở / quyết định cần có | Chủ trì và mốc đóng | Ảnh hưởng nếu chưa đóng |
|---|---|---|---|
| TBD01 | Rubric trường, yêu cầu tài liệu, có bắt buộc AI hay không, người phê duyệt | Sinh viên + giảng viên, tuần1–2 | Chưa tuyên bố đủ điều kiện môn học/tốt nghiệp |
| TBD02 | 3 issuers pilot, scope/năm thực tế, domain/window và policy nguồn; discovery notices có chạy được | Sinh viên, pilot và gate tuần4 | Không nghiệm thu FR03/FR04; cần change record nếu giảm phạm vi |
| TBD03 | Cỡ holdout, gold annotator/checker và các notices ngoài development | Sinh viên, trước freeze tuần8 | Chưa báo accuracy độc lập hoặc coverage toàn tập |
| TBD04 | Máy benchmark, phiên bản dependency và tính phù hợp ngưỡng3s/config cap | Sinh viên, trước freeze nghiệm thu | NFR04/config đề xuất chưa có bằng chứng đo |
| TBD05 | Rounding policy, mapping chỉ tiêu/basis và conflicts thực tế của từng nguồn | Sinh viên, trong pilot trước duyệt dataset | Không auto-pass balance/aggregate còn mơ hồ |
| TBD06 | Người dùng thử độc lập hoặc tự walkthrough, tập nhiệm vụ và phép đo effort | Sinh viên, tuần10–12 | Báo rõ tự đánh giá, chưa chứng minh lợi ích với người dùng ngoài |

TBD không cho phép bỏ qua yêu cầu tương ứng. Có thể thiết kế/triển khai các luồng hiện đã rõ; trước freeze hoặc nghiệm thu phải đóng điểm mở hay ghi thay đổi được chấp nhận. Không cần mua/cài skill để đóng những quyết định nghiệp vụ này.

### 12.2. Quy trình và vòng đời thực hiện

Áp dụng phát triển lặp có các gate: tuần1–2 rà SRS/danh mục; tuần3–4 pilot discovery/extraction/review và gate cỡ mẫu; tuần5–7 hoàn thiện lifecycle/analysis/UI; tuần8 freeze holdout; tuần9–11 đánh giá/snapshot/restore; tuần12–13 hoàn thiện hồ sơ và demo. Lộ trình chi tiết theo S08. SRS là tài liệu sống có baseline, không yêu cầu waterfall cứng hay viết xong toàn bộ UML trước khi thử nguồn.

Change record gồm mã CR, lý do, yêu cầu/dữ liệu bị ảnh hưởng, tác động thời gian/test, quyết định người sở hữu và phiên bản SRS mới. Sau khi giảng viên chấp nhận baseline, thay đổi phạm vi nghiệm thu cần ghi người chấp nhận tương ứng. Không xóa mã yêu cầu; ghi superseded và mã thay thế. Sinh bản Word lại sau khi sửa nguồn Markdown; kết quả kiểm chứng cập nhật theo version đã dùng.

UC và hợp đồng dữ liệu trong SRS đủ cho bước kế tiếp là ERD, sơ đồ kiến trúc/luồng và thiết kế chi tiết. Sequence diagram chỉ cần cho collection/review transaction/lifecycle/replay khi giúp giải quyết thiết kế. UML không tự thay thế acceptance criteria. Tài liệu này không bắt buộc tuân theo một bộ biểu mẫu trường chưa cung cấp.

### 12.3. Phần mở rộng tốt nghiệp

Ưu tiên nhánh đối chiếu phiên bản nguồn và giải thích tác động của metadata/schedule/amount/revision lên ratios, aggregates và cases. Project đã giữ versions/lineage để tạo nền, nhưng không bắt buộc triển khai semantic diff/impact engine đầy đủ hoặc đạt tập khoảng10 chuỗi bản sửa thật trong MVP. Các nhánh ML/predictor chỉ lập SRS riêng sau khi chứng minh labels/time window/sample/no leakage và rubric phù hợp. Không thêm chúng vào mẫu số nghiệm thu hiện tại.

## 13. Thuật ngữ

| Thuật ngữ | Nghĩa trong tài liệu |
|---|---|
| BCTC / LNST | Báo cáo tài chính / lợi nhuận sau thuế |
| CFO | Cash flow from operating activities: dòng tiền thuần hoạt động kinh doanh |
| DPS | Dividend per share: mức cổ tức tiền mặt trên mỗi cổ phiếu |
| Scope | Phạm vi báo cáo: hợp nhất hoặc cấp doanh nghiệp đã xác nhận |
| Profit year | Năm lợi nhuận mà component cổ tức thuộc về theo văn bản |
| Share basis | Cơ sở cổ phiếu/quyền dùng để hiểu và so mức DPS |
| Candidate / reviewed fact | Kết quả trích chưa duyệt / số có nguồn đã được duyệt |
| Provenance / lineage | Bằng chứng nguồn của số / chuỗi quan hệ nguồn–xử lý–kết quả |
| Revision | Phiên bản giá trị/ngữ nghĩa đã giữ lịch sử, không chỉ URL mới |
| Coverage | Mức đã rà nguồn cho một tập/cửa sổ/as_of, khác accuracy |
| Observed DPS | Tổng phần quan sát hợp lệ; chưa chắc toàn bộ mức năm |
| Annual announced DPS | Mức năm công bố với coverage complete_as_of và basis phù hợp |
| Declared zero | Bằng chứng duyệt doanh nghiệp công bố mức0/không chia cho năm tương ứng |
| Snapshot | Gói inputs/versions/config/coverage cố định dùng để tái lập |
| Gold / holdout | Dữ liệu đối chiếu thủ công / tập đánh giá chưa dùng chỉnh parser |
| Policy / execution | Chính sách/mức công bố cổ tức / đối tượng lịch và thực hiện quyền |

## 14. Checklist rà soát SRS

Đã xác định 5 BUC cấp hệ thống; giữ 8 UC phân rã nền tại mục 17 và 3 UC-E ở mục 15; định danh 36 FR còn hoạt động, 12 BR, 8 DR, 5 IR, 10 NFR; có 30 TC nền còn hoạt động, thêm 10 E/11 P ở mục 15. Ma trận bao phủ FR/DR/IR/NFR và liên kết BR; mỗi BR có TC tại mục 4. Thông số mới là đề xuất; điểm chưa biết nằm trong TBD.

V3.3 kế thừa baseline và CR-DIV-02, rút bốn yêu cầu/ba TC tại mục18; mục16 còn 10 D/10 TC-D: tổng 91 mã yêu cầu hoạt động, 51 tình huống kiểm chứng dự kiến; đủ để rà soát và bắt đầu thiết kế/triển khai. Chưa ghi phê duyệt hoặc kết quả kiểm thử ứng dụng. Chỉ đổi trạng thái “đã phê duyệt” khi có người, ngày và quyết định thực tế theo TBD01.

## 15. Tích hợp hướng kết hợp lợi nhuận dòng tiền và cổ tức

### 15.1. Change record CR-PCD-01

Ngày cập nhật 05/10/2026, theo yêu cầu của người thực hiện sửa tài liệu theo hướng mới. Đây là quyết định tích hợp tài liệu và phạm vi dự thảo; chưa có tên/ngày phê duyệt của giảng viên. Khi ghi nhận CR-PCD-01 ngày 05/10, v3.1 là nguồn hiện hành; hiện được kế thừa bởi v3.3/CR-AN-03. Hồ sơ ADD-FAP-PCD-01 là nguồn giải thích/nghiên cứu, không còn bộ nghĩa vụ nghiệm thu song song.

Giữ 3 doanh nghiệp phi tài chính × 2023–2025, sáu facts/BCTC, discovery hai loại nguồn, lifecycle, review, provenance và replay. Thêm một ca cầu nối CFO thật bắt buộc; mục tiêu 1–3 ca, ca thêm chỉ sau gate giờ/nguồn. Không đồng thời cam kết tăng mẫu lên 5–8 doanh nghiệp và tăng chiều sâu. Cầu nối được nhập/duyệt thủ công có ghi phút là phương án hợp lệ cho ca, không thay nghĩa vụ discovery tự động.

Quỹ nền 143 giờ được giữ; dành thêm 24 giờ dự toán cho cầu nối tối thiểu (tổng 167 giờ), chưa phải quỹ giờ người thực hiện xác nhận. Ước lượng nghiên cứu 24–40 giờ vẫn có rủi ro. G4 phải so giờ còn lại với effort quan sát; nếu chỉ có 10–12 giờ/tuần thì cần phân bổ lại/lùi hạn hoặc CR giảm nghĩa vụ, không tuyên bố 167 giờ nằm trong 143 giờ. Chưa đạt G4 thì giữ công việc cầu nối pending, không đánh pass. Rubric vẫn ở TBD01.

Nguồn: [nghiệp vụ cầu nối](../research-profit-cash-dividend/03-nghiep-vu-va-tu-dien.md), [thiết kế chi tiết](../research-profit-cash-dividend/05-thiet-ke-va-workflow.md), [ca DHG/VNM](../research-profit-cash-dividend/08-ca-thuc-te-dhg-vnm.md), [protocol P01–P11](../research-profit-cash-dividend/07-ke-hoach-thi-nghiem-va-kiem-thu.md).

### 15.2. Yêu cầu bổ sung có hiệu lực trong dự thảo

E giữ mã nghiên cứu để truy vết. M áp dụng cho ca tối thiểu; C áp dụng khi chọn ca thêm/góc nhìn bổ sung và phải ghi quyết định. Tất cả ban đầu chưa kiểm chứng.

**E01 — M:** Lưu phương pháp gián tiếp/trực tiếp/unknown, điểm bắt đầu, kỳ, scope, đơn vị và report version. Thiếu context không xuất bridge hoàn chỉnh. Kiểm P04,P05.

**E02 — M:** Mỗi dòng lưu role leaf/subtotal/total, group, raw label/code, giá trị có dấu, locator, review và quan hệ cha–con; subtotal chỉ để đối chiếu, không cộng lại. Kiểm P02,P04,P10.

**E03 — M:** Tính CFO từ điểm đầu và leaves bằng số chính xác; residual=CFO báo cáo−CFO tính, tolerance theo độ làm tròn nguồn. Đối chiếu ít nhất một ca thật; residual0 chưa đủ chứng minh completeness. Kiểm P01,P02,P03,P09.

**E04 — M:** Thiếu dòng/sai scope/không rõ phương pháp trả status và lý do; partial không gắn reconciled_complete, residual không được đặt thành nguyên nhân kinh tế tự tạo. Kiểm P03,P04,P05.

**E05 — C:** Khi chọn phân tích hai năm, chỉ so bridge có kỳ/scope/mapping tương thích; delta CFO bằng delta start+delta groups+delta residual trong tolerance; lưu phiên bản nguồn của cột so sánh. Kiểm P06.

**E06 — M:** Hiển thị LNST cạnh cầu nối LNTT→CFO và ghi đúng điểm bắt đầu. Không đảo LNST thành LNTT bằng thuế thực nộp; muốn dùng LNST phải có chi phí thuế hiện hành/hoãn lại được duyệt. Kiểm P01,P04,P09.

**E07 — M:** Case nối với DPS theo profit_year, timeline riêng và coverage/basis/as_of. Partial không là annual đầy đủ; scheduled không là paid. Không chia CFO cho DPS khác đơn vị. Kiểm P07,P08,P09.

**E08 — M:** Mở kết quả cầu nối/case phải thấy toàn bộ operands/source; export/replay lưu reviewed lines, raw hashes, mapping/formula version và coverage. Snapshot cũ không đổi sau sửa dữ liệu. Kiểm P10,TC23–TC25.

**E09 — M:** Ghi giờ nhập/review/correct theo ca, chất lượng trước/sau duyệt và hình thức tự đánh giá/người kiểm. Đầu ra phải có ít nhất một ca thật đọc được, không gọi fixture là dữ liệu doanh nghiệp. Kiểm P11,TC26,TC28.

**E10 — C:** Nếu chọn góc dòng tiền thực chi, chỉ so CFO với dòng chi chủ sở hữu cùng kỳ/scope và nhãn BCLCTT; mẫu số dương, không gán dòng này vào profit_year hay coi lịch là thực trả. Kiểm P08,P09.

### 15.3. Use case và hợp đồng dữ liệu

UC-E01: chọn report/period/scope → trích hoặc nhập rows → duyệt dấu/role/locator → kiểm tổng/CFO → lưu bridge result và audit trong cùng transaction; thiếu thì partial+issue.

UC-E02: chọn snapshot/case → xem LNST/CFO và cầu nối → mở nguồn từng khoản → đối chiếu DPS profit_year và timeline → xuất case kèm phần chưa biết. Annual DPS chưa đủ vẫn đọc bridge, không kết luận cổ tức cả năm.

UC-E03: raw version mới → candidates/review mới → snapshot mới; snapshot cũ giữ nguyên. Semantic impact engine đầy đủ vẫn thuộc nhánh tốt nghiệp.

Schema bổ sung gồm bridge_definitions, bridge_lines, bridge_results, bridge_operands, analysis_cases và case_evidence theo tài liệu thiết kế nguồn. Khóa report_version/period/scope tách biệt khóa security/event/component. Mỗi leaf chỉ một lần trong operands. Snapshot chứa completeness/status/residual/tolerance, mapping/formula version và mọi dòng đã duyệt; không tham chiếu live mapping khi replay.

Phương pháp gián tiếp: CFO tính=start+Σleaves; không cộng subtotal cùng children. Phương pháp trực tiếp: trình bày nhóm thu–chi đúng báo cáo, không dựng cầu nối gián tiếp giả. Ca tối thiểu chọn tài liệu gián tiếp đủ dòng; tài liệu trực tiếp/unknown dùng kiểm hành vi chặn. Residual không dùng để tự suy tồn kho/phải thu hoặc nguồn tài trợ cổ tức.

### 15.4. Truy vết và kiểm chứng bổ sung

| Yêu cầu | Nguồn nhu cầu | Luồng | Khối | Kiểm chứng |
|---|---|---|---|---|
| E01 | Vì sao CFO khác lợi nhuận; nghiên cứu 03 | UC-E01 | bridge_mapper | P04,P05 |
| E02 | Truy nguồn từng dòng; nghiên cứu 05 | UC-E01,UC-E03 | store/bridge_mapper | P02,P04,P10 |
| E03 | Đối chiếu số học; nghiên cứu 03/08 | UC-E01 | bridge_validator | P01,P02,P03,P09 |
| E04 | Không suy diễn phần thiếu; nghiên cứu 03 | UC-E01,UC-E02 | bridge_validator | P03,P04,P05 |
| E05 | Dòng nào đóng góp biến động; nghiên cứu 03 | UC-E02 | bridge_compare | P06 |
| E06 | Phân biệt LNST và LNTT; nghiên cứu 03 | UC-E02 | UI | P01,P04,P09 |
| E07 | Quan hệ cổ tức đúng góc nhìn; nghiên cứu 03/08 | UC-E02 | case_composer | P07,P08,P09 |
| E08 | Tái lập nguồn và kết quả; nghiên cứu 05 | UC-E02,UC-E03 | snapshot | P10,TC23,TC24,TC25 |
| E09 | Giá trị so công sức; nghiên cứu 07 | UC-E01,UC-E02 | evaluation | P11,TC26,TC28 |
| E10 | Dòng thực chi cùng kỳ; nghiên cứu 03 | UC-E02 | case_composer | P08,P09 |

P01–P11 tại mục này là test cầu nối, dùng id hồ sơ PCD/P01…PCD/P11 để phân biệt P01–P06 vấn đề ở tài liệu 02. Input/expected tại protocol nguồn; hồ sơ dùng schema id/manifest/code/config/expected/actual/pass-fail-not_run/evidence như TC. P06 khi E05 chưa kích hoạt ghi not_applicable kèm quyết định; P08 vẫn kiểm không suy paid ở E07. Gold theo dòng tách lineage development/holdout; DHG đã dùng thiết kế không là holdout độc lập. Chưa có benchmark bridge tự động hoàn chỉnh.

V3.1 gồm 73 yêu cầu nền + 10 E = 83 mã (8 E bắt buộc, 2 E có điều kiện), 8 UC nền + 3 UC-E, 31 TC + 11 P = 42 tình huống dự kiến. Mẫu số áp dụng ghi riêng các C được kích hoạt; không coi cả 83 đã pass. Nghĩa vụ này thay trạng thái đề xuất độc lập của ADD-FAP-PCD-01.

## 16. Chức năng thẩm định bổ sung — CR-DIV-02

### 16.1. Kiểm soát thay đổi và điều kiện hiệu lực

Ngày 11/10/2026 theo yêu cầu người thực hiện nghiên cứu và bổ sung tài liệu. Tổ chức lại UC không thêm nghĩa vụ nền; ba chức năng mới thêm D01–D12. Trạng thái: dự thảo đã tích hợp tài liệu, chưa phê duyệt giảng viên/chưa nghiệm thu ứng dụng. Mức C-D: bắt buộc cho ca/pilot chức năng tương ứng khi phạm vi triển khai được ghi vào manifest; không cam kết CAPEX/D/action cho mọi báo cáo. Tối thiểu đề xuất một ca G02, một ca G03 có chain/basis xác nhận đầy đủ và một trường hợp bị chặn có bằng chứng, và một workflow lưu nhận xét/dossier; phần criteria/screening G01 đã rút tại mục18; chưa được gọi chức năng hoàn chỉnh nếu chỉ hàm tính chạy.

Điểm mở DIV-TBD01: quỹ thêm 64–98 giờ, ca pilot và số người thử; DIV-TBD02: định nghĩa CAPEX/D và phạm vi chủ thể; DIV-TBD03: loại sự kiện/ngày basis đủ chứng cứ; DIV-TBD04: tập tác vụ lưu/đối chiếu và gold độc lập; bộ tiêu chí sàng lọc đã rút. Chủ trì: người thực hiện, chốt trước nghiệm thu với giảng viên về phạm vi. Kế hoạch 167 giờ/checklist v3 là baseline lịch sử chưa gồm D01–D12; không khẳng định có đủ thời gian bằng cách giữ nguyên tổng giờ.

Chi tiết nghiệp vụ/thiết kế/khả thi trong S09. Nghiên cứu đã chạy probe độc lập 20 tests; TC-D của ứng dụng dưới đây vẫn not_run. G02 không gọi CFO−CAPEX là FCFE hoặc kết luận nguồn tài trợ; G03 không cộng cổ phiếu vào tiền nhận; G01 không gán điểm tổng/khuyến nghị lệnh.

### 16.2. Yêu cầu bổ sung theo UC lớn

**D01 [C-D/G02] — Dữ liệu chi đầu tư và phân phối.** Phải lưu CAPEX và tiền thực chi cùng kỳ/chủ thể/đơn vị với CFO, tên dòng/definition/kind, sign mapping, revisions và nguồn đã duyệt. Khoản gộp chủ sở hữu phải giữ nhãn gộp; announced DPS không được thay D thực chi. Chấp nhận: TC-D01. BUC01/02; S09/G02.

**D02 [C-D/G02] — Điều kiện tính riêng từng metric.** Phải chặn missing, sai issuer/kỳ/scope/unit hoặc chưa duyệt; null/reason riêng từng kết quả. CAPEX/D magnitude phải không âm; không abs che mapping sai. Chấp nhận: TC-D02. BUC02; BR01/BR03/BR11, S09/G02.

**D03 [C-D/G02] — Tính bao phủ tiền mặt.** Phải tính CFO−CAPEX, CFO−CAPEX−D và CFO/(CAPEX+D) khi tổng chi>0; CFO âm giữ dấu, tổng chi=0 chỉ làm tỷ số not_applicable. Kèm công thức/version/operands và diễn giải giới hạn. Chấp nhận: TC-D03. BUC02; S09/G02.

**D04 [C-D/G02] — Tra soát và xuất kết quả bao phủ.** Phải hiển thị định nghĩa khoản chi/phạm vi, đường tới nguồn, snapshot và lý do thiếu; xuất/replay cùng dữ liệu. Không hiển thị khoản gộp như cổ tức phổ thông đã tách. Chấp nhận: TC-D04. BUC02/05; FR31/34/35, S09/G02.

**D05 [C-D/G03] — Ledger sự kiện cổ phiếu.** Phải lưu loại, tỷ lệ gốc/factor, các mốc ngày tách riêng, nguồn, quy tắc phần lẻ và chuỗi sửa/hủy đã duyệt. Không suy ngày basis từ record/registration date. Chấp nhận: TC-D05. BUC01/03; S09/G03.

**D06 [C-D/G03] — DPS trên cơ sở tham chiếu.** Phải giữ raw DPS và tính DPS gốc/F trên basis mới cho chuỗi sự kiện được hỗ trợ/duyệt, F bằng tích factor>0; ghi chain và giả định lý thuyết. Không có sự kiện hợp lệ: F=1. Chấp nhận: TC-D06. BUC03; S09/G03.

**D07 [C-D/G03] — Chặn điều chỉnh thiếu cơ sở.** Phải bỏ canceled, chọn revision hiệu lực cho amended, chặn unresolved/unsupported/basis interval chưa xác nhận và dữ liệu tương lai theo as_of. Không double-adjust dữ liệu vendor hoặc EPS đã hồi tố. Chấp nhận: TC-D07. BUC03; BR05/BR07/BR11/BR12, S09/G03.

**D08 [C-D/G03] — Trình bày lịch sử so sánh được.** Phải hiển thị raw/reference basis và lý do khi không tính; annual growth vẫn đòi coverage/period hợp lệ theo FR28. Chưa đủ quyền vị thế không được báo thực nhận. Chấp nhận: TC-D08. BUC03; FR23/24/28, S09/G03.



**D11 [C-D/G01] — Hồ sơ thẩm định và công việc tra soát.** Phải lưu kết quả/bối cảnh doanh nghiệp-kỳ-chỉ tiêu, nhận xét người dùng tách facts, câu hỏi open/resolved có nguồn và author/time vào dossier gắn snapshot. Mở lại sau update giữ đúng phiên bản cũ. Chấp nhận: TC-D11. BUC05; S09/G01.

**D12 [C-D/G01] — Xuất và tái lập hồ sơ.** Phải freeze/export/replay context/results/notes/source refs với version/checksum; không dùng công thức mới âm thầm thay kết quả cũ. Chấp nhận: TC-D12. BUC05; FR34/35, S09/G01.

### 16.3. Tình huống kiểm chứng dự kiến

| Mã | Đầu vào / expected | Trạng thái ứng dụng |
|---|---|---|
| TC-D01 | Dòng CAPEX/36 gộp và notice DPS; nhập sign/kind đúng, DPS bị từ chối làm thực chi | not_run |
| TC-D02 | Thiếu/mismatch scope/kỳ/issuer/unit, chưa duyệt; null/reason, không zero | not_run |
| TC-D03 | DHG và fixture CFO âm/tổng chi0; số dư đúng, ratio null khi tổng chi0 | not_run |
| TC-D04 | Kết quả tới dòng nguồn/definition/snapshot, export giữ nhãn khoản gộp | not_run |
| TC-D05 | FPT 20:3 và floor phần lẻ; ngày riêng/null có reason, không suy basis | not_run |
| TC-D06 | Không sự kiện/một/nhiều/tách/gộp; factor/reference đúng và raw không đổi | not_run |
| TC-D07 | Canceled/amended/unresolved/unsupported/future/vendor adjusted; resolve hoặc chặn đúng | not_run |
| TC-D08 | Annual partial dù factor đủ; không growth, không thực nhận từ lịch | not_run |
| TC-D11 | Ghi note/task, xử lý có evidence; facts không đổi, dossier cũ không đổi sau update | not_run |
| TC-D12 | Freeze/replay dossier và checksum/version sai; đúng bản cũ hoặc lỗi có lý do | not_run |

### 16.4. Ma trận truy vết bổ sung

| Yêu cầu | Nguồn | UC lớn / phân rã | Kiểm chứng |
|---|---|---|---|
| D01 | S09/G02 | BUC01/BUC02 — B02.4a | TC-D01 |
| D02 | S09/G02 | BUC02 — B02.4b | TC-D02 |
| D03 | S09/G02 | BUC02 — B02.4b | TC-D03 |
| D04 | S09/G02 | BUC02/BUC05 — B02.4c | TC-D04 |
| D05 | S09/G03 | BUC01/BUC03 — B03.4a | TC-D05 |
| D06 | S09/G03 | BUC03 — B03.4b/c | TC-D06 |
| D07 | S09/G03 | BUC03 — B03.4b | TC-D07 |
| D08 | S09/G03 | BUC03 — B03.4d/5 | TC-D08 |
| D11 | S09/G01 | BUC05 — B05.1/2 | TC-D11 |
| D12 | S09/G01 | BUC05 — B05.4 | TC-D12 |

## 17. Các UC phân rã nền được bảo toàn từ v3.1

Các luồng dưới đây giữ nội dung/ID để không đứt trace tại mục 11 và checklist baseline; không tiếp tục coi là danh mục chức năng chính. UC01–04/08 thuộc BUC01; UC05 thuộc BUC03; UC06 được chia tiền mặt→BUC02, lịch sử→BUC03, chọn/đối chiếu→BUC04, truy xuất nguồn→BUC05; UC07 thuộc BUC05. Tên UC-E tại mục 15 vẫn là luồng phân rã hướng cầu nối.

### 17.2. UC01 — Thiết lập tập dữ liệu

**Tác nhân:** người vận hành. **Kích hoạt:** bắt đầu pilot hoặc đổi phạm vi đã duyệt. **Tiền điều kiện:** có cấu hình nguồn và danh mục doanh nghiệp hợp lệ.

Luồng chính: (1) chọn doanh nghiệp, năm, scope ưu tiên và thời điểm as_of; (2) lưu tập dự kiến gồm sáu targets/report và cửa sổ rà thông báo; (3) hiển thị ledger và lý do các mục chưa có; (4) xác nhận tập để dùng cho collection và đánh giá. Hậu điều kiện: có manifest phạm vi phiên bản hóa, chưa có mục missing nào bị đổi thành 0.

Ngoại lệ: mã doanh nghiệp chưa ánh xạ → yêu cầu xác nhận identity; kỳ không phải năm đầy đủ → ghi ngoài scope; thay phạm vi đã freeze → tạo phiên bản mới, giữ phiên bản cũ. Kiểm chứng: TC01.

### 17.3. UC02 — Thu và cập nhật tài liệu

**Tác nhân:** người vận hành, nguồn HTTP. **Kích hoạt:** chạy discovery hoặc cập nhật. **Tiền điều kiện:** có UC01 và chính sách nguồn.

Luồng chính: (1) truy danh mục/search và phân trang trong cửa sổ cấu hình; (2) ánh xạ link vào doanh nghiệp/kỳ/loại dự kiến; (3) tải với conditional request khi có; (4) kiểm tra content, giới hạn và hash; (5) ghi raw version, metadata và run log; (6) đưa bản mới vào hàng đợi trích. Hậu điều kiện: raw cũ giữ nguyên, ledger phản ánh success/skip/error, không trùng phiên bản khi chạy lại.

Ngoại lệ: 304 → kiểm cache, không sinh bản mới; timeout/404/HTML giả PDF → ghi lỗi và tiếp tục tài liệu khác; rate limit/policy → backoff/skip; cache hỏng → đánh dấu hỏng và tải lại hợp lệ; nguồn yêu cầu nhập tay → lưu provenance và nhãn assisted. Kiểm chứng: TC02–TC05.

### 17.4. UC03 — Trích và chuẩn hóa

**Tác nhân:** người vận hành. **Tiền điều kiện:** raw version hợp lệ. **Kích hoạt:** tài liệu mới hoặc yêu cầu xử lý lại.

Luồng chính: (1) đọc text/layout và metadata; (2) OCR trang cần thiết khi text thiếu/không dùng được; (3) tạo sáu financial candidates hoặc notice/components; (4) lưu raw value, quy tắc chuẩn hóa, locator và phiên bản parser; (5) chạy validation; (6) đưa vào review. Hậu điều kiện: candidates và issues gắn đúng raw version; chưa xuất bản số chưa duyệt.

Ngoại lệ: bảng/cột/kỳ/scope mơ hồ → giữ candidate ambiguous hoặc target missing; OCR lỗi → lưu lỗi, cho nhập tay có nguồn; notice hai năm → tạo hai components; không xác định profit_year/basis → giữ unresolved và chặn tổng tương ứng. Kiểm chứng: TC06–TC09.

### 17.5. UC04 — Review và xuất bản dữ liệu

**Tác nhân:** người vận hành. **Tiền điều kiện:** có candidates và nguồn mở được. **Kích hoạt:** mở hàng đợi review.

Luồng chính: (1) xem candidate, trang nguồn và issues; (2) duyệt, sửa hoặc từ chối; (3) ghi identity người vận hành local, thời gian, lý do và trước–sau; (4) giải quyết issue blocking bằng sửa có bằng chứng hoặc từ chối; (5) commit fact/component đã duyệt trong một transaction; (6) cập nhật phân tích phụ thuộc. Hậu điều kiện: bản xuất bản truy nguồn được, audit và dữ liệu nhất quán.

Ngoại lệ: nguồn/locator thiếu → chặn duyệt; hai bản cùng khóa mâu thuẫn → chọn revision theo bằng chứng, không lấy giá trị cuối ghi; lỗi giữa transaction → rollback; chấp nhận sai lệch chỉ được với issue warning và ghi lý do, không được bỏ qua thiếu unit/period/scope. Kiểm chứng: TC10–TC12, TC27.

### 17.6. UC05 — Xử lý vòng đời cổ tức

**Tác nhân:** người vận hành. **Kích hoạt:** notice mới, bản sửa/hủy hoặc nguồn đăng trùng. **Tiền điều kiện:** có raw và candidate event.

Luồng chính: (1) đối chiếu identity sự kiện và đối tượng bị thay đổi; (2) xác nhận liên kết duplicate/amends/cancels; (3) phân loại metadata, schedule, amount, rights cancellation hoặc unresolved; (4) duyệt component và trạng thái có hiệu lực; (5) review lại coverage từng profit_year; (6) tính lại tổng hợp hiện hành. Hậu điều kiện: một đợt không bị cộng nhiều lần, lịch sử không mất, snapshot cũ giữ nguyên.

Ngoại lệ: cùng ticker/ngày/DPS nhưng chưa chắc cùng đợt → giữ riêng, yêu cầu review; hủy ngày quyền chưa có thay thế → ngừng đối tượng thực hiện quyền bị hủy, đánh dấu coverage partial/unknown, không suy policy=0; paid date đã qua → vẫn scheduled. Kiểm chứng: TC13–TC17.

### 17.7. UC06 — Tra cứu và phân tích

**Tác nhân:** người đọc/người nghiên cứu. **Tiền điều kiện:** có snapshot dữ liệu đã duyệt. **Kích hoạt:** chọn doanh nghiệp, năm, scope và bộ lọc.

Luồng chính: (1) xem coverage và bảng sáu chỉ tiêu; (2) xem LNST/CFO và timeline DPS; (3) xem ratios/changes có điều kiện; (4) đối chiếu dữ liệu đã chọn; (5) mở operands/components và trang nguồn. Hậu điều kiện: kết quả ghi rõ as_of, scope, đơn vị, n và lý do loại.

Ngoại lệ: dữ liệu thiếu/không tương thích → trạng thái có lý do và khoảng trống đồ thị; phép tính không đủ operands → nêu lý do. Kiểm chứng: TC18–TC21, TC23.

### 17.8. UC07 — Xuất và replay snapshot

**Tác nhân:** người nghiên cứu. **Tiền điều kiện:** có dữ liệu đã duyệt và cấu hình phân tích. **Kích hoạt:** xuất snapshot hoặc mở gói cũ.

Luồng chính: (1) chọn tập và bộ lọc; (2) đóng băng facts/components, coverage, raw references và công thức/config; (3) xuất CSV, JSON, manifest và checksum; (4) kiểm tra gói; (5) replay bằng phiên bản công thức ghi trong manifest; (6) đối chiếu giá trị với kết quả đã lưu. Hậu điều kiện: snapshot tái tính được sau khi hệ thống có nguồn mới.

Ngoại lệ: raw thiếu/hỏng → báo gói chưa tự chứa đủ bằng chứng; phiên bản công thức không được hỗ trợ → từ chối replay có lý do, không âm thầm dùng công thức mới; gói sai checksum → báo invalid. Kiểm chứng: TC24–TC25.

### 17.9. UC08 — Đánh giá và khôi phục

**Tác nhân:** người vận hành/người kiểm thử. **Tiền điều kiện:** có tập gold/holdout freeze hoặc bản backup. **Kích hoạt:** nghiệm thu hoặc diễn tập phục hồi.

Luồng đánh giá: ghi manifest mẫu → chạy baseline/pipeline → đối chiếu từng target → báo số đếm, accuracy, missing, effort và ba case thật → lưu kết quả theo TC. Luồng phục hồi: sao lưu nhất quán database/raw/config → khôi phục thư mục sạch → kiểm checksum và replay một snapshot. Hậu điều kiện: có hồ sơ đánh giá hoặc dữ liệu khôi phục kiểm tra được. Không dùng dữ liệu development như holdout độc lập. Kiểm chứng: TC26–TC29.

## 18. CR-AN-03 — Rút chức năng tìm trường hợp và cập nhật góc nhìn sản phẩm

Ngày 11/10/2026, người thực hiện yêu cầu loại bỏ “Tìm và khám phá trường hợp cần chú ý”, ưu tiên người theo dõi tài chính doanh nghiệp/đầu tư và tổ chức UC lớn→nhỏ. Đây là quyết định phạm vi từ người thực hiện, chưa ghi thành phê duyệt giảng viên hoặc nghiệm thu ứng dụng.

### 18.1. Mã rút khỏi nghĩa vụ hiện hành

| ID giữ để truy vết | Trạng thái | Nội dung được rút |
|---|---|---|
| FR29 | withdrawn | Bộ lọc trường hợp theo biến động LNST/CFO/DPS |
| FR30 | withdrawn | Scatter/Spearman thuộc tác vụ khám phá trường hợp |
| D09 | withdrawn | Bộ tiêu chí sàng lọc có phiên bản |
| D10 | withdrawn | Đánh giá/sàng lọc pass/fail/unknown |
| TC22, TC-D09, TC-D10 | withdrawn | Các phép kiểm tương ứng, không thuộc nghiệm thu hiện hành |

Không tái sử dụng các ID trên cho chức năng khác. TC21 giữ kiểm bộ chọn/bảng/biểu đồ, FR32 chỉ tham chiếu FR25–28; BR11 bỏ nghĩa vụ Spearman. D11/12 giữ bối cảnh phân tích, nhận xét, câu hỏi, nguồn và snapshot; bỏ criteria sàng lọc. US08 và UC06 được điều chỉnh tương ứng. Tổng hoạt động: 36 FR+12 BR+8 DR+5 IR+10 NFR+10 E+10 D=91 yêu cầu; 30 TC+11 P+10 TC-D=51 tình huống dự kiến. Các hàng withdrawn ở đây là sổ quyết định, không là yêu cầu/TC đang hoạt động.

### 18.2. Người dùng và nhóm chức năng

[Danh mục yêu cầu dễ đọc v2.0](27-yeu-cau-chuc-nang-va-vi-du.md) tổ chức năm nhóm chính: khai thác dữ liệu, phân tích tài chính, so sánh doanh nghiệp, theo dõi doanh nghiệp/sự kiện, phân tích cổ tức; hai hướng mở rộng là danh mục và mô phỏng/định giá. Biểu đồ là chức năng nhỏ trong UC tương ứng. Thu/trích/chuẩn hóa/duyệt phục vụ nền dữ liệu; người vận hành hỗ trợ người dùng chính.

Năm BUC trong SRS được giữ làm nhóm truy vết nghĩa vụ đang có, cập nhật tên/luồng cho phù hợp. UC-F03/F04 và các nhánh phân tích mới chưa được thêm nghĩa vụ chỉ bởi có tên trong danh mục nghiên cứu. Bảng đa doanh nghiệp, biên lợi nhuận, cơ cấu chi tiết, DuPont, quý/kế hoạch, watchlist, danh mục và DCF/DDM cần change record riêng cho phần thực sự được chọn. Không đưa chức năng sàng lọc trở lại dưới tên cảnh báo hoặc theo dõi.

### 18.3. Nguồn, lịch sử và tiến độ

[Nghiên cứu 36 repo](../research-high-star-finance/README.md) có bảng số sao, nguồn mã và khả thi. [Snapshot trước cập nhật](history/before-user-removal-2026-10-11.zip) giữ văn bản trước khi rút. Bộ G01/probe và tài liệu đợt trước là lịch sử nghiên cứu; kết quả chạy độc lập không chứng minh chức năng đã tích hợp hoặc còn trong phạm vi.

Word v3.1 và checklist/kế hoạch 167 giờ là baseline trước cập nhật. Không sửa ngược lịch sử hoặc tick tiến độ; khi dùng checklist phải bỏ nghĩa vụ đã withdrawn theo mục này. Quỹ 64–98 giờ trước đây cần tính lại sau loại screening và chọn nhánh mới; chưa có ngân sách/lịch mới đã chốt. Ưu tiên lát cắt dữ liệu→biểu đồ→so sánh→nguồn→lưu, rồi phân tích sâu/cổ tức và theo dõi công bố.

### 18.4. CR-WEB-01 — Giữ kiến trúc web, ngày 11/10/2026

Người thực hiện yêu cầu giữ React/PostgreSQL và sửa tài liệu triển khai. Chọn React/TypeScript/Vite, FastAPI/Python 3.12, PostgreSQL với SQLAlchemy/Alembic; thay phương án pilot Streamlit/SQLite. PaddleOCR, sáu metrics, ba mã/chín báo cáo và thứ tự UC không đổi. Thiết kế mục 2.3, FR38 backup và IR05 giao diện/cấu hình được làm rõ theo web; không thêm ID nghĩa vụ hoặc đổi số 91 yêu cầu/51 ca kiểm hiện hành.

TC26/TC29 cần kiểm khởi chạy frontend/backend/DB và migration, dump/restore PostgreSQL cùng raw/config/snapshots; TC31 kiểm cả origin frontend/API local, giới hạn đường dẫn/tệp và thông tin cấu hình. Có thêm tiêu chí lát cắt API: dữ liệu chính xác dạng chuỗi, lỗi/loading/empty, revision conflict và bộ lọc export. Chưa ghi ca nào đã pass; tiêu chí web bổ sung được ghi riêng trong tuần 1–2, không tự đổi tổng số TC SRS.

Kế hoạch v6 dự toán 195 giờ, tuần 1/2 là 24/22 giờ, thay 178 giờ của v5; quỹ giờ thực chưa xác nhận. Web chạy local trước, chưa mở cloud hoặc nhiều người dùng. [Stack](31-chot-pham-vi-va-stack-paddleocr.md) và [kiến trúc](03-kien-truc-va-du-lieu.md) là nguồn thiết kế hiện hành; bản lịch sử và prototype giữ thông tin công nghệ thực sự đã dùng.
