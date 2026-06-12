"""
Analyze Fund Master Snapshot.
This script provides quick exploratory statistics for fund houses, categories, and risk groups.
Input source: data/raw/01_fund_master.csv.
Output generated: no file; analysis summary is printed to the terminal.
"""

import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\nTotal Records:")
print(len(df))

print("\nColumns:")
print(df.columns)

print("\nUnique Fund Houses:")
print(df["fund_house"].nunique())

print("\nFund Houses:")
print(df["fund_house"].unique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nRisk Categories:")
print(df["risk_category"].unique())