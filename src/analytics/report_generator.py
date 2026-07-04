from pathlib import Path

import pandas as pd

REPORTS_DIR = Path("reports")
OUTPUT_FILE = REPORTS_DIR / "executive_summary.csv"


def load_report(filename):

    file = REPORTS_DIR / filename

    if file.exists():
        return pd.read_csv(file)

    print(f"Warning: {filename} not found.")
    return None


def main():

    print("=" * 70)
    print("EXECUTIVE REPORT GENERATOR")
    print("=" * 70)

    summary = []

    reports = {
        "Monthly Sales": "monthly_sales.csv",
        "Customer State": "customer_state_summary.csv",
        "Customer City": "customer_city_summary.csv",
        "Top Products": "top_products.csv",
        "Product Categories": "product_categories.csv",
        "Top Sellers": "top_sellers.csv",
        "Seller State": "seller_state_summary.csv",
        "Payment Methods": "payment_method_summary.csv",
        "Delivery by State": "delivery_by_state.csv",
        "Customer Segments": "customer_segments.csv"
    }

    for report_name, filename in reports.items():

        df = load_report(filename)

        if df is not None:

            summary.append({
                "Report": report_name,
                "Rows": len(df),
                "Columns": len(df.columns)
            })

            print(f"✓ {report_name:<25} Loaded ({len(df)} rows)")

    summary_df = pd.DataFrame(summary)

    summary_df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("\n" + "=" * 70)
    print("EXECUTIVE REPORT GENERATED")
    print("=" * 70)

    print(summary_df)

    print(f"\nSaved: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()