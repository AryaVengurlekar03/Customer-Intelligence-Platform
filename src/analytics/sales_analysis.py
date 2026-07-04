import pandas as pd

from src.analytics.database_reader import execute_query


def main():

    print("=" * 70)
    print("SALES ANALYSIS REPORT")
    print("=" * 70)

    # Monthly Revenue
    query = """
    SELECT
        DATE_TRUNC('month', o.order_purchase_timestamp) AS month,
        ROUND(SUM(p.payment_value),2) AS revenue
    FROM orders o
    JOIN payments p
        ON o.order_id = p.order_id
    GROUP BY month
    ORDER BY month;
    """

    monthly_sales = execute_query(query)

    print("\nMonthly Revenue\n")
    print(monthly_sales)

    print("\n" + "=" * 70)

    print("Summary Statistics\n")

    print(monthly_sales.describe())

    print("=" * 70)

    monthly_sales.to_csv(
        "reports/monthly_sales.csv",
        index=False
    )

    print("\n✅ Report saved to reports/monthly_sales.csv")


if __name__ == "__main__":
    main()