import shutil
import subprocess
import zipfile
import os
import pandas as pd
import sqlite3

# Set environment variables to change the cache directory
os.environ['KAGGLE_CONFIG_DIR'] = os.path.expanduser('~/.kaggle')
os.environ['KAGGLE_DATASETS_CACHE'] = os.path.expanduser('~/.kaggle/cache')

# Ensure the new cache directory exists
if not os.path.exists(os.environ['KAGGLE_DATASETS_CACHE']):
    os.makedirs(os.environ['KAGGLE_DATASETS_CACHE'])

# Work Package 1: Data Acquisition

# Define Kaggle API commands
commands = [
    'kaggle datasets download -d iamsouravbanerjee/world-population-dataset',
    'kaggle datasets download -d sevgisarac/temperature-change'
]

# Execute the commands to download datasets
for command in commands:
    subprocess.run(command, shell=True, check=True)

# Extract the downloaded ZIP files
zip_files = ['world-population-dataset.zip', 'temperature-change.zip']
extract_folders = ['world-population-dataset', 'temperature-change']

for zip_file, folder in zip(zip_files, extract_folders):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(folder)
    os.remove(zip_file)

# Print current working directory
print("Current working directory:", os.getcwd())

# Check the contents of the extracted folder for the World Population dataset
print("Contents of 'world-population-dataset' folder:", os.listdir('world-population-dataset'))

# Work Package 2: Data Preprocessing

# Load 2020 data from the World Population dataset
pop_csv_file_path = 'world-population-dataset/world_population.csv'

# Try reading the CSV file with different encodings
encodings = ['latin1', 'ISO-8859-1', 'cp1252']
population_df = None

for enc in encodings:
    try:
        population_df = pd.read_csv(pop_csv_file_path, encoding=enc)
        print(f"Successfully read population dataset with encoding: {enc}")
        break
    except Exception as e:
        print(f"Failed to read with encoding {enc}: {e}")

# If all encodings fail, exit the script
if population_df is None:
    print("Failed to read population dataset with all attempted encodings.")
    exit(1)

# Extract the relevant columns for multiple years
population_df_years = population_df[['Country/Territory', '1970 Population', '1980 Population', '1990 Population', '2000 Population', '2010 Population', '2020 Population']].rename(columns={'Country/Territory': 'Country'})

# Melt the population dataframe to have 'Year' and 'Population' columns
population_df_melted = population_df_years.melt(id_vars=['Country'], var_name='Year', value_name='Population')
population_df_melted['Year'] = population_df_melted['Year'].str.extract(r'(\d+)').astype(int)

# Calculate the sum of population for each decade
sum_population_decade = population_df_melted.groupby((population_df_melted['Year'] // 10) * 10)['Population'].sum().reset_index()

# Load the Temperature Change dataset
temp_csv_file_path = 'temperature-change/Environment_Temperature_change_E_All_Data_NOFLAG.csv'

# Try reading the CSV file with different encodings
temperature_df = None

for enc in encodings:
    try:
        temperature_df = pd.read_csv(temp_csv_file_path, encoding=enc)
        print(f"Successfully read temperature dataset with encoding: {enc}")
        break
    except Exception as e:
        print(f"Failed to read with encoding {enc}: {e}")

# If all encodings fail, exit the script
if temperature_df is None:
    print("Failed to read temperature dataset with all attempted encodings.")
    exit(1)

# Reshape the temperature data to have 'Year' and 'Temperature' columns
temperature_df_melted = temperature_df.melt(id_vars=['Area', 'Months'], var_name='Year', value_name='Temperature')

# Use raw string for regex pattern
temperature_df_melted['Year'] = temperature_df_melted['Year'].str.extract(r'(\d+)').astype(float)

# Drop rows with NaN values in 'Year' before converting to int
temperature_df_melted.dropna(subset=['Year'], inplace=True)
temperature_df_melted['Year'] = temperature_df_melted['Year'].astype(int)

# Calculate the average temperature for each decade
avg_temperature_decade = temperature_df_melted.groupby((temperature_df_melted['Year'] // 10) * 10)['Temperature'].mean().reset_index()

# Merge population and temperature data on 'Year'
merged_df = pd.merge(sum_population_decade, avg_temperature_decade, on='Year', how='inner')

# Work Package 5: Database Storage

# Create SQLite database and save the merged dataset
if not os.path.exists('data'):
    os.makedirs('data')
db_path = 'data/merged_data.sqlite'
conn = sqlite3.connect(db_path)

# Save the merged dataset to SQLite database
merged_df.to_sql('merged_data', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

# Remove cache files
cache_files = os.listdir(os.environ['KAGGLE_DATASETS_CACHE'])
for file in cache_files:
    os.remove(os.path.join(os.environ['KAGGLE_DATASETS_CACHE'], file))

# Remove the downloaded folders
shutil.rmtree('world-population-dataset')
shutil.rmtree('temperature-change')