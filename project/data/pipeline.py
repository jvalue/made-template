import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from time import time

# Db_Engine
db_engine = None


############################################
############### Data Extraction ############
############################################
def data_extraction_xls(path):
    t1 = time()
    print("Data Extraction in progress...")

    try:
        df = pd.read_excel(path)
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
        df = pd.read_csv(path)
    except Exception as e:
        print("Error occurred during file reading:", str(e))
        return None
    t2 = time()
    print("Finish: Data Extraction {} s ".format(t2 - t1))
    return df


############################################
############ Data Transformation ###########
############################################
def data_transformation(data_frame, rename_col, drop_col):
    t1 = time()
    print("Data Transformation in progress...")
    # Renaming the columns to english titles
    if rename_col:
        print("Renaming the columns to english titles...")
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


############################################
################# Load Data ################
############################################
def data_loader(data_frame, table_name):
    t1 = time()
    print("SQLite DB Operations....")
    # engine = get_engine(db_engine)
    engine = create_engine("sqlite:///nuremberg_stops_immoscout.db")
    data_frame.to_sql(table_name, engine, if_exists="replace")
    t2 = time()
    print("Finish: Data Loading  {} s ".format(t2 - t1))


def main():
    localPath_Immoscout24 = r"D:\Education\MS-AI\Sem-2\Data_Engineering_[OSS-AMSE]\2023-amse-template\project\datasets\Immoscout24.csv"
    df1 = data_extraction_csv(localPath_Immoscout24)
    df1_drop_cols = ["picturecount", "scoutId"]
    df1 = data_transformation(df1, [], df1_drop_cols)
    data_loader(df1, "immoscout")

    localPath_nuremberg = r"D:\Education\MS-AI\Sem-2\Data_Engineering_[OSS-AMSE]\2023-amse-template\project\datasets\Nuremberg_Stops_IDs_and_geodata.xlsx"
    df2 = data_extraction_xls(localPath_nuremberg)
    df2_drop_cols = {"breakpoint", "GlobalID", "branchOfService", "dataprovider"}
    df2_rename_cols = {
        "VGNKennung": "VAGIdentifier",
        "VAGKennung": "VAGIdentifierChar",
        "Haltepunkt": "breakpoint",
        "GlobalID": "GlobalID",
        "Haltestellenname": "stopName",
        "latitude": "latitude",
        "longitude": "longitude",
        "Betriebszweig": "branchOfService",
        "Dataprovider": "dataprovider",
    }
    df2 = data_transformation(df2, df2_rename_cols, df2_drop_cols)
    data_loader(df2, "nuremberg_stops")


# def get_engine(db_engine=None):
#     if db_engine == None:
#         db_engine = create_engine("sqlite:///nuremberg_stops_immoscout.db")
#     return db_engine


if __name__ == "__main__":
    main()
