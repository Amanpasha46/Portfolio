WITH ranked AS (
 SELECT customer_id,treatment,outcome,uplift,NTILE(10) OVER (ORDER BY uplift DESC) AS uplift_decile
 FROM scored_customers
)
SELECT uplift_decile,COUNT(*) AS customers,AVG(uplift) AS avg_predicted_uplift,
 AVG(CASE WHEN treatment=1 THEN outcome END) AS treated_conversion,
 AVG(CASE WHEN treatment=0 THEN outcome END) AS control_conversion
FROM ranked GROUP BY uplift_decile ORDER BY uplift_decile;
