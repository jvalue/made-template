import pandas as pd
import sqlalchemy as sql
import numpy as np  

#Link of datasourse 1
datasource1_link = 'https://www.landesdatenbank.nrw.de/ldbnrwws/downloader/00/tables/46251-02iz_00.csv'
#I want to start reading lines from 8 row.
lines_to_skip = list(range(1, 8))
lines_to_read = 61 # Number of lines to read

# Read the specified lines from the CSV file into a DataFrame
df = pd.read_csv(datasource1_link, skiprows=lines_to_skip, nrows=lines_to_read, delimiter=';', encoding='latin1')
df.reset_index(inplace=True)
#Rename columns
df.columns = ['PC','Province','Vehicles', 'Cars', 'Trucks', 'Tractors', 'Motorcycles']
#Delete row with missing information
df = df[df['Vehicles'] != "-"]
#Set column type
dtype_mapping = {
    'PC': str, 
    'Province': str,  
    'Vehicles': int,
    'Cars': int,
    'Trucks': int,
    'Tractors': int,
    'Motorcycles': int,  
}

df = df.astype(dtype_mapping)

engine1 = sql.create_engine("sqlite:///data/vehicles.sqlite")
dtype_mapping_sql = {
    'PC': sql.types.String, 
    'Province': sql.types.String,  
    'Vehicles': sql.types.Integer,
    'Cars': sql.types.Integer,
    'Trucks': sql.types.Integer,
    'Tractors': sql.types.Integer,
    'Motorcycles': sql.types.Integer,  
}
df.to_sql("vehicles", engine1, if_exists="replace", index=False, dtype=dtype_mapping_sql)


#Link of datasourse 2
datasource2_link = 'https://www.opengeodata.nrw.de/produkte/umwelt_klima/luftqualitaet/luqs/eu_jahreskenngroessen/LUQS-EU-Kenngroessen-2022.xlsx'
#Get the excel file uploaded on python
xls = pd.ExcelFile(datasource2_link)
#The excel file has 2 sheets, I selected the sheet where the information is.
df2 = pd.read_excel(xls, 'EU-Jahreskenngrößen 2022')

#Declare the columns name
columns_name = [
    'Name','Kennung', 'Gebiets-Name', 'Klassifikation', 'EU-Code',
    'Stickstoffdioxid Zeitl. Überdeckung  %', 'Stickstoffdioxid Jahresmittel µg/m³', 
    'Stickstoffdioxid Max. 1h-Wert', 'Stickstoffdioxid # 1h-Werte  > 200 µg/m³', 
    'Stickstoffdioxid Mess- verfahren', 'PM10 Zeitl. Überdeckung  %',
    'PM10 Jahresmittel µg/m³', 'PM10 # Tagesmittel > 50 µg/m³', 'PM10 Mess- verfahren',
    'PM2,5 Zeitl. Überdeckung  %', 'PM2,5 Jahresmittel µg/m³', 'PM2,5 Mess- verfahren',
    'Schwefeldioxid Zeitl. Überdeckung  %', 'Schwefeldioxid Jahresmittel µg/m³', 
    'Schwefeldioxid Max. 1h-Wert','Schwefeldioxid # 1h-Werte  > 350 µg/m³', 
    'Schwefeldioxid # Tagesmittel > 125 µg/m3','Benzol Zeitl. Überdeckung  %', 
    'Benzol Jahresmittel µg/m³','Benzol Mess- verfahren','Blei Zeitl. Überdeckung  %', 
    'Blei Jahresmittel µg/m³', 'Arsen Zeitl. Überdeckung  %',
    'Arsen Jahresmittel ng/m³', 'Cadmium Zeitl. Überdeckung  %', 
    'Cadmium Jahresmittel ng/m³','Nickel Zeitl. Überdeckung  %', 
    'Nickel Jahresmittel ng/m³', 'Benzopyren Zeitl. Überdeckung  %',
    'Benzopyren Jahresmittel ng/m³'
]

#Capture the part of the dataframe that is relevant for the analysis
df2 = df2.iloc[5:158,:].copy()
#Reset index beacuse all indexes are correlated with df2
df2.reset_index(inplace=True, drop =True)
#change columns name
df2.columns = columns_name

#Need to erase '---' and '--' from all the cells
df2 = df2.replace({'---':np.nan})
df2 = df2.replace({'--':np.nan})
df2 = df2.replace({'nan':np.nan})
df2.head()

