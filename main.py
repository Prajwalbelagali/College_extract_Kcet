import streamlit as st
import pandas as pd
from extractor import extract_text_from_pdf, extract_text_from_image, parse_data

st.set_page_config(page_title="KCET College Extractor")

st.title("📊 KCET College Data Extractor")

uploaded_file = st.file_uploader(
    "Upload PDF or Image",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file:
    file_type = uploaded_file.type

    with st.spinner("Extracting text..."):
        if "pdf" in file_type:
            text = extract_text_from_pdf(uploaded_file)
        else:
            text = extract_text_from_image(uploaded_file)

    st.subheader("📄 Extracted Text Preview")
    st.text_area("Text", text[:2000], height=200)

    st.subheader("🔍 Parsed Data")

    data = parse_data(text)

    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇ Download CSV",
            csv,
            "kcet_colleges.csv",
            "text/csv"
        )
    else:
        st.warning("No structured data found!")
