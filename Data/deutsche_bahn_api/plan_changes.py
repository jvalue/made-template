from deutsche_bahn_api.message import Message


class PlanChange:
    """ This class represents changed train attributes. """
    EVA_NR: int
    stop_id: int
    next_stations: str
    passed_stations: str
    arrival: str
    departure: str
    platform: str
    messages: list[Message]


    def insert_into_db(self, db_engine, table_name):
        db_engine.execute(
            f"""
            INSERT INTO {table_name} VALUES (
                {self.EVA_NR}, '{self.stop_id}', '{self.next_stations}', '{self.passed_stations}', 
                '{self.arrival}', '{self.departure}', '{self.platform}'
              )
            """
        )
    