import pdfplumber
import pytesseract
import cv2
from PIL import Image
import pandas as pd
import re


def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text


def parse_data(text):
    """
    Customize regex based on document format
    Example pattern:
    College Name | CET Code | Branch | District
    """
    data = []

    pattern = re.findall(
        r"([A-Za-z\s]+)\s+(\d{4})\s+([A-Za-z\s]+)\s+([A-Za-z\s]+)",
        text
    )

    for match in pattern:
        college, cet_code, branch, district = match
        data.append({
            "College Name": college.strip(),
            "CET Code": cet_code.strip(),
            "Branch": branch.strip(),
            "District": district.strip()
        })

    return pd.DataFrame(data)
