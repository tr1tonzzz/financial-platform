# Chuẩn bị bảo vệ từ lúc làm project

**Đồng bộ hướng kết hợp 05/10/2026:** theo [SRS v3.1](22-srs-dac-ta-yeu-cau-phan-mem.md), học/triển khai thêm cầu nối LNTT→CFO cho ít nhất một ca, mục tiêu 1–3 sau gate. Đọc [nghiệp vụ](../research-profit-cash-dividend/03-nghiep-vu-va-tu-dien.md) và [ca DHG/VNM](../research-profit-cash-dividend/08-ca-thuc-te-dhg-vnm.md). Minh chứng cần reviewed rows/nguồn, residual/completeness, replay và giờ nhập–duyệt; ghi LNST cạnh LNTT, cổ tức theo profit_year riêng lịch trả. Tuần2 đọc mẫu, tuần4 đo effort, tuần6 cầu nối, tuần8 freeze, tuần10 replay, tuần12–13 kết quả/demo; chưa làm thì ghi pending/not_run. Nhịp báo cáo hai tuần giữ nguyên; theo kế hoạch v3 cho giờ và tiêu chí mới.

## Năng lực và bằng chứng

Tự nói được người dùng/câu hỏi; mở BCTC/notice chỉ kỳ/unit/scope/year component; vẽ raw–candidate–reviewed và event lifecycle; đọc code một hàm; tính tay một ratio/aggregate; giải thích baseline/missing/holdout và giới hạn.

Mỗi tuần ghi một lỗi thật có input, before/after/test: nhầm đơn vị, gộp năm cổ tức, nhân bản JOIN, sửa lịch bị cộng hai lần, thiếu notice thành 0. Không học thuộc đoạn AI viết thay mà chưa chạy.

## Câu hỏi cần luyện

1. Vì sao chọn cổ tức tiền mặt? Một ngách cụ thể, nguồn có bằng chứng, nối được lịch sử với dự đoán sau này.
2. Vì sao đây là IT? Pipeline/adapters/OCR/schema/lifecycle/audit/engine/UI/tests và số đo.
3. Lợi nhuận khác CFO thế nào? Ví dụ có nguồn; scope nhóm khác nguồn tiền chia ở mẹ.
4. Vì sao năm cổ tức khác ngày trả? Tách notice gộp nhiều năm thành components.
5. Ngày thanh toán đã qua có là paid không? Cần payment confirmation, nguồn đang dùng chủ yếu là lịch.
6. Không thấy thông báo có ghi 0 không? Coverage/missing; chỉ nguồn explicit mới ghi zero.
7. Sửa/hủy và stock dividend ảnh hưởng tổng thế nào? Active version, relations và share basis.
8. Tương quan có dự báo/nhân quả không? Mẫu mô tả, phụ thuộc công ty/ngành, chưa predictor.
9. Vì sao SQLite/Streamlit? Một stack/giờ học; ranh giới module cho nâng cấp.
10. Accuracy được chấm ra sao? Toàn target joint, trước/sau review, sample và tự chấm.
11. Mới ở đâu? Triển khai/kiểm định nguồn Việt Nam, không phát minh quan hệ cổ tức hoặc OCR.
12. AI hỗ trợ phần nào? Chỉ phần đã đọc, test/nguồn đã tự kiểm và sửa mình tự làm.

## Demo

8–12 phút: đề tài/scope; schema; danh mục tới BCTC/notice; một candidate lỗi và review; một event hai năm hoặc amendment; chart/ratio và source; bảng quality/holdout; giới hạn/tốt nghiệp. Snapshot fallback đúng dữ liệu nếu mạng lỗi; không trình số giả lập như case thật.

Tuần 12 diễn tập hai lần, một lần thay input/sửa điều kiện trực tiếp. Cá nhân xong task khi chạy, kiểm tra, truy nguồn và tự giải thích được.
