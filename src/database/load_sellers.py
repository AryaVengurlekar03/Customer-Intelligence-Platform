from pathlib import Path

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

from src.config.database import DB_CONFIG

BASE_DIR = Path(__file__).resolve().parents[2]
CSV_FILE = BASE_DIR / "data" / "raw" / "olist_sellers_dataset.csv"


def load_sellers():

    print("=" * 60)
    print("Loading Sellers Dataset...")
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

    cur = conn.cursor()

    cur.execute("DELETE FROM sellers")

    rows = [tuple(row) for row in df.itertuples(index=False, name=None)]

    execute_values(
        cur,
        """
        INSERT INTO sellers
        (
            seller_id,
            seller_zip_code_prefix,
            seller_city,
            seller_state
        )
        VALUES %s
        """,
        rows,
        page_size=1000,
    )

    conn.commit()

    cur.close()
    conn.close()

    print("✅ Sellers loaded successfully!")
    print(f"Inserted {len(rows)} rows.")


if __name__ == "__main__":
    load_sellers()