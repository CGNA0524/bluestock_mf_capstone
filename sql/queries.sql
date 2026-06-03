-- Query 1: Top 5 Funds by AUM

SELECT
    f.scheme_name,
    a.aum_crore
FROM fact_aum a
JOIN dim_fund f
    ON a.fund_id = f.fund_id
ORDER BY a.aum_crore DESC
LIMIT 5;

-- Query 2: Average NAV Per Month

SELECT
    d.year,
    d.month,
    ROUND(AVG(n.nav), 2) AS avg_nav
FROM fact_nav n
JOIN dim_date d
    ON n.date_id = d.date_id
GROUP BY
    d.year,
    d.month
ORDER BY
    d.year,
    d.month;

-- Query 3: Transactions By State

SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- Query 4: Funds with Expense Ratio < 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance p
JOIN dim_fund f
    ON p.fund_id = f.fund_id
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- Query 5: Average Sharpe Ratio By Category

SELECT
    f.category,
    ROUND(AVG(p.sharpe_ratio),2) AS avg_sharpe
FROM fact_performance p
JOIN dim_fund f
    ON p.fund_id = f.fund_id
GROUP BY f.category
ORDER BY avg_sharpe DESC;


-- Query 6: Top 5 Funds By 5-Year Return

SELECT
    f.scheme_name,
    p.return_5yr_pct
FROM fact_performance p
JOIN dim_fund f
    ON p.fund_id = f.fund_id
ORDER BY p.return_5yr_pct DESC
LIMIT 5;


-- Query 7: Highest Rated Funds

SELECT
    f.scheme_name,
    p.morningstar_rating
FROM fact_performance p
JOIN dim_fund f
    ON p.fund_id = f.fund_id
ORDER BY p.morningstar_rating DESC;


-- Query 8: Risk Grade Distribution

SELECT
    risk_grade,
    COUNT(*) AS total_funds
FROM fact_performance
GROUP BY risk_grade;


-- Query 9: Transaction Type Distribution

SELECT
    transaction_type,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;


-- Query 10: Average AUM By Category

SELECT
    f.category,
    ROUND(AVG(a.aum_crore),2) AS avg_aum
FROM fact_aum a
JOIN dim_fund f
    ON a.fund_id = f.fund_id
GROUP BY f.category
ORDER BY avg_aum DESC;