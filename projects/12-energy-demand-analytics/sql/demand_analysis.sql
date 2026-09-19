-- Expected columns: timestamp, demand
SELECT
    EXTRACT(HOUR FROM timestamp) AS hour_of_day,
    AVG(demand) AS avg_demand,
    MAX(demand) AS peak_demand
FROM energy_demand
GROUP BY EXTRACT(HOUR FROM timestamp)
ORDER BY hour_of_day;

-- Daily demand profile
SELECT
    CAST(timestamp AS DATE) AS demand_date,
    AVG(demand) AS avg_demand,
    MAX(demand) AS peak_demand,
    MIN(demand) AS minimum_demand
FROM energy_demand
GROUP BY CAST(timestamp AS DATE)
ORDER BY demand_date;
