import os
import pandas as pd

from deutsche_bahn_api.api_caller import ApiClient
from deutsche_bahn_api.station_loader import StationLoader
from deutsche_bahn_api.timetable_retrieval import TimeTableHandler
from unittest import TestCase

class DataPipelineTest(TestCase):
    pass

class ApiCallTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.api_client = ApiClient(os.environ["DB_CLIENT_ID"], os.environ["DB_API_KEY"])
        station_helper = StationLoader()
        station_helper.load_stations()
        self.sample_station = station_helper.stations_list[10].EVA_NR

    def test_timetable_station_call_success_status_code(self):
        response = self.api_client.get_current_hour_station_timetable(self.sample_station)
        expected = 200
        assert response.status_code == expected

    def test_plan_change_station_call_success_status_code(self):
        response = self.api_client.get_all_timetable_changes_from_station(self.sample_station)
        expected = 200
        assert response.status_code == expected


class ApiDataProcessorTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.api_client = ApiClient(os.environ["DB_CLIENT_ID"], os.environ["DB_API_KEY"])
        station_helper = StationLoader()
        station_helper.load_stations()
        self.sample_station = station_helper.stations_list[10].EVA_NR
        self.train_plan_handler = TimeTableHandler()

    def test_train_plan_data_existence(self):
        response = self.api_client.get_current_hour_station_timetable(self.sample_station)
        trains_this_hour = self.train_plan_handler.get_timetable_data(response)
        sample_train = trains_this_hour[0]

        assert sample_train.station_id == self.sample_station
        assert sample_train.stop_id is not None
        assert sample_train.arrival is not None
        assert sample_train.departure is not None
        assert sample_train.next_stations is not None

    def test_plan_change_data_existence(self):
        response = self.api_client.get_all_timetable_changes_from_station(self.sample_station)
        plan_changes = self.train_plan_handler.get_timetable_changes_data(response)
        sample_plan_change = plan_changes[0]

        assert sample_plan_change.station_id == self.sample_station
        assert sample_plan_change.stop_id is not None
        assert sample_plan_change.arrival is not None
        assert sample_plan_change.departure is not None
        assert sample_plan_change.next_stations is not None

