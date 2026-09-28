# Workforce Scheduling & Capacity Optimization

Practical operations analytics project that converts hourly demand into a cost-aware workforce schedule.

## Objective
Determine how many workers are needed in each time slot and optimize assignments while respecting availability, shift length, and maximum-hours constraints.

## Implementation plan
1. Load and validate demand and employee availability data.
2. Explore demand by hour, weekday, and location.
3. Estimate required staffing from workload/service assumptions.
4. Measure baseline understaffing, overstaffing, coverage, and labor hours.
5. Build an OR-Tools constraint optimization model.
6. Compare baseline and optimized schedules.
7. Analyze KPIs with SQL.
8. Export results for a Power BI operations dashboard.

## KPIs
- Coverage %
- Understaffed hours
- Overstaffed hours
- Labor hours
- Estimated labor cost
- Employee utilization
- Demand-to-capacity ratio

## Skills
Python, Pandas, NumPy, SQL, OR-Tools, operations research, optimization, capacity planning, Power BI.

## Data
This repository does not include proprietary employee data. Add a documented public or synthetic dataset under `data/` and record its source and assumptions.

## Reproducibility
Install dependencies with `pip install -r requirements.txt`, then run the scripts in `src/` after placing the documented input files in `data/`.

No business results are fabricated; metrics should be generated from the selected dataset.
