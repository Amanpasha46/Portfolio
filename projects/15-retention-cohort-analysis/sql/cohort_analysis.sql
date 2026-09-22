-- Customer retention cohort analysis
-- Adapt table/column names to the selected public transaction dataset.

WITH first_purchase AS (
    SELECT
        customer_id,
        DATE_TRUNC('month', MIN(order_date)) AS cohort_month
    FROM transactions
    WHERE customer_id IS NOT NULL
    GROUP BY customer_id
), monthly_activity AS (
    SELECT
        t.customer_id,
        DATE_TRUNC('month', t.order_date) AS order_month,
        fp.cohort_month
    FROM transactions t
    JOIN first_purchase fp USING (customer_id)
), cohort_counts AS (
    SELECT
        cohort_month,
        order_month,
        COUNT(DISTINCT customer_id) AS active_customers
    FROM monthly_activity
    GROUP BY cohort_month, order_month
)
SELECT
    cohort_month,
    order_month,
    active_customers,
    ROUND(
        100.0 * active_customers /
        FIRST_VALUE(active_customers) OVER (
            PARTITION BY cohort_month ORDER BY order_month
        ), 2
    ) AS retention_pct
FROM cohort_counts
ORDER BY cohort_month, order_month;
