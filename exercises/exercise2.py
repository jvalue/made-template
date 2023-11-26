import pandas as pd
from sqlalchemy import create_engine
from io import StringIO
import urllib.request
import re
# 1 : Downloading the CSV file
url = 'https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV'
response = urllib.request.urlopen(url)
csv_content = response.read().decode('utf-8')

#  2: Reading the CSV file into a pandas DataFrame
df = pd.read_csv(StringIO(csv_content),sep=';')
df = df.drop("Status", axis='columns')

# Filter "Verkehr" column
valid_verkehr_values = ["FV", "RV", "nur DPN"]
df = df[df['Verkehr'].isin(valid_verkehr_values)]

numeric_columns = ['Laenge', 'Breite']
df[numeric_columns] = df[numeric_columns].replace({',': '.'}, regex=True)
df[['Laenge', 'Breite']] = df[['Laenge', 'Breite']].apply(pd.to_numeric)

for x in df.index:
    if df.loc[x, "Laenge"] <= -90:
       df = df.drop(x, inplace=True)
    elif df.loc[x, "Laenge"] >= 90:
        df = df.drop(x, inplace=True)
    elif df.loc[x, "Breite"] <= -90:
        df = df.drop(x, inplace=True)
    elif df.loc[x, "Breite"] >= 90:
        df = df.drop(x, inplace=True)


# Function to check the validity of IFOPT values
def is_valid_ifopt(value):
    # Define the pattern for valid IFOPT values
    pattern = r'^[a-zA-Z]{2}:\d+:\d+(?::\d+)?$'
    return pd.notna(value) and bool(re.match(pattern, str(value)))

df = df[df['IFOPT'].apply(is_valid_ifopt)]
df = df.dropna()  # Drop rows with empty cells


#  3: Defining the SQLite database connection and create an SQLAlchemy engine
db_connection_str = 'sqlite:///trainstops.sqlite'
engine = create_engine(db_connection_str)

#  4: Writing the DataFrame to the SQLite database
df.to_sql('trainstops', con=engine, index=False, if_exists='replace')

# Close the engine
engine.dispose()