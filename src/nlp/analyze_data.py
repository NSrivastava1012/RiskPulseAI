import pandas as pd
from src.ingestion.news_ingestion import load_news_data
from src.ingestion.social_ingestion import load_social_data
from src.nlp.preprocessing import clean_text
from src.nlp.sentiment import analyze_sentiment


def analyze_news():
    news_df = load_news_data()

    results = []

    for _, row in news_df.iterrows():

        cleaned_text = clean_text(row["text"])
        sentiment = analyze_sentiment(cleaned_text)

        results.append({
            "company": row["company"],
            "source": row["source"],
            "date": row["date"],
            "headline": row["headline"],
            "text": row["text"],
            "sentiment_label": sentiment["label"],
            "sentiment_score": sentiment["score"]
        })

    return pd.DataFrame(results)


def analyze_social():
    social_df = load_social_data()

    results = []

    for _, row in social_df.iterrows():

        cleaned_text = clean_text(row["text"])
        sentiment = analyze_sentiment(cleaned_text)

        results.append({
            "company": row["company"],
            "source": row["source"],
            "date": row["date"],
            "author": row["author"],
            "text": row["text"],
            "sentiment_label": sentiment["label"],
            "sentiment_score": sentiment["score"]
        })

    return pd.DataFrame(results)


if __name__ == "__main__":

    print("Analyzing financial news...\n")

    news_results = analyze_news()

    print(news_results[
        [
            "company",
            "headline",
            "sentiment_label",
            "sentiment_score"
        ]
    ].to_string(index=False))

    print("\n" + "=" * 70)

    print("\nAnalyzing social media...\n")

    social_results = analyze_social()

    print(social_results[
        [
            "company",
            "text",
            "sentiment_label",
            "sentiment_score"
        ]
    ].to_string(index=False))