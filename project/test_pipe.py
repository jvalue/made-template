import unittest
import os
import sqlite3
from Config.basepipeline import ETLPipeline, DataSource, CSVFile, SQLiteDB

class TestDatasetProcessing(unittest.TestCase):
    def setUp(self):
        # You can modify this path based on your project structure
        self.base_path = r'C:\Users\Piyal\Documents\GitHub\MADE-Project\Project'

    def test_bike_pipeline(self):
        # Bike Sharing Data Pipeline Test
        data_source = DataSource(
            data_name="bike data",
            url="https://www.kaggle.com/datasets/hmavrodiev/london-bike-sharing-dataset",
            source_type=DataSource.KAGGLE_DATA,
            files=(CSVFile(
                file_name="london_merged.csv",
                sep=",",
                names=None,
                dtype={
                    "timestamp": "str",
                    "cnt": float,
                    "t1": float,
                    "t2": float,
                    "hum": float,
                    "wind_speed": float,
                    "weather_code": float,
                    "is_holiday": float,
                    "is_weekend": float,
                    "season": float,
                },
                
            ),)
        )

        sqlite_db = SQLiteDB(
            db_name="main.sqlite",
            table_name="bike_data",
            if_exists=SQLiteDB.REPLACE,
            index=False,
            method=None,
            output_directory=os.path.join(self.base_path, "data"),
        )

        bike_pipeline = ETLPipeline(data_source=data_source, sqlite_db=sqlite_db)
        bike_pipeline.run_pipeline()

        # Ensure the SQLite database is created and the table is populated
        db_path = os.path.join(self.base_path, 'data/main.sqlite')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bike_data")
        result = cursor.fetchall()
        conn.close()

        self.assertGreater(len(result), 1, "The 'bike_data' table does not exist.")

    def test_weather_pipeline(self):
        # London Weather Data Pipeline Test
        data_source = DataSource(
            data_name="weather",
            url="https://www.kaggle.com/datasets/emmanuelfwerr/london-weather-data",
            source_type=DataSource.KAGGLE_DATA,
            files=(CSVFile(
                file_name="london_weather.csv",
                sep=",",
                names=None,
                dtype={
                    "date": "Int64",
                    "cloud_cover": float,
                    "sunshine": float,
                    "global_radiation": float,
                    "max_temp": float,
                    "mean_temp": float,
                    "min_temp": float,
                    "precipitation": float,
                    "pressure": "Int64",
                    "snow_depth": float,
                },
            ),)
        )

        sqlite_db = SQLiteDB(
            db_name="main.sqlite",
            table_name="weather",
            if_exists=SQLiteDB.REPLACE,
            index=False,
            method=None,
            output_directory=os.path.join(self.base_path, "data"),
        )

        weather_pipeline = ETLPipeline(data_source=data_source, sqlite_db=sqlite_db)
        weather_pipeline.run_pipeline()

        # Ensure the SQLite database is created and the table is populated
        db_path = os.path.join(self.base_path, 'data/main.sqlite')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM weather")
        result = cursor.fetchall()
        conn.close()

        self.assertGreater(len(result), 1, "The 'weather' table does not exist.")
    
    def test_main_sqlite_exists(self):
        assert os.path.exists("data/main.sqlite")

if __name__ == '__main__':
    unittest.main()

