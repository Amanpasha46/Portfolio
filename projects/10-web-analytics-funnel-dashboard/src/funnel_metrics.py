"""Reusable metrics for web funnel analysis."""

import pandas as pd


def funnel_counts(events: pd.DataFrame, session_col: str = "session_id", event_col: str = "event_type") -> pd.DataFrame:
    """Return unique-session counts for each funnel event."""
    rows = []
    for event_name in ["visit", "product_view", "add_to_cart", "checkout", "purchase"]:
        count = events.loc[events[event_col].eq(event_name), session_col].nunique()
        rows.append({"event": event_name, "sessions": int(count)})
    return pd.DataFrame(rows)


def conversion_rate(numerator: int, denominator: int) -> float:
    """Safely calculate a conversion rate."""
    return float(numerator / denominator) if denominator else 0.0


def conversion_by_segment(
    events: pd.DataFrame,
    segment_col: str,
    session_col: str = "session_id",
    event_col: str = "event_type",
) -> pd.DataFrame:
    """Calculate visit-to-purchase conversion by a segment such as source or device."""
    visits = (
        events.loc[events[event_col].eq("visit")]
        .groupby(segment_col)[session_col]
        .nunique()
        .rename("visits")
    )
    purchases = (
        events.loc[events[event_col].eq("purchase")]
        .groupby(segment_col)[session_col]
        .nunique()
        .rename("purchases")
    )
    result = pd.concat([visits, purchases], axis=1).fillna(0).reset_index()
    result["conversion_rate"] = result.apply(
        lambda row: conversion_rate(row["purchases"], row["visits"]), axis=1
    )
    return result.sort_values("conversion_rate", ascending=False)
