import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error


def add_time_features(df, timestamp_col='timestamp'):
    out = df.copy()
    out[timestamp_col] = pd.to_datetime(out[timestamp_col])
    out['hour'] = out[timestamp_col].dt.hour
    out['day_of_week'] = out[timestamp_col].dt.dayofweek
    out['month'] = out[timestamp_col].dt.month
    out['is_weekend'] = out['day_of_week'].isin([5, 6]).astype(int)
    return out


def add_lag_features(df, demand_col='demand'):
    out = df.copy()
    out['lag_1'] = out[demand_col].shift(1)
    out['lag_24'] = out[demand_col].shift(24)
    out['rolling_24'] = out[demand_col].shift(1).rolling(24).mean()
    return out


def evaluate_forecast(actual, predicted):
    mae = mean_absolute_error(actual, predicted)
    rmse = mean_squared_error(actual, predicted) ** 0.5
    nonzero = actual != 0
    mape = ((actual[nonzero] - predicted[nonzero]).abs() / actual[nonzero]).mean() * 100
    return {'MAE': mae, 'RMSE': rmse, 'MAPE_pct': float(mape)}
