import pandas as pd
from pathlib import Path


def load_news_data():
    base_dir = Path(__file__).resolve().parents[2]
    file_path = base_dir / "data" / "news_data.csv"

    news_df = pd.read_csv(file_path)

    return news_df


if __name__ == "__main__":
    news_data = load_news_data()

    print("News data loaded successfully!")
    print(f"Number of records: {len(news_data)}")
    print("\nColumns:")
    print(list(news_data.columns))

    print("\nFirst 5 records:")
    print(news_data.head())