import os
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from kaggle.api.kaggle_api_extended import KaggleApi
import requests
import sqlite3
import zipfile


def connect_to_kaggle():
    kaggle_api = KaggleApi()
    kaggle_api.authenticate()

    return kaggle_api

def downdload_kaggle_dataset(kaggle_api, dataset_name, author, file_name, directory, zip_file_name):
    kaggle_api.dataset_download_file(dataset=f"{author}/{dataset_name}", file_name=file_name, path=directory)
    zip_path = os.path.join(directory,zip_file_name)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref :
        zip_ref.extractall(directory)
    os.remove(zip_path)

def download_other_databases(directory, csv_links = {}):
    os.makedirs(directory, exist_ok=True)

    for file_name, url in csv_links.items():
        path = os.path.join(directory, file_name)
        try:
            print(f"Crop Files download started {path}\n")
            response = requests.get(url)
            response.raise_for_status()
            with open(path, 'wb') as file:
                file.write(response.content)
            print(f"Crop Files download done {path}\n")
        except requests.exceptions.RequestException as e:
            print(f"Download Failed {e}")

def checkIfExists(file_paths_crops, file_path_climate):
    for path in file_paths_crops:
        if not os.path.exists(path):
            print(f"Crop file does not exist: {path}\n")
            return False
    if not os.path.exists(file_path_climate):
        print(f"Climate file does not exist: {file_path_climate}\n")
        return False
    
    return True



def process_crop_irrigation(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna(subset=['Ag District'])
    columns_to_drop = ["Program","Period","Week Ending","Geo Level","State ANSI","Ag District","Ag District Code","County","County ANSI","Zip Code","Region","watershed_code","Watershed","Domain","Domain Category","CV (%)"]
    df = df.drop(columns=columns_to_drop)
    df = df[(df['Year'] >= 2018) & (df['Year'] <= 2022)]
    return df


def process_climate_change(file_path):
    df = pd.read_csv(file_path)
    df = df[df['Country'] == 'United States of America']
    df['Year'] = pd.to_datetime(df['Date']).dt.year
    df = df.drop(columns=['Date']) 
    return df

def store_in_sql(df,db_name,table_name, directory):
    db_path = os.path.join(directory, db_name)
    engine = create_engine(f'sqlite:///{db_path}')

    with engine.connect() as connection:
            df.to_sql(table_name, con=connection, if_exists='replace', index=False)

def main():
    file_json = {"crop_irrigated.csv" : "https://quickstats.nass.usda.gov/data/spreadsheet/6F5B8299-4137-3AD0-A9AC-2F699EA2AFC0.csv",
                 "crop_not_irrigated.csv" : "https://quickstats.nass.usda.gov/data/spreadsheet/309C08CD-8129-3A92-9AA4-F5C9BEE0D7A4.csv"}
    api_obj = connect_to_kaggle()

    data_directory = "../data"
    file_paths_crops = ["../data/crop_irrigated.csv", "../data/crop_not_irrigated.csv"]
    file_path_climate = "../data/climate_change_data.csv"
    zip_file_name = "climate_change_data.csv.zip"


    try:
        if not checkIfExists(file_paths_crops, file_path_climate):
            downdload_kaggle_dataset(api_obj,"climate-insights-dataset", "goyaladi", "climate_change_data.csv", data_directory, zip_file_name)
            download_other_databases(data_directory, file_json)
        else :
            print("Files already exist \n")
    except Exception as e:
        print(f"Error in downloading files{e}")

   
    for file_path in file_paths_crops:
        table_name = os.path.splitext(os.path.basename(file_path))[0]
        df = process_crop_irrigation(file_path)
        store_in_sql(df,"Data", table_name, data_directory)

    df = process_climate_change(file_path_climate )
    store_in_sql(df, "Data", "climate_change", data_directory)


if __name__ == '__main__':
    main()





