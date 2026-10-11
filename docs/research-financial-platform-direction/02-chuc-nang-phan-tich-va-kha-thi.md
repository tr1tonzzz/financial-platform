# Các chức năng phân tích: làm được gì, cần dữ liệu gì, có khả thi không?

Ngày 11/10/2026. Tất cả ví dụ A/B và số tiền trong tài liệu này là **giả định**. A01–A08 là mã ý tưởng nghiên cứu, không phải mã FR mới hoặc UC đã nghiệm thu.

## 1. Cấu trúc hiện hành

Theo yêu cầu mới nhất ngày 11/10/2026, A04 đã bị loại; các mã A còn lại dưới đây là năng lực phân rã tham khảo, không phải danh mục UC lớn hiện hành. [Yêu cầu chức năng v2.0](../research-platform/27-yeu-cau-chuc-nang-va-vi-du.md) gom thành khai thác dữ liệu, phân tích, so sánh, theo dõi và cổ tức; thêm danh mục/kịch bản là hướng mở rộng. [SRS v3.3/mục18](../research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md) rút FR29/FR30/D09/D10. [Nghiên cứu36 repo](../research-high-star-finance/README.md) và [khả thi mới](../research-high-star-finance/03-kha-thi-va-thu-tu-thuc-hien.md) thay thứ tự đề nghị trước.

## 2. A01 — Khám phá và lấy dữ liệu tài chính

**Giải quyết:** người dùng muốn lấy một bộ số liệu để nghiên cứu mà không lần lượt mở báo cáo từng công ty.

**Người dùng làm được:** chọn doanh nghiệp, năm, phạm vi và chỉ tiêu; xem bảng theo công ty/kỳ; đọc định nghĩa và đơn vị; nhận biết số còn thiếu/chưa duyệt; chuyển lựa chọn sang biểu đồ hoặc xuất dữ liệu.

**Ví dụ:** chọn A và B, ba năm 2023–2025, hai chỉ tiêu LNST/CFO. Hệ thống trả sáu hàng công ty–năm và hai cột chỉ tiêu; CFO B năm 2024 còn thiếu thì ô để trống có lý do. Người dùng xuất bộ dữ liệu đang chọn kèm thông tin nguồn.

- **Đầu vào:** facts đã duyệt; danh mục công ty/chỉ tiêu; kỳ, phạm vi, đơn vị, phiên bản, nguồn, trạng thái dữ liệu.
- **Xử lý:** truy vấn cùng bộ điều kiện → chuyển thành bảng → giữ các ô thiếu và đường tới nguồn → xuất cùng bộ chọn và bản dữ liệu.
- **Đầu ra:** bộ dữ liệu dùng được cho phân tích, thay vì chỉ danh sách tài liệu.
- **Khả thi:** cao với sáu trường hiện có, chưa cần nguồn giá hoặc API trả phí. Cần xây lớp truy vấn và giao diện; nguồn dữ liệu đủ ba năm chưa hoàn thiện.
- **Đối chiếu:** FR01–FR18 tạo dữ liệu; FR32 có tra cứu; FR34 có CSV/JSON snapshot. Chọn nhiều công ty/chỉ tiêu và xuất đúng bảng đang xem cần đặc tả thêm; vẫn phải giữ khả năng kiểm lại snapshot.

**Một lát cắt hoàn chỉnh:** chọn A/B → hiện cả hàng bị thiếu → chọn CFO A 2025 → xem nguồn → xuất bảng đúng điều kiện. Nếu chỉ tải được một CSV không rõ kỳ/nguồn thì chưa đạt.

