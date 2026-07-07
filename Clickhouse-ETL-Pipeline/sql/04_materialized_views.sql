DROP VIEW IF EXISTS ecommerce.mv_daily_sales;
CREATE MATERIALIZED VIEW ecommerce.mv_daily_sales
ENGINE=SummingMergeTree
PARTITION BY toYYYYMM(day)
ORDER BY day AS
SELECT
event_date day,
countIf(event_type='purchase') purchases,
sumIf(price,event_type='purchase') revenue
FROM ecommerce.fact_events
GROUP BY day;