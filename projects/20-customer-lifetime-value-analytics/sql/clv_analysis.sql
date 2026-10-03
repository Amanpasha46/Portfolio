-- Customer Lifetime Value analytics
-- Adapt table/column names to the documented dataset used.

-- Historical customer value
SELECT
    customer_id,
    COUNT(DISTINCT order_id) AS order_count,
    SUM(quantity * unit_price) AS historical_revenue,
    AVG(quantity * unit_price) AS average_order_value,
    MAX(transaction_date) AS last_purchase_date
FROM transactions
GROUP BY customer_id
ORDER BY historical_revenue DESC;

-- Value by acquisition channel
SELECT
    acquisition_channel,
    COUNT(DISTINCT customer_id) AS customers,
    SUM(quantity * unit_price) AS revenue,
    AVG(quantity * unit_price) AS average_order_value
FROM transactions
GROUP BY acquisition_channel
ORDER BY revenue DESC;

-- Monthly customer revenue trend
SELECT
    DATE_TRUNC('month', transaction_date) AS month,
    COUNT(DISTINCT customer_id) AS active_customers,
    SUM(quantity * unit_price) AS revenue
FROM transactions
GROUP BY 1
ORDER BY 1;
