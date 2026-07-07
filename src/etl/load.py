from src.database.connection import get_engine


def load_dataframe(df, table_name):
    """
    Load DataFrame into PostgreSQL.
    """

    engine = get_engine()

    print(f"Loading {table_name}...")

    try:
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="append",
            index=False,
            chunksize=1000,
            method="multi"
        )

        print(f"✅ {table_name} loaded successfully")

    except Exception as e:
        print(f"\n❌ ERROR loading {table_name}")
        print(e)
        raise