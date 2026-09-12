"""Reusable preparation helpers for the hospital readmission project."""

import pandas as pd


def clean_table(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names and remove exact duplicate rows."""
    out = df.copy()
    out.columns = (
        out.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    return out.drop_duplicates().reset_index(drop=True)


def missingness_report(df: pd.DataFrame) -> pd.DataFrame:
    """Return missing counts and percentages for each column."""
    return (
        pd.DataFrame({
            "missing_count": df.isna().sum(),
            "missing_pct": df.isna().mean().mul(100).round(2),
        })
        .sort_values("missing_pct", ascending=False)
    )
