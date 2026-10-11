# Thiết kế tổng quan màn hình cho năm UC

Ngày **11/10/2026**. [Bản xem tương tác](../design-5-uc/index.html), [bộ SVG chỉnh sửa được](../design-5-uc/man-hinh-5-uc-svg.zip), [danh mục và hướng dẫn nhập](../design-5-uc/README.md).

Thiết kế phục vụ nhìn tổng thể web React/FastAPI/PostgreSQL trước khi triển khai. Có năm màn hình chính và năm màn hình chi tiết. Mọi số liệu, ngày sự kiện, coverage và bố cục chứng từ là **minh họa giả định**, chưa phải dữ liệu HPG/VNM/FPT đã duyệt hoặc kết quả ứng dụng đã chạy.

**Độ đầy đủ chức năng:** bản vẽ chỉ thể hiện lát cắt, không phủ toàn bộ danh mục. Biên lợi nhuận, DuPont, phân tích quý và so sánh xu hướng chưa được vẽ đầy đủ; sáu metrics cũng chưa đủ để triển khai các nhánh đó. [Đánh giá và đề xuất tăng chiều sâu](37-danh-gia-muc-do-ho-tro-nha-dau-tu.md) có bảng từng UC nhỏ, dữ liệu và công sức. Trang duyệt phục vụ người vận hành; luồng chính của nhà đầu tư là phân tích/so sánh/cổ tức và lưu nhận xét.

## Trạng thái Figma

Đã dùng Figma tạo [tệp thiết kế](https://www.figma.com/design/GbpKDOPNhXuCYC2X2Yt7sa), khảo sát thư viện và font. Lần nhập thư viện trả lỗi kết quả vượt giới hạn kích thước, không commit thay đổi; lần tiếp theo bị chặn bởi hạn mức công cụ Starter. Canvas chưa có màn hình. Bộ SVG local là phương án bàn giao để nhập thủ công; không báo đã hoàn thành thiết kế trên canvas Figma.

SVG gồm chữ, hình và đường vector, không có ảnh chụp toàn màn hình làm lớp nền. Sau nhập cần tổ chức auto-layout, components/tokens và nối prototype trong Figma. Bản xem HTML hiện chỉ mô phỏng điều hướng, chưa kết nối API hoặc thực hiện duyệt/lưu/xuất thật.

## Nhóm màn hình lớn → chi tiết

| UC lớn | Màn hình chính | Màn hình chi tiết / năng lực dùng chung |
|---|---|---|
| UC-1 — Khai thác dữ liệu tài chính | Bộ chọn doanh nghiệp/kỳ, bảng sáu chỉ tiêu, nguồn, thiếu và xuất | Định nghĩa/nguồn một ô; duyệt và tra soát cho vai trò vận hành |
| UC-2 — Phân tích tài chính | Biểu đồ LNST–CFO, tỷ số có điều kiện, câu hỏi đọc thêm | Cầu nối LNTT→CFO; hồ sơ nhận xét và bằng chứng |
| UC-3 — So sánh doanh nghiệp | Nhóm tự chọn cùng năm/scope; số tuyệt đối và biểu đồ tỷ số | Nguồn từng mã; lưu nhóm/nhận xét; xu hướng nhóm nhiều năm là bước mở rộng chưa vẽ riêng |
| UC-4 — Theo dõi doanh nghiệp | Danh sách tự chọn, công bố, bản cập nhật và lịch sự kiện | Tiếp tục vào dữ liệu/phân tích/cổ tức, giữ nhận xét cũ; triển khai sau các UC ưu tiên |
| UC-5 — Phân tích cổ tức | DPS theo năm lợi nhuận, các đợt, coverage và bối cảnh tiền | Kiểm cơ sở cổ phiếu; chặn tăng trưởng/điều chỉnh/payout khi chưa đủ dữ liệu; lưu hồ sơ |

## Luồng xem nhanh

1. UC-1 → chọn ô CFO → nguồn/định nghĩa → màn hình duyệt hỗ trợ.
2. UC-1 → UC-2 → xem xu hướng → cầu nối → hồ sơ đã lưu.
3. UC-2 → UC-3 → nhóm tự chọn → nhận xét có bối cảnh.
4. UC-4 → công bố/sự kiện của doanh nghiệp theo dõi → dữ liệu hoặc cổ tức.
5. UC-5 → lịch sử DPS → cơ sở cổ phiếu → nguồn khoản chi/cầu nối → hồ sơ nhận xét.

Chỉ một số nút và điều hướng được nối trong bản xem. Bộ chọn, form sửa, xuất file số liệu và lịch thật là nội dung thiết kế cần triển khai sau. Màn hình minh họa nguồn được dùng chung, không giả định đã mở đúng nguồn thật cho mọi chỉ tiêu/mã.

## Liên hệ kế hoạch và giới hạn

- Tuần 1–2 ưu tiên màn hình UC-1, nguồn và duyệt; dựng browser→API→PostgreSQL chạy được.
- Tuần 3–5 triển khai lát cắt UC-2/3; biểu đồ nằm trong UC tương ứng.
- Tuần 6–8 UC-5 và cầu nối theo ca; UC-4 tuần 9 có điều kiện.
- Các màn hình không tự tăng phạm vi SRS. Không bổ sung sàng lọc, xếp hạng, khuyến nghị mua/bán, danh mục/định giá hoặc dự báo ML.
- Payout được hiển thị ở trạng thái chưa tính khi thiếu dữ liệu; chưa thiết kế quy trình payout hoàn chỉnh. Không coi CFO−CAPEX là FCFE hoặc thông báo là tiền đã thực chi.

Căn cứ: [danh mục UC](27-yeu-cau-chuc-nang-va-vi-du.md), [stack](31-chot-pham-vi-va-stack-paddleocr.md), [metrics](35-dac-ta-metrics-tu-bao-cao-02.md), [kế hoạch 10 tuần](32-ke-hoach-10-tuan-tiep-theo.md). [Kết quả kiểm bản xem](../design-5-uc/validation.json) chỉ đánh giá artifact thiết kế local, chưa đánh giá canvas Figma hoặc nghiệm thu phần mềm.
