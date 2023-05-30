import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
grand_parentdir = os.path.dirname(parentdir)
sys.path.insert(0, grand_parentdir)

from logger import get_file_logger
_logger = get_file_logger(__name__, 'debug')

import requests
from datetime import datetime

class ApiClient:
    def __init__(self, client_id, client_secret) -> None:
        self.client_id = client_id
        self.client_secret = client_secret

        self.headers = {
                "DB-Api-Key": self.client_secret,
                "DB-Client-Id": self.client_id,
            }

    def get_hour_station_timetable(self, station_number, hour):
        hour_date = datetime.strptime(str(hour), "%H")
        hour = hour_date.strftime("%H")
        current_date = datetime.now().strftime("%y%m%d")
        
        response = requests.get(
            f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1"
            f"/plan/{station_number}/{current_date}/{hour}",
            headers=self.headers
        )
        return response

    def get_current_hour_station_timetable(self, station_number):
        current_hour = datetime.now().strftime("%H")
        current_date = datetime.now().strftime("%y%m%d")

        response = requests.get(
            f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1"
            f"/plan/{station_number}/{current_date}/{current_hour}",
            headers=self.headers
        )
        response.EVA_NR = station_number
        return response

    def get_all_timetable_changes_from_station(self, station_number: int) -> str:
        response = requests.get(
            f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/fchg/{station_number}",
            headers=self.headers
        )
        return response
    
    def __str__(self) -> str:
        return "ApiClient(DB_CLIENT_ID=***, DB_API_KEY=***)"
    


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv(".env")

    api = ApiClient(os.environ["DB_CLIENT_ID"], os.environ["DB_API_KEY"])
    response = api.get_current_hour_station_timetable(8000107)

