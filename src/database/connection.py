from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import text
from src.config.database import DB_CONFIG


def get_engine():
    url = URL.create(
        drivername="postgresql+psycopg2",
        username=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        host=DB_CONFIG["host"],
        port=int(DB_CONFIG["port"]),
        database=DB_CONFIG["database"],
    )

    return create_engine(url)


if __name__ == "__main__":
    print("Connecting to PostgreSQL...")

    try:
        engine = get_engine()

        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))

        print("✅ Connected Successfully!")

    except Exception as e:
        print("❌ Connection Failed")
        print(e)