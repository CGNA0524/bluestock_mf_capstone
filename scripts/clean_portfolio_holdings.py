import pandas as pd
from pathlib import Path

# Load file
file_path = Path("data/raw/09_portfolio_holdings.csv")
df = pd.read_csv(file_path)

before_rows = len(df)

# Remove duplicates
df = df.drop_duplicates()

# Remove rows with missing AMFI code
df = df[df["amfi_code"].notna()]

# Convert portfolio date
df["portfolio_date"] = pd.to_datetime(
    df["portfolio_date"],
    errors="coerce"
)

# Numeric columns
numeric_cols = [
    "weight_pct",
    "market_value_cr",
    "current_price_inr"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Trim spaces
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = df[col].str.strip()

# Basic validation
df = df[df["weight_pct"] >= 0]

after_rows = len(df)

# Save cleaned file
output_path = Path(
    "data/processed/portfolio_holdings_clean.csv"
)

df.to_csv(output_path, index=False)

print("Portfolio Holdings Cleaning Complete")
print("Before:", before_rows)
print("After :", after_rows)