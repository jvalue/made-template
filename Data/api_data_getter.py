import os

from deutsche_bahn_api.api_caller import ApiClient
from database_client import SqliteClient
from deutsche_bahn_api.timetable_retrieval import TimeTableHandler
from deutsche_bahn_api.station_loader import StationLoader


api_client = ApiClient(os.environ["DB_CLIENT_ID"], os.environ["DB_API_KEY"])
station_helper = StationLoader()
station_helper.load_stations()
timetable_handler = TimeTableHandler()


# for station in station_helper.stations_list:
#     station.insert_to_db(SqliteClient.db_engine, "stations")


# TODO: tmp
sample = 100


def get_data_to_database():
    for station in station_helper.stations_list[:sample]:
        response = api_client.get_current_hour_station_timetable(
            station.EVA_NR)
        if response.status_code != 200:
            continue
        else:
            trains_in_this_hour = timetable_handler.get_timetable_data(
                response)
            for train_plan in trains_in_this_hour:
                train_plan.insert_into_db(SqliteClient.db_engine, "train_plan")

    for station in station_helper.stations_list[:sample]:
        response = api_client.get_all_timetable_changes_from_station(
            station.EVA_NR)
        if response.status_code != 200:
            continue
        plans_change = timetable_handler.get_timetable_changes_data(response)
        for plan_change in plans_change:
            plan_change.insert_into_db(SqliteClient.db_engine, "plan_change")

    SqliteClient.db_engine.close()
