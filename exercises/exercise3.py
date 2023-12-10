import pandas as pd
import sqlite3
from io import StringIO
import requests

# Download data from the provided link
url = "https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv"
response = requests.get(url)
data = response.text

# Ignore first 6 lines and last 4 lines as metadata
data = "\n".join(data.splitlines()[6:-4])

# Read CSV data into a pandas DataFrame
df = pd.read_csv(StringIO(data), encoding='utf-8', sep=";")

# Rename columns
df.rename(columns={'Unnamed: 0': 'date', 'Unnamed: 1': 'CIN', 'Unnamed: 2': 'name',
                   'Unnamed: 12': 'petrol', 'Unnamed: 22': 'diesel', 'Unnamed: 33': 'gas',
                   'Unnamed: 42': 'electro', 'Unnamed: 52': 'hybrid', 'Unnamed: 63': 'plugInHybrid',
                   'Unnamed: 74': 'others'}, inplace=True)

# Convert CIN to string with leading zero
df['CIN'] = df['CIN'].apply(lambda x: f"{int(x):05}")

# Keep only the specified columns
columns_to_keep = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']
df = df[columns_to_keep]

# Drop rows with invalid values
df = df.dropna(subset=['date', 'name', 'CIN', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others'])
df = df[df['CIN'].astype(str).apply(lambda x: len(x) == 5 and x.isdigit())]
df[columns_to_keep[3:]] = df[columns_to_keep[3:]].apply(lambda x: x.astype(str).str.isdigit() & (x.astype(int) > 0))

# Connect to SQLite database
conn = sqlite3.connect("cars.sqlite")

# Define SQLite types for each column
sqlite_types = {'date': 'TEXT', 'CIN': 'TEXT', 'name': 'TEXT',
                'petrol': 'BIGINT', 'diesel': 'BIGINT', 'gas': 'BIGINT',
                'electro': 'BIGINT', 'hybrid': 'BIGINT', 'plugInHybrid': 'BIGINT', 'others': 'BIGINT'}

# Create SQLite table with appropriate types
create_table_query = f"CREATE TABLE IF NOT EXISTS cars ({', '.join([f'{col} {sqlite_types[col]}' for col in columns_to_keep])})"
conn.execute(create_table_query)

# Write DataFrame to SQLite database
df.to_sql("cars", conn, index=False, if_exists="replace", dtype=sqlite_types)

# Close the connection
conn.close()

print("Data pipeline completed successfully.")
