# Data Quality Monitoring Pipeline

## Project Overview
Build a practical data-quality monitoring workflow that checks business datasets before they reach dashboards or machine-learning pipelines.

## Business Problem
Bad data can create incorrect KPIs, broken dashboards, and unreliable models. This project turns common data-quality rules into measurable monitoring metrics and an alert-ready report.

## Checks
- Missing-value rate
- Duplicate-row rate
- Invalid categorical values
- Numeric range violations
- Date/timestamp validity
- Referential integrity checks
- Unexpected daily volume changes
- Schema/type drift

## Implementation Plan
1. Load a raw transactional dataset.
2. Profile columns, types, cardinality, and nulls.
3. Define business-quality rules.
4. Run automated validation checks.
5. Produce a row-level issue log.
6. Calculate a dataset quality score.
7. Compare daily volumes and detect anomalies.
8. Store results in a quality-report table.
9. Create a Power BI monitoring dashboard.

## Portfolio Skills
Python, Pandas, SQL, data validation, data profiling, anomaly detection, ETL concepts, KPI design, Power BI, and analytics engineering.

## Structure
```text
17-data-quality-monitoring-pipeline/
├── README.md
├── requirements.txt
├── data/
│   └── README.md
├── src/
│   ├── quality_checks.py
│   └── quality_report.py
├── sql/
│   └── quality_checks.sql
└── reports/
    └── findings.md
```

No fabricated quality metrics are included. Run the checks against a documented dataset to generate real results.
