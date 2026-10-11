# Các chức năng hiện tại đã hỗ trợ người đầu tư và phân tích tài chính đến đâu?

Ngày **11/10/2026**. Kết luận nghiên cứu và đề xuất để lựa chọn; **chưa thay phạm vi SRS hoặc kế hoạch 10 tuần**. Căn cứ: [danh mục 38 chức năng](27-yeu-cau-chuc-nang-va-vi-du.md), [SRS hiện hành](22-srs-dac-ta-yeu-cau-phan-mem.md), [thiết kế 5 UC](36-thiet-ke-man-hinh-5-uc.md), [nghiên cứu mã nguồn bổ sung](../research-investor-support/README.md).

## 1. Trả lời trực tiếp

**Có cả hai vấn đề: bản vẽ chưa thể hiện hết yêu cầu, và lát cắt thực hiện hiện tại còn khá hẹp.**

- **Năm UC lớn phù hợp về cách tổ chức:** khai thác → phân tích → so sánh → theo dõi → phân tích cổ tức. Chưa cần thêm UC lớn để làm hệ thống có ích hơn.
- **Bản vẽ là demo tổng quan:** 10 màn hình dùng số giả định; một số liên kết điều hướng hoạt động. Chọn chỉ tiêu, duyệt, lưu và xuất chưa chạy thành chức năng ứng dụng. Màn hình đang mở `review` phục vụ người vận hành, không đại diện trải nghiệm chính của nhà đầu tư.
- **Danh mục yêu cầu rộng hơn bản vẽ:** đã có biên lợi nhuận, cơ cấu tài chính, DuPont, đối chiếu cùng kỳ, so sánh xu hướng và hồ sơ nhận xét. Nhiều mục vẫn là ứng viên bổ sung, chưa thuộc nghiệm thu SRS.
- **Sáu chỉ tiêu lõi đủ bắt đầu kiểm chứng dữ liệu và phân tích lợi nhuận–CFO; chưa đủ đánh giá tài chính doanh nghiệp toàn diện.** Chưa biết doanh thu, lợi nhuận gộp, tài sản/nợ ngắn hạn và nợ vay thì không trả lời tốt về tăng trưởng, hiệu quả và áp lực tài chính.
- **Chưa có bằng chứng hệ thống cải thiện quyết định hay lợi nhuận đầu tư:** cần ứng dụng chạy được và người dùng thử các tác vụ cụ thể. Nghiên cứu GitHub chỉ chứng minh có cách làm đáng tham khảo.

Đích hợp lý của project: **giúp người dùng tự phân tích doanh nghiệp và cổ tức trên dữ liệu có thể kiểm lại**, với HPG/VNM/FPT là mẫu kiểm chứng. Để trả lời thêm “giá nào phù hợp để mua?” hoặc “khoản đầu tư của tôi hiệu quả ra sao?”, cần lớp giá/giả định định giá hoặc sổ giao dịch riêng; các phần này đang ở UC-F07/06 mở rộng.

## 2. Người dùng cần trả lời gì, hệ thống còn thiếu gì?

| Câu hỏi thực tế | Đầu ra hữu ích | Hiện tại | Đề xuất |
|---|---|---|---|
| Doanh nghiệp đang tăng trưởng hay suy giảm? | Doanh thu, lợi nhuận, CFO nhiều kỳ; thay đổi mức và % | Demo LNST–CFO; chưa có doanh thu lõi | Làm sâu F02.1/.2, bổ sung doanh thu |
| Lợi nhuận tăng do bán được nhiều hơn hay biên tốt hơn? | Biên gộp/ròng và phân rã doanh thu–biên | Đã nêu F02.2, chưa vẽ/chưa đủ dữ liệu | Thêm lợi nhuận gộp; nối biểu đồ với dòng nguồn |
| Lợi nhuận có chuyển thành tiền không, khoản nào gây chênh lệch? | Xu hướng LNST–CFO và cầu nối LNTT→CFO | Có đặc tả/case nghiên cứu, demo minh họa | Hoàn thành F02.4/.5 theo ca, không chỉ tỷ số |
| Doanh nghiệp có áp lực thanh toán/nợ vay không? | Tài sản/nợ ngắn hạn, nợ vay, cấu trúc kỳ hạn | Demo nợ phải trả/tài sản không trả lời đủ | Mở nhánh phân tích thanh khoản/nợ vay trong UC-F02 |
| So với những công ty tôi chọn, điểm khác nhau là gì? | So số, tỷ số và xu hướng cùng kỳ; nêu khác ngành | Demo cùng một năm, số và vài tỷ số | Hoàn thành F03.3, không xếp hạng “tốt nhất” |
| Cổ tức đã công bố thế nào, các khoản chi có được CFO bao phủ không? | DPS/đợt/năm lợi nhuận; CFO–CAPEX–phân phối; basis | Có demo và đặc tả, chưa có lịch sử mẫu hoàn chỉnh | Hoàn thành F05.1–.4; payout khi đủ chủ thể |
| Tôi dựa vào điều gì để tiếp tục theo dõi doanh nghiệp? | Nhận xét, câu hỏi còn mở, nguồn và phiên bản lưu | Có F02.8/F05.6 và D11/12; demo hồ sơ tĩnh | Hoàn thành lưu/mở lại/xuất một lần phân tích |
| Dữ liệu mới làm thay đổi nhận xét cũ ở đâu? | Đối chiếu số trước/sau và mở hồ sơ cũ | Có nền phiên bản, chưa có luồng sử dụng thật | F04.4/.5 sau core, không tự khuyến nghị mua/bán |
| Cổ tức tương ứng bao nhiêu với giá đang xét? | Lợi suất có ngày giá, kỳ DPS và cơ sở cổ phiếu | Chưa có giá; không thuộc lát cắt đã chốt | Nghiên cứu sau core, không đưa vào MVP bằng nhãn mới |

