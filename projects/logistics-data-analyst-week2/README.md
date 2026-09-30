# Logistics Data Analyst Internship – Week 2

## Data Collection, Cleaning and Preprocessing

**Intern:** Mohammed Aman Pasha

This project demonstrates a reproducible logistics-data preprocessing pipeline. The Freight Analysis Framework (FAF), maintained through a Bureau of Transportation Statistics and Federal Highway Administration partnership, is used as the public domain reference.

For hands-on preprocessing, the Python script creates a simulated delivery dataset with realistic logistics variables and deliberately introduces common data-quality issues: missing values, duplicate shipment IDs, inconsistent category formatting, and extreme observations.

### Pipeline
1. Simulate logistics data
2. Profile the raw dataset
3. Standardize data types and categories
4. Remove duplicate shipment IDs
5. Impute missing numeric values using medians
6. Fill missing categories with Unknown
7. Apply business-rule validation
8. Create delay and cost-per-kilometre features
9. Detect outliers using the IQR method
10. Detect multivariate anomalies using Isolation Forest
11. Standardize selected numeric features using StandardScaler
12. Save raw and cleaned datasets

### Files
- week2_logistics_preprocessing.py – complete runnable preprocessing demonstration
- requirements.txt – Python dependencies
- logistics_raw.csv and logistics_clean_preprocessed.csv are generated when the script is run locally

### Run
pip install -r requirements.txt
python week2_logistics_preprocessing.py

### Public References
- FHWA Freight Analysis Framework: https://ops.fhwa.dot.gov/freight/freight_analysis/faf/
- pandas missing data: https://pandas.pydata.org/docs/user_guide/missing_data.html
- pandas fillna: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html
- scikit-learn StandardScaler: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
- scikit-learn Isolation Forest: https://scikit-learn.org/stable/auto_examples/ensemble/plot_isolation_forest.html