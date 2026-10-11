from flask import Flask, jsonify, render_template
import json
import pandas as pd

from src.risk_engine.engine import analyze_risk
from src.portfolio.stress_test import (
    calculate_stress_test,
    get_top_risk_events
)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/api/risk-signals")
def risk_signals():
    df = pd.read_csv("data/risk_signals.csv")

    records = json.loads(
        df.to_json(orient="records")
    )

    return jsonify(records)


@app.route("/api/stress-test")
def stress_test():
    results = calculate_stress_test()

    records = json.loads(
        results.to_json(orient="records")
    )

    return jsonify(records)

@app.route("/api/top-risk-events")
def top_risk_events():

    events = get_top_risk_events()

    records = json.loads(
        events.to_json(orient="records")
    )

    return jsonify(records)

@app.route("/api/summary")
def summary():

    risk_df = pd.read_csv("data/risk_signals.csv")
    stress_df = calculate_stress_test()

    total_portfolio = float(stress_df["value"].sum())
    total_loss = float(stress_df["estimated_loss"].sum())
    stressed_value = float(stress_df["stressed_value"].sum())

    loss_percentage = (
        (total_loss / total_portfolio) * 100
    )

    return jsonify({
        "total_portfolio_value": total_portfolio,
        "estimated_stress_loss": total_loss,
        "stressed_portfolio_value": stressed_value,
        "portfolio_loss_percentage": round(float(loss_percentage), 2),
        "total_risk_signals": int(len(risk_df)),
        "critical_events": int(
            (risk_df["risk_level"] == "Critical").sum()
        ),
        "high_risk_events": int(
            (risk_df["risk_level"] == "High").sum()
        )
    })


if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )