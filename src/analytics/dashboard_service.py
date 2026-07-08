from src.analytics.database_reader import DatabaseReader


class DashboardService:

    def __init__(self):
        self.db = DatabaseReader()

    def get_total_revenue(self):

        sql = """
        SELECT ROUND(SUM(payment_value),2) AS total_revenue
        FROM payments;
        """

        return self.db.query(sql)

    def get_total_orders(self):

        sql = """
        SELECT COUNT(*) AS total_orders
        FROM orders;
        """

        return self.db.query(sql)

    def get_total_customers(self):

        sql = """
        SELECT COUNT(DISTINCT customer_unique_id) AS total_customers
        FROM customers;
        """

        return self.db.query(sql)

    def get_total_sellers(self):

        sql = """
        SELECT COUNT(*) AS total_sellers
        FROM sellers;
        """

        return self.db.query(sql)

    def get_monthly_revenue(self):

        sql = """
        SELECT
            DATE_TRUNC('month', order_purchase_timestamp) AS month,
            ROUND(SUM(payment_value),2) AS revenue
        FROM orders o
        JOIN payments p
        ON o.order_id = p.order_id
        GROUP BY month
        ORDER BY month;
        """

        return self.db.query(sql)