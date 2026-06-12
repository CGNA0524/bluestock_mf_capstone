"""
Generate Risk-Based Fund Recommendations.
This script filters schemes by user-selected risk appetite and ranks by Sharpe ratio.
Input source: ../data/processed/scheme_performance_clean.csv and console risk input.
Output generated: no file; top recommendations are printed to the terminal.
"""

import pandas as pd

funds = pd.read_csv(
    "../data/processed/scheme_performance_clean.csv"
)

risk = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

risk_map = {
    "Low": ["Low"],
    "Moderate": ["Moderate"],
    "High": ["High"]
}

filtered = funds[
    funds["risk_grade"].isin(
        risk_map[risk]
    )
]

top3 = (
    filtered.sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print("\nRecommended Funds:\n")

print(
    top3[
        [
            "scheme_name",
            "fund_house",
            "sharpe_ratio"
        ]
    ]
)