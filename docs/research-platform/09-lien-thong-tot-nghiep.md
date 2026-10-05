# Liên thông đồ án: đối chiếu phiên bản và ảnh hưởng tới phân tích

**Quyết định mới ngày 04/10/2026 sau nghiên cứu lần hai:** ưu tiên làm sâu hệ thống qua đối chiếu phiên bản BCTC/thông báo và giải thích ảnh hưởng tới kết quả phân tích. Dự đoán duy trì/giảm cổ tức chuyển thành tùy chọn sau gate dữ liệu. Project hiện tại vẫn thu thập–kiểm định–phân tích mô tả; chưa tự thêm nhánh đồ án vào ngân sách 13 tuần. [Bằng chứng và lựa chọn](20-nghien-cuu-lan-hai-va-chot-de-tai.md). Tên/rubric/thời gian tốt nghiệp cần trao đổi sau, chưa bảo đảm liên thông tự động.

## Hướng ưu tiên: thay đổi có ý nghĩa và kết quả phụ thuộc

Người vận hành nhận BCTC hoặc thông báo mới, cần phân biệt thay nội dung hành chính, lịch, số tiền và đối tượng thực hiện quyền; muốn biết ratio/aggregate/case nào cần review/tái tính. Nguồn mới không được làm mất snapshot đã dùng trong báo cáo.

Cập nhật 05/10/2026 theo SRS v3.1: project có thêm cầu nối CFO theo ca, giữ operands/mapping/formula versions. Nhánh tốt nghiệp có thể đối chiếu tác động bản sửa lên bridge/residual/case sau gate. Phạm vi đầu: sáu financial targets hiện hành, bridge ở ca chọn và fields/components cổ tức; ghép cùng kỳ/scope/basis trước diff. Lưu quan hệ operands tới kết quả bằng bảng SQLite; không bắt buộc graph database. Review bản mới trước khi thay active view. Không tự suy hủy ngày đăng ký thành không chia cổ tức, không hứa khôi phục mọi phiên bản lịch sử.

Đánh giá bằng gold cặp tài liệu/chuỗi sự kiện thật, so hash-only/overwrite/refresh toàn bộ với diff nghiệp vụ/cập nhật kết quả phụ thuộc. Đo đúng loại thay đổi/impact, công sức review và tái lập snapshot. Fixture giả lập giữ riêng khỏi bằng chứng nguồn thật. Chi tiết baseline/gate/cỡ pilot trong mục 6 của báo cáo nghiên cứu lần hai.

**Gate trước khi chốt nhánh đồ án:** khảo sát khoảng 10 cặp phiên bản/chuỗi sự kiện từ ít nhất ba doanh nghiệp, có ít nhất hai loại thay đổi nghiệp vụ; lập gold và đo công sức. Đây là mục tiêu kiểm tra khả thi đề xuất, chưa đủ để khẳng định hiệu quả thống kê. Nếu thiếu bản sửa BCTC, giới hạn nghiên cứu vào vòng đời thông báo cổ tức. Chưa đạt gate thì chưa cam kết benchmark/version-impact hoàn chỉnh.

## Phương án tùy chọn: dự đoán cổ tức

Các mục dưới giữ protocol nghiên cứu trước để tái sử dụng khi dữ liệu, quỹ giờ và yêu cầu giảng viên phù hợp; không còn là hướng nối tiếp duy nhất.

## 0 Câu chuyện người dùng và mục đích cần xác định trước

Tình huống giả định: Minh đã dùng hồ sơ lịch sử lợi nhuận–CFO–DPS để đọc doanh nghiệp. Khi BCTC năm mới công bố, Minh phải chọn trong danh sách theo dõi những doanh nghiệp cần kiểm tra sâu trước vì mức cổ tức công bố sắp tới có thể giảm. Minh cần tín hiệu có đầu vào đã biết tại thời điểm đó và bằng chứng kiểm định, chưa thể sử dụng các thông báo tương lai để nhận định quá khứ.

