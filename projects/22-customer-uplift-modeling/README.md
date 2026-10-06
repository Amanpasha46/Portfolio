# Customer Uplift Modeling for Targeted Offers

Estimate which customers are most likely to purchase because of a marketing offer, rather than simply predicting who will purchase.

## Implementation
1. Validate treatment, outcome, customer IDs, and pre-treatment features.
2. Split train/test without post-treatment leakage.
3. Train separate treatment/control response models (T-learner).
4. Estimate individual uplift.
5. Rank customers into uplift deciles.
6. Evaluate uplift@10/20/30% and a Qini-style curve.
7. Compare uplift, propensity, and random targeting.
8. Simulate campaign-budget scenarios.
9. Document causal assumptions and limitations.

## Skills
Python, pandas, NumPy, scikit-learn, uplift modeling, SQL, model evaluation, business analytics.

## Run
```bash
pip install -r requirements.txt
python src/uplift_model.py
```

Use a public randomized marketing/uplift dataset or the reproducible demo generator. Do not claim causal impact from observational data without discussing confounding and overlap.
