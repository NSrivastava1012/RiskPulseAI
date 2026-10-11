from src.nlp.event_classifier import classify_event
from src.nlp.impact_score import calculate_impact_score
from src.risk_engine.engine import analyze_risk


def test_geopolitical_event():
    result = classify_event(
        "Geopolitical tensions may disrupt the international supply chain."
    )

    assert result["event_type"] == "Geopolitical"


def test_critical_impact():
    result = calculate_impact_score(
        -0.953,
        "Geopolitical",
        "Reuters"
    )

    assert result["impact_score"] == 10
    assert result["risk_level"] == "Critical"


def test_risk_engine():
    result = analyze_risk(
        "Alpha Motors warned that geopolitical tensions could disrupt its international supply chain.",
        "Reuters"
    )

    assert result["event_type"] == "Geopolitical"
    assert result["sentiment_label"] == "Negative"
    assert result["impact_score"] == 10
    assert result["risk_level"] == "Critical"