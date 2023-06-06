# Exercise 2
import pandas as pd
from sqlalchemy import create_engine
from time import time


############################################
############### Data Extraction ############
############################################
def data_extraction_csv(path):
    t1 = time()
    print("Data Extraction in progress...")
    try:
        # df = pd.read_csv(path)
        df = pd.read_csv(path, on_bad_lines='skip', delimiter=';')
    except Exception as e:
        print("Error occurred during file reading:", str(e))
        return None
    t2 = time()
    print("Finish: Data Extraction {} s ".format(t2 - t1))
    return df


############################################
############ Data Transformation ###########
############################################
def fitDataType(df):
    return df


def data_transformation(data_frame):
    t1 = time()
    print("Data Transformation in progress...")
    try:
        # Step 1: Drop the "Status" column
        data_frame = data_frame.drop('Status', axis=1)

        # Step 2: Drop rows with invalid values
        data_frame['Laenge'] = data_frame['Laenge'].str.replace(',', '.').astype(float)
        data_frame['Breite'] = data_frame['Breite'].str.replace(',', '.').astype(float)

        #Data Validation
        data_frame = data_frame[
            (data_frame["Verkehr"].isin(["FV", "RV", "nur DPN"])) &  # Valid "Verkehr" values
            (data_frame["Laenge"].between(-90, 90)) &  # Valid "Laenge" values
            (data_frame["Breite"].between(-90, 90)) &  # Valid "Breite" values
            (data_frame["IFOPT"].str.match(r"^[A-Za-z]{2}:\d+:\d+(?::\d+)?$"))  # Valid "IFOPT" values
            ].dropna()  # Drop rows with empty cells

        #Change Data Types
        data_type = {
            "EVA_NR": int,
            "DS100": str,
            "IFOPT": str,
            "NAME": str,
            "Verkehr": str,
            "Laenge": float,
            "Breite": float,
            "Betreiber_Name": str,
            "Betreiber_Nr": int
        }
        transformed_df = data_frame.astype(data_type)

        data_frame = data_frame.reset_index(drop=True)

        # Fit appropriate data types using the fitDataType method
        # data_frame = fitDataType(data_frame)
    except Exception as e:
        print("Error occurred during file reading:", str(e))
        return None

    # Return the transformed DataFrame
    t2 = time()
    print("Finish: Data Transformation {} s ".format(t2 - t1))
    return data_frame


############################################
################# Load Data ################
############################################
def data_loader(data_frame, table_name):
    t1 = time()
    print("SQLite DB Operations....")
    engine = create_engine("sqlite:///trainstops.sqlite")
    data_frame.to_sql(table_name, engine, if_exists="replace")
    t2 = time()
    print("Finish: Data Loading  {} s ".format(t2 - t1))


def main():
    path = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
    data_frame = data_extraction_csv(path)
    data_frame = data_transformation(data_frame)
    data_loader(data_frame,"trainstops")



if __name__ == "__main__":
    main()
