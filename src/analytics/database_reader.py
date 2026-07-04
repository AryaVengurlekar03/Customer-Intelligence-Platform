import pandas as pd
import psycopg2

from src.config.database import DB_CONFIG


def get_connection():
    """
    Create and return a PostgreSQL connection.
    """
    return psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
    )


def read_table(table_name):
    """
    Read an entire table into a Pandas DataFrame.
    """
    conn = get_connection()

    query = f"SELECT * FROM {table_name};"

    df = pd.read_sql(query, conn)

    conn.close()

    return df


def execute_query(query):
    """
    Execute any SQL query and return the result as a DataFrame.
    """
    conn = get_connection()

    df = pd.read_sql(query, conn)

    conn.close()

    return df