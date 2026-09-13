# Supply Chain Inventory Optimization

A portfolio project that analyzes inventory, demand, lead time, and supplier performance to reduce stockouts and excess inventory.

## Business Goal

Help an operations team decide which products need attention by combining demand variability, supplier lead time, inventory levels, and service risk.

## Questions

- Which products have the highest stockout risk?
- Which suppliers have the longest or most variable lead times?
- Which SKUs have excess inventory?
- What is the reorder point for each SKU?
- Which products should be prioritized for replenishment?

## Skills

- Python and Pandas
- Data cleaning and feature engineering
- Inventory KPIs
- ABC analysis
- Demand variability and safety stock
- Reorder-point calculations
- Supplier performance analytics
- Power BI dashboarding

## Implementation Plan

1. Add a public inventory/orders dataset to `data/raw/`.
2. Clean product, order, supplier, inventory, and date fields.
3. Aggregate demand by SKU and time period.
4. Calculate average demand, demand variability, lead time, safety stock, reorder point, inventory turnover, and stockout risk.
5. Perform ABC classification using cumulative revenue or demand value.
6. Create a replenishment-priority score.
7. Build a Power BI dashboard for inventory health, supplier performance, and SKU priorities.
8. Document recommendations and limitations. Do not invent results before running the analysis.

## Suggested Dashboard

- Inventory Health Overview
- SKU ABC Classification
- Stockout & Replenishment Risk
- Supplier Lead-Time Performance
- Demand Trends

## GitHub Structure

```text
09-supply-chain-inventory-optimization/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   │   └── README.md
│   └── processed/
├── notebooks/
│   └── 01_inventory_analysis.ipynb
├── src/
│   ├── __init__.py
│   └── inventory_metrics.py
└── reports/
    └── README.md
```

## Resume Bullet

**Supply Chain Inventory Optimization | Python, Pandas, Power BI** — Analyzed SKU demand, inventory levels, supplier lead times, and variability to engineer inventory-health KPIs, ABC classifications, safety-stock and reorder-point metrics, and replenishment priorities for operations decision-making.
