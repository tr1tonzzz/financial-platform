# Minh chứng đã chạy và protocol nghiệm thu tiếp theo

Ngày 11/10/2026. Phân biệt mức bằng chứng để báo cáo với thầy: **nguồn/code đã đọc**, **prototype phép tính đã chạy**, **ứng dụng tích hợp chưa chạy**, **thử người dùng chưa chạy**.

| Nội dung | Trạng thái / bằng chứng | Chưa chứng minh |
|---|---|---|
| 3 GitHub mới | Metadata, commit, tree, source snapshots, hash; đọc tĩnh | Chạy thành công, độ chính xác, hiệu quả đầu tư |
| G02 DHG 2025/comparative 2024 | Xem trang PDF; chép ba dòng; tính Decimal; [inputs](evidence/real-cases.json), [outputs](evidence/probe-results.json) | Tự trích CAPEX/D; gold độc lập; lịch sử 3 năm; cổ tức phổ thông tách khoản |
| G03 FPT | Đối chiếu VSDC; tính floor(21×3/20)=3 cổ phiếu thêm | Ngày basis hiệu lực và số đủ quyền đợt tiền mặt sau trên tài khoản thực |
| G01 | Prototype một điều kiện số dư fail và một điều kiện DPS unknown, giữ cả hai | Giao diện sàng lọc, lưu hồ sơ end-to-end và tác vụ người dùng |
| Luật miền nghiệp vụ | **20 test methods đạt**, có subcases; [mã kiểm tra](../../scripts/research/test_dividend_functions_probe.py) | Không phải TC-D01–12 của ứng dụng, không phải benchmark dữ liệu |

Các tests kiểm: missing≠zero; issuer/period/scope/unit; nguồn/duyệt/thông tin tương lai; khoản chi magnitude; mẫu số=0; CFO âm; cấm lấy announced DPS thay thực chi; basis identity/chain/tách-gộp/canceled/unsupported/unresolved; không double-adjust; partial annual; phần lẻ; AND ba trạng thái; unknown được giữ cùng fail; operator/unit không hợp lệ. Fixture giả lập dùng cho rules; ca DHG và thông báo FPT dùng cho kiểm tra tính khả thi dữ liệu.

Tái chạy từ gốc repository:

```powershell
python scripts/research/test_dividend_functions_probe.py
python scripts/research/dividend_functions_probe.py
python scripts/research/validate_dividend_function_docs.py
```

Probe chỉ dùng thư viện chuẩn, không cần tải network và không import dự án GitHub. Kết quả Decimal có nhiều chữ số; UI dự kiến làm tròn khi hiển thị. Đối chiếu DHG là tự kiểm của người soạn, chưa có người thứ hai; `reviewed` trong fixture chỉ nghĩa research author đã nhìn nguồn, không phải trạng thái production review. Thời điểm available_at của DHG đặt ngày quan sát nghiên cứu 11/10/2026; **chưa xác minh ngày công bố lịch sử**, không dựng kết quả point-in-time trước ngày này. Cột so sánh 2024 dùng nguồn 2025, không dữ liệu biết sẵn trong 2024.

## Bộ kiểm chứng ứng dụng dự kiến

TC-D01–04: nhập/duyệt đúng loại CAPEX/D; chặn thiếu/sai metadata; tính và mẫu số; nguồn/xuất. TC-D05–08: ledger tỷ lệ/ngày; basis chain; trạng thái/canceled/unsupported/double-adjust; annual coverage và xuất. TC-D09–12: criteria/version; ba trạng thái; dossier/note/snapshot; freeze/replay. Chi tiết nghĩa vụ ở mục 16 SRS. Mỗi TC có expected fixture, actual, version, log/snapshot, người chạy và `passed/failed/not_run`; nghiên cứu này giữ **not_run ở ứng dụng**.

Bổ sung tối thiểu một ca G02 có số dư dương và một ca âm; một trường hợp khoản trả gộp; một trường hợp công ty mẹ/hợp nhất khác scope; G03 một basis chain xác nhận đầy đủ, một missing/unsupported và FPT floor example; G01 ba hồ sơ pass/fail/unknown với ít nhất một fail+unknown. Gold độc lập cần người xác minh trang/kỳ/scope/ý nghĩa, không chỉ copy output probe. Chốt trước tiêu chí sai số số học theo precision nguồn, điều kiện hiển thị và các chặn bắt buộc; mọi kết quả xuất bản phải có provenance.

## Thực nghiệm giá trị sử dụng

Chạy tác vụ nhập tay và dùng hệ thống trên cùng tập hoặc tập tương đương, có đổi thứ tự để giảm hiệu ứng học. Đo riêng: thời gian tìm nguồn, nhập/duyệt, tra soát, lập hồ sơ; số lỗi số liệu và lỗi diễn giải; số câu hỏi quan trọng nhận diện đúng; số kết quả thiếu bị kết luận sai. Pilot ít người chỉ đánh giá khả dụng, chưa suy hiệu quả đầu tư/khả năng dự báo. Báo cả missing và công sức review, không chỉ tốc độ hàm tính.

## Nội dung demo ngắn để trao đổi với thầy

Một UC nhỏ B02.4: đầu vào ba dòng DHG → kiểm kỳ/scope/định nghĩa → số dư −125,629 tỷ → mở nguồn và lập câu hỏi. Một UC nhỏ B03.4: nguồn quyền FPT 20:3 → factor lý thuyết/rounding → minh họa 21 thành 24 → chỉ ra dữ liệu basis còn thiếu. Một UC nhỏ B04.3/B05.1: tiêu chí số dư → fail và DPS unknown → danh sách lý do → hồ sơ cần tra soát. Nêu prototype đã chạy, phần UI/data workflow mới đề xuất. Không lặp tổng quan đề tài hoặc gán ba phép tính là ứng dụng đã hoàn thành.
