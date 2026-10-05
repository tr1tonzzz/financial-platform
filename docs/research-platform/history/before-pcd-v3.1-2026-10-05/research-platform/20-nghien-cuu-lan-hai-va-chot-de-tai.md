# Nghiên cứu lần hai và chốt đề tài

Ngày khảo sát: **04/10/2026** (Asia/Saigon). Thực hiện theo yêu cầu nghiên cứu lại, tìm ngách đủ chiều sâu cho đồ án và chốt một hướng triển khai. Đây là quyết định triển khai theo yêu cầu người thực hiện, chưa là phê duyệt của giảng viên hoặc kết quả nghiệm thu.

## 1. Quyết định cuối cùng

**Giữ và chốt tên đề tài:**

> **Xây dựng hệ thống thu thập, chuẩn hóa và phân tích dữ liệu lợi nhuận, dòng tiền kinh doanh và cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam.**

**Trọng tâm kỹ thuật:** kiểm định dữ liệu có truy vết và xử lý vòng đời sự kiện cổ tức. Phân tích lợi nhuận–CFO–DPS là tình huống sử dụng để chứng minh hệ thống tạo ra kết quả kiểm chứng được. Chọn một hệ thống tập trung, không triển khai đồng thời tám nhánh khảo sát bên dưới.

**Nhánh mở rộng ưu tiên cho đồ án:** đối chiếu thay đổi giữa các phiên bản BCTC/thông báo và giải thích ảnh hưởng tới kết quả phân tích. Dự đoán cổ tức chuyển từ hướng nối tiếp mặc định thành phương án có điều kiện; chatbot tài chính không thuộc phạm vi chốt.

Lý do giữ tên: tên hiện tại đã phản ánh đúng công việc và ngách; đổi thành tên bao trùm toàn bộ tài chính hoặc thêm AI chưa tạo đóng góp. Cần làm sâu và đo được các phần kỹ thuật đã thiết kế trước khi mở rộng. Từ “cổ tức” trong tên được đặc tả là **DPS tiền mặt công bố**, không mặc định đã thực trả.

## 2. Ý tưởng hiện tại có tốt và đã bị trùng chưa?

