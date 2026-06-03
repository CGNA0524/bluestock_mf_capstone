# Data Dictionary – Bluestock Mutual Fund Capstone

## Overview

This document describes the datasets used in the Bluestock Mutual Fund Analytics Capstone Project, including column definitions, data types, business meanings, and source references.

---

# 01_fund_master.csv

| Column             | Data Type | Description                   |
| ------------------ | --------- | ----------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme identifier |
| fund_house         | Text      | Asset Management Company name |
| scheme_name        | Text      | Mutual fund scheme name       |
| category           | Text      | Fund category                 |
| sub_category       | Text      | Fund sub-category             |
| plan               | Text      | Direct/Regular plan           |
| launch_date        | Date      | Scheme launch date            |
| benchmark          | Text      | Benchmark index               |
| expense_ratio_pct  | Float     | Expense ratio percentage      |
| exit_load_pct      | Float     | Exit load percentage          |
| min_sip_amount     | Float     | Minimum SIP investment        |
| min_lumpsum_amount | Float     | Minimum lump-sum investment   |
| fund_manager       | Text      | Fund manager name             |
| risk_category      | Text      | Risk classification           |
| sebi_category_code | Text      | SEBI category code            |

Source: AMFI India

---

# 02_nav_history.csv

| Column    | Data Type | Description       |
| --------- | --------- | ----------------- |
| amfi_code | Integer   | Scheme identifier |
| date      | Date      | NAV date          |
| nav       | Float     | Net Asset Value   |

Source: MFAPI / AMFI

---

# 03_aum_by_fund_house.csv

| Column         | Data Type | Description       |
| -------------- | --------- | ----------------- |
| date           | Date      | Reporting date    |
| fund_house     | Text      | AMC name          |
| aum_lakh_crore | Float     | AUM in lakh crore |
| aum_crore      | Float     | AUM in crore      |
| num_schemes    | Integer   | Number of schemes |

Source: AMFI Industry Reports

---

# 04_monthly_sip_inflows.csv

| Column                    | Data Type | Description                      |
| ------------------------- | --------- | -------------------------------- |
| month                     | Date      | Reporting month                  |
| sip_inflow_crore          | Float     | Monthly SIP inflows              |
| active_sip_accounts_crore | Float     | Active SIP accounts              |
| new_sip_accounts_lakh     | Float     | New SIP accounts                 |
| sip_aum_lakh_crore        | Float     | SIP assets under management      |
| yoy_growth_pct            | Float     | Year-over-year growth percentage |

Source: AMFI Monthly Reports

---

# 05_category_inflows.csv

| Column           | Data Type | Description       |
| ---------------- | --------- | ----------------- |
| month            | Date      | Reporting month   |
| category         | Text      | Fund category     |
| net_inflow_crore | Float     | Net inflow amount |

Source: AMFI Monthly Reports

---

# 06_industry_folio_count.csv

| Column              | Data Type | Description           |
| ------------------- | --------- | --------------------- |
| month               | Date      | Reporting month       |
| total_folios_crore  | Float     | Total industry folios |
| equity_folios_crore | Float     | Equity folios         |
| debt_folios_crore   | Float     | Debt folios           |
| hybrid_folios_crore | Float     | Hybrid folios         |
| others_folios_crore | Float     | Other folios          |

Source: AMFI Industry Statistics

---

# 07_scheme_performance.csv

| Column             | Data Type | Description             |
| ------------------ | --------- | ----------------------- |
| amfi_code          | Integer   | Scheme identifier       |
| scheme_name        | Text      | Fund scheme             |
| fund_house         | Text      | AMC name                |
| category           | Text      | Fund category           |
| plan               | Text      | Plan type               |
| return_1yr_pct     | Float     | 1-year return           |
| return_3yr_pct     | Float     | 3-year return           |
| return_5yr_pct     | Float     | 5-year return           |
| benchmark_3yr_pct  | Float     | Benchmark return        |
| alpha              | Float     | Alpha metric            |
| beta               | Float     | Beta metric             |
| sharpe_ratio       | Float     | Sharpe ratio            |
| sortino_ratio      | Float     | Sortino ratio           |
| std_dev_ann_pct    | Float     | Annualised volatility   |
| max_drawdown_pct   | Float     | Maximum drawdown        |
| aum_crore          | Float     | Assets under management |
| expense_ratio_pct  | Float     | Expense ratio           |
| morningstar_rating | Integer   | Morningstar rating      |
| risk_grade         | Text      | Risk grade              |

Source: Value Research / Morningstar / AMFI

---

# 08_investor_transactions.csv

| Column             | Data Type | Description                |
| ------------------ | --------- | -------------------------- |
| investor_id        | Text      | Unique investor identifier |
| transaction_date   | Date      | Transaction date           |
| amfi_code          | Integer   | Scheme identifier          |
| transaction_type   | Text      | SIP, Lumpsum, Redemption   |
| amount_inr         | Float     | Transaction amount         |
| state              | Text      | Investor state             |
| city               | Text      | Investor city              |
| city_tier          | Text      | Tier 1 / Tier 2 / Tier 3   |
| age_group          | Text      | Investor age bucket        |
| gender             | Text      | Investor gender            |
| annual_income_lakh | Float     | Annual income              |
| payment_mode       | Text      | Payment method             |
| kyc_status         | Text      | KYC completion status      |

Source: Simulated Investor Dataset

---

# 09_portfolio_holdings.csv

| Column            | Data Type | Description               |
| ----------------- | --------- | ------------------------- |
| amfi_code         | Integer   | Scheme identifier         |
| stock_symbol      | Text      | Stock ticker              |
| stock_name        | Text      | Company name              |
| sector            | Text      | Industry sector           |
| weight_pct        | Float     | Portfolio weight          |
| market_value_cr   | Float     | Market value in crore     |
| current_price_inr | Float     | Current stock price       |
| portfolio_date    | Date      | Portfolio disclosure date |

Source: Fund Portfolio Disclosures

---

# 10_benchmark_indices.csv

| Column      | Data Type | Description          |
| ----------- | --------- | -------------------- |
| date        | Date      | Trading date         |
| index_name  | Text      | Benchmark index name |
| close_value | Float     | Index closing value  |

Source: NSE / BSE Benchmark Data
