import logging
import unittest
from unittest.mock import patch
import pandas as pd
import sqlite3
from project3 import main

# record program running information using log
logging.basicConfig(filename='data/project3.log',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class SystemTestDataPipeline(unittest.TestCase):
    # mock 2 functions of project3
    @patch('project3.download_dataset')
    @patch('project3.read_csv')
    def test_full_data_pipeline(self, mock_read_csv, mock_download_dataset):

        # Mock download_dataset to return two mocked file paths
        mock_download_dataset.side_effect = [
            "mocked_path/fbi-us/california-crime",
            "mocked_path/kwullum/fatal-police-shootings-in-the-us"
        ]
        logging.info(f"Successfully do mock download dataset")

        # Mock read_csv to return fake DataFrames which each structure is
        # identical to the actual Dataframe's structure
        mock_read_csv.side_effect = [
            # Dataset1: Crime and enforcement data, two DataFrames
            pd.DataFrame({
                'City': ['Alameda'],
                'Population': ['78,613'],
                'Violent crime': [148],
                'Murder and nonnegligent manslaughter': [2],
                'Rape (revised definition)': [7],
                'Rape (legacy definition)': [0],
                'Robbery': [61],
                'Aggravated assault': [78],
                'Property crime': ['1,819'],
                'Burglary': [228],
                'Larceny-theft': ['1,245'],
                'Motor vehicle theft': [346],
                'Arson': [18]
            }),

            pd.DataFrame({
                'City': ['Alameda'],
                'Population': ['78,613'],
                'Total law\renforcement\remployees': [112],
                'Total \rofficers': [83],
                'Total \rcivilians': [29]
            }),

            # Dataset2: Social factors data, three DataFrames
            pd.DataFrame({
                'Geographic Area': ['CA'],
                'City': ['Alameda city'],
                'Median Income': [79312]
            }),

            pd.DataFrame({
                'Geographic Area': ['CA'],
                'City': ['Alameda city'],
                'poverty_rate': [9.8]
            }),

            pd.DataFrame({
                'Geographic Area': ['CA'],
                'City': ['Alameda city'],
                'percent_completed_hs': [91.3]
            }),
        ]
        logging.info(f"Successfully do mock read dataframe")

        # Create a SQLite Database in memory
        conn = sqlite3.connect(":memory:")

        # main function execution
        main(conn=conn)
        logging.info(f"Successfully execute main function")

        # uses cursor object to do validation
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        # save all results in a tuple
        tables = {row[0] for row in cursor.fetchall()}
        print("Tables in database:", tables)
        logging.info(f"Tables in database: {tables}")

        # validates if expected tables are in the tuple
        self.assertIn('crime_enforcement', tables)
        self.assertIn('factors', tables)

        # connection is closed
        conn.close()

        # output result
        print("Test passed: All expected functions were called and database operations were successful.")
        logging.info(f"Test passed: All expected functions were called and database operations were successful.\n")

if __name__ == '__main__':
    unittest.main()
