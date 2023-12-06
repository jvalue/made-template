import os


import unittest

import sys
project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print(project_directory)
sys.path.insert(0, project_directory)
from pipeline import ETLPipeline, SQLiteDB, CSVFile, DataSource



class TestSystem(unittest.TestCase):

    # System Testing: whole ETL pipeline
    def test_data_pipeline(self):
        # Define your datasets
        population_csv = CSVFile(
            file_name="Population_Berlin.csv",
            sep=",",
            dtype={},
            names=None,
            transform=None,
            compression=None,
            encoding="unicode_escape",
        )

        crime_csv = CSVFile(
            file_name="Berlin_crimes.csv",
            sep=",",
            dtype={},
            names=None,
            transform=None,
            compression=None,
            encoding="utf-8",
        )

        # Update your data sources with the provided links

        # For population data source
        population_data_source = DataSource(
            data_name="Berlin_Population_Dataset",
            url="https://www.kaggle.com/datasets/shreejahoskerenatesh/berlin-district-population",
            source_type=DataSource.KAGGLE_DATA,
            files=(population_csv,),
        )

        # For crime data source
        crime_data_source = DataSource(
            data_name="Berlin_Crime_Dataset",
            url="https://www.kaggle.com/datasets/danilzyryanov/crime-in-berlin-2012-2019",
            source_type=DataSource.KAGGLE_DATA,
            files=(crime_csv,),
        )
        output_directory = os.path.join(project_directory,'data')
        # Define your SQLite database
        sqlite_db = SQLiteDB(
            db_name="my_database.sqlite",
            table_name="Berlin Crime",
            if_exists=SQLiteDB.REPLACE,
            index=False,
            output_directory=output_directory,
            method=None,
        )

        sqlite_db2 = SQLiteDB(
            db_name="my_database.sqlite",
            table_name="population",
            if_exists=SQLiteDB.REPLACE,
            index=False,
            output_directory=output_directory,
            method=None,
        )

        # Create ETL pipelines for each dataset
        population_pipeline = ETLPipeline(data_source=population_data_source, sqlite_db=sqlite_db2)
        crime_pipeline = ETLPipeline(data_source=crime_data_source, sqlite_db=sqlite_db)

        # Run the ETL pipelines
        population_pipeline.run_pipeline()
        crime_pipeline.run_pipeline()


        self.assertTrue(os.path.exists(os.path.join(project_directory, "data", "crime-in-berlin-2012-2019", "Berlin_crimes.csv")))
        self.assertTrue(os.path.exists(os.path.join(project_directory, "data", "berlin-district-population", "Population_Berlin.csv")))
        self.assertTrue(os.path.exists(os.path.join(project_directory, "data", "my_database.sqlite")))

        
