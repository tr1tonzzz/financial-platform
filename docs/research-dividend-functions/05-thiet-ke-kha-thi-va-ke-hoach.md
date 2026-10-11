# Thiết kế tích hợp, tính khả thi và kế hoạch triển khai

Ngày 11/10/2026. Thiết kế hiện hành giữ web React/FastAPI/Python/PostgreSQL theo [quyết định stack](../research-platform/31-chot-pham-vi-va-stack-paddleocr.md); thay phương án pilot Python/SQLite/Streamlit trước đó. Prototype nghiên cứu không thay thế service ứng dụng; tên bảng/interface dưới đây là thiết kế đề xuất, chưa là migration đã chạy.

**Đối chiếu code hiện tại:** repository có các script nghiên cứu/thu nguồn, như [crawler](../../scripts/research/crawl_official_reports.py) và probe; chưa có web React/FastAPI/PostgreSQL hoàn chỉnh để tích hợp ngay. Vì vậy giờ bổ sung bên dưới là ước tính sau khi có hạ tầng baseline, không là tổng thời gian từ trạng thái repository hiện tại.

## Mô hình dữ liệu bổ sung

| Thực thể | Thuộc tính chính / quy tắc |
|---|---|
| financial_fact mở rộng | metric CAPEX/distribution, period/scope/unit/source/revision như sáu facts; thêm definition/kind/recipient_scope/sign_mapping |
| corporate_action + revision | Ratio và các mốc ngày riêng; kind/status/link sửa-hủy; basis_confirmed/evidence; không ghi đè nguồn |
| basis_interval | source_basis/target_basis, khoảng hiệu lực đã duyệt, action_revision_ids, factor, applicability_reason |
| metric_result | metric_id/version, Decimal value hoặc null, status/reason, operand_refs, snapshot_id, definition |
| screen_definition + version | Điều kiện có operator/threshold/unit, universe/window, cấu hình missing cố định, người tạo/thời gian |
| screening_run | criteria_version, snapshot_id, từng condition_result, outcome và excluded; chưa có job chạy nền |
| diligence_dossier | issuer, run/snapshot refs, trạng thái draft/reviewed_by_user; không giả làm phê duyệt tài chính |
| diligence_note/task | author/time/text, source refs, loại giả thuyết/nhận xét, open/resolved, bằng chứng xử lý |

Khóa fact vẫn dùng issuer/period/scope/metric/revision; không ghép bằng ticker đơn lẻ. Chỉ facts reviewed được metric service đọc. Dossier dùng fact revision bất biến và lưu bộ tiêu chí/version. Cập nhật dữ liệu không thay hồ sơ freeze. Parser và UI không tự sửa cùng field mà thiếu audit. Migration thêm bảng/cột riêng và kiểm backup trước chuyển đổi; đây là bước triển khai, chưa làm trong nghiên cứu.

## Giao diện xử lý và giao diện sử dụng

`compute_cash_coverage(fact_refs, snapshot)` trả metric riêng cho số dư và tỷ số, definition/kind, operands và reason; lỗi tỷ số không xóa số dư hợp lệ. `resolve_basis_interval(issuer, from_basis, to_basis, as_of)` trả action chain hoặc blocking reasons. `normalize_dps(raw_component_refs, interval)` giữ raw song song; không tự discovery sự kiện. `evaluate_screen(criteria_version, snapshot)` trả từng điều kiện và ba trạng thái, giữ universe count. `freeze_dossier(run, notes, tasks)` xuất dữ liệu tự chứa đủ để replay khi công thức còn được hỗ trợ.

Màn hình theo năm UC lớn: Hồ sơ dữ liệu → Nền tảng tiền mặt → Lịch sử cổ tức → Sàng lọc/đối chiếu → Hồ sơ thẩm định. Nút “Tra soát bằng chứng” tới operand và trang nguồn; trạng thái không tính được hiện lý do cùng hành động cần làm. Thu thập/nhập/duyệt là các tác vụ trong Hồ sơ dữ liệu, không thêm thành nhóm sản phẩm ngang hàng. Người dùng không cần đọc parser hay tên thư viện OCR để quyết định thẩm định.

## Đánh giá khả thi có điều kiện

