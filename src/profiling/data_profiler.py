from pathlib import Path
import pandas as pd

# ==========================
# Paths
# ==========================

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DATA = BASE_DIR / "data" / "raw"

REPORT_DIR = BASE_DIR / "reports" / "profiling"

REPORT_DIR.mkdir(parents=True, exist_ok=True)

FILES = {
    "customers": "olist_customers_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "category_translation": "product_category_name_translation.csv",
}


def profile_dataframe(df, name):
    report = []

    report.append(("Dataset", name))
    report.append(("Rows", len(df)))
    report.append(("Columns", len(df.columns)))
    report.append(("Duplicate Rows", df.duplicated().sum()))
    report.append(("Memory Usage (MB)", round(df.memory_usage(deep=True).sum()/1024**2,2)))

    print("\n" + "="*80)
    print(name.upper())
    print("="*80)

    print(f"Shape : {df.shape}")

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nSummary Statistics")
    print(df.describe(include='all').transpose())

    report_df = pd.DataFrame(report, columns=["Metric","Value"])

    report_df.to_csv(REPORT_DIR / f"{name}_summary.csv", index=False)

    print(f"\nReport Saved -> {name}_summary.csv")


def main():

    for dataset, file in FILES.items():

        df = pd.read_csv(RAW_DATA / file)

        profile_dataframe(df, dataset)


if __name__ == "__main__":
    main()