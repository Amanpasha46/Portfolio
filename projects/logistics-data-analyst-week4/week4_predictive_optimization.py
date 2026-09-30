"""
Week 4 – Predictive Modeling and Optimization in Logistics Systems
Target: Delivery_Time_hr
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("week4_logistics_dataset.csv")

features = [
    "Destination_Zone", "Vehicle_Type", "Shipment_Volume",
    "Route_Distance_km", "Congestion_Index", "Weather_Index",
    "Promised_Time_hr"
]
target = "Delivery_Time_hr"

X = df[features]
y = df[target]

categorical = ["Destination_Zone", "Vehicle_Type"]
preprocessor = ColumnTransformer(
    [("cat", OneHotEncoder(handle_unknown="ignore"), categorical)],
    remainder="passthrough"
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(
        n_estimators=180, max_depth=12, min_samples_leaf=3,
        random_state=42, n_jobs=-1
    ),
    "Gradient Boosting": GradientBoostingRegressor(
        n_estimators=180, max_depth=3, learning_rate=0.05,
        random_state=42
    )
}

for name, model in models.items():
    pipe = Pipeline([("prep", preprocessor), ("model", model)])
    pipe.fit(X_train, y_train)
    pred = pipe.predict(X_test)
    print(
        name,
        "MAE=", round(mean_absolute_error(y_test, pred), 3),
        "RMSE=", round(mean_squared_error(y_test, pred) ** 0.5, 3),
        "R2=", round(r2_score(y_test, pred), 3)
    )

# Cross-validation for Random Forest
best_model = Pipeline([
    ("prep", preprocessor),
    ("model", RandomForestRegressor(
        n_estimators=180, max_depth=12, min_samples_leaf=3,
        random_state=42, n_jobs=-1
    ))
])
cv = KFold(n_splits=5, shuffle=True, random_state=42)
cv_rmse = -cross_val_score(
    best_model, X, y, cv=cv, scoring="neg_root_mean_squared_error"
)
print("CV RMSE mean:", round(cv_rmse.mean(), 3))

# Hyperparameter tuning
grid = GridSearchCV(
    Pipeline([
        ("prep", preprocessor),
        ("model", RandomForestRegressor(random_state=42, n_jobs=-1))
    ]),
    {
        "model__n_estimators": [120, 180],
        "model__max_depth": [8, 12],
        "model__min_samples_leaf": [2, 3]
    },
    cv=3, scoring="neg_root_mean_squared_error", n_jobs=-1
)
grid.fit(X_train, y_train)
print("Best parameters:", grid.best_params_)

# Rule-based operational optimization
def recommend_vehicle(row):
    if row["Route_Distance_km"] > 35 or row["Shipment_Volume"] > 30:
        return "Truck"
    if row["Route_Distance_km"] <= 12 and row["Congestion_Index"] < 0.55:
        return "Bike"
    return "Van"

df["Recommended_Vehicle"] = df.apply(recommend_vehicle, axis=1)
print(df["Recommended_Vehicle"].value_counts())
