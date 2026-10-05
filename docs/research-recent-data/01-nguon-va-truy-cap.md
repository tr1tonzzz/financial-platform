# Nguồn và khả năng truy cập dữ liệu 2025–2026

Kiểm tra ngày 03/10/2026. Mỗi trạng thái dưới đây chỉ mô tả thao tác thực hiện trong môi trường này. URL tải, SHA-256, kích thước, HTTP status, timestamp thu thập và kết quả PDF được lưu trong [download-evidence.json](download-evidence.json).

## 1. BCTC từ doanh nghiệp

| Nguồn chính thức | Danh mục local | File thực tải | Giới hạn đã thấy |
|---|---|---|---|
| [Hòa Phát](https://www.hoaphat.com.vn/quan-he-co-dong/bao-cao-tai-chinh) | HTTP 200 | FY2025, Q1/2026, H1/2026: 3 PDF | Phân biệt BCTC đầy đủ với bản kết quả kinh doanh; Q1 có text lỗi mã chữ |
| [Dược Hậu Giang](https://dhgpharma.com.vn/vi/bao-cao-tai-chinh) | HTTP 200 | Ba kỳ trên: 3 PDF | Ba file đều cần OCR trong phép thử text |
| [Vĩnh Hoàn](https://www.vinhhoan.com/investors-2/) | HTTP 200 | Ba kỳ, hai ngôn ngữ: 6 PDF | Không đếm bản EN thành quan sát khác; tiêu đề nhóm trên web không đủ xác định mức bảo đảm |
| [Vinamilk](https://www.vinamilk.com.vn/investor/reports/financial) | HTTP 200 | Q1 và H1/2026: 2 PDF | Trang đầu hiện năm 2026; chưa thử bộ chọn năm để tải FY2025; web reader từng báo 403 nhưng Python tải được |
| [REE](https://www.reecorp.com/danh-muc-bao-cao/bao-cao-tai-chinh/) | HTTP 200 | Chưa tải 3 PDF mới được phát hiện | Robots chặn `/*.pdf$`; đã loại các seed đó khỏi tự động tải |
| [FPT](https://fpt.com/vi/nha-dau-tu/thong-tin-cong-bo) | HTTP 200 | Chưa tải 3 PDF mới được phát hiện | Link hiện tại qua `/api/media/...`; robots chặn `/api/` |

Việc robots chặn là căn cứ lựa chọn đường thu thập tự động của project, không phải kết luận pháp lý về việc đọc tài liệu bằng mọi cách. Nguồn thay thế chính thức hoặc tài liệu do người dùng cung cấp là phương án cần kiểm tra riêng cho REE/FPT; chưa tuyên bố đã hoàn thành.

Một URL báo cáo thường niên FPT được tìm thấy trước đó trả 404. Không sinh URL của kỳ mới bằng cách thay năm trong URL cũ. Mỗi lần phát hiện phải đi từ danh mục thực tế và lưu context của anchor, vì tên link đôi khi trống.

## 2. Thời điểm công bố khác kỳ tài chính

| Báo cáo | Ngày trên danh mục đã đọc | Ý nghĩa |
|---|---|---|
| HPG FY2025 | 27/03/2026 | Kết thúc kỳ 31/12/2025 không đồng nghĩa có thể dùng số liệu từ ngày đó |
| HPG Q1/2026 | 29/04/2026 | Dùng ngày công bố để dựng lịch thông tin |
| HPG H1/2026 | 28/08/2026 | Báo cáo soát xét sáu tháng |
| DHG FY2025 | 21/03/2026 | Báo cáo kiểm toán ký 12/03/2026; ngày ký và ngày công bố khác nhau |
| DHG Q1/2026 / H1/2026 | 20/04/2026 / 14/08/2026 | Ghi hai tài liệu độc lập, không thay thế âm thầm |
| VNM Q1/2026 / H1/2026 | 29/04/2026 / 30/07/2026 | Q1 cũng có soát xét; không mặc định mọi quý đều chưa soát xét |

Nguồn ngày là trang danh mục/chi tiết đã lưu trong raw evidence, không suy từ thư mục `/2026/03/` hoặc tên file. Các ngày này là mốc công bố **quan sát được ở nguồn đang đọc**; chưa chứng minh đó là lần công bố sớm nhất trên tất cả kênh. Khi backtest, cần đối chiếu công bố sở giao dịch và lịch phiên bản; nếu chỉ biết ngày, dùng quy ước thận trọng đã định nghĩa và không bịa giờ.

## 3. HNX: thử đường tải có xác thực TLS

[Trang công bố VHE năm 2025 trên HNX](https://www.hnx.vn/vi-vn/m-niem-yet/tin-tuc/Bao%20cao%20tai%20chinh%20nam%202025-603961-1.html) bị lỗi `CERTIFICATE_VERIFY_FAILED` khi Python dùng trust store của môi trường. `curl.exe` của Windows dùng Schannel tải trang thành công, rồi tải [tệp hợp nhất đính kèm](https://owa.hnx.vn/ftp///cims/2026/3_W4/000000016025637_VI_BaoCaoTaiChinh_Nam_2025_BaoCaoHopNhat.pdf) thành công: HTTP 200, 6.308.475 bytes, 35 trang có text, `ssl_verify_result=0`.

Không dùng `-k` hay tắt kiểm tra TLS. SHA-256 của PDF: `ca7e028eb6c6e9224fa61b0f678459776079ec40efd59ec4059df69e65afa064`. Thời gian tải quan sát 1,224 giây. Chỉ ghi ngày thu thập vì lần curl này không lưu timestamp chính xác; không tự bổ sung giờ vào bằng chứng.

Kết quả chứng minh một đường tải HNX hoạt động, chưa chứng minh crawl phân trang, toàn bộ kỳ hoặc mọi công ty. HOSE chưa được thử tải trong khảo sát này. Việc Schannel và Python khác kết quả là vấn đề cần kiểm tra trust store/chứng chỉ riêng; không đủ dữ kiện quy nguyên nhân hoàn toàn cho website. [Tài liệu curl về CA và native certificate store](https://curl.se/docs/sslcerts.html).

## 4. VSDC: tìm và tải thông báo cổ tức

Host **`vsdc.vn`** tải được bằng Python với xác thực TLS. Kết quả này bổ sung cho khảo sát trước gặp lỗi ở `vsd.vn`; không xóa hoặc đổi kết quả lịch sử của phép thử cũ.

[Lịch thực hiện quyền ngày 12/05/2026](https://vsdc.vn/vi/lich-giao-dich?date=12%2F05%2F2026&tab=LICH_THQ) trả HTTP 200. Từ anchor có thật `/ad/195056`, probe tải được thông báo DHG. Như vậy đã kiểm tra cả phát hiện link từ danh mục và tải trang chi tiết, không chỉ tìm thủ công bằng công cụ search. Trang đầu chỉ hiển thị 10/38 bản ghi; phân trang và phủ ngày chưa được triển khai. Lịch gồm cổ tức cổ phiếu, trái phiếu và sự kiện khác nên phải lọc nghiệp vụ.

Đã lưu bốn thông báo: [VNM 197038](https://vsdc.vn/vi/ad1/197038), [VNM 187729](https://vsdc.vn/vi/ad1/187729), [DHG 199544](https://vsdc.vn/vi/ad1/199544), [DHG 195056](https://vsdc.vn/vi/ad1/195056). Nội dung và mốc thời gian được trình bày ở [tài liệu tài chính](03-ky-tai-chinh-co-tuc-va-nhan.md).

## 5. Các trạng thái truy cập phải giữ riêng

- REE/FPT: `skipped_by_robots`, không phải PDF tải lỗi.
- Một số host CDN trả 403 cho robots; VSDC trả HTML website ở `/robots.txt`, không phải robots hợp lệ. Ghi `robots_unknown`, không suy đó là cho phép hay cấm toàn bộ. Khi triển khai crawler định kỳ cần xác định chính sách truy cập phù hợp trước khi tăng phạm vi.
- Python lỗi TLS trên HNX; curl có xác thực tải thành công: lưu cả lỗi và transport thành công.
- HTTP 200 với HTML không phải bằng chứng tải PDF; kiểm tra magic bytes và mở bằng PDF parser. Số liệu tài chính chỉ được ghi nhận sau đối chiếu, không lấy nhãn match làm giá trị đã kiểm chứng.

Đây là mẫu thuận tiện, chọn từ nguồn đã biết; không phải lấy mẫu ngẫu nhiên để ước lượng tỷ lệ thành công của thị trường.
