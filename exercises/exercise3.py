import pandas as pd 

url = 'https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv'
new_col = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]
col = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']

df = pd.read_csv(url, sep=';', encoding="iso-8859-1", header=None, skiprows=6, skipfooter=4,
                 usecols=new_col, names=col, engine='python', na_values='.', thousands=',',
                 dtype={'CIN': str})

# Filter out rows with '-' in petrol column
df = df[df['petrol'].apply(lambda x: '-' not in str(x))]

#Validating all columns to be positive integers
numeric_columns = ['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']

df = df[df[numeric_columns].apply(pd.to_numeric, errors='coerce').gt(0).all(axis=1)]


# Ensure 'CIN' column has exactly five characters
df = df[df['CIN'].str.len() == 5]

# Convert data types
dtypes = {'petrol': 'int64', 'diesel': 'int64', 'gas': 'int64', 'electro': 'int64',
              'hybrid': 'int64', 'plugInHybrid': 'int64', 'others': 'int64'}
df = df.astype(dtypes)

# Write data to SQLite database
df.to_sql('cars', 'sqlite:///cars.sqlite', if_exists='replace', index=False)
