# Backlog triển khai và sổ quyết định

## Góp ý ghi nhận 11/10/2026 — đợt nghiên cứu ưu tiên

**Kết quả khảo sát GitHub cùng ngày:** đã đọc nguồn/mã của [9 dự án](../research-github-dividend/README.md) và đề nghị G02 (bao phủ chi đầu tư/chi cổ tức), G03 (cơ sở cổ phiếu), G01 (hồ sơ thẩm định/sàng lọc có lý do). G01 tái dùng nhiều yêu cầu cũ; G02/G03 cần dữ liệu và change record nếu chọn. Đã tính ca giả lập độc lập, chưa chạy repository, chưa có kiểm chứng người dùng hoặc tích hợp tính năng.

Người thực hiện yêu cầu ghi nhớ góp ý và lên kế hoạch nghiên cứu sâu chức năng hỗ trợ đầu tư. [Kế hoạch chi tiết](26-ke-hoach-nghien-cuu-sau-gop-y-giang-vien.md) đề xuất đợt 12–18/10, 15 giờ chưa xác nhận; có phương án 12 giờ. Ưu tiên chọn UC hỗ trợ thẩm định cổ tức, ca tác động cổ tức bằng cổ phiếu, protocol và chạy thử PaddleOCR, rồi lát cắt chức năng/đánh giá. Đây là backlog nghiên cứu bổ sung; chưa đổi SRS, chưa thay engine OCR hoặc tick các việc triển khai hiện hành. Ngày ghi nhận không mặc định là ngày buổi gặp thầy.

## D14 và CR-PCD-01 ngày 05/10/2026

Theo yêu cầu cập nhật tài liệu dựa trên hướng mới, tích hợp cầu nối CFO vào SRS v3.1 và kế hoạch/checklist v3. Giữ sáu targets/pilot/lifecycle; một ca bắt buộc, 1–3 ca theo gate. Dự toán nền143 + cầu nối24 =167 giờ, chưa xác nhận thời gian thực; G4 quyết định tăng giờ/lùi hạn/CR thu hẹp nếu chỉ có10–12 giờ mỗi tuần. Không bỏ nghĩa vụ nền để làm cầu nối. Chưa có phê duyệt giảng viên hay test ứng dụng pass.

Backlog thêm: tuần1–4 chọn ca/đọc rows/đo effort; tuần5 schema và mapping; tuần6 validator/residual; tuần7 UI/case/provenance; tuần8 freeze gold/mapping; tuần9 đo; tuần10 replay; tuần11 regression/restore; tuần12–13 demo/bàn giao. E05 so cặp năm/E10 thực chi và tăng issuers phải có quyết định riêng. D09 giữ tên là lịch sử trước cập nhật tên diễn đạt theo hướng kết hợp.

**D13 — 04/10/2026:** kế hoạch [v2 theo SRS v3.0](04-ke-hoach-13-tuan.md) và [checklist đồng bộ](checklist-13-tuan.html) là backlog chi tiết hiện hành, gồm W01-01…W13-06, toàn bộ73 yêu cầu/31TC, outputs và gates. T01–T08 bên dưới là nhóm định hướng, không thay các việc/tiêu chí mới. Chuẩn bị holdout tuần7, freeze đầu tuần8 trước đo; version/cache từ tuần2, replay tuần10, restore/performance/safety tuần11. [Bắt đầu và mẫu hồ sơ](23-bat-dau-va-minh-chung-thuc-hien.md). Chưa tick tiến độ chỉ vì cập nhật kế hoạch.

## Quyết định đã thống nhất ngày 03/10/2026

| ID | Quyết định | Lý do |
|---|---|---|
| D01 | Một ngách lợi nhuận–CFO–cổ tức tiền mặt | Người thực hiện muốn tập trung và liên thông lên dự đoán |
| D02 | Project phân tích mô tả, predictor để tốt nghiệp | Nền học và dữ liệu chưa đủ cho mô hình |
| D03 | Target là DPS công bố theo profit_year | Nguồn đang có là thông báo/lịch, chưa payment confirmation |
| D04 | Sáu financial targets lõi | Đã có mẫu phát triển; giảm phần ngoài câu hỏi chính |
| D05 | Pilot 3 × 3 năm; gate 5–8 doanh nghiệp | Quỹ 13 tuần, 10–12 giờ/tuần gồm học/report |
| D06 | Python HTTP/lxml, text/OCR, PostgreSQL, React | Web React/FastAPI/PostgreSQL theo quyết định mới; migration/API/frontend cần triển khai |
| D07 | Human review metadata/closure/số có audit | Không giả định crawl và OCR luôn đúng |
| D08 | Hợp nhất ưu tiên, entity tách scope | Không trộn riêng/hợp nhất hoặc suy khả năng chi tiền mẹ từ nhóm |

Đây là quyết định của người thực hiện và phương pháp triển khai; chưa có xác nhận giảng viên/rubric/hạn thực.

## Việc làm tiếp theo theo phụ thuộc

**Quyết định sau nghiên cứu lần hai ngày 04/10/2026:**

