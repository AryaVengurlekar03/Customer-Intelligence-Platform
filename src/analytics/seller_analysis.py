from src.analytics.database_reader import execute_query


def main():

    print("=" * 70)
    print("SELLER ANALYSIS REPORT")
    print("=" * 70)

    # Top Sellers by Revenue
    query_revenue = """
    SELECT
        oi.seller_id,
        COUNT(DISTINCT oi.order_id) AS total_orders,
        ROUND(SUM(oi.price), 2) AS total_revenue,
        ROUND(AVG(oi.price), 2) AS average_order_value
    FROM order_items oi
    GROUP BY oi.seller_id
    ORDER BY total_revenue DESC
    LIMIT 20;
    """

    revenue_df = execute_query(query_revenue)

    print("\nTop Sellers by Revenue\n")
    print(revenue_df)

    revenue_df.to_csv(
        "reports/top_sellers.csv",
        index=False
    )

    # Seller Performance by State
    query_state = """
    SELECT
        s.seller_state,
        COUNT(DISTINCT s.seller_id) AS total_sellers,
        ROUND(SUM(oi.price),2) AS total_revenue
    FROM sellers s
    JOIN order_items oi
        ON s.seller_id = oi.seller_id
    GROUP BY s.seller_state
    ORDER BY total_revenue DESC;
    """

    state_df = execute_query(query_state)

    print("\nSeller Performance by State\n")
    print(state_df)

    state_df.to_csv(
        "reports/seller_state_summary.csv",
        index=False
    )

    # Highest Rated Sellers
    query_rating = """
    SELECT
        oi.seller_id,
        ROUND(AVG(r.review_score),2) AS average_rating,
        COUNT(r.review_id) AS total_reviews
    FROM order_items oi
    JOIN reviews r
        ON oi.order_id = r.order_id
    GROUP BY oi.seller_id
    HAVING COUNT(r.review_id) >= 20
    ORDER BY average_rating DESC
    LIMIT 20;
    """

    rating_df = execute_query(query_rating)

    print("\nTop Rated Sellers\n")
    print(rating_df)

    rating_df.to_csv(
        "reports/top_rated_sellers.csv",
        index=False
    )

    print("\n✅ Seller reports generated successfully!")


if __name__ == "__main__":
    main()