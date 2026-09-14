-- Adapt table and column names to the selected dataset.
-- Example event-level funnel counts.
SELECT
  COUNT(DISTINCT CASE WHEN event_type = 'visit' THEN session_id END) AS visits,
  COUNT(DISTINCT CASE WHEN event_type = 'product_view' THEN session_id END) AS product_views,
  COUNT(DISTINCT CASE WHEN event_type = 'add_to_cart' THEN session_id END) AS add_to_carts,
  COUNT(DISTINCT CASE WHEN event_type = 'checkout' THEN session_id END) AS checkouts,
  COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN session_id END) AS purchases
FROM web_events;

-- Conversion rate from visits to purchases.
SELECT
  1.0 * COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN session_id END)
  / NULLIF(COUNT(DISTINCT CASE WHEN event_type = 'visit' THEN session_id END), 0) AS purchase_conversion_rate
FROM web_events;