Khung này là suy luận thiết kế từ nhu cầu trong trao đổi và nguồn tham khảo, chưa là kết quả phỏng vấn nhà đầu tư. CFA Institute nhấn mạnh phân tích phải kết hợp số liệu với diễn giải, so sánh và bối cảnh; tỷ số đơn lẻ chưa giải thích nguyên nhân. [Financial Analysis Techniques](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/financial-analysis-techniques).

## 3. Phân biệt bản vẽ, danh mục và phần phải thực hiện

“Có trong demo” dưới đây chỉ nghĩa **đã minh họa**, không nghĩa đã chạy với dữ liệu thật. Không dùng tỷ lệ màn hình/ID để báo phần trăm hoàn thành chức năng.

| UC và chức năng nhỏ | Bản vẽ hiện tại | Danh mục/SRS và khoảng trống |
|---|---|---|
| **UC-F01 — Khai thác dữ liệu tài chính doanh nghiệp** | Bảng sáu chỉ tiêu, nguồn, độ đầy đủ; trang vận hành | Hợp với lát cắt đầu, nhưng chưa là kho đầy đủ ba BCTC |
| F01.1 Tra cứu doanh nghiệp và hồ sơ cơ bản | Có bộ chọn minh họa | Tìm kiếm/hồ sơ thực chưa chạy |
| F01.2 Xem dữ liệu tài chính nhiều kỳ | Có bảng sáu dòng | Mở rộng nhóm dòng theo câu hỏi phân tích; không bắt buộc nhập toàn bộ PDF |
| F01.3 Chọn và xuất bộ dữ liệu | Có nút/chọn kỳ tĩnh | Chọn chỉ tiêu và xuất thật chưa chạy; chọn nhiều chỉ tiêu là bổ sung |
| F01.4 Tra cứu định nghĩa và truy xuất bằng chứng | Có màn hình nguồn minh họa | Cần đúng trang/cột nguồn thật cho từng ô |
| F01.5 Xem độ đầy đủ và phiên bản dữ liệu | Có ví dụ ô thiếu | Cần phân biệt chưa tìm/chờ duyệt/đã duyệt/đã sửa |
| F01.6 Thu thập, chuẩn hóa và duyệt dữ liệu tài chính | Có trang review | Chức năng hỗ trợ vận hành; không là trung tâm màn hình của nhà đầu tư |
| **UC-F02 — Phân tích dữ liệu tài chính** | LNST–CFO, vài tỷ số, cầu nối và hồ sơ | Đây là nhóm cần tăng chiều sâu nhất |
| F02.1 Xem biểu đồ và bảng xu hướng tài chính | Đã vẽ LNST–CFO | FR25/32 có nền; bộ chọn và liên kết bảng–biểu đồ cần làm rõ |
| F02.2 Phân tích tăng trưởng và biên lợi nhuận | Chưa vẽ | Đã có trong danh mục; doanh thu/biên vẫn ngoài sáu trường lõi |
| F02.3 Phân tích cơ cấu tài sản và nguồn vốn | Chỉ tiền/tài sản, nợ phải trả/tài sản | FR27 hẹp; cơ cấu chi tiết và nhánh thanh khoản/nợ vay cần bổ sung |
| F02.4 Phân tích khả năng chuyển lợi nhuận thành tiền | Đã vẽ xu hướng/tỷ số | FR26 có nền; cần đọc nhiều kỳ, không kết luận từ CFO/LNST một năm |
| F02.5 Phân rã dòng tiền và chênh lệch các kỳ | Có cầu nối một kỳ | E01–E10 theo ca; phân rã thay đổi giữa hai kỳ chưa được vẽ |
| F02.6 Phân tích sinh lời và DuPont | Chưa vẽ | Có trong danh mục, cần số dư bình quân và scope phù hợp |
| F02.7 Đối chiếu quý/cùng kỳ và kế hoạch–thực hiện | Chưa vẽ | Có trong danh mục; ngoài mẫu năm 2023–2025 hiện tại |
| F02.8 Lưu, chú thích và xuất lần phân tích | Có hồ sơ tĩnh | FR34/35, D11/12 có nền; lưu/mở lại/xuất chưa chạy |
| **UC-F03 — So sánh tài chính doanh nghiệp** | Nhóm tự chọn, cùng năm | Không thể gọi ba mã khác ngành là benchmark ngành |
| F03.1 So sánh chỉ tiêu nhiều doanh nghiệp | Đã vẽ | Bảng nhiều doanh nghiệp là bổ sung đã nằm trong kế hoạch core |
| F03.2 So sánh tỷ số và cơ cấu | Đã vẽ vài tỷ số | Tái sử dụng metric, quy tắc và nguồn của UC-F02 |
| F03.3 So sánh xu hướng qua nhiều kỳ | Chưa vẽ riêng | Có trong danh mục; bổ sung biểu đồ cùng chỉ tiêu theo năm |
| F03.4 Đối chiếu với nhóm ngành xác định mẫu | Chưa vẽ | Không phù hợp mẫu ba mã đã chốt; để sau |
| **UC-F04 — Theo dõi doanh nghiệp và sự kiện** | Danh sách, công bố, lịch minh họa | Giữ ưu tiên sau 01/02/03/05 |
| F04.1 Quản lý danh sách theo dõi | Đã vẽ | Danh sách tự chọn, chưa lưu thật |
| F04.2 Xem công bố mới theo doanh nghiệp | Đã vẽ | Cần nguồn/ngày công bố và loại văn bản |
| F04.3 Xem lịch sự kiện có nguồn | Đã vẽ | Cần phân biệt dự kiến/đã sửa/xác nhận, không suy đã trả tiền |
| F04.4 Đối chiếu dữ liệu trước/sau cập nhật | Có ví dụ sửa số | Cần nối phiên bản với nguồn và bối cảnh phân tích |
| F04.5 Tiếp tục phân tích từ cập nhật | Có điều hướng | Cần mở đúng hồ sơ/phiên bản, chưa phải chức năng đã chạy |
| **UC-F05 — Phân tích cổ tức** | Lịch sử DPS, đợt, tiền sau chi và basis | Chưa đủ để kết luận độ bền vững tương lai |
| F05.1 Xem lịch sử và biểu đồ cổ tức tiền mặt | Đã vẽ | Cần kiểm đủ đợt theo năm lợi nhuận |
| F05.2 Đối chiếu chính sách, quyền, lịch thanh toán | Đã vẽ một phần | Cần đặt nghị quyết/chính sách cạnh từng đợt thực tế |
| F05.3 Phân tích tiền sau chi đầu tư và phân phối | Đã vẽ một kỳ | G02 có nền; cần bối cảnh và nhiều kỳ khi dữ liệu đủ |
| F05.4 Kiểm cơ sở cổ phiếu và tính so sánh DPS | Có màn hình chặn | G03 có nền; chuỗi điều chỉnh cần chứng cứ |
| F05.5 Đối chiếu phân phối với lợi nhuận phù hợp | Chỉ minh họa “chưa đủ để tính” | Payout hoàn chỉnh là bổ sung; không gọi đã hoàn thành vì có trạng thái chặn |
| F05.6 Lưu nhận xét/câu hỏi về cổ tức | Có hồ sơ tĩnh | Dùng lại hồ sơ phân tích và bằng chứng |

