import sqlite3
import pandas as pd
from typing import Union
import geopandas as gpd

def fetch_table(conn: sqlite3.Connection, table_name: str) -> pd.DataFrame:
    """
    Fetch all records from the specified table in the SQLite database.

    :param conn: sqlite3.Connection
        The connection object to the SQLite database.
    :param table_name: str
        The name of the table to fetch data from.
    :return: pd.DataFrame
        A DataFrame containing all records from the specified table.
    """
    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql_query(query, conn)
    df.drop(columns="ï»¿ObjectId", inplace=True)
    return df


def prepare_temperature_change_data_for_maps(df: pd.DataFrame) -> gpd.GeoDataFrame:
    """
    Prepare the dataset by updating ISO3 codes, calculate the average temperature change,
    and merge with the world map.

    :param df: pd.DataFrame
        DataFrame containing the temperature change data.
    :return: gpd.GeoDataFrame
        GeoDataFrame containing the merged world map and temperature change data.
    """
    
    # Update multiple ISO3 codes in one line
    df['ISO3'] = df['ISO3'].replace({
        'TCA': 'TUR',
        'ARE': 'UAE'
    })
    
    # Calculate the average temperature change for each country
    year_columns = df.columns[2:]  # Assuming the first columns are 'ISO3', 'Country', etc.
    df['Average_Temperature_Change'] = df[year_columns].mean(axis=1)
    
    # Load the world map shapefile
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world = world[(world.name != "Antarctica")]
    
    # Ensure the world map data has an ISO3 code column
    world = world.rename(columns={'iso_a3': 'ISO3'})
    
    # Merge the temperature data with the world map using ISO3 codes
    merged = world.set_index('ISO3').join(df.set_index('ISO3'), how='left')
    
    return merged