import pandas as pd
import numpy as np
from time import time
import sqlite3


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


def main():
    
    path_intstudent = "https://docs.google.com/spreadsheets/d/1n9DXXIBUI5VpP8-qgCdhxvoV6FJgUyAVrz1VxAFZVNo/export?format=xlsx"
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
    data_loader("datasets.sqlite", df2, "intstudents")

    
    #path_Immoscout24 = "https://docs.google.com/spreadsheets/d/1Bhi9CZjfI6qlM-2J1TVeDy_JfIcSBqufXlHV6IuT7n4/export?format=xlsx"
    path_Immoscout24 = r"C:\Users\mual273859\Downloads\archive\immo_data.csv"
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

    # # Change 'city' column value 'Deggendorf' to 'Deggendorf_kreis'
    # df1.loc[df1['regio2'] == 'Deggendorf_kreis'] = 'Deggendorf'
    
    # only fetch data with city name available in students data
    university_cities = df2['City'].unique()
    df1 = df1[df1['regio2'].isin(university_cities)]

    # Format datasets
    df1 = data_transformation(df1, df1_rename_cols, df1_drop_cols)
    data_loader("datasets.sqlite", df1, "immoscout")


if __name__ == "__main__":
    main()