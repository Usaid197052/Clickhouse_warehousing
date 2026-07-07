SELECT 'events' table_name,count() rows FROM ecommerce.events
UNION ALL
SELECT 'stg_events',count() FROM ecommerce.stg_events
UNION ALL
SELECT 'fact_events',count() FROM ecommerce.fact_events;

SELECT
countIf(price<0) negative_prices,
countIf(brand='Unknown') unknown_brand,
countIf(category_code='Unknown') unknown_category
FROM ecommerce.stg_events;

SELECT event_type,count()
FROM ecommerce.fact_events
GROUP BY event_type;