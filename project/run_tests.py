import unittest
from unittest.mock import patch, MagicMock
import os
import pandas as pd
from prepare_data import (
    create_temp_directory,
    create_database_engine,
    create_tables,
    download_and_extract_data,
    load_main_and_metadata_files,
    save_to_database,
    clean_up,
)


class TestDataProcessing(unittest.TestCase):

    @patch("os.makedirs")
    def test_create_temp_directory(self, mock_makedirs):
        path = create_temp_directory()
        self.assertTrue(mock_makedirs.called)
        self.assertEqual(path, "project/temp_dir")

    @patch("prepare_data.create_engine")
    def test_create_database_engine(self, mock_create_engine):
        db_path = "data/world_data.sqlite"
        engine = create_database_engine()
        mock_create_engine.assert_called_with(f"sqlite:///{db_path}")
        self.assertIsNotNone(engine)

    @patch("requests.get")
    @patch("zipfile.ZipFile")
    def test_download_and_extract_data(self, mock_zipfile, mock_requests):
        mock_response = MagicMock()
        mock_response.content = b"dummy content"
        mock_requests.return_value = mock_response

        urls = {
            "north_america": "https://api.worldbank.org/v2/en/country/NAC?downloadformat=csv",
            "latin_america_caribbean": "https://api.worldbank.org/v2/en/country/LCN?downloadformat=csv",
        }
        temp_dir = "temp_dir"

        download_and_extract_data(urls, temp_dir)
        self.assertTrue(mock_zipfile.called)

    @patch("os.listdir")
    @patch("pandas.read_csv")
    def test_load_main_and_metadata_files(self, mock_read_csv, mock_listdir):
        mock_listdir.return_value = ["API_data.csv", "Metadata_Indicator.csv"]
        main_files, metadata_files = load_main_and_metadata_files("temp_dir")

        self.assertEqual(main_files, ["API_data.csv"])
        self.assertEqual(metadata_files, ["Metadata_Indicator.csv"])

    @patch("pandas.DataFrame.to_sql")
    def test_save_to_database(self, mock_to_sql):
        merged_df = pd.DataFrame()
        tables = {
            "NAC": MagicMock(),  # Mock for North America table
            "LCN": MagicMock(),  # Mock for Latin America/Caribbean table
        }

        save_to_database(merged_df, "NAC", tables, None)
        self.assertTrue(mock_to_sql.called)
        

    @patch("shutil.rmtree")
    def test_clean_up(self, mock_rmtree):
        clean_up("temp_dir")
        self.assertTrue(mock_rmtree.called)


if __name__ == "__main__":
    unittest.main()