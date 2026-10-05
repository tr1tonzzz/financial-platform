# Lộ trình học gắn với project

**Đồng bộ 04/10/2026:** dùng [kế hoạch v2](04-ke-hoach-13-tuan.md) và [hướng dẫn buổi đầu/mẫu minh chứng](23-bat-dau-va-minh-chung-thuc-hien.md) để thực hiện. Bài học bên dưới là nền; phân bổ giờ, outputs và TC lấy từ kế hoạch theo SRS v3.0. Tuần2 học/làm version-cache nền; tuần10 hoàn thiện export/replay mọi kết quả; tuần11 thêm restore/performance/local safety. Hủy ngày quyền không đồng nghĩa hủy policy hoặc annual DPS=0.

Mục tiêu tự hiểu và giải thích được phần mình làm. Học theo task tuần, không chờ học hết tài chính/Python rồi mới bắt đầu.

## 1 Tài chính tối thiểu

Ba BCTC; lợi nhuận khác CFO; instant khác duration; hợp nhất/riêng/entity; đơn vị/người dùng cột; nợ phải trả khác nợ vay; DPS khác phần trăm mệnh giá/yield; năm lợi nhuận khác ngày trả; proposed/right notice khác confirmed paid; cổ phiếu thay basis.

Đọc [từ điển](12-kien-thuc-tai-chinh-va-tu-dien.md). Bài tập nguồn thật: tách VNM notice nhiều năm thành components, giải thích vì sao chưa gán thực trả. Bài tập giả lập: assets 100, liabilities 40, equity 60, LNST 8, CFO 3, cash 10 (triệu VND). Cân đối=0, CFO/LNST=0,375, cash/assets=10%, liabilities/assets=40%. Số giả lập chỉ để học, không là case doanh nghiệp thật.

## 2 Python và IT

Tuần 1–2: biến/list/dict/if/for/hàm, pathlib, file JSON, lỗi, virtualenv/Git, HTTP/urljoin/selector/hash. Tự viết một hàm chọn link và lưu manifest. Tuần 3–4: normalize số, regex nhiều dòng, text/OCR, SQL/join/keys/transaction; giải thích một lỗi cột.

Tuần 5–6: pandas merge/group với cardinality check, missing, Streamlit/state, module và tests. Tự tách một notice thành hai năm, kiểm tra không nhân bản tài chính khi JOIN nhiều events. Tuần 7–10: batch/logs/coverage, update/version và snapshot. Class/typing học khi cần module, không học mọi framework cùng lúc.

Nguồn: [Python](https://docs.python.org/3.12/tutorial/), [pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html), [SQLite](https://www.sqlite.org/lang.html), [Streamlit](https://docs.streamlit.io/get-started/fundamentals). Tutorial Python giả định nền lập trình cơ bản, nên cần ví dụ 10–20 dòng nếu chưa vững.

## 3 Phân tích và kiểm định

Học mẫu số/coverage/precision/recall, mean/median, scatter, Spearman, mẫu lặp theo công ty, selection bias, correlation khác causation. Với 15–24 quan sát, ưu tiên mô tả và case; không cần mô hình đa biến phức tạp.

Phân biệt download success và numerical correctness; confidence OCR khác accuracy; development khác holdout; số sau review khác độ đúng tự động. “Không thấy cổ tức” không bằng 0; amendment có thể làm tổng khác mà không là hai payments.

## 4 Tự kiểm tra hiểu

Mỗi tuần tự tính một ví dụ, viết/sửa một hàm, đổi input và dự đoán output, đọc nguồn thật, nói 2–3 phút không nhìn đáp án. Card module gồm input/output/logic/lỗi/test; card ratio gồm công thức/đơn vị/điều kiện/nguồn. Learning log chỉ ghi việc đã học thật. AI hỗ trợ không thay review số hoặc khả năng tự giải thích.

## Đọc sách song song

Chọn [Trí tuệ tài chính và lộ trình đọc](15-sach-nen-tang-va-cach-doc.md); ưu tiên lợi nhuận, bảng cân đối, dòng tiền và tỷ số, áp dụng vào BCTC thật. Đọc trong quỹ học đã tính. Nhật ký hằng tuần, Word/slide tổng hợp hai tuần một lần.
