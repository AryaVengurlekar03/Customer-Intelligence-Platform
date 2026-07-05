from pathlib import Path

from src.analytics.database_reader import execute_query

REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)


def main():

    print("=" * 70)
    print("DELIVERY ANALYSIS REPORT")
    print("=" * 70)

    # -------------------------------------------------------
    # Average Delivery Time
    # -------------------------------------------------------

    query_delivery_time = """
    SELECT
        ROUND(
            AVG(
                EXTRACT(EPOCH FROM (
                    order_delivered_customer_date -
                    order_purchase_timestamp
                )) / 86400
            ),
            2
        ) AS average_delivery_days
    FROM orders
    WHERE order_delivered_customer_date IS NOT NULL;
    """

    delivery_df = execute_query(query_delivery_time)

    print("\nAverage Delivery Time\n")
    print(delivery_df)

    delivery_df.to_csv(
        REPORTS_DIR / "average_delivery_time.csv",
        index=False
    )

    # -------------------------------------------------------
    # Delivery Performance by State
    # -------------------------------------------------------

    query_state = """
    SELECT

        c.customer_state,

        ROUND(
            AVG(
                EXTRACT(EPOCH FROM (
                    o.order_delivered_customer_date -
                    o.order_purchase_timestamp
                )) / 86400
            ),
            2
        ) AS average_delivery_days

    FROM customers c

    JOIN orders o
        ON c.customer_id = o.customer_id

    WHERE o.order_delivered_customer_date IS NOT NULL

    GROUP BY c.customer_state

    ORDER BY average_delivery_days DESC;
    """

    state_df = execute_query(query_state)

    print("\nDelivery Performance by State\n")
    print(state_df)

    state_df.to_csv(
        REPORTS_DIR / "delivery_by_state.csv",
        index=False
    )

    # -------------------------------------------------------
    # Delayed Orders
    # -------------------------------------------------------

    query_delayed = """
    SELECT
        COUNT(*) AS delayed_orders
    FROM orders
    WHERE order_delivered_customer_date >
          order_estimated_delivery_date;
    """

    delayed_df = execute_query(query_delayed)

    print("\nDelayed Deliveries\n")
    print(delayed_df)

    delayed_df.to_csv(
        REPORTS_DIR / "delayed_deliveries.csv",
        index=False
    )

    # -------------------------------------------------------
    # Early Orders
    # -------------------------------------------------------

    query_early = """
    SELECT
        COUNT(*) AS early_deliveries
    FROM orders
    WHERE order_delivered_customer_date <
          order_estimated_delivery_date;
    """

    early_df = execute_query(query_early)

    print("\nEarly Deliveries\n")
    print(early_df)

    early_df.to_csv(
        REPORTS_DIR / "early_deliveries.csv",
        index=False
    )

    # -------------------------------------------------------
    # Highest Freight Orders
    # -------------------------------------------------------

    query_freight = """
    SELECT

        order_id,

        ROUND(SUM(freight_value),2) AS freight_cost

    FROM order_items

    GROUP BY order_id

    ORDER BY freight_cost DESC

    LIMIT 20;
    """

    freight_df = execute_query(query_freight)

    print("\nTop Freight Orders\n")
    print(freight_df)

    freight_df.to_csv(
        REPORTS_DIR / "highest_freight_orders.csv",
        index=False
    )

    print("\n" + "=" * 70)
    print("DELIVERY ANALYSIS COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    main()