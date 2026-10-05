# Ý tưởng dự án và câu chuyện người dùng

**Cập nhật hướng triển khai 05/10/2026:** Xây dựng hệ thống thu thập, chuẩn hóa và phân tích lợi nhuận, dòng tiền kinh doanh trong mối liên hệ với cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam. Lấy lợi nhuận→chuyển thành tiền làm trục, đối chiếu cổ tức; [SRS v3.1](22-srs-dac-ta-yeu-cau-phan-mem.md) tích hợp cầu nối CFO tối thiểu một ca, mục tiêu 1–3 sau gate. Giữ pilot/sáu trường; chưa ghi nhận phê duyệt giảng viên. Các quyết định ngày 03–04/10 bên dưới là bối cảnh trước cập nhật này.

Ngày cập nhật: **04/10/2026 sau nghiên cứu lần hai**. Tài liệu dùng để trình bày bài toán với giảng viên trước khi triển khai và chuẩn bị hướng nối tiếp cho đồ án tốt nghiệp. Yêu cầu chi tiết nằm trong [SRS v2.3](02-de-tai-va-srs.md); tài liệu này diễn giải cùng phạm vi. [Quyết định cuối và prior art](20-nghien-cuu-lan-hai-va-chot-de-tai.md).

**Tên đề tài hiện hành:** Xây dựng hệ thống thu thập, chuẩn hóa và phân tích lợi nhuận, dòng tiền kinh doanh trong mối liên hệ với cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam.

## 1 Ý tưởng cốt lõi và mục đích sử dụng

Hệ thống giúp người theo dõi doanh nghiệp nhìn lịch sử **lợi nhuận sau thuế, dòng tiền kinh doanh và mức cổ tức tiền mặt được công bố theo năm lợi nhuận** trên cùng một hồ sơ có thể truy nguồn. Người dùng thấy các biến thay đổi thế nào, có năm nào biến động khác chiều, và dữ liệu có đủ để so sánh hay chưa.

Người dùng chính là cá nhân theo dõi doanh nghiệp phi tài chính, có kiến thức tài chính cơ bản. Người nghiên cứu sử dụng dữ liệu/biểu đồ để viết phân tích có bằng chứng; người vận hành duyệt và sửa lỗi trích/ghép dữ liệu. MVP dùng một ứng dụng, chưa yêu cầu hệ thống tài khoản hay nhiều người đồng thời.

Giá trị sử dụng cần chứng minh là giảm thao tác gom tài liệu/nhập lại số, phát hiện lỗi ghép cổ tức và làm kết quả dễ kiểm chứng. Chưa có số đo chứng minh mức tiết kiệm hoặc khảo sát xác nhận nhu cầu.

## 2 Câu chuyện nền dẫn vào user story

**Nhân vật và tình huống dưới đây là giả định thiết kế.** Minh đang theo dõi cổ tức của một số doanh nghiệp phi tài chính. Khi đọc tin “doanh nghiệp X tăng lợi nhuận và công bố cổ tức”, Minh muốn kiểm tra ba năm gần đây: lợi nhuận có tăng cùng dòng tiền kinh doanh không, và cổ tức công bố tăng hay giảm trong bối cảnh đó? Minh cần trả lời trước khi chọn doanh nghiệp để đọc sâu hơn.

Minh mở các BCTC năm và nhập số vào bảng tính. Có báo cáo ghi đơn vị nghìn đồng, báo cáo khác ghi triệu đồng; nếu chọn nhầm báo cáo riêng thay cho hợp nhất, các tỷ số có thể sai. Khi tìm cổ tức, Minh gặp thông báo đăng năm sau nhưng chia cho lợi nhuận năm trước, một thông báo gộp hai năm, một đợt được đăng ở hai nơi và một bản sửa lịch thanh toán. Minh chưa biết mình đã tìm đủ các đợt hay chưa. Cộng theo năm đăng hoặc điền 0 khi không tìm thấy thông báo sẽ làm nhận xét sai.

Với hệ thống dự kiến, Minh chọn X và 2023–2025. Minh thấy bảng sáu chỉ tiêu, trạng thái đã duyệt, scope và coverage từng năm. Minh đọc hai đường lợi nhuận–CFO và chuỗi DPS ở biểu đồ có đơn vị riêng; xem các đợt cấu thành tổng, công thức và nguồn. Khi thấy lợi nhuận tăng nhưng CFO giảm, Minh mở đúng trang BCTC để kiểm tra. Nếu lịch sử cổ tức một năm chưa đủ, hệ thống ghi rõ phần đã quan sát và chưa đưa ra kết luận giảm.

