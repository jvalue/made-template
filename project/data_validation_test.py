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
def Test_file():
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

def Check_null():
    # Connect to SQLite database
    Sqlfilepath = os.path.join(os.getcwd(), "data", "Zomato.sqlite")
    conn = sqlite3.connect(Sqlfilepath)

    # Test case: Selecting the query using PANDAS function to check whether the data is stored in the database.
    query = "SELECT * FROM Zomato"
    df = pd.read_sql_query(query, conn)
    if df.isnull().any().any():
        print("DataFrame contains null values.")
    else:
        print("DataFrame does not contain null values.")
    # print(df.head())

    # Close the connection
    conn.close()
    
def Test_file_2():
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

def Check_null_2():
    # Connect to SQLite database
    Sqlfilepath = os.path.join(os.getcwd(), "data", "Banglore.sqlite")
    conn = sqlite3.connect(Sqlfilepath)

    # Test case: Selecting the query using PANDAS function to check whether the data is stored in the database.
    query = "SELECT * FROM Banglore"
    df = pd.read_sql_query(query, conn)
    if df.isnull().any().any():
        print("DataFrame contains null values.")
    else:
        print("DataFrame does not contain null values.")
    # print(df.head())

    # Close the connection
    conn.close()

def Test_dataset():
    #Step 1 Check Zomato dataset availabke in folder data
    print("Testing if data exists in Zomato dataset Banglore_1")
    Test_file()
    print("Test run 1.1 complete for zomato dataset")

    #Step 2 Check Zomato dataset availabke in folder data
    print("Testing to check null values in Zomato dataset Banglore_1")
    Check_null()
    print("Test run 1.2 complete for zomato dataset")

    #Step 3 Check Zomato banglore dataset availabke in folder data
    print("Testing if data exists in Zomato dataset Banglore_2")
    Test_file_2()
    print("Test run 2.1 complete for zomato banglore dataset")

    #Step 4 Check Zomato banglore dataset availabke in folder data
    print("Testing to check null values in Zomato dataset Banglore_2")
    Check_null_2()
    print("Test run 2.2 complete for zomato banglore dataset")
    
    print("All Test runs Completed :)")

if __name__ == "__main__":
    Test_dataset()