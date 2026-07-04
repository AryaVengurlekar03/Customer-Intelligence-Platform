import psycopg2

from src.config.database import DB_CONFIG

TABLES = [

    "customers",

    "orders",

    "products",

    "payments",

    "reviews",

    "order_items",

    "sellers",

    "geolocation",

    "category_translation",

]


conn = psycopg2.connect(
    host=DB_CONFIG["host"],
    port=DB_CONFIG["port"],
    database=DB_CONFIG["database"],
    user=DB_CONFIG["user"],
    password=DB_CONFIG["password"],
)

cur = conn.cursor()

print("=" * 70)

for table in TABLES:

    cur.execute(f"SELECT COUNT(*) FROM {table}")

    rows = cur.fetchone()[0]

    print(f"{table:<25}{rows}")

print("=" * 70)

cur.close()

conn.close()