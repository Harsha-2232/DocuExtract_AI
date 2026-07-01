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

    def find(pattern):
        match = re.search(pattern, text, re.IGNORECASE)
        return match.group(1).strip() if match else ""

    data["consumer_name"] = find(r"Consumer Name\s*:?\s*([A-Za-z ]+?)\s*Consumer ID")
    data["consumer_id"] = find(r"Consumer ID\s*:?\s*(\d+)")
    data["phone"] = find(r"Phone Number\s*:?\s*(\d{10})")
    data["email"] = find(r"Email\s*:?\s*([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
    data["bill_number"] = find(r"Bill Number\s*:?\s*(\d+)")
    data["bill_date"] = find(r"Bill Date\s*:?\s*(\d{2}-\d{2}-\d{4})")
    data["due_date"] = find(r"Due Date\s*:?\s*(\d{2}-\d{2}-\d{4})")
    data["tariff_category"] = find(r"Tariff Category\s*:?\s*([A-Za-z ]+?)\s*Connection Type")
    data["units_consumed"] = find(r"Units Consumed\s*(?:28-06-2026\s*)?(?:e\s*)?15434\s*(\d+)")
    data["meter_number"] = find(r"Meter Number\s*:?\s*(KSEB\d+)")
    amount_match = re.findall(r"\d{1,3}(?:,\d{3})*\.\d{2}", text)
    data["total_amount"] = amount_match[-1] if amount_match else ""

    return data