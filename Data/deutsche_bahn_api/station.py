from typing import NamedTuple

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

    def insert_to_db(self, db_engine, table_name):
        db_engine.execute(
            f"""
            INSERT INTO {table_name} VALUES ({self.EVA_NR}, '{self.DS100}', '{self.IFOPT}', '{self.NAME}',
            '{self.Verkehr}', '{self.Laenge}', '{self.Breite}', '{self.Betreiber_Name}', {self.Betreiber_Nr}, '{self.Status}');
           """

        )
