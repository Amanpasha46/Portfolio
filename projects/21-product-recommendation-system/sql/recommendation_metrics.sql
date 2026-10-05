-- Recommendation monitoring examples
SELECT customer_id, COUNT(*) AS recommendations, AVG(rank) AS avg_rank
FROM recommendations
GROUP BY customer_id
ORDER BY recommendations DESC;

-- Catalog coverage
SELECT COUNT(DISTINCT product_id) * 1.0 / NULLIF((SELECT COUNT(DISTINCT product_id) FROM products), 0) AS catalog_coverage
FROM recommendations;
