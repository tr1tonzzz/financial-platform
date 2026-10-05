# 07 — Kế hoạch 13 tuần, thí nghiệm và kiểm thử

**Trạng thái cập nhật05/10/2026:** hướng kết hợp đã được tích hợp vào [SRS v3.1](../research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md), CR-PCD-01/mục15, theo yêu cầu cập nhật tài liệu của người thực hiện. Tối thiểu một ca cầu nối là nghĩa vụ dự thảo; E05/E10 và ca thêm có điều kiện. Nội dung đề xuất ngày04/10 bên dưới là cơ sở nghiên cứu; các câu “chưa tích hợp/chờ change record” mô tả trạng thái lúc đó, được thay bởi SRS v3.1. Chưa có phê duyệt giảng viên hoặc kiểm thử ứng dụng đã chạy. Kế hoạch/checklist v3 là lịch triển khai duy nhất; bảng tuần/giờ trong hồ sơ nghiên cứu là phương án trước tích hợp.

Đây là phương án tích hợp extension vào [kế hoạch13 tuần hiện hành](../research-platform/04-ke-hoach-13-tuan.md), không tự thay lịch đã chọn. Tuần tính từ ngày bắt đầu project, chưa gán ngày lịch khi người thực hiện chưa chốt.

## 1. Kế hoạch và đầu ra

| Tuần | Công việc | Bằng chứng/gate |
|---|---|---|
| 1 | Chốt câu hỏi, phạm vi, thuật ngữ; trao đổi đề cương09 | G0: tên/phạm vi/rubric; ghi điểm chưa được phê duyệt |
| 2 | Lập expected ledger3 × 3, đọc thủ công ca DHG/VNM, chọn nguồn | Bảng nguồn/context/gold development; báo cáo mốc 2 |
| 3 | Discovery BCTC và notices, raw versions; thử OCR/review | Log tự tìm thật, không chỉ danh sách URL file |
| 4 | Hoàn thành lát cắt pilot và đo giờ/field/event | G1: khả thi baseline; quyết định có mở rộng và nhận extension |
| 5 | Lifecycle/components/coverage; thiết kế bridge lines/roles | Fixtures gộp năm/sửa/hủy; bridge một năm có source |
| 6 | Cầu nối và residual, review, so sánh cột năm | G2: ít nhất1 ca thật đối chiếu; báo cáo mốc 6 |
| 7 | Dashboard LNST–CFO–DPS, drill-down nguồn, case composer | Luồng đọc case hoàn chỉnh; partial hiển thị đúng |
| 8 | Freeze mẫu, formula/config, gold và holdout | G3: tách lineage phát triển/đánh giá; báo cáo mốc 8 |
| 9 | Đo extraction/ghép/bridge trước–sau review | Kết quả counts/denominators, lỗi và phút sửa |
| 10 | Thử tác vụ người dùng và hoàn thiện export/replay | So thời gian/đúng câu trả lời; báo cáo mốc 10 |
| 11 | Sửa lỗi, regression đúng phạm vi, backup/restore | Không sửa gold để hợp parser; rerun phần bị ảnh hưởng |
| 12 | Viết kết quả, limits, hướng tốt nghiệp; diễn tập demo | G4: hồ sơ nghiệm thu theo baseline+CR chấp nhận |
| 13 | Hoàn tất báo cáo, demo, bàn giao source/data manifest | Dataset có provenance, case thật, tài liệu chạy lại |

Giữ nhịp báo cáo cuối tuần 2/4/6/8/10/12 và tổng kết13. Không phát sinh một lịch báo cáo cạnh tranh với checklist cũ.

## 2. Ngân sách công sức extension

Giả định lập kế hoạch: một người có thể dành12–15 giờ/tuần, tổng156–195 giờ; đây **không phải** quỹ giờ người dùng đã xác nhận. Extension dự kiến24–40 giờ: mapping/gold4–6; schema/validator6–10; UI/source6–10; kiểm thử/case/đánh giá8–14. Ước lượng chưa qua đo; không cộng40 giờ lên kế hoạch cũ mà mặc định vẫn kịp.

Ở G1, lấy giờ thực tế cho report/event/page, số templates còn lại và giờ việc nền. Dùng `giờ còn cần = việc nền còn lại + extension + dự phòng`; chỉ nhận extension khi nhỏ hơn quỹ giờ còn lại. Nếu không đủ, giảm từ3 ca xuống1 ca hoặc hoãn extension; không cắt discovery/review/truy nguồn cốt lõi để giữ số biểu đồ. Tối thiểu giữ khoảng20% quỹ còn lại làm dự phòng theo kế hoạch đề xuất, cập nhật sau pilot.

## 3. Thiết kế đánh giá hệ thống

**Tập phát triển:** DHG2025 và thông báo VNM đã dùng trong nghiên cứu, cùng tài liệu gần trùng/phiên bản của chúng. **Holdout:** report/template/event lineage chưa dùng sửa parser/mapping. Cột2024 trong DHG2025 không phải holdout độc lập. Không đưa bản tiếng Anh của cùng báo cáo sang holdout rồi gọi tài liệu mới.

Giữ expected targets trước khi trích; mẫu số gồm cả trường thiếu. Đo discovery coverage trên ledger đã rà thủ công, extraction joint correctness đúng giá trị/đơn vị/kỳ/scope/metric, component joint correctness, review effort, residual và provenance. Cầu nối khớp tổng không đủ chứng minh mọi dòng đúng: hai lỗi có thể triệt tiêu; cần đối chiếu từng dòng với gold.

