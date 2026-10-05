# N4 — Dữ liệu và đánh giá phiên bản BCTC

Protocol đề xuất, chưa thực hiện. [Đề xuất](01-de-xuat-nghien-cuu.md), [IT](03-ky-thuat-it.md).

## 1. Xây mẫu đối chiếu thật

Tìm cặp báo cáo gốc/điều chỉnh và cặp số năm trước/cột so sánh năm sau trong pilot. Ghi cả cặp không thay đổi và cặp khác cơ sở, tránh chỉ thu những cặp có khác biệt. Đếm riêng số doanh nghiệp, cặp document, kỳ và facts; nhiều facts cùng một cặp không phải nhiều trường hợp độc lập.

Mục tiêu khởi đầu đề xuất là 5–10 cặp thật nếu nguồn cho phép; đây không phải số đã thu hay căn cứ đủ lực thống kê. Nếu chỉ tìm được ít cặp, giữ ở mức case và không gọi benchmark đại diện.

## 2. Gold và tiêu chí so sánh

Gold ghi values tại hai nguồn, đơn vị, phạm vi, kỳ, ngày công bố/evidence, tình trạng tương thích và nguyên nhân có nguồn. Reviewer đọc raw độc lập với output engine; nguyên nhân không đủ notes giữ unknown. Tolerance làm tròn dựa trên đơn vị bảng và quy tắc định trước.

Tách cặp dùng phát triển mapping khỏi cặp kiểm tra cuối. Các lỗi tổng hợp kiểm tra nhánh xử lý; không cộng chúng vào tỷ lệ chính xác trên doanh nghiệp thật. Nếu thiếu cặp holdout, công bố hạn chế thay vì tạo benchmark giả.

## 3. Thí nghiệm đề xuất

**A. Phát hiện khác biệt:** so engine với gold, đo precision/recall trên facts tương thích; báo số đúng/sai/không đủ so sánh và error taxonomy. Báo coverage để tránh chỉ giữ phần dễ.

**B. Ngày khả dụng:** chọn T nằm giữa hai công bố đã xác minh; so `public_as_of(T)` với `latest_verified`. Bản xuất hiện sau T phải không nằm trong bộ as-of. Cặp thiếu ngày không thuộc đánh giá này.

**C. Ảnh hưởng chỉ số:** tính cùng công thức CFO/LNST, cash/assets hoặc liabilities/assets ở hai snapshot đủ dữ liệu. Báo số chỉ số/cảnh báo thay đổi và trường hợp không tính được. Thay đổi không tự đồng nghĩa cải thiện dự báo.

**D. Công sức:** đo thời gian review mỗi cặp, số conflict và query latency trên quy mô đã ghi. Nếu thử index, so cùng dữ liệu và truy vấn trước/sau; không suy hiệu năng production từ bộ nhỏ.

## 4. Điều kiện trở thành đề tài thay thế

N4 chỉ thay trọng tâm khi pilot ghi nhận vấn đề nhãn cổ tức không thể khắc phục trong quỹ giờ, đồng thời có nguồn và cặp đối chiếu đủ bảo vệ phần dữ liệu. Chuyển hướng phải sửa tên, RQ, đặc tả, kế hoạch và thước đo cùng nhau. Không chỉ bỏ phần ML rồi tuyên bố đã hoàn thành một đề tài khác.

## 5. Artifact cần tạo

Manifest cặp, gold/evidence, taxonomy, policy lựa chọn phiên bản, snapshot trước/sau, bảng kết quả và protocol tái lập. Đây là đầu ra dự kiến; chưa có kết quả mới trong đợt nghiên cứu tài liệu này.
