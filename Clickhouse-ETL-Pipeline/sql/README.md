# ClickHouse SQL Layer V3

Production-oriented SQL layer for the ecommerce analytics project.

Execution Order
1. 00_init.sql
2. 01_staging.sql
3. 02_dimensions.sql
4. 03_fact_events.sql
5. 04_materialized_views.sql
6. 05_data_marts.sql
7. 06_quality_checks.sql

Features
- Raw → Staging → Warehouse → Marts
- Monthly partitioning
- LowCardinality optimization
- Incremental-ready structure
- Materialized views
- BI-ready marts
- Validation queries
