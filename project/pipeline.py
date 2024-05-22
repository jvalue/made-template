import subprocess
import zipfile
import os
import pandas as pd
import sqlite3
import requests
from io import StringIO
import matplotlib.pyplot as plt
import seaborn as sns

# Work Package 1: Data Acquisition

# Define Kaggle API commands
commands = [
    'kaggle datasets download -d iamsouravbanerjee/world-population-dataset',
    'kaggle datasets download -d sevgisarac/temperature-change'
]

# Execute the commands to download datasets
for command in commands:
    subprocess.run(command, shell=True)

# Extract the downloaded ZIP files
zip_files = ['world-population-dataset.zip', 'temperature-change.zip']
extract_folders = ['world-population-dataset', 'temperature-change']

for zip_file, folder in zip(zip_files, extract_folders):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(folder)
    os.remove(zip_file)

# Work Package 2: Data Preprocessing

# Load 2020 data from the World Population dataset
pop_csv_file_path = 'world-population-dataset/population.csv'
population_df = pd.read_csv(pop_csv_file_path)
population_df_2020 = population_df[population_df['Year'] == 2020]

# Load 2020 data from the Temperature Change dataset
temp_csv_file_path = 'temperature-change/Environment_Temperature_change_E_All_Data_NOFLAG.csv'
temperature_df = pd.read_csv(temp_csv_file_path)
temperature_df_2020 = temperature_df[temperature_df['Year'] == 2020]

# Clean datasets (e.g., handle missing values, drop unnecessary columns)
population_df_2020.dropna(inplace=True)
temperature_df_2020.dropna(inplace=True)

# Work Package 3: Data Integration

# Merge datasets on the 'Country' column
merged_df = pd.merge(population_df_2020, temperature_df_2020, on='Country', how='inner')

# Work Package 4: Data Analysis

# Descriptive statistics
print(merged_df.describe())

# Correlation analysis
correlation = merged_df['Population Growth'].corr(merged_df['Temperature Change'])
print(f'Correlation between Population Growth and Temperature Change: {correlation}')

# Visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(data=merged_df, x='Population Growth', y='Temperature Change')
plt.title('Population Growth vs Temperature Change')
plt.xlabel('Population Growth')
plt.ylabel('Temperature Change')
plt.show()

# Work Package 5: Database Storage

# Create SQLite database and save the merged dataset
db_path = 'data/merged_data.sqlite'
conn = sqlite3.connect(db_path)
merged_df.to_sql('population_temperature', conn, if_exists='replace', index=False)
conn.close()

# Work Package 6: Reporting

# Report Outline:
report_content = """
# Report: Analyzing the Effect of Population Growth on Temperature Changes

## Introduction
This project investigates the relationship between population growth and temperature changes on a global scale. By analyzing historical data on CO2 emissions and population trends, we assess how increases in population contribute to rising atmospheric CO2 levels and, consequently, global temperatures.

## Methodology
### Data Sources and Acquisition
- World Population Growth dataset from Kaggle
- Temperature Change dataset from Kaggle

### Data Preprocessing and Integration
- Loaded 2020 data from both datasets
- Cleaned and merged the data on the 'Country' column

### Analysis Methods
- Conducted descriptive statistics
- Performed correlation analysis
- Created visualizations to illustrate relationships and trends

## Results
### Descriptive Statistics
""" + merged_df.describe().to_string() + """

### Correlation Analysis
Correlation between Population Growth and Temperature Change: """ + str(correlation) + """

### Visualizations
- Scatter plot of Population Growth vs Temperature Change

## Discussion
The correlation analysis and visualizations provide insights into the relationship between population growth and temperature changes. This information is crucial for developing strategies to mitigate climate change.

## Conclusion
Understanding the relationship between population growth and temperature changes helps in addressing global warming. Further research is recommended to explore additional factors influencing climate change.

## Recommendations for Future Research
- Investigate the impact of industrialization and urbanization on climate change.
- Explore the effects of policy interventions on CO2 emissions and temperature changes.
"""

# Save the report to a text file
report_file_path = 'data/report.txt'
with open(report_file_path, 'w') as file:
    file.write(report_content)

print(f'Report saved to {report_file_path}')
