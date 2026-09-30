"""
Week 2 - Logistics Data Collection, Cleaning and Preprocessing
Mohammed Aman Pasha
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

RANDOM_STATE = 42
rng = np.random.default_rng(RANDOM_STATE)
n = 1000
zones = ["Zone A", "Zone B", "Zone C", "Zone D", "Zone E"]
vehicles = ["Van", "Truck", "Bike"]

df = pd.DataFrame({
    "shipment_id": [f"S{i:04d}" for i in range(1, n + 1)],
    "order_date": pd.date_range("2026-09-01", periods=n, freq="h").date,
    "origin_zone": rng.choice(zones, n),
    "destination_zone": rng.choice(zones, n),
    "vehicle_type": rng.choice(vehicles, n, p=[0.55, 0.30, 0.15]),
    "package_count": rng.integers(1, 10, n),
    "weight_kg": np.round(rng.gamma(3, 35, n), 2),
    "distance_km": np.round(rng.gamma(3, 8, n), 2),
    "travel_time_min": np.round(rng.gamma(3, 25, n), 1),
    "promised_time_min": rng.integers(30, 180, n),
    "transport_cost": np.round(rng.uniform(80, 1800, n), 2),
    "delivery_status": rng.choice(["Delivered", "Late", "Failed"], n, p=[0.78, 0.18, 0.04])
})

# Introduce realistic data-quality issues
for col in ["weight_kg", "distance_km", "travel_time_min", "transport_cost"]:
    idx = rng.choice(df.index, size=15, replace=False)
    df.loc[idx, col] = np.nan

idx = rng.choice(df.index, size=10, replace=False)
df.loc[idx, "vehicle_type"] = " " + df.loc[idx, "vehicle_type"].astype(str).str.lower() + " "

df.loc[rng.choice(df.index, 4, replace=False), "distance_km"] = [500, 650, 800, 1000]
df.loc[rng.choice(df.index, 4, replace=False), "transport_cost"] = [9000, 11000, 13000, 15000]

duplicates = df.sample(5, random_state=RANDOM_STATE)
df_raw = pd.concat([df, duplicates], ignore_index=True)
df_raw.to_csv("logistics_raw.csv", index=False)

print("Raw shape:", df_raw.shape)
print(df_raw.isna().sum())

# Cleaning
df = df_raw.copy()
df["vehicle_type"] = df["vehicle_type"].astype("string").str.strip().str.title()
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

numeric_cols = [
    "package_count", "weight_kg", "distance_km",
    "travel_time_min", "promised_time_min", "transport_cost"
]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.drop_duplicates(subset=["shipment_id"], keep="first").copy()

for col in ["weight_kg", "distance_km", "travel_time_min", "transport_cost"]:
    df[col] = df[col].fillna(df[col].median())

for col in ["origin_zone", "destination_zone", "vehicle_type"]:
    df[col] = df[col].fillna("Unknown")

df = df[
    (df["package_count"] > 0) &
    (df["weight_kg"] >= 0) &
    (df["distance_km"] > 0) &
    (df["travel_time_min"] > 0) &
    (df["transport_cost"] >= 0)
].copy()

# Feature engineering
df["delay_minutes"] = df["travel_time_min"] - df["promised_time_min"]
df["cost_per_km"] = df["transport_cost"] / df["distance_km"].replace(0, np.nan)
df["is_late"] = (df["delay_minutes"] > 0).astype(int)

# IQR outlier flag
q1 = df["distance_km"].quantile(0.25)
q3 = df["distance_km"].quantile(0.75)
iqr = q3 - q1
df["distance_iqr_outlier"] = (
    (df["distance_km"] < q1 - 1.5 * iqr) |
    (df["distance_km"] > q3 + 1.5 * iqr)
)

# Multivariate anomaly detection
anomaly_features = ["distance_km", "travel_time_min", "weight_kg", "transport_cost"]
iso = IsolationForest(contamination=0.02, random_state=RANDOM_STATE)
df["anomaly"] = iso.fit_predict(df[anomaly_features].fillna(0))

# Standardization
scale_cols = ["distance_km", "travel_time_min", "weight_kg", "transport_cost"]
scaler = StandardScaler()
df[[f"{c}_scaled" for c in scale_cols]] = scaler.fit_transform(df[scale_cols])

df.to_csv("logistics_clean_preprocessed.csv", index=False)

print("Cleaned shape:", df.shape)
print("Remaining missing values:")
print(df.isna().sum())
print("Potential IQR distance outliers:", int(df["distance_iqr_outlier"].sum()))
print("Potential Isolation Forest anomalies:", int((df["anomaly"] == -1).sum()))
print("Saved logistics_raw.csv and logistics_clean_preprocessed.csv")
