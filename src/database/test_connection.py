import psycopg2
from src.config.database import DB_CONFIG


def test_connection():
    try:
        conn = psycopg2.connect(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            database=DB_CONFIG["database"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
        )

        cursor = conn.cursor()

        cursor.execute("SELECT version();")

        version = cursor.fetchone()

        print("=" * 60)
        print("✅ PostgreSQL Connection Successful!")
        print("=" * 60)
        print("Database :", DB_CONFIG["database"])
        print("User     :", DB_CONFIG["user"])
        print("Host     :", DB_CONFIG["host"])
        print("\nPostgreSQL Version:")
        print(version[0])
        print("=" * 60)

        cursor.close()
        conn.close()

    except Exception as e:
        print("=" * 60)
        print("❌ Connection Failed")
        print(e)
        print("=" * 60)


if __name__ == "__main__":
    test_connection()