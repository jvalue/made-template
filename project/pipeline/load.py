import pandas as pd
import sqlite3
from colorama import init, Fore

from utils import get_directory_absolute_path

# Initialize colorama
init(autoreset=True)


def save_to_csv(df: pd.DataFrame, filename):
    """
    Saves the DataFrame to a CSV file.

    Args:
    - df (pd.DataFrame): DataFrame to save.
    - filename (str): Name of the output CSV file.
    """
    try:
        df.to_csv(filename, index=False)
        print(Fore.GREEN + f"Data saved to {filename}")
    except Exception as e:
        print(Fore.RED + f"Error saving data to {filename}: {e}")


def merge_datasets(temp_df: pd.DataFrame, co2_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merges the temperature and CO2 emissions datasets.

    Args:
    - temp_df (pd.DataFrame): DataFrame containing temperature data.
    - co2_df (pd.DataFrame): DataFrame containing CO2 emissions data.

    Returns:
    - pd.DataFrame: Merged DataFrame.
    """
    try:
        merged_df = pd.merge(temp_df, co2_df, on=['Area', 'Year'])
        print(Fore.GREEN + "Successfully merged temperature and CO2 data.")
        return merged_df.dropna()

    except Exception as e:
        print(Fore.RED + f"Error merging datasets: {e}")
        return None


def save_to_sqlite(data_frame: pd.DataFrame, db_name, table_name) -> None:
    """
    Saves the DataFrame to an SQLite database.

    Args:
    - df (pd.DataFrame): DataFrame to save.
    - table_name (str): Name of the table to save the data into.
    """

    try:
        cwd = get_directory_absolute_path()

        print(cwd)

        path = f"{cwd}/data/{db_name}.sqlite"
        conn = sqlite3.connect(path)
        data_frame.to_sql(f"{table_name}", conn,
                          index=False, if_exists="replace")
        conn.commit()
        conn.close()

        print(Fore.GREEN +
              f"Data saved to {table_name} table in {path}")

    except Exception as e:
        print(Fore.RED + f"Error saving data to SQLite database: {e}")
