import pandas as pd

from src.ingestion.news_ingestion import load_news_data
from src.ingestion.social_ingestion import load_social_data
from src.risk_engine.engine import analyze_risk


def analyze_news():
    news_df = load_news_data()

    results = []

    for _, row in news_df.iterrows():

        risk_result = analyze_risk(
            row["text"],
            row["source"]
        )

        risk_result["company"] = row["company"]
        risk_result["date"] = row["date"]
        risk_result["data_source"] = "Financial News"
        risk_result["headline"] = row["headline"]

        results.append(risk_result)

    return pd.DataFrame(results)


def analyze_social():
    social_df = load_social_data()

    results = []

    for _, row in social_df.iterrows():

        risk_result = analyze_risk(
            row["text"],
            row["source"]
        )

        risk_result["company"] = row["company"]
        risk_result["date"] = row["date"]
        risk_result["data_source"] = "Social Media"
        risk_result["author"] = row["author"]

        results.append(risk_result)

    return pd.DataFrame(results)


if __name__ == "__main__":
    print("Running RiskPulseAI on financial news...")

    news_results = analyze_news()

    print("\nNEWS RESULTS")
    print("=" * 80)
    print(
        news_results[
            ["company", "event_type", "sentiment_score", "impact_score", "risk_level"]
        ].to_string(index=False)
    )

    print("\nRunning RiskPulseAI on social media...")

    social_results = analyze_social()

    print("\nSOCIAL MEDIA RESULTS")
    print("=" * 80)
    print(
        social_results[
            ["company", "event_type", "sentiment_score", "impact_score", "risk_level"]
        ].to_string(index=False)
    )

    # Combine both datasets
    combined_results = pd.concat(
        [news_results, social_results],
        ignore_index=True
    )

    # Save results
    output_path = "data/risk_signals.csv"
    combined_results.to_csv(output_path, index=False)

    print("\n" + "=" * 80)
    print("Risk analysis completed successfully!")
    print(f"Total records analyzed: {len(combined_results)}")
    print(f"Results saved to: {output_path}")