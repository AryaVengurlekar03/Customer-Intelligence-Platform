import pandas as pd
from sqlalchemy import text
from pathlib import Path
from src.database.connection import get_engine
class Loader:
    def order_status(self):
     return self.execute("""
        SELECT
            order_status,
            COUNT(*) AS total_orders
        FROM orders
        GROUP BY order_status
        ORDER BY total_orders DESC
    """)
    def __init__(self):
        self.engine = get_engine()

    def execute(self, sql):
        with self.engine.connect() as conn:
            return pd.read_sql(text(sql), conn)

    # ---------------- KPIs ---------------- #

    def total_revenue(self):
        return self.execute("""
            SELECT ROUND(SUM(payment_value),2) AS revenue
            FROM payments
        """)

    def total_orders(self):
        return self.execute("""
            SELECT COUNT(*) AS orders
            FROM orders
        """)

    def total_customers(self):
        return self.execute("""
            SELECT COUNT(DISTINCT customer_unique_id) AS customers
            FROM customers
        """)

    def total_sellers(self):
        return self.execute("""
            SELECT COUNT(*) AS sellers
            FROM sellers
        """)

    # ---------------- Charts ---------------- #

    def monthly_revenue(self):
        return self.execute("""
            SELECT
                DATE_TRUNC('month', order_purchase_timestamp) AS month,
                ROUND(SUM(payment_value),2) AS revenue
            FROM orders
            JOIN payments USING(order_id)
            GROUP BY month
            ORDER BY month
        """)

    def revenue_by_state(self):
        return self.execute("""
            SELECT
                customer_state,
                ROUND(SUM(payment_value),2) AS revenue
            FROM customers
            JOIN orders USING(customer_id)
            JOIN payments USING(order_id)
            GROUP BY customer_state
            ORDER BY revenue DESC
        """)

    def payment_methods(self):
        return self.execute("""
            SELECT
                payment_type,
                COUNT(*) AS total
            FROM payments
            GROUP BY payment_type
            ORDER BY total DESC
        """)
    def top_categories(self):
        return self.execute("""
        SELECT
            ct.product_category_name_english AS category,
            ROUND(SUM(price),2) AS revenue
        FROM order_items oi
        JOIN products p
            ON oi.product_id = p.product_id
        JOIN category_translation ct
            ON p.product_category_name = ct.product_category_name
        GROUP BY ct.product_category_name_english
        ORDER BY revenue DESC
        LIMIT 10
    """)

    def monthly_orders(self):
     return self.execute("""
        SELECT
            DATE_TRUNC('month', order_purchase_timestamp) AS month,
            COUNT(*) AS total_orders
        FROM orders
        GROUP BY month
        ORDER BY month
    """)
    def average_order_value(self):
     return self.execute("""
        SELECT
            ROUND(AVG(payment_value),2) AS avg_order_value
        FROM payments
    """)
    def top_sellers(self):
     return self.execute("""
        SELECT
            seller_id,
            ROUND(SUM(price),2) AS revenue
        FROM order_items
        GROUP BY seller_id
        ORDER BY revenue DESC
        LIMIT 10
    """)
    def customer_distribution(self):
     return self.execute("""
        SELECT
            customer_state,
            COUNT(*) AS customers
        FROM customers
        GROUP BY customer_state
        ORDER BY customers DESC
    """)
    def top_customers(self):
     return self.execute("""
        SELECT
            c.customer_unique_id,
            ROUND(SUM(p.payment_value),2) AS revenue
        FROM customers c
        JOIN orders o
            ON c.customer_id = o.customer_id
        JOIN payments p
            ON o.order_id = p.order_id
        GROUP BY c.customer_unique_id
        ORDER BY revenue DESC
        LIMIT 10
    """)
    def revenue_state(self):
      return self.execute("""
        SELECT
            c.customer_state,
            ROUND(SUM(p.payment_value),2) AS revenue
        FROM customers c
        JOIN orders o
            ON c.customer_id=o.customer_id
        JOIN payments p
            ON o.order_id=p.order_id
        GROUP BY c.customer_state
        ORDER BY revenue DESC
    """)
    def unique_customers(self):
     return self.execute("""
        SELECT
            COUNT(DISTINCT customer_unique_id) AS customers
        FROM customers
    """)
    def total_products(self):
     return self.execute("""
        SELECT COUNT(*) AS products
        FROM products
    """)
    def top_product_categories(self):
     return self.execute("""
        SELECT
            ct.product_category_name_english AS category,
            COUNT(*) AS total_sales,
            ROUND(SUM(oi.price),2) AS revenue
        FROM order_items oi
        JOIN products p
            ON oi.product_id = p.product_id
        JOIN category_translation ct
            ON p.product_category_name = ct.product_category_name
        GROUP BY ct.product_category_name_english
        ORDER BY revenue DESC
        LIMIT 10
    """)
    def top_products(self):
     return self.execute("""
        SELECT
            oi.product_id,
            ROUND(SUM(price),2) AS revenue
        FROM order_items oi
        GROUP BY oi.product_id
        ORDER BY revenue DESC
        LIMIT 10
    """)
    def product_revenue_distribution(self):
     return self.execute("""
        SELECT
            ct.product_category_name_english AS category,
            ROUND(SUM(oi.price),2) AS revenue
        FROM order_items oi
        JOIN products p
            ON oi.product_id = p.product_id
        JOIN category_translation ct
            ON p.product_category_name = ct.product_category_name
        GROUP BY ct.product_category_name_english
        ORDER BY revenue DESC
    """)
    def average_delivery_days(self):
     return self.execute("""
        SELECT
            ROUND(
                AVG(
                    EXTRACT(EPOCH FROM (
                        order_delivered_customer_date -
                        order_purchase_timestamp
                    )) / 86400
                ),
                2
            ) AS avg_days
        FROM orders
        WHERE order_delivered_customer_date IS NOT NULL
    """)
    def delivery_status(self):
     return self.execute("""
        SELECT
            CASE
                WHEN order_delivered_customer_date <= order_estimated_delivery_date
                    THEN 'On Time'
                ELSE 'Delayed'
            END AS delivery_status,
            COUNT(*) AS total
        FROM orders
        WHERE order_delivered_customer_date IS NOT NULL
        GROUP BY delivery_status
    """)
    def monthly_deliveries(self):
     return self.execute("""
        SELECT
            DATE_TRUNC('month', order_purchase_timestamp) AS month,
            COUNT(*) AS deliveries
        FROM orders
        WHERE order_delivered_customer_date IS NOT NULL
        GROUP BY month
        ORDER BY month
    """)
    def deliveries_by_state(self):
     return self.execute("""
        SELECT
            c.customer_state,
            COUNT(*) AS deliveries
        FROM customers c
        JOIN orders o
            ON c.customer_id = o.customer_id
        WHERE o.order_delivered_customer_date IS NOT NULL
        GROUP BY c.customer_state
        ORDER BY deliveries DESC
    """)
    def cluster_distribution(self):
     return self.execute("""
        SELECT
            cluster,
            COUNT(*) AS customers
        FROM customer_clusters
        GROUP BY cluster
        ORDER BY cluster
    """)
    def cluster_summary(self):
     return self.execute("""
        SELECT *
        FROM customer_clusters
        ORDER BY cluster
    """)

    # ==========================================
# ML OUTPUTS
# ==========================================

    def cluster_summary(self):
     return pd.read_csv(
        Path("ml_output/customer_cluster_summary.csv")
    )


    def customer_clusters(self):
     return pd.read_csv(
        Path("ml_output/customer_clusters.csv")
    )


    def cluster_report(self):

     with open(
        "ml_output/cluster_report.txt",
        "r",
        encoding="utf8"
    ) as f:

      return f.read()
    def customer_clusters(self):
     return pd.read_csv("ml_output/customer_clusters.csv")

    
    def cluster_summary(self):
     return pd.read_csv("ml_output/customer_cluster_summary.csv")


    def cluster_report(self):
     with open(
        "ml_output/cluster_report.txt",
        "r",
        encoding="utf-8"
    ) as f:
        return f.read()