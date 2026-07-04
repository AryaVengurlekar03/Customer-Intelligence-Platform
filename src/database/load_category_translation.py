from pathlib import Path

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

from src.config.database import DB_CONFIG

BASE_DIR = Path(__file__).resolve().parents[2]
CSV_FILE = BASE_DIR / "data" / "raw" / "product_category_name_translation.csv"


def load_category_translation():

    print("=" * 60)
    print("Loading Category Translation Dataset...")
    print("=" * 60)

    df = pd.read_csv(CSV_FILE)

    # Replace NaN with None
    df = df.astype(object)
    df = df.where(pd.notnull(df), None)

    print(f"Rows found: {len(df)}")

    conn = psycopg2.connect(
    host=DB_CONFIG["host"],
    port=DB_CONFIG["port"],
    database=DB_CONFIG["database"],
    user=DB_CONFIG["user"],
    password=DB_CONFIG["password"],
)

    print("Connected to database:", DB_CONFIG["database"])

    cur = conn.cursor()

    cur.execute("DELETE FROM category_translation")

    rows = [tuple(row) for row in df.itertuples(index=False, name=None)]

    execute_values(
        cur,
        """
        INSERT INTO category_translation
        (
            product_category_name,
            product_category_name_english
        )
        VALUES %s
        """,
        rows,
        page_size=1000,
    )

    conn.commit()

    cur.close()
    conn.close()

    print("✅ Category Translation loaded successfully!")
    print(f"Inserted {len(rows)} rows.")


if __name__ == "__main__":
    load_category_translation()