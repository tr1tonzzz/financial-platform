# Phương pháp thu thập và xử lý dữ liệu đã thống nhất

## Thu thập dòng cầu nối cho ca chọn

SRS v3.1 thêm dòng BCLCTT/LNTT cho tối thiểu một ca trong pilot. Lưu toàn bảng/context và locator từng dòng, role leaf/subtotal/total, dấu, đơn vị, scope, cột năm và report version trước duyệt. Ưu tiên phương pháp gián tiếp; trực tiếp/unknown không tự chuyển thành cầu nối giả. Nhập tay là fallback có ghi phút và nhãn assisted cho cầu nối, không thay discovery BCTC/thông báo. Sáu targets toàn mẫu vẫn giữ. [Quy tắc chi tiết](../research-profit-cash-dividend/04-nguon-chuan-hoa-va-chat-luong.md).

Phiên bản 2.0 ngày 03/10/2026. Áp dụng cho project lợi nhuận–dòng tiền–cổ tức tiền mặt. Đây là phương pháp triển khai; không mô tả mọi module như đã hoàn thành.

## 1 Quyết định công nghệ và nguồn

Python 3.12, HTTP + lxml cho discovery, downloader chung, pdfplumber/pypdf cho text và metadata, render + Tesseract vie/eng cho scan, SQLite cho dữ liệu và Streamlit cho ứng dụng. Pin thư viện sau smoke test, tái sử dụng prototype đã kiểm chứng. Chưa cần Scrapy/Playwright nếu HTML đã có dữ liệu; dùng browser chỉ cho control năm/trang công khai thực sự cần, sau kiểm tra policy.

| Loại dữ liệu | Nguồn chính | Nguồn đối chiếu/fallback |
|---|---|---|
| BCTC | Trang IR chính thức của doanh nghiệp | Công bố sở khi adapter đã kiểm tra; file nhập giữ URL/provenance |
| Cổ tức tiền mặt | VSDC thông báo quyền và sửa/hủy | IR, nghị quyết ĐHĐCĐ/HĐQT và thông báo liên quan |
| Corporate actions | VSDC/IR có nguồn và ngày hiệu lực | Review tay nếu chưa tự đọc được |
| Dữ liệu số bên thứ ba | Không là nguồn gốc MVP | Chỉ đối chiếu nếu điều kiện truy cập/dữ liệu phù hợp |

Không dùng dataset có sẵn làm nguồn demo chính. Seed gồm issuer, ticker/ISIN nếu có, URL danh mục hoặc truy vấn công khai; URL từng tài liệu phát hiện và đường discovery phải lưu. Nhập trực tiếp URL để sửa thiếu được gắn assisted/manual, không đếm như discovery tự động.

## 2 Chọn mẫu và expected ledger

Pilot 3 công ty × 2023–2025; VNM/DHG là ứng viên vì đã có thông báo mẫu, công ty thứ ba chọn sau kiểm tra nguồn/scope/lịch sử. Chưa xác nhận chín BCTC đủ. Mỗi issuer có scope chính cho series; ghi lý do và ngành. Mục tiêu sau gate là 5–8 doanh nghiệp, 15–24 BCTC năm.

Ledger gồm expected issuer–year–scope, năm tài chính thật, nguồn cần rà, khoảng ngày công bố đã rà, pagination/filter, trạng thái found/downloaded/reviewed và lý do thiếu. Với cổ tức theo profit_year, rà từ các đợt tạm ứng trong năm đến các đợt còn lại năm sau **và các sửa đổi tới snapshot**, không giới hạn bằng năm thanh toán. Nếu nghị quyết/thông báo còn đợt chưa chốt, kéo dài kiểm tra và giữ partial.

Chọn doanh nghiệp có lịch sử tiền mặt thuận lợi cho pilot; báo selection bias, không suy kết quả cho mọi doanh nghiệp niêm yết hay mô hình có/không trả cổ tức.

## 3 Tự phát hiện tài liệu

BCTC: đọc HTML IR, theo phân trang đã quan sát có budget, lấy tên/context/ngày và link. Loại tổng quan, giải trình đứng riêng, CBTT đơn thuần; bundle có BCTC thật vẫn kiểm tra trang. Marker quý/bán niên trước marker năm; report year khác upload year. Xác nhận tên doanh nghiệp, khoảng kỳ, scope, assurance và unit bằng header PDF trước trích.

Cổ tức: phát hiện thông báo theo ticker/ISIN qua trang tìm kiếm/danh mục công khai VSDC hoặc IR, có bộ lọc thời gian và pagination. Chỉ theo luồng đã đọc được/được phép, không đoán endpoint nội bộ. Parser lấy **nội dung thông báo chính**, dừng trước tin cùng tổ chức/tin khác; không trích các link liên quan thành cùng một sự kiện. Lưu query/page/discovered_from để chứng minh discovery.

Adapter cổ tức chưa hoàn chỉnh. Gate tuần 2 thử một luồng tự phát hiện nhiều thông báo; nếu website khó, dùng adapter IR chính thức tương ứng và ghi coverage VSDC đối chiếu. Không giả lập full history từ bốn seed mẫu.

## 4 Tải và cập nhật raw

Kiểm tra source policy theo host; known Disallow thì skip, policy chưa xác định mặc định pending/skip trong collector thường xuyên. Research probe host file Hòa Phát trước có cờ hữu hạn và log unknown, không tự biến thành nguồn scheduler được Allow.

