import pandas as pd
from sqlalchemy import create_engine
import os.path
from os import path
import sqlite3

# The dataets are stored in the repository. 
dataset1 = pd.read_csv('/Users/akshatkhara/Desktop/Study Material/Semester 3/Methods of Advance Data Engineering/made-template-WS2324/India_Injury_Road_Accident_Fatality_2017-2020.csv')
dataset2 = pd.read_csv('/Users/akshatkhara/Desktop/Study Material/Semester 3/Methods of Advance Data Engineering/made-template-WS2324/Road Accident Data 2020 India.csv')

# The dataset are stored in Pandas DataFrame to be later stored in SQLLite Database
data1 = pd.DataFrame(dataset1)
data2 = pd.DataFrame(dataset2)

# Connect to SQLite database
conn = sqlite3.connect('/Users/akshatkhara/Desktop/Study Material/Semester 3/Methods of Advance Data Engineering/made-template-WS2324/data/indian_road_accident.db')

# Use the to_sql method to write the DataFrame to a SQLite table
data1.to_sql('accident_india', conn, index=False, if_exists='replace')

#Optional selceting the query using PANDAS function to check whether the data is stored in the database.
# query = "SELECT * FROM accident_india"
# df = pd.read_sql_query(query, conn)
# print(df.head())

# Close the connection
conn.close()


