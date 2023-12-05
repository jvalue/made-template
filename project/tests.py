import unittest
from unittest.mock import patch, Mock
import pandas as pd
from pandas.io import sql 
from pathlib import Path
from sqlalchemy import create_engine
import os
import unittest
from pathlib import Path
from pipeline2 import Pipeline  # Replace with the actual module name where your Pipeline class is defined

class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.file1_path = 'https://raw.githubusercontent.com/aiplanethub/Datasets/master/Chronic%20Kidney%20Disease%20(CKD)%20Dataset/ChronicKidneyDisease.csv'
        self.file2_path = 'https://raw.githubusercontent.com/npradaschnor/Pima-Indians-Diabetes-Dataset/master/diabetes.csv'
        self.tablename1 = Path(self.file1_path).stem
        self.tablename2 = Path(self.file2_path).stem
        self.output_directory = 'C:/Users/z004j5vt/made-template-ws2324/data/'
        self.pipeline = Pipeline(self.file1_path, self.file2_path, self.output_directory)

    def test_run_pipeline(self):
        self.pipeline.run_pipeline(self.tablename1, self.tablename2)
        # Check if output files exist
        self.assertTrue(os.path.exists('output_file1.csv'))
        self.assertTrue(os.path.exists('output_file2.csv'))
    
    def test_outcome_to_binary(self):
        # Mock data with a specific column that should be converted to binary
        self.pipeline.df1 = pd.DataFrame({'classification': ['notckd', 'ckd', 'notckd', 'ckd']})
        self.pipeline.outcome_to_binary()
        self.assertTrue(all(self.pipeline.df1['Outcome'].isin([0, 1])))

    def test_normal_to_binary(self):
        # Mock data with a specific column that should be converted to binary
        self.pipeline.df1 = pd.DataFrame({'SomeColumn': ['normal', 'abnormal', 'normal', 'abnormal']})
        self.pipeline.normal_to_binary()
        self.assertTrue(all(self.pipeline.df1['SomeColumn'].isin([0, 1])))  
    def test_present_to_binary(self):
        # Mock data with a specific column that should be converted to binary
        self.pipeline.df1 = pd.DataFrame({'AnotherColumn': ['notpresent', 'present', 'notpresent', 'present']})
        self.pipeline.present_to_binary()
        self.assertTrue(all(self.pipeline.df1['AnotherColumn'].isin([0, 1])))

    def test_good_to_binary(self):
        # Mock data with a specific column that should be converted to binary
        self.pipeline.df1 = pd.DataFrame({'YetAnotherColumn': ['good', 'poor', 'good', 'poor']})
        self.pipeline.good_to_binary()
        self.assertTrue(all(self.pipeline.df1['YetAnotherColumn'].isin([0, 1])))
        
    def test_save_to_sqlite(self):
        # Mock data for testing
        mock_data = {'Column1': [1, 2, 3], 'Column2': ['A', 'B', 'C']}
        mock_df = pd.DataFrame(mock_data)

        # Assign the mock data to the pipeline's df1 (you can adjust this based on your actual data structure)
        self.pipeline.df1 = mock_df
        self.pipeline.df2 = mock_df
        # Specify temporary table names for testing
        temp_table1 = 'temp_table1'
        temp_table2 = 'temp_table2'

        # Run the save_to_sqlite method
        engine = create_engine('sqlite:///:memory:')  # Use an in-memory SQLite database for testing
        self.pipeline.df1.to_sql(temp_table1, engine, index=False)
        self.pipeline.df2.to_sql(temp_table2, engine, index=False)

        # Check if tables exist in the SQLite database
        connection = engine.connect()

        # Check if the temporary tables are present in the SQLite database
        self.assertTrue(connection.dialect.has_table(connection, temp_table1))
        self.assertTrue(connection.dialect.has_table(connection, temp_table2))

        # Clean up: Drop the temporary tables from the SQLite database
        connection.execute(f'DROP TABLE IF EXISTS {temp_table1}')
        connection.execute(f'DROP TABLE IF EXISTS {temp_table2}')

        # Close the database connection
        connection.close()

      

    # Add more test functions as needed

if __name__ == '__main__':
    unittest.main()
