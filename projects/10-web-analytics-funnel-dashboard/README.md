# Web Analytics Funnel & Conversion Dashboard

A practical portfolio project focused on product/web analytics rather than another predictive ML problem.

## Business Goal

Analyze anonymized website-event data to understand how visitors move through a conversion funnel, identify drop-off points, compare traffic sources and devices, and recommend experiments that can improve conversion.

## Business Questions

- What is the overall visitor-to-purchase conversion rate?
- Where is the largest funnel drop-off?
- Which acquisition channels convert best?
- Does conversion differ by device type?
- Which landing pages or product categories need attention?
- How do conversion and engagement change over time?

## Skills

- Python and Pandas
- Data cleaning and event-log transformation
- Funnel analysis
- Cohort and retention basics
- Conversion-rate analysis
- SQL-ready analytical thinking
- Statistical A/B-test concepts
- Power BI dashboarding

## Implementation Plan

1. Add a public, anonymized web-events or e-commerce funnel dataset to `data/raw/`.
2. Clean event timestamps, visitor/session identifiers, traffic source, device, and event types.
3. Build session-level and visitor-level funnel tables.
4. Calculate visit-to-product-view, add-to-cart, checkout, and purchase conversion rates.
5. Compare conversion by source, device, landing page, and time period.
6. Create cohort-style retention/return-visit metrics where the dataset supports them.
7. Add an A/B-testing section explaining hypothesis, control/treatment, conversion lift, confidence interval, and statistical significance; only report test results when real experiment data exists.
8. Build a Power BI dashboard with funnel, acquisition, device, trend, and segment views.
9. Document three evidence-based product/marketing recommendations.

## Suggested Dashboard

- Executive Funnel Overview
- Acquisition Channel Performance
- Device & Landing-Page Conversion
- Conversion Trend
- Segment / Cohort Analysis

## GitHub Structure

```text
10-web-analytics-funnel-dashboard/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   │   └── README.md
│   └── processed/
├── notebooks/
│   └── 01_funnel_analysis.ipynb
├── sql/
│   └── funnel_metrics.sql
├── src/
│   ├── __init__.py
│   └── funnel_metrics.py
└── reports/
    └── README.md
```

## Resume Bullet

**Web Analytics Funnel Dashboard | Python, Pandas, SQL, Power BI** — Transformed anonymized website event data into session-level funnel metrics, analyzed conversion drop-offs across acquisition channels and devices, and developed an interactive dashboard with evidence-based recommendations for conversion optimization.

## Portfolio Note

Do not fabricate conversion rates, statistical significance, or business impact. Add actual metrics after running the analysis on the selected public dataset.
