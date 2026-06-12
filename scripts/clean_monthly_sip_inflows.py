"""
Clean Monthly SIP Inflows Dataset.
This script formats SIP monthly metrics and enforces numeric consistency for analysis.
Input source: data/raw/04_monthly_sip_inflows.csv.
Output generated: data/processed/monthly_sip_inflows_clean.csv.
"""

import pandas as pd
from pathlib import Path

# Load file
file_path = Path("data/raw/04_monthly_sip_inflows.csv")
df = pd.read_csv(file_path)

before_rows = len(df)

# Remove duplicates
df = df.drop_duplicates()

# Convert month column
df["month"] = pd.to_datetime(
    df["month"],
    errors="coerce"
)

# Numeric columns
numeric_cols = [
    "sip_inflow_crore",
    "active_sip_accounts_crore",
    "new_sip_accounts_lakh",
    "sip_aum_lakh_crore",
    "yoy_growth_pct"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Remove spaces from text columns
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = df[col].str.strip()

# Basic validation
df = df[df["sip_inflow_crore"] >= 0]

after_rows = len(df)

# Save cleaned file
output_path = Path(
    "data/processed/monthly_sip_inflows_clean.csv"
)

df.to_csv(output_path, index=False)

print("Monthly SIP Cleaning Complete")
print("Before:", before_rows)
print("After :", after_rows)