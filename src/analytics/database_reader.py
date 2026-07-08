import pandas as pd
from sqlalchemy import text
from src.database.connection import get_engine


class DatabaseReader:
    """
    Executes SQL queries and returns pandas DataFrames.
    """

    def __init__(self):
        self.engine = get_engine()

    def query(self, sql: str):

        with self.engine.connect() as conn:
            return pd.read_sql(text(sql), conn)