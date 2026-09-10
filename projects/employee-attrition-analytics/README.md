# Employee Attrition Analytics

## Project Overview
Analyze employee HR data to identify the main drivers of employee attrition and build an interpretable attrition-risk model. This project adds HR analytics and classification to the portfolio, complementing earlier churn, sales, marketing ROI, forecasting, and support-ticket projects.

## Business Questions
- What is the overall employee attrition rate?
- Which departments, roles, and tenure groups have the highest attrition?
- How do overtime, job satisfaction, income, and work-life balance relate to attrition?
- Which employee segments should HR prioritize for retention?
- How accurately can a simple model flag employees at higher attrition risk?

## Implementation Plan
1. Obtain a public employee attrition dataset.
2. Load and validate the data with Pandas.
3. Clean missing values, duplicates, and categorical fields.
4. Perform EDA with attrition-rate comparisons and distributions.
5. Engineer useful features such as tenure bands and income bands.
6. Build a baseline Logistic Regression classifier.
7. Evaluate using precision, recall, F1-score, ROC-AUC, and confusion matrix.
8. Explain the most important drivers and convert findings into HR recommendations.
9. Optionally build a Power BI dashboard with Attrition Rate, Headcount, high-risk segments, and department comparisons.

## Skills
Python, Pandas, NumPy, Matplotlib, Seaborn, scikit-learn, classification, feature engineering, model evaluation, HR analytics, Power BI.

## GitHub Structure
```text
employee-attrition-analytics/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/              # add public dataset locally; do not commit sensitive data
│   └── processed/
├── notebooks/
│   └── 01_attrition_analysis.ipynb
├── src/
│   ├── __init__.py
│   ├── prepare_data.py
│   └── train_model.py
└── reports/
    └── README.md
```

## Expected Portfolio Output
A reproducible notebook, cleaned dataset, EDA charts, model metrics, feature-importance/coefficients explanation, and optional Power BI dashboard.

## Resume Bullet
**Employee Attrition Analytics | Python, Pandas, scikit-learn, Power BI** — Analyzed employee attrition patterns across departments, tenure, compensation, overtime, and satisfaction; engineered predictive features and evaluated an interpretable classification model using precision, recall, F1-score, and ROC-AUC to support retention decisions.
