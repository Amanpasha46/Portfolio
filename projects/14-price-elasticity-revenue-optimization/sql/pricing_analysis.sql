-- Project 14: Price Elasticity & Revenue Optimization

-- Revenue by product
SELECT
    product_id,
    SUM(quantity) AS units_sold,
    SUM(price * quantity) AS revenue,
    AVG(price) AS avg_price
FROM sales
GROUP BY product_id
ORDER BY revenue DESC;

-- Monthly price and demand relationship
SELECT
    product_id,
    DATE_TRUNC('month', sale_date) AS month,
    AVG(price) AS avg_price,
    SUM(quantity) AS units_sold,
    SUM(price * quantity) AS revenue
FROM sales
GROUP BY product_id, DATE_TRUNC('month', sale_date)
ORDER BY product_id, month;
