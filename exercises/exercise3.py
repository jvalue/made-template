#import necessary libraries 
import pandas as pd


# load data with required columns and except the first 6 rows
columns_to_keep = [0,1,2,12,22,32,42,52,62,72]

# URL of the data source
data_frame = pd.read_csv('https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv', sep = ';', encoding='utf-8', dtype = {1: str}, skiprows = 6, usecols = columns_to_keep)

# drop last 4 rows
data_frame = data_frame[:-4]

# rename columns
column_names = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']
data_frame.columns = column_names

# remove columns with invalid CIN values
data_frame = data_frame[data_frame['CIN'].str.len() == 5]

# remove rows with non-positive values
postive_columns = ['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']

for column in postive_columns:
    data_frame = data_frame[data_frame[column] != '-']

data_frame[postive_columns] = data_frame[postive_columns].astype(int)

for column in postive_columns:
    data_frame = data_frame[data_frame[column] > 0]

# save transformed database
data_frame.to_sql('cars', 'sqlite:///cars.sqlite', if_exists='replace', index=False)