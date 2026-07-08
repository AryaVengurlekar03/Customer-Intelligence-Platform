/*
============================================================
CUSTOMER INTELLIGENCE PLATFORM
Module 10 - Dashboard Queries
Author : Utkarsh Tiwari
============================================================
Objective:
Create KPI and visualization queries for dashboards.
============================================================
*/


-- ==========================================================
-- KPI 1 : Total Revenue
-- ==========================================================

SELECT
ROUND(SUM(payment_value),2) AS total_revenue
FROM payments;


-- ==========================================================
-- KPI 2 : Total Customers
-- ==========================================================

SELECT
COUNT(DISTINCT customer_unique_id) AS total_customers
FROM customers;


-- ==========================================================
-- KPI 3 : Total Orders
-- ==========================================================

SELECT
COUNT(*) AS total_orders
FROM orders;


-- ==========================================================
-- KPI 4 : Average Order Value
-- ==========================================================

SELECT
ROUND(AVG(payment_value),2) AS average_order_value
FROM payments;


-- ==========================================================
-- KPI 5 : Total Sellers
-- ==========================================================

SELECT
COUNT(*) AS total_sellers
FROM sellers;


-- ==========================================================
-- Dashboard Chart 1
-- Monthly Revenue Trend
-- ==========================================================

SELECT

DATE_TRUNC('month',
order_purchase_timestamp) AS month,

ROUND(
SUM(payment_value),
2
) AS revenue

FROM orders AS o
JOIN payments AS p

ON o.order_id=p.order_id

GROUP BY month

ORDER BY month;


-- ==========================================================
-- Dashboard Chart 2
-- Monthly Orders
-- ==========================================================

SELECT

DATE_TRUNC('month',
order_purchase_timestamp) AS month,

COUNT(*) AS total_orders

FROM orders

GROUP BY month

ORDER BY month;


-- ==========================================================
-- Dashboard Chart 3
-- Revenue by State
-- ==========================================================

SELECT

customer_state,

ROUND(
SUM(payment_value),
2
) AS revenue

FROM customers c

JOIN orders o

ON c.customer_id=o.customer_id

JOIN payments p

ON o.order_id=p.order_id

GROUP BY customer_state

ORDER BY revenue DESC;


-- ==========================================================
-- Dashboard Chart 4
-- Top Product Categories
-- ==========================================================

SELECT

ct.product_category_name_english,

ROUND(
SUM(price),
2
) AS revenue

FROM order_items oi

JOIN products p

ON oi.product_id=p.product_id

JOIN category_translation ct

ON p.product_category_name=
ct.product_category_name

GROUP BY
ct.product_category_name_english

ORDER BY revenue DESC

LIMIT 15;


-- ==========================================================
-- Dashboard Chart 5
-- Order Status Distribution
-- ==========================================================

SELECT

order_status,

COUNT(*) AS total_orders

FROM orders

GROUP BY order_status

ORDER BY total_orders DESC;


-- ==========================================================
-- Dashboard Chart 6
-- Payment Method Distribution
-- ==========================================================

SELECT

payment_type,

COUNT(*) AS transactions

FROM payments

GROUP BY payment_type

ORDER BY transactions DESC;


-- ==========================================================
-- Dashboard Chart 7
-- Top Sellers
-- ==========================================================

SELECT

seller_id,

ROUND(
SUM(price),
2
) AS revenue

FROM order_items

GROUP BY seller_id

ORDER BY revenue DESC

LIMIT 10;


-- ==========================================================
-- Dashboard Chart 8
-- Top Customers
-- ==========================================================

SELECT

customer_unique_id,

ROUND(
SUM(payment_value),
2
) AS revenue

FROM customers c

JOIN orders o

ON c.customer_id=o.customer_id

JOIN payments p

ON o.order_id=p.order_id

GROUP BY customer_unique_id

ORDER BY revenue DESC

LIMIT 10;


-- ==========================================================
-- Dashboard Chart 9
-- Customer Distribution by State
-- ==========================================================

SELECT

customer_state,

COUNT(*) AS customers

FROM customers

GROUP BY customer_state

ORDER BY customers DESC;


-- ==========================================================
-- Dashboard Chart 10
-- Review Score Distribution
-- ==========================================================

SELECT

review_score,

COUNT(*) AS reviews

FROM reviews

GROUP BY review_score

ORDER BY review_score;


/*
============================================================
End of Dashboard Queries
============================================================
*/
