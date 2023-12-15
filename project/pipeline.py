import pandas as pd
from sqlalchemy import create_engine
import os
import re
import sqlite3
import kaggle
import requests
import opendatasets as od
import shutil
import zipfile
import ipdb

# class DataPipeline:

def download_csv_files():
    kaggle.api.authenticate()
    dataset_path = os.path.join(os.getcwd(), "data")
    banglore_csv = os.path.join(os.getcwd(), "data/BangaloreZomatoData.csv")

    # Download Zomato Dataset 1
    source_path1 = os.path.join(os.getcwd(), "zomato-dataset")
    zomato_csv = os.path.join(os.getcwd(), "data/zomato.csv")
    od.download('https://www.kaggle.com/datasets/rajeshrampure/zomato-dataset/data')

    # Gather all files
    allfiles = os.listdir(source_path1)
    
    # iterate on all files to move them to destination folder
    for f in allfiles:
        src_path = os.path.join(source_path1, f)
        dst_path = os.path.join(dataset_path, f)
        shutil.move(src_path, dst_path)

    zomato_banglore_1 = pd.read_csv(zomato_csv)
    zomato_banglore_1_df = pd.DataFrame(zomato_banglore_1)
    shutil.rmtree("zomato-dataset")

    # Download Zomato Banglore Dataset 2
    source_path2 = os.path.join(os.getcwd(), "zomato-bangalore-restaurants-2022")
    zomato_csv = os.path.join(os.getcwd(), "data/zomato.csv")
    od.download('https://www.kaggle.com/datasets/vora1011/zomato-bangalore-restaurants-2022/data')
    # Gather all files
    allfiles = os.listdir(source_path2)
    
    # iterate on all files to move them to destination folder
    for f in allfiles:
        src_path = os.path.join(source_path2, f)
        dst_path = os.path.join(dataset_path, f)
        shutil.move(src_path, dst_path)
    
    zomato_banglore_2 = pd.read_csv(banglore_csv)
    zomato_banglore_2_df = pd.DataFrame(zomato_banglore_2)
    shutil.rmtree("zomato-bangalore-restaurants-2022")
    
    return zomato_banglore_1_df, zomato_banglore_2_df

def Zomato_banglore_1(dataframe):

    # import ipdb; ipdb.set_trace()

    zomato_banglore_1_cleaned_df = dataframe
    zomato_banglore_1_cleaned_df.dropna(inplace=True)
    zomato_banglore_1_cleaned_df = zomato_banglore_1_cleaned_df.drop(["url", "address", "phone", "reviews_list", "menu_item"], axis='columns')
    # def is_valid_ifopt(value):
    #     pattern = r'^[a-zA-Z0-9]'
    #     return pd.notna(value) and bool(re.match(pattern, str(value)))
    # zomato_banglore_1_cleaned_df = zomato_banglore_1_cleaned_df[zomato_banglore_1_cleaned_df['IFOPT'].apply(is_valid_ifopt)]

    # Online_order and Book_table column cleaning
    zomato_banglore_1_cleaned = zomato_banglore_1_cleaned_df[zomato_banglore_1_cleaned_df['online_order'].isin(['Yes','No'])]
    zomato_banglore_1_cleaned = zomato_banglore_1_cleaned_df[zomato_banglore_1_cleaned_df['book_table'].isin(['Yes','No'])]
    
    # Rate column cleaning
    zomato_banglore_1_cleaned_df['rate'] = zomato_banglore_1_cleaned_df['rate'].str.replace('/5', '')
    zomato_banglore_1_cleaned_df['rate'] = zomato_banglore_1_cleaned_df['rate'].str.replace('\W', '', regex=True)
    zomato_banglore_1_cleaned_df['rate'] = zomato_banglore_1_cleaned_df['rate'].str.replace('\D', '', regex=True)
    # zomato_banglore_1_cleaned_df['rate'] = zomato_banglore_1_cleaned_df['rate'].astype(int)

    # import ipdb; ipdb.set_trace()
    return zomato_banglore_1_cleaned_df

    # # Remove All Letters from Strings
    # zomato_banglore_1_cleaned_df['my_column'] = zomato_banglore_1_cleaned_df['my_column'].str.replace('\D', '', regex=True)

    # # Remove All Numbers from Strings
    # zomato_banglore_1_cleaned_df['my_column'] = zomato_banglore_1_cleaned_df['my_column'].str.replace('\d+', '', regex=True)

    # # Remove Special Characters
    # zomato_banglore_1_cleaned_df['my_column'] = zomato_banglore_1_cleaned_df['my_column'].str.replace('\W', '', regex=True)

    
