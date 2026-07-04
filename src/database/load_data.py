import pandas as pd

from src.database.connection import get_engine
from src.database.database_utils import CSV_FILES, RAW_DATA

engine = get_engine()

LOAD_ORDER = [

    "customers",

    "products",

    "sellers",

    "orders",

    "payments",

    "reviews",

    "order_items",

    "geolocation",

    "category_translation"

]


for table in LOAD_ORDER:

    print("=" * 70)

    print(f"Loading {table}")

    df = pd.read_csv(
        RAW_DATA / CSV_FILES[table]
    )

    print(df.shape)

    df.to_sql(
        table,
        engine,
        if_exists="append",
        index=False
    )

    print(f"{table} Loaded Successfully")

print("=" * 70)

print("ALL TABLES LOADED")