UC-F06/07 là hai hướng mở rộng riêng trong danh mục, không thuộc bộ năm màn hình. Việc chưa vẽ chúng không phải lỗi thiếu màn hình của năm UC hiện tại.

## 4. Giữ UC lớn, làm sâu các nhánh có ích

### UC-F01 — Khai thác dữ liệu tài chính doanh nghiệp

**Phân rã:** tra cứu doanh nghiệp → xem bảng nhóm chỉ tiêu nhiều kỳ → chọn bộ dữ liệu → truy xuất nguồn/định nghĩa → xem độ đầy đủ/phiên bản → xuất dữ liệu.

Ví dụ: người dùng muốn lấy doanh thu, lợi nhuận và CFO của VNM qua ba năm. Người dùng chọn các dòng, thấy rõ dòng thiếu, kiểm một ô về nguồn và xuất bộ số để dùng tiếp. Phía vận hành thu/trích/duyệt là nhánh hỗ trợ, hiển thị theo vai trò.

### UC-F02 — Phân tích dữ liệu tài chính

| Nhánh nhỏ | Giải quyết gì trước? | Cách thể hiện | Dữ liệu bổ sung |
|---|---|---|---|
| **Xem xu hướng và chọn chỉ tiêu** — F02.1 | Tự xem khoản mình quan tâm thay vì chỉ một biểu đồ cố định | Bảng liên kết biểu đồ đường/cột; đổi khoảng năm, chọn điểm xem nguồn; lưu lựa chọn | Không cần thêm trường cho sáu chỉ tiêu đã có |
| **Phân tích tăng trưởng và biên lợi nhuận** — F02.2 | Phân biệt tăng quy mô với tăng hiệu quả | Doanh thu/LNST; biên gộp/ròng theo năm; thay đổi biên tính bằng điểm phần trăm | Doanh thu thuần, lợi nhuận gộp |
| **Phân tích cơ cấu, thanh khoản và nợ vay** — làm sâu F02.3 | Phân biệt tài sản lớn với khả năng đáp ứng nghĩa vụ ngắn hạn | Cơ cấu tài sản/nguồn vốn; tài sản–nợ ngắn hạn; nợ vay ngắn/dài hạn | Tài sản ngắn hạn, nợ ngắn hạn, vay/nợ thuê tài chính ngắn và dài hạn theo định nghĩa được duyệt |
| **Đối chiếu lợi nhuận với tiền và phân rã CFO** — F02.4/.5 | Biết khoản kế toán nào góp vào chênh lệch | LNST–CFO, LNTT→CFO; chọn dòng cầu nối xem chứng từ | Các dòng gián tiếp, LNTT, thuế và context; đã có kế hoạch theo ca |
| **Phân tích ROA/ROE và DuPont** — F02.6 | Biết sinh lời tăng nhờ biên, hiệu quả tài sản hay hệ số vốn | Ba thành phần đặt cạnh nhau; công thức và cơ sở bình quân | Doanh thu, số dư đầu/cuối; lợi nhuận/vốn cùng chủ thể |
| **Lưu nhận xét và bằng chứng** — F02.8 | Tạo được kết quả nghiên cứu để dùng lại | Ghi nhận xét/câu hỏi tại chỉ tiêu hoặc biểu đồ; lưu bộ chọn, bản số và nguồn; mở lại/xuất | Dùng nền dossier/snapshot, không cần thêm chỉ tiêu BCTC |

