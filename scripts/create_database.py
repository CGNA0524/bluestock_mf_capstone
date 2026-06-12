"""
Build Analytics SQLite Database.
This script creates dimensional and fact tables from cleaned mutual fund datasets.
Input sources: data/processed/*_clean.csv files used for funds, NAV, transactions, and performance.
Output generated: data/db/bluestock_mf.db.
"""

import pandas as pd
from sqlalchemy import create_engine

# =========================
# DATABASE CONNECTION
# =========================

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

# =========================
# LOAD FILES
# =========================

funds = pd.read_csv(
    "data/processed/fund_master_clean.csv"
)

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

tx = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

perf = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

# =========================
# CREATE dim_fund
# =========================

dim_fund = funds[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "plan"
    ]
].drop_duplicates()

dim_fund = dim_fund.reset_index(
    drop=True
)

dim_fund["fund_id"] = (
    dim_fund.index + 1
)

dim_fund = dim_fund[
    [
        "fund_id",
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "plan"
    ]
]

# =========================
# CREATE dim_date
# =========================

nav_dates = pd.to_datetime(
    nav["date"]
)

tx_dates = pd.to_datetime(
    tx["transaction_date"]
)

all_dates = pd.concat(
    [
        nav_dates,
        tx_dates
    ]
).drop_duplicates()

dim_date = pd.DataFrame(
    {
        "full_date": sorted(all_dates)
    }
)

dim_date = dim_date.reset_index(
    drop=True
)

dim_date["date_id"] = (
    dim_date.index + 1
)

dim_date["year"] = (
    dim_date["full_date"]
    .dt.year
)

dim_date["quarter"] = (
    dim_date["full_date"]
    .dt.quarter
)

dim_date["month"] = (
    dim_date["full_date"]
    .dt.month
)

dim_date["day"] = (
    dim_date["full_date"]
    .dt.day
)

dim_date = dim_date[
    [
        "date_id",
        "full_date",
        "year",
        "quarter",
        "month",
        "day"
    ]
]

# =========================
# FUND LOOKUP
# =========================

fund_lookup = dict(
    zip(
        dim_fund["amfi_code"],
        dim_fund["fund_id"]
    )
)

# =========================
# DATE LOOKUP
# =========================

date_lookup = dict(
    zip(
        pd.to_datetime(
            dim_date["full_date"]
        ),
        dim_date["date_id"]
    )
)

# =========================
# FACT NAV
# =========================

nav["date"] = pd.to_datetime(
    nav["date"]
)

fact_nav = pd.DataFrame()

fact_nav["fund_id"] = (
    nav["amfi_code"]
    .map(fund_lookup)
)

fact_nav["date_id"] = (
    nav["date"]
    .map(date_lookup)
)

fact_nav["nav"] = nav["nav"]

# =========================
# FACT TRANSACTIONS
# =========================

tx["transaction_date"] = (
    pd.to_datetime(
        tx["transaction_date"]
    )
)

fact_transactions = tx.copy()

fact_transactions["fund_id"] = (
    fact_transactions["amfi_code"]
    .map(fund_lookup)
)

fact_transactions["date_id"] = (
    fact_transactions[
        "transaction_date"
    ].map(date_lookup)
)

fact_transactions = (
    fact_transactions.drop(
        columns=[
            "amfi_code",
            "transaction_date"
        ]
    )
)

# =========================
# FACT PERFORMANCE
# =========================

fact_performance = perf.copy()

fact_performance["fund_id"] = (
    fact_performance["amfi_code"]
    .map(fund_lookup)
)

fact_performance = (
    fact_performance.drop(
        columns=[
            "amfi_code",
            "scheme_name",
            "fund_house",
            "category",
            "plan",
            "aum_crore"
        ]
    )
)

# =========================
# FACT AUM
# =========================

fact_aum = pd.DataFrame()

fact_aum["fund_id"] = (
    perf["amfi_code"]
    .map(fund_lookup)
)

fact_aum["aum_crore"] = (
    perf["aum_crore"]
)

# =========================
# LOAD TABLES
# =========================

dim_fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

dim_date.to_sql(
    "dim_date",
    engine,
    if_exists="replace",
    index=False
)

fact_nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

fact_transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

fact_performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

fact_aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

# =========================
# VALIDATION
# =========================

print("\nDatabase Created Successfully\n")

print(
    "dim_fund:",
    len(dim_fund)
)

print(
    "dim_date:",
    len(dim_date)
)

print(
    "fact_nav:",
    len(fact_nav)
)

print(
    "fact_transactions:",
    len(fact_transactions)
)

print(
    "fact_performance:",
    len(fact_performance)
)

print(
    "fact_aum:",
    len(fact_aum)
)