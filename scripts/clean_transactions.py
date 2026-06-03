import pandas as pd

tx = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("Before:", len(tx))

# Convert Date
tx["transaction_date"] = pd.to_datetime(
    tx["transaction_date"]
)

# Standardize transaction type
tx["transaction_type"] = (
    tx["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Amount validation
tx = tx[
    tx["amount_inr"] > 0
]

# KYC validation
valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

tx = tx[
    tx["kyc_status"].isin(valid_kyc)
]

print("After:", len(tx))

tx.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Transaction Cleaning Complete")