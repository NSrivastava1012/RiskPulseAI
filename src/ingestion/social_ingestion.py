import pandas as pd
from pathlib import Path


def load_social_data():
    base_dir = Path(__file__).resolve().parents[2]
    file_path = base_dir / "data" / "social_data.csv"

    social_df = pd.read_csv(file_path)

    return social_df


if __name__ == "__main__":
    social_data = load_social_data()

    print("Social media data loaded successfully!")
    print(f"Number of records: {len(social_data)}")

    print("\nColumns:")
    print(list(social_data.columns))

    print("\nFirst 5 records:")
    print(social_data.head())