# E-commerce Sales Performance — SQL Analytics

## Project Goal
Analyze an e-commerce order dataset to identify revenue drivers, customer behavior, product performance, and monthly sales trends using SQL.

## Business Questions
1. What are monthly revenue and order trends?
2. Which products and categories generate the most revenue?
3. Which customers contribute the most revenue?
4. What is the average order value (AOV)?
5. Which regions have the strongest sales performance?
6. How much revenue comes from repeat customers?

## Skills Demonstrated
- SQL data cleaning
- JOINs and aggregations
- CASE statements
- CTEs
- Window functions and ranking
- Date-based analysis
- Business KPI design
- Translating analysis into recommendations

## KPIs
- Total Revenue
- Total Orders
- Average Order Value
- Unique Customers
- Repeat Customer Rate
- Revenue by Category
- Monthly Revenue Growth

## Implementation Plan
1. Load `orders`, `customers`, and `products` tables into SQLite/PostgreSQL/MySQL.
2. Validate duplicates, nulls, dates, quantities, and prices.
3. Run the KPI queries in `sql/01_kpis.sql`.
4. Analyze product, customer, regional, and monthly performance with `sql/02_business_analysis.sql`.
5. Export the query results to CSV.
6. Build a Power BI dashboard from the result tables.
7. Add screenshots and business recommendations to this README.

## Suggested Dashboard Pages
- Executive Overview
- Product & Category Performance
- Customer & Region Analysis
- Monthly Trend

## Repository Structure
```text
projects/ecommerce-sales-sql-analysis/
├── README.md
├── requirements.md
├── data/
│   └── README.md
└── sql/
    ├── 01_kpis.sql
    └── 02_business_analysis.sql
```

## Dataset
Use any public e-commerce orders dataset with equivalent fields. Do not commit large raw datasets or private customer information. Place local data under `data/` and document its source in `data/README.md`.

## Resume Bullet
**E-commerce Sales Performance Analysis | SQL, Power BI** — Analyzed order, customer, product, and regional data using SQL CTEs, joins, aggregations, and window functions to identify revenue drivers, customer trends, and sales opportunities; prepared KPI outputs for an interactive Power BI dashboard.
