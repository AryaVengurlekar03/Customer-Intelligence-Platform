from pathlib import Path

import pandas as pd

INPUT_FILE = Path("ml_output/customer_clusters.csv")
OUTPUT_FILE = Path("ml_output/customer_cluster_summary.csv")


def generate_cluster_summary():

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            "Run kmeans_model.py first."
        )

    df = pd.read_csv(INPUT_FILE)

    summary = (
        df.groupby("cluster")
        .agg(
            customers=("customer_unique_id", "count"),
            avg_recency=("recency", "mean"),
            avg_frequency=("frequency", "mean"),
            avg_monetary=("monetary", "mean"),
        )
        .round(2)
        .reset_index()
    )

    # Assign Business Labels
    labels = {
        0: "Champions",
        1: "Loyal Customers",
        2: "Potential Loyalists",
        3: "At Risk",
        4: "Budget Buyers"
    }

    summary["segment_name"] = summary["cluster"].map(labels)

    summary.to_csv(OUTPUT_FILE, index=False)

    print("=" * 60)
    print("CUSTOMER CLUSTER SUMMARY")
    print("=" * 60)
    print(summary)
    print("\nSaved:", OUTPUT_FILE)


if __name__ == "__main__":
    generate_cluster_summary()