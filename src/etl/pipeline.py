from src.etl.load import load_csv_to_postgres
from src.etl.transform import (
    transform_dataframe,
    save_interim,
)


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

    datasets = extract_data()

    for table in LOAD_ORDER:

        df = datasets[table]

        validate_dataframe(df, table)

        df = transform_dataframe(df, table)

        csv_file = save_interim(df, table)

    load_csv_to_postgres(csv_file, table)


if __name__ == "__main__":
    run_pipeline()