Cuối luồng, Minh xuất snapshot để lưu số liệu, nguồn và phần còn thiếu. Minh có cơ sở chọn trường hợp cần tìm hiểu sâu và có thể trình bày điều dữ liệu cho thấy. Hệ thống chưa quyết định mua/bán hay bảo đảm cổ tức tương lai.

**User story tổng quát:** Là người theo dõi doanh nghiệp, tôi muốn đối chiếu lợi nhuận, dòng tiền kinh doanh và cổ tức tiền mặt công bố qua các năm trên dữ liệu có nguồn và độ đầy đủ rõ ràng, để nhận ra những trường hợp cần đọc sâu và tự kiểm chứng nhận xét.

## 3 Ba câu hỏi hệ thống phải trả lời

### 3.1 Hệ thống phục vụ mục đích gì

Hỗ trợ đọc lịch sử tài chính và cổ tức có bằng chứng: tập hợp đúng dữ liệu, tính đúng những chỉ số đã định nghĩa, nhận diện tình huống khác chiều và cho người dùng kiểm tra nguồn. Project tập trung vào hiểu dữ liệu quá khứ; tốt nghiệp dự kiến bổ sung tín hiệu để ưu tiên theo dõi tương lai khi đủ điều kiện đánh giá.

### 3.2 Hệ thống thực hiện được gì

Các dòng dưới đây là **chức năng phải xây dựng**, chưa phải danh sách chức năng đã hoàn thành.

| Người dùng hỏi | Hệ thống phải trả lời bằng gì | Điều kiện cần nêu khi trình bày |
|---|---|---|
| Lợi nhuận và CFO của X thay đổi thế nào? | Giá trị từng năm, chênh lệch, % LNST khi nền dương, hai đường cùng đơn vị | Cùng kỳ/scope; thiếu dữ liệu để khoảng trống; AN01 |
| Có năm nào lợi nhuận tăng nhưng CFO giảm/âm? | Bộ lọc trả năm/cặp năm cùng số cụ thể và nguồn | Chỉ là điều kiện quan sát, chưa kết luận nguyên nhân; AN01, AN06 |
| CFO bằng bao nhiêu lần LNST? | CFO/LNST cùng năm, công thức và operands | LNST >0; CFO âm vẫn giữ dấu; AN02 |
| Tiền và nợ phải trả chiếm bao nhiêu tài sản? | Hai tỷ lệ % và diễn biến theo năm; VCSH hiển thị trong bảng và phục vụ validation cân đối | Tài sản >0, cùng ngày/scope; nợ phải trả khác nợ vay; AN03 |
| Cổ tức tiền mặt công bố cho từng năm lợi nhuận là bao nhiêu? | Các đợt, tổng phần quan sát, tổng annual khi đủ, chênh lệch/% khi so sánh hợp lệ | Đúng năm lợi nhuận, không trùng, active version, cùng basis và đủ coverage; AN04 |
| Thông báo gộp năm hoặc bản sửa có làm tổng sai không? | Timeline, components từng năm, quan hệ sửa/hủy và tổng active | Sửa lịch không thêm tiền; lịch trả chưa là xác nhận thực trả; AN05 |
| DPS tăng/giữ/giảm trong khi lợi nhuận và CFO thay đổi ra sao? | Biểu đồ theo cùng năm với đơn vị riêng và danh sách case thỏa điều kiện | Mọi biến cần thiết đủ/comparable; chưa suy nhân quả; AN06 |
| Quan hệ trên mẫu hợp lệ và ngoại lệ là gì? | Scatter/hệ số nếu đủ điều kiện, n, bộ lọc và ba case thật có nguồn | Mẫu nhỏ, dữ liệu lặp theo công ty; không coi hệ số là mô hình dự báo; AN07 |
| Một số/nhận xét dựa trên đâu và có làm lại được không? | Công thức, operands/components, source hash/version/locator, coverage và export snapshot | 100% giá trị xuất bản có truy vết; US05, US07 |

Sáu trường BCTC lõi là LNST tổng, CFO, tiền và tương đương tiền, tổng tài sản, tổng nợ phải trả và VCSH. Pilot là 3 doanh nghiệp × 2023–2025; mở rộng 5–8 doanh nghiệp sau gate công sức. Không thêm chỉ tiêu chỉ vì thường gặp trong “phân tích BCTC”; mỗi chỉ tiêu bổ sung cần câu hỏi và dữ liệu tương ứng.

### 3.3 Hệ thống giải quyết vấn đề thực tế nào

