# 📄 DocuExtract AI

An AI-powered Document Extraction System built with Python and Streamlit.

## Features

- Upload PDF
- Upload Images (JPG, PNG)
- Upload TXT files
- OCR using Tesseract
- PDF Text Extraction
- Structured Data Extraction
- JSON Output
- CSV Export

## Tech Stack

- Python
- Streamlit
- PDFPlumber
- PyTesseract
- Pillow
- Pandas

## Project Workflow

Upload File
↓

Detect File Type
↓

Extract Text
↓

Clean Text
↓

Structured Data Extraction
↓

Display JSON
↓

Download CSV

## Installation

```bash
git clone https://github.com/yourusername/DocuExtract_AI.git

cd DocuExtract_AI

pip install -r requirements.txt

streamlit run app.py
```

## Future Improvements

- EasyOCR
- PaddleOCR
- LLM Extraction
- Resume Parser
- Invoice Parser
- Aadhaar Parser
- Multi-language OCR
