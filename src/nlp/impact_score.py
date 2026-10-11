EVENT_SEVERITY = {
    "Geopolitical": 10,
    "Macroeconomic": 9,
    "Credit Event": 9,
    "Regulatory": 8,
    "M&A": 7,
    "Earnings": 6,
    "Management Change": 5,
    "Product Launch": 4,
    "Other": 2
}


SOURCE_WEIGHT = {
    "Reuters": 1.0,
    "Bloomberg": 1.0,
    "Financial Times": 1.0,
    "X": 0.85
}


def calculate_impact_score(sentiment_score, event_type, source):
    """
    Calculate an impact score from 1 to 10.

    Factors:
    - Sentiment severity
    - Event severity
    - Source credibility/weight
    """

    # Get event severity
    event_score = EVENT_SEVERITY.get(event_type, 2)

    # Absolute sentiment represents severity regardless
    # of whether sentiment is positive or negative.
    sentiment_severity = abs(sentiment_score)

    # Combine event severity and sentiment severity
    raw_score = (
        (event_score * 0.70)
        + (sentiment_severity * 10 * 0.30)
    )

    # Apply source weighting
    source_weight = SOURCE_WEIGHT.get(source, 0.80)

    adjusted_score = raw_score * source_weight

    # Keep score within 1-10
    impact_score = max(1, min(10, round(adjusted_score)))

    # Determine risk level
    if impact_score <= 3:
        risk_level = "Low"
    elif impact_score <= 6:
        risk_level = "Medium"
    elif impact_score <= 8:
        risk_level = "High"
    else:
        risk_level = "Critical"

    return {
        "impact_score": impact_score,
        "risk_level": risk_level
    }


if __name__ == "__main__":

    test_cases = [
        {
            "company": "Alpha Motors",
            "sentiment": -0.9530,
            "event": "Geopolitical",
            "source": "Reuters"
        },
        {
            "company": "Gamma Tech",
            "sentiment": 0.4440,
            "event": "Product Launch",
            "source": "Bloomberg"
        },
        {
            "company": "Delta Bank",
            "sentiment": -0.2027,
            "event": "Credit Event",
            "source": "Reuters"
        },
        {
            "company": "Epsilon Pharma",
            "sentiment": 0.9312,
            "event": "Regulatory",
            "source": "Reuters"
        }
    ]

    for case in test_cases:

        result = calculate_impact_score(
            case["sentiment"],
            case["event"],
            case["source"]
        )

        print("\nCompany:", case["company"])
        print("Sentiment:", case["sentiment"])
        print("Event:", case["event"])
        print("Source:", case["source"])
        print("Impact Score:", result["impact_score"])
        print("Risk Level:", result["risk_level"])