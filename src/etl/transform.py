import pandas as pd


def transform_dataframe(df: pd.DataFrame, table_name: str):

    print(f"Transforming {table_name}...")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove spaces from column names
    df.columns = df.columns.str.strip()

    # Fix Olist column names to match PostgreSQL schema
    if table_name == "products":
        df = df.rename(columns={
            "product_name_lenght": "product_name_length",
            "product_description_lenght": "product_description_length"
        })

    print(f"Finished transforming {table_name}")

    return df