def Zomato_database_file(dataframe):
    Zomato_banglore_cleaned = dataframe
    # Connect to SQLite database
    Sqlfilepath = os.path.join(os.getcwd(), "data", "Zomato.sqlite")
    conn = sqlite3.connect(Sqlfilepath)
    # Use the to_sql method to write the DataFrame to a SQLite table
    Zomato_banglore_cleaned.to_sql('Zomato', conn, index=False, if_exists='replace')

    # Close the connection
    conn.close()


def Zomato_banglore_2(dataframe):

    # import ipdb; ipdb.set_trace()

    zomato_banglore_2_cleaned_df = dataframe

    zomato_banglore_2_cleaned_df.dropna(inplace=True)

    return zomato_banglore_2_cleaned_df

    # # Remove All Letters from Strings
    # zomato_banglore_2_cleaned_df['my_column'] = zomato_banglore_2_cleaned_df['my_column'].str.replace('\D', '', regex=True)

    # # Remove All Numbers from Strings
    # zomato_banglore_2_cleaned_df['my_column'] = zomato_banglore_2_cleaned_df['my_column'].str.replace('\d+', '', regex=True)

    # # Remove Special Characters
    # zomato_banglore_2_cleaned_df['my_column'] = zomato_banglore_2_cleaned_df['my_column'].str.replace('\W', '', regex=True)

    
def Zomato_database_file_2(dataframe):
    Zomato_banglore_cleaned = dataframe
    # Connect to SQLite database
    Sqlfilepath = os.path.join(os.getcwd(), "data", "Banglore.sqlite")
    conn = sqlite3.connect(Sqlfilepath)
    # Use the to_sql method to write the DataFrame to a SQLite table
    Zomato_banglore_cleaned.to_sql('Banglore', conn, index=False, if_exists='replace')

    # Close the connection
    conn.close()

def data_pipeline():
    print("Downloading Datasets... ")
    zomato_banglore_1_df, zomato_banglore_2_df = download_csv_files()
    print("Download complete")

    #Step 2 Clean zomato banglore dataset 1 and Load into SQLite file
    print("Cleaning Zomato dataset Banglore_1")
    zomato_banglore_1_cleaned = Zomato_banglore_1(zomato_banglore_1_df)
    print("Zomato data cleaned loading into SQL Lite database")
    Zomato_database_file(zomato_banglore_1_cleaned)
    print("Loaded data into SQL file successfully")

    #Step 3 Clean zomato banglore dataset 2 and Load into SQLite file
    print("Cleaning Zomato dataset Banglore_2")
    zomato_banglore_2_cleaned = Zomato_banglore_2(zomato_banglore_2_df)
    print("Zomato data cleaned loading into SQL Lite database")
    Zomato_database_file_2(zomato_banglore_2_cleaned)
    print("Loaded data into SQL file successfully")
    
    print("All Tasks Completed :) ")

if __name__ == "__main__":
    data_pipeline()

"""
dataset_path = os.path.join(os.getcwd(), "data")
# Download Zomato dataset
kagle.api.authenticate()
url = "https://www.kaggle.com/datasets/rajeshrampure/zomato-dataset/download?datasetVersionNumber=1"
response = requests.head(url)
print(response.headers.get("content-length"))

# kaggle.api.dataset_download_files('rajeshrampure/zomato-dataset', path='/Users/akshatkhara/Desktop/Study Material/Semester 3/Methods of Advance Data Engineering/made-template-WS2324/data', unzip=True)
# kaggle.api.dataset_download_files('vora1011/zomato-bangalore-restaurants-2022', path='/Users/akshatkhara/Desktop/Study Material/Semester 3/Methods of Advance Data Engineering/made-template-WS2324/data', unzip=True)


# The dataets are stored in the repository data folder. 
dataset1 = pd.read_csv('/Users/akshatkhara/Desktop/Study Material/Semester 3/Methods of Advance Data Engineering/made-template-WS2324/data/zomato.csv')
dataset2 = pd.read_csv('/Users/akshatkhara/Desktop/Study Material/Semester 3/Methods of Advance Data Engineering/made-template-WS2324/data/BangaloreZomatoData.csv')

# The dataset are stored in Pandas DataFrame to be later stored in SQLLite Database
data1 = pd.DataFrame(dataset1)
data2 = pd.DataFrame(dataset2)

print(data1.head())

# Connect to SQLite database
# conn = sqlite3.connect('/Users/akshatkhara/Desktop/Study Material/Semester 3/Methods of Advance Data Engineering/made-template-WS2324/data/zomato.db')

# Use the to_sql method to write the DataFrame to a SQLite table
# data1.to_sql('accident_india', conn, index=False, if_exists='replace')

#Optional selceting the query using PANDAS function to check whether the data is stored in the database.
# query = "SELECT * FROM accident_india"
# df = pd.read_sql_query(query, conn)
# print(df.head())

# Close the connection
# conn.close()
"""