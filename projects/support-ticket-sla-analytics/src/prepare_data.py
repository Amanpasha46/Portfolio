"""Clean support-ticket data and create operational features."""

import pandas as pd


def prepare_tickets(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned ticket dataframe with response/resolution features."""
    data = df.copy()
    data.columns = [c.strip().lower().replace(" ", "_") for c in data.columns]

    for col in ["created_at", "first_response_at", "resolved_at"]:
        if col in data.columns:
            data[col] = pd.to_datetime(data[col], errors="coerce")

    data = data.drop_duplicates(subset=["ticket_id"] if "ticket_id" in data else None)

    if {"created_at", "first_response_at"}.issubset(data.columns):
        data["first_response_hours"] = (
            data["first_response_at"] - data["created_at"]
        ).dt.total_seconds() / 3600

    if {"created_at", "resolved_at"}.issubset(data.columns):
        data["resolution_hours"] = (
            data["resolved_at"] - data["created_at"]
        ).dt.total_seconds() / 3600

    if "ticket_text" in data.columns:
        data["text_length"] = data["ticket_text"].fillna("").astype(str).str.len()

    return data


if __name__ == "__main__":
    print("Import prepare_tickets() from this module and pass a pandas DataFrame.")
