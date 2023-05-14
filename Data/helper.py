import os
from os.path import join, dirname
import sqlite3

db_path = join(dirname(os.path.abspath('')), os.environ["SQLITE_DB_NAME"])
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def get_data_from_sqlite(self):
    self.cursor.execute("select * from stations")
    rows = self.cursor.fetchall()
    return rows