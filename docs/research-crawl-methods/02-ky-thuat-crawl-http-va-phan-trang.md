# Kỹ thuật IT: crawl danh mục, phân trang và chọn tài liệu

> **Trạng thái 03/10/2026 — hồ sơ thử nghiệm thu thập.** Project hiện hành tập trung thu thập, kiểm định và phân tích lợi nhuận–dòng tiền–cổ tức tiền mặt. Xem [SRS hiện hành](../research-platform/02-de-tai-va-srs.md) và [phương pháp thống nhất](../research-platform/11-phuong-phap-thu-thap-va-xu-ly.md). Các ngưỡng cảnh báo, dự báo, scope và lịch cũ bên dưới chỉ để tham khảo; không là yêu cầu MVP hiện hành.

## 1. HTTP + HTML trước

Lần thử mới dùng thư viện Python `urllib.request`, `lxml` và `pypdf`, không chạy JavaScript hay trình duyệt. Bốn danh mục đã trả HTML có link PDF. Đây là lựa chọn ít thành phần nhất để người mới học Python giải thích được request → HTML → selector → item → file.

Mỗi adapter trả: mã doanh nghiệp, catalog URL, anchor title, context một dòng/thẻ, ngày công bố nếu có và URL file. HPG/HPA lấy ancestor `div.item`; DHG lấy `div.share-holders-body`; VHC chỉ lấy đoạn chứa link. Không lấy toàn trang làm context: các năm/kỳ/ngôn ngữ khác sẽ làm nhiễu metadata.

Danh mục thường có link tên file và link “Download” trỏ cùng URL. Dedup theo URL trong một nguồn/lần chạy, giữ anchor có tên tài liệu. Chuẩn hóa link tương đối bằng `urljoin`; không đoán tên file theo mẫu ngày tháng. URL có hai dấu `/` trong path được giữ nguyên theo link nguồn, không tự chuẩn hóa rồi giả định tài liệu tương đương.

## 2. Phân trang có giới hạn

Chỉ theo link quan sát được, cùng host và cùng path danh mục, có tham số `page`. Sắp số trang bằng số nguyên; không sắp chuỗi để trang 13 đứng trước trang 2. DHG bắt đầu page=0; HPG/HPA mặc định trang đầu là 1. Chạy cuối giới hạn hai trang/nguồn: HPG 2, DHG 2, VHC 1, HPA 2, tổng 7 trang HTML.

Giới hạn này phục vụ chứng minh dữ liệu gần hiện tại. Muốn bổ sung 2023–2024 phải cấu hình kỳ khác, mở số trang có giới hạn và kiểm tra coverage; prototype hiện chỉ lọc FY2025/H1-2026. Không nói mã hiện tại đã thu được lịch sử ba năm.

Trong MVP, dừng khi đã tìm đủ tập kỳ mong đợi **và** kiểm tra các trang có thể chứa bản thay thế; dừng theo ngày sớm nhất chỉ là tối ưu có điều kiện vì bản đính chính cũ có thể được đăng lại gần đây. Luôn có page budget để tránh vòng lặp hoặc crawl toàn site.

## 3. Phân loại ứng viên

Thứ tự cần áp dụng: loại tài liệu → kỳ → phạm vi → mức kiểm toán/soát xét → ngôn ngữ. Marker quý/bán niên được xét trước năm. Ví dụ thực nghiệm đã phát hiện và sửa:

- `Consolidated FS for the first half 2025` là H1-2025, không phải FY2025.
- `BCTC đã soát xét 30.06.2025` là ứng viên bán niên theo năm dương lịch, cần xác nhận khoảng kỳ trong PDF.
- `FY2025-Q3.25...` có marker quý, không phải báo cáo năm chỉ vì chứa FY2025.
- `BCTC năm 2025` upload tháng 3/2026 vẫn thuộc kỳ 2025.
- Tên PDF có “và giải trình” có thể là bundle chứa BCTC thật; phải đọc tên anchor đầy đủ, không loại máy móc mọi URL chứa từ đó.

Loại bản tổng quan kinh doanh, thư giải trình, CBTT và báo cáo riêng khỏi danh sách mục tiêu của pilot. Với loại/phạm vi chưa rõ, giữ `unknown`, không suy ra hợp nhất từ việc doanh nghiệp niêm yết. Rule-based classifier hiện chỉ là prototype cho các nguồn đã chọn; metadata vẫn là **candidate** trước khi đối chiếu header PDF.

## 4. Trình duyệt tự động khi nào cần?

Chỉ chuyển sang Playwright khi HTML chưa có link sau khi kiểm tra nguồn và phải thao tác bộ chọn năm/nút tải công khai. Luồng đề xuất: mở trang → chọn năm bằng control thấy được → chờ trạng thái tải/nội dung → lấy link/nội dung công khai → đưa vào downloader chung. [Tài liệu download của Playwright](https://playwright.dev/python/docs/downloads) mô tả cách chờ và lưu download. Đây là phương án đã nghiên cứu, **chưa chạy thử** trong crawler này.

Không cần browser cho bốn nguồn đã thử. Vinamilk là ứng viên kiểm tra UI năm tiếp theo; khảo sát trước đã lấy được Q1/H1-2026 từ HTML nhưng chưa thử bộ chọn năm để lấy FY2025. Không gọi hidden endpoint bị chặn chỉ vì tìm thấy trong JavaScript.

## 5. Khi nào dùng Scrapy?

`urllib + lxml` phù hợp cho 1–2 adapter, một người mới học, số request nhỏ. Chuyển Scrapy khi có nhiều nguồn/queue/resume cần framework chung; [Files Pipeline](https://docs.scrapy.org/en/latest/topics/media-pipeline.html) hỗ trợ tải file, trạng thái và checksum. [AutoThrottle](https://docs.scrapy.org/en/latest/topics/autothrottle.html) giúp điều chỉnh tốc độ theo độ trễ. Chưa cài/chạy Scrapy trong thử nghiệm mới; đây là phương án phát triển, không là điều kiện MVP.

Downloader pilot hiện có: một request đồng thời, cách request cùng host ít nhất 1 giây hoặc Crawl-delay đọc được, timeout 20 giây, tối đa hai lần với một số HTTP lỗi tạm thời, response cap 30 MiB, 1–3 trang và 1–3 file/công ty. Với Retry-After số lớn hơn 30 giây thì hoãn nguồn; ngày HTTP trong Retry-After chưa được parser triển khai. Redirect được báo lỗi để review, chưa tự follow. Các giới hạn tránh một nguồn lỗi làm treo toàn lần chạy.
