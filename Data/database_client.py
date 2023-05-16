import sqlite3
import os
from os.path import join, dirname
import sqlite3
import sqlalchemy
import pandas as pd

DB_PATH = join(dirname(os.path.abspath('')), os.environ["SQLITE_DB_NAME"])


class SqliteClient:
    db_engine = sqlite3.connect(DB_PATH)
    # db_engine = conn.cursor()

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

    db_engine.execute("""
    CREATE TABLE IF NOT EXISTS train_plan (
    EVA_NR int,
    stop_id text,
    trip_type text,
    train_type text,
    train_number text,
    train_line text,
    platform text,
    next_stations text,
    passed_stations text,
    arrival text,
    departure text,
    FOREIGN KEY (EVA_NR) REFERENCES stations(EVA_NR)
    )
    """)

    db_engine.execute("""
        CREATE TABLE IF NOT EXISTS plan_change(
        EVA_NR int,
        stop_id text,
        next_stations text,
        passed_stations text,
        arrival text,
        departure text,
        platform text,
        FOREIGN KEY (EVA_NR) REFERENCES stations(EVA_NR),
        FOREIGN KEY (stop_id) REFERENCES train_plan(stop_id)
        )
    """)

    def get_data_from_table(self, table_name: str):
        return pd.read_sql_query(f"select * from {table_name}", self.conn)
