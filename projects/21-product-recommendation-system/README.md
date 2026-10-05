# Product Recommendation System

An end-to-end recommendation engine using implicit purchase behavior.

## Business problem
E-commerce teams want to personalize product discovery and increase conversion.

## Approach
1. Clean transaction data.
2. Build a customer-product interaction matrix.
3. Create a popularity baseline.
4. Train item-item collaborative filtering with cosine similarity.
5. Generate top-N recommendations excluding products already purchased.
6. Evaluate with Precision@K, Recall@K and Hit Rate using a time-aware holdout.
7. Compare the model with the popularity baseline.
8. Export recommendations for BI.

## Skills
Python, Pandas, NumPy, scikit-learn, recommender systems, sparse matrices, cosine similarity, feature engineering, ranking metrics, SQL and business analytics.

## Dataset
Use a public transaction dataset such as UCI Online Retail. Do not commit raw data; document download steps in data/README.md.

## Structure
README.md, requirements.txt, data/README.md, src/recommender.py, sql/recommendation_metrics.sql, reports/findings.md

## Outputs
Top recommendations per customer, Precision@5, Recall@5, baseline comparison, catalog coverage and business recommendations.
