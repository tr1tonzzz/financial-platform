# Pilot, công sức và tái lập khảo sát

Khảo sát hoàn thành ngày 03/10/2026. Mục tiêu bước kế tiếp là đo khả năng mở rộng, không dùng số file đã tải để tuyên bố đạt pilot trong SRS.

## 1. Pilot gần hiện tại theo hai mức

**Mức A:** 10 doanh nghiệp phi tài chính × BCTC kiểm toán năm 2025 × sáu chỉ tiêu, cùng lịch sự kiện cổ tức đủ để đánh giá độ phủ. Chọn có chủ đích nhiều ngành, layout, PDF text/scan và doanh nghiệp có/không tìm thấy sự kiện; không chỉ chọn các công ty trả cổ tức đều. DHG, HPG, VHC, VNM là bốn ứng viên từ nguồn đã thử; VHE là ứng viên kiểm tra nguồn HNX, chưa chứng minh đầy đủ cổ tức. REE/FPT cần đường tài liệu chính thức khác được kiểm tra hoặc nhập có nguồn trước khi chốt vào pilot. Danh sách 10 chưa được chốt trong phép thử này.

**Mức B:** thêm Q1 và H1/2026 cho bốn doanh nghiệp có đường tải đã chạy, tức tám báo cáo cập nhật. Chỉ mở rộng cả 10 công ty × ba kỳ = 30 báo cáo nếu thời gian chuẩn hóa đáp ứng. Bản tiếng Anh và tiếng Việt không tăng số quan sát.

Hai mức trên kiểm tra khả thi của dữ liệu mới. Pilot lịch sử 2020–2024, số công ty tối thiểu và kiểm tra nhãn của SRS vẫn phải thực hiện; không thay chúng bằng 10 báo cáo năm 2025.

## 2. Thước đo và điều kiện mở rộng đề xuất

| Thước đo | Cách tính | Mốc đề xuất, chưa đạt/đo đầy đủ |
|---|---|---|
| Phủ báo cáo năm 2025 | Báo cáo đúng kỳ/scope thu được / 10 kỳ kỳ vọng | ≥8/10 để xem xét thêm 2025; công bố công ty thiếu và lý do |
| Hoàn chỉnh sáu chỉ tiêu | Quan sát có đủ sáu giá trị đã duyệt / báo cáo kỳ vọng | Đo cả trên expected và downloaded để không che missing |
| Đúng giá trị trước sửa | Giá trị trích khớp gold độc lập / mọi target trên holdout, tính missing là lỗi | ≥95% để xem xét tăng tự động hóa; cần cỡ mẫu/CI và kết quả theo layout |
| Truy vết sau duyệt | Giá trị xuất bản có file, kỳ, unit, scope, locator / giá trị xuất bản | 100%, theo yêu cầu SRS |
| Công sức | Phút phát hiện + parser + review + sửa / báo cáo, tách các phần | Lấy median/P90 thực đo, không lấy thời gian OCR thay thế |
| Cổ tức | Số khoảng đã rà đủ nguồn, số sự kiện và điều chỉnh, tỷ lệ profit_year xác minh | Không suy “không trả” từ không tìm thấy |
| Nhãn | Số mẫu eligible, unknown, censored và ca giảm/ngừng mỗi split | Dùng gate ML của research-design, không tính mẫu chưa khép |

Mốc 8/10 và 95% là tiêu chí vận hành **đề xuất cho pilot này**, không phải tỷ lệ thành công đã đạt và không tự sửa TP. Nếu không đạt, giữ 2025/2026 ở vài case đã duyệt và tập trung dữ liệu lịch sử. Không mở rộng lên 60–80 công ty khi công sức review chưa đo.

## 3. Ước lượng để lập kế hoạch

Giả định sơ bộ 15–40 phút kiểm tra/sửa một báo cáo sáu chỉ tiêu: 18 báo cáo của mức A+B cần khoảng 4,5–12 giờ review. Thêm 4–8 giờ khảo sát/chỉnh adapter và 3–6 giờ rà sự kiện cổ tức cho ra **11,5–26 giờ** công việc pilot gần hiện tại, chưa bao gồm xây crawler production, dataset lịch sử hay đánh giá ML. Đây là ngân sách giả định để kiểm tra, không phải đo thời gian công việc đã thực hiện.

So với tổng 130–156 giờ của kế hoạch hiện hành, không nên tự cộng phạm vi này thành nghĩa vụ phủ quý đầy đủ. Có thể tái sử dụng file đã tải và dùng một vài case 2026 trước. Giá trị quyết định của pilot là đo tỷ lệ phải sửa và thời gian người duyệt; 29,8 giây OCR không chứng minh toàn bộ báo cáo được chuẩn hóa trong nửa phút.

## 4. Thành phần đã lưu

| Thành phần | Vị trí trong repository |
|---|---|
| Probe URL/PDF | `scripts/research/probe_recent_sources.py` |
| Seed danh mục, robots, tài liệu, nguồn EN và cổ tức | `scripts/research/recent_*_seeds.json` |
| OCR ảnh đã render | `scripts/research/probe_ocr.cjs`, `recent_ocr_pages.json` |
| Tóm tắt PDF và đối chiếu 12 target | `scripts/research/summarize_recent_probe.py` |
| Trích bốn HTML cổ tức | `scripts/research/extract_recent_dividend_examples.py` |
| Raw evidence, ignored bởi Git | `data-sets/research-evidence/2026-10-03-recent/` |
| Bằng chứng chia sẻ | Bốn JSON trong thư mục tài liệu này |

