import os
import requests
import pandas as pd
import sqlite3
from io import StringIO

# Define URLs for datasets
emissions_url = 'https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EDGAR/datasets/v432_FT2016/EDGARv432_FT2016_CO2_total_emissions_1970-2016.csv'
cancer_deaths_url = 'https://lincolnshire.ckan.io/dataset/a30070f9-7627-463f-867a-e351e1d15dd7/resource/f77ad392-7548-4a23-b3a1-e351b98ad214/download/deathsallcancers1.csv'

# Download datasets
def download_csv(url):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    return StringIO(response.content.decode('utf-8'))

emissions_data = download_csv(emissions_url)
cancer_deaths_data = download_csv(cancer_deaths_url)

# Read datasets into pandas DataFrames
emissions_df = pd.read_csv(emissions_data)
cancer_deaths_df = pd.read_csv(cancer_deaths_data)

# Inspect the datasets to understand their structure
print(emissions_df.columns)
print(cancer_deaths_df.columns)

# Process emissions data
# Assuming emissions data has columns like 'ISO_NAME' and year columns
emissions_df = emissions_df[['ISO_NAME', '2016']]  # Select the country and 2016 columns
emissions_df.rename(columns={'ISO_NAME': 'Country', '2016': 'CO2_Emissions'}, inplace=True)

# Process cancer deaths data
cancer_deaths_df = cancer_deaths_df[['GeoName', 'Persons(Number)DeathsUnder75']]
cancer_deaths_df.rename(columns={'GeoName': 'Country', 'Persons(Number)DeathsUnder75': 'Cancer_Deaths'}, inplace=True)

# Merge datasets on the country column
merged_df = pd.merge(emissions_df, cancer_deaths_df, on='Country', how='inner')

# Save DataFrame to SQLite database
data_folder = 'data'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

db_path = os.path.join(data_folder, 'final_dataset.sqlite')
conn = sqlite3.connect(db_path)

# Store DataFrame in the SQLite database
merged_df.to_sql('emissions_cancer_deaths', conn, index=False, if_exists='replace')

# Close the connection
conn.close()
