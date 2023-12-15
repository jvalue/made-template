import pandas as pd
from sqlalchemy import create_engine
import os
import re
import sqlite3
import kaggle
import requests
# import opendatasets as od
# import shutil
# import zipfile
import ipdb

# class Test:
def Test_run():
    # Connect to SQLite database
    Sqlfilepath = os.path.join(os.getcwd(), "data", "Zomato.sqlite")
    conn = sqlite3.connect(Sqlfilepath)

    # Test case: Selecting the query using PANDAS function to check whether the data is stored in the database.
    query = "SELECT * FROM Zomato"
    df = pd.read_sql_query(query, conn)
    if len(df)>1:
        print("Data exists in SQL file located in the data folder")
    else:
        print("Data does not exist in SQL file")
    # print(df.head())

    # Close the connection
    conn.close()

    
def Test_run_2():
    # Connect to SQLite database
    Sqlfilepath = os.path.join(os.getcwd(), "data", "Banglore.sqlite")
    conn = sqlite3.connect(Sqlfilepath)

    # Test case: Selecting the query using PANDAS function to check whether the data is stored in the database.
    query = "SELECT * FROM Banglore"
    df = pd.read_sql_query(query, conn)
    if len(df)>1:
        print("Data exists in SQL file located in the data folder")
    else:
        print("Data does not exist in SQL file")
    # print(df.head())

    # Close the connection
    conn.close()

def Test_dataset():
    #Step 1 Check Zomato dataset availabke in folder data
    print("Testing Zomato dataset Banglore_1")
    Test_run()
    print("Test run 1 complete fro zomato dataset")

    #Step 2 Check Zomato banglore dataset availabke in folder data
    print("Testing Zomato dataset Banglore_2")
    Test_run_2()
    print("Test run 2 complete for zomato banglore dataset")
    
    print("All Tasks Completed! ")

if __name__ == "__main__":
    Test_dataset()