"""Business metrics for customer churn analysis."""

import pandas as pd


def churn_rate(df: pd.DataFrame, churn_col: str = "churn") -> float:
    """Return churn percentage for Yes/No-style churn labels."""
    values = df[churn_col].astype(str).str.strip().str.lower()
    return round(values.isin(["yes", "1", "true"]).mean() * 100, 2)


def churn_by_segment(df: pd.DataFrame, segment_col: str, churn_col: str = "churn") -> pd.DataFrame:
    """Calculate customers and churn rate by a segment."""
    data = df.copy()
    data["_churn"] = data[churn_col].astype(str).str.strip().str.lower().isin(["yes", "1", "true"])
    return (
        data.groupby(segment_col, dropna=False)
        .agg(customers=(churn_col, "size"), churn_rate=("_churn", "mean"))
        .assign(churn_rate=lambda x: (x["churn_rate"] * 100).round(2))
        .sort_values("churn_rate", ascending=False)
        .reset_index()
    )
