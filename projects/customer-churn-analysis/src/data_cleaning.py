"""Reusable cleaning helpers for the customer churn project."""

import pandas as pd


def clean_customer_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean common issues in a customer churn dataset."""
    data = df.copy()
    data.columns = [c.strip().lower().replace(" ", "_") for c in data.columns]
    data = data.drop_duplicates()

    # Convert common numeric columns safely when present.
    for col in ["tenure", "monthly_charges", "total_charges"]:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce")

    data = data.dropna(subset=[c for c in ["customerid", "churn"] if c in data.columns])
    return data.reset_index(drop=True)