| ID | Quyết định | Tác động |
|---|---|---|
| D09 | Giữ tên đề tài, sáu trường và pilot/gate; kiểm định/truy vết và lifecycle là lõi | Không mở project sang chatbot/giá/ML; làm sâu contract và thí nghiệm đã có |
| D10 | Đối chiếu phiên bản/ảnh hưởng là nhánh đồ án ưu tiên | Thay ưu tiên predictor trong hồ sơ trước; dự đoán chỉ còn tùy chọn sau gate |
| D11 | Phân biệt hủy ngày đăng ký/quyền/thông báo với hủy phương án cổ tức | Không suy annual DPS = 0; rà bản thay thế; bổ sung test và coverage |
| D12 | Phân loại thay đổi hành chính/lịch/mức/hiệu lực trước cập nhật | Hash đổi không mặc định số thay đổi; giữ snapshot và audit |

[Báo cáo và tám nhánh đã khảo sát](20-nghien-cuu-lan-hai-va-chot-de-tai.md) · [Sổ nguồn](21-so-nguon-nghien-cuu-lan-hai.md). Đây là quyết định triển khai theo yêu cầu chốt của người thực hiện, không là giảng viên phê duyệt hay tính năng đã xong.

| Thứ tự | Đầu ra | Tiêu chí xong |
|---|---|---|
| T01 | Chọn 3 issuer và source/expected ledger | Đủ nguồn BCTC/sự kiện, scope chính và lý do chọn |
| T02 | Một vertical slice | BCTC + notice thật tới candidates/review/aggregate; đọc được source |
| T03 | Discovery cổ tức | Tự tìm nhiều notice từ trang công khai, giữ tuyến discovery và pagination |
| T04 | Mở collector kỳ 2023–2025 | Bỏ fixed FY2025/H1 filter theo config, giữ regression tests |
| T05 | Pilot 9 BCTC + sự kiện | Sáu target/report, events/components, missing và phút review |
| T06 | PostgreSQL/UI review | Keys/transaction, source/event versions và audit |
| T07 | Dashboard ba case | Chuỗi đủ/comparable, timeline, provenance/export |
| T08 | Holdout và report | Baselines, metrics, giới hạn, Word/slide thống nhất |

T01–T08 là backlog tương lai; không tick hoàn thành bằng việc đã có tài liệu. Chưa cần predictor; API FastAPI và frontend React nằm trong kiến trúc hiện hành, chưa triển khai. Không tự tạo lịch gửi thầy. Người thực hiện tự giải thích một module mỗi tuần.

## Gate thu hẹp

Tuần 2: một luồng nguồn tới dữ liệu phải chạy; event discovery thất bại thì thử IR adapter chính thức trước, báo phần assisted riêng. Tuần 4: đo thời gian pilot rồi chốt số issuer, không đổi missing thành 0. Tuần 8: freeze scope/holdout. Tuần 11: feature freeze. Nếu hạn/giờ thực khác giả định, lập lại ngân sách.

## Lịch sử

A1 sức khỏe tài chính là quyết định trước, [snapshot](history/a1-2026-10-03.zip). Các forecast score/threshold từ bộ initial-docs cũ là nghiên cứu lịch sử, không hiện hành. Khi đổi target/scope/nguồn phải ghi ngày, lý do, tác động dữ liệu và cập nhật SRS cùng Word/slide.

## Cập nhật nhịp báo cáo

Ngày 03/10/2026, người thực hiện yêu cầu checklist mỗi tuần và Word/slide hai tuần một lần. Giữ 13 tuần: sáu đợt tuần 2/4/6/8/10/12 và tổng kết tuần 13. Nhật ký tuần là nội bộ; thay nhịp cũ trong tài liệu và proposal. [Bản trước thay nhịp](history/before-biweekly-2026-10-03.zip).

## Cập nhật 11/10/2026 — nghiên cứu triển khai và UC lớn

[Bộ ba chức năng](../research-dividend-functions/README.md) đã có đặc tả G02/G03/G01, kiến trúc, dự toán, ca DHG/FPT và 20 tests prototype. [SRS3.2](22-srs-dac-ta-yeu-cau-phan-mem.md) nhóm lại 5 BUC, giữ UC cũ là phân rã và thêm12 D/12 TC-D. GitHub thêm3 repo, tổng12. Tiếp theo triển khai lát dọc nguồn→duyệt→metric→dossier; chốt quỹ giờ/pilot trước nghiệm thu. Chưa có application acceptance, gold độc lập hay OCR đối chứng. Kế hoạch167 giờ cũ chưa bao gồm64–98 giờ bổ sung dự toán.

## Cập nhật tiếp 11/10/2026 — làm rõ hướng nền tảng dữ liệu và phần phân tích (lịch sử trước CR-AN-03)

