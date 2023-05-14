import sqlite3
from typing import NamedTuple
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(os.path.abspath('')), '.env')
load_dotenv(dotenv_path)



class Station(NamedTuple):
    EVA_NR: int
    DS100: str
    IFOPT: str
    NAME: str
    Verkehr: str
    Laenge: str
    Breite: str
    Betreiber_Name: str
    Betreiber_Nr: int
    Status: str

    db_path = join(dirname(os.path.abspath('')), os.environ["SQLITE_DB_NAME"])
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
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

    def persist_to_sqlite(self):
        self.cursor.execute(
            f"""
            INSERT INTO stations VALUES ({self.EVA_NR}, '{self.DS100}', '{self.IFOPT}', '{self.NAME}',
            '{self.Verkehr}', '{self.Laenge}', '{self.Breite}', '{self.Betreiber_Name}', {self.Betreiber_Nr}, '{self.Status}')
           """
        )



