import sqlite3
import os
from os.path import join, dirname
import sqlite3
import sqlalchemy
import pandas as pd

DB_PATH = join(dirname(os.path.abspath('')), os.environ["SQLITE_DB_NAME"])


class SqliteClient:
    db_engine = sqlite3.connect(DB_PATH)

    @staticmethod
    def get_data_from_table(table_name: str):
        return pd.read_sql_query(f"select * from {table_name}", SqliteClient.db_engine)