| Câu hỏi | Kết luận dựa trên khảo sát |
|---|---|
| Quan hệ lợi nhuận/dòng tiền với cổ tức có mới không? | Không. Đã có nghiên cứu trên doanh nghiệp Việt Nam, gồm Alphonse–Tran và công trình CTU. FCF của các bài không được đồng nhất với CFO của project. [E01](https://www.ccsenet.org/journal/index.php/ijef/article/view/32728), [E02](https://ctujs.ctu.edu.vn/index.php/ctujs/article/view/583) |
| Dashboard BCTC, lịch và dự phóng cổ tức đã có chưa? | Có. FiinTrade công bố chức năng BCTC chuẩn hóa và lịch sử/dự phóng cổ tức. Gọi thư viện dữ liệu rồi vẽ chart sẽ giao nhau nhiều. [E03](https://web.fiintrade.vn/nhom-trang-tinh-nang/phan-tich-co-ban/bao-cao-tai-chinh/), [E04](https://web.fiintrade.vn/nhom-trang-tinh-nang/phan-tich-co-ban/co-tuc-va-du-bao/) |
| Thu và chuẩn hóa dữ liệu chứng khoán Việt Nam đã có chưa? | Có, Vnstock công bố kết nối nguồn bên thứ ba và các hàm BCTC. Chưa chạy/benchmark thư viện trong lượt này. [E05](https://github.com/thinh-vu/vnstock) |
| Trích bảng/PDF và truy nguồn là phát minh mới? | Không. Docling có biểu diễn bảng, vị trí và provenance; Docling Graph có ledger truy về chunks/trang. [E06](https://github.com/docling-project/docling/blob/main/docs/concepts/docling_document.md), [E07](https://github.com/docling-project/docling-graph/blob/main/docs/fundamentals/graph-management/provenance.md) |
| Hỏi đáp tài chính tiếng Việt còn là ngách trống? | Không nên giả định. ViNumQA đã có bài tại VLSP 2025; ViFinQA có dataset card công khai. Chúng khác bài toán vòng đời cổ tức nhưng là prior art khi đề xuất chatbot. [E10](https://aclanthology.org/2025.vlsp-1.25/), [E11](https://huggingface.co/datasets/AIGuruTinix/ViFinQA) |
| Có tìm thấy đồ án trùng toàn bộ hệ thống này không? | Chưa xác định được trong tập nguồn công khai đã tra cứu. Không suy ra chưa ai làm; kho nội bộ trường và sản phẩm trả phí chưa được khảo sát đầy đủ. |
| Còn đáng làm không? | **Có, theo hướng hệ thống phần mềm có đánh giá.** Giá trị nằm ở xử lý đúng nguồn/kỳ/đơn vị/scope/sự kiện và đo chất lượng, công sức, khả năng tái lập. Đây là nhận định chọn hướng, không cam kết đạt rubric chưa được cung cấp. |

Phân biệt **giao nhau về ý tưởng**, **giao nhau về chức năng**, và **sao chép công trình**. Một đề tài ứng dụng có prior art vẫn có thể có đóng góp triển khai và đánh giá của người thực hiện. Không lấy việc chưa tìm được tên nguyên văn làm chứng cứ độc quyền.

## 3. Các bằng chứng mới khiến hướng này đáng làm sâu

### 3.1 Một thông báo chứa hai năm lợi nhuận

Thông báo VNM ngày 30/08/2024 nêu tổng 2.450 đồng/cổ phiếu, gồm 950 đồng cho đợt cuối năm 2023 và 1.500 đồng tạm ứng đợt 1 năm 2024. Một dòng thông báo phải tách thành hai components; gán toàn bộ vào năm đăng sẽ sai. [E15 — VSDC](https://vsdc.vn/vi/ad/174349).

Đây là bằng chứng về ca nghiệp vụ, **không xác nhận lịch sử DPS của hai năm đã đầy đủ**. Không cần nghiên cứu nhân quả mới để chứng minh lỗi ghép năm có thể ảnh hưởng biểu đồ.

### 3.2 Thay lịch không tạo một khoản cổ tức mới

VC7 có thông báo ngày 05/03/2026 chuyển lịch từ 06/03/2026 sang 05/06/2026, tham chiếu thông báo gốc số 17/TB-VSDC. Thông báo ngày 28/05/2026 tiếp tục chuyển từ 05/06/2026 sang 30/06/2027, tham chiếu 815/TB-VSDC. Bản gốc công bố ngày 06/01/2026 nêu 500 đồng/cổ phiếu cho năm 2024. [E17](https://vsd.vn/vi/ad/192812), [E18](https://vsdc.vn/vi/ad/196257), [E21 — bản gốc](https://vsdc.vn/vi/ad/190751).

Hệ thống cần nối quan hệ gốc–sửa, lưu lịch cũ/mới và thời điểm biết thông tin, giữ DPS khi chỉ đổi lịch. Ngày dự kiến đã qua không đủ để đánh dấu thực trả. Case 2026 chỉ là mẫu kiểm tra vòng đời, không mở scope chính thành dataset toàn thị trường 2026.

### 3.3 Hủy ngày đăng ký cuối cùng không đồng nghĩa không chia cổ tức

SVC ngày 19/07/2024 hủy ngày đăng ký cuối cùng 22/07/2024 của thông báo tạm ứng cổ tức, với lý do điều chỉnh phương án. [E16 — VSDC](https://vsd.vn/vi/ad/173190).

**Bổ sung đặc tả quan trọng:** phân loại đối tượng bị hủy: thông báo/quyền/ngày đăng ký/lịch/phương án. Chỉ cập nhật đối tượng có bằng chứng. Thông báo thực hiện quyền đã bị hủy không còn là đợt thực hiện active; vẫn giữ lịch sử và quyết định phê duyệt nếu có. Đưa annual coverage về trạng thái cần rà bản thay thế khi chưa rõ. Không tự ghi annual DPS = 0 hoặc kết luận doanh nghiệp hủy toàn bộ cổ tức.

### 3.4 Thay HTML chưa chắc thay nghiệp vụ

Thông báo điều chỉnh nội dung VNM ngày 08/05/2025 thay thông tin giấy tờ nhận cổ tức để phù hợp Luật Căn cước; nội dung khác không đổi. Đã đọc body ở host vsdc.vn sau khi route vsd.vn lỗi. [E19 — VSDC](https://vsdc.vn/vi/ad/182559).

Hash đổi chỉ chứng minh bytes khác. Cần phân biệt thay sidebar/nội dung hành chính, thay lịch, thay mức và thay hiệu lực. Lượt này chưa benchmark parser trên case đó, không ghi là đã xử lý được.

**Đánh giá:** các ca trên tạo bài toán hệ thống cụ thể, kiểm thử được. Chưa chứng minh sản phẩm thương mại thiếu khả năng xử lý chúng, hoặc phương pháp xử lý là mới trên thế giới.

## 4. Tám nhánh liên quan và lựa chọn

Mức giao nhau và khả thi dưới đây là đánh giá chuyên môn cho người làm một mình, ngân sách giả định 13 tuần × 10–12 giờ; không phải điểm benchmark hay thống kê số đồ án.

| Nhánh | Sản phẩm và chiều sâu | Prior art / dữ liệu cần | Quyết định |
|---|---|---|---|
| **N1. Hồ sơ cổ tức theo vòng đời sự kiện** | Tách nhiều năm, nhận diện cùng đợt, nối bản sửa/hủy, timeline và aggregate có coverage | Lịch cổ tức đã có ở E04; ca thật E15–E19. Cần gold liên kết sự kiện | **Lõi ưu tiên số 1**; giữ trong đề tài hiện tại |
| **N2. Kiểm định và duyệt dữ liệu có bằng chứng** | Rule engine về unit/kỳ/scope, kiểm tra tài sản = nợ phải trả + VCSH khi đủ và tương thích, review queue, audit | Data validation đã có E12; đóng góp là contract tài chính cụ thể và đánh giá lỗi/công sức | **Lõi ưu tiên số 2**; tập trung quy tắc hữu hạn |
| **N3. Đối chiếu phiên bản và ảnh hưởng tới phân tích** | Diff sáu chỉ tiêu/các trường sự kiện; xác định ratio/aggregate/case bị ảnh hưởng; tái tính sau review và giữ snapshot cũ | “As filed” có E13; đối chiếu chuỗi BCTC có prior art E14. Cần cặp nguồn thật cùng kỳ/scope | **Nhánh đồ án ưu tiên**; project chỉ hoàn thiện nền version/snapshot |
| **N4. Ưu tiên công việc review theo lỗi và ảnh hưởng** | Xếp hàng theo thiếu metadata, mâu thuẫn nguồn và số kết quả phụ thuộc; so với FIFO | Cần ghi thời gian/issue từ pilot, không phải nhãn dự báo đầu tư | Bổ sung nhỏ sau pilot nếu còn giờ; chưa gọi điểm rule là xác suất chính xác |
| **N5. Đối chiếu BCTC trước/sau kiểm toán** | So khác biệt số và ratios cùng kỳ/scope; nối bằng chứng | Phải thu cả hai loại báo cáo; khác biệt có thể do điều chỉnh/phân loại, không chứng minh gian lận | Ngách đồ án thay thế N3 nếu tìm được nhiều cặp thật; không làm song song hai nghiên cứu |
| **N6. Phân tích mức chi cổ tức và nguồn tiền** | Muốn phân tích payout/khả năng bao phủ cần EPS/thu nhập đúng đối tượng, số cổ phiếu hoặc tiền thực trả cùng scope/thời gian | Nghiên cứu tài chính E01–E02; nhu cầu dữ liệu vượt sáu trường lõi | Chỉ mở có điều kiện. Không tính CFO/DPS vì khác đơn vị; không kết luận pháp lý từ BCTC hợp nhất |
| **N7. Dự đoán giảm/không giảm DPS** | Pipeline nhãn theo thời điểm, baseline, chia thời gian, đánh giá lớp giảm | ML cổ tức có E20; dự phóng sản phẩm E04. Cần nhiều firm-years, ngày khả dụng, coverage và cửa sổ nhãn khép | **Không chọn làm mặc định**. Chỉ mở sau gate dữ liệu, ngân sách và yêu cầu giảng viên |
| **N8. Hỏi đáp tài chính có kiểm chứng** | Retrieval + chương trình tính toán trên facts đã duyệt, trích nguồn và từ chối khi thiếu | FinQA/TAT-QA E08–E09; tiếng Việt E10–E11. Cần benchmark truy hồi và câu trả lời riêng | Không đưa vào đề tài chốt; tính cạnh tranh cao và làm loãng luồng dữ liệu |

N1/N2 không phải tính năng vừa phát minh trong lượt này: đã có phần lớn trong SRS. Nghiên cứu lần hai **xác nhận cần làm sâu và đo chúng**, đồng thời bổ sung phân loại ý nghĩa thay đổi/hủy và chọn N3 làm hướng đồ án rõ hơn.

## 5. Phạm vi chốt cho project hiện tại

### Dữ liệu và sản phẩm

- Pilot 3 doanh nghiệp phi tài chính × 2023–2025; sáu trường BCTC hiện hành. VNM/DHG là ứng viên cổ tức có mẫu rõ, doanh nghiệp thứ ba chốt qua rà nguồn; chưa coi nguồn ba năm đã đầy đủ.
- Mục tiêu mở rộng 5–8 doanh nghiệp sau gate công sức tuần 4. Không tăng quy mô để tên đề tài trông lớn hơn.
- Thu nguồn chính thức: BCTC ở IR; thông báo cổ tức VSDC/IR. Lưu tuyến discovery, raw, hash, ngày công bố/ngày thấy riêng và source locator.
- Chỉ tiêu tới candidate → validation → review → reviewed fact. Sửa có trước/sau/lý do; không biến review thành accuracy tự động.
- Thông báo tới event/components/relations; phân biệt sửa lịch, sửa mức, hủy đối tượng thực hiện và nội dung hành chính.
- Bảng năm và timeline; lợi nhuận/CFO, CFO/LNST theo điều kiện, tiền/tài sản, nợ phải trả/tài sản, DPS theo năm lợi nhuận khi đủ và cùng basis.
- Người đọc mở nguồn/operands; người vận hành xử lý issue; export snapshot tái lập được. Stack Python/SQLite/Streamlit hiện hành đủ cho phạm vi này.

### Bổ sung hữu hạn cho chất lượng

Chọn một bộ quy tắc nhỏ, mỗi rule có mã, severity, điều kiện áp dụng, bằng chứng và cách xử lý. Ví dụ: thiếu đơn vị; cùng fact key nhưng nguồn mâu thuẫn; sai kỳ/scope; tổng components khác DPS nguồn; asset–liabilities–equity sai vượt tolerance đã chốt.

Identity kế toán chỉ chạy trên ba số cùng ngày/scope/đơn vị, xét làm tròn. Nó là tín hiệu review, không bảo đảm toàn bộ BCTC đúng. Fact chưa có ba operands thì báo không kiểm tra được. Dữ liệu đủ sáu trường đã có nên không cần thêm hàng chục chỉ tiêu để bắt đầu.

Một thay đổi được phân loại `metadata_only`, `schedule_change`, `amount_change`, `rights_cancellation`, `unresolved` sau kiểm tra. Không dùng một cờ `cancelled` chung cho mọi loại hủy. Rule engine nhẹ là lựa chọn triển khai; không bắt buộc cài cả nền tảng Great Expectations/DataHub.

### Ngoài phạm vi

Giá/yield/backtest, portfolio, scoring sức khỏe tổng hợp, OCR hoàn hảo mọi biểu mẫu, phủ toàn thị trường, chatbot, predictor và xác nhận tiền đã trả khi thiếu bằng chứng. Phân tích mô tả không chứng minh nhân quả hoặc gian lận.

## 6. Nhánh đồ án ưu tiên: thay đổi có ý nghĩa và ảnh hưởng

**Câu hỏi:** khi tài liệu hoặc thông báo được cập nhật, hệ thống nhận biết đúng phần dữ liệu nào thay đổi và kết quả phân tích nào cần cập nhật, với công sức review bao nhiêu?

| Thành phần | Phạm vi nghiên cứu hữu hạn |
|---|---|
| Đơn vị đối chiếu | Financial fact: issuer + metric + period + scope + unit/basis; event theo identity đã review |
| Phát hiện thay đổi | Bỏ qua layout/bytes không ảnh hưởng; so giá trị và metadata nghiệp vụ đã chuẩn hóa; chưa tự hòa giải mọi dòng BCTC |
| Đồ thị phụ thuộc | Fact/component → ratio/annual aggregate → case; có thể lưu bảng quan hệ trong SQLite, không bắt buộc graph database |
| Quy trình | Đánh dấu cần review → duyệt bản có hiệu lực → tính lại kết quả phụ thuộc; lưu before/after và snapshot cũ |
| Dữ liệu đánh giá | Cặp PDF/notice thật và gold loại thay đổi/đối tượng bị ảnh hưởng; fixture giả lập báo riêng |
| Baseline | Hash-only gắn cờ mọi thay đổi; latest-overwrite; refresh mọi kết quả; so với diff nghiệp vụ và cập nhật theo phụ thuộc |
| Số đo | Precision/recall loại thay đổi và impact; số kết quả đúng sau cập nhật; phút review; runtime; tái lập snapshot |

Nguồn SEC cho thấy dữ liệu theo bản đã nộp là cách tổ chức đã tồn tại; preprint *Reclassified to Conform* nghiên cứu tái dựng chuỗi BCTC qua các bản công bố. Không tuyên bố semantic diff hay provenance là ý tưởng chưa ai làm. Chọn phạm vi sáu chỉ tiêu/thông báo Việt Nam và đánh giá riêng. [E13](https://www.sec.gov/data-research/sec-markets-data/financial-statement-notes-data-sets), [E14](https://arxiv.org/abs/2609.38754).

**Gate đề xuất cho đồ án, không phải ngưỡng chuẩn:** trước khi cam kết N3, trong một vòng khảo sát thu được khoảng 10 cặp phiên bản/chuỗi sự kiện thật, gồm ít nhất hai loại thay đổi nghiệp vụ, từ ít nhất ba doanh nghiệp; lập gold và đo thời gian gán nhãn. Bộ nhỏ này chỉ kiểm tra khả thi. Cỡ tập đánh giá cuối phải chốt theo độ đa dạng và công sức, không kết luận hiệu quả phổ quát từ 10 cặp. Nếu chỉ có hash đổi mà số/nghiệp vụ không đổi, chưa đủ cho nhánh này.

Không tìm đủ bản sửa BCTC thì giới hạn N3 vào vòng đời cổ tức, giữ BCTC làm đầu vào phân tích. Không dựng restatement giả rồi báo là dữ liệu thị trường. Nếu nguồn chỉ có bản mới nhất, không hứa khôi phục lịch sử point-in-time.

## 7. Đánh giá để đề tài có sức nặng

| Câu hỏi đánh giá | So sánh | Số đo/bằng chứng |
|---|---|---|
| Trích đúng bao nhiêu trước khi con người sửa? | B0 text-only; B1 text/OCR + parser; B2 thêm rule/review | Joint correctness metric/value/unit/period/scope; tỷ lệ thiếu; phút review; B2 tách khỏi accuracy tự động |
| Xử lý sự kiện tốt hơn cộng theo năm đăng không? | Baseline một dòng/notice so components + relations | Đúng profit_year/đợt/loại sửa; precision/recall event relations; aggregate theo gold |
| Quy tắc kiểm định phát hiện lỗi nào? | Parser so parser + rules; cùng tập chưa dùng chỉnh rule | Precision/recall issue; lỗi bỏ sót; báo động sai; trường hợp không kiểm tra được |
| Cập nhật có đúng và giữ lịch sử không? | Overwrite so reviewed versions/snapshots | Tái tính khớp; không trùng; nguồn cũ mở được; không đánh dấu paid từ lịch |
| Người dùng làm nhiệm vụ nhanh/đúng hơn không? | Thủ công trên cùng nguồn so pipeline có tính review | Thời gian, tỷ lệ hoàn thành, lỗi; ghi rõ số người và thứ tự nhiệm vụ |

Freeze gold/holdout trước vòng đánh giá chính, tránh cùng notice ở hai route hoặc bản gần giống nằm ở cả development và holdout. Tập ca khó có thể chọn có chủ đích nhưng báo riêng, không đại diện tần suất lỗi toàn thị trường. Chấm ô trích không làm tăng số quan sát độc lập của phân tích tài chính. Thử nghiệm bỏ từng thành phần (ablation) giúp chứng minh tác dụng của rules/relations, không chỉ báo accuracy chung.

## 8. Trình tự làm và hồ sơ cần nộp

Giữ phát triển lặp và tăng dần; phần dữ liệu tham khảo CRISP-DM. SRS, UC, ERD/pipeline, từ điển, rules và protocol được cập nhật theo dữ liệu thật. Không đợi hoàn chỉnh toàn bộ tài liệu mới thử collector.

| Mốc | Việc ưu tiên | Đầu ra kiểm tra được |
|---|---|---|
| Tuần 1–2 | Chốt người dùng/scope; khảo sát mẫu; SRS/UC bản đầu; một luồng xuyên suốt | Một BCTC + notice → số/sự kiện đã review → kết quả mở nguồn được |
| Tuần 3–4 | Pilot 9 BCTC; discovery cổ tức; rules hữu hạn; audit/DB | Gold, lỗi, phút/report/notice; quyết định quy mô |
| Tuần 5–6 | Lifecycle/coverage/UI; tests ca nhiều năm/sửa/hủy | Tổng DPS đúng và trạng thái rõ; canceled record date không thành declared_zero |
| Tuần 7–8 | Hoàn thiện dataset; freeze holdout; so baselines | Kết quả chất lượng và công sức với mẫu số rõ |
| Tuần 9–10 | Ba case mô tả; cập nhật/export/snapshot | Case thật có operands; nguồn mới không đổi snapshot cũ |
| Tuần 11–13 | Feature freeze, nghiệm thu, báo cáo/demo, chạy môi trường mới | Bảng yêu cầu → module → test → bằng chứng; bundle tái lập |

N3 được khảo sát và lập protocol riêng khi bước sang đồ án; không nhét toàn bộ nhánh mới vào ngân sách project 13 tuần. Chỉ ưu tiên N4 nếu pilot cho thấy review là nút thắt và còn quỹ giờ.

## 9. Giới hạn của lượt nghiên cứu và tuyên bố được phép

Đây là khảo sát có mục tiêu về công trình, sản phẩm, công cụ và nguồn nghiệp vụ; không phải tổng quan hệ thống toàn bộ đồ án Việt Nam. Tra cứu theo nhóm: dividend policy/CFO/FCF; phần mềm BCTC/cổ tức; PDF/table/provenance; Vietnamese financial QA; phiên bản/as-filed; data validation; cancellation/payment amendments; đồ án liên quan. Có kiểm tra lại prior art thay vì chỉ dựa hồ sơ cũ.

Các cụm đã dùng gồm `Vietnam dividend policy free cash flow profitability listed firms research`, `financial statement extraction benchmark FinQA TAT-QA FinTabNet`, `Vietnam financial document question answering benchmark`, `báo cáo tài chính đồ án OCR`, `cổ tức đồ án hệ thống`, cùng tìm kiếm domain VSDC/FiinTrade/SEC/GitHub và cụm điều chỉnh/hủy cổ tức. Các truy vấn repo/provenance/dự đoán cũng được kiểm tra để tìm prior art cho các nhánh.

Không đăng nhập/mua gói thương mại, không benchmark đối thủ, không chạy lại kết quả các bài. Một số route VSDC timeout/lỗi; E15/E18/E19 và bản gốc VC7 đã đọc lại thành công trên host vsdc.vn. CTU E02 chỉ đọc nội dung được lập chỉ mục, ghi rõ ở sổ nguồn. Đọc nguồn bằng công cụ web không chứng minh collector của project tự tải được. Không truy cập kho đồ án nội bộ trường. Không biết toàn bộ lịch sử và quyền thu thập của từng nguồn; khảo sát tài liệu không tự cấp phép crawl định kỳ.

**Có thể nói:** “Em tự thiết kế, triển khai và đánh giá một hệ thống dữ liệu có kiểm định/truy vết; tập trung các ca cổ tức nhiều năm và thay đổi thông báo trên nguồn Việt Nam.”

**Chưa thể nói:** “Hệ thống đầu tiên”, “chưa ai làm”, “dự đoán tin cậy”, “chứng minh cổ tức bền vững”, hoặc “chắc chắn đủ chuẩn tốt nghiệp”. Giá trị đồ án phải gắn artifact và số đo, đối chiếu rubric hệ thống phần mềm khi có.

## 10. Đối chiếu với quyết định cũ

- Giữ tên, sáu trường, pilot/gate, stack và phân tích mô tả đã chọn; không mở project thành nghiên cứu tài chính mẫu lớn.
- Xác nhận N1/N2 là phần cốt lõi cần làm sâu; bổ sung rõ nghĩa hủy đối tượng thực hiện và thay đổi phi tài chính.
- **Thay ưu tiên liên thông:** N3 đối chiếu phiên bản/ảnh hưởng đứng trước N7 dự đoán. Protocol predictor cũ giữ làm phương án tùy chọn, không xóa lịch sử.
- Chưa có dataset mới hoặc benchmark mới từ lượt khảo sát; các số crawler trước vẫn là bằng chứng development.
- SRS/UC/rules và tài liệu trình bày cần dùng quyết định này khi cập nhật. Word/slide đã xuất trước lượt này chưa chứa phần nghiên cứu mới; không coi chúng đã được tái tạo.

Sổ bằng chứng kèm trạng thái đọc: [21-so-nguon-nghien-cuu-lan-hai.md](21-so-nguon-nghien-cuu-lan-hai.md).
