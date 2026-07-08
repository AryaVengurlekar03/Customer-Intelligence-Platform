from sqlalchemy import text
from src.database.connection import get_engine

TABLES = [
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


def verify_database():
    engine = get_engine()

    with engine.connect() as conn:
        print("\n" + "=" * 60)
        print("DATABASE VERIFICATION")
        print("=" * 60)

        for table in TABLES:
            result = conn.execute(
                text(f"SELECT COUNT(*) FROM {table};")
            ).scalar()

            print(f"{table:<25} {result:,} rows")


if __name__ == "__main__":
    verify_database()