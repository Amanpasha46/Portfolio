-- Expected alert table: asset_id, timestamp, anomaly_score, anomaly_flag, severity

SELECT DATE(timestamp) AS alert_date, COUNT(*) AS flagged_readings, COUNT(DISTINCT asset_id) AS affected_assets
FROM equipment_anomaly_alerts
WHERE anomaly_flag = 1
GROUP BY DATE(timestamp)
ORDER BY alert_date;

SELECT asset_id, COUNT(*) AS alert_count, MAX(anomaly_score) AS peak_anomaly_score, AVG(anomaly_score) AS avg_anomaly_score
FROM equipment_anomaly_alerts
WHERE anomaly_flag = 1
GROUP BY asset_id
ORDER BY peak_anomaly_score DESC, alert_count DESC;
