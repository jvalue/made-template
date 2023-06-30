import unittest
import os
import pandas as pd
import sqlite3
from project.pipeline import OpenChargeMapAPI, ChargerData, get_state_by_coord

class TestPipeline(unittest.TestCase):

    def test_open_charge_map_api(self):
        # Replace this with your actual Open Charge Map API key
        api_key = "YOUR_API_KEY"

        # Set up the API endpoint and parameters
        open_charge_map_api = OpenChargeMapAPI(api_key)

        # Fetch data from the API
        data = open_charge_map_api.fetch_data()

        # Check if data is fetched successfully
        self.assertIsNotNone(data)
        self.assertTrue(len(data) > 0)

    def test_charger_data_processing(self):
        url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-ladesaulen-in-deutschland/exports/csv"
        charger_data = ChargerData(url)
        charger_data.process_data()

        # Validate the processed DataFrame
        self.assertIsNotNone(charger_data.df_new)
        self.assertTrue(len(charger_data.df_new) > 0)

    def test_geolocation(self):
        # Test the function that gets the state based on coordinates
        # Assuming the given coordinates are correct, the state should not be empty
        state = get_state_by_coord("51.5074, 0.1278")
        self.assertNotEqual(state, '')

    def test_merged_data(self):
        # Assuming you have already run the data pipeline and generated the CSV files,
        # read the CSV files and perform merging to check the result
        df_new = pd.read_csv("./data/mobi_data.csv")
        df_map = pd.read_csv("./data/EV_Charging_Points_Germany.csv")

        # Merge the DataFrames based on the 'State' column
        merged = pd.merge(df_new, df_map, on='State', how='inner')

        # Validate the merged DataFrame
        self.assertIsNotNone(merged)
        self.assertTrue(len(merged) > 0)

    def test_database_creation(self):
        # Assuming you have already run the data pipeline and generated the database file,
        # connect to the database and check if the table exists
        conn = sqlite3.connect('./data/data.db')  # Connect to the database file
        cursor = conn.cursor()

        # Check if the table 'charging_station_data' exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='charging_station_data'")
        table_exists = cursor.fetchone()

        # Validate that the table exists
        self.assertIsNotNone(table_exists)

        # Close the database connection
        conn.close()

if __name__ == '__main__':
    unittest.main()
