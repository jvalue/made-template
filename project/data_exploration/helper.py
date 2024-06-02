import sqlite3
import pandas as pd
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


def prepare_data_for_maps(df: pd.DataFrame, year_start_col: int) -> gpd.GeoDataFrame:
    """
    Prepare the dataset by updating ISO3 codes,
    calculating the average of specified columns,
    and merging with the world map.

    :param df: pd.DataFrame
        DataFrame containing the data.
    :param year_start_col: int
        The starting column index for the year data.
    :return: gpd.GeoDataFrame
        GeoDataFrame containing the merged world map and aggregated data.
    """
    # Update multiple ISO3 codes in one line
    df["ISO3"] = df["ISO3"].replace({"TCA": "TUR", "ARE": "UAE"})

    # Calculate the average of the specified columns for each country
    year_columns = df.columns[year_start_col:]
    df["Average_Value"] = df[year_columns].mean(axis=1)

    # Load the world map shapefile
    world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    world = world[(world.name != "Antarctica")]

    # Ensure the world map data has an ISO3 code column
    world = world.rename(columns={"iso_a3": "ISO3"})

    # Merge the data with the world map using ISO3 codes
    merged = world.set_index("ISO3").join(df.set_index("ISO3"), how="left")

    return merged


def reshape_land_cover_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Reshape the land cover alteration DataFrame to ensure three rows per country ISO3
    based on Climate_Influence and remove the Unit and Indicator columns.

    :param df: pd.DataFrame
        DataFrame containing the land cover alteration data.
    :return: pd.DataFrame
        Reshaped DataFrame with three rows per country ISO3 based on Climate_Influence.
    """
    # Drop 'Unit' and 'Indicator' columns
    df = df.drop(columns=["Unit", "Indicator"])

    # Ensure three rows per country ISO3 based on Climate_Influence
    reshaped_df = (
        df.pivot_table(
            index=["ISO3", "Country"], columns="Climate_Influence", aggfunc="first"
        )
        .stack(level=1)
        .reset_index()
    )

    return reshaped_df


def aggregate_average_change(df: pd.DataFrame, start_col: int = 2) -> pd.Series:
    """
    Aggregate the overall average change over the years.

    :param df: pd.DataFrame
        DataFrame containing the annual data.
    :param start_col: int
        The starting column index from which the years' data begins.
    :return: pd.Series
        Series containing the average change for each year.
    """
    year_columns = df.columns[start_col:]
    avg_change = df[year_columns].mean()
    return avg_change
