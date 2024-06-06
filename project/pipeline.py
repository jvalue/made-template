import os
import shutil
import subprocess
import zipfile
import pandas as pd
import sqlite3
import json

# Navigate to the parent directory
parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# Read Kaggle API token information from .gitignore file in the parent directory
kaggle_token_info = {}
gitignore_path = os.path.join(parent_dir, '.gitignore')
with open(gitignore_path) as f:
    for line in f:
        if line.strip().startswith('{'):
            kaggle_token_info = json.loads(line.strip())

# Set Kaggle environment variables
os.environ['KAGGLE_CONFIG_DIR'] = os.path.expanduser('~/.kaggle')
os.makedirs(os.environ['KAGGLE_CONFIG_DIR'], exist_ok=True)

# Create kaggle.json file with the token
kaggle_config_path = os.path.join(os.environ['KAGGLE_CONFIG_DIR'], 'kaggle.json')
with open(kaggle_config_path, 'w') as f:
    json.dump(kaggle_token_info, f)

# Ensure the cache directory exists
os.environ['KAGGLE_DATASETS_CACHE'] = os.path.expanduser('~/.kaggle/cache')
os.makedirs(os.environ['KAGGLE_DATASETS_CACHE'], exist_ok=True)

# Kaggle datasets to download
datasets = [
    ('iamsouravbanerjee/world-population-dataset', 'world-population-dataset.zip', 'world-population-dataset'),
    ('sevgisarac/temperature-change', 'temperature-change.zip', 'temperature-change')
]

# Download and extract datasets
for dataset, zip_file, folder in datasets:
    subprocess.run(f'kaggle datasets download -d {dataset}', shell=True, check=True)
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(folder)
    os.remove(zip_file)

# Function to read CSV with various encodings
def read_csv_with_encodings(file_path, encodings=['latin1', 'ISO-8859-1', 'cp1252']):
    for enc in encodings:
        try:
            return pd.read_csv(file_path, encoding=enc)
        except Exception as e:
            print(f"Failed to read {file_path} with encoding {enc}: {e}")
    return None

# Load and preprocess population data
pop_df = read_csv_with_encodings('world-population-dataset/world_population.csv')
if pop_df is None:
    print("Failed to read population dataset with all attempted encodings.")
    exit(1)

pop_df = pop_df[['Country/Territory', '1970 Population', '1980 Population', '1990 Population', '2000 Population', '2010 Population', '2020 Population']]
pop_df = pop_df.rename(columns={'Country/Territory': 'Country'})
pop_df = pop_df.melt(id_vars=['Country'], var_name='Year', value_name='Population')
pop_df['Year'] = pop_df['Year'].str.extract(r'(\d+)').astype(int)
pop_df = pop_df.groupby((pop_df['Year'] // 10) * 10)['Population'].sum().reset_index()

# Load and preprocess temperature data
temp_df = read_csv_with_encodings('temperature-change/Environment_Temperature_change_E_All_Data_NOFLAG.csv')
if temp_df is None:
    print("Failed to read temperature dataset with all attempted encodings.")
    exit(1)

temp_df = temp_df.melt(id_vars=['Area', 'Months'], var_name='Year', value_name='Temperature')
temp_df['Year'] = temp_df['Year'].str.extract(r'(\d+)').astype(float)
temp_df = temp_df.dropna(subset=['Year']).astype({'Year': int})
temp_df = temp_df.groupby((temp_df['Year'] // 10) * 10)['Temperature'].mean().reset_index()

# Merge datasets
merged_df = pd.merge(pop_df, temp_df, on='Year')

# Save merged data to SQLite database
os.makedirs('data', exist_ok=True)
conn = sqlite3.connect('data/merged_data.sqlite')
merged_df.to_sql('merged_data', conn, if_exists='replace', index=False)
conn.close()

# Clean up cache and extracted folders
#shutil.rmtree('world-population-dataset')
#shutil.rmtree('temperature-change')
#for file in os.listdir(os.environ['KAGGLE_DATASETS_CACHE']):
  #  os.remove(os.path.join(os.environ['KAGGLE_DATASETS_CACHE'], file))
