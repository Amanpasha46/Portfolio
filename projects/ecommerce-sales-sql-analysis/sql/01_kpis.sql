-- Core e-commerce KPIs

SELECT
    ROUND(SUM(o.quantity * o.unit_price), 2) AS total_revenue,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(DISTINCT o.customer_id) AS unique_customers,
    ROUND(SUM(o.quantity * o.unit_price) / COUNT(DISTINCT o.order_id), 2) AS average_order_value
FROM orders o;

-- Revenue by month
SELECT
    strftime('%Y-%m', order_date) AS month,
    ROUND(SUM(quantity * unit_price), 2) AS revenue,
    COUNT(DISTINCT order_id) AS orders
FROM orders
GROUP BY strftime('%Y-%m', order_date)
ORDER BY month;

-- Revenue by category
SELECT
    p.category,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS revenue,
    SUM(o.quantity) AS units_sold
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;
