# Fraud Detection & Transaction Monitoring

## Overview
A practical analytics and machine-learning project for identifying suspicious financial transactions and prioritizing alerts for investigation.

## Business Questions
- Which transaction patterns are unusual?
- Which accounts, locations, devices, or transaction types generate more alerts?
- What threshold gives a useful balance between catching suspicious activity and limiting false alerts?
- How should investigators prioritize cases?

## Implementation Plan
1. Load and validate a public transaction dataset.
2. Clean missing values, duplicates, invalid amounts, and timestamps.
3. Explore transaction amount, frequency, geography, device, and time patterns.
4. Engineer behavioral features such as transaction frequency, amount deviation, velocity, and time-of-day indicators.
5. Apply Isolation Forest for unsupervised anomaly detection.
6. If labeled fraud data exists, compare with Logistic Regression as a supervised baseline.
7. Evaluate using precision, recall, F1, PR-AUC, and ROC-AUC where applicable.
8. Tune an alert threshold and create investigation-priority bands.
9. Build a Power BI monitoring dashboard.
10. Document findings, limitations, and recommendations without claiming fraud from an anomaly score alone.

## Portfolio Skills
Python, Pandas, NumPy, SQL, feature engineering, anomaly detection, scikit-learn, model evaluation, threshold tuning, Power BI, business analytics.

## Repository Structure
- `data/` - source and processed data instructions
- `notebooks/` - EDA and modeling workflow
- `sql/` - transaction analysis queries
- `src/` - reusable preprocessing and anomaly functions
- `dashboard/` - Power BI documentation
- `reports/` - findings and methodology

## Data Ethics
Use only public or synthetic data. An anomaly score is an investigation signal, not proof of fraud. Avoid storing personally identifiable information in the repository.