Runtime thực dùng: Python 3.12.14, pdfplumber 0.11.9, Node 24.15.0, Tesseract.js 7.0.0 và Poppler trong môi trường. Version này là hồ sơ phép thử, chưa phải dependency lock của application. Lần đầu OCR có thể tải language models về cache; cần mạng và giữ model/version để tái lập tốt hơn.

## 5. Chạy lại trong PowerShell tại root repository

Các đường runtime dưới đây là đường có thật trên máy khảo sát; máy khác thay tương ứng. Các seed là snapshot ngày 03/10, không phải bộ tự phát hiện URL tương lai. Cần đọc lại robots khi tải mới vì cờ `probe_allowed` không tự cập nhật theo website.

```powershell
$researchPython = 'C:\Users\admin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$researchNode = 'C:\Program Files\nodejs\node.exe'
$researchTesseract = 'C:\Users\admin\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\node_modules\tesseract.js'
$researchPoppler = 'C:\Users\admin\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe'
$researchEvidence = 'data-sets/research-evidence/2026-10-03-recent'

# Đọc robots và danh mục trước khi quyết định tải các tài liệu.
& $researchPython scripts/research/probe_recent_sources.py scripts/research/recent_robots_seeds.json $researchEvidence
& $researchPython scripts/research/probe_recent_sources.py scripts/research/recent_catalog_seeds.json $researchEvidence

# Chỉ chạy sau khi đối chiếu lại policy và các seed cho phép tải.
& $researchPython scripts/research/probe_recent_sources.py scripts/research/recent_document_seeds.json $researchEvidence
& $researchPython scripts/research/probe_recent_sources.py scripts/research/recent_alternative_seeds.json $researchEvidence
& $researchPython scripts/research/probe_recent_sources.py scripts/research/recent_dividend_discovery_seeds.json $researchEvidence
```

Probe tái dùng download thành công cùng ID/URL, giữ timestamp cũ; không phải tái đo truy cập trực tiếp khi thấy `cached=true`. Muốn làm snapshot mới, dùng thư mục output mới. Snapshot mới có thể khác hash vì nguồn thay phiên bản; không ghi đè bằng chứng cũ.

HNX cần đường bổ sung vì Python lỗi CA. Lệnh đã dùng phương án Schannel, vẫn xác thực TLS:

```powershell
curl.exe --fail --location --max-time 30 --max-filesize 31457280 --dump-header "$researchEvidence/hnx-vhe-fy2025-curl-headers.txt" --output "$researchEvidence/hnx-vhe-fy2025-curl.pdf" --write-out 'HTTP=%{http_code} TLS=%{ssl_verify_result} bytes=%{size_download} seconds=%{time_total}' 'https://owa.hnx.vn/ftp///cims/2026/3_W4/000000016025637_VI_BaoCaoTaiChinh_Nam_2025_BaoCaoHopNhat.pdf'
```

Trong khảo sát gốc, file HNX đã được mở bằng cùng hàm `inspect_pdf` và lưu `hnx-vhe-fy2025-curl-inspection.json`; `summarize_recent_probe.py` sẽ đọc file này nếu PDF HNX tồn tại. Trên thư mục mới phải tạo inspection bằng hàm đó trước khi summarize, không coi bước curl là đã kiểm tra PDF. Có thể chạy:

```powershell
@'
import json
import sys
from pathlib import Path
sys.path.insert(0, 'scripts/research')
from probe_recent_sources import inspect_pdf
evidence = Path(sys.argv[1])
result = inspect_pdf(evidence / 'hnx-vhe-fy2025-curl.pdf', evidence)
(evidence / 'hnx-vhe-fy2025-curl-inspection.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
'@ | & $researchPython - $researchEvidence
```

Render lại đúng 10 trang rồi OCR nếu muốn tái chạy, thay vì chỉ xem kết quả OCR đã lưu:

```powershell
New-Item -ItemType Directory -Force "$researchEvidence/ocr" | Out-Null
$researchJobs = Get-Content scripts/research/recent_ocr_pages.json -Raw -Encoding utf8 | ConvertFrom-Json
foreach ($researchJob in $researchJobs) {
    & $researchPoppler -f $researchJob.pdf_page -l $researchJob.pdf_page -r 220 -singlefile -png "$researchEvidence/$($researchJob.document).pdf" "$researchEvidence/ocr/$($researchJob.id)"
}
& $researchNode scripts/research/probe_ocr.cjs $researchTesseract scripts/research/recent_ocr_pages.json "$researchEvidence/ocr"
& $researchPython scripts/research/summarize_recent_probe.py $researchEvidence docs/research-recent-data
& $researchPython scripts/research/extract_recent_dividend_examples.py $researchEvidence docs/research-recent-data/dividend-event-examples.json
```

`recent_ocr_pages.json` dùng đường ảnh tương đối với root repository và thư mục snapshot gốc; nếu đổi output directory thì sửa đường ảnh theo snapshot mới. Các giá trị đối chiếu trong script summarize là tham chiếu từ ảnh snapshot gốc, không tự là gold cho tài liệu đổi phiên bản. Script cũng ghi metadata thời gian curl gốc như trường `*_observed`; không dùng nó làm số đo của lần curl mới. Chạy lại OCR có thể cho số đo khác; cần lưu run mới riêng khi làm benchmark.

## 6. Kết quả cần có trước khi nhận phạm vi mới

Một bảng coverage đủ 10 công ty, dữ liệu được duyệt, số giờ thực đo và danh sách missing là đầu ra cần cho quyết định bổ sung 2025 rộng hơn. Nếu làm nghiên cứu dự báo, cần bảng nhãn trưởng thành và split theo thời gian riêng. Việc tải được PDF 2026 và phân tích case mới đã khả thi; cam kết tự động hoàn toàn hoặc mô hình dự báo trên nhãn mới chưa có đủ bằng chứng.
