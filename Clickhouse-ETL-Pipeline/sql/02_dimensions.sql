DROP TABLE IF EXISTS ecommerce.dim_products;
CREATE TABLE ecommerce.dim_products
ENGINE=ReplacingMergeTree
ORDER BY product_id AS
SELECT product_id,any(brand) brand,any(category_id) category_id,any(category_code) category_code
FROM ecommerce.stg_events GROUP BY product_id;

DROP TABLE IF EXISTS ecommerce.dim_users;
CREATE TABLE ecommerce.dim_users
ENGINE=ReplacingMergeTree
ORDER BY user_id AS
SELECT user_id,min(event_time) first_seen,max(event_time) last_seen
FROM ecommerce.stg_events GROUP BY user_id;

DROP TABLE IF EXISTS ecommerce.dim_categories;
CREATE TABLE ecommerce.dim_categories
ENGINE=ReplacingMergeTree
ORDER BY category_id AS
SELECT category_id,any(category_code) category_code
FROM ecommerce.stg_events GROUP BY category_id;

DROP TABLE IF EXISTS ecommerce.dim_dates;
CREATE TABLE ecommerce.dim_dates
ENGINE=MergeTree
ORDER BY full_date AS
SELECT DISTINCT
event_date full_date,
event_year,event_month,event_day,
toDayOfWeek(event_date) weekday,
toISOWeek(event_date) iso_week,
toQuarter(event_date) quarter
FROM ecommerce.stg_events;