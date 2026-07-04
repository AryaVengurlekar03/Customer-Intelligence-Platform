/*
============================================================
CUSTOMER INTELLIGENCE PLATFORM
Module 07 - Seller Analysis
Author : Utkarsh Tiwari
============================================================
Objective:
Analyze seller performance, revenue contribution,
order volume and customer satisfaction.
============================================================
*/


-- ==========================================================
-- Business Question 1
-- How many sellers are registered?
-- ==========================================================

SELECT
    COUNT(*) AS total_sellers
FROM sellers;

/*
Business Insight:
- Shows total active sellers on the platform.
*/


-- ==========================================================
-- Business Question 2
-- Which sellers sold the most products?
-- ==========================================================

SELECT
    seller_id,
    COUNT(*) AS total_products_sold
FROM order_items
GROUP BY seller_id
ORDER BY total_products_sold DESC
LIMIT 10;

/*
Business Insight:
- Identifies the most active sellers.
*/


-- ==========================================================
-- Business Question 3
-- Which sellers generated the highest revenue?
-- ==========================================================

SELECT
    seller_id,
    ROUND(SUM(price),2) AS total_revenue
FROM order_items
GROUP BY seller_id
ORDER BY total_revenue DESC
LIMIT 10;

/*
Business Insight:
- Shows top revenue-generating sellers.
*/


-- ==========================================================
-- Business Question 4
-- Average revenue per seller
-- ==========================================================

SELECT
    ROUND(AVG(seller_revenue),2) AS average_revenue
FROM
(
    SELECT
        seller_id,
        SUM(price) AS seller_revenue
    FROM order_items
    GROUP BY seller_id
) revenue;

/*
Business Insight:
- Measures average seller performance.
*/


-- ==========================================================
-- Business Question 5
-- Average order value per seller
-- ==========================================================

SELECT
    seller_id,
    ROUND(AVG(price),2) AS average_order_value
FROM order_items
GROUP BY seller_id
ORDER BY average_order_value DESC
LIMIT 10;

/*
Business Insight:
- Identifies premium sellers.
*/


-- ==========================================================
-- Business Question 6
-- Sellers with highest freight charges
-- ==========================================================

SELECT
    seller_id,
    ROUND(AVG(freight_value),2) AS average_freight
FROM order_items
GROUP BY seller_id
ORDER BY average_freight DESC
LIMIT 10;

/*
Business Insight:
- Indicates sellers associated with
  expensive deliveries.
*/


-- ==========================================================
-- Business Question 7
-- Seller revenue by state
-- ==========================================================

SELECT
    s.seller_state,
    ROUND(SUM(oi.price),2) AS revenue
FROM sellers s
JOIN order_items oi
ON s.seller_id = oi.seller_id
GROUP BY s.seller_state
ORDER BY revenue DESC;

/*
Business Insight:
- Shows which states contribute
  the most seller revenue.
*/


-- ==========================================================
-- Business Question 8
-- Number of sellers by state
-- ==========================================================

SELECT
    seller_state,
    COUNT(*) AS total_sellers
FROM sellers
GROUP BY seller_state
ORDER BY total_sellers DESC;

/*
Business Insight:
- Indicates seller concentration.
*/


-- ==========================================================
-- Business Question 9
-- Top sellers by customer review score
-- ==========================================================

SELECT

oi.seller_id,

ROUND(AVG(r.review_score),2) AS average_rating

FROM order_items oi

JOIN reviews r

ON oi.order_id = r.order_id

GROUP BY oi.seller_id

HAVING COUNT(*) >= 20

ORDER BY average_rating DESC

LIMIT 10;

/*
Business Insight:
- Identifies highly rated sellers.
*/


-- ==========================================================
-- Business Question 10
-- Lowest rated sellers
-- ==========================================================

SELECT

oi.seller_id,

ROUND(AVG(r.review_score),2) AS average_rating

FROM order_items oi

JOIN reviews r

ON oi.order_id = r.order_id

GROUP BY oi.seller_id

HAVING COUNT(*) >= 20

ORDER BY average_rating

LIMIT 10;

/*
Business Insight:
- Helps identify sellers needing improvement.
*/


-- ==========================================================
-- Business Question 11
-- Sellers with the highest number of unique products
-- ==========================================================

SELECT

seller_id,

COUNT(DISTINCT product_id) AS unique_products

FROM order_items

GROUP BY seller_id

ORDER BY unique_products DESC

LIMIT 10;

/*
Business Insight:
- Shows sellers with the largest catalog.
*/


-- ==========================================================
-- Business Question 12
-- Revenue contribution percentage by seller
-- ==========================================================

SELECT

seller_id,

ROUND(SUM(price),2) AS revenue,

ROUND(
SUM(price) * 100.0 /
(SELECT SUM(price) FROM order_items),
2
) AS revenue_percentage

FROM order_items

GROUP BY seller_id

ORDER BY revenue DESC

LIMIT 10;

/*
Business Insight:
- Shows contribution of top sellers
  to total company revenue.
*/


-- ==========================================================
-- End of Seller Analysis
-- ==========================================================