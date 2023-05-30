import os
import sys
sys.path.append(os.path.dirname(os.path.abspath('')))
from dotenv import load_dotenv
load_dotenv(".env")

import pandas as pd

from Data.database_client import SqliteClient
from Data.deutsche_bahn_api.api_caller import ApiClient
from Data.deutsche_bahn_api.station_loader import StationLoader
from Data.deutsche_bahn_api.timetable_retrieval import TimeTableHandler

from unittest import TestCase

api_client = ApiClient(os.environ["DB_CLIENT_ID"], os.environ["DB_API_KEY"])
station_loader = StationLoader()
station_loader.load_stations()
sample_station = station_loader.stations_list[10].EVA_NR



class TestDataPipeline(TestCase):

    def test_pipeline(self):
        self.station_loader = StationLoader()
        self.api_client = ApiClient(os.environ["DB_CLIENT_ID"], os.environ["DB_API_KEY"])
        self.timetable_handler = TimeTableHandler()
        self.sqlite_client = SqliteClient()
        self.station_loader.load_stations()
        self.sample_station = self.station_loader.stations_list[10].EVA_NR
        response = self.api_client.get_current_hour_station_timetable(sample_station)
        trains_this_hour = self.timetable_handler.get_timetable_data(response)
        response = self.api_client.get_all_timetable_changes_from_station(sample_station)
        plan_changes = self.timetable_handler.get_timetable_changes_data(response)
        
        sample_plan_change = plan_changes[0]
        sample_train = trains_this_hour[0]
        sample_train.insert_into_db(SqliteClient.db_engine, os.environ["TRAIN_PLAN_TABLE"])
        sample_plan_change.insert_into_db(SqliteClient.db_engine, os.environ["PLAN_CHANGE_TABLE"])

        df = pd.read_sql(f"select * from {os.environ['TRAIN_PLAN_TABLE']}", SqliteClient.db_engine)
        df = df.query(f"EVA_NR == {sample_train.EVA_NR}")
        self.assertGreater(len(df), 0)

        df = pd.read_sql(f"select * from {os.environ['PLAN_CHANGE_TABLE']}", SqliteClient.db_engine)
        df = df.query(f"EVA_NR == {sample_plan_change.EVA_NR}")
        self.assertGreater(len(df), 0)


class StationLoaderTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.station_loader = StationLoader()

    def _test_station_loader(self):
        self.station_loader.load_stations()
        expected = "Station(EVA_NR=8002551, DS100='AELB', IFOPT='de:02000:11943', NAME='Hamburg Elbbrücken', Verkehr='RV', Laenge='10,0245', Breite='53,5345', Betreiber_Name='DB Station und Service AG', Betreiber_Nr=0, Status='neu')"
        actual = self.station_loader.stations_list[0]
        self.assertEqaual(actual, expected)

    def test_stations_number(self):
        self.station_loader.load_stations()
        expected = 6519
        assert len(self.station_loader.stations_list) == expected


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


class TimeTableDataHandlerTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sample_station = station_loader.stations_list[10].EVA_NR
        self.timetable_handler = TimeTableHandler()

    def test_train_plan_data_existence(self):
        response = api_client.get_current_hour_station_timetable(self.sample_station)
        trains_this_hour = self.timetable_handler.get_timetable_data(response)
        sample_train = trains_this_hour[0]

        assert sample_train.EVA_NR == self.sample_station
        assert sample_train.stop_id is not None
        assert sample_train.arrival is not None
        assert sample_train.departure is not None
        assert sample_train.next_stations is not None

    def test_plan_change_data_existence(self):
        response = api_client.get_all_timetable_changes_from_station(self.sample_station)
        plan_changes = self.timetable_handler.get_timetable_changes_data(response)
        sample_plan_change = plan_changes[0]

        assert sample_plan_change.EVA_NR == self.sample_station
        assert sample_plan_change.stop_id is not None
        assert sample_plan_change.arrival is not None
        assert sample_plan_change.departure is not None
        assert sample_plan_change.next_stations is not None

class SqliteInsertionTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.timetable_handler = TimeTableHandler()

    def test_train_plan_insertion(self):
        response = api_client.get_current_hour_station_timetable(sample_station)
        trains_this_hour = self.timetable_handler.get_timetable_data(response)
        sample_train = trains_this_hour[0]

        sample_train.insert_into_db(SqliteClient.db_engine, os.environ["TRAIN_PLAN_TABLE"])

        df = pd.read_sql(f"select * from {os.environ['TRAIN_PLAN_TABLE']}", SqliteClient.db_engine)
        df = df.query(f"EVA_NR == {sample_train.EVA_NR}")

        assert len(df) > 0

    def test_plan_change_insertion(self):
        response = api_client.get_all_timetable_changes_from_station(sample_station)
        plan_changes = self.timetable_handler.get_timetable_changes_data(response)
        sample_plan_change = plan_changes[0]

        sample_plan_change.insert_into_db(SqliteClient.db_engine, os.environ["PLAN_CHANGE_TABLE"])
        
        df = pd.read_sql(f"select * from {os.environ['PLAN_CHANGE_TABLE']}", SqliteClient.db_engine)
        df = df.query(f"EVA_NR == {sample_plan_change.EVA_NR}")

        assert len(df) > 0



