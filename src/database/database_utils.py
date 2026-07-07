from sqlalchemy import text
from src.database.connection import get_engine


def truncate_tables():
    engine = get_engine()

    tables = [
    "order_items",
    "reviews",
    "payments",
    "orders",
    "products",
    "customers",
    "sellers",
    "geolocation",
    "category_translation"
]

    with engine.begin() as conn:
        for table in tables:
            print(f"Clearing {table}...")
            conn.execute(
                text(f'TRUNCATE TABLE "{table}" RESTART IDENTITY CASCADE;')
            )

    print("✅ Database cleaned.")


if __name__ == "__main__":
    print("database_utils.py is running")
    truncate_tables()