# IoT Equipment Anomaly Monitoring

## Project Goal
Build an analytics and data-science pipeline that detects unusual equipment sensor behavior and turns those signals into maintenance priorities.

## Business Problem
Operations teams often discover equipment problems after downtime occurs. This project uses temperature, vibration, pressure, runtime, and power-consumption signals to identify abnormal behavior early and prioritize assets for inspection.

## Implementation Plan
1. Ingest timestamped sensor readings.
2. Validate timestamps, ranges, missingness, and duplicate readings.
3. Engineer rolling mean, rolling standard deviation, rate-of-change, and utilization features.
4. Create a transparent baseline using rolling z-scores.
5. Compare with an Isolation Forest model.
6. Evaluate alerts against documented maintenance events without leaking future information.
7. Rank assets using anomaly severity, recurrence, and recent activity.
8. Store alert outputs in an analytics table.
9. Query alert trends with SQL.
10. Build a Power BI dashboard for operations teams.

## Evaluation
Use precision, recall, F1-score, alert rate, and lead time when maintenance-event labels are available. If labels are unavailable, report stability checks, false-alert review rules, and sensitivity analysis rather than inventing accuracy.

## Portfolio Skills
Python, Pandas, NumPy, scikit-learn, time-series feature engineering, anomaly detection, SQL, model evaluation, monitoring concepts, Power BI, business storytelling.

## Data
Do not commit private industrial data. Use a public sensor dataset or clearly documented synthetic data. Record the source and license in data/README.md.

## Suggested Dashboard
- Asset risk ranking
- Anomalies by day
- Sensor contribution
- Alert severity distribution
- Repeat-anomaly rate
- Recent sensor trends
- Maintenance priority queue

## Limitations
Anomaly detection identifies unusual behavior, not guaranteed failures. Thresholds and model scores require operational validation before production use.
