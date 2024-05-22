import sqlite3
import pandas as pd
import requests
from io import StringIO
from pathlib import Path

def download_csv_to_sqlite(db_name: str, table_name: str, csv_url: str) -> None:
    """
    Downloads a CSV file from a given URL and inserts it into a table in a SQLite database.
    
    If the table already exists in the database, it will be replaced.
    
    :param db_name: Name of the SQLite database file.
    :type db_name: str
    :param table_name: Name of the table to be created/updated in the database.
    :type table_name: str
    :param csv_url: URL of the CSV file to be downloaded.
    :type csv_url: str
    :return: None
    """
    
    response = requests.get(csv_url)
    response.raise_for_status()  
    
    csv_data = StringIO(response.text)
    df = pd.read_csv(csv_data)

    conn = sqlite3.connect(db_name)

    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    conn.close()

def delete_columns_with_high_nulls(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """
    Delete columns with more than the specified threshold of null values.

    :param df: DataFrame to clean.
    :type df: pd.DataFrame
    :param threshold: Threshold for null values (default is 0.5).
    :type threshold: float
    :return: DataFrame with columns deleted if more than threshold of null values.
    :rtype: pd.DataFrame
    """
    col_threshold = len(df) * threshold
    df = df.loc[:, df.isnull().sum() <= col_threshold]
    return df

def drop_null_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop rows with any null values.

    :param df: DataFrame to clean.
    :type df: pd.DataFrame
    :return: DataFrame with rows containing null values dropped.
    :rtype: pd.DataFrame
    """
    df = df.dropna()
    return df

def apply_transformations_to_table(db_path: str, table_name: str) -> None:
    """
    Apply cleaning transformations to a table in a SQLite database:
    1. Delete columns with more than 50% null values.
    2. Drop rows with any null values.

    :param db_path: Path to the SQLite database file.
    :type db_path: str
    :param table_name: Name of the table to transform.
    :type table_name: str
    :return: None
    """
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    
    # Apply transformations
    df = delete_columns_with_high_nulls(df, threshold=0.5)
    df = drop_null_rows(df)
    
    # Save the cleaned data back to the database
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    conn.close()

if __name__ == "__main__":
    db_name = Path("./data/climate_data.db")

    datasources = {
        "Annual_Surface_Temperature_Change": "https://opendata.arcgis.com/datasets/4063314923d74187be9596f10d034914_0.csv",
        "World_Monthly_CO2_Concentrations": "https://opendata.arcgis.com/datasets/9c3764c0efcc4c71934ab3988f219e0e_0.csv",
        "Change_in_Mean_Sea_Levels": "https://opendata.arcgis.com/datasets/b84a7e25159b4c65ba62d3f82c605855_0.csv",
        "Land_Cover_Alteration": "https://opendata.arcgis.com/datasets/b1e6c0ea281f47b285addae0cbb28f4b_0.csv"
    }

    for table_name, csv_url in datasources.items():
        download_csv_to_sqlite(db_name, table_name, csv_url)

    print("All data has been downloaded and stored in the database.")
    
    for table_name in datasources.keys():
        apply_transformations_to_table(db_name, table_name)
    
    print("Data cleaning and transformation applied to all tables.")
