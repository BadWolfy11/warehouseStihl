from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from io import BytesIO
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def generate_pdf(documents, total):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    p.setFont('Arial', 12)
    
    p.drawString(100, height - 50, "Документы")
    p.drawString(100, height - 70, f"Всего документов: {total}")

    y = height - 100
    for doc in documents:
        p.drawString(100, y, f"ID: {doc['id']}, Название: {doc['name']}, Дата: {doc['data']}")
        y -= 20

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer