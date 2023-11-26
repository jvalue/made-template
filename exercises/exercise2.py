import pandas as pd
from sqlalchemy import create_engine
from io import StringIO
import urllib.request
import re

# Downloading and Reading the CSV file into a pandas DataFrame
url = 'https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV'
response = urllib.request.urlopen(url)
csv_content = response.read().decode('utf-8')
df = pd.read_csv(StringIO(csv_content),sep=';')
df = df.drop("Status", axis='columns')

# Filter "Verkehr" column
Verkehr_valid_values = ["FV", "RV", "nur DPN"]
df = df[df['Verkehr'].isin(Verkehr_valid_values)]

# Filter for speicific dimension i.e. Latitude and Longtitude
Dimension = ['Laenge', 'Breite']
df[Dimension] = df[Dimension].replace({',': '.'}, regex=True)
df[['Laenge', 'Breite']] = df[['Laenge', 'Breite']].apply(pd.to_numeric)

for x in df.index:
    if df.loc[x, "Laenge"] <= -90 or df.loc[x, "Laenge"] >= 90 :
        df = df.drop(x, inplace=True)
    elif df.loc[x, "Breite"] <= -90 or df.loc[x, "Breite"] >= 90 :
        df = df.drop(x, inplace=True)

# Function to check the validity of IFOPT values
def is_valid_ifopt(value):
    pattern = r'^[a-zA-Z]{2}:\d+:\d+(?::\d+)?$'
    return pd.notna(value) and bool(re.match(pattern, str(value)))
df = df[df['IFOPT'].apply(is_valid_ifopt)]

# Drop cells with empty rows
df = df.dropna()

# Use fitting SQLite types (e.g., BIGINT, TEXT or FLOAT) for all columns
df['Betreiber_Nr'] =  df['Betreiber_Nr'].astype(int)

# Defining the SQLite database connection and create an SQLAlchemy engine
db_connection_str = 'sqlite:///trainstops.sqlite'
engine = create_engine(db_connection_str)

# Writing the DataFrame to the SQLite database
df.to_sql('trainstops', con=engine, index=False, if_exists='replace')

# Close the engine
engine.dispose()