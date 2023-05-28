import pandas as pd
import sqlite3
import os
import unittest


class OutputFileTest(unittest.TestCase):
    
    def test_output_file_creation(self):
        file_path = "../data/verkehrszaelungen.sqlite"
        self.assertTrue(os.path.exists(file_path), f"Output file '{file_path}' does not exist.")
        print(f"Output file '{file_path}' exists. Test passed!")

if __name__ == "__main__":
    unittest.main()
