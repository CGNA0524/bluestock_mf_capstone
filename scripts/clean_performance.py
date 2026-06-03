import pandas as pd

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("Before:", len(perf))

perf = perf.drop_duplicates()

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Expense Ratio Validation
perf = perf[
    (perf["expense_ratio_pct"] >= 0.1)
    &
    (perf["expense_ratio_pct"] <= 2.5)
]

print("After:", len(perf))

perf.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Performance Cleaning Complete")