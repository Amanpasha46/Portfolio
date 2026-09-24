-- Generic SQL checks to adapt to your dataset

-- 1. Row count
SELECT COUNT(*) AS row_count
FROM transactions;

-- 2. Missing customer IDs
SELECT COUNT(*) AS missing_customer_id
FROM transactions
WHERE customer_id IS NULL;

-- 3. Duplicate transaction IDs
SELECT transaction_id, COUNT(*) AS duplicate_count
FROM transactions
GROUP BY transaction_id
HAVING COUNT(*) > 1;

-- 4. Invalid transaction amounts
SELECT COUNT(*) AS invalid_amounts
FROM transactions
WHERE amount < 0;

-- 5. Daily volume monitoring
SELECT CAST(transaction_date AS DATE) AS transaction_day,
       COUNT(*) AS row_count
FROM transactions
GROUP BY CAST(transaction_date AS DATE)
ORDER BY transaction_day;
