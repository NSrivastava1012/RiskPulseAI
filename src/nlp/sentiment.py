from transformers import pipeline


# Load the financial sentiment model
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="ProsusAI/finbert"
)


def analyze_sentiment(text):
    """
    Analyze financial text using FinBERT.

    Returns:
        sentiment label
        sentiment score between -1 and +1
        probabilities for positive, neutral and negative
    """

    if not isinstance(text, str) or not text.strip():
        return {
            "label": "Neutral",
            "score": 0.0,
            "positive": 0.0,
            "neutral": 1.0,
            "negative": 0.0
        }

    # Request probabilities for all three classes
    results = sentiment_pipeline(
        text,
        top_k=None
    )

    probabilities = {
        result["label"].lower(): result["score"]
        for result in results
    }

    positive = probabilities.get("positive", 0.0)
    neutral = probabilities.get("neutral", 0.0)
    negative = probabilities.get("negative", 0.0)

    # Convert probabilities into a -1 to +1 sentiment score
    sentiment_score = positive - negative

    # Determine dominant sentiment
    if positive >= neutral and positive >= negative:
        label = "Positive"
    elif negative >= positive and negative >= neutral:
        label = "Negative"
    else:
        label = "Neutral"

    return {
        "label": label,
        "score": round(sentiment_score, 4),
        "positive": round(positive, 4),
        "neutral": round(neutral, 4),
        "negative": round(negative, 4)
    }


if __name__ == "__main__":

    sample_texts = [
        "Alpha Motors reported better than expected quarterly revenue.",
        "Delta Bank reported a significant increase in loan defaults.",
        "The company announced a routine management meeting."
    ]

    for text in sample_texts:

        result = analyze_sentiment(text)

        print("\nText:")
        print(text)

        print("Sentiment:", result["label"])
        print("Score:", result["score"])
        print("Positive:", result["positive"])
        print("Neutral:", result["neutral"])
        print("Negative:", result["negative"])