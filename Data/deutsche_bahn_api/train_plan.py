from __future__ import annotations

import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(os.path.abspath('')), '.env')
load_dotenv(dotenv_path)

import pandas as pd

from deutsche_bahn_api.train_changes import TrainChanges
from Data.database_client import SqliteClient

class TrainPlan:
    """A train given a station (train in station).

    Returns:
        _type_: _description_
    """
    stop_id: str
    trip_type: str
    train_type: str
    train_number: str
    train_line: str | None
    platform: str
    # passed_stations: str | None
    stations: str
    arrival: str
    departure: str | None
    train_changes: TrainChanges | None
    station: str


    def info(self) -> pd.DataFrame:
        df = pd.DataFrame({
            "Train Number": self.train_number,
            "Train Type": self.train_type,
            "Platform": self.platform,
            "Arrival Time": self.arrival,
            "Train Line": self.train_line,
            "Departure": self.departure,
            "Planned Stations": self.stations,
            "Stop ID": self.stop_id,
            }, index=[0])
        return df

    def __str__(self) -> str:
        return f"TrainPlan(train_number={self.train_number}, train_type={self.train_type}, )"
    
    def inset_into_sqlite(self):
        pass