from src.analytics.database_reader import execute_query


def display(title, value):
    print(f"{title:<35}: {value}")


def main():

    print("=" * 60)
    print("CUSTOMER INTELLIGENCE PLATFORM")
    print("EXECUTIVE KPI DASHBOARD")
    print("=" * 60)

    queries = {

        "Total Revenue":
        """
        SELECT ROUND(SUM(payment_value),2)
        FROM payments;
        """,

        "Total Orders":
        """
        SELECT COUNT(*)
        FROM orders;
        """,

        "Total Customers":
        """
        SELECT COUNT(DISTINCT customer_unique_id)
        FROM customers;
        """,

        "Total Sellers":
        """
        SELECT COUNT(*)
        FROM sellers;
        """,

        "Total Products":
        """
        SELECT COUNT(*)
        FROM products;
        """,

        "Average Order Value":
        """
        SELECT ROUND(AVG(payment_value),2)
        FROM payments;
        """
    }

    for title, query in queries.items():

        result = execute_query(query)

        display(title, result.iloc[0, 0])

    print("=" * 60)


if __name__ == "__main__":
    main()