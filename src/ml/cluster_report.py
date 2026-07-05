from pathlib import Path

import pandas as pd

INPUT_FILE = Path("ml_output/customer_cluster_summary.csv")
OUTPUT_FILE = Path("ml_output/cluster_report.txt")


def get_business_insight(segment):

    insights = {
        "Champions":
            "High-value customers with frequent purchases. Reward them with loyalty programs and exclusive offers.",

        "Loyal Customers":
            "Consistent repeat buyers. Encourage referrals and personalized recommendations.",

        "Potential Loyalists":
            "Recently active customers with growth potential. Offer targeted promotions.",

        "At Risk":
            "Customers whose activity has declined. Launch re-engagement campaigns.",

        "Budget Buyers":
            "Price-sensitive customers. Promote discounts and bundle offers."
    }

    return insights.get(segment, "No business insight available.")


def generate_report():

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            "Run customer_clusters.py first."
        )

    df = pd.read_csv(INPUT_FILE)

    report = []

    report.append("=" * 70)
    report.append("CUSTOMER CLUSTER REPORT")
    report.append("=" * 70)
    report.append("")

    for _, row in df.iterrows():

        report.append(f"Cluster ID      : {row['cluster']}")
        report.append(f"Segment Name    : {row['segment_name']}")
        report.append(f"Customers       : {row['customers']}")
        report.append(f"Average Recency : {row['avg_recency']:.2f}")
        report.append(f"Average Frequency : {row['avg_frequency']:.2f}")
        report.append(f"Average Monetary : {row['avg_monetary']:.2f}")
        report.append("Business Insight:")
        report.append(get_business_insight(row["segment_name"]))
        report.append("")
        report.append("-" * 70)
        report.append("")

    report_text = "\n".join(report)

    OUTPUT_FILE.write_text(report_text, encoding="utf-8")

    print(report_text)

    print(f"\n✅ Report saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_report()