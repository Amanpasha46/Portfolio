# Retail Demand Forecasting

## Portfolio Project #4

### Goal
Build a time-series analytics project that forecasts weekly product demand and helps a retailer plan inventory.

### Business Questions
- What products and categories have the highest demand?
- Which products show strong seasonality or trends?
- What will demand look like over the next 4–8 weeks?
- Which products may face stock-out risk if inventory is limited?
- How can forecasts support purchasing decisions?

### Skills Demonstrated
- Python and Pandas
- Time-series data preparation
- Exploratory data analysis
- Rolling averages and lag features
- Forecasting evaluation with MAE and RMSE
- Visualization with Matplotlib
- Business interpretation of forecasts

### Implementation Plan
1. Obtain a public retail sales dataset containing date, product/category, quantity and optionally price.
2. Clean dates, missing values, duplicates and invalid quantities.
3. Aggregate sales to weekly product/category demand.
4. Explore trend, seasonality and unusual demand spikes.
5. Create lag and rolling-average features.
6. Build a baseline forecast and compare it with a simple machine-learning/time-series model.
7. Evaluate forecasts using MAE and RMSE.
8. Produce a forecast table and charts for the next 4–8 weeks.
9. Convert findings into inventory and purchasing recommendations.

### Suggested Deliverables
- Cleaned dataset
- EDA notebook
- Forecasting script/notebook
- Actual vs predicted chart
- Product forecast table
- Short business recommendations

### GitHub Structure
```text
retail-demand-forecasting/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   │   └── README.md
│   └── processed/
├── notebooks/
│   └── demand_forecasting.ipynb
├── src/
│   └── forecast.py
└── outputs/
    └── README.md
```

### Resume Bullet
**Retail Demand Forecasting | Python, Pandas, Time Series** — Cleaned and aggregated retail sales data, engineered lag and rolling-demand features, evaluated forecasting models using MAE/RMSE, and translated demand forecasts into inventory planning recommendations.
