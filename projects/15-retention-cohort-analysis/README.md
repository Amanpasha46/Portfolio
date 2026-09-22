# Customer Retention & Cohort Analysis

## Project idea
Analyze customer cohorts to understand retention, repeat purchasing, and customer lifetime behavior. This project focuses on cohort analysis rather than churn classification, adding a distinct product/customer analytics skill.

## Business questions
- How does retention change by acquisition month?
- Which cohorts generate the strongest repeat revenue?
- Where is the largest retention drop after the first purchase?
- How does customer value evolve across cohorts?
- Which acquisition cohorts should receive retention-focused attention?

## Implementation plan
1. Load order/customer transaction data.
2. Clean dates, customer IDs, quantities, prices, and cancelled/invalid orders.
3. Calculate first-purchase month for each customer.
4. Assign each transaction to a customer cohort and cohort age.
5. Build monthly retention and revenue matrices.
6. Calculate repeat-purchase rate, cohort revenue, and cumulative customer value.
7. Segment cohorts by acquisition period.
8. Create retention heatmaps and revenue visualizations.
9. Use SQL for cohort extraction and KPI validation.
10. Build a Power BI dashboard and summarize actionable findings.

## Skills
Python, Pandas, SQL, cohort analysis, customer segmentation, retention metrics, data visualization, Power BI, business storytelling.

## Key metrics
- Cohort size
- Monthly retention rate
- Repeat purchase rate
- Revenue per retained customer
- Cumulative cohort revenue
- Average order value
- Customer lifetime value proxy

## Data
Use a public transaction dataset with customer ID, order date, quantity, unit price, and order/invoice status. Document the source, license, and retrieval date before analysis. Do not commit restricted or oversized raw data.

## Expected deliverables
- Reproducible Python analysis
- SQL cohort queries
- Retention heatmap
- Cohort revenue analysis
- Power BI dashboard
- Business recommendations based on observed results

No business results are fabricated in this repository; metrics should be generated from the selected documented dataset.