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
    
    path_Immoscout24 = "https://docs.google.com/spreadsheets/d/1Bhi9CZjfI6qlM-2J1TVeDy_JfIcSBqufXlHV6IuT7n4/export?format=xlsx"
    df1 = data_extraction_xls(path_Immoscout24)
    df1_drop_cols = ["picturecount", "scoutId", "geo_bln", "geo_krs"]
    df1_rename_cols = {
        "regio1": "federalState",
        "geo_plz": "zipCode",
        "regio2": "district",
        "regio3": "cityTown"
    }
    df1 = data_transformation(df1, df1_rename_cols, df1_drop_cols)
    data_loader("datasets.sqlite", df1, "immoscout")

    path_intstudent = "https://docs.google.com/spreadsheets/d/1n9DXXIBUI5VpP8-qgCdhxvoV6FJgUyAVrz1VxAFZVNo/export?format=xlsx"
    df2 = data_extraction_xls(path_intstudent)
    df2_drop_cols = []
    df2_rename_cols = {
        "stadt": "city",
        "universität": "university",
        "Geisteswissenschaften": "Humanities",
        "Sozialwissenschaften": "Social sciences",
        "Mathematik": "Mathematics",
        "Ingenieurwissenschaften": "Engineering sciences",
        "Informatik": "Computer Science",
        "Medizin": "Medicine",
        "Landwirtschaft": "Agriculture"
    }
    df2 = data_transformation(df2, df2_rename_cols, df2_drop_cols)
    data_loader("datasets.sqlite", df2, "intstudents")

if __name__ == "__main__":
    main()