import pandas as pd
from sqlalchemy import create_engine
import sqlite3
import kaggle

# Download Zomato dataset
kaggle.api.dataset_download_files('rajeshrampure/zomato-dataset', path='/Users/akshatkhara/Desktop/Study Material/Semester 3/Methods of Advance Data Engineering/made-template-WS2324/data', unzip=True)
kaggle.api.dataset_download_files('vora1011/zomato-bangalore-restaurants-2022', path='/Users/akshatkhara/Desktop/Study Material/Semester 3/Methods of Advance Data Engineering/made-template-WS2324/data', unzip=True)


# The dataets are stored in the repository data folder. 
dataset1 = pd.read_csv('/Users/akshatkhara/Desktop/Study Material/Semester 3/Methods of Advance Data Engineering/made-template-WS2324/data/zomato.csv')
dataset2 = pd.read_csv('/Users/akshatkhara/Desktop/Study Material/Semester 3/Methods of Advance Data Engineering/made-template-WS2324/data/BangaloreZomatoData.csv')

# The dataset are stored in Pandas DataFrame to be later stored in SQLLite Database
data1 = pd.DataFrame(dataset1)
data2 = pd.DataFrame(dataset2)

print(data1.head())

# Connect to SQLite database
# conn = sqlite3.connect('/Users/akshatkhara/Desktop/Study Material/Semester 3/Methods of Advance Data Engineering/made-template-WS2324/data/indian_road_accident.db')

# Use the to_sql method to write the DataFrame to a SQLite table
# data1.to_sql('accident_india', conn, index=False, if_exists='replace')

#Optional selceting the query using PANDAS function to check whether the data is stored in the database.
# query = "SELECT * FROM accident_india"
# df = pd.read_sql_query(query, conn)
# print(df.head())

# Close the connection
# conn.close()