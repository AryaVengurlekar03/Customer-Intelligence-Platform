/*
============================================================
CUSTOMER INTELLIGENCE PLATFORM
Module 11 - Interview SQL Queries
============================================================
*/


-- Top 10 Customers by Revenue

SELECT
customer_unique_id,
ROUND(SUM(payment_value),2) revenue
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN payments p
ON o.order_id=p.order_id
GROUP BY customer_unique_id
ORDER BY revenue DESC
LIMIT 10;


-- Top 10 Products by Revenue

SELECT
product_id,
ROUND(SUM(price),2) revenue
FROM order_items
GROUP BY product_id
ORDER BY revenue DESC
LIMIT 10;


-- Monthly Revenue

SELECT
DATE_TRUNC('month',
order_purchase_timestamp) month,
ROUND(SUM(payment_value),2) revenue
FROM orders o
JOIN payments p
ON o.order_id=p.order_id
GROUP BY month
ORDER BY month;


-- Customer Lifetime Value

SELECT
customer_unique_id,
ROUND(SUM(payment_value),2) lifetime_value
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN payments p
ON o.order_id=p.order_id
GROUP BY customer_unique_id
ORDER BY lifetime_value DESC;


-- Average Delivery Time

SELECT
ROUND(
AVG(
order_delivered_customer_date-
order_purchase_timestamp
),2)
FROM orders
WHERE order_delivered_customer_date IS NOT NULL;


-- Most Popular Payment Method

SELECT
payment_type,
COUNT(*)
FROM payments
GROUP BY payment_type
ORDER BY COUNT(*) DESC;


-- Highest Rated Products

SELECT
oi.product_id,
ROUND(AVG(review_score),2) rating
FROM order_items oi
JOIN reviews r
ON oi.order_id=r.order_id
GROUP BY oi.product_id
HAVING COUNT(*)>=10
ORDER BY rating DESC
LIMIT 10;


/*
============================================================
End of Interview Queries
============================================================
*/