**GUS01:** Là người theo dõi cổ tức, tôi muốn xem ước lượng/tín hiệu về việc DPS công bố trong 12 tháng sau cutoff giảm so với cửa sổ trước, để ưu tiên đọc sâu doanh nghiệp; tôi muốn biết dữ liệu đầu vào, hiệu quả so baseline và trường hợp không đủ điều kiện.

Đầu ra dự kiến là giảm/không giảm theo ngưỡng đã chốt hoặc không đủ điều kiện đánh giá. “Không giảm” có thể là duy trì hoặc tăng, không đồng nghĩa giữ nguyên. Xác suất chỉ dùng khi mô hình đã được đánh giá và hiệu chỉnh; hiệu quả sắp thứ tự đọc sâu cần đánh giá riêng với quy trình người dùng, chưa suy từ F1/PR-AUC.

Câu chuyện này được xác định trước để định hướng dữ liệu, **chưa là chức năng hay tiêu chí nghiệm thu project hiện tại**. [SRS v2.1 mục 6](02-de-tai-va-srs.md) và [tài liệu trình bày ý tưởng](16-y-tuong-va-cau-chuyen-nguoi-dung.md) ghi cùng câu chuyện; protocol và gate dưới đây quyết định khả năng triển khai.

## 1 Tái sử dụng

Collector/raw/version, financial facts đã review, event components/lifecycle/basis, coverage/snapshots, schema, tests và UI. Chưa cần chuyển sang hỏi đáp AI hoặc xây nhiều hướng song song.

## 2 Protocol dự đoán phải chốt trước mô hình

Phương án ưu tiên để kiểm tra: cutoff là ngày BCTC năm được xác nhận khả dụng; features chỉ dùng thông tin đã biết tại cutoff. Target là thay đổi tổng DPS **công bố trong 12 tháng sau cutoff** so cửa sổ so sánh trước, trên basis đã xử lý. Đây khác bảng profit_year hồi cứu của project. Ngưỡng giảm là tham số chốt trước test sau pilot, chưa mặc định 30%.

Nếu chọn target theo năm lợi nhuận tiếp theo, phải lập protocol mới và xử lý tạm ứng/các thông báo đến muộn; không hoán đổi hai target sau xem kết quả. Chỉ làm một định nghĩa chính trong luận văn.

Nhãn censored khi cửa sổ chưa khép; unknown khi không đủ coverage/basis; absence không là omission/zero. Một BCTC FY2025 công bố tháng 3/2026 có window đến tháng 3/2027 nên tại 03/10/2026 chưa trưởng thành. Thông báo lịch trả không là thực trả, target tên công bố phải nhất quán.

## 3 Điều kiện khả thi

Cần nhiều năm/issuer hơn 15–24 quan sát hiện tại, đủ trường hợp giảm và đủ quality/point-in-time dates. Cohort toàn công ty trả đều sẽ khó đánh giá lớp giảm; pilot phải kiểm tra label distribution và công sức mở rộng trước cam kết mô hình.

Share changes, restated facts và bản thay thế sau cutoff không được đưa ngược vào feature lịch sử. Nguồn chỉ biết ngày công bố hiện tại hoặc thiếu version lịch sử phải ghi giới hạn point-in-time, không giả định lịch sử hoàn hảo.

## 4 Baseline và đánh giá tương lai

Baseline lịch sử giữ mức/carry-forward theo target đã định nghĩa; sau đó Logistic Regression hoặc cây đơn giản nếu sample/lớp đủ. Chia thời gian trước/sau và xử lý cửa sổ trùng; không random split các kỳ/cùng phiên bản gây leakage. Đo precision/recall/F1/PR-AUC với lớp giảm, calibration nếu dùng xác suất, số mẫu và uncertainty.

Đánh giá chất lượng extraction và nhãn riêng trước model. Chỉ nói model hữu ích sau so baseline trên holdout; không hứa dự đoán chính xác hoặc đề xuất đầu tư. Các mô hình/framework chỉ chốt khi tới giai đoạn này.
