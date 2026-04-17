import pdfplumber
import pytesseract
from PIL import Image
import re
import io


# ✅ FIXED PDF FUNCTION
def extract_text_from_pdf(file):
    text = ""

    # Convert uploaded file to BytesIO
    with pdfplumber.open(io.BytesIO(file.read())) as pdf:
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"

    return text


# ✅ IMAGE OCR
def extract_text_from_image(file):
    image = Image.open(file)
    text = pytesseract.image_to_string(image)
    return text


# ✅ SIMPLE PARSER
def parse_data(text):
    lines = text.split("\n")
    data = []

    for line in lines:
        line = line.strip()

        # Simple flexible pattern
        parts = line.split()

        if len(parts) >= 4:
            data.append({
                "Raw Line": line
            })

    return data
