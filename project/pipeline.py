import os
import shutil
import requests
import gzip
import shutil
import pandas as pd
import os
import sqlite3

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

url = 'https://bulk.meteostat.net/v2/daily/KGVQ0.csv.gz'
dataset = 'imdevskp/corona-virus-report'

if os.path.exists('data/corona_virus_report'):
    shutil.rmtree('data/corona_virus_report')

if os.path.exists('data/usa_county_wise.csv'):
    os.remove('data/usa_county_wise.csv')

api.dataset_download_files(
    dataset, path='data/corona_virus_report', unzip=True,)

shutil.move('data/corona_virus_report/usa_county_wise.csv', 'data')

covid_data_csv = pd.read_csv('data/usa_county_wise.csv')

shutil.rmtree('data/corona_virus_report')

compressed_file_path = 'KGVQ0.csv.gz'
extracted_file_path = 'KGVQ0.csv'

with requests.get(url, stream=True) as response:
    with open(compressed_file_path, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

with gzip.open(compressed_file_path, 'rb') as f_in:
    with open(extracted_file_path, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

file = pd.read_csv("KGVQ0.csv")

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

headerList = ['date', 'tavg', 'tmin', 'tmax', 'prcp',
              'snow', 'wdir', 'wspd', 'wpgt', 'pres', 'tsun']
file.to_csv("KGVQ0.csv", header=headerList, index=False)

file_updated = pd.read_csv("KGVQ0.csv")

connection = sqlite3.connect('data/result.db')
file_updated.to_sql('tempreture', connection, if_exists='replace', index=False)
covid_data_csv.to_sql('covid', connection, if_exists='replace', index=False)

connection.commit()
connection.close()

if os.path.exists('data/KGVQ0.csv'):
    os.remove('data/KGVQ0.csv')

shutil.move('KGVQ0.csv', 'data')
os.remove("KGVQ0.csv.gz")
