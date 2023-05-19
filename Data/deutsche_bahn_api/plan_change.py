import pandas as pd

from deutsche_bahn_api.data_processor import DataProcessor

class PlanChange:
    """ This class represents changed train attributes. """

    def __init__(self) -> None:
        self.station_number = "N/A"
        self.stop_id = "N/A"
        self.next_stations = "N/A"
        self.passed_stations = "N/A"
        self.arrival = "N/A"
        self.departure = "N/A"
        self.platform = "N/A"

    def insert_into_db(self, db_engine, table_name):
        self.arrival = DataProcessor.process_date_format(self.arrival)
        self.departure = DataProcessor.process_date_format(self.departure)

        db_engine.execute(
            f"""
            INSERT INTO {table_name} VALUES (
                {self.station_number}, '{self.stop_id}', '{self.next_stations}', '{self.passed_stations}', 
                '{self.arrival}', '{self.departure}', '{self.platform}'
              )
            """
        )
        db_engine.commit()
    
    def info(self) -> pd.DataFrame:
        df = pd.DataFrame({
            "Station Number": self.station_number,
            "Stop ID": self.stop_id,
            "Passed Stations": self.passed_stations,
            "Next Stations": self.next_stations,
            "Arrival Time": self.arrival,
            "Departure Time": self.departure,
            "Platform": self.platform,
        }, index=[0])
        return df
