import pandas as pd
import numpy as np
from pathlib import Path

DATA = Path('data/processed')

# Load all datasets
funds = pd.read_csv(DATA / 'fund_master_clean.csv')
nav = pd.read_csv(DATA / 'nav_history_clean.csv')
perf = pd.read_csv(DATA / 'scheme_performance_clean.csv')
tx = pd.read_csv(DATA / 'investor_transactions_clean.csv')
aum = pd.read_csv(DATA / 'aum_by_fund_house_clean.csv')
sip = pd.read_csv(DATA / 'monthly_sip_inflows_clean.csv')
holdings = pd.read_csv(DATA / 'portfolio_holdings_clean.csv')
cat_inflow = pd.read_csv(DATA / 'category_inflows_clean.csv')
folio = pd.read_csv(DATA / 'industry_folio_count_clean.csv')

# Convert dates
nav["date"] = pd.to_datetime(nav["date"])
aum["date"] = pd.to_datetime(aum["date"])
sip["month"] = pd.to_datetime(sip["month"])
cat_inflow["month"] = pd.to_datetime(cat_inflow["month"])
folio["month"] = pd.to_datetime(folio["month"])

print('=' * 80)
print('COMPREHENSIVE PROJECT DATA EXTRACTION FOR REPORT UPDATE')
print('=' * 80)

# 1. BASIC DATASET METRICS
print('\n1. DATASET SIZES:')
total_records = len(funds) + len(nav) + len(perf) + len(tx) + len(aum) + len(sip) + len(holdings)
print(f'Fund Master: {len(funds)} | NAV: {len(nav)} | Perf: {len(perf)} | Tx: {len(tx)} | AUM: {len(aum)} | SIP: {len(sip)} | Holdings: {len(holdings)}')
print(f'TOTAL RECORDS: {total_records}')

# 2. CATEGORIES
print('\n2. FUND CATEGORIES:')
cat_dist = funds['category'].value_counts()
for cat, count in cat_dist.items():
    pct = (count / len(funds)) * 100
    print(f'  {cat}: {count} ({pct:.1f}%)')

# 3. FUND HOUSES
print('\n3. TOP FUND HOUSES:')
fh_dist = funds['fund_house'].value_counts()
for fh, count in fh_dist.items():
    pct = (count / len(funds)) * 100
    print(f'  {fh}: {count} ({pct:.1f}%)')

# 4. AGE GROUPS
print('\n4. INVESTOR AGE GROUPS:')
age_dist = tx['age_group'].value_counts().sort_index()
for age, count in age_dist.items():
    pct = (count / len(tx)) * 100
    print(f'  {age}: {count:,} ({pct:.1f}%)')

# 5. GENDER
print('\n5. INVESTOR GENDER:')
gen_dist = tx['gender'].value_counts()
for gen, count in gen_dist.items():
    pct = (count / len(tx)) * 100
    print(f'  {gen}: {count:,} ({pct:.1f}%)')

# 6. CITY TIER
print('\n6. CITY TIER DISTRIBUTION:')
tier_dist = tx['city_tier'].value_counts()
for tier, count in tier_dist.items():
    pct = (count / len(tx)) * 100
    print(f'  {tier}: {count:,} ({pct:.1f}%)')

# 7. TRANSACTION TYPES
print('\n7. TRANSACTION TYPE:')
tt_dist = tx['transaction_type'].value_counts()
for tt, count in tt_dist.items():
    pct = (count / len(tx)) * 100
    print(f'  {tt}: {count:,} ({pct:.1f}%)')

# 8. KYC STATUS
print('\n8. KYC STATUS:')
kyc_dist = tx['kyc_status'].value_counts()
for kyc, count in kyc_dist.items():
    pct = (count / len(tx)) * 100
    print(f'  {kyc}: {count:,} ({pct:.1f}%)')

# 9. STATES
print('\n9. TOP 10 STATES BY INVESTMENT:')
state_inv = tx.groupby('state')['amount_inr'].sum().sort_values(ascending=False).head(10)
for state, amt in state_inv.items():
    print(f'  {state}: ₹{amt:,.0f}')
print(f'Total States: {tx["state"].nunique()}')

# 10. GEOGRAPHIC COVERAGE
print('\n10. GEOGRAPHIC METRICS:')
print(f'  Total States: {tx["state"].nunique()}')
print(f'  Total Cities: {tx["city"].nunique()}')
print(f'  Unique Investors: {tx["investor_id"].nunique():,}')

# 11. NAV DATE RANGE
print('\n11. NAV TIME PERIOD:')
print(f'  Start: {nav["date"].min().date()}')
print(f'  End: {nav["date"].max().date()}')
print(f'  Duration: {(nav["date"].max() - nav["date"].min()).days} days (~{(nav["date"].max() - nav["date"].min()).days / 365:.1f} years)')

