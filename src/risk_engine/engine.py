from src.nlp.preprocessing import clean_text
from src.nlp.sentiment import analyze_sentiment
from src.nlp.event_classifier import classify_event
from src.nlp.impact_score import calculate_impact_score


def analyze_risk(text, source):
    """
    Run the complete RiskPulseAI pipeline on one piece of text.
    """

    # Step 1: Clean text
    cleaned_text = clean_text(text)

    # Step 2: Sentiment analysis
    sentiment = analyze_sentiment(cleaned_text)

    # Step 3: Event classification
    event = classify_event(cleaned_text)

    # Step 4: Impact scoring
    impact = calculate_impact_score(
        sentiment["score"],
        event["event_type"],
        source
    )

    # Step 5: Combine everything
    result = {
        "text": text,
        "source": source,
        "sentiment_label": sentiment["label"],
        "sentiment_score": sentiment["score"],
        "event_type": event["event_type"],
        "event_evidence": event["matched_keywords"],
        "impact_score": impact["impact_score"],
        "risk_level": impact["risk_level"]
    }

    return result


if __name__ == "__main__":

    test_text = (
        "Alpha Motors faces geopolitical supply chain disruption."
    )

    result = analyze_risk(
        test_text,
        "Reuters"
    )

    print("\nRiskPulseAI Result")
    print("=" * 50)

    for key, value in result.items():
        print(f"{key}: {value}")