"""Reusable metrics for public-transit accessibility analysis."""

import pandas as pd


def accessibility_rate(population: pd.Series, covered_population: pd.Series) -> pd.Series:
    """Return the share of population covered by transit."""
    return (covered_population / population.replace(0, pd.NA)).fillna(0)


def stop_density(stops: pd.Series, area_sq_km: pd.Series) -> pd.Series:
    """Return transit stops per square kilometer."""
    return (stops / area_sq_km.replace(0, pd.NA)).fillna(0)


def priority_score(accessibility: pd.Series, population: pd.Series, stop_density_value: pd.Series) -> pd.Series:
    """Create a simple transparent priority score: higher means greater need."""
    access_gap = 1 - accessibility.clip(0, 1)
    pop_norm = population / population.max() if population.max() else population
    density_gap = 1 - (stop_density_value / stop_density_value.max()).clip(0, 1) if stop_density_value.max() else stop_density_value
    return 0.5 * access_gap + 0.3 * pop_norm + 0.2 * density_gap
