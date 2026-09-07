# Marketing Campaign ROI Analysis

## Project idea
Analyze digital marketing campaign performance to identify which channels and campaigns generate the best return on investment (ROI).

## Business questions
- Which campaign has the highest ROI?
- Which channel generates the most revenue?
- What is the cost per acquisition (CPA)?
- Which campaigns should receive more budget?
- Does conversion rate differ by channel?

## Skills demonstrated
- Python / Pandas
- Data cleaning and feature engineering
- Marketing KPIs: CTR, conversion rate, CPA, ROAS and ROI
- Exploratory data analysis
- Power BI dashboard design
- Business recommendations

## KPI formulas
- CTR = Clicks / Impressions
- Conversion Rate = Conversions / Clicks
- CPA = Spend / Conversions
- ROAS = Revenue / Spend
- ROI = (Revenue - Spend) / Spend

## Implementation plan
1. Add the campaign CSV to `data/raw/`.
2. Run `src/prepare_data.py` to clean data and calculate KPIs.
3. Explore campaign, channel and audience performance.
4. Export the prepared dataset for Power BI.
5. Build pages for Executive Overview, Channel Performance and Campaign Optimization.
6. Document findings and budget recommendations.

## GitHub structure
```text
marketing-campaign-roi-analysis/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   └── processed/
└── src/
    ├── __init__.py
    └── prepare_data.py
```

## Portfolio outcome
The finished project should demonstrate the full workflow: raw marketing data -> cleaning -> KPI engineering -> analysis -> dashboard -> business recommendation.
