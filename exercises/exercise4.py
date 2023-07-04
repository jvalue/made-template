import os
from pathlib import Path
import shutil
import time
from typing import Callable, Any
import urllib.request
import zipfile
import pandas as pd
from sqlalchemy import BIGINT, FLOAT, TEXT


def download_and_extract_zip(url: str, max_tries: int = 5, sec_wait_before_retry: float = 5) -> str:
    # Filename and -path definitions
    data_name = Path(url).stem
    extract_path = os.path.join(os.curdir, data_name)
    zip_name = data_name + '.zip'
    # Download zip with retries
    for i in range(1, max_tries+1):
        try:
            urllib.request.urlretrieve(url, zip_name)
            break
        except:
            print(f'Couldn\'t load zip from given url! (Try {i}/{max_tries})')
            if i < max_tries: time.sleep(sec_wait_before_retry)
    # Check if download was successfull
    if not os.path.exists(zip_name):
        raise FileNotFoundError(f'Failed to load zip from url {url}')
    # Extract and delete zip file
    with zipfile.ZipFile(zip_name, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    os.remove(zip_name)
    # Return path to extracted data
    return extract_path


def validate(df: pd.DataFrame, column: str, constraint: Callable[[Any], bool]) -> pd.DataFrame:
    df = df.loc[df[column].apply(constraint)]
    return df


def celsius_to_fahrenheit(temp_cels: float) -> float:
    return (temp_cels * 9/5) + 32


if __name__ == '__main__':
    zip_url = 'https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip'
    data_filename = 'data.csv'
    
    # Download and unzip data
    data_path = download_and_extract_zip(zip_url)
    
    # Read and reshape data
    df = pd.read_csv(os.path.join(data_path, data_filename),
                     sep=';',
                     index_col=False,
                     usecols=['Geraet', 'Hersteller', 'Model', 'Monat', 'Temperatur in °C (DWD)', 'Batterietemperatur in °C', 'Geraet aktiv'],
                     decimal=',')
    
    # Rename columns
    df.rename(columns={
        'Temperatur in °C (DWD)': 'Temperatur',
        'Batterietemperatur in °C':'Batterietemperatur'
        }, inplace=True)
    
    # Transform data
    df['Temperatur'] = celsius_to_fahrenheit(df['Temperatur'])
    df['Batterietemperatur'] = celsius_to_fahrenheit(df['Batterietemperatur'])
    
    # Validate data 
    df = validate(df, 'Geraet', lambda x: x > 0)
    df = validate(df, 'Monat', lambda x: x in range(1, 13))
    df = validate(df, 'Temperatur', lambda x: -459.67 < x < 212)
    df = validate(df, 'Batterietemperatur', lambda x: -459.67 < x < 212)
    df = validate(df, 'Geraet aktiv', lambda x: x in ['Ja', 'Nein'])
    
    # Write data into SQLite database
    table = 'temperatures'
    database = 'temperatures.sqlite'
    df.to_sql(table, f'sqlite:///{database}', if_exists='replace', index=False, dtype={
        'Geraet': BIGINT,
        'Hersteller': TEXT,
        'Model': TEXT,
        'Monat': BIGINT,
        'Temperatur': FLOAT,
        'Batterietemperatur': FLOAT,
        'Geraet aktiv': TEXT
    })
    
    # Delete downloaded data
    shutil.rmtree(data_path)
    
    print('Datapipeline finished successfully')
    print(f'Data is stored in table "{table}" in database "{database}"')
