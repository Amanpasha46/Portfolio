# Energy Demand & Peak Load Analytics

## Project idea
Analyze hourly electricity-demand data to understand peak-load behavior, recurring demand patterns, and short-term demand dynamics.

## Business questions
- When does electricity demand peak?
- How do weekday, weekend, hour, and seasonal patterns differ?
- Which periods create the highest operational load?
- How accurately can a simple baseline forecast future demand?

## Implementation plan
1. Load hourly demand data.
2. Validate timestamps, missing observations, duplicates, and outliers.
3. Build hourly, daily, weekly, and monthly demand summaries.
4. Engineer hour, weekday, month, lag, and rolling-average features.
5. Identify peak-load periods and peak frequency.
6. Build a transparent baseline forecasting model.
7. Evaluate using MAE, RMSE, and MAPE.
8. Create Power BI-ready summary tables.
9. Translate results into operational recommendations.

## Skills
Python, Pandas, NumPy, SQL, time-series analysis, feature engineering, forecasting, model evaluation, Power BI.

## Data
Use a public electricity-demand dataset. Keep raw data in `data/raw/` only when redistribution is permitted; document the source and license.

## Folder structure
```text
12-energy-demand-analytics/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_forecasting.ipynb
├── sql/
│   └── demand_analysis.sql
├── src/
│   ├── preprocessing.py
│   └── forecasting.py
└── reports/
    └── findings.md
```

No performance figures are fabricated; metrics should be generated after the dataset is downloaded and the workflow is executed.