-- Fraud / anomaly monitoring starter queries

-- 1. Daily transaction volume and value
SELECT
    CAST(timestamp AS DATE) AS transaction_date,
    COUNT(*) AS transaction_count,
    SUM(amount) AS transaction_value
FROM transactions
GROUP BY CAST(timestamp AS DATE)
ORDER BY transaction_date;

-- 2. High-value transaction monitoring
SELECT *
FROM transactions
WHERE amount >= 10000
ORDER BY amount DESC;

-- 3. Transaction activity by hour
SELECT
    EXTRACT(HOUR FROM timestamp) AS transaction_hour,
    COUNT(*) AS transaction_count,
    AVG(amount) AS average_amount
FROM transactions
GROUP BY EXTRACT(HOUR FROM timestamp)
ORDER BY transaction_hour;
