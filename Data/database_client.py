
import sqlite3
import os
from os.path import join, dirname
import sqlite3
import sqlalchemy
import pandas as pd

DB_PATH = join(dirname(os.path.abspath('')), os.environ["SQLITE_DB_NAME"])


class SqliteClient:
    conn = sqlite3.connect(DB_PATH)
    db_engine = conn.cursor()

    db_engine.execute("""
CREATE TABLE IF NOT EXISTS stations (
    EVA_NR int,
    DS100 text,
    IFOPT text,
    NAME text,
    Verkehr text,
    Laenge text,
    Breite text,
    Betreiber_Name text,
    Betreiber_Nr int,
    Status text,
    PRIMARY KEY (EVA_NR)
)
""")

    def get_data_from_table(self, table_name: str):
        return pd.read_sql_query(f"select * from {table_name}", self.conn)
