"""
Inspect Raw Data Ingestion Inputs.
This script profiles each raw CSV by shape, data types, and sample records.
Input source: all CSV files under data/raw/.
Output generated: no file; ingestion diagnostics are printed to the terminal.
"""

import pandas as pd
import os

folder_path = "data/raw"

files = os.listdir(folder_path)

for file in files:
    if file.endswith(".csv"):
        print("="*50)
        print("File:", file)

        df = pd.read_csv(os.path.join(folder_path, file))

        print("Shape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\n")