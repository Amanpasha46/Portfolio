# Public Transit Accessibility Analysis

## Project Overview
Analyze public-transit stops, routes, and neighborhood population data to identify areas with limited access to transit and prioritize locations for service improvement.

This project adds geospatial analytics to the portfolio rather than another classification, churn, sales, or forecasting project.

## Business Problem
A city planning team wants to answer:
- Which neighborhoods are poorly served by public transit?
- How many residents live beyond a reasonable walking distance from a transit stop?
- Which areas have high population but low transit accessibility?
- Where should additional stops or routes be considered first?

## Core Metrics
- Transit stops per square kilometer
- Population within 400m / 800m of a stop
- Population outside the 800m service area
- Accessibility rate by neighborhood
- Transit accessibility priority score

## Tech Stack
- Python
- Pandas / NumPy
- GeoPandas
- Shapely
- Matplotlib
- OpenStreetMap or a city open-data portal

## Implementation Plan
1. Download a public GTFS transit feed or city transit-stop dataset.
2. Obtain neighborhood boundaries and population data from the same city or a compatible open-data source.
3. Clean stop coordinates and remove invalid records.
4. Convert datasets into GeoDataFrames using a suitable projected CRS.
5. Create 400m and 800m service buffers around transit stops.
6. Use spatial joins to estimate population covered by each service area.
7. Calculate accessibility metrics for every neighborhood.
8. Rank neighborhoods using a transparent priority score based on population, coverage, and stop density.
9. Create maps showing transit stops, service areas, and high-priority neighborhoods.
10. Summarize 3–5 actionable planning recommendations.

## Deliverables
- Reproducible Python analysis
- Cleaned/derived dataset
- Transit accessibility map
- Neighborhood ranking table
- Executive summary of findings

## Suggested Questions for the Final Analysis
1. What percentage of the population is within 800m of a transit stop?
2. Which five neighborhoods have the lowest accessibility?
3. Are high-population neighborhoods also well served?
4. Which neighborhoods combine high population with low stop density?
5. How would the priority ranking change when using a 400m rather than 800m walking threshold?

## Important Methodology Note
This is an analytical prioritization exercise, not a claim about actual transit quality. Walking-distance buffers are approximations and should be validated with street-network travel distances before operational decisions.

## Portfolio Outcome
This project demonstrates the ability to combine multiple public datasets, perform spatial transformations and joins, engineer business metrics, visualize geographic patterns, and convert analysis into planning recommendations.
