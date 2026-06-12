"""
Orchestrate End-to-End ETL Pipeline.
This script executes cleaning modules and database creation in a fixed production sequence.
Input source: script list referencing raw-to-processed transformation modules.
Output generated: refreshed data/processed/*_clean.csv files and data/db/bluestock_mf.db.
"""

import subprocess

scripts = [
    "scripts/clean_fund_master.py",
    "scripts/clean_nav_history.py",
    "scripts/clean_aum_by_fund_house.py",
    "scripts/clean_monthly_sip_inflows.py",
    "scripts/clean_category_inflows.py",
    "scripts/clean_industry_folio_count.py",
    "scripts/clean_performance.py",
    "scripts/clean_transactions.py",
    "scripts/clean_portfolio_holdings.py",
    "scripts/clean_benchmark_indices.py",
    "scripts/create_database.py"
]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python", script], check=True)

print("ETL Pipeline Completed Successfully!")