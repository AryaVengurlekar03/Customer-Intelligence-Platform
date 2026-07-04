import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

from src.config.database import DB_CONFIG


def load_table(df, table_name):
    """
    Load a pandas DataFrame into PostgreSQL.
    """

    print(f"Loading {table_name}...")

    # Convert all NaN values to Python None (PostgreSQL NULL)
    df = df.astype(object)
    df = df.where(pd.notnull(df), None)
    conn = psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
    )

    cur = conn.cursor()

    # Delete old data
    cur.execute(f"DELETE FROM {table_name}")

    rows = [tuple(row) for row in df.itertuples(index=False, name=None)]

    columns = ", ".join(df.columns)

    query = f"""
        INSERT INTO {table_name}
        ({columns})
        VALUES %s
    """

    execute_values(
        cur,
        query,
        rows,
        page_size=1000
    )

    conn.commit()

    print(f"✅ Loaded {len(rows)} rows into {table_name}")

    cur.close()
    conn.close()