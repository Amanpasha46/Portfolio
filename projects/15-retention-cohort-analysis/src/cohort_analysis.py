import pandas as pd


def prepare_transactions(df, customer_col='customer_id', date_col='order_date'):
    out = df.copy()
    out[date_col] = pd.to_datetime(out[date_col], errors='coerce')
    out = out.dropna(subset=[customer_col, date_col])
    out['order_month'] = out[date_col].dt.to_period('M').dt.to_timestamp()
    first_purchase = out.groupby(customer_col)['order_month'].transform('min')
    out['cohort_month'] = first_purchase
    out['cohort_age'] = (
        (out['order_month'].dt.year - out['cohort_month'].dt.year) * 12
        + (out['order_month'].dt.month - out['cohort_month'].dt.month)
    )
    return out


def retention_table(df, customer_col='customer_id'):
    unique = df[[customer_col, 'cohort_month', 'cohort_age']].drop_duplicates()
    counts = unique.groupby(['cohort_month', 'cohort_age'])[customer_col].nunique()
    sizes = counts.groupby(level=0).first()
    retention = counts.div(sizes, level=0).unstack(fill_value=0)
    return retention


def cohort_revenue(df, revenue_col='revenue'):
    return df.groupby(['cohort_month', 'cohort_age'])[revenue_col].sum().unstack(fill_value=0)
