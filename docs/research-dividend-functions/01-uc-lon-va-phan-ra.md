# Cấu trúc UC lớn theo mục tiêu sử dụng

**Lịch sử nghiên cứu trước CR-AN-03:** phần sàng lọc/criteria/pass-fail-unknown G01 và BUC04 cũ đã loại theo yêu cầu người thực hiện ngày11/10/2026. Chỉ kế thừa lưu nhận xét/câu hỏi/bằng chứng và snapshot. [SRS v3.3/mục18](../research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md) và [danh mục UC v2.0](../research-platform/27-yeu-cau-chuc-nang-va-vi-du.md) là nguồn hiện hành; prototype cũ giữ làm bằng chứng lịch sử.

Ngày 11/10/2026. BUC là UC nghiệp vụ cấp hệ thống; các UC01–UC08 của SRS cũ được giữ làm luồng phân rã để truy vết. Không coi mỗi bước xử lý dữ liệu là một chức năng nghiệp vụ ngang hàng. Khi trình bày với thầy, chọn một UC nhỏ đã làm, nêu đầu vào → xử lý → đầu ra → minh chứng; khi mô tả sản phẩm, dùng năm UC lớn sau.

| UC lớn | Tác nhân và vấn đề thực tế | Kết quả hoàn chỉnh | Phân rã để triển khai |
|---|---|---|---|
| BUC01 — Quản lý hồ sơ dữ liệu doanh nghiệp | Người vận hành cần tập dữ liệu có thể phân tích và tra soát | Hồ sơ theo doanh nghiệp/kỳ, dữ liệu đã duyệt, độ đầy đủ và lịch sử | B01.1 phạm vi; B01.2 thu/cập nhật; B01.3 trích/chuẩn hóa; B01.4 duyệt; B01.5 kiểm chất lượng/phục hồi |
| BUC02 — Đánh giá nền tảng tiền mặt cho cổ tức | Người đọc cần biết lợi nhuận chuyển thành tiền ra sao, tiền tạo ra bao phủ khoản chi thế nào | Bảng đối chiếu LNST–CFO, cầu nối CFO và phân tích tiền sau CAPEX/phân phối có nguồn | B02.1 xu hướng; B02.2 cơ cấu; B02.3 cầu nối; B02.4 bao phủ G02; B02.5 luận điểm cần tra soát |
| BUC03 — Tra soát lịch sử chính sách và quyền cổ tức | Người đọc cần phân biệt thay đổi chính sách, dữ liệu thiếu và thay đổi số cổ phiếu | Lịch sử tiền mặt theo năm lợi nhuận, lịch quyền và lịch sử so sánh trên basis xác định | B03.1 vòng đời; B03.2 tổng theo năm; B03.3 coverage; B03.4 basis G03; B03.5 giải thích biến động |
| BUC04 — Sàng lọc và đối chiếu ứng viên cổ tức | Người nghiên cứu cần chọn hồ sơ để đọc sâu từ tập theo dõi | Danh sách đạt/không đạt/chưa đủ cơ sở theo tiêu chí, giải thích từng điều kiện | B04.1 chọn tập; B04.2 điều kiện; B04.3 đánh giá G01; B04.4 đối chiếu; B04.5 lưu bộ tiêu chí |
| BUC05 — Quản lý hồ sơ thẩm định cổ tức | Người nghiên cứu cần ghi nhận nhận xét và kiểm tra lại về sau | Hồ sơ có số liệu, luận điểm, nguồn, việc cần tra soát và snapshot tái lập | B05.1 lập hồ sơ; B05.2 ghi nhận luận điểm; B05.3 tra soát nguồn; B05.4 xuất/replay; B05.5 kiểm lại khi dữ liệu đổi (giai đoạn sau) |

## Luồng đầu cuối và ranh giới

Người vận hành hoàn tất BUC01 → người đọc đánh giá BUC02/03 → người nghiên cứu chọn ứng viên BUC04 → lưu hồ sơ BUC05. Dữ liệu thiếu có thể tạo hồ sơ cần bổ sung; không bị xóa khỏi tập để danh sách còn lại trông đầy đủ. Truy vết nguồn là năng lực dùng chung của mọi UC, không tách thành sản phẩm độc lập. Kiểm thử/backup là năng lực vận hành trong BUC01.

BUC05 quản lý quá trình thẩm định; chưa có mua bán, tài khoản chứng khoán hay danh mục vị thế. Các tác nhân có thể là cùng một người ở ứng dụng local. Quan hệ giữa UC thể hiện phụ thuộc dữ liệu, không mặc định mọi quan hệ là UML `include` hoặc `extend`.

