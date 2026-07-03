from pathlib import Path
import pandas as pd

# Project root
BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DATA_PATH = BASE_DIR / "data" / "raw"

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


def load_csv(filename: str) -> pd.DataFrame:
    file_path = RAW_DATA_PATH / filename

    if not file_path.exists():
        raise FileNotFoundError(f"{filename} not found in {RAW_DATA_PATH}")

    return pd.read_csv(file_path)


def load_all_data():
    datasets = {}

    for name, file in FILES.items():
        datasets[name] = load_csv(file)

    return datasets


if __name__ == "__main__":
    data = load_all_data()

    print("=" * 70)
    print("DATASET SUMMARY")
    print("=" * 70)

    for name, df in data.items():
        print(f"{name:<25} Rows: {len(df):>8} Columns: {len(df.columns):>3}")

    print("=" * 70)