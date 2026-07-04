import pandas as pd


def validate_dataframe(df: pd.DataFrame, table_name: str):

    print("\n" + "=" * 70)
    print(f"VALIDATING {table_name.upper()}")
    print("=" * 70)

    print(f"Rows : {len(df)}")
    print(f"Columns : {len(df.columns)}")

    print(f"Duplicate Rows : {df.duplicated().sum()}")

    print("\nMissing Values")

    print(df.isnull().sum())

    return True