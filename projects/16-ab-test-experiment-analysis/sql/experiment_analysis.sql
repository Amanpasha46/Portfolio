-- A/B test KPI queries
-- Expected columns: user_id, experiment_group, converted, device, country, traffic_source

SELECT
    experiment_group,
    COUNT(DISTINCT user_id) AS users,
    SUM(converted) AS conversions,
    AVG(converted) AS conversion_rate
FROM experiment_users
GROUP BY experiment_group;

SELECT
    device,
    experiment_group,
    COUNT(DISTINCT user_id) AS users,
    AVG(converted) AS conversion_rate
FROM experiment_users
GROUP BY device, experiment_group
ORDER BY device, experiment_group;
