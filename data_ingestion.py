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