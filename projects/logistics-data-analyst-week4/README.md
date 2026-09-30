# Week 4 – Predictive Modeling and Optimization in Logistics Systems

This project applies predictive analytics to a hypothetical logistics system.

## Objective
Forecast shipment delivery time and use the predictions to support operational optimization.

## Dataset
A simulated dataset of 1,500 shipment records with:
- Destination zone
- Vehicle type
- Shipment volume
- Route distance
- Congestion index
- Weather index
- Promised delivery time
- Actual delivery time

## Modeling
Three regression models are compared:
1. Linear Regression
2. Random Forest Regression
3. Gradient Boosting Regression

Evaluation metrics:
- MAE
- RMSE
- R²

The project also demonstrates 5-fold cross-validation and Random Forest hyperparameter tuning.

## Optimization
Predicted delivery risk is used to prioritize shipments. A practical vehicle-assignment heuristic recommends bikes for short, lower-volume, lower-congestion routes, vans for medium routes, and trucks for long or high-volume routes.

## Files
- week4_predictive_optimization.py
- week4_logistics_dataset.csv
- requirements.txt
