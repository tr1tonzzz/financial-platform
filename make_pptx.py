import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]
img_dir = 'docs/report-docs/images'

def add_bg(slide, img_name):
    path = os.path.join(img_dir, img_name)
    if os.path.exists(path):
        slide.shapes.add_picture(path, 0, 0, prs.slide_width, prs.slide_height)

def add_title_slide():
    slide = prs.slides.add_slide(blank)
    add_bg(slide, 'hust-blue-169-title.png')
    txBox = slide.shapes.add_textbox(Inches(1), Inches(2.2), Inches(11.3), Inches(1))
    p = txBox.text_frame.paragraphs[0]
    p.text = "BÁO CÁO TỔNG QUAN: FINANCIAL DATA PLATFORM (FDP)"
    p.font.bold = True; p.font.size = Pt(36); p.font.color.rgb = RGBColor(0, 90, 140)
    
    txBox2 = slide.shapes.add_textbox(Inches(1), Inches(4.5), Inches(11.3), Inches(1.5))
    p2 = txBox2.text_frame.paragraphs[0]
    p2.text = "Sinh viên thực hiện: Phạm Hải Nam - 20235791\nGiảng viên hướng dẫn: TS. Nguyễn Đức Toàn"
    p2.font.bold = True; p2.font.size = Pt(20)

def add_section_slide(p1, p2_text):
    slide = prs.slides.add_slide(blank)
    add_bg(slide, 'hust-blue-169-content-full.png')
    txBox = slide.shapes.add_textbox(Inches(1), Inches(2.5), Inches(11.3), Inches(2))
    p = txBox.text_frame.paragraphs[0]
    p.text = p1
    p.font.bold = True; p.font.size = Pt(44); p.alignment = PP_ALIGN.CENTER
    p2 = txBox.text_frame.add_paragraph()
    p2.text = p2_text
    p2.font.bold = True; p2.font.size = Pt(36); p2.alignment = PP_ALIGN.CENTER

def add_content_slide(title, items, is_logo_only=False):
    slide = prs.slides.add_slide(blank)
    add_bg(slide, 'hust-blue-169-content-logo.png' if is_logo_only else 'hust-blue-169-content-full.png')
    
    if title:
        txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(12), Inches(1))
        p = txBox.text_frame.paragraphs[0]
        p.text = title
        p.font.bold = True; p.font.size = Pt(28)
        if not is_logo_only:
            p.font.color.rgb = RGBColor(255, 255, 255)
    
    if items:
        txBox = slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(11.3), Inches(5))
        tf = txBox.text_frame
        tf.word_wrap = True
        for idx, (level, text) in enumerate(items):
            p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
            p.text = text
            p.font.size = Pt(22)
            p.level = level

# Generate Presentation
add_bg(prs.slides.add_slide(blank), 'hust-blue-169-intro.png')
add_bg(prs.slides.add_slide(blank), 'hust-blue-169-section.png')
add_title_slide()

add_section_slide("Phần I", "Tổng quan đề tài")
add_content_slide("1. Đặt vấn đề", [
    (0, "Bối cảnh & Nhu cầu:"),
    (1, "- Cần một hệ thống thu thập dữ liệu báo cáo tài chính công khai, chuẩn hóa thành các chỉ tiêu thống nhất."),
    (1, "- Yêu cầu kiểm tra chất lượng và lưu trữ dữ liệu có hỗ trợ truy vấn theo thời điểm lịch sử."),
    (0, "Giải pháp - Hệ thống Financial Data Platform (FDP):"),
    (1, "- Nguồn dữ liệu: SEC Financial Statement Data Sets (doanh nghiệp niêm yết tại Mỹ)."),
    (1, "- Vai trò: Đóng vai trò trung gian giữa nguồn dữ liệu công khai và người sử dụng thông qua giao diện web và API.")
])
add_content_slide("2. Mục tiêu đề tài", [
    (0, "Thu thập -> Chuẩn hóa -> Kiểm tra chất lượng -> Lưu trữ -> Truy vấn -> Khai thác"),
    (0, "Các mục tiêu cụ thể:"),
    (1, "- Thu thập dữ liệu tài chính từ SEC."),
    (1, "- Chuẩn hóa dữ liệu thô thành tập chỉ tiêu tài chính chuẩn hóa (canonical metrics)."),
    (1, "- Kiểm tra và ghi nhận các vấn đề chất lượng dữ liệu."),
    (1, "- Lưu trữ dữ liệu lịch sử, duy trì các phiên bản (restatement)."),
    (1, "- Khai thác: xem xu hướng, so sánh doanh nghiệp và lọc theo điều kiện."),
    (1, "- Cung cấp dữ liệu qua giao diện Web và API.")
])
add_content_slide("3. Đối tượng sử dụng", [
    (0, "Hệ thống hướng tới ba nhóm đối tượng chính:"),
    (0, "1. End User (Người dùng cuối): Sử dụng giao diện web để tìm kiếm, tra cứu và xem thông tin tài chính của doanh nghiệp."),
    (0, "2. API Consumer (Bên tiêu thụ API): Truy cập dữ liệu thông qua API phục vụ các mục đích xử lý hoặc tích hợp vào hệ thống khác."),
    (0, "3. System Operator (Người vận hành): Phụ trách vận hành, theo dõi quá trình thu thập/xử lý dữ liệu, kiểm tra log và kiểm soát hệ thống.")
])

