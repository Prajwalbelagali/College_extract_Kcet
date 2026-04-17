import pdfplumber
import pytesseract
from PIL import Image
import re
import numpy as np

# Safe import for OpenCV
try:
    import cv2
except ImportError:
    cv2 = None


# -------- PDF TEXT EXTRACTION --------
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


# -------- IMAGE TEXT EXTRACTION --------
def extract_text_from_image(file):
    image = Image.open(file)

    if cv2:
        img = np.array(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
    else:
        text = pytesseract.image_to_string(image)

    return text


# -------- DATA PARSING --------
def parse_data(text):
    lines = text.split("\n")
    data = []

    for line in lines:
        line = line.strip()

        # Example pattern:
        # College Name - Branch - CET Code - District
        match = re.match(r"(.+?)\s+([A-Z]{2,})\s+(\d{3,5})\s+(.+)", line)

        if match:
            college = match.group(1)
            branch = match.group(2)
            code = match.group(3)
            district = match.group(4)

            data.append({
                "College": college,
                "Branch": branch,
                "CET Code": code,
                "District": district
            })

    return data
