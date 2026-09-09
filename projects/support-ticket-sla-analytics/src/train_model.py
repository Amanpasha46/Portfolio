"""Baseline SLA-breach classifier using TF-IDF + Logistic Regression."""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


def train_sla_model(df, text_col="ticket_text", target_col="sla_breached"):
    """Train and evaluate a reproducible text-classification baseline."""
    data = df[[text_col, target_col]].dropna().copy()
    X_train, X_test, y_train, y_test = train_test_split(
        data[text_col].astype(str),
        data[target_col],
        test_size=0.2,
        random_state=42,
        stratify=data[target_col],
    )

    model = Pipeline([
        ("tfidf", TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=2)),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced")),
    ])
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return model, classification_report(y_test, predictions, zero_division=0)


if __name__ == "__main__":
    print("Import train_sla_model() and pass a prepared ticket dataframe.")
