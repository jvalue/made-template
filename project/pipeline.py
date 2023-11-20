import pandas as pd
import sqlalchemy
import requests
import io
import sqlite3

from sqlalchemy import create_engine


url_2009 = "https://datamillnorth.org/download/road-traffic-accidents/288d2de3-0227-4ff0-b537-2546b712cf00/2009.csv"
url_2015 = "https://datamillnorth.org/download/road-traffic-accidents/df98a6dd-704e-46a9-9d6d-39d608987cdf/2015.csv"
url_2018 = "https://datamillnorth.org/download/road-traffic-accidents/8c100249-09c5-4aac-91c1-9c7c3656892b/RTC%25202018_Leeds.csv"

def fetch_and_read (url):
    try:
        response = requests.get(url)
        return pd.read_csv(io.StringIO(response.text), sep =";" , on_bad_lines='skip')
    except requests.RequestsException as e:
        print(f"the fetching data from {url}: {e}")
        pd.DataFrame()
    except pd.errors.ParserError as e:
        print(f"error parsing csv from {url}: {e}")
        pd.DataFrame()
            
    
df_2009 = fetch_and_read(url_2009)
df_2015 = fetch_and_read(url_2015)
df_2018 = fetch_and_read(url_2018)


df_2009_selected = df_2009[['Type of Vehicle', 'Casualty Severity']]
df_2015_selected = df_2015[['Type of Vehicle', 'Casualty Severity']]
df_2018_selected = df_2018[['Type of Vehicle', 'Casualty Severity']]


conn = sqlite3.connect('./data/accidents.sqlite')

df_2009_selected.to_sql('accidents_2009', conn, index=False, if_exists='replace')
df_2015_selected.to_sql('accidents_2015', conn, index=False, if_exists='replace')
df_2018_selected.to_sql('accidents_2018', conn, index=False, if_exists='replace')

conn.close()