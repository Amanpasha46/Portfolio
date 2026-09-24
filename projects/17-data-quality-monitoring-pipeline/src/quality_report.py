import pandas as pd
from quality_checks import missing_rate, duplicate_rate


def build_quality_summary(df):
    missing = missing_rate(df)
    return pd.DataFrame({
        "metric": ["row_count", "column_count", "duplicate_rate_pct", "max_missing_rate_pct"],
        "value": [len(df), len(df.columns), duplicate_rate(df), float(missing.max()) if len(missing) else 0.0],
    })


def daily_volume_check(df, date_col):
    dates = pd.to_datetime(df[date_col], errors="coerce").dt.date
    counts = dates.value_counts().sort_index().rename("row_count").reset_index()
    counts.columns = ["date", "row_count"]
    counts["pct_change"] = counts["row_count"].pct_change() * 100
    return counts
