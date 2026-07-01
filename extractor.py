import pdfplumber
import pytesseract
from PIL import Image
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_from_pdf(file):
    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


def extract_from_image(file):
    image = Image.open(file)
    text = pytesseract.image_to_string(image)
    return text


def extract_from_txt(file):
    text = file.read().decode("utf-8")
    return text


def clean_text(text):
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_fields(text):
    data = {}

    email = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    phone = re.findall(r"\b[6-9]\d{9}\b", text)
    amount = re.findall(r"(?:₹|Rs\.?|INR)\s?\d+[,\d]*", text)
    date = re.findall(r"\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b", text)
    invoice = re.findall(r"(?:Invoice No|Invoice Number|INV)[\s:.-]*[A-Za-z0-9-]+", text, re.I)

    data["email"] = email[0] if email else ""
    data["phone"] = phone[0] if phone else ""
    data["amount"] = amount[0] if amount else ""
    data["date"] = date[0] if date else ""
    data["invoice_number"] = invoice[0] if invoice else ""

    return data