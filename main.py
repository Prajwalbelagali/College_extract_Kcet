from extractor import extract_text_from_pdf, extract_text_from_image, parse_data
from utils import save_to_csv
import sys


def main():
    file_path = input("Enter file path (PDF/Image): ")

    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        text = extract_text_from_image(file_path)

    df = parse_data(text)

    if df.empty:
        print("No data extracted. Please check format or regex.")
    else:
        print(df.head())
        save_to_csv(df, "output.csv")


if __name__ == "__main__":
    main()
