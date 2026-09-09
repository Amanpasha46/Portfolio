# Support Ticket SLA Analytics & Priority Prediction

## Portfolio Project #5

### Project idea
Analyze customer-support tickets to understand service performance and build a machine-learning model that predicts whether a new ticket is likely to miss its SLA (service-level agreement).

This project adds **text analytics, classification, model evaluation, and operational analytics** to the portfolio without repeating the earlier churn, sales, marketing ROI, or forecasting projects.

### Business problem
A support team receives thousands of tickets. Managers need to know where SLA breaches happen and which new tickets require early intervention.

### Business questions
- What percentage of tickets miss the SLA?
- Which issue types and priority levels have the most breaches?
- Does response time or ticket complexity relate to SLA performance?
- Which support teams have the highest breach rate?
- Can we predict SLA-breach risk early enough for a manager to intervene?

### Skills demonstrated
- Python / Pandas
- Data cleaning and feature engineering
- Text preprocessing with scikit-learn
- TF-IDF features
- Binary classification
- Train/test split and cross-validation
- Precision, recall, F1-score and confusion matrix
- Operational KPI analysis
- Business recommendations

### Suggested dataset
Use a public customer-support/ticket dataset with fields such as ticket text, priority, category, created time, response time, resolution time and SLA status. If a dataset does not contain an SLA label, define a transparent business rule from response/resolution time and document it.

Do not commit private customer tickets or personally identifiable information.

### Implementation plan
1. Add the public ticket CSV to `data/raw/` or document its download source.
2. Clean missing values, duplicate tickets, timestamps and categorical values.
3. Create operational features such as first-response hours, resolution hours, ticket age and text length.
4. Explore SLA-breach rates by priority, category and support team.
5. Convert ticket text into TF-IDF features.
6. Train a baseline Logistic Regression classifier.
7. Evaluate with precision, recall, F1-score and a confusion matrix; focus on recall for breach detection.
8. Review the most informative text/features and convert model output into an intervention list.
9. Summarize operational recommendations for support managers.

### Recommended deliverables
- Reproducible analysis notebook
- Clean feature dataset
- SLA KPI summary
- Classification model
- Confusion matrix and evaluation metrics
- Feature-importance/interpretable model output
- Short business recommendation report

### GitHub structure
```text
projects/support-ticket-sla-analytics/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   │   └── README.md
│   └── processed/
├── notebooks/
│   └── 01_sla_analysis_and_model.ipynb
├── src/
│   ├── __init__.py
│   ├── prepare_data.py
│   └── train_model.py
└── reports/
    └── README.md
```

### Suggested model workflow
```text
Raw Tickets
    ↓
Cleaning & Validation
    ↓
SLA KPI Analysis
    ↓
Text + Operational Features
    ↓
TF-IDF + Logistic Regression
    ↓
Precision / Recall / F1
    ↓
SLA-Breach Risk List
    ↓
Manager Recommendations
```

### Resume bullet
**Support Ticket SLA Analytics & Prediction | Python, Pandas, scikit-learn** — Analyzed support-ticket operations, engineered response/resolution and text features, built a TF-IDF + Logistic Regression classifier for SLA-breach risk, and evaluated performance using precision, recall and F1-score to support proactive ticket intervention.
