# I1 — Thiết kế dữ liệu, benchmark và đánh giá

Ngày: 03/10/2026. Trạng thái: protocol; kết quả nhỏ đã chạy ở [khảo sát](../03-khao-sat-nguon-thuc-te.md).

## 1. Bộ đối chiếu và phép chia

Theo TP: ít nhất 20 BCTC thật từ ít nhất 10 công ty, rải năm/kiểu bảng, đơn vị và dấu số. Cố định sáu facts mục tiêu mỗi báo cáo, tối đa 120 ô cần đọc; giữ ô nguồn không có và ô không đọc được riêng.

Đề xuất 10 báo cáo development và 10 evaluation, tách theo công ty hoặc nhóm bố cục để hạn chế học thuộc template. Có thể tăng số báo cáo khi gold còn quá ít. Mỗi nhóm cần nêu số công ty/file/ô chứ không chỉ tỷ lệ. Bộ này đánh giá parser, khác cohort 30 công ty dùng phân tích.

Gold gồm metric, raw/normalized value, unit, period, scope, basis, page/region, audit evidence và người đọc. Đọc gold trước khi nhìn output parser. Nếu không có người thứ hai, ghi hạn chế và đọc lại một mẫu ngẫu nhiên.

## 2. Ba thí nghiệm

| Thí nghiệm | So sánh | Cấu hình phải giữ cố định |
|---|---|---|
| E1: parser | Text toàn trang vs text theo vùng/nhãn | Cùng PDF, mapping development và facts mục tiêu |
| E2: validation | Parser trước và sau bộ quy tắc | Không sửa gold theo output; liệt kê rule/version |
| E3: công sức | Nhập tay vs parser + review | Cùng tiêu chí hoàn tất; ghi thời gian setup riêng |

E3 dễ bị người đọc nhớ số nếu làm cả hai cách trên cùng file. Đề xuất chia file tương đương, hoán đổi phương pháp giữa người đọc nếu có; nếu một người, dùng nhóm file khác và thừa nhận khác biệt bố cục/công ty.

## 3. Chỉ số và mẫu số

- **Combined accuracy:** ô đúng cả số/đơn vị/kỳ/phạm vi / tổng ô đối chiếu có đáp án xác định; kiểm tra basis thêm ở lớp metadata.
- **Extraction precision:** ứng viên đúng / mọi ứng viên parser phát ra; tính cả ứng viên trùng/sai.
- **Extraction recall:** facts mục tiêu tìm đúng / facts tồn tại trong gold.
- **Cohort coverage:** ô đã duyệt / `N_companies × N_years × 6` của cohort đã chốt; không loại công ty khó khỏi mẫu số sau chạy.
- **Provenance completeness:** facts xuất bản có toàn bộ locator/hash/version / facts xuất bản.
- **Review cost:** phút/file, phút/fact, tỷ lệ file cần sửa; báo median và P90 nếu đủ mẫu.

Tách trước/sau review, text/scan, một cột/spread, basis và đơn vị. Coverage thấp do thiếu báo cáo khác recall thấp khi parser bỏ sót số đang có.

## 4. Kiểm tra có mục tiêu

Fixture phải có: ngoặc âm, đơn vị triệu/nghìn, thiếu đơn vị, cột 2023/2024 đảo vị trí, bảng split hai trang, riêng/hợp nhất, sửa sau cutoff, tài sản cân nhưng cùng sai hệ số, nhãn mơ hồ. Assert cả trạng thái và locator, không chỉ giá trị số.

Thử chạy hai lần: raw không nhân bản; snapshot cũ giữ version; facts không tăng do duplicate. Chạy lại từ raw với config/lockfile cố định và so sánh dữ liệu sau canonical sort, không coi timestamp vận hành là nội dung phải bằng nhau.

## 5. Báo cáo kết quả và gate

File kết quả phải ghi số đúng/tổng, số công ty, confidence interval phù hợp và bảng lỗi. Ô cùng báo cáo phụ thuộc nhau; không suy độ tin cậy từ 120 ô như 120 file độc lập. Với ít file ưu tiên phân bố theo file và giới hạn.

Gate đề xuất bám SRS: accuracy ≥95%, coverage ≥80%, provenance 100%; chưa đạt thì thu hẹp kiểu PDF và công bố lý do, không đổi số đã đo. So sánh ưu thế cần cả thời gian và lỗi; tốc độ cao nhưng sửa tay nhiều có thể không tốt hơn baseline.

## 6. Artifacts khi thực hiện

Gold và danh sách file giữ hash; config/mapping; log parser/review; bảng kết quả trước/sau; manifest snapshot; báo cáo Markdown `results/i1-parser-benchmark-<snapshot>.md`. Hiện chưa tạo báo cáo final vì chưa chạy benchmark này.
