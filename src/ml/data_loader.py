from src.analytics.database_reader import execute_query


def load_customer_data():

    query = """
    SELECT
        c.customer_unique_id,
        MAX(o.order_purchase_timestamp) AS last_purchase,
        COUNT(DISTINCT o.order_id) AS frequency,
        ROUND(SUM(p.payment_value),2) AS monetary
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    JOIN payments p
        ON o.order_id = p.order_id
    GROUP BY c.customer_unique_id;
    """

    return execute_query(query)


if __name__ == "__main__":

    df = load_customer_data()

    print(df.head())

    print()

    print(df.info())