import pandas as pd
import numpy as np
from time import time
import sqlite3
from kaggle.api.kaggle_api_extended import KaggleApi
import os
import zipfile

# Data Extraction 

def data_extraction_xls(path):
    t1 = time()
    print("Data Extraction in progress...")

    try:
        df = pd.read_excel(path, engine='openpyxl')
    except Exception as e:
        print("Error occurred during file reading:", str(e))
        return None
    t2 = time()
    print("Finish: Data Extraction {} s ".format(t2 - t1))
    return df

def data_extraction_csv(path):
    t1 = time()
    print("Data Extraction in progress...")

    try:
        df = pd.read_csv(path, encoding='latin-1')
    except Exception as e:
        print("Error occurred during file reading:", str(e))
        return None
    t2 = time()
    print("Finish: Data Extraction {} s ".format(t2 - t1))
    return df

# Data Transformation 
def data_transformation(data_frame, rename_col, drop_col):
    t1 = time()
    print("Data Transformation in progress...")
    # Renaming the columns to english titles
    if rename_col:
        print("Renaming the columns to english titles...")
        print(" data_frame", data_frame)
        data_frame = data_frame.rename(columns=rename_col)

    print("Removing Unwanted Columns...")
    if drop_col:
        data_frame = data_frame.drop(columns=drop_col)

    print("Replacing Nan Values...")
    # Replace Nan values with 0
    data_frame = data_frame.replace(np.nan, 0)
    t2 = time()
    print("Finish: Data Transformation {} s ".format(t2 - t1))
    return data_frame

# Load Data 
def data_loader(db_file, data_frame, table_name):
    t1 = time()
    print("SQLite DB Operations....")
    # Connect to the SQLite databases
    conn = sqlite3.connect(db_file)

    # Store the data in the specified tabless
    data_frame.to_sql(table_name, conn, if_exists='replace', index=False)
    # Close the database connection
    conn.close()
    t2 = time()
    print("Finish: Data Loading  {} s ".format(t2 - t1))

# Enable Kaggle API, go to the "API" section and click on "Create New API Token."
# This will download a file named kaggle.json to your computer then Store Kaggle API Key in system user folder
def fetch_kaggle_dataset(dataset, target_folder, filename):
    api = KaggleApi()
    api.authenticate()
    username, dataset_name = dataset.split('/')[-2:]
    zip_file_path = os.path.join(target_folder,f"{dataset_name}.zip")
    api.dataset_download_files(f"{username}/{dataset_name}", path=target_folder, unzip=False)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extract(filename, path=target_folder)
            
def main():
    
    path_intstudent = "https://firesoftstudio.com/student_data.xlsx"
    df2 = data_extraction_xls(path_intstudent)

    # correct date format in year cloumn
    df2['Jahr'] = pd.to_datetime(df2['Jahr'].str.split('/').str[0], format='%Y')
    df2['Jahr'] = df2['Jahr'].dt.strftime('%Y')

    #drop rows with num values
    df2 = df2.dropna()

    # List of columns to convert from float64 to int
    columns = ['Geisteswissenschaften', 'Sozialwissenschaften', 'Mathematik',
                 'Ingenieurwissenschaften', 'Informatik',
                 'medizin', 'Landwirtschaft']
    
    # Convert selected columns to int
    df2[columns] = df2[columns].astype(int)
    
    df2_drop_cols = []
    df2_rename_cols = {
        "Jahr": "Year",
        "Stadt": "City",
        "Universität": "University",
        "Geisteswissenschaften": "Humanities",
        "Sozialwissenschaften": "Social sciences",
        "Mathematik": "Mathematics",
        "Ingenieurwissenschaften": "Engineering sciences",
        "Informatik": "Computer Science",
        "medizin": "Medicine",
        "Landwirtschaft": "Agriculture"
    }
    df2 = data_transformation(df2, df2_rename_cols, df2_drop_cols)
    data_loader("../dataset.sqlite", df2, "intstudents")


    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, "..", "data")

    fetch_kaggle_dataset('corrieaar/apartment-rental-offers-in-germany', data_dir, 'immo_data.csv')
    path_Immoscout24 = r"../data/immo_data.csv"
    df1 = data_extraction_csv(path_Immoscout24)
    
    # Check if column is empty and drop corresponding rows
    df1.dropna(subset=['regio1', 'regio2', 'noRooms'], inplace=True)
    
    # Fetch only Bayren state dataset
    df1 = df1[df1['regio1'] == 'Bayern']
    
    # Drop not needed columns
    df1_drop_cols = ["picturecount", "scoutId", "geo_bln", "geo_krs", "telekomHybridUploadSpeed", "telekomTvOffer", "newlyConst", "balcony", "picturecount", "pricetrend", "telekomUploadSpeed", "scoutId", "firingTypes", "yearConstructedRange", "interiorQual", "petsAllowed", "streetPlain", "lift", "baseRentRange", "typeOfFlat", "energyEfficiencyClass", "lastRefurbish", "electricityBasePrice", "electricityKwhPrice", "date"]
    
    # correct the formats of data values
    df1['regio2'] = df1['regio2'].str.encode('latin-1').str.decode('utf-8')


    df1_rename_cols = {
        "regio1": "federalState",
        "geo_plz": "zipCode",
        "regio2": "City",
        "regio3": "Town"
    }
  
    # only fetch data with city name available in students data
    university_cities = df2['City'].unique()
    df1 = df1[df1['regio2'].isin(university_cities)]

    # Format dataset
    df1 = data_transformation(df1, df1_rename_cols, df1_drop_cols)
    data_loader("../dataset.sqlite", df1, "immoscout")


if __name__ == "__main__":
    main()