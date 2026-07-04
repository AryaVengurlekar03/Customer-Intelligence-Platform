from pathlib import Path

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

from src.config.database import DB_CONFIG

BASE_DIR = Path(__file__).resolve().parents[2]
CSV_FILE = BASE_DIR / "data" / "raw" / "olist_order_reviews_dataset.csv"


def load_reviews():

    print("=" * 60)
    print("Loading Reviews Dataset...")
    print("=" * 60)

    df = pd.read_csv(CSV_FILE)

    # Convert date columns
    date_columns = [
        "review_creation_date",
        "review_answer_timestamp",
    ]

    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    # Replace NaN/NaT with None
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

    cur.execute("DELETE FROM reviews")

    rows = [tuple(row) for row in df.itertuples(index=False, name=None)]

    execute_values(
        cur,
        """
        INSERT INTO reviews
        (
            review_id,
            order_id,
            review_score,
            review_comment_title,
            review_comment_message,
            review_creation_date,
            review_answer_timestamp
        )
        VALUES %s
        """,
        rows,
        page_size=1000,
    )

    conn.commit()

    cur.close()
    conn.close()

    print("✅ Reviews loaded successfully!")
    print(f"Inserted {len(rows)} rows.")


if __name__ == "__main__":
    load_reviews()