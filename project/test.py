import unittest
import subprocess
import pandas as pd
import sqlite3
import os

class TestPipeline(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Run the pipeline before tests"""
        subprocess.run(['python3', 'pipeline.py'], check=True)
    
    def test_output_file_exists(self):
        """Test SQLite database file is created"""
        self.assertTrue(os.path.isfile('data/merged_data.sqlite'), "Database file does not exist.")
    
    def test_database_contents(self):
        """Test the contents of the SQLite database"""
        conn = sqlite3.connect('data/merged_data.sqlite')
        cursor = conn.cursor()
        
        # Check if the table 'merged_data' exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='merged_data';")
        table_exists = cursor.fetchone()
        self.assertIsNotNone(table_exists, "Table 'merged_data' does not exist in the database.")
        
        # Check the structure of the table
        df = pd.read_sql_query("SELECT * FROM merged_data", conn)
        
        # Print actual columns for debugging
        print("Actual columns:", df.columns.tolist())
        
        expected_columns = ['Decade', 'Population', 'Temperaturechange']
        self.assertTrue(all(column in df.columns for column in expected_columns), "Column mismatch in 'merged_data' table")
        
        # Check Decade column values
        self.assertTrue(df['Decade'].min() >= 1970, "Decade column has values less than 1970")
        self.assertTrue(df['Decade'].max() <= 2020, "Decade column has values greater than 2020")
        
        # Check null values in Population and Temperaturechange
        self.assertTrue(df['Population'].notnull().all(), "Population column contains null values")
        self.assertTrue(df['Temperaturechange'].notnull().all(), "Temperaturechange column contains null values")

        conn.close()

if __name__ == '__main__':
    unittest.main()
