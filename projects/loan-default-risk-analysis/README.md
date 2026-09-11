# Loan Default Risk Analysis

## Project Idea
Analyze loan applications to identify the factors associated with default and build an interpretable machine-learning model that estimates default risk. This project adds credit-risk analytics to the portfolio and is intentionally different from churn, sales, marketing ROI, forecasting, NLP support tickets, and HR attrition projects.

## Business Questions
- What customer and loan characteristics are associated with default?
- How does default rate vary by income, loan amount, interest rate, and credit history?
- Which borrower segments have the highest risk?
- How accurately can a model classify default risk?
- How could a lender use risk scores to prioritize manual review?

## Implementation Plan
1. Use a public loan/credit-risk dataset and place the raw CSV in `data/raw/`.
2. Clean missing values, duplicates, data types, and categorical fields.
3. Perform EDA with default-rate, income, loan-amount, and credit-history comparisons.
4. Engineer useful features such as debt-to-income ratio and loan-to-income ratio when source columns allow.
5. Split the data into train/test sets with stratification.
6. Train Logistic Regression as an interpretable baseline and compare with a tree-based model.
7. Evaluate using precision, recall, F1, ROC-AUC, and a confusion matrix. Do not report fabricated metrics; calculate them from the chosen dataset.
8. Identify high-risk segments and translate results into practical lending recommendations.
9. Add charts and a concise executive summary to the repository.
10. Optional: build a Power BI dashboard showing approval/default KPIs and risk segments.

## Suggested Deliverables
- Cleaned dataset or reproducible cleaning script
- EDA notebook
- Model training/evaluation notebook
- Feature-importance or coefficient analysis
- Confusion matrix and ROC curve
- Business recommendations
- Optional Power BI dashboard screenshot

## GitHub Structure
```text
loan-default-risk-analysis/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   │   └── README.md
│   └── processed/
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_modeling.ipynb
├── src/
│   ├── __init__.py
│   ├── prepare_data.py
│   └── train_model.py
└── reports/
    └── README.md
```

## Skills Demonstrated
Python, Pandas, NumPy, exploratory data analysis, feature engineering, scikit-learn, classification, model evaluation, interpretable ML, credit-risk analytics, and business communication.

## Resume Bullet
**Loan Default Risk Analysis | Python, Pandas, scikit-learn** — Cleaned and analyzed loan application data, engineered borrower-risk features, compared interpretable classification models using precision, recall, F1-score and ROC-AUC, and translated high-risk segments into practical lending recommendations.

## Note
This is an educational portfolio project. Model outputs should not be used as real-world lending decisions without appropriate validation, fairness testing, governance, and domain review.
