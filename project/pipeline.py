import os
import shutil
import subprocess
import zipfile
import pandas as pd
import sqlite3
from kaggle import KaggleApi
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Set Kaggle environment variables
os.environ['KAGGLE_CONFIG_DIR'] = os.path.expanduser('~/.kaggle')
os.makedirs(os.environ['KAGGLE_CONFIG_DIR'], exist_ok=True)

# Read Kaggle API token information from .gitignore or parent folder file
kaggle_token_info = {}
with open('../.gitignore') as f:
    for line in f:
        if line.strip().startswith('{'):
            kaggle_token_info = json.loads(line.strip())

# Create kaggle.json file with the token
kaggle_config_path = os.path.join(os.environ['KAGGLE_CONFIG_DIR'], 'kaggle.json')
with open(kaggle_config_path, 'w') as f:
    json.dump(kaggle_token_info, f)

# Ensure the cache directory exists
cache_dir = os.path.join(os.environ['KAGGLE_CONFIG_DIR'], 'cache')
os.makedirs(cache_dir, exist_ok=True)

# Instantiate Kaggle API
api = KaggleApi()

# Download and extract population dataset
dataset = 'iamsouravbanerjee/world-population-dataset'
folder = 'world-population-dataset'
try:
    api.dataset_download_files(dataset, path=folder, unzip=True)
except Exception as e:
    print(f"Error downloading dataset: {e}")
    exit(1)

# Function to read CSV with various encodings
def read_csv_with_encodings(file_path, encodings=['latin1', 'ISO-8859-1', 'cp1252']):
    for enc in encodings:
        try:
            return pd.read_csv(file_path, encoding=enc)
        except Exception as e:
            print(f"Failed to read {file_path} with encoding {enc}: {e}")
    return None

# Load and preprocess population data
pop_df = read_csv_with_encodings(f'{folder}/world_population.csv')
if pop_df is None:
    print("Failed to read population dataset with all attempted encodings.")
    exit(1)

pop_df = pop_df[['Country/Territory', '1970 Population', '1980 Population', '1990 Population', '2000 Population', '2010 Population', '2020 Population']]
pop_df = pop_df.rename(columns={'Country/Territory': 'Country'})
pop_df = pop_df.melt(id_vars=['Country'], var_name='Year', value_name='Population')
pop_df['Decade'] = pop_df['Year'].str.extract(r'(\d+)').astype(int)
pop_df = pop_df.groupby((pop_df['Decade'] // 10) * 10)['Population'].sum().reset_index()
#pop_df['Population Growth Rate'] = pop_df['Population'].pct_change() * 100


# Download and extract temperature dataset
dataset = 'sevgisarac/temperature-change'
folder = 'temperature-change'
try:
    api.dataset_download_files(dataset, path=folder, unzip=True)
except Exception as e:
    print(f"Error downloading dataset: {e}")
    exit(1)

# Load and preprocess temperature data
temp_df = read_csv_with_encodings(f'{folder}/Environment_Temperature_change_E_All_Data_NOFLAG.csv')
if temp_df is None:
    print("Failed to read temperature dataset with all attempted encodings.")
    exit(1)

temp_df = temp_df.melt(id_vars=['Area', 'Months'], var_name='Year', value_name='Temperaturechange')
temp_df['Year'] = temp_df['Year'].str.extract(r'(\d+)').astype(float)
temp_df = temp_df.dropna(subset=['Year']).astype({'Year': int})
temp_df['Decade'] = (temp_df['Year'] // 10) * 10

avg_temp_decade = temp_df.groupby('Decade')['Temperaturechange'].mean().reset_index()
avg_temp_2011_to_2019 = temp_df[temp_df['Year'].between(2011, 2019)]['Temperaturechange'].mean()
avg_temp_decade = pd.concat([avg_temp_decade, pd.DataFrame({'Decade': [2020], 'Temperaturechange': [avg_temp_2011_to_2019]})], ignore_index=True)
avg_temp_decade = avg_temp_decade[avg_temp_decade['Decade'] != 1960]


# Merge datasets
merged_df = pd.merge(pop_df, avg_temp_decade, on='Decade')

# Save merged data to SQLite database
os.makedirs('data', exist_ok=True)
conn = sqlite3.connect('data/merged_data.sqlite')
merged_df.to_sql('merged_data', conn, if_exists='replace', index=False)
conn.close()

# Clean up cache and extracted folders
shutil.rmtree('world-population-dataset')
shutil.rmtree('temperature-change')
for file in os.listdir(cache_dir):
    os.remove(os.path.join(cache_dir, file))
