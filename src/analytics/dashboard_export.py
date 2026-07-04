from pathlib import Path

import pandas as pd

REPORTS_DIR = Path("reports")
EXPORT_DIR = Path("dashboard_data")

EXPORT_DIR.mkdir(exist_ok=True)


def export_file(filename):

    source = REPORTS_DIR / filename

    if not source.exists():
        print(f"❌ Missing: {filename}")
        return

    df = pd.read_csv(source)

    destination = EXPORT_DIR / filename

    df.to_csv(destination, index=False)

    print(f"✅ Exported {filename}")


def main():

    print("=" * 70)
    print("DASHBOARD EXPORT")
    print("=" * 70)

    files = [

        "monthly_sales.csv",

        "customer_state_summary.csv",

        "customer_city_summary.csv",

        "top_products.csv",

        "product_categories.csv",

        "top_sellers.csv",

        "seller_state_summary.csv",

        "payment_method_summary.csv",

        "payment_installments.csv",

        "top_payments.csv",

        "average_delivery_time.csv",

        "delivery_by_state.csv",

        "delayed_deliveries.csv",

        "early_deliveries.csv",

        "highest_freight_orders.csv",

        "customer_segments.csv",

        "executive_summary.csv"

    ]

    for file in files:

        export_file(file)

    print("\n" + "=" * 70)
    print("Dashboard Export Completed Successfully")
    print("=" * 70)
    print(f"\nExport Folder: {EXPORT_DIR.resolve()}")


if __name__ == "__main__":
    main()