| Vấn đề | Cách giải quyết | Cách kiểm tra lợi ích/hành vi |
|---|---|---|
| Tốn công gom tài liệu và nhập lại số liệu | Collector, chuẩn hóa và lưu tập dữ liệu có nguồn | So thời gian/công sức với nhập tay cùng tập; ghi phần còn cần review |
| Dễ chỉ nhìn lợi nhuận mà bỏ qua CFO | Hiển thị hai đại lượng cùng năm và điều kiện biến động khác chiều | Tính tay một case, kiểm tra bộ lọc và nguồn; đánh giá người dùng có hiểu kết quả |
| Tổng DPS sai do khác năm, nhiều đợt, trùng hoặc sửa | Components theo profit_year và event lifecycle | Ca notice hai năm, đăng trùng, sửa mức/sửa lịch/hủy cho kết quả mong đợi |
| Nhầm dữ liệu thiếu thành không chia cổ tức | Coverage riêng, missing reason và chặn kết luận chưa đủ | Ca partial/unknown vẫn giữ phần quan sát, không xuất annual growth |
| Không kiểm chứng hoặc tái lập được kết quả | Truy nguồn, audit, phiên bản và snapshot | Mở nguồn từng operands; tái tính snapshot cũ sau cập nhật |

Phạm vi giải quyết là công việc thu thập, đọc, đối chiếu và kiểm chứng. Hệ thống chưa chứng minh đủ tiền chia cổ tức của công ty mẹ, nguyên nhân lợi nhuận–CFO khác biệt hoặc khả năng duy trì cổ tức trong tương lai.

## 4 Một ví dụ đủ cụ thể để nói với thầy

**Ví dụ giả định, không phải dữ liệu thị trường đã thu:** X có LNST năm 2023 là 100 tỷ và CFO 90 tỷ; năm 2024 LNST 120 tỷ và CFO 40 tỷ. DPS công bố đủ trên cùng cơ sở cổ phiếu tăng từ 1.000 lên 1.500 đồng.

Hệ thống trả lời được: LNST tăng 20%, CFO giảm 50 tỷ, CFO/LNST giảm từ 0,90 xuống khoảng 0,33 lần, DPS tăng 50%. Người dùng thấy tình huống “lợi nhuận và cổ tức tăng trong khi CFO giảm” và mở được hai BCTC cùng các thông báo cấu thành DPS để kiểm tra.

Nếu chưa rà đủ cổ tức năm 2024, 1.500 đồng chỉ là tổng phần quan sát. Hệ thống chưa gọi đó là tổng đầy đủ hay kết luận cổ tức tăng 50%. Nếu chỉ sửa lịch trả, tổng không tăng thêm. Đây là những hành vi nghiệp vụ phải làm được, vượt khỏi việc vẽ biểu đồ các số đã nhập sẵn.

Kịch bản ba năm, bản sửa mức và các kết quả tính tay nằm ở **mục 3.3 SRS**. Demo thật phải dùng số đã kiểm chứng và giữ rõ phần chưa đủ.

## 5 Câu chuyện nền xác định trước cho đồ án tốt nghiệp

**Hướng ưu tiên mới:** Minh/người vận hành nhận BCTC hoặc thông báo cổ tức cập nhật. Người dùng cần biết số/trường nào thay đổi, lịch hay mức tiền thay đổi, ratio/tổng DPS/case nào bị ảnh hưởng và vì sao. Hệ thống đối chiếu phiên bản, đưa thay đổi cần review, cập nhật kết quả phụ thuộc sau duyệt và giữ snapshot cũ. Kiểm định bằng cặp nguồn thật, gold và baseline; chưa là chức năng đã hoàn thành hoặc nghĩa vụ project 13 tuần.

**Phương án dự đoán tùy chọn, giữ từ hồ sơ trước:** câu chuyện GUS01 dưới đây chỉ mở sau gate dữ liệu và ngân sách, không còn là hướng nối tiếp mặc định.

Sau khi đã có lịch sử đáng tin cậy, Minh theo dõi danh sách nhiều doanh nghiệp. Ở thời điểm BCTC năm vừa công bố, Minh muốn chọn những doanh nghiệp cần ưu tiên đọc sâu vì mức cổ tức tiền mặt công bố trong giai đoạn tới có thể giảm. Minh cần một tín hiệu có thể đánh giá được và giải thích dữ liệu đầu vào; Minh không thể biết trước các thông báo tương lai.

**GUS01:** Là người theo dõi cổ tức, tôi muốn xem tín hiệu/ước lượng việc DPS công bố trong 12 tháng sau cutoff giảm so với cửa sổ trước, để ưu tiên kiểm tra doanh nghiệp; tôi muốn biết dữ liệu đã khả dụng tại cutoff, hiệu quả so với baseline và các trường hợp không đủ điều kiện.

