from src.analytics.database_reader import execute_query


def main():

    print("=" * 70)
    print("PRODUCT ANALYSIS REPORT")
    print("=" * 70)

    # Top Selling Products
    query_products = """
    SELECT
        oi.product_id,
        COUNT(*) AS total_units_sold,
        ROUND(SUM(oi.price), 2) AS total_revenue
    FROM order_items oi
    GROUP BY oi.product_id
    ORDER BY total_units_sold DESC
    LIMIT 20;
    """

    products_df = execute_query(query_products)

    print("\nTop Selling Products\n")
    print(products_df)

    products_df.to_csv(
        "reports/top_products.csv",
        index=False
    )

    # Top Product Categories
    query_categories = """
    SELECT
        ct.product_category_name_english,
        COUNT(*) AS total_items_sold,
        ROUND(SUM(oi.price),2) AS revenue
    FROM order_items oi
    JOIN products p
        ON oi.product_id = p.product_id
    JOIN category_translation ct
        ON p.product_category_name = ct.product_category_name
    GROUP BY ct.product_category_name_english
    ORDER BY revenue DESC
    LIMIT 20;
    """

    categories_df = execute_query(query_categories)

    print("\nTop Product Categories\n")
    print(categories_df)

    categories_df.to_csv(
        "reports/product_categories.csv",
        index=False
    )

    print("\nReports Generated Successfully!")


if __name__ == "__main__":
    main()