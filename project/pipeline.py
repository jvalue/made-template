import pandas as pd
import sqlite3
from sqlalchemy.exc import SQLAlchemyError

def fetch_data(url):
    #Fetch data from a given URL and return as a DataFrame.
    
    try:
        return pd.read_csv(url)
    except pd.errors.EmptyDataError as e:
        print(f"Error fetching data from {url}: {e}")
        return pd.DataFrame()  # Return empty DataFrame if error


def store_data(df, db_path, table_name):
    #Store data into a SQLite table in the specified database.

    try:
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
    except SQLAlchemyError as e:
        print(f"Failed to store data in table {table_name} at {db_path}: {e}")

def main():
    # Main function to orchestrate the fetching and storing of data.
    
    db_path = './data/climate.db'
    
    # Define data sources and corresponding table names
    sources = {
        "https://opendata.arcgis.com/datasets/b13b69ee0dde43a99c811f592af4e821_0.csv": "climate_disaster_freq",
        "https://opendata.arcgis.com/datasets/7cae02f84ed547fbbd6210d90da19879_0.csv": "climate_inform_risk",
        "https://opendata.arcgis.com/datasets/d22a6decd9b147fd9040f793082b219b_0.csv": "govt_expenditure"
    }
    
    for url, table_name in sources.items():
        df = fetch_data(url)
        if not df.empty:  # Proceed only if DataFrame is not empty
            store_data(df, db_path, table_name)

if __name__ == "__main__":
    main()