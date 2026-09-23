import numpy as np
from scipy.stats import norm


def conversion_rate(conversions, users):
    return conversions / users if users else np.nan


def two_proportion_z_test(control_conversions, control_users, treatment_conversions, treatment_users):
    p1 = conversion_rate(control_conversions, control_users)
    p2 = conversion_rate(treatment_conversions, treatment_users)
    pooled = (control_conversions + treatment_conversions) / (control_users + treatment_users)
    se = np.sqrt(pooled * (1 - pooled) * (1 / control_users + 1 / treatment_users))
    z = (p2 - p1) / se if se else np.nan
    p_value = 2 * norm.sf(abs(z)) if np.isfinite(z) else np.nan
    return {"control_rate": p1, "treatment_rate": p2, "absolute_lift": p2 - p1, "relative_lift": (p2 - p1) / p1 if p1 else np.nan, "z_stat": z, "p_value": p_value}


def proportion_ci(successes, trials, confidence=0.95):
    p = successes / trials
    z = norm.ppf(1 - (1 - confidence) / 2)
    se = np.sqrt(p * (1 - p) / trials)
    return p - z * se, p + z * se
