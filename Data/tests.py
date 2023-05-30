import os
import pandas as pd

from deutsche_bahn_api.api_caller import ApiClient
from deutsche_bahn_api.station_loader import StationLoader
from unittest import TestCase

class DataPipelineTest(TestCase):
    def __init__(self) -> None:
        self.api_client = ApiClient(os.environ["DB_CLIENT_ID"], os.environ["DB_API_KEY"])
        station_helper = StationLoader()
        station_helper.load_stations()
        self.sample_station = station_helper.stations_list[10]

    def test_timetable_station_call_success_status_code(self):
        response = self.api_client.get_current_hour_station_timetable(self.sample_station)
        assert response.status_code == 200

    def test_plan_change_station_call_success_status_code(self):
        response = self.api_client.get_all_timetable_changes_from_station(self.sample_station)
        assert response.status_code == 200



