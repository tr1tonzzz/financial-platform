# Sổ nguồn — hướng nền tảng dữ liệu và năng lực phân tích

Truy cập ngày **11/10/2026**. Nguồn GitHub được lưu theo commit cố định; nội dung web là nội dung truy cập vào ngày nghiên cứu, có thể được cập nhật sau đó.

## 1. GitHub: sáu nguồn trong đợt này

| Mã | Repository tại commit đọc | Bản lưu metadata/cây tệp/hash | Số tệp lưu | Tình trạng sử dụng |
|---|---|---|---:|---|
| FP-S01 | [dgunning/edgartools — 2460109](https://github.com/dgunning/edgartools/tree/246010946cdbe588b0397643fb1598a04fe0cad6) | [inventory](evidence/github/dgunning__edgartools/inventory.json) | 6 | Bổ sung; đọc tĩnh |
| FP-S02 | [JerBouma/FinanceDatabase — 5583c4e](https://github.com/JerBouma/FinanceDatabase/tree/5583c4ef5d51fa404a65aa4685da60aca69b7538) | [inventory](evidence/github/JerBouma__FinanceDatabase/inventory.json) | 4 | Bổ sung; đọc tĩnh |
| FP-S03 | [JerBouma/FinanceToolkit — 37ed6f0](https://github.com/JerBouma/FinanceToolkit/tree/37ed6f01465b4bfb6718b07e1d65826734f53337) | [inventory](evidence/github/JerBouma__FinanceToolkit/inventory.json) | 4 | Đọc sâu lại commit đợt trước |
| FP-S04 | [theOGognf/finagg — 614631d](https://github.com/theOGognf/finagg/tree/614631d8e26bdbb21c1a6e6a3a10972a00e1d24b) | [inventory](evidence/github/theOGognf__finagg/inventory.json) | 5 | Bổ sung; đọc tĩnh |
| FP-S05 | [Fincept-Corporation/FinceptTerminal — 3f444cb](https://github.com/Fincept-Corporation/FinceptTerminal/tree/3f444cb7ab712d85a57d270d5edd6e7a2ef50d55) | [inventory](evidence/github/Fincept-Corporation__FinceptTerminal/inventory.json) | 8 | Bổ sung; đọc tĩnh |
| FP-S06 | [OpenBB-finance/backends-for-openbb — a629370](https://github.com/OpenBB-finance/backends-for-openbb/tree/a6293707576e16edda8305adda95b07b6a4b968b) | [inventory](evidence/github/OpenBB-finance__backends-for-openbb/inventory.json) | 5 | Bổ sung; backend ví dụ |

Tổng **32 tệp** chưa gồm sáu inventory. Không tính tệp này là sáu hệ thống đã chạy. Mã bản lưu là bằng chứng khảo sát, không được nhập làm mã ứng dụng của project.

Inventory giữ SHA, ngày commit, ngày thu, cây tệp và SHA-256 từng tệp đã tải. Metadata license GitHub của Fincept là `NOASSERTION`; [tệp LICENSE thực tế](evidence/github/Fincept-Corporation__FinceptTerminal/LICENSE) có nội dung AGPL v3 và thông báo dual licensing. Chưa thực hiện quyết định tái sử dụng code từ repo này. Các inventory khác có metadata MIT hoặc Apache-2.0 và tệp license bản lưu.

## 2. Tài liệu chính thức và nghiên cứu gốc

| Mã | Nguồn | Đã đọc để làm rõ điều gì? | Loại bằng chứng |
|---|---|---|---|
| FP-S07 | [CFA Institute — Financial Analysis Techniques, curriculum 2026](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/financial-analysis-techniques) | Quy trình phân tích, cơ sở so sánh, vai trò tỷ số và biểu đồ | Tài liệu nghề nghiệp; phần Introduction/Learning Outcomes công khai, không đọc phần khóa trong Learning Ecosystem |
| FP-S08 | [OpenBB — Interacting With Data](https://docs.openbb.co/workspace/analysts/widgets/interacting-with-data) | Tham số liên kết, bảng/biểu đồ và dữ liệu nền | Tài liệu sản phẩm chính thức, trang ghi cập nhật 29/09/2026 |
| FP-S09 | [OpenBB — Dashboards](https://docs.openbb.co/workspace/analysts/dashboards) | Tổ chức và sử dụng lại không gian phân tích | Tài liệu sản phẩm chính thức |
| FP-S10 | [EdgarTools — Company Facts](https://edgartools.readthedocs.io/en/latest/guides/company-facts/) | Truy vấn facts và bảng nhiều kỳ | Tài liệu dự án chính thức, đối chiếu với FP-S01 |
| FP-S11 | [Shneiderman, 1996 — The Eyes Have It: A Task by Data Type Taxonomy for Information Visualizations](https://api.drum.lib.umd.edu/server/api/core/bitstreams/419fe7fc-d7d8-4929-bdf0-f4a3041455c1/content) | Các tác vụ khám phá trực quan, lịch sử và trích xuất | Bản báo cáo nghiên cứu gốc trên kho University of Maryland; CS-TR-3665/ISR-TR-96-66 |
| FP-S12 | [OpenBB — Widgets JSON Reference](https://docs.openbb.co/workspace/developers/json-specs/widgets-json-reference) | Cấu hình loại góc nhìn/tham số/dữ liệu | Tài liệu kỹ thuật chính thức; tham khảo khả thi, chưa tích hợp |

FP-S07/FP-S11 cung cấp cơ sở quy trình và thiết kế, không là bằng chứng hệ thống project cải thiện lợi nhuận đầu tư. FP-S08/FP-S09/FP-S12 thuộc sản phẩm Workspace; không gộp tình trạng mã mở với backend mẫu FP-S06.

## 3. Kế thừa nghiên cứu trong repository

- [Khảo sát GitHub cổ tức trước](../research-github-dividend/README.md): chín repo, G01–G10 và bằng chứng tĩnh.
- [Nghiên cứu triển khai ba chức năng](../research-dividend-functions/README.md): thêm ba repo; G02/G03/G01 có prototype độc lập và ca nguồn DHG/FPT.
- [Nghiên cứu lợi nhuận–CFO–cổ tức](../research-profit-cash-dividend/README.md): cầu nối theo ca và các điều kiện dữ liệu.
- [SRS v3.3](../research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md): FR25–FR28/FR31–FR32/FR34–FR35, E và D còn hoạt động; FR29/30/D09/10 đã rút tại mục18.
- [Tài liệu giải thích chức năng](../research-platform/27-yeu-cau-chuc-nang-va-vi-du.md): bản đọc đơn giản, phân biệt nền và đề xuất.

Chín repo + ba repo trước + năm repo bổ sung = **17 repo khác nhau**. FinanceToolkit đợt này là nguồn đọc lại. Không cộng đọc lại thành repo thứ 18.

## 4. Kiểm tra hồ sơ nghiên cứu

[Kết quả kiểm tra tài liệu và bản lưu](evidence/research-validation.json) ghi số tệp, liên kết nội bộ, hash tệp và tham chiếu code tại commit cố định. Đây là kiểm tra toàn vẹn hồ sơ, không phải kiểm thử ứng dụng hoặc xác nhận các nhu cầu đã được người dùng thử nghiệm.
