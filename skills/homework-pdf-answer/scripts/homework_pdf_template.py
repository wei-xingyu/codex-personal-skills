from pathlib import Path

import fitz
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


def register_chinese_font(name="SimHei"):
    candidates = [
        r"C:\Windows\Fonts\simhei.ttf",
        r"C:\Windows\Fonts\Deng.ttf",
        r"C:\Windows\Fonts\simsun.ttc",
    ]
    for path in candidates:
        if Path(path).exists():
            pdfmetrics.registerFont(TTFont(name, path))
            return name
    raise FileNotFoundError("No Chinese font found. Install or point to SimHei/Deng/Simsun.")


class HomeworkPdf:
    def __init__(self, pdf_path, title, font_name="SimHei"):
        self.pdf_path = Path(pdf_path)
        self.pdf_path.parent.mkdir(parents=True, exist_ok=True)
        self.font = font_name
        self.c = canvas.Canvas(str(self.pdf_path), pagesize=landscape(A4))
        self.c.setTitle(title)
        self.title = title

    def header(self):
        c = self.c
        c.setFillColor(colors.HexColor("#eef2ff"))
        c.rect(36, 552, 770, 36, fill=1, stroke=0)
        self.text(50, 562, self.title, 17)

    def text(self, x, y, s, size=12, color=colors.black):
        self.c.setFillColor(color)
        self.c.setFont(self.font, size)
        self.c.drawString(x, y, s)

    def center(self, x, y, s, size=12):
        self.c.setFillColor(colors.black)
        self.c.setFont(self.font, size)
        self.c.drawCentredString(x, y, s)

    def line(self, x1, y1, x2, y2, arrow=False, dash=False):
        c = self.c
        c.setStrokeColor(colors.HexColor("#111827"))
        c.setLineWidth(1.25)
        c.setDash(5, 4) if dash else c.setDash()
        c.line(x1, y1, x2, y2)
        c.setDash()
        if arrow:
            import math

            a = math.atan2(y2 - y1, x2 - x1)
            length = 7
            for delta in (0.82, -0.82):
                aa = a + 3.14159 * delta
                c.line(x2, y2, x2 + length * math.cos(aa), y2 + length * math.sin(aa))

    def box(self, x, y, w, h, title, rows=None, fill="#ffffff"):
        c = self.c
        c.setFillColor(colors.HexColor(fill))
        c.setStrokeColor(colors.HexColor("#111827"))
        c.roundRect(x, y, w, h, 3, fill=1, stroke=1)
        c.line(x, y + h - 28, x + w, y + h - 28)
        self.center(x + w / 2, y + h - 19, title, 12)
        yy = y + h - 47
        for row in rows or []:
            self.text(x + 8, yy, row, 9)
            yy -= 15

    def code_block(self, x, y, lines, size=10, leading=13, width=730):
        c = self.c
        height = leading * len(lines) + 16
        c.setFillColor(colors.HexColor("#f8fafc"))
        c.roundRect(x - 8, y - height + 8, width, height, 4, fill=1, stroke=0)
        c.setFont(self.font, size)
        c.setFillColor(colors.black)
        yy = y
        for line in lines:
            c.drawString(x, yy, line)
            yy -= leading

    def show_page(self):
        self.c.showPage()

    def save(self):
        self.c.save()


def render_pdf(pdf_path, out_dir, zoom=1.45):
    pdf_path = Path(pdf_path)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    paths = []
    for i, page in enumerate(doc, start=1):
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
        path = out_dir / f"page-{i}.png"
        pix.save(path)
        paths.append(path)
    return paths


if __name__ == "__main__":
    font = register_chinese_font()
    pdf = HomeworkPdf("output/pdf/homework-demo.pdf", "作业答案整理", font)
    pdf.header()
    pdf.text(50, 520, "第 1 题：示例", 16)
    pdf.text(50, 495, "答案：这里填写简短答案。", 12)
    pdf.box(320, 360, 160, 70, "Example", ["+ method()"])
    pdf.save()
    for rendered in render_pdf("output/pdf/homework-demo.pdf", "tmp/pdfs/homework-demo"):
        print(rendered)
