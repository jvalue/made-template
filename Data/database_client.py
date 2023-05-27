import os
from os.path import join, dirname

import sqlite3
import sqlalchemy
import pandas as pd

DB_PATH = join(dirname(os.path.abspath('')), os.environ["SQLITE_DB_NAME"])


class SqliteClient:
    try:
        db_engine = sqlite3.connect(os.environ["DB_PATH"])
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

    @staticmethod
    def get_data_from_table(table_name: str):
        return pd.read_sql_query(f"select * from {table_name};", SqliteClient.db_engine)