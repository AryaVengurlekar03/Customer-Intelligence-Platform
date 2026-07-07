from sqlalchemy import text
from src.database.connection import get_engine


def truncate_tables():
    """
    Remove all data from tables before loading fresh data.
    """

    engine = get_engine()

    tables = [
        "order_items",
        "order_reviews",
        "order_payments",
        "orders",
        "products",
        "customers",
        "sellers",
        "geolocation",
        "product_category_translation"
    ]

    with engine.begin() as conn:
        for table in tables:
            print(f"Clearing {table}...")
            conn.execute(text(f'TRUNCATE TABLE "{table}" RESTART IDENTITY CASCADE;'))

    print("\n✅ Database cleared successfully.")