/*
============================================================
CUSTOMER INTELLIGENCE PLATFORM
Module 02 - Customer Analysis
Author : Utkarsh Tiwari
============================================================
Objective:
Analyze customer demographics, locations, and purchasing behavior.
============================================================
*/


-- ==========================================================
-- Business Question 1
-- Which states have the highest number of customers?
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
- Helps decide where to focus marketing campaigns.
- Useful for warehouse and logistics planning.
*/


-- ==========================================================
-- Business Question 2
-- Which cities have the highest number of customers?
-- ==========================================================

SELECT
    customer_city,
    COUNT(*) AS total_customers
FROM customers
GROUP BY customer_city
ORDER BY total_customers DESC
LIMIT 10;

/*
Business Insight:
- Shows the Top 10 customer cities.
- High customer concentration indicates strong market demand.
- Useful for targeted advertising and regional expansion.
*/


-- ==========================================================
-- Business Question 3
-- How many unique customers have placed orders?
-- ==========================================================

SELECT
    COUNT(DISTINCT customer_id) AS purchasing_customers
FROM orders;

/*
Business Insight:
- Measures the number of customers who actually made purchases.
- Useful for customer conversion analysis.
*/


-- ==========================================================
-- Business Question 4
-- Which customers placed the highest number of orders?
-- ==========================================================

SELECT
    c.customer_unique_id,
    c.customer_city,
    c.customer_state,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY
    c.customer_unique_id,
    c.customer_city,
    c.customer_state
ORDER BY total_orders DESC
LIMIT 10;

/*
Business Insight:
- Identifies repeat customers.
- These customers are ideal for loyalty programs.
- Repeat buyers contribute significantly to long-term revenue.
*/


-- ==========================================================
-- Business Question 5
-- Which states generated the highest number of orders?
-- ==========================================================

SELECT
    c.customer_state,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_state
ORDER BY total_orders DESC;

/*
Business Insight:
- Shows order distribution across states.
- Helps identify regions with high business activity.
*/


-- ==========================================================
-- Business Question 6
-- Which cities generated the highest number of orders?
-- ==========================================================

SELECT
    c.customer_city,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_city
ORDER BY total_orders DESC
LIMIT 10;

/*
Business Insight:
- Identifies cities contributing the most orders.
- Helps optimize regional logistics and inventory planning.
*/


-- ==========================================================
-- Business Question 7
-- Customer distribution by state (Percentage)
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
- Displays the percentage contribution of each state.
- Helps compare market share across regions.
*/


-- ==========================================================
-- Business Question 8
-- Top 10 customers based on purchase frequency
-- ==========================================================

SELECT
    c.customer_unique_id,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_unique_id
ORDER BY total_orders DESC
LIMIT 10;

/*
Business Insight:
- Identifies the company's most frequent buyers.
- These customers are valuable for retention strategies.
*/


-- ==========================================================
-- End of Customer Analysis
-- ==========================================================