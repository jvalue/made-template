import os
import pandas as pd

from deutsche_bahn_api.data_processor import DataProcessor

class TrainPlan:
    """A train plan given a station (train in station)."""

    def __init__(self) -> None:
        self.station_id: int
        self.stop_id = None
        self.trip_type = None
        self.train_type = None
        self.train_number = None
        self.train_line = None
        self.platform = None
        self.passed_stations = None
        self.next_stations = None
        self.arrival = None
        self.departure = None
        self.plan_change = None

    def info(self) -> pd.DataFrame:
        df = pd.DataFrame({
            "Station Number": self.station_id,
            "Stop ID": self.stop_id,
            "Train Number": self.train_number,
            "Train Type": self.train_type,
            "Train Line": self.train_line,
            "Passed Stations": self.passed_stations,
            "Planned Stations": self.next_stations,
            "Arrival Time": self.arrival,
            "Departure": self.departure,
            "Platform": self.platform,
        }, index=[0])
        return df

    def __str__(self) -> str:
        return f"TrainPlan(train_number={self.train_number}, train_type={self.train_type}, )"
    
    def insert_into_db(self, db_engine, table_name):
        self.arrival = DataProcessor.process_date_format(self.arrival)
        self.departure = DataProcessor.process_date_format(self.departure)

        db_engine.execute(
            f"""
            INSERT OR REPLACE INTO {table_name} VALUES (
                {self.station_id}, '{self.stop_id}', '{self.trip_type}', '{self.train_type}', '{self.train_number}',
              '{self.train_line}', '{self.platform}', '{self.next_stations}', '{self.passed_stations}', '{self.arrival}', 
              '{self.departure}'
              );
            """
        )
        db_engine.commit()
