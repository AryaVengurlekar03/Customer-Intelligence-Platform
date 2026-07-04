from pathlib import Path

import pandas as pd

from src.analytics.database_reader import execute_query


REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)


def main():

    print("=" * 70)
    print("CUSTOMER SEGMENTATION (RFM)")
    print("=" * 70)

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

    rfm = execute_query(query)

    # --------------------------
    # Calculate Recency
    # --------------------------

    reference_date = rfm["last_purchase"].max()

    rfm["recency"] = (
        reference_date - rfm["last_purchase"]
    ).dt.days

    # --------------------------
    # RFM Scores
    # --------------------------

    rfm["R"] = pd.qcut(
        rfm["recency"],
        5,
        labels=[5, 4, 3, 2, 1],
        duplicates="drop"
    )

    rfm["F"] = pd.qcut(
        rfm["frequency"].rank(method="first"),
        5,
        labels=[1, 2, 3, 4, 5]
    )

    rfm["M"] = pd.qcut(
        rfm["monetary"],
        5,
        labels=[1, 2, 3, 4, 5],
        duplicates="drop"
    )

    rfm["RFM_SCORE"] = (
        rfm["R"].astype(str)
        + rfm["F"].astype(str)
        + rfm["M"].astype(str)
    )

    # --------------------------
    # Customer Segments
    # --------------------------

    def segment(row):

        r = int(row["R"])
        f = int(row["F"])
        m = int(row["M"])

        if r >= 4 and f >= 4 and m >= 4:
            return "Champions"

        elif r >= 3 and f >= 4:
            return "Loyal Customers"

        elif r >= 4 and f <= 2:
            return "Potential Loyalists"

        elif r <= 2 and f >= 3:
            return "At Risk"

        elif r == 1 and f == 1:
            return "Lost Customers"

        else:
            return "Regular Customers"

    rfm["segment"] = rfm.apply(segment, axis=1)

    print("\nCustomer Segments\n")

    print(
        rfm["segment"]
        .value_counts()
    )

    rfm.to_csv(
        REPORTS_DIR / "customer_segments.csv",
        index=False
    )

    print("\nSaved:")
    print("reports/customer_segments.csv")

    print("=" * 70)


if __name__ == "__main__":
    main()