-- Top products using a window function
WITH product_sales AS (
    SELECT
        p.product_id,
        p.product_name,
        p.category,
        SUM(o.quantity * o.unit_price) AS revenue
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY p.product_id, p.product_name, p.category
), ranked AS (
    SELECT *,
           DENSE_RANK() OVER (ORDER BY revenue DESC) AS revenue_rank
    FROM product_sales
)
SELECT product_id, product_name, category,
       ROUND(revenue, 2) AS revenue,
       revenue_rank
FROM ranked
WHERE revenue_rank <= 10
ORDER BY revenue_rank;

-- Customer lifetime revenue and repeat-customer flag
WITH customer_orders AS (
    SELECT
        c.customer_id,
        c.customer_name,
        c.region,
        COUNT(DISTINCT o.order_id) AS order_count,
        SUM(o.quantity * o.unit_price) AS revenue
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.customer_name, c.region
)
SELECT
    customer_id,
    customer_name,
    region,
    order_count,
    ROUND(revenue, 2) AS lifetime_revenue,
    CASE WHEN order_count > 1 THEN 'Repeat' ELSE 'One-time' END AS customer_type
FROM customer_orders
ORDER BY lifetime_revenue DESC;

-- Regional performance
SELECT
    c.region,
    COUNT(DISTINCT o.order_id) AS orders,
    COUNT(DISTINCT o.customer_id) AS customers,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS revenue,
    ROUND(SUM(o.quantity * o.unit_price) / COUNT(DISTINCT o.order_id), 2) AS aov
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.region
ORDER BY revenue DESC;
