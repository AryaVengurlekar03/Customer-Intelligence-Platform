import psycopg2
from src.config.database import DB_CONFIG

try:
    conn = psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
    )

    print("✅ Connected Successfully!")

    conn.close()

except Exception as e:
    print("❌ Connection Failed")
    print(e)