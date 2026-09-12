# Hospital Readmission Analytics

## Project Overview
Analyze hospital encounter data to identify patterns associated with 30-day readmissions and build an interpretable risk model. The project focuses on healthcare operations analytics rather than repeating the previous sales, churn, forecasting, NLP, HR, and credit-risk projects.

## Business Questions
- What is the 30-day readmission rate?
- Which patient/encounter segments have the highest readmission rates?
- How do prior visits, length of stay, and discharge disposition relate to readmission?
- Which factors are most useful for predicting readmission risk?
- How could hospitals prioritize follow-up resources?

## Skills
- Python, Pandas, NumPy
- Data cleaning and validation
- Exploratory data analysis
- Feature engineering
- Logistic Regression / tree-based classification
- Precision, recall, F1, ROC-AUC
- Model interpretation
- Healthcare operations analytics

## Implementation Plan
1. Obtain a public, de-identified hospital/readmission dataset.
2. Document the dataset and data dictionary; do not use private patient information.
3. Clean missing values, duplicates, invalid categories, and numeric fields.
4. Define the target as 30-day readmission where supported by the dataset.
5. Explore readmission by demographics, prior utilization, stay length, medications/procedures, and discharge information.
6. Engineer clinically/operationally meaningful features without data leakage.
7. Split data into train/test sets and establish a simple baseline.
8. Train an interpretable classification model and evaluate with precision, recall, F1, ROC-AUC, and a confusion matrix.
9. Explain the strongest model drivers and create actionable operational segments.
10. Document limitations, fairness considerations, and that the model is for portfolio/analytical demonstration—not clinical decision-making.

## GitHub Structure
```text
08-hospital-readmission-analytics/
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

## Expected Portfolio Deliverables
- Reproducible cleaning pipeline
- EDA notebook with 6–8 useful charts
- Model comparison table
- Confusion matrix and ROC curve
- Feature-importance/model-explanation chart
- Short business recommendations section
- Dashboard or polished summary page

## Resume Bullet
**Hospital Readmission Analytics | Python, Pandas, scikit-learn** — Analyzed de-identified hospital encounter data, engineered readmission-risk features, built and evaluated interpretable classification models using precision, recall, F1-score and ROC-AUC, and translated model findings into operational follow-up recommendations.
