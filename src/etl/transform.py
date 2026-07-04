import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

INTERIM_PATH = BASE_DIR / "data" / "interim"
INTERIM_PATH.mkdir(exist_ok=True)


def transform_dataframe(df, table_name):
    """
    Apply basic transformations to a dataframe.
    """

    print(f"Transforming {table_name}...")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Clean column names
    df.columns = df.columns.str.strip()

    # Replace empty strings with NULL values
    df = df.replace("", pd.NA)

    return df


def save_interim(df, table_name):
    """
    Save transformed dataframe.
    """

    output_file = INTERIM_PATH / f"{table_name}.csv"

    df.to_csv(output_file, index=False)

    print(f"Saved: {output_file.name}")

    return output_file