Ví dụ giả định về **doanh thu–biên**: doanh thu 1.000→1.100 tỷ, biên ròng 10%→8%; LNST 100→88 tỷ. Người dùng thấy bán được nhiều hơn nhưng lợi nhuận giảm vì biên giảm. Có thể phân rã số học theo một thứ tự khai báo: tác động doanh thu `(1.100−1.000)×10%=+10`, tác động biên `1.100×(8%−10%)=−22`; tổng `−12`. Đây là phân rã kế toán có quy ước, **chưa chứng minh nguyên nhân kinh tế**; muốn hiểu nguyên nhân phải đọc giá vốn/chi phí/thuyết minh. Phần phân rã này là đề xuất làm sâu F02.2.

Ví dụ giả định về **nợ vay**: nợ phải trả 400 tỷ có thể chứa phải trả nhà cung cấp và nhiều nghĩa vụ khác; nợ vay thực tế chỉ 120 tỷ. Hiển thị đúng hai loại giúp tránh nhận xét sai từ tỷ lệ nợ phải trả/tài sản. Tỷ số thanh toán hiện hành = tài sản ngắn hạn/nợ ngắn hạn; tỷ số không tự chứng minh các khoản phải thu/tồn kho sẽ đổi thành tiền đúng hạn.

Phải thu/tồn kho, số ngày thu tiền/vòng quay và phân tích kỳ hạn/lãi vay sâu hơn là bước sau. Hai số dư cuối năm chỉ cho thấy khoản mục đổi; không tự thay các dòng biến động trên BCLCTT hoặc chứng minh lý do CFO giảm.

### UC-F03 — So sánh tài chính doanh nghiệp

**Phân rã:** chọn nhóm công ty → chọn chỉ tiêu/kỳ/cơ sở → so số tuyệt đối → so tỷ số → so xu hướng → lưu nhận xét.

