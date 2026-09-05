# Customer Churn Analysis

## Project Overview
A practical end-to-end data analytics project that identifies which customer segments are most likely to churn and translates the findings into retention actions.

## Business Problem
A subscription company wants to reduce customer churn. The goal is to understand churn drivers, quantify retention risk, and build a dashboard-ready analysis for business stakeholders.

## Skills Demonstrated
- Python and pandas for data cleaning and analysis
- Exploratory data analysis (EDA)
- SQL-style business metrics
- Customer segmentation
- Feature engineering
- Data visualization
- Business recommendations
- Git/GitHub project documentation

## Key Questions
1. What is the overall churn rate?
2. Which customer segments have the highest churn?
3. Does tenure affect churn?
4. Which contract/payment patterns are associated with churn?
5. What customer groups should the business prioritize for retention?

## Implementation Plan
1. Load a public customer churn dataset.
2. Clean missing values, duplicates, and inconsistent categories.
3. Create features such as tenure bands, monthly-spend bands, and customer value segments.
4. Perform EDA with churn-rate comparisons.
5. Build charts for the highest-impact drivers.
6. Create a retention-priority score using churn rate, customer count, and revenue exposure.
7. Summarize findings as business recommendations.
8. Add a dashboard screenshot when the visualization layer is completed.

## Suggested Dataset
Use the IBM Telco Customer Churn dataset or another clearly licensed public churn dataset. Store the raw dataset in `data/raw/` only if its license permits redistribution; otherwise document the download source in the notebook.

## Repository Structure
```text
customer-churn-analysis/
├── README.md
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── 01_customer_churn_eda.ipynb
├── src/
│   ├── __init__.py
│   ├── data_cleaning.py
│   └── analysis.py
├── reports/
│   └── figures/
├── requirements.txt
└── .gitignore
```

## Portfolio Deliverables
- Cleaned analysis dataset
- Reproducible Python notebook
- 5–7 decision-focused visualizations
- Executive summary of churn drivers
- Retention-priority segment table
- Optional Power BI/Tableau dashboard

## Resume Bullet
**Customer Churn Analysis:** Analyzed subscription customer data with Python/pandas to identify churn drivers, segment high-risk customers, and translate behavioral patterns into data-driven retention recommendations.
