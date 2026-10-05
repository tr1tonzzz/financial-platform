# I3 — Nghiên cứu vòng đời và chất lượng sự kiện cổ tức

Ngày: 03/10/2026. P0 cho chuẩn hóa/ghép sự kiện; phân tích hoãn lịch nâng cao là mở rộng. Phục vụ RQ1 và tính hợp lệ nhãn RQ2/RQ3.

## 1. Vấn đề và hướng giải quyết

Một quyền cổ tức có thể xuất hiện ở nghị quyết, thông báo quyền, đính chính, đổi lịch và xác nhận thực hiện. Nếu mỗi bài viết là một event, tổng DPS bị đếm trùng. Nếu năm đăng tin thay năm lợi nhuận, payout và mức thay đổi bị tính sai.

Nên nghiên cứu **mô hình sự kiện có phiên bản và các thành phần DPS**, với bảng đối chiếu thủ công. Đây là phần nghiệp vụ tạo độ tin cậy cho dataset, không chỉ một lịch trên dashboard.

## 2. Bằng chứng ban đầu

[VNM 174349](https://www.vsd.vn/vi/ad1/174349) gộp hai năm lợi nhuận trong một lịch. [VSH 174490](https://www.vsd.vn/vi/ad/174490) sửa lịch theo hướng sớm hơn. Đã đọc hai trang qua web, chưa crawl local hoặc xác nhận thực trả; chi tiết ở [khảo sát](../03-khao-sat-nguon-thuc-te.md).

Hai ví dụ đủ hỗ trợ thiết kế component/amendment, chưa chứng minh tần suất lỗi trên thị trường.

## 3. Câu hỏi nghiên cứu

- I3-RQ1: đối chiếu phiên bản thay đổi tổng DPS và số sự kiện bao nhiêu so với cách coi mỗi thông báo là một event?
- I3-RQ2: phân bổ đúng profit_year thay đổi bao nhiêu quan sát firm-year?
- I3-RQ3: đủ bằng chứng thực trả ở bao nhiêu cửa sổ, hay cần chọn đích cổ tức được công bố?
- I3-RQ4, mở rộng: thay đổi lịch liên hệ chỉ số dòng tiền thế nào, khi phân biệt dời sớm với dời muộn?

RQ4 chưa là yêu cầu MVP. Hoãn lịch, giảm DPS và không chi là ba kết quả khác nhau.

## 4. Phạm vi và sản phẩm

Tiền mặt trước; quyền cổ phiếu chỉ dùng để phân biệt loại và theo dõi thay đổi cơ sở cổ phiếu. Thu thập lịch sử phù hợp BCTC/cutoff, không chỉ 2020–2024 theo ngày thông báo vì cổ tức năm lợi nhuận đó có thể công bố sau 2024.

Sản phẩm: gold notices, event registry, versions/components, coverage ledger, bảng tác động dedupe/phân bổ, timeline và quyết định loại nhãn. Liên kết với VN-FR-07/08/12.

## 5. Tiêu chí và phương án dự phòng

Đánh giá đúng DPS/ngày/loại, pair precision/recall ghép trùng và số nhãn thay đổi. Mọi trạng thái paid cần chứng cứ phù hợp; lịch đã qua không đủ. Nếu không có bằng chứng thực trả, nghiên cứu được phép đổi đích sang “giảm mức được công bố” sau quyết định pilot và cập nhật đề cương.

Nếu nguồn lịch sử thiếu, ưu tiên event timeline và báo độ phủ; giữ unknown. Không cố hoàn thành bảng nhãn bằng cách điền 0.

## 6. Tài liệu cần thiết

[Tài chính sự kiện](02-kien-thuc-tai-chinh.md), [IT phiên bản](03-ky-thuat-it.md), [đối chiếu/đánh giá](04-du-lieu-thi-nghiem-danh-gia.md), V02/V03 trong [sổ nguồn](../02-so-tai-lieu-tham-khao.md).

Bước tiếp: đọc ít nhất 20 thông báo gồm các chuỗi điều chỉnh, tìm nguồn đầu tiên và bằng chứng kết quả; không chỉ lấy 20 thông báo đơn giản độc lập.
