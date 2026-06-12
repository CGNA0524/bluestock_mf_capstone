"""
Clean NAV History Dataset.
This script sorts, deduplicates, and validates scheme-level NAV time series records.
Input source: data/raw/02_nav_history.csv.
Output generated: data/processed/nav_history_clean.csv.
"""

import pandas as pd
from pathlib import Path

nav = pd.read_csv("data/raw/02_nav_history.csv")

print("Before:", len(nav))

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav = nav.drop_duplicates()

nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

nav = nav[
    nav["nav"] > 0
]

print("After:", len(nav))

nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("Done")