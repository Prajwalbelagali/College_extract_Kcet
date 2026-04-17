import pandas as pd


def save_to_csv(df, output_file):
    df.to_csv(output_file, index=False)
    print(f"CSV saved as {output_file}")
