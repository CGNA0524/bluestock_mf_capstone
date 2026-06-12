# Bluestock Mutual Fund Capstone

## Project Overview

This project is a mutual fund analytics pipeline built around AMFI and market datasets. It ingests raw CSV files, cleans and standardizes them, builds a SQLite analytics database, generates research reports, and powers a Power BI dashboard for fund, SIP, investor, and industry-level analysis.

The repository is organized as a full data workflow:
- `data/raw/` holds the source datasets and live NAV extracts.
- `data/processed/` stores cleaned CSVs used for analysis and database loading.
- `scripts/` contains the cleaning and database build scripts.
- `sql/` contains the schema and example analytical queries.
- `reports/` contains derived analysis outputs and scorecards.
- `dashboard/` contains the Power BI dashboard file and exported visuals.

## Repository Structure

```text
amfi_validation.py        # Validates AMFI codes across raw datasets
data_ingestion.py         # Quick inspection of raw CSV files
fund_master_analysis.py   # Basic exploratory summary of fund master data
live_nav_fetch.py         # Downloads live NAV data from the MF API
scripts/                  # Cleaning and database creation scripts
sql/                      # SQLite schema and sample queries
reports/                  # Analysis outputs and derived metrics
dashboard/                # Power BI dashboard assets
data/raw/                 # Raw input CSVs and downloaded NAV files
data/processed/           # Cleaned CSV outputs
data/db/                  # SQLite database output
```

## Setup

### 1. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, allow scripts for the current session first:

```powershell
Set-ExecutionPolicy -Scope Process RemoteSigned
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

The project uses common Python data libraries such as `pandas`, `requests`, and `sqlalchemy`.

## How To Run The ETL

The project’s ETL is script-based. Run the steps in this order from the repository root:

### 1. Inspect or validate source data

```powershell
python data_ingestion.py
python amfi_validation.py
python fund_master_analysis.py
```

These scripts help confirm the raw data is present and that AMFI codes align across the main source files.

### 2. Download live NAV files, if needed

```powershell
python live_nav_fetch.py
```

This fetches live NAV history for the tracked schemes and writes the files into `data/raw/`.

### 3. Clean the raw datasets

Run the cleaning scripts in `scripts/` to generate the processed CSV files in `data/processed/`.

Typical order:

```powershell
python scripts\clean_fund_master.py
python scripts\clean_nav_history.py
python scripts\clean_aum_by_fund_house.py
python scripts\clean_monthly_sip_inflows.py
python scripts\clean_category_inflows.py
python scripts\clean_industry_folio_count.py
python scripts\clean_performance.py
python scripts\clean_transactions.py
python scripts\clean_portfolio_holdings.py
python scripts\clean_benchmark_indices.py
```

After this step, the cleaned files should exist in `data/processed/`.

### 4. Build the SQLite database

```powershell
python scripts\create_database.py
```

This creates `data/db/bluestock_mf.db` with the following tables:
- `dim_fund`
- `dim_date`
- `fact_nav`
- `fact_transactions`
- `fact_performance`
- `fact_aum`

### 5. Use the SQL assets

You can inspect `sql/schema.sql` for the table definitions and `sql/queries.sql` for example analytics queries such as top funds by AUM, average NAV by month, transactions by state, and category-level performance views.

## How To Open The Dashboard

The dashboard is a Power BI dashboard, not a web app.

1. Open `dashboard/bluestock_mf.pbix` in Power BI Desktop.
2. Refresh the data if required so it points to the latest processed files or SQLite database.
3. Review the included pages and visuals such as:
   - Fund performance
   - Industry overview
   - Investor analytics
   - SIP market trends

The folder also includes exported visuals and a PDF export for quick review:
- `dashboard/Dashboard.pdf`
- `dashboard/Fund_Performance.png`
- `dashboard/Industry_Overview.png`
- `dashboard/Investor_Analytics.png`
- `dashboard/SIP_Market_Trends.png`

## Datasets

### Raw Inputs

The raw datasets are stored in `data/raw/`.

- `01_fund_master.csv` - scheme master data with AMFI code, fund house, category, launch date, benchmark, expense ratio, exit load, minimum investment, fund manager, and risk classification.
- `02_nav_history.csv` - historical NAV records by scheme and date.
- `03_aum_by_fund_house.csv` - assets under management by AMC over time.
- `04_monthly_sip_inflows.csv` - monthly SIP inflows, active accounts, new accounts, SIP AUM, and growth.
- `05_category_inflows.csv` - net inflows by fund category.
- `06_industry_folio_count.csv` - industry folio counts by category.
- `07_scheme_performance.csv` - scheme return and risk metrics such as alpha, beta, Sharpe ratio, Sortino ratio, drawdown, and ratings.
- `08_investor_transactions.csv` - investor transaction-level data with demographic and payment information.
- `09_portfolio_holdings.csv` - portfolio disclosure holdings with stock weights and market values.
- `10_benchmark_indices.csv` - benchmark index close values over time.
- `*_nav.csv` files - live NAV extracts downloaded from MF API for selected schemes.

### Cleaned Outputs

The cleaned datasets are stored in `data/processed/` and are the primary inputs for analysis and database creation.

- `fund_master_clean.csv`
- `nav_history_clean.csv`
- `aum_by_fund_house_clean.csv`
- `monthly_sip_inflows_clean.csv`
- `category_inflows_clean.csv`
- `industry_folio_count_clean.csv`
- `scheme_performance_clean.csv`
- `investor_transactions_clean.csv`
- `portfolio_holdings_clean.csv`
- `benchmark_indices_clean.csv`

### Analysis Reports

The `reports/` folder contains derived analytics and scorecards, including:
- `fund_scorecard.csv`
- `sharpe_ratio_rankings.csv`
- `sortino_ratio_rankings.csv`
- `tracking_error.csv`
- `max_drawdown.csv`
- `alpha_beta.csv`
- `var_cvar_report.csv`
- `sip_continuity_report.csv`
- `cohort_analysis.csv`
- `cohort_top_fund.csv`
- `hhi_concentration.csv`
- `data_quality_summary.txt`
- `data_dictionary.md`

## Notes

- Run all commands from the repository root so relative paths resolve correctly.
- The SQLite database is generated from the processed CSV files, so the cleaning scripts should be run before `create_database.py`.
- The project is designed for analysis in Python and Power BI rather than as a hosted web application.

## Project Deliverables

### D1 – ETL Pipeline
- Python ETL and cleaning scripts

### D2 – SQLite Database
- bluestock_mf.db
- schema.sql

### D3 – Exploratory Data Analysis
- 03_eda_analysis.ipynb

### D4 – Performance Analytics
- 04_performance_analytics.ipynb
- Performance metric reports

### D5 – Interactive Dashboard
- bluestock_mf.pbix
- Dashboard.pdf

### D6 – Advanced Analytics
- 05_advanced_analytics.ipynb
- VaR/CVaR
- Cohort Analysis
- SIP Continuity Analysis
- HHI Analysis
- Fund Recommender

### D7 – Final Report & Presentation
- Final_Report.pdf
- Bluestock_MF_Presentation.pptx

## Key Results

- Analyzed 40 mutual fund schemes
- Built SQLite analytics database
- Generated performance and risk metrics
- Computed Historical VaR and CVaR
- Developed Rolling Sharpe Ratio analytics
- Built investor cohort and SIP continuity models
- Created Power BI dashboard with 5 pages

## Author

Chirag Nagra

Data Analyst Internship Project
Bluestock Mutual Fund Analytics Capstone