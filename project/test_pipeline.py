import pytest
import sqlite3
import os
import pandas as pd
from pipeline import fetch_and_read, transform_and_store

URL_2009 = "https://datamillnorth.org/download/road-traffic-accidents/288d2de3-0227-4ff0-b537-2546b712cf00/2009.csv"
URL_2015 = "https://datamillnorth.org/download/road-traffic-accidents/df98a6dd-704e-46a9-9d6d-39d608987cdf/2015.csv"
URL_2016 = "https://datamillnorth.org/download/road-traffic-accidents/b2c7ebba-312a-4b3d-a324-6a5eda85fa5b/Copy%2520of%2520Leeds_RTC_2016.csv"

def sample_data():
    df_2009 = fetch_and_read(URL_2009)
    df_2015 = fetch_and_read(URL_2015)
    df_2016 = fetch_and_read(URL_2016)
    
    return df_2009, df_2015, df_2016

def test_fetch_and_read(sample_data):
    df_2009, df_2015, df_2016 = sample_data
    
    assert not df_2009.empty, "2009 Dataset is empty, fetching failed"
    assert not df_2015.empty, "2015 Dataset is empty, fetching failed"
    assert not df_2016.empty, "2016 Dataset is empty, fetching failed"


def test_transform_and_store(sample_data):
    df_2009, df_2015, df_2016 = sample_data

    conn = sqlite3.connect(':memory:')

    try:
        transform_and_store(df_2009, 'accidents_2009', conn)
        transform_and_store(df_2015, 'accidents_2015', conn)
        transform_and_store(df_2016, 'accidents_2016', conn)

        tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
        assert 'accidents_2009' in tables['name'].values
        assert 'accidents_2015' in tables['name'].values
        assert 'accidents_2016' in tables['name'].values


    finally:
        conn.close()