| Chiều | G02 | G03 | G01 |
|---|---|---|---|
| Dữ liệu hiện có | CFO có; phải bổ sung CAPEX/D | DPS có cấu trúc; phải bổ sung action/basis | Sáu facts và FR29 dùng được; metric mới tùy tiêu chí |
| Minh chứng Việt Nam | Trang DHG chứa ba dòng lõi, có nhãn khoản gộp | FPT có ratio/rounding; chưa đủ mọi ngày hiệu lực | Chạy lọc minh họa DHG với một fail và một unknown |
| Khó nhất | Xác nhận đúng loại chi và chủ thể nhận | Xác nhận basis, hiệu lực, coverage, tránh double-adjust | Ngữ nghĩa missing và hồ sơ tái lập được |
| Làm sớm | Nhập/duyệt một ca, service Decimal | Một loại quyền miễn phí, chain được duyệt | Bộ lọc hiện hữu + lưu tiêu chí + dossier |
| Chưa cam kết | Trích tự động mọi BCTC; bền vững tương lai | Mọi corporate action; thực nhận từng tài khoản | Xếp hạng tối ưu; hiệu quả lợi nhuận; toàn thị trường |

## Thứ tự thực hiện và dự toán

Các giờ dưới đây là **ước tính thiết kế**, chưa đo và chưa cộng vào lịch 13 tuần. Giả định hạ tầng BUC01, audit/snapshot và UI cơ bản đã hoạt động; nếu chưa, công việc nền phải hoàn thành trước và ước tính này tăng. Không cộng công sức nghiên cứu đã làm vào giờ lập trình còn lại.

| Gói việc | Ước tính giờ | Đầu ra / điểm hoàn thành |
|---|---:|---|
| Chốt schema/metric registry/reason codes chung | 4–6 | Data contract và lưu refs tương thích snapshot |
| G02 một ca end-to-end | 16–24 | Nhập/duyệt → tính → UI → nguồn → xuất; TC-D01–04 |
| G03 chế độ A, 1–2 ca quyền miễn phí | 18–28 | Ledger/chain → basis → DPS song song → nguồn; TC-D05–08 |
| G01 criteria và dossier | 20–30 | Ba nhóm → giải thích → notes/tasks → freeze/replay; TC-D09–12 |
| Thử tác vụ/đối chiếu độc lập và chỉnh | 6–10 | Hồ sơ expected/actual, giờ và lỗi người dùng |
| **Tổng bổ sung** | **64–98** | Ngoài baseline 167 giờ; có phần tái sử dụng nhưng chưa đo để trừ |

Trong 2–3 buổi đầu, ưu tiên một luồng dọc G02 DHG để có minh chứng dễ trao đổi: nguồn → reviewed input → residual → câu hỏi thẩm định → dossier. Sau đó G03 với nguồn FPT và một fixture có đủ basis để kiểm tính; ghi rõ FPT chưa đủ basis thay vì giả định hoàn thiện. G01 mức tối thiểu có thể làm song song về thiết kế, nhưng tích hợp metric mới sau khi hai service ổn định. Một chức năng được gọi hoàn chỉnh khi người dùng thực hiện được tác vụ đầu cuối, không chỉ hàm tính đúng.

Để đẩy tiến độ: giữ pilot nhỏ; nhập có nguồn các trường mới trước tự động hóa; tái dùng audit/snapshot; làm từng lát đầu cuối; mỗi buổi kết thúc bằng artifact chạy lại được. Không đồng thời thêm giá, vị thế và dự báo. Nếu quỹ còn lại nhỏ hơn dự toán, chọn slice tối thiểu của ba chức năng để trao đổi phạm vi với thầy; không tự bỏ các FR baseline để dành chỗ. Quỹ giờ/cỡ mẫu/ngưỡng chấp nhận là điểm mở của CR-DIV-02, không cần chờ chúng mới chuẩn bị thiết kế và prototype.

## Định nghĩa hoàn thành và minh chứng

Mỗi UC lớn có tác vụ end-to-end trên ca thật hoặc trạng thái thiếu có nguồn; expected/actual và snapshot; tests lỗi miền nghiệp vụ; có đo nhập/duyệt/thẩm định; phân biệt development với holdout. 20 tests prototype hiện tại kiểm luật tính, chưa đạt định nghĩa này. OCR benchmark Paddle/Tesseract là nhánh chất lượng đầu vào BUC01 riêng: dùng cùng trang/gold, đo lỗi **field số/kỳ/cột**, effort review và môi trường CPU; không suy Paddle tốt hơn vì tên dự án hoặc benchmark khác miền. Nghiên cứu này không thay thế benchmark đó.
