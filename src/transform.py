# Placeholder for transformation logic
import pandas as pd

def clean_claims_data(input_path, output_path):
    """ Reads raw data, cleans column names,
    and saves the cleaned file """
    df = pd.read_csv(input_path)

    df.columns = (
        df.columns.str.lower()
        .str.replace(' ','_')
        .str.replace(r'[^\w_]','', regex=True)
    )

    df.to_csv(output_path, index=False)

    print(f"Data cleaned and saved to {output_path}")

if __name__ == '__main__':
    clean_claims_data(
        input_path="../raw_data/claims_raw.csv",
        output_path="../output/claims_cleaned.csv"
    )