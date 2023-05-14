from __future__ import annotations
from deutsche_bahn_api.plan_changes import PlanChange
import pandas as pd

import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(os.path.abspath('')), '.env')
load_dotenv(dotenv_path)


class TrainPlan:
    """A train given a station (train in station).

    Returns:
        _type_: _description_
    """
    EVA_NR: int
    stop_id: str
    trip_type: str
    train_type: str
    train_number: str
    train_line: str | None
    platform: str
    passed_stations: str | None
    next_stations: str
    arrival: str
    departure: str | None
    plan_change: PlanChange | None

    def info(self) -> pd.DataFrame:
        df = pd.DataFrame({
            "Train Number": self.train_number,
            "Train Type": self.train_type,
            "Platform": self.platform,
            "Arrival Time": self.arrival,
            "Train Line": self.train_line,
            "Departure": self.departure,
            "Planned Stations": self.next_stations,
            "Stop ID": self.stop_id,
        }, index=[0])
        return df

    def __str__(self) -> str:
        return f"TrainPlan(train_number={self.train_number}, train_type={self.train_type}, )"

    def insert_into_db(self, db_engine, table_name):
        db_engine.execute(
            f"""
            INSERT INTO {table_name} VALUES (
                {self.EVA_NR}, '{self.stop_id}', '{self.trip_type}', '{self.train_type}', '{self.train_number}',
              '{self.train_line}', '{self.platform}', '{self.next_stations}', '{self.passed_stations}', '{self.arrival}', 
              '{self.departure}'
              )
            """
        )
