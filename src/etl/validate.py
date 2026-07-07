import pandas as pd
from src.etl.extract import extract_data


def validate_dataframe(df: pd.DataFrame, table_name: str):
    """
    Validate a dataframe before loading it.
    """

    print("\n" + "=" * 70)
    print(f"VALIDATING: {table_name.upper()}")
    print("=" * 70)

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\nColumn Names:")
    print(list(df.columns))

    print("\nMissing Values:")
    print(df.isnull().sum())

    print(f"\nDuplicate Rows: {df.duplicated().sum()}")

    print("\nData Types:")
    print(df.dtypes)

    print("=" * 70)


if __name__ == "__main__":

    datasets = extract_data()

    for table_name, dataframe in datasets.items():
        validate_dataframe(dataframe, table_name)