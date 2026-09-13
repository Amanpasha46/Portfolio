"""Reusable inventory-analysis calculations."""

import pandas as pd
import numpy as np


def add_inventory_metrics(
    df: pd.DataFrame,
    demand_col: str = "demand",
    lead_time_col: str = "lead_time_days",
    inventory_col: str = "inventory_level",
) -> pd.DataFrame:
    """Add demand, safety-stock, reorder-point and risk metrics.

    Assumes demand is measured consistently per period and lead time is in days.
    Adapt the period conversion to the dataset before using the output for decisions.
    """
    out = df.copy()
    demand = pd.to_numeric(out[demand_col], errors="coerce")
    lead_time = pd.to_numeric(out[lead_time_col], errors="coerce")
    inventory = pd.to_numeric(out[inventory_col], errors="coerce")

    out["demand_mean"] = demand
    out["demand_std"] = demand.fillna(0)
    out["safety_stock"] = 1.65 * out["demand_std"] * np.sqrt(lead_time.clip(lower=0))
    out["reorder_point"] = out["demand_mean"] * lead_time.clip(lower=0) + out["safety_stock"]
    out["stockout_risk"] = (inventory < out["reorder_point"]).astype(int)
    return out


def abc_classification(df: pd.DataFrame, value_col: str) -> pd.DataFrame:
    """Classify SKUs into A/B/C using cumulative value share."""
    out = df.copy()
    out = out.sort_values(value_col, ascending=False).reset_index(drop=True)
    total = out[value_col].sum()
    out["cumulative_share"] = out[value_col].cumsum() / total if total else 0
    out["abc_class"] = pd.cut(
        out["cumulative_share"],
        bins=[-np.inf, 0.80, 0.95, np.inf],
        labels=["A", "B", "C"],
    )
    return out