Thêm F03.3 vào thiết kế: cùng một chỉ tiêu qua 2023–2025, mỗi công ty một đường; đổi sang bảng khi cần đọc chính xác. Với dữ liệu tiền và % khác đơn vị, dùng các biểu đồ riêng. Nếu chọn chế độ năm gốc = 100, phải khai báo năm gốc và chỉ áp dụng khi cơ sở hợp lệ; giữ khả năng trở về số gốc. Mẫu ba mã khác ngành chỉ hỗ trợ đối chiếu mô tả; không tự suy công ty có biên cao hơn là đầu tư tốt hơn.

### UC-F04 — Theo dõi doanh nghiệp và sự kiện

**Phân rã:** quản lý danh sách tự chọn → xem công bố → xem lịch có nguồn → đối chiếu bản số → tiếp tục hồ sơ phân tích.

Giá trị cần thể hiện: sau công bố mới, người dùng biết mình đã đọc đến đâu và nhận xét đang dựa trên bản số nào. Giữ triển khai sau core. Không thêm bộ tự tìm mã, chấm điểm đạt/không đạt hoặc cảnh báo sàng lọc đã loại bỏ.

### UC-F05 — Phân tích cổ tức

**Phân rã:** xem lịch sử theo năm lợi nhuận → kiểm các đợt/chính sách → xem lợi nhuận/CFO/CAPEX/phân phối nhiều kỳ → kiểm cơ sở cổ phiếu → đối chiếu payout khi hợp lệ → lưu nhận xét.

Ví dụ giả định: DPS ba năm cùng cơ sở là 1.000/1.200/1.500 đồng; CFO là 120/90/80 tỷ, CAPEX 30/40/50 tỷ và khoản phân phối đã định nghĩa 40/50/60 tỷ. Bảng số dư sau hai khoản chi là +50/0/−30 tỷ giúp người dùng thấy mức chi tăng trong khi CFO giảm. Cần đọc thêm tiền đầu kỳ, vay và nguồn tài trợ; **không kết luận chắc chắn sẽ cắt cổ tức**, cũng không gọi số dư này là FCFE.

Payout có thể dùng `DPS theo năm lợi nhuận / EPS` chỉ khi cùng chủ thể cổ đông thường, kỳ, basis cổ phiếu và quy tắc lợi nhuận phù hợp; không trộn cổ tức trả trong năm với EPS của một năm lợi nhuận khác. Payout tổng tiền đòi hỏi xác định đúng khoản phân phối cho cổ đông công ty mẹ và lợi nhuận tương ứng, không lấy nguyên dòng chi cổ tức hợp nhất có thể gồm cổ đông không kiểm soát. [F05.5 và dữ liệu cần thu](29-du-lieu-can-thu-thap-cho-uc-1-2-3-5.md).

Ba năm mô tả mẫu nhỏ, chưa phản ánh đầy đủ chu kỳ kinh doanh hoặc chứng minh chính sách bền vững dài hạn.

## 5. Những phần thực sự còn thiếu, và phần chưa cần làm ngay

| Phần | Kết luận | Quan hệ với yêu cầu hiện có |
|---|---|---|
| Bộ chọn chỉ tiêu, bảng–biểu đồ–nguồn liên kết | Cần để biến màn hình thành công cụ sử dụng | Làm rõ F01.3/F02.1/.8; một số tương tác ngoài FR32 hẹp |
| Doanh thu/biên lợi nhuận | Ưu tiên bổ sung cao nhất về chiều sâu | Đã là ứng viên F02.2, cần đặc tả/metrics/TC nếu tích hợp |
| Thanh khoản và nợ vay | Khoảng trống đáng bổ sung, sau một ca dữ liệu khả thi | Làm sâu F02.3; FR27 hiện không bao phủ đầy đủ |
| So sánh xu hướng nhiều kỳ | Cần vẽ thêm, không cần UC lớn mới | F03.3 đã có trong danh mục; ngoài lát cắt so một năm |
| Hồ sơ nhận xét có nguồn/mở lại | Cần hoàn thành để có đầu ra phân tích | D11/12 có nền, chưa là app đã chạy |
| ROA/ROE/DuPont | Hữu ích nhưng sau doanh thu và số dư phù hợp | F02.6 đã có; ROE cổ đông mẹ cần thêm trường |
| Phân tích theo mảng kinh doanh/địa lý | Hữu ích để hiểu động lực, chọn một ca sau core | Đề xuất mới làm sâu F02.2; cần thuyết minh/BCTN và mapping thay đổi cơ cấu |
| Quý/TTM, kế hoạch–thực hiện | Hữu ích để theo dõi hiện tại, ngoài mẫu năm đã chốt | F02.7 đã có; không hứa hệ thống dữ liệu năm là theo dõi cập nhật đầy đủ |
| Giá, lợi suất cổ tức, P/E/P/B và kịch bản | Cần nếu mở sang quyết định mức giá | Chưa thuộc MVP; định giá/kịch bản ở UC-F07, cần CR riêng nếu chọn |
| Giao dịch, thu nhập cổ tức thực nhận, hiệu quả danh mục | Cần nếu phục vụ tài sản đã nắm giữ của cá nhân | UC-F06; cần ledger/vị thế, không suy từ watchlist |
| AI/dự đoán/tự khuyến nghị | Không cần để xử lý các khoảng trống trên | Chưa chọn; dữ liệu 3 mã × 3 năm không đủ để chứng minh mô hình dự báo |

