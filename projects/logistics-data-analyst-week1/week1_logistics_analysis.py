"""
Week 1 - Logistics Data Analyst Internship
Strategic Planning and Data Exploration

This script illustrates the proposed analytical workflow.
It expects a CSV named logistics_delivery_data.csv with suitable
order, delivery, route and vehicle fields.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("logistics_delivery_data.csv")

# Basic inspection
print(df.head())
print(df.info())
print(df.isnull().sum())

# Cleaning
df = df.drop_duplicates(subset="order_id")
df["dispatch_time"] = pd.to_datetime(df["dispatch_time"])
df["delivery_time"] = pd.to_datetime(df["delivery_time"])
df["promised_time"] = pd.to_datetime(df["promised_time"])

# Feature engineering
df["delay_minutes"] = (
    (df["delivery_time"] - df["promised_time"])
    .dt.total_seconds() / 60
)
df["late_flag"] = (df["delay_minutes"] > 0).astype(int)

# KPIs
on_time_rate = (df["late_flag"] == 0).mean() * 100
avg_delivery_time = df["delivery_minutes"].mean()
avg_distance = df["distance_km"].mean()

print(f"On-time delivery rate: {on_time_rate:.2f}%")
print(f"Average delivery time: {avg_delivery_time:.2f} minutes")
print(f"Average route distance: {avg_distance:.2f} km")

# Zone-level EDA
zone_summary = (
    df.groupby("zone")
      .agg(
          orders=("order_id", "count"),
          avg_delay=("delay_minutes", "mean"),
          avg_distance=("distance_km", "mean")
      )
      .sort_values("orders", ascending=False)
)

print(zone_summary)

zone_summary["orders"].plot(kind="bar", title="Orders by Zone")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.show()

# Regression example
features = ["distance_km", "stops", "package_count"]
X = df[features]
y = df["delivery_minutes"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)
mae = mean_absolute_error(y_test, pred)
print(f"Regression MAE: {mae:.2f} minutes")

# Clustering example
X_cluster = zone_summary[
    ["orders", "avg_delay", "avg_distance"]
].fillna(0)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_cluster)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
zone_summary["cluster"] = kmeans.fit_predict(X_scaled)

print("\nZone clusters:")
print(zone_summary[["cluster"]])

# Route optimization is planned as the next analytical stage.
# Google OR-Tools can be used for vehicle routing with
# capacity and time-window constraints.
