"""Reusable helpers for retail demand forecasting."""

import pandas as pd


def prepare_weekly_demand(df, date_col="date", quantity_col="quantity"):
    """Return weekly demand after validating dates and quantities."""
    data = df.copy()
    data[date_col] = pd.to_datetime(data[date_col], errors="coerce")
    data[quantity_col] = pd.to_numeric(data[quantity_col], errors="coerce")
    data = data.dropna(subset=[date_col, quantity_col])
    data = data[data[quantity_col] >= 0]
    weekly = (
        data.set_index(date_col)[quantity_col]
        .resample("W")
        .sum()
        .rename("demand")
        .reset_index()
    )
    return weekly


def add_lag_features(weekly, target="demand", lags=(1, 2, 4), windows=(4, 8)):
    """Add lag and rolling-mean features to weekly demand."""
    result = weekly.copy()
    for lag in lags:
        result[f"lag_{lag}"] = result[target].shift(lag)
    for window in windows:
        result[f"rolling_mean_{window}"] = result[target].shift(1).rolling(window).mean()
    return result


if __name__ == "__main__":
    print("Import prepare_weekly_demand() and add_lag_features() in your notebook or pipeline.")