So ba chế độ nền: B0=text-only; B1=text+OCR/mapping; B2=B1+review. Với extension, báo riêng phần chép tay. Công bố cả lỗi trước và sau review; B2 không là accuracy tự động. Chất lượng trường bridge đo trên mọi leaf kỳ vọng, không chỉ các dòng hệ thống tìm thấy.

## 4. Thí nghiệm trả lời RQ2 và RQ3

**RQ2:** cùng bộ câu hỏi trên hai giao diện/đầu ra: A=bảng LNST/CFO/tỷ số và nguồn; B=A+cầu nối/đóng góp/truy nguồn theo dòng. Câu hỏi: lợi nhuận và CFO có cùng chiều, dòng nào đóng góp lớn, có thể kết luận gì về cổ tức, nguồn nằm đâu? Dùng2–3 ca, hoán đổi thứ tự A/B và phân ca tương đương nếu có người thử để giảm học đáp án. Ghi số câu đúng, số diễn giải vượt nguồn, thời gian và số lần mở tài liệu. Nếu chỉ sinh viên tự làm, gọi là walkthrough tự đánh giá, không tuyên bố bằng chứng tiết kiệm thời gian với cộng đồng người dùng.

**RQ3:** tạo hai bảng từ cùng nguồn freeze: naive join theo năm công bố và correct join theo profit_year/component/coverage. Đếm số firm-year thay đổi, amount bị phân bổ khác, số nhận xét phải đổi; nguồn gốc vẫn là chuẩn để xác định đúng. Không tính naive join thành lựa chọn hợp lệ để sản phẩm dùng. Thử thêm một revision để so snapshot; không dùng thông tin sau cutoff trong kết quả as-of.

Pilot 9 firm-year, mở rộng tối đa24 firm-year trong phương án này. Không đủ cơ sở biến thành mô hình nhiều biến dự báo thị trường. Thống kê mô tả/tương quan chỉ thăm dò, ghi n doanh nghiệp, n năm, missing và selection. Các firm-year cùng doanh nghiệp không độc lập; không dùng p-value đơn giản để tuyên bố quy luật. Không đặt một ngưỡng n tùy ý là đủ cho hồi quy; cần thiết kế/power và phân bố nhãn khi mở rộng sau.

## 5. Danh mục kiểm tra extension

Các P01–P11 là kế hoạch nghiệm thu, **chưa chạy trên app**. Script nghiên cứu hiện chỉ xác nhận số học ca thật và cấu trúc tài liệu; không được ghi tất cả tests dưới đây pass.

| ID | Đầu vào | Kết quả kỳ vọng |
|---|---|---|
| P01 | LNTT100, khấu hao20, vốn lưu động−30, thuế tiền−10, CFO80 | Tính80, residual0, cùng context |
| P02 | Thêm subtotal120 vào P01 | Tổng vẫn80 vì subtotal không cộng lại |
| P03 | Bỏ dòng−30 khỏi P01 | Partial; observed sum110, residual−30; không tự gọi khoản thiếu là tồn kho |
| P04 | Dòng VND và triệu VND; ngoặc âm; scope khác | Đổi đơn vị có source, giữ dấu; khác scope bị chặn |
| P05 | BCLCTT trực tiếp hoặc phương pháp unknown | Hiển thị thu–chi/thiếu context; không tạo cầu nối gián tiếp giả |
| P06 | Hai bộ leaves đầy đủ của DHG2025/cột2024 | Delta groups khớp delta CFO; lưu report version cho cột so sánh |
| P07 | Notice VNM gồm350 cho2024 và2500 cho2025 | Tách đúng, không gán2850 cho một năm; partial không annual đủ |
| P08 | Lịch đã qua; dòng 36 trả tiền trong2025 | Không tự đánh paid từ lịch; không gán dòng 36 vào profit_year2025 |
| P09 | LNST≤0, assets≤0, denominator payout0 | Null+reason ở tỷ số liên quan; số gốc vẫn hiển thị |
| P10 | Export bridge→thay mapping/fact→replay bản cũ | Số cũ/operands/source hashes giữ nguyên; raw thiếu báo incomplete |
| P11 | Log OCR/review/nhập tay và tác vụ A/B | Báo denominator/effort đầy đủ, ghi ai đánh giá và giới hạn mẫu |

Các fixture dùng số nhỏ là giả định; ca DHG/VNM là nguồn thật. Hai loại có nhãn riêng trong manifest. Sai số phép cộng VND trong ca DHG phải bằng0; với nguồn đã làm tròn dùng rounding policy của source, không sửa số để ép0.

## 6. Tiêu chí hoàn tất và bước mở rộng

Baseline đạt các gate trong SRS v3.0; extension chỉ hoàn tất khi các Must trong CR được kiểm chứng, có ca thật đọc được, dữ liệu thiếu được xử lý và báo cáo effort/limits. Không coi số lượng tài liệu viết ra là phần mềm đã hoàn thành.

Tốt nghiệp có thể mở sâu một nhánh: semantic diff/ảnh hưởng kết luận; parser bridge nhiều template với benchmark; hoặc nghiên cứu panel lớn theo thiết kế riêng. Ưu tiên chọn một nhánh sau khi biết lỗi và nhu cầu, tránh mở cả ML, RAG, toàn thị trường và app đa người dùng cùng lúc.
