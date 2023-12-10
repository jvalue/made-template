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

# Define column names
column_names = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']

# Read CSV data into a pandas DataFrame with specified column names
df = pd.read_csv(StringIO(data), encoding='utf-8', sep=";", names=column_names, header=None)

# Convert CIN to string with leading zero
df['CIN'] = df['CIN'].apply(lambda x: f"{int(x):05}" if x.isdigit() else x)

# Drop all columns not in the specified list
df = df[column_names]

# Drop rows with invalid values
df = df.dropna(subset=column_names)
df = df[df['CIN'].astype(str).apply(lambda x: len(x) == 5 and x.isdigit())]

# Convert numeric columns to positive integers, handling non-numeric values
numeric_columns = column_names[3:]
for col in numeric_columns:
    if col not in ['date', 'name']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        df[col] = df[col].apply(lambda x: int(x) if pd.notna(x) and x > 0 else None)

# Drop rows with NaN values (resulting from non-numeric values in numeric columns)
df = df.dropna()
# Connect to SQLite database
conn = sqlite3.connect("cars.sqlite")

# Define SQLite types for each column
sqlite_types = {'date': 'TEXT', 'CIN': 'TEXT', 'name': 'TEXT',
                'petrol': 'BIGINT', 'diesel': 'BIGINT', 'gas': 'BIGINT',
                'electro': 'BIGINT', 'hybrid': 'BIGINT', 'plugInHybrid': 'BIGINT', 'others': 'BIGINT'}

# Create SQLite table with appropriate types
create_table_query = f"CREATE TABLE IF NOT EXISTS cars ({', '.join([f'{col} {sqlite_types[col]}' for col in column_names])})"
conn.execute(create_table_query)

# Write DataFrame to SQLite database
df.to_sql("cars", conn, index=False, if_exists="replace", dtype=sqlite_types)

# Close the connection
conn.close()

print("Data pipeline completed successfully.")

