import pandas as pd


# Estimated price shock based on risk level
RISK_SHOCK = {
    "Low": 0.02,
    "Medium": 0.05,
    "High": 0.10,
    "Critical": 0.20
}


def load_portfolio():
    portfolio_df = pd.read_csv("data/portfolio.csv")
    return portfolio_df


def load_risk_signals():
    risk_df = pd.read_csv("data/risk_signals.csv")
    return risk_df


def calculate_stress_test():
    portfolio = load_portfolio()
    risk_signals = load_risk_signals()

    # Aggregate risk by company
    company_risk = (
        risk_signals
        .groupby("company")
        .agg(
            average_impact=("impact_score", "mean"),
            maximum_impact=("impact_score", "max"),
            risk_events=("impact_score", "count")
        )
        .reset_index()
    )

    # Determine overall risk level using maximum impact
    def get_risk_level(score):
        if score <= 3:
            return "Low"
        elif score <= 6:
            return "Medium"
        elif score <= 8:
            return "High"
        else:
            return "Critical"

    company_risk["risk_level"] = company_risk["maximum_impact"].apply(
        get_risk_level
    )

    # Calculate estimated stress loss
    company_risk["shock_rate"] = company_risk["risk_level"].map(
        RISK_SHOCK
    )

    # Merge portfolio exposure with company risk
    stress_results = portfolio.merge(
        company_risk,
        on="company",
        how="left"
    )

    # Companies without risk signals
    stress_results["shock_rate"] = stress_results["shock_rate"].fillna(0)

    stress_results["estimated_loss"] = (
        stress_results["value"] * stress_results["shock_rate"]
    )

    stress_results["stressed_value"] = (
        stress_results["value"] - stress_results["estimated_loss"]
    )

    return stress_results

def get_top_risk_events():
    risk_signals = load_risk_signals()

    # Sort by highest impact first
    top_events = (
        risk_signals
        .sort_values(
            by=["company", "impact_score"],
            ascending=[True, False]
        )
        .groupby("company")
        .first()
        .reset_index()
    )

    return top_events


if __name__ == "__main__":

    print("Running portfolio stress test...")
    print("=" * 80)

    results = calculate_stress_test()

    display_columns = [
        "company",
        "asset_type",
        "value",
        "risk_level",
        "maximum_impact",
        "shock_rate",
        "estimated_loss",
        "stressed_value"
    ]

    print(results[display_columns].to_string(index=False))

    total_portfolio = results["value"].sum()
    total_loss = results["estimated_loss"].sum()
    stressed_portfolio = results["stressed_value"].sum()

    loss_percentage = (total_loss / total_portfolio) * 100

    print("\n" + "=" * 80)
    print(f"Original Portfolio Value : ${total_portfolio:,.2f}")
    print(f"Estimated Stress Loss    : ${total_loss:,.2f}")
    print(f"Stressed Portfolio Value : ${stressed_portfolio:,.2f}")
    print(f"Portfolio Loss           : {loss_percentage:.2f}%")

    # Save results
    results.to_csv(
        "data/stress_test_results.csv",
        index=False
    )

    print("\nStress test results saved to: data/stress_test_results.csv")