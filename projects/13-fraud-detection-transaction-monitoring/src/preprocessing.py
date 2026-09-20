import pandas as pd


def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """Basic, reusable transaction cleaning without inventing domain-specific rules."""
    out = df.copy()
    out = out.drop_duplicates().reset_index(drop=True)
    if "amount" in out.columns:
        out["amount"] = pd.to_numeric(out["amount"], errors="coerce")
        out = out[out["amount"].notna() & (out["amount"] >= 0)]
    if "timestamp" in out.columns:
        out["timestamp"] = pd.to_datetime(out["timestamp"], errors="coerce")
        out = out[out["timestamp"].notna()]
    return out.reset_index(drop=True)


def add_time_features(df: pd.DataFrame, timestamp_col="timestamp") -> pd.DataFrame:
    out = df.copy()
    ts = pd.to_datetime(out[timestamp_col], errors="coerce")
    out["hour"] = ts.dt.hour
    out["day_of_week"] = ts.dt.dayofweek
    out["is_weekend"] = (ts.dt.dayofweek >= 5).astype(int)
    return out
