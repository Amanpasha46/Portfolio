import pandas as pd
from sklearn.ensemble import IsolationForest


def fit_isolation_forest(df: pd.DataFrame, feature_columns, contamination="auto", random_state=42):
    """Fit an Isolation Forest and return the dataframe with anomaly fields.

    anomaly_flag: -1 indicates an observation isolated as anomalous, 1 otherwise.
    anomaly_score: larger values indicate observations that are more typical.
    """
    model = IsolationForest(
        contamination=contamination,
        random_state=random_state,
        n_estimators=200,
    )
    x = df[feature_columns].copy()
    model.fit(x)
    result = df.copy()
    result["anomaly_flag"] = model.predict(x)
    result["anomaly_score"] = model.decision_function(x)
    return result, model
