import re


EVENT_KEYWORDS = {
    "Geopolitical": [
        "geopolitical",
        "war",
        "conflict",
        "sanction",
        "supply chain",
        "international tension",
        "trade war"
    ],

    "Macroeconomic": [
        "interest rate",
        "interest rates",
        "inflation",
        "central bank",
        "gdp",
        "recession",
        "economic growth",
        "monetary policy"
    ],

    "Credit Event": [
        "loan default",
        "loan defaults",
        "debt default",
        "credit downgrade",
        "credit risk",
        "bankruptcy",
        "rising defaults"
    ],

    "M&A": [
        "merger",
        "acquisition",
        "acquire",
        "takeover",
        "merger and acquisition"
    ],

    "Product Launch": [
        "launch",
        "launches",
        "launched",
        "new product",
        "new platform",
        "ai platform",
        "product release"
    ],

    "Regulatory": [
        "regulatory",
        "regulator",
        "regulators",
        "investigation",
        "compliance",
        "approval",
        "government regulation"
    ],

    "Earnings": [
        "revenue",
        "earnings",
        "quarterly results",
        "quarterly revenue",
        "profit",
        "loss",
        "forecast",
        "revenue forecast"
    ],

    "Management Change": [
        "new ceo",
        "new cfo",
        "appointed ceo",
        "appointed cfo",
        "management change",
        "executive resignation",
        "resigned"
    ]
}


def classify_event(text):
    """
    Classify financial text into an event category.

    Returns:
        event_type
        matched_keywords
    """

    if not isinstance(text, str) or not text.strip():
        return {
            "event_type": "Other",
            "matched_keywords": []
        }

    text_lower = text.lower()

    matched_events = []

    for event_type, keywords in EVENT_KEYWORDS.items():

        matched_keywords = []

        for keyword in keywords:

            # Match phrases/words while avoiding partial word matches
            pattern = r"\b" + re.escape(keyword) + r"\b"

            if re.search(pattern, text_lower):
                matched_keywords.append(keyword)

        if matched_keywords:
            matched_events.append(
                (event_type, matched_keywords)
            )

    # No event detected
    if not matched_events:
        return {
            "event_type": "Other",
            "matched_keywords": []
        }

    # Select the event with the most matching keywords
    best_event = max(
        matched_events,
        key=lambda item: len(item[1])
    )

    return {
        "event_type": best_event[0],
        "matched_keywords": best_event[1]
    }


if __name__ == "__main__":

    test_texts = [
        "Alpha Motors faces geopolitical supply chain disruption.",
        "The central bank raises interest rates.",
        "Delta Bank reports rising loan defaults.",
        "Gamma Tech launches a new AI platform.",
        "Regulators announced an investigation into the company.",
        "The company reported strong quarterly revenue."
    ]

    for text in test_texts:

        result = classify_event(text)

        print("\nText:")
        print(text)

        print("Event:", result["event_type"])
        print("Matched keywords:", result["matched_keywords"])