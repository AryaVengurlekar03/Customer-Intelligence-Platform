/*
============================================================
CUSTOMER INTELLIGENCE PLATFORM
Module 04 - Product Analysis
Author : Utkarsh Tiwari
============================================================
Objective:
Analyze product performance, sales, revenue,
and category trends.
============================================================
*/


-- ==========================================================
-- Business Question 1
-- Which products are sold the most?
-- ==========================================================

SELECT
    product_id,
    COUNT(*) AS total_units_sold
FROM order_items
GROUP BY product_id
ORDER BY total_units_sold DESC
LIMIT 10;

/*
Business Insight:
- Identifies best-selling products.
- Useful for inventory planning.
*/


-- ==========================================================
-- Business Question 2
-- Which product categories generate the highest revenue?
-- ==========================================================

SELECT

    p.product_category_name,

    ROUND(SUM(oi.price),2) AS total_revenue

FROM order_items oi

JOIN products p
ON oi.product_id = p.product_id

GROUP BY p.product_category_name

ORDER BY total_revenue DESC

LIMIT 10;

/*
Business Insight:
- Reveals the most profitable product categories.
- Helps prioritize inventory and marketing.
*/


-- ==========================================================
-- Business Question 3
-- Which product categories sold the highest quantity?
-- ==========================================================

SELECT

    p.product_category_name,

    COUNT(*) AS total_items_sold

FROM order_items oi

JOIN products p
ON oi.product_id = p.product_id

GROUP BY p.product_category_name

ORDER BY total_items_sold DESC

LIMIT 10;

/*
Business Insight:
- High sales volume doesn't always mean high revenue.
- Compare with revenue analysis.
*/


-- ==========================================================
-- Business Question 4
-- Top 10 Most Expensive Products Sold
-- ==========================================================

SELECT

    product_id,

    MAX(price) AS highest_price

FROM order_items

GROUP BY product_id

ORDER BY highest_price DESC

LIMIT 10;

/*
Business Insight:
- Identifies premium products.
*/


-- ==========================================================
-- Business Question 5
-- Average Product Price
-- ==========================================================

SELECT

    ROUND(AVG(price),2) AS average_product_price

FROM order_items;

/*
Business Insight:
- Measures average selling price.
*/


-- ==========================================================
-- Business Question 6
-- Most Expensive Product Category
-- ==========================================================

SELECT

    p.product_category_name,

    ROUND(AVG(oi.price),2) AS average_price

FROM products p

JOIN order_items oi
ON p.product_id = oi.product_id

GROUP BY p.product_category_name

ORDER BY average_price DESC

LIMIT 10;

/*
Business Insight:
- Shows premium product categories.
*/


-- ==========================================================
-- Business Question 7
-- Product Categories with Highest Freight Cost
-- ==========================================================

SELECT

    p.product_category_name,

    ROUND(AVG(oi.freight_value),2) AS average_freight

FROM products p

JOIN order_items oi
ON p.product_id = oi.product_id

GROUP BY p.product_category_name

ORDER BY average_freight DESC

LIMIT 10;

/*
Business Insight:
- Identifies categories with expensive shipping.
*/


-- ==========================================================
-- Business Question 8
-- Products Sold by Number of Sellers
-- ==========================================================

SELECT

    product_id,

    COUNT(DISTINCT seller_id) AS sellers

FROM order_items

GROUP BY product_id

ORDER BY sellers DESC

LIMIT 10;

/*
Business Insight:
- Products sold by multiple sellers
  indicate healthy marketplace competition.
*/


-- ==========================================================
-- Business Question 9
-- Products with Highest Average Review Score
-- ==========================================================

SELECT

    oi.product_id,

    ROUND(AVG(r.review_score),2) AS average_rating

FROM order_items oi

JOIN reviews r
ON oi.order_id = r.order_id

GROUP BY oi.product_id

HAVING COUNT(*) >= 10

ORDER BY average_rating DESC

LIMIT 10;

/*
Business Insight:
- Highly rated products improve customer satisfaction.
*/


-- ==========================================================
-- Business Question 10
-- Lowest Rated Products
-- ==========================================================

SELECT

    oi.product_id,

    ROUND(AVG(r.review_score),2) AS average_rating

FROM order_items oi

JOIN reviews r
ON oi.order_id = r.order_id

GROUP BY oi.product_id

HAVING COUNT(*) >= 10

ORDER BY average_rating

LIMIT 10;

/*
Business Insight:
- Helps identify products needing quality improvements.
*/


-- ==========================================================
-- Business Question 11
-- Revenue by Product Category (English Names)
-- ==========================================================

SELECT

    ct.product_category_name_english,

    ROUND(SUM(oi.price),2) AS revenue

FROM order_items oi

JOIN products p
ON oi.product_id = p.product_id

JOIN category_translation ct
ON p.product_category_name = ct.product_category_name

GROUP BY ct.product_category_name_english

ORDER BY revenue DESC

LIMIT 15;

/*
Business Insight:
- Shows revenue by translated (English) category names.
- Makes dashboard reporting easier.
*/


-- ==========================================================
-- Business Question 12
-- Top 15 Product Categories by Orders
-- ==========================================================

SELECT

    ct.product_category_name_english,

    COUNT(*) AS total_orders

FROM order_items oi

JOIN products p
ON oi.product_id = p.product_id

JOIN category_translation ct
ON p.product_category_name = ct.product_category_name

GROUP BY ct.product_category_name_english

ORDER BY total_orders DESC

LIMIT 15;

/*
Business Insight:
- Identifies categories with highest demand.
*/


-- ==========================================================
-- End of Product Analysis
-- ==========================================================