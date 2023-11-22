# Python imports
import os

# Third-party imports
import numpy as np
import pandas as pd

# Self imports6
from Config.basepipeline import (
    ETLPipeline,
    DataSource,
    CSVFile,
    SQLiteDB,
)

if __name__ == "__main__":
    data_directory = os.path.join(os.getcwd(), "data")
    
    # Bike Sharing Data Pipeline
    
    bike_output_db = SQLiteDB(
        db_name="main.sqlite",
        table_name="bike_data",
        if_exists=SQLiteDB.REPLACE,
        index=False,
        method=None,
        output_directory=data_directory,
    )
    bike_file_dtype = {
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
    }

    def transform_bike(data_frame: pd.DataFrame):
        
        data_frame = data_frame.rename(columns={"cnt": "new bike shares"})
        data_frame = data_frame.rename(columns={"t1": "real temp"})
        data_frame = data_frame.rename(columns={"t2": "feel temp"})
        return data_frame

    bike_file = CSVFile(
        file_name="london_merged.csv",
        sep=",",
        names=None,
        dtype=bike_file_dtype,
        transform=transform_bike,
    )
    bike_data_source = DataSource(
        data_name="bike data",
        url="https://www.kaggle.com/datasets/hmavrodiev/london-bike-sharing-dataset",
        source_type=DataSource.KAGGLE_DATA,
        files=(bike_file,),
    )
    bike_pipeline = ETLPipeline(
        data_source=bike_data_source,
        sqlite_db=bike_output_db,
    )
    bike_pipeline.run_pipeline()

    # London Weather Data Pipeline
    
    weather_output_db = SQLiteDB(
        db_name="main.sqlite",
        table_name="weather",
        if_exists=SQLiteDB.REPLACE,
        index=False,
        method=None,
        output_directory=data_directory,
    )
    weather_file_dtype = {
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
    }
    

    
    weather_file = CSVFile(
        file_name="london_weather.csv",
        sep=",",
        names=None,
        dtype=weather_file_dtype,
    )
    weather_data_source = DataSource(
        data_name="weather",
        url="https://www.kaggle.com/datasets/emmanuelfwerr/london-weather-data",
        source_type=DataSource.KAGGLE_DATA,
        files=(weather_file,),
    )
    weather_pipeline = ETLPipeline(
        data_source=weather_data_source,
        sqlite_db=weather_output_db,
    )
    weather_pipeline.run_pipeline()