from sqlalchemy import create_engine, inspect
import pandas as pd
from pipeline import (
    data_extraction_xls,
    data_transformation
)


def test_dataset_extraction(path):
    df = data_extraction_xls(path)
    assert not df.empty, "Dataset Extraction Failed"
    print("Extract Dataset: Test Passed")
    return df

def test_data_extraction_csv(path):
    df = data_extraction_xls(path)
    assert not df.empty, "Dataset Extraction Failed"
    print("Extract Dataset: Test Passed")
    return df


def test_dataset_transformation(data, rename_col, drop_col):
    df = data_transformation(data, rename_col, drop_col)
    assert df.isna().any().any() == False, "Invalid data Found in Dataset"
    print("Dataset Transformation: Test Passed")
    return df


def test_dataset_loader(table_name):
    engine = create_engine(f"sqlite:///datasets.sqlite")

    # Create an inspector object
    inspector = inspect(engine)

    # Check if a table exists in the database
    exists = inspector.has_table(table_name)
    assert exists, f"The table '{table_name}' does not exist in the database."
    print("test_dataset_loader: " + table_name + "Table exists, Test Passed")


def test_pipeline():

    path_intstudent = "https://docs.google.com/spreadsheets/d/1n9DXXIBUI5VpP8-qgCdhxvoV6FJgUyAVrz1VxAFZVNo/export?format=xlsx"
    df2 = test_dataset_extraction(path_intstudent)

    # correct date format in year cloumn
    df2['Jahr'] = pd.to_datetime(df2['Jahr'].str.split('/').str[0], format='%Y')
    df2['Jahr'] = df2['Jahr'].dt.strftime('%Y-%m-%d')

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
        "Jahr": "year",
        "Stadt": "city",
        "Universität": "university",
        "Geisteswissenschaften": "Humanities",
        "Sozialwissenschaften": "Social sciences",
        "Mathematik": "Mathematics",
        "Ingenieurwissenschaften": "Engineering sciences",
        "Informatik": "Computer Science",
        "medizin": "Medicine",
        "Landwirtschaft": "Agriculture"
    }

    test_dataset_transformation(df2, df2_rename_cols, df2_drop_cols)

    test_dataset_loader("intstudents")

    #path_Immoscout24 = "https://docs.google.com/spreadsheets/d/1Bhi9CZjfI6qlM-2J1TVeDy_JfIcSBqufXlHV6IuT7n4/export?format=xlsx"
    path_Immoscout24 = r"C:\Users\mual273859\Downloads\archive\immo_data.csv"
    df1 = test_data_extraction_csv(path_Immoscout24)
    
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

    # Change 'city' column value 'Deggendorf' to 'Deggendorf_kreis'
    df1.loc[df1['regio2'] == 'Deggendorf_kreis'] = 'Deggendorf'
    
    # only fetch data with city name available in students data
    university_cities = df2['City'].unique()
    df1 = df1[df1['regio2'].isin(university_cities)]

    test_dataset_transformation(df1, df1_rename_cols, df1_drop_cols)

    test_dataset_loader("immoscout")

if __name__ == "__main__":
    test_pipeline()