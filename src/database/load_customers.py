from pathlib import Path

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

from src.config.database import DB_CONFIG


BASE_DIR = Path(__file__).resolve().parents[2]
CSV_FILE = BASE_DIR / "data" / "raw" / "olist_customers_dataset.csv"


def load_customers():

    print("=" * 60)
    print("Loading Customers Dataset...")
    print("=" * 60)

    # Read CSV
    df = pd.read_csv(CSV_FILE)

    print(f"Rows found: {len(df)}")

    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
    )

    cur = conn.cursor()

    # Clear existing data (safe because table is currently empty)
    cur.execute("DELETE FROM customers")

    # Prepare rows
    rows = [
        (
            row.customer_id,
            row.customer_unique_id,
            int(row.customer_zip_code_prefix),
            row.customer_city,
            row.customer_state,
        )
        for row in df.itertuples(index=False)
    ]

    execute_values(
        cur,
        """
        INSERT INTO customers
        (
            customer_id,
            customer_unique_id,
            customer_zip_code_prefix,
            customer_city,
            customer_state
        )
        VALUES %s
        """,
        rows,
        page_size=1000,
    )

    conn.commit()

    cur.close()
    conn.close()

    print("✅ Customers loaded successfully!")
    print(f"Inserted {len(rows)} rows.")


if __name__ == "__main__":
    load_customers()