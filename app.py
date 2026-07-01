import streamlit as st
import pandas as pd
from extractor import (
    extract_from_pdf,
    extract_from_image,
    extract_from_txt,
    clean_text,
    extract_fields
)

st.set_page_config(page_title="DocuExtract AI", layout="wide")

st.title("DocuExtract AI")
st.write("AI Powered Document Extraction System")

uploaded_file = st.file_uploader(
    "Upload PDF, Image, or Text File",
    type=["pdf", "png", "jpg", "jpeg", "txt"]
)

if uploaded_file is not None:
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        raw_text = extract_from_pdf(uploaded_file)

    elif file_name.endswith((".png", ".jpg", ".jpeg")):
        raw_text = extract_from_image(uploaded_file)

    elif file_name.endswith(".txt"):
        raw_text = extract_from_txt(uploaded_file)

    else:
        st.error("Unsupported file type")
        raw_text = ""

    if raw_text:
        cleaned_text = clean_text(raw_text)
        extracted_data = extract_fields(cleaned_text)

        st.subheader("Raw Extracted Text")
        st.text_area("Text", cleaned_text, height=250)

        st.subheader("Structured Extracted Data")
        st.json(extracted_data)

        df = pd.DataFrame([extracted_data])

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "Download CSV",
            csv,
            "extracted_data.csv",
            "text/csv"
        )
    else:
        st.warning("No text extracted from this file.")