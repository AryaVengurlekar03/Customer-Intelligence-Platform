from pathlib import Path

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

from src.config.database import DB_CONFIG

BASE_DIR = Path(__file__).resolve().parents[2]
CSV_FILE = BASE_DIR / "data" / "raw" / "olist_order_payments_dataset.csv"


def load_payments():

    print("=" * 60)
    print("Loading Payments Dataset...")
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

    cur.execute("DELETE FROM payments")

    rows = [tuple(row) for row in df.itertuples(index=False, name=None)]

    execute_values(
        cur,
        """
        INSERT INTO payments
        (
            order_id,
            payment_sequential,
            payment_type,
            payment_installments,
            payment_value
        )
        VALUES %s
        """,
        rows,
        page_size=1000,
    )

    conn.commit()

    cur.close()
    conn.close()

    print("✅ Payments loaded successfully!")
    print(f"Inserted {len(rows)} rows.")


if __name__ == "__main__":
    load_payments()