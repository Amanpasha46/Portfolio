"""Clean campaign data and calculate marketing KPIs."""
from pathlib import Path
import pandas as pd


def prepare_campaign_data(input_path: str, output_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)
    df.columns = (df.columns.str.strip().str.lower().str.replace(" ", "_", regex=False))

    required = {"impressions", "clicks", "conversions", "spend", "revenue"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    numeric = ["impressions", "clicks", "conversions", "spend", "revenue"]
    for col in numeric:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    df = df.drop_duplicates().copy()
    df["ctr"] = (df["clicks"] / df["impressions"].replace(0, pd.NA)).fillna(0)
    df["conversion_rate"] = (df["conversions"] / df["clicks"].replace(0, pd.NA)).fillna(0)
    df["cpa"] = (df["spend"] / df["conversions"].replace(0, pd.NA)).fillna(0)
    df["roas"] = (df["revenue"] / df["spend"].replace(0, pd.NA)).fillna(0)
    df["roi"] = ((df["revenue"] - df["spend"]) / df["spend"].replace(0, pd.NA)).fillna(0)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return df


if __name__ == "__main__":
    prepare_campaign_data("data/raw/campaigns.csv", "data/processed/campaigns_prepared.csv")
