import pandas as pd
from pathlib import Path

# Load file
file_path = Path("data/raw/06_industry_folio_count.csv")
df = pd.read_csv(file_path)

before_rows = len(df)

# Remove duplicates
df = df.drop_duplicates()

# Convert month
df["month"] = pd.to_datetime(
    df["month"],
    errors="coerce"
)

# Numeric columns
numeric_cols = [
    "total_folios_crore",
    "equity_folios_crore",
    "debt_folios_crore",
    "hybrid_folios_crore",
    "others_folios_crore"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Basic validation
df = df[df["total_folios_crore"] >= 0]

after_rows = len(df)

# Save cleaned file
output_path = Path(
    "data/processed/industry_folio_count_clean.csv"
)

df.to_csv(output_path, index=False)

print("Industry Folio Cleaning Complete")
print("Before:", before_rows)
print("After :", after_rows)