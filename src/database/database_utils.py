from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DATA = BASE_DIR / "data" / "raw"

CSV_FILES = {

    "customers":
    "olist_customers_dataset.csv",

    "orders":
    "olist_orders_dataset.csv",

    "products":
    "olist_products_dataset.csv",

    "sellers":
    "olist_sellers_dataset.csv",

    "payments":
    "olist_order_payments_dataset.csv",

    "reviews":
    "olist_order_reviews_dataset.csv",

    "order_items":
    "olist_order_items_dataset.csv",

    "geolocation":
    "olist_geolocation_dataset.csv",

    "category_translation":
    "product_category_name_translation.csv"
}