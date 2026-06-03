import pandas as pd
from pathlib import Path

# Load data
file_path = Path("data/raw/01_fund_master.csv")
df = pd.read_csv(file_path)

before_rows = len(df)

# Remove duplicates
df = df.drop_duplicates()

# Remove rows with missing AMFI code
df = df[df["amfi_code"].notna()]

# Convert launch date
df["launch_date"] = pd.to_datetime(
    df["launch_date"],
    errors="coerce"
)

# Numeric columns
numeric_cols = [
    "expense_ratio_pct",
    "exit_load_pct",
    "min_sip_amount",
    "min_lumpsum_amount"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Trim text columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

after_rows = len(df)

# Save cleaned file
output_path = Path(
    "data/processed/fund_master_clean.csv"
)

df.to_csv(output_path, index=False)

print("Fund Master Cleaning Complete")
print("Before:", before_rows)
print("After :", after_rows)