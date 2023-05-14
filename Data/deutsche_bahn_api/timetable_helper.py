from __future__ import annotations
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

from datetime import datetime, timedelta
from typing import Optional

import requests
import xml.etree.ElementTree as elementTree

from deutsche_bahn_api.api_authentication import ApiAuthentication
from deutsche_bahn_api.message import Message, resolve_message_by_code
from deutsche_bahn_api.station import Station
from deutsche_bahn_api.train_plan import TrainPlan
from deutsche_bahn_api.plan_changes import PlanChange


class TimetableHelper:
    station: Station
    api_authentication: ApiAuthentication

    def __init__(self, station: Station, api_authentication: ApiAuthentication) -> None:
        self.station = station
        self.api_authentication = api_authentication

    def get_timetable_xml(self, hour: Optional[int] = None, date: Optional[datetime] = None) -> str:
        hour_date: datetime = datetime.now()
        if hour:
            hour_date = datetime.strptime(str(hour), "%H")
        date_string: str = datetime.now().strftime("%y%m%d")
        if date is not None:
            date_string = date.strftime("%y%m%d")
        hour: str = hour_date.strftime("%H")
        response = requests.get(
            f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1"
            f"/plan/{self.station.EVA_NR}/{date_string}/{hour}",
            headers=self.api_authentication.get_headers()
        )
        if response.status_code == 410:
            return self.get_timetable_xml(int(hour), datetime.now() + timedelta(days=1))
        elif response.status_code == 401:
            raise Exception("Can't request timetable because the credentials are not correct. Please make sure that "
                            "you providing the correct credentials.")
        elif response.status_code != 200:
            raise Exception("Can't request timetable! The request failed with the HTTP status code {}: {}"
                            .format(response.status_code, response.text))
        return response.text

    def get_timetable(self, hour: Optional[int] = None) -> list[TrainPlan]:
        train_list: list[TrainPlan] = []
        trains = elementTree.fromstringlist(self.get_timetable_xml(hour))
        for train in trains:
            trip_label_object: dict[str, str] | None = None
            arrival_object: dict[str, str] | None = None
            departure_object: dict[str, str] | None = None
            for train_details in train:
                if train_details.tag == "tl":
                    trip_label_object = train_details.attrib
                if train_details.tag == "dp":
                    departure_object = train_details.attrib
                if train_details.tag == "ar":
                    arrival_object = train_details.attrib

            if not departure_object:
                """ Arrival without department """
                continue

            train_object: TrainPlan = TrainPlan()
            train_object.EVA_NR = self.station.EVA_NR
            train_object.stop_id = train.attrib["id"]
            train_object.train_type = trip_label_object["c"]
            train_object.train_number = trip_label_object["n"]
            train_object.platform = departure_object['pp']
            train_object.next_stations = departure_object['ppth']
            train_object.departure = departure_object['pt']

            if "f" in trip_label_object:
                train_object.trip_type = trip_label_object["f"]

            if "l" in departure_object:
                train_object.train_line = departure_object['l']
            else:
                train_object.train_line = "N/A"

            if arrival_object:
                train_object.passed_stations = arrival_object['ppth']
                train_object.arrival = arrival_object['pt']
            else:
                train_object.arrival = "N/A"
                train_object.passed_stations = "N/A"

            train_list.append(train_object)

        return train_list

    def get_timetable_changes(self, trains: list) -> list[TrainPlan]:
        response = requests.get(
            f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/fchg/{self.station.EVA_NR}",
            headers=self.api_authentication.get_headers()
        )
        changed_trains = elementTree.fromstringlist(response.text)

        train_plans = []
        plans_change = []

        for changed_train in changed_trains:
            found_train: TrainPlan | None = None
            plan_change: PlanChange = PlanChange()
            plan_change.messages = []
            plan_change.EVA_NR = self.station.EVA_NR

            for train_plan in trains:
                if train_plan.stop_id == changed_train.attrib["id"]:
                    found_train = train_plan
                    plan_change.stop_id = train_plan.stop_id

            if not found_train:
                train_plan.plan_change = None
                continue

            for changes in changed_train:
                if changes.tag == "dp":
                    if "ct" in changes.attrib:
                        plan_change.departure = changes.attrib["ct"]
                    if "cpth" in changes.attrib:
                        plan_change.next_stations = changes.attrib["cpth"]
                    else:
                        plan_change.next_stations = "N/A"
                    if "cp" in changes.attrib:
                        plan_change.platform = changes.attrib["cp"]
                    else:
                        plan_change.platform = "N/A"
                else:
                    plan_change.departure = "N/A"
                    plan_change.next_stations = "N/A"
                    plan_change.platform = "N/A"
                    plan_change.platform = "N/A"

                if changes.tag == "ar":
                    if "ct" in changes.attrib:
                        plan_change.arrival = changes.attrib["ct"]
                    if "cpth" in changes.attrib:
                        plan_change.passed_stations = changes.attrib["cpth"]
                    else:
                        plan_change.passed_stations = "N/A"
                else:
                    plan_change.arrival = "N/A"
                    plan_change.passed_stations = "N/A"


                for message in changes:
                    new_message = Message()
                    new_message.id = message.attrib["id"]
                    new_message.code = message.attrib["c"]
                    new_message.time = message.attrib["ts"]
                    new_message.message = resolve_message_by_code(int(message.attrib["c"]))
                    plan_change.messages.append(new_message)
                    
            plans_change.append(plan_change)
            found_train.plan_change = plan_change
            train_plans.append(found_train)

        return train_plans