Nghiên cứu mã Stocknear cho thấy chọn chỉ tiêu và mở biểu đồ là chức năng riêng, không chỉ một hình vẽ trên dashboard. FinanceToolkit tách profitability/liquidity/solvency và DuPont; Fincept đặt bảng, biểu đồ và xuất dữ liệu trong luồng equity research. Đây là căn cứ thiết kế, chưa là bằng chứng người dùng của project cần toàn bộ các tính năng đó. [Bằng chứng tại commit cố định](../research-investor-support/README.md).

## 6. Gói dữ liệu và công sức để lựa chọn

Giữ đích bắt buộc hiện tại **9 BCTC/54 ô lõi**. Các tổng dưới đây là **targets dự kiến nếu chọn gói**, không phải số đã thu hoặc đã duyệt. Chưa tính notice, dòng cầu nối, metadata và các bản sửa.

| Gói đề xuất | Trường mới/đầu ra | Phạm vi thử | Targets và công sức tăng thêm |
|---|---|---|---|
| A — Phân tích doanh thu và biên | Doanh thu thuần + lợi nhuận gộp; xu hướng doanh thu, biên gộp/ròng, đổi biên | Trước hết 1 công ty × 3 năm; mở 3 công ty khi ổn | Một công ty: thêm 6 ô; cả pilot: thêm 18, tổng 72. Cả pilot khoảng 12–20 giờ |
| B — Phân tích thanh khoản và nợ vay | Tài sản ngắn hạn, nợ ngắn hạn, vay/nợ thuê tài chính ngắn và dài hạn đúng định nghĩa; cơ cấu và tỷ số | Một công ty × 3 năm trước | Một công ty: thêm 12 ô; cả pilot: thêm 36. A+B cả pilot: tổng 108; B khoảng 18–28 giờ, hoặc 8–14 giờ cho một công ty |
| C — Phân tích ROA/ROE/DuPont | Số dư đầu–cuối và lựa chọn scope; doanh thu dùng lại A | Một ca cùng chủ thể trước | Chỉ tính ROA nhóm/ROE tổng khi đủ cơ sở; thiếu đầu kỳ 2023 phải thu số dư 31/12/2022. Cả 3 mã, assets+equity đầu kỳ thêm tối đa 6 ô; không tự thêm năm báo cáo đích. Khoảng 8–14 giờ cho một ca có dữ liệu sẵn |
| U — Hoàn thiện thao tác phân tích | Bộ chọn chỉ tiêu, xem số/nguồn từ biểu đồ, F03.3, ghi chú cùng bối cảnh | Dùng dữ liệu lõi | Không tăng ô BCTC; khoảng 6–10 giờ tăng thêm nếu mở rộng ngoài lát cắt hiện có |

Ước lượng do nghiên cứu này đề xuất, gồm định nghĩa, mapping/duyệt, API/React và kiểm ca; chưa đo khi triển khai. Không cộng chúng vào 195 giờ v6 như thể đã có quỹ giờ. Mở toàn A+B+U có thể tăng khoảng **36–58 giờ**; không nên tự thêm tất cả vào 10 tuần.

Với gói C, LNST tổng/tổng vốn chủ sở hữu bình quân chỉ là ROE theo cơ sở toàn nhóm được khai báo; không gắn nhãn ROE cổ đông công ty mẹ. Muốn ROE của cổ đông mẹ cần LNST thuộc cổ đông mẹ và vốn thuộc cổ đông mẹ, cùng phạm vi, cùng cơ sở bình quân. Công thức DuPont phải dùng các thành phần tương thích với định nghĩa ROE đã chọn.

