# A/B Test Experiment Analysis

## Project Idea
Analyze an online experiment where users are randomly assigned to control and treatment groups. Determine whether a product change produced a statistically credible improvement in conversion while checking sample balance and practical impact.

## Business Questions
- Is treatment conversion different from control conversion?
- What is the absolute and relative lift?
- Is the observed difference statistically significant?
- Is the effect large enough to matter commercially?
- Are experiment groups balanced across key user segments?

## Implementation Plan
1. Load experiment-level user data.
2. Validate unique users, missing values, and treatment/control assignment.
3. Check randomization balance across device, country, and traffic source.
4. Calculate conversion rate, absolute lift, and relative lift.
5. Run a two-proportion statistical test and confidence interval.
6. Perform segment-level analysis without cherry-picking results.
7. Visualize conversion and uncertainty.
8. Summarize the evidence and business implications.

## Skills
Python, Pandas, NumPy, SciPy, SQL, statistics, hypothesis testing, confidence intervals, experimentation, data visualization, business communication.

## GitHub Structure
```text
16-ab-test-experiment-analysis/
├── README.md
├── requirements.txt
├── data/
│   └── README.md
├── src/
│   └── experiment_analysis.py
├── sql/
│   └── experiment_analysis.sql
└── reports/
    └── findings.md
```

No performance results are fabricated in this repository. Results should be generated from a documented dataset.
