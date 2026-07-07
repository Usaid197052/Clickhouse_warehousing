DROP TABLE IF EXISTS ecommerce.sales_dashboard;
CREATE TABLE ecommerce.sales_dashboard
ENGINE=MergeTree
ORDER BY day AS
SELECT
event_date day,
countIf(event_type='view') views,
countIf(event_type='cart') carts,
countIf(event_type='purchase') purchases,
uniqExact(user_id) active_users,
sumIf(price,event_type='purchase') revenue,
round(avgIf(price,event_type='purchase'),2) avg_order_value,
round(if(countIf(event_type='view')=0,0,
countIf(event_type='purchase')/countIf(event_type='view')*100),2) conversion_rate
FROM ecommerce.fact_events
GROUP BY day;

DROP TABLE IF EXISTS ecommerce.brand_dashboard;
CREATE TABLE ecommerce.brand_dashboard
ENGINE=MergeTree
ORDER BY brand AS
SELECT
p.brand,
countIf(f.event_type='purchase') purchases,
sumIf(f.price,f.event_type='purchase') revenue,
uniqExact(f.user_id) customers
FROM ecommerce.fact_events f
LEFT JOIN ecommerce.dim_products p USING(product_id)
GROUP BY p.brand;

DROP TABLE IF EXISTS ecommerce.category_dashboard;
CREATE TABLE ecommerce.category_dashboard
ENGINE=MergeTree
ORDER BY category_id AS
SELECT
category_id,
countIf(event_type='purchase') purchases,
sumIf(price,event_type='purchase') revenue
FROM ecommerce.fact_events
GROUP BY category_id;