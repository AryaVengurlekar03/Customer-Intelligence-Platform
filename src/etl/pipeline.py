from src.etl.extract import extract_data
from src.etl.validate import validate_dataframe
from src.etl.transform import transform_dataframe
from src.etl.load import load_dataframe
from src.database.database_utils import truncate_tables

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


def run_pipeline():
    truncate_tables()
    datasets = extract_data()

    for table in LOAD_ORDER:

        print(f"\n{'=' * 70}")
        print(f"Processing {table}")
        print(f"{'=' * 70}")

        df = datasets[table]

        validate_dataframe(df, table)

        df = transform_dataframe(df, table)

        load_dataframe(df, table)

    print("\n🎉 ETL Pipeline Completed Successfully!")


if __name__ == "__main__":
    print("🚀 Starting ETL Pipeline...")
    run_pipeline()