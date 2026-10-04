from __future__ import annotations

import pandas as pd
from sklearn.ensemble import IsolationForest

SENSOR_COLUMNS = ["temperature", "vibration", "pressure", "power_kw"]


def add_rolling_features(df: pd.DataFrame, window: int = 24) -> pd.DataFrame:
    """Add rolling mean, rolling std, and rate-of-change features per asset."""
    data = df.sort_values(["asset_id", "timestamp"]).copy()
    for col in SENSOR_COLUMNS:
        grouped = data.groupby("asset_id")[col]
        data[f"{col}_roll_mean"] = grouped.transform(
            lambda s: s.rolling(window, min_periods=max(3, window // 4)).mean()
        )
        data[f"{col}_roll_std"] = grouped.transform(
            lambda s: s.rolling(window, min_periods=max(3, window // 4)).std()
        )
        data[f"{col}_roc"] = grouped.pct_change()
    return data


def fit_isolation_forest(df: pd.DataFrame, contamination: float = 0.02, random_state: int = 42):
    """Fit Isolation Forest without using future maintenance labels."""
    features = [c for c in df.columns if c.endswith("_roll_mean") or c.endswith("_roll_std") or c.endswith("_roc")]
    model_df = df.dropna(subset=features).copy()
    model = IsolationForest(n_estimators=300, contamination=contamination, random_state=random_state)
    model.fit(model_df[features])
    model_df["anomaly_score"] = -model.decision_function(model_df[features])
    model_df["anomaly_flag"] = (model.predict(model_df[features]) == -1).astype(int)
    return model_df, model


if __name__ == "__main__":
    print("Load a documented sensor dataset, engineer features, then call fit_isolation_forest().")
