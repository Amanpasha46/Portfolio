# Project 18 — Customer Voice NLP Intelligence

## Project Idea
Turn customer reviews or support comments into actionable insights using Natural Language Processing (NLP). Classify sentiment, discover recurring topics, and rank issues that deserve product or support attention.

## Business Questions
- What percentage of customer feedback is positive, neutral, or negative?
- Which topics are most associated with negative sentiment?
- Which recurring issues should product teams prioritize?
- How do sentiment and topic mix change over time?
- Can automated NLP reduce manual review effort?

## Implementation Plan
1. Load a documented public review/feedback dataset.
2. Validate schema, duplicates, missing text, and timestamps.
3. Clean and normalize text without destroying useful context.
4. Create sentiment features and inspect class balance.
5. Build a baseline sentiment classifier using TF-IDF + Logistic Regression.
6. Evaluate precision, recall, F1, and a confusion matrix.
7. Discover recurring themes with TF-IDF keywords and NMF topic modeling.
8. Combine topic and sentiment results into an issue-priority table.
9. Use SQL for aggregate feedback KPIs.
10. Build a Power BI dashboard for sentiment, topics, trends, and priority issues.

## Skills
Python, Pandas, NLP, TF-IDF, Logistic Regression, NMF topic modeling, scikit-learn, SQL, Power BI, model evaluation, business storytelling.

## Reproducibility
No fabricated results are included. Download a documented public dataset, place it in data/raw/, then run the analysis scripts.

## Portfolio Outcome
Demonstrate an end-to-end workflow from unstructured customer text to measurable business recommendations.