**Khả thi tại Việt Nam:** Vnstock có giao diện dữ liệu ba BCTC và tỷ số, là nguồn đối chiếu ứng viên; chưa thử truy vấn thành công đủ HPG/VNM/FPT và mọi năm trong nghiên cứu này. Giữ BCTC doanh nghiệp/nguồn công bố là bằng chứng gốc và lưu mapping, không thay pipeline Paddle chỉ vì có API. [Vnstock Fundamental](https://vnstocks.com/docs/vnstock/phan-tich-co-ban-fundamental).

HPG có danh mục BCTC hợp nhất kiểm toán 2025 và công văn giải trình. FPT có BCTN số với các phần theo khối kinh doanh, thuận lợi để thử luồng đọc bối cảnh/mảng; cần đối chiếu lại thuyết minh và phạm vi trước dùng số. Chưa chứng minh corpus đủ chín báo cáo, dữ liệu từng dòng VNM hoặc nguồn giá ổn định. [HPG — báo cáo tài chính](https://www.hoaphat.com.vn/quan-he-co-dong/bao-cao-tai-chinh), [FPT — BCTN 2025, đánh giá chung](https://bctn2025.fpt.com/vi/phan-tich-hoat-dong-kinh-doanh/danh-gia-chung/).

## 7. Cách thực hiện trên stack đã chốt

| Lớp | Việc cần thực hiện | Giá trị đối với người dùng |
|---|---|---|
| PostgreSQL + SQLAlchemy/Alembic | Thêm định nghĩa chỉ tiêu/operands và facts theo scope/kỳ/version; duyệt từng ô; snapshot hồ sơ | Mở lại đúng bản số; thêm chỉ tiêu không phá dữ liệu cũ |
| FastAPI/Python | Tính metric có công thức, operands, trạng thái/lý do; trả bảng và chuỗi theo cùng bộ chọn; export số đầy đủ | Bảng/biểu đồ/công thức nhất quán; số thiếu không thành 0 |
| React/TypeScript | Chọn nhóm phân tích/chỉ tiêu; liên kết bảng–biểu đồ–nguồn; so nhiều năm; ghi chú/lưu | Người dùng tự đặt câu hỏi và kiểm câu trả lời |
| Thu thập/Paddle/duyệt | Thêm mapping dòng có mục đích; có thể nhập tham chiếu thủ công để thử một ca | Chứng minh có dữ liệu cho chức năng trước khi tổng quát hóa OCR |
| Đánh giá | Chạy ca đủ/thiếu/cross-scope/sửa số; thử tác vụ với người dùng | Phân biệt tính đúng với giúp người dùng phân tích được |

Tiền tiếp tục dùng Decimal/NUMERIC, JSON chuỗi chính xác; frontend chuyển số cho tọa độ biểu đồ, không là nguồn tính công thức. Với chỉ tiêu dẫn xuất, mở công thức phải truy lại các operands và phiên bản. Không chọn thư viện tính rồi mặc định công thức/phạm vi Việt Nam tương đương.

Ví dụ cần kiểm: tại cùng commit FinanceToolkit, `profitability_model.get_interest_coverage_ratio` dùng operating income/lãi vay; hàm cùng tên trong `solvency_model` cộng thêm khấu hao. Hàm debt-service coverage dùng nợ ngắn hạn làm proxy và mô tả rõ giới hạn. Vì vậy phải đặt nhãn theo numerator/denominator thực, không gọi mọi biến thể là một tỷ số duy nhất. [Hai công thức và lưu ý chuyển thể](../research-investor-support/README.md#kiem-cong-thuc-truoc-khi-chuyen-the).

## 8. Thứ tự đề xuất trong thời hạn hiện tại

1. **Tuần 1–2:** giữ UC-F01/Paddle/web/API/PostgreSQL đang chốt. Bổ sung khả năng mở rộng danh mục chỉ tiêu trong thiết kế dữ liệu, chưa bắt buộc thu thêm toàn bộ gói A/B.
2. **Tuần 3–5:** làm lát cắt phân tích và so sánh lõi chạy thật, nguồn và lưu kết quả. Nếu ca dữ liệu lõi ổn và còn giờ, ưu tiên **A cho một công ty**; đề xuất F03.3 dùng lại series cùng kỳ. Các phần ngoài tiêu chí v6 cần ghi rõ công sức và quyết định chọn trước khi đưa vào nghiệm thu.
3. **Tuần 6–8:** hoàn thành UC-F05, G02/G03/cầu nối theo ca. Dùng nhiều kỳ khi đã duyệt được, không mở rộng đủ mọi công ty trước khi có một luồng hoàn chỉnh.
4. **Sau core:** chọn B hoặc DuPont theo ca. Nếu chọn làm trong 10 tuần, cần trao đổi tradeoff với UC-F04 có điều kiện tuần 9 hoặc phần mở rộng khác; chưa tự thay lịch/195 giờ.
5. **Sau project:** quý/TTM, mảng kinh doanh, giá/yield, danh mục và định giá tùy mục tiêu. Chưa cần ML để thực hiện những chức năng phân tích ở trên.

**Tác động SRS:** A ảnh hưởng F01.2/F02.2 và metrics/DR/TC; B làm sâu F02.3 và thêm nghĩa vụ beyond FR27; U/F03.3 làm rõ IR/FR32 và ca tương tác nếu được chọn. Chưa cấp ID yêu cầu mới, không đổi 91 yêu cầu/51 TC hiện hành hoặc manifest sáu trường. [Sổ đề xuất](../research-investor-support/evidence/gap-review.json) ghi trạng thái `proposed_not_integrated`.

## 9. Kiểm “đủ hỗ trợ” bằng tác vụ sử dụng

Các tiêu chí dưới đây là **kế hoạch đánh giá**, chưa có kết quả. Tác vụ mở rộng chỉ nghiệm thu sau khi được chọn phạm vi.

| Tác vụ | Người dùng phải làm được | Cách kiểm |
|---|---|---|
| Đọc tình hình ba năm | Chọn mã/kỳ, nhận ra hướng LNST/CFO và ô thiếu | Đối chiếu bộ số chuẩn, không chỉ kiểm biểu đồ hiện ra |
| Giải thích một biến động | Từ năm CFO giảm, tìm dòng cầu nối và nguồn; phân biệt suy luận với dữ kiện | Bộ câu trả lời tham chiếu có source refs |
| Phân biệt quy mô/hiệu quả | So hai mã bằng mức, tỷ số và xu hướng; ghi giới hạn khác ngành | Kiểm scope/đơn vị/câu trả lời, không chấm mã nào “tốt hơn” |
| Đọc cổ tức đúng năm/basis | Xác định đợt/năm lợi nhuận, nhận ra dữ liệu basis chưa đủ; tính G02 khi hợp lệ | Ca đủ và ca bị chặn; không dùng lịch trả như tiền thực nhận |
| Lưu kết quả nghiên cứu | Lưu nhận xét/câu hỏi kèm bảng/nguồn, mở lại sau bản sửa | Giữ kết quả cũ, tạo phân tích mới có phiên bản rõ |
| Phân tích doanh thu/biên — nếu chọn A | Nhận ra doanh thu tăng nhưng biên/LNST giảm, kiểm nguồn và giới hạn phân rã | Ca kiểm có số giả định trước, số doanh nghiệp đã duyệt sau |
| Phân tích thanh khoản/nợ vay — nếu chọn B | Phân biệt nợ phải trả và nợ vay; đọc tỷ số đúng loại nghĩa vụ | Ca có dòng nợ vay/kỳ hạn rõ và ca thiếu |

Chỉ số nên đo: thời gian hoàn thành, câu trả lời đúng theo bằng chứng, lỗi nhầm kỳ/đơn vị/scope, tỷ lệ truy lại nguồn được và mở lại hồ sơ đúng bản. Đề xuất thử 3–5 người thuộc vai trò mục tiêu; so tác vụ tương đương bằng PDF/bảng tính và bằng hệ thống, đổi thứ tự dùng để hạn chế hiệu ứng học. Mẫu nhỏ chỉ giúp phát hiện vấn đề và kiểm giá trị sử dụng; không suy đã tăng lợi nhuận đầu tư.

## 10. Nội dung trao đổi ngắn với giảng viên

**Word:** nêu khoảng trống sáu chỉ tiêu → phân rã UC-F02/F05 theo câu hỏi người dùng → bảng dữ liệu/công sức gói lựa chọn → minh chứng code/demo đã chạy → tác vụ đánh giá và hạn chế. Hiện chỉ có nghiên cứu/thiết kế, chưa viết “đã triển khai” các gói mới.

**Slide:** một slide “demo hiện thể hiện đến đâu”, một slide “làm sâu UC-F02/F05”, một slide “dữ liệu và tác vụ kiểm chứng”. Dùng một ví dụ doanh thu–biên hoặc CFO–CAPEX–phân phối, không lặp toàn bộ tổng quan đề tài.

**Demo sau triển khai:** mã/kỳ → biểu đồ → chọn điểm/dòng → nguồn → so sánh → ghi nhận xét → lưu/mở lại. Màn hình duyệt chỉ xuất hiện khi giải thích nền dữ liệu; trọng tâm trình bày là tác vụ của người phân tích.
