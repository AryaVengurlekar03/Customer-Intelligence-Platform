/*
============================================================
CUSTOMER INTELLIGENCE PLATFORM
Module 05 - Delivery Analysis
Author : Utkarsh Tiwari
============================================================
Objective:
Analyze delivery performance, shipping efficiency,
and customer satisfaction.
============================================================
*/


-- ==========================================================
-- Business Question 1
-- Average delivery time (days)
-- ==========================================================

SELECT
    ROUND(
        AVG(
            order_delivered_customer_date -
            order_purchase_timestamp
        ),
        2
    ) AS average_delivery_days
FROM orders
WHERE order_delivered_customer_date IS NOT NULL;

/*
Business Insight:
- Measures average delivery time.
- Helps evaluate logistics performance.
*/


-- ==========================================================
-- Business Question 2
-- Average shipping time (Seller to Courier)
-- ==========================================================

SELECT

ROUND(

AVG(

order_delivered_carrier_date -
order_purchase_timestamp

),

2

) AS average_shipping_days

FROM orders

WHERE order_delivered_carrier_date IS NOT NULL;

/*
Business Insight:
- Measures how quickly sellers hand over
  orders to logistics partners.
*/


-- ==========================================================
-- Business Question 3
-- Average courier delivery time
-- ==========================================================

SELECT

ROUND(

AVG(

order_delivered_customer_date -
order_delivered_carrier_date

),

2

) AS courier_delivery_days

FROM orders

WHERE order_delivered_customer_date IS NOT NULL
AND order_delivered_carrier_date IS NOT NULL;

/*
Business Insight:
- Evaluates courier performance.
*/


-- ==========================================================
-- Business Question 4
-- Delayed Deliveries
-- ==========================================================

SELECT

COUNT(*) AS delayed_orders

FROM orders

WHERE order_delivered_customer_date >
order_estimated_delivery_date;

/*
Business Insight:
- Counts orders delivered after
  estimated delivery date.
*/


-- ==========================================================
-- Business Question 5
-- Early Deliveries
-- ==========================================================

SELECT

COUNT(*) AS early_deliveries

FROM orders

WHERE order_delivered_customer_date <
order_estimated_delivery_date;

/*
Business Insight:
- Orders delivered before estimated date.
*/


-- ==========================================================
-- Business Question 6
-- Delivery Status Distribution
-- ==========================================================

SELECT

order_status,

COUNT(*) AS total_orders

FROM orders

GROUP BY order_status

ORDER BY total_orders DESC;

/*
Business Insight:
- Shows order lifecycle distribution.
*/


-- ==========================================================
-- Business Question 7
-- States with longest delivery time
-- ==========================================================

SELECT

c.customer_state,

ROUND(

AVG(

o.order_delivered_customer_date -
o.order_purchase_timestamp

),

2

) AS average_days

FROM customers c

JOIN orders o
ON c.customer_id = o.customer_id

WHERE o.order_delivered_customer_date IS NOT NULL

GROUP BY c.customer_state

ORDER BY average_days DESC;

/*
Business Insight:
- Identifies states with slower deliveries.
*/


-- ==========================================================
-- Business Question 8
-- Top 10 Fastest Delivery States
-- ==========================================================

SELECT

c.customer_state,

ROUND(

AVG(

o.order_delivered_customer_date -
o.order_purchase_timestamp

),

2

) AS average_days

FROM customers c

JOIN orders o
ON c.customer_id = o.customer_id

WHERE o.order_delivered_customer_date IS NOT NULL

GROUP BY c.customer_state

ORDER BY average_days

LIMIT 10;

/*
Business Insight:
- Identifies best-performing states.
*/


-- ==========================================================
-- Business Question 9
-- Monthly Delivery Performance
-- ==========================================================

SELECT

DATE_TRUNC(
'month',
order_purchase_timestamp
) AS month,

ROUND(

AVG(

order_delivered_customer_date -
order_purchase_timestamp

),

2

) AS average_delivery_days

FROM orders

WHERE order_delivered_customer_date IS NOT NULL

GROUP BY month

ORDER BY month;

/*
Business Insight:
- Helps identify seasonal logistics trends.
*/


-- ==========================================================
-- Business Question 10
-- Average Freight Cost
-- ==========================================================

SELECT

ROUND(

AVG(freight_value),

2

) AS average_freight_cost

FROM order_items;

/*
Business Insight:
- Measures shipping cost per item.
*/


-- ==========================================================
-- Business Question 11
-- Top 10 Orders with Highest Freight
-- ==========================================================

SELECT

order_id,

ROUND(

SUM(freight_value),

2

) AS freight_cost

FROM order_items

GROUP BY order_id

ORDER BY freight_cost DESC

LIMIT 10;

/*
Business Insight:
- High freight orders may reduce profitability.
*/


-- ==========================================================
-- Business Question 12
-- Freight Cost Percentage of Product Price
-- ==========================================================

SELECT

ROUND(

AVG(

freight_value / price

) * 100,

2

) AS freight_percentage

FROM order_items;

/*
Business Insight:
- Indicates shipping cost relative to product value.
*/


-- ==========================================================
-- End of Delivery Analysis
-- ==========================================================