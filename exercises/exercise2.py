import pandas as pd
from typing import Callable, Any
import time
import re
import sqlalchemy

def extract_csv_from_url(url: str) -> pd.DataFrame:
    i = 0
    max_i = 10
    df = None
    while (i < 10):
        try:
            df = pd.read_csv(url, sep=';', decimal=',')
            break
        except:
            i += 1
            print(f"Couldn't extract csv from given url! (Try {i}/{max_i})")
            time.sleep(2)
    if df is None:
        raise Exception(f"Failed to extract csv from given url {url}")
    return df

def drop_invalid_col(df: pd.DataFrame, column: str, valid: Callable[[Any], bool]) -> pd.DataFrame:
    df = df.loc[df[column].apply(valid)]
    return df
    

if __name__ == '__main__':
    # Url to csv file
    DATA_URL = 'https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV'
    
    # Extract dataframe from csv (with retries)
    df = extract_csv_from_url(DATA_URL)
    
    # Drop the Status column
    df = df.drop(columns=['Status'])
    
    # Drop rows with invalid values
    df = df.dropna()
    df = drop_invalid_col(df, 'Verkehr', lambda x: x in ['FV', 'RV', 'nur DPN'])
    df = drop_invalid_col(df, 'Laenge', lambda x: -90 < x < 90)
    df = drop_invalid_col(df, 'Breite', lambda x: -90 < x < 90)
    df = drop_invalid_col(df, 'IFOPT', lambda x: re.match("^..:[0-9]+:[0-9]+(:[0-9]+)?$", x) is not None)
    
    # Load dataframe into sqlite database, with matching datatypes
    df.to_sql('trainstops', 'sqlite:///trainstops.sqlite', if_exists='replace', index=False, dtype={
        "EVA_NR": sqlalchemy.BIGINT,
        "DS100": sqlalchemy.TEXT,
        "IFOPT": sqlalchemy.TEXT,
        "NAME": sqlalchemy.TEXT,
        "Verkehr": sqlalchemy.TEXT,
        "Laenge": sqlalchemy.FLOAT,
        "Breite": sqlalchemy.FLOAT,
        "Betreiber_Name": sqlalchemy.TEXT,
        "Betreiber_Nr": sqlalchemy.BIGINT
    })
  