| Nội dung | Xác định trước cho tốt nghiệp |
|---|---|
| Mục đích | Sắp thứ tự doanh nghiệp cần kiểm tra sâu từ danh sách theo dõi |
| Đầu vào | Facts và lịch sử cổ tức đã biết tại cutoff; nguồn/phiên bản đủ để kiểm tra thời điểm |
| Target ưu tiên | Thay đổi DPS công bố trong 12 tháng sau cutoff so cửa sổ trước trên basis hợp lệ; ngưỡng giảm chốt sau pilot, trước test |
| Đầu ra dự kiến | Giảm/không giảm hoặc không đủ điều kiện; “không giảm” có thể duy trì/tăng; xác suất cần đánh giá và hiệu chỉnh |
| Điều kiện triển khai | Nhiều năm/doanh nghiệp hơn MVP, đủ nhãn giảm, cửa sổ kết quả khép, coverage/basis hợp lệ và protocol chống leakage |
| Cách kiểm tra | Chia thời gian, so baseline, precision/recall/F1/PR-AUC cho lớp giảm, calibration nếu dùng xác suất; lợi ích ưu tiên đọc sâu cần đánh giá riêng |

Project hiện tại chuẩn bị nguồn, phiên bản, thời điểm công bố, facts/events, coverage và snapshot để kiểm tra khả năng mở rộng. Project vẫn chỉ phân tích mô tả. Bảng profit_year hồi cứu cần chuyển sang protocol cutoff riêng trước khi làm dự báo; 15–24 BCTC mục tiêu của project chưa đủ để cam kết predictor. Chi tiết ở [hướng tốt nghiệp](09-lien-thong-tot-nghiep.md).

## 6 Đoạn trình bày ý tưởng với giảng viên

> Em chọn bài toán người theo dõi cổ tức muốn đối chiếu lợi nhuận, dòng tiền kinh doanh và mức cổ tức công bố của doanh nghiệp qua nhiều năm. Câu chuyện là một người đọc thấy tin doanh nghiệp tăng lợi nhuận và chia cổ tức, nhưng khi tự kiểm tra phải gom nhiều BCTC, nhập số và ghép các thông báo cổ tức khác năm, có nhiều đợt hoặc bản sửa. Sai đơn vị, sai phạm vi hay thiếu thông báo đều có thể làm nhận xét sai.
>
> Em xây hệ thống thu thập và chuẩn hóa sáu chỉ tiêu BCTC cùng sự kiện cổ tức, có review và nguồn cho mỗi kết quả. Hệ thống trả lời cụ thể lợi nhuận và CFO tăng giảm bao nhiêu, CFO bằng bao nhiêu lần lợi nhuận, tiền và nợ phải trả chiếm bao nhiêu tài sản, DPS công bố theo năm lợi nhuận là bao nhiêu, và các biến có trường hợp biến động khác chiều nào. Người dùng xem bảng, biểu đồ, timeline, công thức và mở nguồn để kiểm tra; dữ liệu thiếu không được đổi thành 0.
>
> Ví dụ giả định, lợi nhuận tăng từ 100 lên 120 tỷ nhưng CFO giảm từ 90 xuống 40 tỷ, trong khi DPS tăng từ 1.000 lên 1.500 đồng. Hệ thống chỉ ra lợi nhuận tăng 20%, CFO giảm 50 tỷ, CFO/LNST giảm từ 0,90 xuống 0,33 lần và DPS tăng 50% nếu lịch sử cổ tức đủ và cùng cơ sở cổ phiếu. Kết quả giúp người dùng chọn trường hợp cần đọc sâu; project chưa kết luận nguyên nhân hay dự đoán cổ tức.
>
> Em bắt đầu pilot ba doanh nghiệp trong ba năm, đánh giá độ đúng, độ phủ, công sức review, xử lý trùng/sửa/hủy và khả năng truy nguồn/tái lập. Hướng đồ án ưu tiên là đối chiếu các phiên bản tài liệu/thông báo và giải thích ảnh hưởng tới kết quả phân tích. Dự đoán giảm cổ tức là phương án tùy chọn khi đủ dữ liệu, nhãn và đánh giá theo thời gian so với baseline.

Đoạn trình bày là nội dung đề xuất để trao đổi, chưa được gửi và chưa có xác nhận của giảng viên. Khi nhận phản hồi, cập nhật [SRS](02-de-tai-va-srs.md) và các báo cáo liên quan theo cùng phạm vi.
