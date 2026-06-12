"""
Clean AUM by Fund House Dataset.
This script prepares AMC-level AUM records through type normalization and quality checks.
Input source: data/raw/03_aum_by_fund_house.csv.
Output generated: data/processed/aum_by_fund_house_clean.csv.
"""

import pandas as pd
from pathlib import Path

# Load file
file_path = Path("data/raw/03_aum_by_fund_house.csv")
df = pd.read_csv(file_path)

before_rows = len(df)

# Remove duplicates
df = df.drop_duplicates()

# Convert date
df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

# Numeric columns
numeric_cols = [
    "aum_lakh_crore",
    "aum_crore",
    "num_schemes"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Remove leading/trailing spaces
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = df[col].str.strip()

# Basic validation
df = df[df["aum_crore"] >= 0]

after_rows = len(df)

# Save cleaned file
output_path = Path(
    "data/processed/aum_by_fund_house_clean.csv"
)

df.to_csv(output_path, index=False)

print("AUM Cleaning Complete")
print("Before:", before_rows)
print("After :", after_rows)