import numpy as np
import pandas as pd
import statsmodels.api as sm


def estimate_log_log_elasticity(df, price_col="price", quantity_col="quantity"):
    """Estimate a simple constant price elasticity from log(price) and log(quantity).

    This is an association estimate, not proof of causal elasticity.
    """
    data = df[[price_col, quantity_col]].replace([np.inf, -np.inf], np.nan).dropna().copy()
    data = data[(data[price_col] > 0) & (data[quantity_col] > 0)]
    if len(data) < 3:
        raise ValueError("At least three positive observations are required.")
    X = sm.add_constant(np.log(data[price_col]))
    y = np.log(data[quantity_col])
    model = sm.OLS(y, X).fit()
    return model


def simulate_revenue(df, elasticity, price_change):
    """Simulate quantity and revenue after a proportional price change."""
    out = df.copy()
    factor = 1 + price_change
    out["scenario_price"] = out["price"] * factor
    out["scenario_quantity"] = out["quantity"] * factor ** elasticity
    out["scenario_revenue"] = out["scenario_price"] * out["scenario_quantity"]
    out["baseline_revenue"] = out["price"] * out["quantity"]
    out["revenue_change_pct"] = np.where(
        out["baseline_revenue"] != 0,
        (out["scenario_revenue"] / out["baseline_revenue"] - 1) * 100,
        np.nan,
    )
    return out
