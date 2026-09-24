import pandas as pd


def missing_rate(df):
    return (df.isna().mean() * 100).sort_values(ascending=False)


def duplicate_rate(df):
    if len(df) == 0:
        return 0.0
    return float(df.duplicated().mean() * 100)


def numeric_range_violations(df, rules):
    issues = []
    for column, bounds in rules.items():
        if column not in df.columns:
            continue
        low, high = bounds
        mask = df[column].notna() & ((df[column] < low) | (df[column] > high))
        issues.append({"column": column, "violations": int(mask.sum())})
    return pd.DataFrame(issues)


def categorical_violations(df, rules):
    issues = []
    for column, allowed in rules.items():
        if column not in df.columns:
            continue
        mask = df[column].notna() & ~df[column].isin(allowed)
        issues.append({"column": column, "violations": int(mask.sum())})
    return pd.DataFrame(issues)
