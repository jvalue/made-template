import os
import sqlite3
import pandas as pd

DB_PATH = os.environ["DB_PATH"]

class SqliteClient:
    try:
        db_engine = sqlite3.connect(os.environ["DB_PATH"])
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

    @staticmethod
    def get_data_from_table(table_name: str):
        return pd.read_sql_query(f"select * from {table_name};", SqliteClient.db_engine)