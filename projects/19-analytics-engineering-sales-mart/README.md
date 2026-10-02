# Analytics Engineering Sales Mart

## Project Overview
Build a production-style analytics engineering workflow that converts raw e-commerce orders into tested, documented, BI-ready sales marts.

The project focuses on the layer between raw operational data and dashboards: reproducible transformations, dimensional modeling, data quality tests, and KPI definitions.

## Business Questions
- What are daily and monthly net sales?
- Which products and categories drive revenue?
- How do order counts and average order value change over time?
- Can source totals be reconciled with the analytical mart?
- Which data-quality issues should block reporting?

## Implementation Plan
1. Load raw order data into DuckDB.
2. Profile and standardize source columns.
3. Build SQL staging models.
4. Create customer, product, order, and daily-sales analytical models.
5. Add dbt-style tests for nulls, uniqueness, relationships, and accepted values.
6. Run reconciliation checks against source totals.
7. Expose the final mart to Power BI.
8. Document KPI definitions, assumptions, and actual findings.

## Skills
Python, SQL, DuckDB, dbt concepts, ELT, dimensional modeling, data testing, reconciliation, Power BI, documentation.

## Architecture
Raw files -> DuckDB -> Staging SQL -> Analytical marts -> Quality tests -> BI dashboard

## Important
No business metrics are fabricated. Results should be generated from a documented dataset and recorded in reports/findings.md.