## Đặc tả mục tiêu từng UC

**BUC01.** Kích hoạt: khởi tạo/cập nhật pilot. Đầu vào: doanh nghiệp, kỳ, nguồn, as_of, tài liệu. Luồng: thiết lập ledger → thu phiên bản → trích candidates → kiểm tra → người vận hành duyệt → công bố facts. Đầu ra: snapshot dữ liệu có provenance và coverage. Ngoại lệ: nguồn lỗi, OCR sai, scope mơ hồ hoặc bản sửa chưa xử lý giữ pending/blocking. Hoàn thành khi người đọc sử dụng được hồ sơ hoặc biết chính xác mục nào còn thiếu. Không hoàn thành chỉ vì tải được PDF.

**BUC02.** Kích hoạt: mở hồ sơ tiền mặt. Đầu vào: facts cùng kỳ/chủ thể, các dòng cầu nối và CAPEX/phân phối được chọn. Luồng: kiểm điều kiện → tính xu hướng/tỷ số/cầu nối → tính bao phủ → hiển thị operands và giới hạn → tạo vấn đề cần đọc. Đầu ra: kết quả số và lập luận mô tả. Thiếu CAPEX không chặn xem LNST/CFO; chỉ chặn kết quả phụ thuộc CAPEX. Không kết luận nguyên nhân hoặc tính bền vững chỉ từ một năm.

**BUC03.** Kích hoạt: tra soát chính sách/lịch sử. Đầu vào: thông báo, components, coverage, sự kiện cổ phiếu. Luồng: resolve hiệu lực → tổng năm lợi nhuận → kiểm basis → hiển thị DPS gốc và kết quả trên basis tham chiếu khi hợp lệ. Đầu ra: thay đổi có thể giải thích, hoặc trạng thái chưa so sánh được. Sửa lịch không đổi chính sách tiền mặt; hủy quyền không tự biến cả năm thành không cổ tức.

**BUC04.** Kích hoạt: chọn bộ tiêu chí. Đầu vào: tập doanh nghiệp, cửa sổ năm, snapshot và điều kiện. Luồng: kiểm tương thích → đánh giá từng điều kiện → tổng hợp ba trạng thái → đối chiếu 2–3 hồ sơ → chọn hồ sơ cần đọc. Đầu ra: danh sách và giải thích đủ tái tính. Người dùng có thể chọn hồ sơ không đạt để tra soát; đây là hỗ trợ thẩm định, không bộ máy khuyến nghị lệnh.

**BUC05.** Kích hoạt: lưu kết quả thẩm định. Đầu vào: bộ lọc, kết quả BUC02–04, ghi chú. Luồng: tạo dossier → ghi luận điểm gắn nguồn → ghi câu hỏi còn mở → freeze phiên bản → xuất/replay. Đầu ra: hồ sơ có thể mở lại sau khi số liệu hiện hành đổi. Không tự đổi ghi chú người dùng thành sự thật nguồn; ghi chú có author/time và phân biệt với dữ liệu đã duyệt.

## Ánh xạ bảo toàn yêu cầu

| UC lớn | Yêu cầu nền | Luồng phân rã cũ | Bổ sung |
|---|---|---|---|
| BUC01 | FR01–FR18, FR33, FR36–FR38 | UC01–UC04, UC08 | Nhập/duyệt trường mới D01/D05; hạ tầng dùng chung |
| BUC02 | FR25–FR27; E01–E10 theo mục 15 | UC06, UC-E01–UC-E03 | D01–D04 / TC-D01–TC-D04 |
| BUC03 | FR19–FR24, FR28 | UC05, phần lịch sử UC06 | D05–D08 / TC-D05–TC-D08 |
| BUC04 | FR29–FR30, FR32 | phần lọc UC06 | D09–D10 / TC-D09–TC-D10 |
| BUC05 | FR31, FR34–FR35 | UC07, tra soát trong UC06 | D11–D12 / TC-D11–TC-D12 |

Một FR có thể được sử dụng bởi nhiều UC; bảng ghi UC chịu trách nhiệm chính. PF01–PF09 trong tài liệu nhu cầu là nhóm năng lực hỗ trợ được kế thừa, không tiếp tục dùng làm danh mục UC lớn. Không đổi ID để tránh đứt truy vết code/test/plan trước đây. BUC04 hiện có lọc trường hợp trong baseline; phần mới là tiêu chí lưu được, ba trạng thái và hồ sơ tác vụ.
