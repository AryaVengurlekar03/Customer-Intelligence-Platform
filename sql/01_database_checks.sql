/*
===========================================================
CUSTOMER INTELLIGENCE PLATFORM
01 - DATABASE HEALTH CHECKS
===========================================================
Purpose:
Verify that all tables are loaded correctly before analysis.
===========================================================
*/

-- 1. Total records in each table

SELECT COUNT(*) AS total_customers
FROM customers;

SELECT COUNT(*) AS total_orders
FROM orders;

SELECT COUNT(*) AS total_products
FROM products;

SELECT COUNT(*) AS total_sellers
FROM sellers;

SELECT COUNT(*) AS total_payments
FROM payments;

SELECT COUNT(*) AS total_reviews
FROM reviews;

SELECT COUNT(*) AS total_order_items
FROM order_items;

SELECT COUNT(*) AS total_geolocations
FROM geolocation;

SELECT COUNT(*) AS total_category_translations
FROM category_translation;


-- 2. Check for duplicate customer IDs
SELECT
    customer_id,
    COUNT(*)
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;


-- 3. Check for duplicate order IDs
SELECT
    order_id,
    COUNT(*)
FROM orders
GROUP BY order_id
HAVING COUNT(*) > 1;


-- 4. Check for missing customer IDs in orders
SELECT COUNT(*) AS missing_customer_ids
FROM orders
WHERE customer_id IS NULL;


-- 5. Check products with missing category
SELECT COUNT(*) AS products_without_category
FROM products
WHERE product_category_name IS NULL;


-- 6. Distribution of order status
SELECT
    order_status,
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC;