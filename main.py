import streamlit as st
import pandas as pd
from extractor import extract_text_from_pdf, extract_text_from_image

st.set_page_config(page_title="KCET Extractor")

st.title("KCET College Extractor")

uploaded_file = st.file_uploader(
    "Upload PDF or Image",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    try:
        file_bytes = uploaded_file.read()

        # Detect file type safely
        if uploaded_file.name.lower().endswith(".pdf"):
            text = extract_text_from_pdf(file_bytes)
        else:
            text = extract_text_from_image(file_bytes)

        if not text:
            st.error("No text extracted from file.")
        else:
            st.subheader("Extracted Text")
            st.text_area("Preview", text[:1500], height=250)

            # Simple output (no parsing crash)
            df = pd.DataFrame({"Extracted Text": text.split("\n")})
            st.dataframe(df)

            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("Download CSV", csv, "output.csv")

    except Exception as e:
        st.error(f"App crashed: {e}")
