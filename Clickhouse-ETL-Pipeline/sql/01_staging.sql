DROP TABLE IF EXISTS ecommerce.stg_events;
CREATE TABLE ecommerce.stg_events
(
 event_time DateTime,
 event_date Date,
 event_year UInt16,
 event_month UInt8,
 event_day UInt8,
 event_hour UInt8,
 event_type LowCardinality(String),
 product_id UInt64,
 category_id UInt64,
 category_code LowCardinality(String),
 brand LowCardinality(String),
 price Decimal(10,2),
 user_id UInt64,
 user_session UUID
)
ENGINE=MergeTree
PARTITION BY toYYYYMM(event_time)
ORDER BY (event_date,event_type,product_id,user_id);

INSERT INTO ecommerce.stg_events
SELECT
 event_time,
 toDate(event_time),
 toYear(event_time),
 toMonth(event_time),
 toDayOfMonth(event_time),
 toHour(event_time),
 lower(event_type),
 product_id,
 category_id,
 ifNull(category_code,'Unknown'),
 ifNull(brand,'Unknown'),
 price,
 user_id,
 user_session
FROM ecommerce.events;