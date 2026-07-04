from pathlib import Path
import psycopg2
from src.config.database import DB_CONFIG


def get_connection():
    return psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
    )


def load_csv_to_postgres(csv_path: Path, table_name: str):

    conn = get_connection()
    cur = conn.cursor()

    with open(csv_path, "r", encoding="utf-8") as f:

        next(f)  # Skip header

        cur.copy_expert(
            f"""
            COPY {table_name}
            FROM STDIN
            WITH (
                FORMAT CSV,
                DELIMITER ',',
                NULL '',
                HEADER FALSE
            )
            """,
            f,
        )

    conn.commit()

    cur.close()
    conn.close()

    print(f"Loaded {table_name}")