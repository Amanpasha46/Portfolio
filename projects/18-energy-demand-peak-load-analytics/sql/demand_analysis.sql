-- Adapt table and column names to the selected dataset.

SELECT EXTRACT(HOUR FROM timestamp) AS hour_of_day, AVG(demand) AS avg_demand
FROM energy_demand
GROUP BY EXTRACT(HOUR FROM timestamp)
ORDER BY hour_of_day;

SELECT DATE(timestamp) AS demand_date, MAX(demand) AS peak_demand
FROM energy_demand
GROUP BY DATE(timestamp)
ORDER BY peak_demand DESC;

SELECT CASE WHEN EXTRACT(DOW FROM timestamp) IN (0, 6) THEN 'Weekend' ELSE 'Weekday' END AS day_type,
       AVG(demand) AS avg_demand
FROM energy_demand
GROUP BY day_type;