Một request/host đồng thời, delay ít nhất 1 giây và theo policy, timeout 20 giây, size cap 30 MiB, retry hữu hạn cho lỗi tạm thời. Giữ TLS verification; không theo host redirect chưa kiểm tra. Downloader lưu HTTP status/headers, catalog URL, retrieved/checked_at, SHA-256 và raw HTML/PDF. PDF phải qua magic check và mở được.

Kiểm tra lại catalog bằng mạng; file dùng ETag/Last-Modified conditional GET nếu hỗ trợ và cache local còn đúng hash. 304 giữ phiên bản, 200 hash giống không thêm bản, hash đổi giữ cũ/thêm mới và đưa metadata/facts cần review. HTML thông báo cũng giữ lịch sử bytes; template/sidebar thay đổi không tự là sửa nội dung sự kiện, cần diff main notice.

## 5 Trích dữ liệu

Financial: thử text/tọa độ trước, kiểm tra encoding/nhãn/cột; thiếu text thì render trang bảng chính và OCR. Tạo sáu candidate targets, kỳ hiện tại và số so sánh có vai trò rõ. Giữ raw label/value/unit, normalized VND integer/Decimal, PDF page/bbox, phương pháp và parser version.

Event: lấy issuer, ticker, notice ID/version, kind, published_at, record_date, scheduled_payment_date, DPS VND/cổ phiếu, par value, profit year và sửa/hủy. Một thông báo có nhiều năm được tách components; không nhân bản toàn event. Quy đổi phần trăm trên mệnh giá thành DPS chỉ khi có mệnh giá rõ. Không dùng tỷ lệ mệnh giá như yield.

## 6 Kiểm định và review

Financial: A−L−E với tolerance nguồn, đúng unit/period/scope, số ngoặc âm, nhãn LNST tổng và CFO đúng dòng. Cân đối đúng không xác nhận cột đúng. Event: ticker, ngày, DPS/components và tổng, âm/trống, năm không rõ, identity, amendments, corporate actions. Không gán 0 vì không thấy dữ liệu.

Review UI hiển thị trang/đoạn gốc và cờ lỗi. Trước/sau/lý do được ghi transaction với audit. Chỉ reviewed facts/events đi vào phân tích xuất bản; pending/missing có lý do riêng.

## 7 Ghép và xuất snapshot

Ghép issuer ID + fiscal/profit year được xác nhận. Chọn document version/scope theo policy snapshot, lấy active event components không trùng/hủy. Tổng hợp observed DPS cùng coverage status. Chỉ series đủ/comparable được tính biến động; raw khác basis phải chờ xử lý.

Dataset snapshot giữ document/fact/event version IDs, cutoff, config và review IDs. Timeline theo lịch công bố/chốt quyền/thanh toán hiển thị riêng bảng theo năm lợi nhuận. Phân tích chi tiết ở [quy tắc ghép](13-ghep-co-tuc-va-phan-tich.md).

## 8 Phần đã có và thứ tự triển khai

Đã có crawler BCTC FY2025/H1-2026 và 304, OCR sáu trường ở hai tài liệu development, bốn thông báo cổ tức mẫu. Chưa thu tự động đầy đủ 2023–2025, chưa có event discovery adapter, history SQLite hoặc UI review.

Thứ tự: một issuer end-to-end → adapter cổ tức + tách năm → pilot chín BCTC và ledger → SQLite/review → dashboard → mở rộng và holdout. Tự động hóa phát hiện/tải là lõi; xác nhận metadata/closure và sửa OCR có người review được chấp nhận nhưng phải đo công sức.

## 9 Thuật ngữ và đầu ra để người mới theo dõi

| Thuật ngữ | Hiểu và thực hiện |
|---|---|
| IR | Trang quan hệ cổ đông của doanh nghiệp, có danh mục công bố |
| Discovery/adapter | Tự tìm tài liệu từ danh mục; mỗi website có bộ đọc phù hợp |
| Raw/provenance | File gốc và bằng chứng URL, ngày tải, hash, trang/đoạn nguồn |
| Candidate/reviewed | Số máy đọc đang chờ kiểm tra / số đã xác nhận được đưa vào phân tích |
| Scope/series | Phạm vi báo cáo (hợp nhất/riêng/cấp doanh nghiệp) và chuỗi năm cùng định nghĩa |
| Component | Phần DPS thuộc một năm lợi nhuận trong một thông báo |
| Coverage ledger | Sổ ghi nguồn, trang và khoảng ngày đã rà, phần còn thiếu và căn cứ kết luận đủ |
| Snapshot/holdout | Bản dữ liệu chốt tại một mốc / tài liệu để đánh giá chưa dùng chỉnh parser |

Đầu ra dự kiến của một lần chạy: manifest nguồn và file gốc → JSON candidates cùng lỗi → facts/events đã duyệt trong SQLite → bảng năm và timeline trong snapshot → biểu đồ và CSV/JSON export. Một dòng phân tích phải lần được tới từng số BCTC và component cổ tức gốc. JSON trích xuất ban đầu không tự được xem là dataset cuối.

Ví dụ đọc bằng tay trước khi viết code: thông báo VNM 187729 có 2.850 đồng/cổ phiếu gồm 350 của 2024 và 2.500 của 2025. Tạo một event, hai components; sau đó đưa đúng phần vào đúng năm, kiểm tra còn thông báo khác hay không. Đọc [từ điển và ví dụ có nguồn](12-kien-thuc-tai-chinh-va-tu-dien.md) trước khi lập bảng.