#Set the value types of each column
dtype_mapping2 = {
    'Name': str, 
    'Kennung': str, 
    'Gebiets-Name': str, 
    'Klassifikation': str, 
    'EU-Code': str,
    'Stickstoffdioxid Zeitl. Überdeckung  %': float, 
    'Stickstoffdioxid Jahresmittel µg/m³': float, 
    'Stickstoffdioxid Max. 1h-Wert': float,
    'Stickstoffdioxid # 1h-Werte  > 200 µg/m³': float, 
    'Stickstoffdioxid Mess- verfahren': str, 
    'PM10 Zeitl. Überdeckung  %': float,
    'PM10 Jahresmittel µg/m³': float, 
    'PM10 # Tagesmittel > 50 µg/m³': float, 
    'PM10 Mess- verfahren': str,
    'PM2,5 Zeitl. Überdeckung  %': float, 
    'PM2,5 Jahresmittel µg/m³': float, 
    'PM2,5 Mess- verfahren': str,
    'Schwefeldioxid Zeitl. Überdeckung  %': float, 
    'Schwefeldioxid Jahresmittel µg/m³': float, 
    'Schwefeldioxid Max. 1h-Wert': float,
    'Schwefeldioxid # 1h-Werte  > 350 µg/m³': float, 
    'Schwefeldioxid # Tagesmittel > 125 µg/m3': float,
    'Benzol Zeitl. Überdeckung  %': float, 
    'Benzol Jahresmittel µg/m³': float, 
    'Benzol Mess- verfahren': str,
    'Blei Zeitl. Überdeckung  %': float, 
    'Blei Jahresmittel µg/m³': float, 
    'Arsen Zeitl. Überdeckung  %': float,
    'Arsen Jahresmittel ng/m³': float, 
    'Cadmium Zeitl. Überdeckung  %': float, 
    'Cadmium Jahresmittel ng/m³': float,
    'Nickel Zeitl. Überdeckung  %': float, 
    'Nickel Jahresmittel ng/m³': float, 
    'Benzopyren Zeitl. Überdeckung  %': float,
    'Benzopyren Jahresmittel ng/m³': float
}

df2 = df2.astype(dtype_mapping2)

engine2 = sql.create_engine("sqlite:///data/airpollution.sqlite")
dtype_mapping2_sql = {
    'Name': sql.types.String, 
    'Kennung': sql.types.String, 
    'Gebiets-Name': sql.types.String, 
    'Klassifikation': sql.types.String, 
    'EU-Code': sql.types.String,
    'Stickstoffdioxid Zeitl. Überdeckung  %': sql.types.Float, 
    'Stickstoffdioxid Jahresmittel µg/m³': sql.types.Float, 
    'Stickstoffdioxid Max. 1h-Wert': sql.types.Float,
    'Stickstoffdioxid # 1h-Werte  > 200 µg/m³': sql.types.Float, 
    'Stickstoffdioxid Mess- verfahren': sql.types.String, 
    'PM10 Zeitl. Überdeckung  %': sql.types.Float,
    'PM10 Jahresmittel µg/m³': sql.types.Float, 
    'PM10 # Tagesmittel > 50 µg/m³': sql.types.Float, 
    'PM10 Mess- verfahren': sql.types.String,
    'PM2,5 Zeitl. Überdeckung  %': sql.types.Float, 
    'PM2,5 Jahresmittel µg/m³': sql.types.Float, 
    'PM2,5 Mess- verfahren': sql.types.String,
    'Schwefeldioxid Zeitl. Überdeckung  %': sql.types.Float, 
    'Schwefeldioxid Jahresmittel µg/m³': sql.types.Float, 
    'Schwefeldioxid Max. 1h-Wert': sql.types.Float,
    'Schwefeldioxid # 1h-Werte  > 350 µg/m³': sql.types.Float, 
    'Schwefeldioxid # Tagesmittel > 125 µg/m3': sql.types.Float,
    'Benzol Zeitl. Überdeckung  %': sql.types.Float, 
    'Benzol Jahresmittel µg/m³': sql.types.Float, 
    'Benzol Mess- verfahren': sql.types.String,
    'Blei Zeitl. Überdeckung  %': sql.types.Float, 
    'Blei Jahresmittel µg/m³': sql.types.Float, 
    'Arsen Zeitl. Überdeckung  %': sql.types.Float,
    'Arsen Jahresmittel ng/m³': sql.types.Float, 
    'Cadmium Zeitl. Überdeckung  %': sql.types.Float, 
    'Cadmium Jahresmittel ng/m³': sql.types.Float,
    'Nickel Zeitl. Überdeckung  %': sql.types.Float, 
    'Nickel Jahresmittel ng/m³': sql.types.Float, 
    'Benzopyren Zeitl. Überdeckung  %': sql.types.Float,
    'Benzopyren Jahresmittel ng/m³': sql.types.Float
}
df2.to_sql("airpollution", engine2, if_exists="replace", index=False, dtype=dtype_mapping2_sql)