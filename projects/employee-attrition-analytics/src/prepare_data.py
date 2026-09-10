"""Reusable cleaning and feature-engineering helpers for employee attrition data."""
import pandas as pd


def clean_employee_data(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    data.columns = [c.strip().lower().replace(" ", "_") for c in data.columns]
    data = data.drop_duplicates()
    return data


def add_tenure_band(df: pd.DataFrame, tenure_col: str = "years_at_company") -> pd.DataFrame:
    data = df.copy()
    if tenure_col in data.columns:
        data["tenure_band"] = pd.cut(
            data[tenure_col],
            bins=[-1, 2, 5, 10, float("inf")],
            labels=["0-2", "3-5", "6-10", "10+"]
        )
    return data
