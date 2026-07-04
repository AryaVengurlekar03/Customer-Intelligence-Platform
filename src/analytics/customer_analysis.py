from src.analytics.database_reader import execute_query


def main():

    print("=" * 70)
    print("CUSTOMER ANALYSIS REPORT")
    print("=" * 70)

    # Total Customers by State
    query_state = """
    SELECT
        customer_state,
        COUNT(*) AS total_customers
    FROM customers
    GROUP BY customer_state
    ORDER BY total_customers DESC;
    """

    state_df = execute_query(query_state)

    print("\nTop States by Customers\n")
    print(state_df.head(10))

    state_df.to_csv(
        "reports/customer_state_summary.csv",
        index=False
    )

    # Top Cities
    query_city = """
    SELECT
        customer_city,
        COUNT(*) AS total_customers
    FROM customers
    GROUP BY customer_city
    ORDER BY total_customers DESC
    LIMIT 20;
    """

    city_df = execute_query(query_city)

    print("\nTop Cities\n")
    print(city_df)

    city_df.to_csv(
        "reports/customer_city_summary.csv",
        index=False
    )

    print("\nReports Generated Successfully")


if __name__ == "__main__":
    main()