# 12. PERFORMANCE METRICS
print('\n12. PERFORMANCE METRICS RANGES:')
print(f'  1Y Return: {perf["return_1yr_pct"].min():.2f}% to {perf["return_1yr_pct"].max():.2f}%')
print(f'  3Y Return: {perf["return_3yr_pct"].min():.2f}% to {perf["return_3yr_pct"].max():.2f}%')
print(f'  5Y Return: {perf["return_5yr_pct"].min():.2f}% to {perf["return_5yr_pct"].max():.2f}%')
print(f'  Sharpe Ratio: {perf["sharpe_ratio"].min():.2f} to {perf["sharpe_ratio"].max():.2f}')
print(f'  Sortino Ratio: {perf["sortino_ratio"].min():.2f} to {perf["sortino_ratio"].max():.2f}')
print(f'  Alpha: {perf["alpha"].min():.2f}% to {perf["alpha"].max():.2f}%')
print(f'  Beta: {perf["beta"].min():.2f} to {perf["beta"].max():.2f}')
print(f'  Volatility: {perf["std_dev_ann_pct"].min():.2f}% to {perf["std_dev_ann_pct"].max():.2f}%')
print(f'  Max Drawdown: {perf["max_drawdown_pct"].min():.2f}% to {perf["max_drawdown_pct"].max():.2f}%')
print(f'  Expense Ratio: {perf["expense_ratio_pct"].min():.2f}% to {perf["expense_ratio_pct"].max():.2f}%')

# 13. SIP METRICS
print('\n13. SIP INFLOW METRICS:')
print(f'  Min: ₹{sip["sip_inflow_crore"].min():,.0f} Cr')
print(f'  Max: ₹{sip["sip_inflow_crore"].max():,.0f} Cr')
print(f'  Mean: ₹{sip["sip_inflow_crore"].mean():,.0f} Cr')
print(f'  Start (Jan 2022): ₹{sip.iloc[0]["sip_inflow_crore"]:,.0f} Cr')
print(f'  End (Dec 2025): ₹{sip.iloc[-1]["sip_inflow_crore"]:,.0f} Cr')
sip_growth = ((sip.iloc[-1]["sip_inflow_crore"] / sip.iloc[0]["sip_inflow_crore"]) - 1) * 100
print(f'  Growth Rate: {sip_growth:.1f}%')

# 14. TRANSACTION AMOUNT
print('\n14. TRANSACTION AMOUNT METRICS:')
print(f'  Min: ₹{tx["amount_inr"].min():,.0f}')
print(f'  Max: ₹{tx["amount_inr"].max():,.0f}')
print(f'  Mean: ₹{tx["amount_inr"].mean():,.0f}')
print(f'  Median: ₹{tx["amount_inr"].median():,.0f}')

# 15. AUM BY FUND HOUSE
print('\n15. AUM BY FUND HOUSE (Latest):')
latest_aum = aum.sort_values('date').drop_duplicates('fund_house', keep='last')
latest_aum = latest_aum.sort_values('aum_crore', ascending=False)
for idx, row in latest_aum.head(5).iterrows():
    print(f'  {row["fund_house"]}: ₹{row["aum_lakh_crore"]:.2f}T (₹{row["aum_crore"]:,.0f} Cr)')

# 16. FOLIO COUNT
print('\n16. INDUSTRY FOLIO COUNT:')
print(f'  Start (Jan 2022): {folio.iloc[0]["total_folios_crore"]:.2f} Cr')
print(f'  End (Dec 2025): {folio.iloc[-1]["total_folios_crore"]:.2f} Cr')
folio_growth = ((folio.iloc[-1]["total_folios_crore"] / folio.iloc[0]["total_folios_crore"]) - 1) * 100
print(f'  Growth: {folio_growth:.1f}%')

# 17. PORTFOLIO SECTORS
print('\n17. TOP SECTORS IN HOLDINGS:')
sector_alloc = holdings.groupby('sector')['weight_pct'].sum().sort_values(ascending=False)
for sector, weight in sector_alloc.head(10).items():
    print(f'  {sector}: {weight:.2f}%')

# 18. TOP FUNDS BY SHARPE
print('\n18. TOP 5 FUNDS BY SHARPE RATIO:')
top_sharpe = perf.nlargest(5, 'sharpe_ratio')[['scheme_name', 'sharpe_ratio', 'return_5yr_pct', 'aum_crore']]
for idx, row in top_sharpe.iterrows():
    print(f'  {row["scheme_name"]}: {row["sharpe_ratio"]:.2f} | 5Y Return: {row["return_5yr_pct"]:.2f}% | AUM: ₹{row["aum_crore"]:,.0f} Cr')

# 19. CATEGORY INFLOW TREND
print('\n19. CATEGORY BREAKDOWN (LATEST):')
latest_cat = cat_inflow.sort_values('month').drop_duplicates('category', keep='last')
for idx, row in latest_cat.iterrows():
    print(f'  {row["category"]}: ₹{row["net_inflow_crore"]:,.0f} Cr')

# 20. INCOME DISTRIBUTION
print('\n20. INVESTOR INCOME DISTRIBUTION:')
income_avg = tx.groupby('annual_income_lakh')['amount_inr'].agg(['count', 'mean']).sort_index(ascending=False)
print(income_avg.to_string())
