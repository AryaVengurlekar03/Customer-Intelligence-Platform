/*
============================================================
CUSTOMER INTELLIGENCE PLATFORM
Module 08 - Geographical Analysis
Author : Utkarsh Tiwari
============================================================
Objective:
Analyze customer and seller distribution,
regional sales performance, and logistics.
============================================================
*/


-- ==========================================================
-- Business Question 1
-- Customer Distribution by State
-- ==========================================================

SELECT
    customer_state,
    COUNT(*) AS total_customers
FROM customers
GROUP BY customer_state
ORDER BY total_customers DESC;

/*
Business Insight:
- Identifies states with the largest customer base.
- Useful for regional marketing campaigns.
*/


-- ==========================================================
-- Business Question 2
-- Top 15 Customer Cities
-- ==========================================================

SELECT
    customer_city,
    COUNT(*) AS total_customers
FROM customers
GROUP BY customer_city
ORDER BY total_customers DESC
LIMIT 15;

/*
Business Insight:
- Shows cities with the highest customer concentration.
*/


-- ==========================================================
-- Business Question 3
-- Seller Distribution by State
-- ==========================================================

SELECT
    seller_state,
    COUNT(*) AS total_sellers
FROM sellers
GROUP BY seller_state
ORDER BY total_sellers DESC;

/*
Business Insight:
- Helps understand seller presence across Brazil.
*/


-- ==========================================================
-- Business Question 4
-- Revenue by Customer State
-- ==========================================================

SELECT
    c.customer_state,
    ROUND(SUM(p.payment_value),2) AS total_revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN payments p
ON o.order_id = p.order_id
GROUP BY c.customer_state
ORDER BY total_revenue DESC;

/*
Business Insight:
- Shows which states contribute most revenue.
*/


-- ==========================================================
-- Business Question 5
-- Revenue by Seller State
-- ==========================================================

SELECT
    s.seller_state,
    ROUND(SUM(oi.price),2) AS total_revenue
FROM sellers s
JOIN order_items oi
ON s.seller_id = oi.seller_id
GROUP BY s.seller_state
ORDER BY total_revenue DESC;

/*
Business Insight:
- Identifies states with the highest-performing sellers.
*/


-- ==========================================================
-- Business Question 6
-- Average Delivery Time by Customer State
-- ==========================================================

SELECT
    c.customer_state,
    ROUND(
        AVG(
            o.order_delivered_customer_date -
            o.order_purchase_timestamp
        ),
        2
    ) AS avg_delivery_days
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.order_delivered_customer_date IS NOT NULL
GROUP BY c.customer_state
ORDER BY avg_delivery_days DESC;

/*
Business Insight:
- Highlights states experiencing slower deliveries.
*/


-- ==========================================================
-- Business Question 7
-- Top 10 Cities by Revenue
-- ==========================================================

SELECT
    c.customer_city,
    ROUND(SUM(p.payment_value),2) AS revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN payments p
ON o.order_id = p.order_id
GROUP BY c.customer_city
ORDER BY revenue DESC
LIMIT 10;

/*
Business Insight:
- Identifies cities generating the highest revenue.
*/


-- ==========================================================
-- Business Question 8
-- Average Revenue per Customer State
-- ==========================================================

SELECT
    c.customer_state,
    ROUND(AVG(p.payment_value),2) AS average_revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN payments p
ON o.order_id = p.order_id
GROUP BY c.customer_state
ORDER BY average_revenue DESC;

/*
Business Insight:
- Measures customer spending by state.
*/


-- ==========================================================
-- Business Question 9
-- Customers vs Sellers by State
-- ==========================================================

SELECT
    c.customer_state,
    COUNT(DISTINCT c.customer_id) AS customers,
    COUNT(DISTINCT s.seller_id) AS sellers
FROM customers c
LEFT JOIN sellers s
ON c.customer_state = s.seller_state
GROUP BY c.customer_state
ORDER BY customers DESC;

/*
Business Insight:
- Compares customer demand with seller availability.
*/


-- ==========================================================
-- Business Question 10
-- Top 10 States by Total Orders
-- ==========================================================

SELECT
    c.customer_state,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_state
ORDER BY total_orders DESC
LIMIT 10;

/*
Business Insight:
- Shows regions with the highest order volume.
*/


-- ==========================================================
-- Business Question 11
-- Customer Percentage by State
-- ==========================================================

SELECT
    customer_state,
    COUNT(*) AS total_customers,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM customers),
        2
    ) AS percentage
FROM customers
GROUP BY customer_state
ORDER BY percentage DESC;

/*
Business Insight:
- Displays market share by state.
*/


-- ==========================================================
-- Business Question 12
-- Top 10 Cities with Highest Average Order Value
-- ==========================================================

SELECT
    c.customer_city,
    ROUND(AVG(p.payment_value),2) AS average_order_value
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN payments p
ON o.order_id = p.order_id
GROUP BY c.customer_city
HAVING COUNT(o.order_id) >= 20
ORDER BY average_order_value DESC
LIMIT 10;

/*
Business Insight:
- Finds cities where customers spend the most.
*/


-- ==========================================================
-- End of Geographical Analysis
-- ==========================================================