from __future__ import annotations
import pandas as pd

from deutsche_bahn_api.train_changes import TrainChanges


class Train:
    stop_id: str
    trip_type: str
    train_type: str
    train_number: str
    train_line: str | None
    platform: str
    passed_stations: str | None
    stations: str
    arrival: str
    departure: str | None
    train_changes: TrainChanges | None


    def info(self) -> pd.DataFrame:
        df = pd.DataFrame({
            "Train Number": self.train_number,
            "Train Type": self.train_type,
            "Platform": self.platform,
            # "Arrival Time": self.arrival,
            # "Train Line": self.train_line,
            "Departure": self.departure,
            "Planned Stations": self.stations,
            "Stop ID": self.stop_id,
            }, index=[0])
        return df
