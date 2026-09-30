"""
Week 3 - Advanced Data Analysis and Visualization in Logistics
YuvaIntern Logistics Data Analyst Internship

This script simulates logistics data, performs EDA, and generates
visualizations using pandas and matplotlib.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

n = 1200
dates = pd.date_range("2026-01-01", periods=90, freq="D")
zones = ["North", "South", "East", "West", "Central"]
vehicles = ["Van", "Truck", "Bike"]

df = pd.DataFrame({
    "Shipment_ID": [f"S{i:04d}" for i in range(1, n + 1)],
    "Order_Date": np.random.choice(dates, n),
    "Origin_Zone": np.random.choice(zones, n),
    "Destination_Zone": np.random.choice(zones, n),
    "Vehicle_Type": np.random.choice(vehicles, n, p=[.50, .25, .25]),
    "Shipment_Volume": np.random.poisson(18, n) + 2,
    "Route_Distance_km": np.clip(np.random.gamma(2.2, 9, n) + 4, 3, 90),
})

df["Travel_Time_hr"] = (
    0.35 + df["Route_Distance_km"] / 32 + np.random.normal(0, .22, n)
).clip(.25, 7).round(2)

peak = np.where(df["Order_Date"].dt.dayofweek.isin([4, 5]), .35, 0)
df["Delivery_Time_hr"] = (
    df["Travel_Time_hr"] + peak + np.random.normal(.15, .25, n)
).clip(.3, 8).round(2)

df["Promised_Time_hr"] = (
    df["Route_Distance_km"] / 34 + .75 + np.random.normal(0, .12, n)
).clip(.7, 5.5).round(2)

df["Delivery_Delay_hr"] = (
    df["Delivery_Time_hr"] - df["Promised_Time_hr"]
).clip(lower=0).round(2)

df["Transportation_Cost"] = (
    38 + df["Route_Distance_km"] * 1.85
    + df["Shipment_Volume"] * .72
    + df["Delivery_Time_hr"] * 9
    + np.random.normal(0, 14, n)
).clip(25, 450).round(2)

df["Cost_per_Shipment"] = (
    df["Transportation_Cost"] / df["Shipment_Volume"]
).round(2)

df["On_Time"] = np.where(
    df["Delivery_Time_hr"] <= df["Promised_Time_hr"], "Yes", "No"
)

numeric = [
    "Shipment_Volume", "Route_Distance_km", "Travel_Time_hr",
    "Delivery_Time_hr", "Promised_Time_hr", "Delivery_Delay_hr",
    "Transportation_Cost", "Cost_per_Shipment"
]

print("\nDESCRIPTIVE STATISTICS")
print(df[numeric].describe().round(2))

print("\nCORRELATION MATRIX")
print(df[numeric].corr().round(2))

print("\nON-TIME RATE")
print(round(df["On_Time"].eq("Yes").mean() * 100, 2), "%")

# Distribution
plt.figure(figsize=(8, 4.8))
plt.hist(df["Delivery_Time_hr"], bins=30)
plt.xlabel("Delivery Time (hours)")
plt.ylabel("Number of Shipments")
plt.title("Distribution of Delivery Time")
plt.tight_layout()
plt.savefig("delivery_time_distribution.png", dpi=180)
plt.close()

# Time trend
daily = df.groupby("Order_Date")["Shipment_Volume"].sum()
plt.figure(figsize=(8, 4.8))
plt.plot(daily.index, daily.values)
plt.xlabel("Order Date")
plt.ylabel("Total Shipment Volume")
plt.title("Daily Shipment Volume Trend")
plt.xticks(rotation=35)
plt.tight_layout()
plt.savefig("daily_shipment_volume.png", dpi=180)
plt.close()

# Relationship
plt.figure(figsize=(8, 4.8))
plt.scatter(df["Route_Distance_km"], df["Transportation_Cost"], alpha=.45, s=18)
plt.xlabel("Route Distance (km)")
plt.ylabel("Transportation Cost")
plt.title("Transportation Cost vs Route Distance")
plt.tight_layout()
plt.savefig("cost_vs_distance.png", dpi=180)
plt.close()

# Correlation matrix
corr = df[numeric].corr()
plt.figure(figsize=(8, 6))
im = plt.imshow(corr.values, aspect="auto")
plt.colorbar(im, label="Correlation")
plt.xticks(range(len(numeric)),
           [x.replace("_", " ") for x in numeric],
           rotation=60, ha="right", fontsize=7)
plt.yticks(range(len(numeric)),
           [x.replace("_", " ") for x in numeric], fontsize=7)
plt.title("Correlation Matrix of Key Logistics Metrics")
plt.tight_layout()
plt.savefig("correlation_matrix.png", dpi=180)
plt.close()

# Zone comparison
zone = df.groupby("Destination_Zone")["Delivery_Time_hr"].mean().sort_values()
plt.figure(figsize=(8, 4.8))
plt.bar(zone.index, zone.values)
plt.xlabel("Destination Zone")
plt.ylabel("Average Delivery Time (hours)")
plt.title("Average Delivery Time by Destination Zone")
plt.tight_layout()
plt.savefig("delivery_time_by_zone.png", dpi=180)
plt.close()

# Vehicle comparison
vehicle = df.groupby("Vehicle_Type")["On_Time"].apply(
    lambda s: s.eq("Yes").mean() * 100
)
plt.figure(figsize=(8, 4.8))
plt.bar(vehicle.index, vehicle.values)
plt.xlabel("Vehicle Type")
plt.ylabel("On-Time Delivery Rate (%)")
plt.title("On-Time Delivery Rate by Vehicle Type")
plt.tight_layout()
plt.savefig("on_time_by_vehicle.png", dpi=180)
plt.close()

df.to_csv("week3_logistics_hypothetical_dataset.csv", index=False)
print("\nAnalysis complete. Dataset and visualization files were generated.")