Người thực hiện lưu ý các UC nghe thiên về quản lý BCTC, yêu cầu nghiên cứu chức năng phân tích hữu ích hơn; đây không phải phủ định các UC. [Nghiên cứu mới](../research-financial-platform-direction/README.md) bổ sung năm repo, đọc sâu lại FinanceToolkit và tài liệu nghề nghiệp/thiết kế tương tác; lưu 32 tệp tại sáu commit. Chưa chạy các ứng dụng tham chiếu hoặc xác nhận nhu cầu bằng phỏng vấn độc lập.

Đề nghị thứ tự nghiên cứu/triển khai: A01 khám phá dữ liệu → A02 dashboard có tương tác → A03 so sánh doanh nghiệp → A04 sàng lọc/khám phá liên kết; sau đó A05/A06 kế thừa cầu nối/G02/G03, A08 kế thừa G01 và A07 theo dõi thay đổi sau khi có phiên bản/lần phân tích lưu. So sánh song song được đề nghị nâng ưu tiên; giữ nền thu/duyệt/truy nguồn. Chọn mở rộng doanh thu/biên lợi nhuận, vốn lưu động hoặc thanh khoản ngắn hạn theo câu hỏi thực tế, không tự thêm mọi trường vào pilot.

Đã cập nhật [tài liệu chức năng v1.1](27-yeu-cau-chuc-nang-va-vi-du.md) để chỉ rõ biểu đồ/xu hướng/scatter đã có yêu cầu, phần tương tác mới và điều kiện dữ liệu. SRS vẫn v3.2, 95 mã/54 tình huống dự kiến; chưa đổi tên BUC, ngân sách, lịch triển khai hoặc tick tiến độ. Bước tiếp theo là chọn một lát cắt người dùng hoàn chỉnh trong [bản khả thi](../research-financial-platform-direction/02-chuc-nang-phan-tich-va-kha-thi.md), đặc tả phần bổ sung và đo công sức trước khi lập change record.

## Quyết định mới nhất 11/10/2026 — loại A04, nghiên cứu rộng và phân rã chức năng

Theo yêu cầu người thực hiện, bỏ “Tìm và khám phá trường hợp cần chú ý”; các đề nghị screening phía trên không còn hiệu lực. [SRS v3.3/mục18](22-srs-dac-ta-yeu-cau-phan-mem.md) rút FR29/FR30/D09/D10, còn91 yêu cầu/51 TC dự kiến. Không tái đưa screening dưới tên cảnh báo. Danh sách theo dõi/so sánh do người dùng tự chọn vẫn được nghiên cứu.

[Khảo sát36 repo](../research-high-star-finance/README.md):25 repo ≥3.000 sao,12 repo ≥10.000 sao;35 README và mã chọn lọc17 repo,87 tệp lưu/34 tham chiếu dòng mã. Chưa chạy dự án nguồn. [Danh mục v2.0](27-yeu-cau-chuc-nang-va-vi-du.md) gồm năm nhóm chính và hai hướng mở rộng,38 chức năng nhỏ có mục đích/ví dụ; các bổ sung vẫn là ứng viên.

Ưu tiên mới nhất theo người thực hiện: **UC-F01/02/03/05 trước, UC-F04 sau**. [Kế hoạch mới](28-ke-hoach-thuc-hien-uc-1-2-3-5.md) kiểm tiến độ từ mã/minh chứng, chọn bảng dữ liệu→biểu đồ/tỷ số→so sánh→hồ sơ cổ tức, kèm [dữ liệu cần thu](29-du-lieu-can-thu-thap-cho-uc-1-2-3-5.md). Doanh thu/biên/cơ cấu, DuPont, quý/kế hoạch, benchmark, danh mục/định giá chọn sau theo nguồn và công sức. Quỹ167 giờ là baseline;64–98 giờ cũ cần dự toán lại, không tự hứa hoàn thành toàn danh mục. Ước lượng mới không cộng cơ học vào các ngân sách cũ và chưa gắn tuần lịch.


## Chốt tiếp 11/10/2026 — doanh nghiệp và OCR

**Lịch mới sau quyết định stack:** người thực hiện còn 10 tuần, yêu cầu ba UC đầu cơ bản trong 4–5 tuần. [Kế hoạch v6](32-ke-hoach-10-tuan-tiep-theo.md)/[HTML](checklist-10-tuan-v4.html) có 60 việc, 195 giờ dự toán chưa xác nhận quỹ giờ; tuần 4 demo, tuần 5 mở ba mã, UC-5 tuần 6–8, UC-4 tuần 9 có điều kiện. Giữ kế hoạch/tick 13 tuần làm lịch sử.

Người thực hiện chọn **HPG/VNM/FPT**, FY2023–FY2025, và yêu cầu **PaddleOCR làm OCR chính**. Giữ số mẫu/ID yêu cầu, cập nhật thiết kế SRS mục 1.3/2.3 và [manifest](../../config/pilot-scope.json). [Quyết định chi tiết](31-chot-pham-vi-va-stack-paddleocr.md): Tesseract đối chứng, pin package/model sau smoke test, chưa cài/chạy Paddle. DHG/VHC giữ làm nghiên cứu trước, không nằm trong mẫu nghiệm thu chính.
