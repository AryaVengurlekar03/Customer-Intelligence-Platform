from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DATA_PATH = BASE_DIR / "data" / "raw"


DATASETS = {
    "customers": "olist_customers_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "products": "olist_products_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "category_translation": "product_category_name_translation.csv",
}


def extract_data():
    """
    Read all CSV files into pandas DataFrames.
    """

    datasets = {}

    for table, filename in DATASETS.items():

        file_path = RAW_DATA_PATH / filename

        print(f"Reading {filename}...")

        datasets[table] = pd.read_csv(file_path)

    return datasets


if __name__ == "__main__":
    datasets = extract_data()

    print("\n" + "=" * 60)
    print("DATASETS LOADED SUCCESSFULLY")
    print("=" * 60)

    for name, df in datasets.items():
        print(f"{name}: {df.shape}")