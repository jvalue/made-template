import unittest
import os
from extract_OpenChargerMap import OpenChargeMapAPI

class TestOpenChargeMapAPI(unittest.TestCase):
    def setUp(self):
        api_key = "2777768f-8252-49e0-be9e-297268caa42c"
        self.open_charge_map_api = OpenChargeMapAPI(api_key)

    def test_fetch_data(self):
        data = self.open_charge_map_api.fetch_data()
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
    
    def test_extract_information(self):
        data = [
            {
                "AddressInfo": {
                    "Title": "Address 1",
                    "Town": "Town 1",
                    "StateOrProvince": "State 1",
                    "Postcode": "12345",
                    "Latitude": 1.2345,
                    "Longitude": 5.4321
                },
                "UsageType": {"Title": "Public"},
                "StatusType": {"Title": "Operational"}
            },
            {
                "AddressInfo": {
                    "Title": "Address 2",
                    "Town": "Town 2",
                    "StateOrProvince": "State 2",
                    "Postcode": "54321",
                    "Latitude": 5.4321,
                    "Longitude": 1.2345
                },
                "UsageType": None,
                "StatusType": {"Title": "Unknown"}
            }
        ]
        
        extracted_data = self.open_charge_map_api.extract_information(data)
        
        expected_data = [
            {
                "Title": "Address 1",
                "Town": "Town 1",
                "State": "State 1",
                "Postcode": "12345",
                "Latitude": 1.2345,
                "Longitude": 5.4321,
                "Usage_Type": "Public",
                "Status": "Operational"
            },
            {
                "Title": "Address 2",
                "Town": "Town 2",
                "State": "State 2",
                "Postcode": "54321",
                "Latitude": 5.4321,
                "Longitude": 1.2345,
                "Usage_Type": "N/A",
                "Status": "Unknown"
            }
        ]
        
        self.assertEqual(extracted_data, expected_data)

    def test_save_to_csv(self):
        data = [
            {
                "Title": "Address 1",
                "Town": "Town 1",
                "State": "State 1",
                "Postcode": "12345",
                "Latitude": 1.2345,
                "Longitude": 5.4321,
                "Usage_Type": "Public",
                "Status": "Operational"
            },
            {
                "Title": "Address 2",
                "Town": "Town 2",
                "State": "State 2",
                "Postcode": "54321",
                "Latitude": 5.4321,
                "Longitude": 1.2345,
                "Usage_Type": "N/A",
                "Status": "Unknown"
            }
        ]
        
        csv_file_path = "test_output.csv"
        self.open_charge_map_api.save_to_csv(data, csv_file_path)
        
        self.assertTrue(os.path.isfile(csv_file_path))
        os.remove(csv_file_path)

if __name__ == "__main__":
    unittest.main()
