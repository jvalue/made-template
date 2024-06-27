import os
import unittest
import sqlite3


class TestDataPipeline(unittest.TestCase):

    def test_output_files_exist(self):

        self.assertTrue(os.path.isfile('data/KGVQ0.csv'))

        self.assertTrue(os.path.isfile('data/result.db'))

    def test_database_tables_exist(self):

        path = 'data/result.db'
        connection = sqlite3.connect(path)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='tempreture';")
        self.assertIsNotNone(cursor.fetchone())

        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='covid';")
        self.assertIsNotNone(cursor.fetchone())

        connection.close()


if __name__ == '__main__':
    unittest.main()