add_section_slide("Phần II", "Phân tích tập dữ liệu SEC")
add_content_slide("Phân tích file sub.txt và num.txt", [
    (0, "sub.txt (Thông tin báo cáo)"),
    (1, "- CIK: Mã nhận diện công ty từ SEC."),
    (1, "- adsh: Khóa chính, mã truy cập hồ sơ."),
    (1, "- sic: Mã ngành nghề kinh doanh."),
    (1, "- form: Loại báo cáo (10-K, 10-Q)."),
    (1, "- fy & fp: Năm và kỳ tài chính."),
    (0, "num.txt (Dữ liệu số liệu)"),
    (1, "- adsh: Khóa ngoại liên kết sub.txt."),
    (1, "- tag: Tên chỉ số (NetIncomeLoss,...)."),
    (1, "- ddate: Ngày chốt sổ."),
    (1, "- qtrs: Thời gian phát sinh (0: 1 thời điểm, 1: 1 quý, 4: 1 năm)."),
    (1, "- value: Giá trị thực tế.")
], True)
add_content_slide("Phân tích file tag.txt và pre.txt", [
    (0, "tag.txt (Danh mục tham chiếu)"),
    (1, "- Định nghĩa cấu trúc cho chỉ số."),
    (1, "- datatype: Kiểu dữ liệu (monetary, shares, pure)."),
    (1, "- crdr: Cờ quy đổi dấu C/D (Credit/Debit)."),
    (1, "- tlabel & doc: Nhãn hiển thị UI và mô tả nghiệp vụ."),
    (0, "pre.txt (Cấu trúc trình bày)"),
    (1, "- Hỗ trợ tái tạo giao diện gốc."),
    (1, "- stmt: Bảng chứa số liệu (BS, IS, CF)."),
    (1, "- line: Thứ tự dòng."),
    (1, "- inpth: Độ thụt lề (cấp bậc khoản mục)."),
    (1, "- negating: Đổi dấu khi hiển thị UI (1: đổi).")
], True)

add_section_slide("Phần III", "Nghiên cứu Case Study")
add_content_slide("Các nền tảng dữ liệu tham khảo (1)", [
    (0, "1. Nasdaq Data Fabric"),
    (1, "- Mô hình: 'Managed pipeline' - quản lý nạp dữ liệu, chất lượng và hạ tầng."),
    (1, "- Đặc điểm: Cung cấp catalog tập trung, phân quyền chi tiết qua một API duy nhất."),
    (1, "-> Ứng dụng data catalog tập trung và phân quyền cơ bản."),
    (0, "2. Polygon.io"),
    (1, "- Dịch vụ: Cung cấp dữ liệu thị trường (stock, crypto, forex)."),
    (1, "- Đặc điểm: API REST versioned rất chuẩn mực (/v1/{resource}/...) và WebSocket."),
    (1, "-> Cấu trúc REST endpoint chuẩn để thiết kế API cho FDP.")
])
add_content_slide("Các nền tảng dữ liệu tham khảo (2)", [
    (0, "3. Economatica"),
    (1, "- Mô hình: Nền tảng phân tích tài chính sâu (40 năm dữ liệu)."),
    (1, "- Tính năng: Screener (lọc đa điều kiện), Comparative matrix (so sánh dữ liệu)."),
    (1, "-> Gợi ý tính năng query lọc và vẽ biểu đồ so sánh."),
    (0, "4. AlphaSense"),
    (1, "- Mô hình: Tìm kiếm bằng AI/NLP trên tài liệu phi cấu trúc (transcript, news)."),
    (1, "-> Khác nhóm bài toán nhưng gợi ý hướng mở rộng AI/Semantic Search trong tương lai.")
])

add_section_slide("Phần IV", "Phạm vi của đề tài")
add_content_slide("1. Phạm vi chức năng", [
    (1, "- Thu thập (Ingestion): Dùng khóa (CIK + adsh), ghi log chi tiết."),
    (1, "- Chuẩn hóa: Ánh xạ về canonical metric theo mức ưu tiên; xử lý theo thời đoạn (qtrs) và dấu (crdr)."),
    (1, "- Kiểm tra chất lượng: Dùng khóa (cik + tag + ddate + qtrs + adsh) phát hiện trùng, gắn cờ lỗi (không xóa)."),
    (1, "- Lưu trữ lịch sử: Báo cáo điều chỉnh lưu song song, không ghi đè; hỗ trợ versioning."),
    (1, "- Truy vấn & Phân tích: Tìm kiếm DN, xem lịch sử/xu hướng, so sánh (2-5 DN), tính chỉ số dẫn xuất."),
    (1, "- Kênh cung cấp: Giao diện Web (Desktop) và REST API.")
], True)
add_content_slide("2. Phạm vi dữ liệu", [
    (0, "Quy mô tham chiếu (SEC Data)"),
    (1, "- Quy mô doanh nghiệp: 30 doanh nghiệp (đa dạng mã ngành - sic)."),
    (1, "- Độ sâu thời gian: Tối thiểu 12 quý dữ liệu lịch sử."),
    (1, "- Dữ liệu chỉ tiêu: Tập canonical metrics xác định trước."),
    (1, "- Dữ liệu thị trường: Bổ sung dữ liệu lịch sử giá cổ phiếu."),
    (0, "Mục tiêu chất lượng dữ liệu"),
    (1, "Đạt tối thiểu 70% coverage (độ phủ) đối với ít nhất 6 canonical metrics.")
], True)

add_bg(prs.slides.add_slide(blank), 'hust-blue-169-end.png')

prs.save('docs/report-docs/Slide_Tongquan.pptx')
