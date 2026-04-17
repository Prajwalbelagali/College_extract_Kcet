import streamlit as st
import pandas as pd
from extractor import extract_text_from_pdf, extract_text_from_image, parse_data

st.title("KCET College Extractor")

uploaded_file = st.file_uploader(
    "Upload PDF or Image",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    try:
        file_type = uploaded_file.type

        if "pdf" in file_type:
            text = extract_text_from_pdf(uploaded_file)
        else:
            text = extract_text_from_image(uploaded_file)

        st.subheader("Extracted Text")
        st.text_area("Preview", text[:1000], height=200)

        data = parse_data(text)

        if data:
            df = pd.DataFrame(data)
            st.dataframe(df)

            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("Download CSV", csv, "data.csv")

        else:
            st.warning("No data extracted")

    except Exception as e:
        st.error(f"Error: {e}")
