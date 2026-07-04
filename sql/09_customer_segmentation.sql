/*
============================================================
CUSTOMER INTELLIGENCE PLATFORM
Module 09 - Customer Segmentation (RFM Analysis)
Author : Utkarsh Tiwari
============================================================
Objective:
Segment customers based on Recency, Frequency,
and Monetary (RFM) metrics.
============================================================
*/


-- ==========================================================
-- Business Question 1
-- Total Unique Customers
-- ==========================================================

SELECT
COUNT(DISTINCT customer_unique_id) AS total_customers
FROM customers;

/*
Business Insight:
Shows total unique customers in the business.
*/


-- ==========================================================
-- Business Question 2
-- Customer Order Frequency
-- ==========================================================

SELECT

c.customer_unique_id,

COUNT(o.order_id) AS total_orders

FROM customers c

JOIN orders o
ON c.customer_id=o.customer_id

GROUP BY c.customer_unique_id

ORDER BY total_orders DESC

LIMIT 20;

/*
Business Insight:
Identifies repeat customers.
*/


-- ==========================================================
-- Business Question 3
-- Total Customer Spending
-- ==========================================================

SELECT

c.customer_unique_id,

ROUND(
SUM(p.payment_value),
2
) AS total_spent

FROM customers c

JOIN orders o
ON c.customer_id=o.customer_id

JOIN payments p
ON o.order_id=p.order_id

GROUP BY c.customer_unique_id

ORDER BY total_spent DESC

LIMIT 20;

/*
Business Insight:
Shows highest spending customers.
*/


-- ==========================================================
-- Business Question 4
-- Average Spending per Customer
-- ==========================================================

SELECT

ROUND(

AVG(customer_spending),

2

) AS average_customer_spending

FROM

(

SELECT

customer_id,

SUM(payment_value) AS customer_spending

FROM orders o

JOIN payments p

ON o.order_id=p.order_id

GROUP BY customer_id

) t;

/*
Business Insight:
Average revenue generated per customer.
*/


-- ==========================================================
-- Business Question 5
-- Customer Lifetime Value
-- ==========================================================

SELECT

c.customer_unique_id,

ROUND(

SUM(payment_value),

2

) AS lifetime_value

FROM customers c

JOIN orders o
ON c.customer_id=o.customer_id

JOIN payments p
ON o.order_id=p.order_id

GROUP BY c.customer_unique_id

ORDER BY lifetime_value DESC

LIMIT 20;

/*
Business Insight:
Highest value customers.
*/


-- ==========================================================
-- Business Question 6
-- Last Purchase Date
-- ==========================================================

SELECT

customer_unique_id,

MAX(order_purchase_timestamp) AS last_purchase

FROM customers c

JOIN orders o

ON c.customer_id=o.customer_id

GROUP BY customer_unique_id;

/*
Business Insight:
Determines customer recency.
*/


-- ==========================================================
-- Business Question 7
-- RFM Dataset
-- ==========================================================

SELECT

c.customer_unique_id,

MAX(order_purchase_timestamp) AS last_purchase,

COUNT(DISTINCT o.order_id) AS frequency,

ROUND(
SUM(payment_value),
2
) AS monetary

FROM customers c

JOIN orders o
ON c.customer_id=o.customer_id

JOIN payments p
ON o.order_id=p.order_id

GROUP BY customer_unique_id;

/*
Business Insight:
Creates dataset for RFM analysis.
*/


-- ==========================================================
-- Business Question 8
-- Top 20 VIP Customers
-- ==========================================================

SELECT

c.customer_unique_id,

COUNT(o.order_id) AS frequency,

ROUND(
SUM(payment_value),
2
) AS monetary

FROM customers c

JOIN orders o
ON c.customer_id=o.customer_id

JOIN payments p
ON o.order_id=p.order_id

GROUP BY customer_unique_id

HAVING
COUNT(o.order_id)>=5

ORDER BY monetary DESC

LIMIT 20;

/*
Business Insight:
VIP customers for loyalty campaigns.
*/


-- ==========================================================
-- Business Question 9
-- One-Time Customers
-- ==========================================================

SELECT

COUNT(*)

FROM

(

SELECT

customer_id,

COUNT(order_id) total_orders

FROM orders

GROUP BY customer_id

HAVING COUNT(order_id)=1

)t;

/*
Business Insight:
Shows one-time buyers.
*/


-- ==========================================================
-- Business Question 10
-- Repeat Customers
-- ==========================================================

SELECT

COUNT(*)

FROM

(

SELECT

customer_id,

COUNT(order_id)

FROM orders

GROUP BY customer_id

HAVING COUNT(order_id)>1

)t;

/*
Business Insight:
Shows customer retention.
*/


-- ==========================================================
-- Business Question 11
-- Top Customers by Frequency
-- ==========================================================

SELECT

c.customer_unique_id,

COUNT(order_id) AS orders

FROM customers c

JOIN orders o

ON c.customer_id=o.customer_id

GROUP BY customer_unique_id

ORDER BY orders DESC

LIMIT 20;

/*
Business Insight:
Customers with highest purchase frequency.
*/


-- ==========================================================
-- Business Question 12
-- Top Customers by Monetary Value
-- ==========================================================

SELECT

c.customer_unique_id,

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

LIMIT 20;

/*
Business Insight:
Highest revenue-generating customers.
*/


-- ==========================================================
-- Business Question 13
-- Average Orders per Customer
-- ==========================================================

SELECT

ROUND(

AVG(order_count),

2

)

FROM

(

SELECT

customer_id,

COUNT(order_id) order_count

FROM orders

GROUP BY customer_id

)t;

/*
Business Insight:
Average purchase frequency.
*/


-- ==========================================================
-- Business Question 14
-- Average Customer Lifetime Value
-- ==========================================================

SELECT

ROUND(

AVG(customer_value),

2

)

FROM

(

SELECT

customer_id,

SUM(payment_value) customer_value

FROM orders o

JOIN payments p

ON o.order_id=p.order_id

GROUP BY customer_id

)t;

/*
Business Insight:
Average CLV.
*/


-- ==========================================================
-- Business Question 15
-- Customer Segmentation Dataset
-- ==========================================================

SELECT

c.customer_unique_id,

MAX(order_purchase_timestamp) AS recency,

COUNT(DISTINCT o.order_id) AS frequency,

ROUND(
SUM(payment_value),
2
) AS monetary

FROM customers c

JOIN orders o
ON c.customer_id=o.customer_id

JOIN payments p
ON o.order_id=p.order_id

GROUP BY customer_unique_id

ORDER BY monetary DESC;

/*
Business Insight:
Final dataset for Python,
Power BI,
Machine Learning,
and Streamlit dashboard.
*/


-- ==========================================================
-- END OF CUSTOMER SEGMENTATION
-- ==========================================================