**Bài học nguồn:** [EdgarTools truy vấn facts](https://github.com/dgunning/edgartools/blob/246010946cdbe588b0397643fb1598a04fe0cad6/edgar/entity/query.py#L148), [FinanceDatabase chọn tập dữ liệu](https://github.com/JerBouma/FinanceDatabase/blob/5583c4ef5d51fa404a65aa4685da60aca69b7538/financedatabase/query_model.py#L76). Áp dụng mô hình truy vấn; không giả định các thư viện này đã cung cấp BCTC Việt Nam.

## 3. A02 — Theo dõi tình hình tài chính bằng biểu đồ

**Giải quyết:** bảng số nhiều kỳ khiến người dùng khó nhìn ra xu hướng hoặc phải tự vẽ lại trong Excel.

**Người dùng làm được:** đổi doanh nghiệp/giai đoạn; bật/tắt chuỗi; xem số và biến động khi chọn năm; chuyển bảng↔biểu đồ; xem chi tiết của điểm đang chọn. Các vùng hiển thị dùng cùng bộ lọc.

| Góc nhìn | Dùng để nhận ra điều gì? | Cần dữ liệu nào? |
|---|---|---|
| Đường/cột LNST và CFO theo năm | Lợi nhuận và tiền kinh doanh có cùng chiều không? | LNST/CFO đã duyệt cùng phạm vi |
| Đường CFO/LNST | Tiền kinh doanh so với lợi nhuận thay đổi thế nào? | Hai số cùng kỳ; chỉ tính khi LNST>0 |
| Cột tỷ trọng tiền/tài sản và nợ phải trả/tài sản | Cơ cấu tài chính thay đổi ở hai khía cạnh đang quan sát | Tiền, tài sản, nợ phải trả tại cùng ngày/phạm vi |
| DPS theo năm và dòng thời gian sự kiện | Mức công bố và sự kiện quyền thay đổi thế nào? | Thông báo, độ đầy đủ, cơ sở cổ phiếu; năm lợi nhuận tách lịch thanh toán |

Hai tỷ trọng tiền/nợ phải trả không phải các phần cộng lại thành một cơ cấu 100%; trình bày thành các chỉ tiêu riêng. Tổng nợ phải trả không đồng nghĩa nợ vay. DPS dùng đơn vị đồng/cổ phiếu riêng với các biểu đồ tiền của doanh nghiệp.

**Ví dụ:** A có LNST 90→100 tỷ, CFO 130→80 tỷ. Người dùng nhìn thấy hai chuỗi khác chiều, chọn năm cuối, xem CFO/LNST=0,8 và tra cứu số 80 tỷ. Đây là điểm bắt đầu tìm hiểu, chưa giải thích nguyên nhân giảm tiền.

- **Khả thi:** cao về trực quan hóa với dữ liệu lõi; tương tác chọn điểm và giữ đồng bộ cần triển khai. Ba năm đủ minh họa thay đổi, chưa là lịch sử dài.
- **Đối chiếu:** FR25–FR28/FR32 đã yêu cầu các phân tích và biểu đồ. Đồng bộ lựa chọn, bảng↔biểu đồ và chọn điểm cần làm rõ thêm. Biểu đồ giá chứng khoán chưa có nguồn trong MVP.
- **Lát cắt hoàn chỉnh:** chọn A → nhận ra năm LNST/CFO khác chiều → chọn năm đó → xem bảng/nguồn cùng năm → lưu lựa chọn. Đổi sang B phải cập nhật toàn bộ vùng hiển thị.

**Bài học nguồn:** [mã dựng biểu đồ tài chính Fincept](https://github.com/Fincept-Corporation/FinceptTerminal/blob/3f444cb7ab712d85a57d270d5edd6e7a2ef50d55/fincept-qt/src/screens/equity_research/EquityFinancialsTab_Populate.cpp#L324); [OpenBB tương tác dữ liệu](https://docs.openbb.co/workspace/analysts/widgets/interacting-with-data) mô tả bộ lọc liên kết và chuyển bảng/biểu đồ. Học cách tương tác, không sao chép cả terminal.

## 4. A03 — So sánh doanh nghiệp

**Giải quyết:** một số liệu của A khó có ý nghĩa nếu thiếu cơ sở đối chiếu; số tiền lớn có thể chỉ phản ánh doanh nghiệp lớn.

**Người dùng làm được:** chọn 2–3 doanh nghiệp, kỳ và chỉ tiêu; xem bảng song song, đường/cột so sánh; chuyển số tuyệt đối↔tỷ số phù hợp; xem chỗ không tương thích hoặc còn thiếu.

**Ví dụ:** cùng năm và cùng loại phạm vi, A có CFO 80 và LNST 100 tỷ; B có CFO 60 và LNST 50 tỷ. A tạo ra số tiền CFO lớn hơn; B có CFO/LNST 1,2 so với A 0,8. Người dùng biết sự khác biệt để kiểm tra tiếp, không tự suy B tốt hơn toàn diện.

- **Dữ liệu:** dùng được CFO/LNST, tiền/tài sản, nợ phải trả/tài sản từ sáu trường; kèm phương pháp và trạng thái. Nếu so DPS cần kiểm năm/coverage/basis của từng chuỗi.
- **Cách thực hiện:** một bảng so sánh và 1–2 biểu đồ dùng chung dữ liệu; nhãn đầy đủ; cho người dùng chọn nhóm. Không cần bộ chọn tự động “đối thủ cạnh tranh” ở đợt đầu.
- **Khả thi:** cao cho so sánh nhóm do người dùng chọn. Benchmark ngành có độ khó lớn hơn vì cần danh mục ngành đáng tin và đủ doanh nghiệp tương đồng.
- **Đối chiếu:** dữ liệu/tỷ số/biểu đồ đã có FR25–FR32, nhưng màn hình so sánh nhiều doanh nghiệp là bổ sung chưa được chốt; liên quan G04 trong nghiên cứu trước. Nên nâng ưu tiên để làm rõ giá trị phân tích.

**Điều kiện:** cùng kỳ, loại dữ liệu và phạm vi theo chính sách so sánh; nếu một bên riêng lẻ, một bên hợp nhất thì phải giải quyết tương thích trước khi ghép vào nhóm phân tích chung. Không gán “bình quân ngành” cho ba doanh nghiệp pilot khác ngành. Chuẩn hóa về năm gốc chỉ dùng khi cơ sở hợp lệ; không che dấu nền bằng 0 hoặc âm.

**Lát cắt hoàn chỉnh:** chọn A/B và chỉ tiêu → xem hai góc nhìn tuyệt đối/tỷ số → chỉ ra khác biệt → xem cơ sở tính của một ô → lưu nhóm so sánh.

**Bài học nguồn:** [Fincept Peers](https://github.com/Fincept-Corporation/FinceptTerminal/blob/3f444cb7ab712d85a57d270d5edd6e7a2ef50d55/fincept-qt/src/screens/equity_research/EquityPeersTab.cpp#L143), [FinanceToolkit dữ liệu tự cung cấp](https://github.com/JerBouma/FinanceToolkit/blob/37ed6f01465b4bfb6718b07e1d65826734f53337/financetoolkit/toolkit_controller.py#L105), [finagg nhóm ngành](https://github.com/theOGognf/finagg/blob/614631d8e26bdbb21c1a6e6a3a10972a00e1d24b/src/finagg/sec/feat/_refined/annual.py#L42).

## 5. A05 — Phân tích các khoản tạo ra chênh lệch tiền

**Giải quyết:** biết CFO giảm hoặc số dư âm vẫn chưa biết cần đọc khoản nào trong báo cáo.

**Người dùng làm được:** xem các khoản điều chỉnh từ lợi nhuận trước thuế đến CFO; chọn khoản lớn để xem nguồn; xem phần chênh lệch chưa giải thích; tiếp tục xem tiền sau chi đầu tư và phân phối.

**Ví dụ:** CFO giảm 50 tỷ giữa hai năm. Khi các dòng nguồn đủ và tương thích, hệ thống chỉ ra khoản biến động phải thu đóng góp −40 tỷ vào chênh lệch, các khoản khác tổng −10 tỷ. Người dùng biết ưu tiên đọc thuyết minh phải thu. Đóng góp theo dòng kế toán chưa tự chứng minh khách mất khả năng trả nợ.

- **Đầu vào:** lợi nhuận trước thuế, dòng điều chỉnh phi tiền, vốn lưu động và các dòng khác theo BCTC; CFO; CAPEX và khoản thực chi khi chọn G02. Sáu trường lõi tự chúng chưa đủ dựng cầu nối đầy đủ.
- **Xử lý:** mapping có duyệt → cộng theo dấu dòng nguồn → đối chiếu CFO → trình bày phần giải thích và residual; chỉ so đóng góp hai năm khi mapping/kỳ tương thích.
- **Đầu ra:** bảng phân rã hoặc waterfall, những dòng cần đọc tiếp và nguồn của từng dòng; sau đó là CFO−CAPEX−khoản thực chi.
- **Khả thi:** vừa cho 1–3 ca có duyệt thủ công hỗ trợ; thấp hơn nếu yêu cầu tự động bao phủ mọi mẫu báo cáo. Khó chính ở xác định đúng dòng, không phải vẽ waterfall.
- **Đối chiếu:** E01–E10 và G02/D01–D04 đã nghiên cứu. So cặp năm E05, thực chi E10 phụ thuộc gate tương ứng; không mặc định toàn bộ ca đã đủ điều kiện. Thiết kế waterfall/đi từ biến động đến dòng nguồn cần cụ thể thêm.

**Lát cắt hoàn chỉnh:** nhận ra CFO giảm ở A02 → mở cầu nối của A → biết dòng đóng góp lớn và phần chưa giải thích → xem trang nguồn → ghi câu hỏi. Cầu nối bắt đầu ở lợi nhuận trước thuế; không dùng LNST thay thế âm thầm.

[Nghiên cứu cầu nối hiện có](../research-profit-cash-dividend/README.md); [G02 và ca DHG](../research-dividend-functions/02-g02-bao-phu-tien-mat.md). Ca DHG kiểm số dư sau khoản chi, chưa là minh chứng đã dựng đủ cầu nối hoặc phân rã nguyên nhân hai năm.

## 6. A06 — Phân tích lịch sử cổ tức và sự kiện liên quan

**Giải quyết:** người dùng dễ đọc nhầm năm trả thành năm lợi nhuận, cộng trùng thông báo hoặc so DPS trên cơ sở cổ phiếu khác nhau.

**Người dùng làm được:** xem biểu đồ DPS theo năm lợi nhuận; dòng thời gian các đợt quyền; chọn sự kiện để xem điều chỉnh/hủy/thay thế; nhận lý do chưa so sánh được; xem DPS gốc và cơ sở tham chiếu khi đủ bằng chứng.

**Ví dụ:** đợt thanh toán tháng 6/2026 ghi trả phần còn lại của lợi nhuận 2025. Nó nằm ở năm 2025 trên biểu đồ lịch sử, đồng thời có mốc tháng 6/2026 trên lịch thanh toán. Người dùng thấy cả hai nghĩa mà không cộng vào sai năm.

- **Dữ liệu:** notices/components, vòng đời, năm lợi nhuận, lịch quyền, coverage và ledger sự kiện cổ phiếu.
- **Khả thi:** vừa; timeline dễ dựng khi dữ liệu chuẩn, độ đầy đủ và quan hệ giữa các thông báo mới là phần khó. G03 có prototype phép tính, chưa đủ chuỗi sự kiện cho mọi công ty.
- **Đối chiếu:** FR19–FR24/FR28/FR32, G03/D05–D08. Đặt sự kiện cạnh biểu đồ tài chính là đề xuất tương tác, không là bằng chứng sự kiện gây ra biến động tài chính.

**Lát cắt hoàn chỉnh:** chọn năm lịch sử → xem các đợt cấu thành → biết có đủ cơ sở tổng hợp không → chọn sự kiện cổ phiếu → hiểu điều kiện so sánh DPS.

Lịch công bố/ngày đăng ký/lịch thanh toán không chứng minh tiền đã về tài khoản. Hỗ trợ lịch thu nhập theo vị thế và đối soát thực nhận cần dữ liệu vị thế, điều kiện đủ quyền và thanh toán; tách thành giai đoạn khác.

## 7. A07 — Theo dõi doanh nghiệp và thay đổi dữ liệu

**Giải quyết:** người dùng đã phân tích rồi nhưng không biết bản dữ liệu mới làm nhận xét cũ cần xem lại ở đâu.

**Người dùng làm được:** lưu danh sách doanh nghiệp quan tâm; xem thay đổi đã duyệt; mở bản trước/sau; biết biểu đồ/phép tính đã lưu nào sử dụng số bị sửa. Cảnh báo trong ứng dụng trước; không cần email hoặc thông báo bên ngoài.

**Ví dụ:** CFO A đổi từ 120 thành 125 tỷ sau duyệt bản mới. Hệ thống hiển thị thay đổi và phép tính số dư sau khoản chi đổi −20→−15 tỷ; nhận xét cũ vẫn giữ bản nguồn cũ. Người dùng tự quyết định cập nhật nhận xét.

- **Dữ liệu:** phiên bản fact/event đã duyệt, thời điểm ghi nhận, danh sách theo dõi, liên kết operands→kết quả đã lưu.
- **Xử lý:** so phiên bản → phân biệt chỉ đổi tệp với đổi giá trị/kỳ/phạm vi → tìm các kết quả phụ thuộc → trình bày trước/sau.
- **Khả thi:** vừa cho danh sách và bảng thay đổi; khó hơn cho xác định ảnh hưởng tự động đến nhiều kết quả. Làm sau A08 và lớp phiên bản.
- **Đối chiếu:** nền đã có phiên bản và snapshot; feed theo dõi/ảnh hưởng là phần mới, liên quan G07 và nhánh đối chiếu phiên bản đã nghiên cứu. FR35 bảo toàn lần phân tích cũ; không phải chức năng cảnh báo tự động đã có.

**Lát cắt hoàn chỉnh:** theo dõi A → duyệt sửa một fact → xem thay đổi → mở kết quả phụ thuộc → giữ được bản phân tích trước. Ngày hệ thống quan sát dữ liệu không mặc định là ngày nguồn công bố.

**Bài học nguồn:** [Fincept Watchlist](https://github.com/Fincept-Corporation/FinceptTerminal/blob/3f444cb7ab712d85a57d270d5edd6e7a2ef50d55/fincept-qt/src/screens/watchlist/WatchlistScreen.cpp#L571) chứng minh cấu trúc danh sách theo dõi; ý tưởng theo dõi ảnh hưởng của BCTC là chuyển thể của nghiên cứu này, không được coi là chức năng đã tìm thấy nguyên vẹn trong file đó.

## 8. A08 — Lưu và tiếp tục một lần phân tích

**Giải quyết:** hôm sau người dùng muốn xem tiếp cùng nhóm công ty, bảng, biểu đồ và câu hỏi đã ghi.

**Người dùng làm được:** lưu tập công ty, giai đoạn, chỉ tiêu, bộ lọc, dạng hiển thị và ghi chú; mở lại lần phân tích; xuất dữ liệu/bằng chứng; chủ động tạo bản mới khi muốn dùng dữ liệu cập nhật.

**Ví dụ:** lưu “A/B — lợi nhuận và CFO 2023–2025”. Mở chế độ bản đã chốt thì thấy đúng số cũ. Chọn “tạo bản với dữ liệu hiện hành” thì hệ thống lập lần phân tích mới, chỉ rõ dữ liệu khác ở đâu.

- **Dữ liệu:** bộ chọn giao diện, snapshot, phiên bản công thức, ghi chú và đường nguồn.
- **Khả thi:** cao cho cấu hình một bố cục cố định; vừa cho phục hồi/kiểm tra toàn vẹn. Kéo thả tự thiết kế dashboard chưa cần để giải quyết nhu cầu này.
- **Đối chiếu:** FR34/35, D11–D12 có snapshot/bối cảnh/hồ sơ; lưu cấu hình góc nhìn và chọn chế độ bản cũ/hiện hành cần đặc tả thêm. Hồ sơ thẩm định là một mẫu phân tích trên năng lực này.

**Lát cắt hoàn chỉnh:** lưu sau A03 → đóng/mở lại → nhận đúng công ty/kỳ/điều kiện/số đã chốt → xem nguồn → lập bản mới có chủ đích. Chỉ lưu một đoạn ghi chú chưa đủ cho chức năng này.

## 9. Cần thêm nhóm dữ liệu nào để phân tích sâu hơn?

Ưu tiên năng lực A01–A03 trước, sau đó chọn mở rộng theo câu hỏi. Các nhóm dưới đây **chưa thuộc sáu trường lõi**.

| Câu hỏi cần giải quyết | Chức năng bổ sung có ích | Dữ liệu phải thêm | Ưu tiên đề xuất |
|---|---|---|---|
| Lợi nhuận tăng nhờ bán nhiều hơn hay biên lợi nhuận đổi? | Xem doanh thu và biên lợi nhuận ròng theo năm; nếu có đủ dòng thì thêm biên gộp | Doanh thu; LNST đã có; lợi nhuận gộp hoặc doanh thu/giá vốn tương thích | Nhóm dữ liệu kế tiếp sau lát cắt phân tích lõi |
| Tiền bị giữ ở phải thu/hàng tồn kho như thế nào? | Đọc cơ cấu vốn lưu động, phân rã đóng góp vào CFO | Dòng điều chỉnh CFO và/hoặc phải thu, tồn kho, phải trả; định nghĩa phạm vi | Ưu tiên ca cầu nối đã chọn |
| Doanh nghiệp có sức ép thanh toán ngắn hạn không? | Xem tài sản/nợ ngắn hạn, cấu trúc nợ vay và lịch đáo hạn khi có | Tài sản ngắn hạn, nợ ngắn hạn, nợ vay, kỳ hạn; thêm điều kiện cho từng tỷ số | Sau khi nguồn dữ liệu này được kiểm chứng |
| Mức cổ tức đang xét thay đổi thế nào nếu CFO/khoản chi khác đi? | Kịch bản giả định CFO−CAPEX−phân phối với các giá trị người dùng đặt | Dữ liệu G02 + giả định và bản gốc tách riêng | Tùy chọn sau G02; không phải dự báo |

Không tính biên lợi nhuận khi chưa có doanh thu. Chỉ có tổng nợ phải trả/tài sản chưa trả lời được thanh khoản ngắn hạn hay kỳ hạn nợ. ROE/DuPont/vòng quay cần đúng định nghĩa tử số và số dư bình quân, đủ các dòng nguồn; không thêm chỉ vì toolkit có sẵn công thức.

API/SDK cho người dùng khác xây công cụ trên dữ liệu là hướng mở rộng hợp lý của nền tảng. MVP có truy vấn và xuất bộ dữ liệu để dùng lại đã tạo nền; chưa cần xây API công khai để chứng minh giá trị ban đầu.

## 10. Thứ tự triển khai và kiểm chứng giá trị sử dụng

### Lát cắt đầu tiên: người dùng khai thác dữ liệu và phát hiện khác biệt

Chọn A/B, ba năm, một phạm vi tương thích → xem bảng chất lượng → xem LNST/CFO → so sánh tỷ số → chọn điểm để xem số/nguồn → lưu lần phân tích.

Chỉ cần một trang phân tích với bộ chọn chung, bảng dữ liệu, hai vùng biểu đồ và vùng chi tiết. Hai doanh nghiệp đủ cho so sánh; ba doanh nghiệp dùng thử bảng đối chiếu. UI đơn giản nhưng tác vụ phải hoàn chỉnh.

### Lát cắt tiếp: đi từ chênh lệch tới câu hỏi cổ tức

Từ năm CFO giảm → xem cầu nối có duyệt → kiểm khoản chi G02 → đọc lịch cổ tức/G03 → ghi câu hỏi và bằng chứng D11–D12/A08. Tái sử dụng prototype đã có; tiếp tục hoàn thiện nền thu/duyệt cho các đầu vào mở rộng.

### Lát cắt sau: dùng lại và theo dõi

Mở bản phân tích trước → có một sửa đổi đã duyệt → so trước/sau → chỉ ra kết quả phụ thuộc → tạo lần phân tích mới. A07 không nên làm trước khi nguồn/phiên bản/lần phân tích đã lưu ổn định.

### Kiểm chứng theo tác vụ, không theo số biểu đồ

| Tác vụ thử với người dùng | Điều cần quan sát | Tiêu chí để đánh giá |
|---|---|---|
| Đọc xu hướng LNST/CFO của doanh nghiệp đã chọn | Nhận diện đúng xu hướng/kỳ và số thiếu | Đối chiếu với dữ liệu đã duyệt; đo thời gian/lỗi so với đọc bảng nguồn |
| So sánh A/B cùng năm | Biết phân biệt số tuyệt đối/tỷ số và cơ sở so sánh | Ghi câu trả lời, lỗi trộn kỳ/phạm vi và số bước thao tác |
| Đi từ kết quả đến bằng chứng | Tìm đúng operands và trang nguồn | Tỷ lệ hoàn thành, phút tìm, lỗi nguồn/đơn vị |
| Tiếp tục phân tích sau cập nhật | Biết bản đã lưu khác dữ liệu mới ở đâu | Mở lại đúng bản, phát hiện đúng sửa đổi, không ghi đè nhận xét cũ |

Đây là protocol đề xuất, chưa phải kết quả thực nghiệm. Cơ sở nhu cầu hiện tại là quy trình phân tích nghề nghiệp, chức năng của các dự án nguồn và góp ý của người thực hiện; chưa có phỏng vấn người dùng độc lập xác nhận mức độ cần từng ý tưởng. Không dùng việc có biểu đồ làm bằng chứng cải thiện lợi nhuận đầu tư.

## 11. Tóm tắt thay đổi so với các tài liệu trước

| Nội dung | Cách xử lý đề xuất |
|---|---|
| Thu thập/chuẩn hóa/duyệt | Giữ nền dữ liệu; trình bày là UC phân rã hỗ trợ khai thác |
| Biểu đồ/xu hướng | Đã có yêu cầu nền; cụ thể hóa tác vụ và tương tác |
| G02/G03 và lưu hồ sơ D11/D12 | Kế thừa phân tích sâu/lịch sử/lưu; G01 screening đã rút |
| So sánh nhiều doanh nghiệp | Nâng ưu tiên nghiên cứu và đề nghị vào lát cắt phân tích đầu |
| Danh sách theo dõi/ảnh hưởng | Đề xuất giai đoạn sau, phụ thuộc nguồn/phiên bản/lần phân tích |
| Dữ liệu bổ sung | Chọn theo câu hỏi; không tự tăng scope cho mọi công ty |
| SRS, tiến độ và ngân sách | CR-AN-03 rút4 yêu cầu/3 TC; lịch/giờ cũ là baseline, phần mới cần chọn và dự toán |

[Bằng chứng nguồn](01-bang-chung-va-bai-hoc.md) · [Kết luận hướng sản phẩm](README.md) · [Yêu cầu chức năng giải thích đơn giản](../research-platform/27-yeu-cau-chuc-nang-va-vi-du.md).
