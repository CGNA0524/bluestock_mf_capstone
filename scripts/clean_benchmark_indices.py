import pandas as pd
from pathlib import Path

# Load file
file_path = Path("data/raw/10_benchmark_indices.csv")
df = pd.read_csv(file_path)

before_rows = len(df)

# Remove duplicates
df = df.drop_duplicates()

# Convert date
df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

# Convert close value
df["close_value"] = pd.to_numeric(
    df["close_value"],
    errors="coerce"
)

# Trim spaces
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = df[col].str.strip()

# Basic validation
df = df[df["close_value"] > 0]

after_rows = len(df)

# Save cleaned file
output_path = Path(
    "data/processed/benchmark_indices_clean.csv"
)

df.to_csv(output_path, index=False)

print("Benchmark Indices Cleaning Complete")
print("Before:", before_rows)
print("After :", after_rows)