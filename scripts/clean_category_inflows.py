import pandas as pd
from pathlib import Path

# Load file
file_path = Path("data/raw/05_category_inflows.csv")
df = pd.read_csv(file_path)

before_rows = len(df)

# Remove duplicates
df = df.drop_duplicates()

# Convert month column
df["month"] = pd.to_datetime(
    df["month"],
    errors="coerce"
)

# Convert inflow column to numeric
df["net_inflow_crore"] = pd.to_numeric(
    df["net_inflow_crore"],
    errors="coerce"
)

# Trim spaces
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = df[col].str.strip()

after_rows = len(df)

# Save cleaned file
output_path = Path(
    "data/processed/category_inflows_clean.csv"
)

df.to_csv(output_path, index=False)

print("Category Inflows Cleaning Complete")
print("Before:", before_rows)
print("After :", after_rows)