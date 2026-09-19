import pandas as pd


def prepare_demand_data(df, timestamp_col='timestamp', demand_col='demand'):
    out = df.copy()
    out[timestamp_col] = pd.to_datetime(out[timestamp_col], errors='coerce')
    out[demand_col] = pd.to_numeric(out[demand_col], errors='coerce')
    out = out.dropna(subset=[timestamp_col, demand_col]).drop_duplicates(subset=[timestamp_col])
    out = out.sort_values(timestamp_col).set_index(timestamp_col)
    out['hour'] = out.index.hour
    out['day_of_week'] = out.index.dayofweek
    out['month'] = out.index.month
    out['is_weekend'] = (out['day_of_week'] >= 5).astype(int)
    out['lag_1h'] = out[demand_col].shift(1)
    out['rolling_24h'] = out[demand_col].rolling(24, min_periods=1).mean()
    return out.reset_index()
