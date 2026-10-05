# Sổ nguồn nghiên cứu lần hai

Ngày kiểm tra **04/10/2026**. Các mã dưới đây trỏ tới nguồn gốc, không phải trang kết quả tìm kiếm. “Đọc trang” là nội dung HTML/abstract/tài liệu được trả về; không đồng nghĩa đọc/tái lập toàn bộ công trình. “Chỉ mục” là trích nội dung được lập chỉ mục trên nguồn gốc; mở trang thất bại. Chưa chạy công cụ hoặc kiểm thử sản phẩm nào trong lượt này.

| Mã | Nguồn | Điều hỗ trợ / mức truy cập | Giới hạn |
|---|---|---|---|
| E01 | [Alphonse & Tran, A Two-Step Approach to Investigate Dividend Policy, 2014](https://www.ccsenet.org/journal/index.php/ijef/article/view/32728) | Đọc abstract nhà xuất bản; chính sách cổ tức Việt Nam có nghiên cứu xét lợi nhuận/FCF | Không tái lập kinh tế lượng; FCF khác CFO |
| E02 | [Vu, The impact of the free cash flow and the firm’s life cycle on dividend policy, 2023](https://ctujs.ctu.edu.vn/index.php/ctujs/article/view/583) | Chỉ mục abstract CTU: mẫu 110 công ty HOSE, 2014–2020; FCF/vòng đời/chính sách cổ tức | Mở trang timeout; không đọc full text trong lượt này |
| E03 | [FiinTrade: Báo cáo tài chính](https://web.fiintrade.vn/nhom-trang-tinh-nang/phan-tich-co-ban/bao-cao-tai-chinh/) | Đọc mô tả chức năng BCTC chuẩn hóa, xem quý/năm | Không đăng nhập, không đánh giá dữ liệu/logic nội bộ |
| E04 | [FiinTrade: Cổ tức và dự báo](https://web.fiintrade.vn/nhom-trang-tinh-nang/phan-tich-co-ban/co-tuc-va-du-bao/) | Đọc mô tả lịch sử/lịch/dự phóng cổ tức | Không kết luận mô hình dự phóng, độ chính xác hoặc chức năng chưa công bố |
| E05 | [Vnstock, repository thinh-vu/vnstock](https://github.com/thinh-vu/vnstock) | Đọc README: kết nối/chuẩn hóa nguồn bên thứ ba; balance_sheet/cash_flow/income_statement/ratios | Không chạy thư viện; mã công khai không mặc định giấy phép open-source hay quyền dữ liệu. Repo vnstock-official cũng được thấy nhưng không dùng để đại diện bản hiện hành |
| E06 | [Docling: DoclingDocument](https://github.com/docling-project/docling/blob/main/docs/concepts/docling_document.md) | Đọc tài liệu: bảng/text/layout/provenance | Không chứng minh trích chính xác chỉ tiêu BCTC Việt Nam |
| E07 | [Docling Graph: Data Grounding & Provenance](https://github.com/docling-project/docling-graph/blob/main/docs/fundamentals/graph-management/provenance.md) | Đọc tài liệu ledger chunks/trang/node | Prior art cho truy nguồn; chưa benchmark cả pipeline |
| E08 | [FinQA, 2021](https://arxiv.org/abs/2109.00122) | Đọc metadata/abstract; QA và numerical reasoning trên báo cáo tài chính | Task khác extraction end-to-end và lifecycle cổ tức |
| E09 | [TAT-QA, 2021](https://arxiv.org/abs/2105.07624) | Đọc metadata/abstract; suy luận từ bảng và văn bản tài chính | Không là gold Việt Nam cho project |
| E10 | [VLSP 2025 challenge: Numerical Reasoning Question and Answer](https://aclanthology.org/2025.vlsp-1.25/) | Đọc metadata và [PDF, abstract/task/dataset/metrics](https://aclanthology.org/2025.vlsp-1.25.pdf); ViNumQA gồm hơn 4.000 bộ câu hỏi–chương trình–đáp án theo bài | Không tải/chạy benchmark; không đồng nhất benchmark QA với pipeline thu dữ liệu cổ tức |
| E11 | [ViFinQA dataset card, AIGuruTinix](https://huggingface.co/datasets/AIGuruTinix/ViFinQA) | Đọc card tự công bố: 1.012 câu hỏi, 1.973 báo cáo OCR, 100 công ty, 2015–2025 | Số theo tác giả/card tại thời điểm đọc, chưa xác minh từng file/nhãn; không mặc định peer review hoặc quyền dùng PDF nguồn |
| E12 | [Great Expectations: GX Core overview](https://docs.greatexpectations.io/docs/core/introduction/gx_overview/) | Đọc tài liệu official về validation/Expectations/results | Kiểm định dữ liệu là prior art; thư viện không tự giải quyết contract tài chính của project |
| E13 | [SEC: Financial Statement and Notes Data Sets](https://www.sec.gov/data-research/sec-markets-data/financial-statement-notes-data-sets) | Đọc trang official: dữ liệu XBRL theo bản đã nộp, tổ chức để phân tích qua thời gian | Nguồn Mỹ khác PDF/công bố Việt Nam; không dùng như dữ liệu pilot |
| E14 | [Chris Martin, Reclassified to Conform, arXiv v1, 30/09/2026](https://arxiv.org/abs/2609.38754) | Đọc abstract/metadata: tái dựng chuỗi dòng BCTC, restatement, citation và kiểm tra totals | **Preprint mới**, chưa xác nhận phản biện/tái lập; không lấy số hiệu năng trong abstract làm kết quả đã xác minh |
| E15 | [VSDC: VNM, đợt cuối 2023 và tạm ứng đợt 1/2024](https://vsdc.vn/vi/ad/174349) | Đọc body, ngày 30/08/2024: tổng 2.450 = 950 + 1.500 đồng/cổ phiếu theo hai năm | Route vsd.vn timeout, host vsdc.vn đọc thành công; không chứng minh annual coverage đầy đủ |
| E16 | [VSDC: SVC hủy ngày đăng ký cuối cùng](https://vsd.vn/vi/ad/173190) | Đọc trang, ngày 19/07/2024: hủy ngày đăng ký 22/07/2024 của notice trước | Không đồng nghĩa hủy mọi quyết định cổ tức hoặc annual DPS bằng 0 |
| E17 | [VSDC: VC7 điều chỉnh lịch](https://vsd.vn/vi/ad/192812) | Đọc trang, ngày 05/03/2026: 06/03/2026 → 05/06/2026; tham chiếu 17/TB-VSDC | Bản gốc đọc được sau đó ở E21; chưa benchmark liên kết tự động |
| E18 | [VSDC: VC7 điều chỉnh lịch tiếp](https://vsdc.vn/vi/ad/196257) | Đọc body, ngày 28/05/2026: 05/06/2026 → 30/06/2027; tham chiếu 815/TB-VSDC | Route vsd.vn lỗi, host vsdc.vn đọc được; chỉ là lịch công bố, chưa payment confirmation |
| E19 | [VSDC: VNM điều chỉnh nội dung thông báo](https://vsdc.vn/vi/ad/182559) | Đọc body: sửa giấy tờ nhận cổ tức, lý do phù hợp Luật Căn cước; ngày 08/05/2025, nội dung khác không đổi | Route vsd.vn lỗi, host vsdc.vn đọc được; không suy thay DPS từ tiêu đề điều chỉnh |
| E20 | [Ivașcu, Understanding Dividend Puzzle Using Machine Learning](https://link.springer.com/article/10.1007/s10614-023-10439-7) | Đọc abstract/metadata: công bố online 08/08/2023, tập 64 năm 2024; dùng ML nghiên cứu chính sách cổ tức | Nội dung sau abstract có paywall; chứng minh ML cổ tức đã có, không phải cùng target giảm DPS của project |
| E21 | [VSDC: VC7 thông báo gốc cổ tức năm 2024](https://vsdc.vn/vi/ad/190751) | Đọc body, công bố 06/01/2026: DPS 500 đồng, ngày đăng ký 26/01/2026, lịch trả 06/03/2026 | Lịch bị sửa bởi E17/E18; không dùng bản gốc như lịch hiện hành |

## Các nguồn tìm thấy nhưng không dùng làm bằng chứng chính

- Trang chương trình Frontiers of Factor Investing 2024 có mục *Dividend Forecasts via Machine Learning*, nhưng PDF tải lỗi. Chỉ hỗ trợ định hướng tìm kiếm; không lấy kết quả chưa đọc để xếp hạng mô hình.
- VLSP 2026 có trang task numerical QA trong chỉ mục, mở lỗi. Dùng bài VLSP 2025/PDF đã đọc làm bằng chứng chính.
- Các bài 2026/SAGE và dataset QA khác xuất hiện trong tìm kiếm, chưa đọc đủ để suy luận phạm vi/hiệu năng; không dựa vào chúng cho quyết định chốt.
- Các fork Great Expectations không dùng để đại diện dự án; ưu tiên tài liệu official E12.
- Kết quả đồ án từ Scribd/Studocu, Reddit và trang tổng hợp không được dùng để khẳng định tỷ lệ trùng hoặc chưa ai làm. Tìm kiếm kho .edu.vn chưa xác định được đồ án công khai trùng toàn bộ.

## Cách tái kiểm tra

1. Mở URL nguồn gốc, đối chiếu body/abstract với mệnh đề trong [báo cáo quyết định](20-nghien-cuu-lan-hai-va-chot-de-tai.md).
2. Với repo/tài liệu sống, pin commit/version nếu dùng làm baseline thực nghiệm; lượt khảo sát này chưa pin hoặc chạy.
3. E15/E18/E19/E21 đã đọc được trên host vsdc.vn. Collector vẫn phải lưu raw/locator/hash và kiểm tra lại nguồn trước khi đưa vào dataset gold; công cụ web đọc được không tính là discovery/download của project đã thành công.
4. Ghi riêng ví dụ thật, fixture giả lập và holdout; không biến ca nghiệp vụ tìm trên web thành kết quả parser đã đạt.
