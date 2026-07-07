DROP TABLE IF EXISTS ecommerce.fact_events;
CREATE TABLE ecommerce.fact_events
(
 event_time DateTime,
 event_date Date,
 event_type LowCardinality(String),
 product_id UInt64,
 category_id UInt64,
 user_id UInt64,
 user_session UUID,
 price Decimal(10,2)
)
ENGINE=MergeTree
PARTITION BY toYYYYMM(event_time)
ORDER BY(event_date,event_type,product_id,user_id);

INSERT INTO ecommerce.fact_events
SELECT event_time,event_date,event_type,product_id,category_id,user_id,user_session,price
FROM ecommerce.stg_events;