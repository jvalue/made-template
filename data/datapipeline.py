import pandas as pd
import datetime as dt
import numpy as np
import urllib
import os


DATA_DIR = os.path.dirname(__file__)
URL_DS_1 = 'https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Energie/Unternehmen_Institutionen/E_Mobilitaet/Ladesaeuleninfrastruktur.xlsx?__blob=publicationFile'
URL_DS_2_BASE = 'https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ28/fz28_{year:04}_{month:02}.xlsx?__blob=publicationFile'
URL_DS_3 = 'https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/02-bundeslaender.xlsx?__blob=publicationFile'


def get_abbreviations_dict() -> dict[str, str]:
    ''' Returns a dictionary with the abbrevations for every german state based on https://www.destatis.de/DE/Methoden/abkuerzung-bundeslaender-DE-EN.html '''
    return {
        'Baden-Württemberg': 'BW',
        'Bayern': 'BY',
        'Berlin': 'BE',
        'Brandenburg': 'BB',
        'Bremen':'HB',
        'Hamburg':'HH',
        'Hessen':'HE',
        'Mecklenburg-Vorpommern':'MV',
        'Niedersachsen':'NI',
        'Nordrhein-Westfalen':'NW',
        'Rheinland-Pfalz':'RP',
        'Saarland':'SL',
        'Sachsen':'SN',
        'Sachsen-Anhalt':'ST',
        'Schleswig-Holstein':'SH',
        'Thüringen':'TH',
        'Germany':'DE'
    }


def get_datasource_1() -> pd.DataFrame:
    df = pd.read_excel(io=URL_DS_1,
                       sheet_name='4.1 Ladepunkte je BL',
                       header=[6, 7],
                       index_col=4)

    # Drop unimportant rows and columns
    df = df.iloc[:-1, 4:]

    # Assign index and column names
    df.columns.names = ['Date', 'Type']
    df.index.name = 'State'
    
    return df


def get_datasource_2_1() -> pd.DataFrame:
    # Get the latest available version
    today = dt.date.today()
    month, year = today.month, today.year
    df = None
    for _ in range(6):
        month -= 1
        if month == 0:
            month = 12
            year -= 1
        try:
            url = URL_DS_2_BASE.format(year=year, month=month)
            df = pd.read_excel(io=url, 
                               sheet_name='FZ 28.2', 
                               index_col=1)
            break
        except urllib.error.HTTPError:
            continue
    if df is None:
        raise Exception('Couldn\'t load Datasource 2.1')
    
    # Drop unimportant rows and columns
    # Note: Besides the amount of all new registrations, we only need the colums for clectric cars and
    # plug-in-hybrids, because only those are important for the correlation with the charging infrastructure
    df = df.iloc[:, [1, 6, 8]]
    df.dropna(inplace=True)

    # Rename the columns (NR = New Registrations)
    df.columns = ['NR Overall', 'NR Electric', 'NR Plug-in-Hybrid']

    # Just take the rows for the annual amounts
    df = df.loc[list(filter(lambda i: 'Jahr' in i,  df.index))]

    # Rename the index values 
    df.index = df.index.map(lambda i: int(i.split(' ')[1]))
    df.index.name = 'Year'

    # Drop current year, if it isn't complete (we just want data for complete years in the dataframe)
    if month != 12 and year in df.index:
        df = df.drop(year)
    
    return df
    
    
def get_datasource_2_2(year: int, month: int = 12) -> pd.DataFrame:
    url = URL_DS_2_BASE.format(year=year, month=month)
    try:
        df = pd.read_excel(io=url,
                           sheet_name='FZ 28.9',
                           index_col=1)
    except urllib.error.HTTPError:
        raise Exception(f'Couldn\'t load Datasource 2.2 for Year {year} and Month {month}')
        
    # Drop unimportant rows and columns
    # Note: Besides the amount of all new registrations, we only need the colums for clectric cars and
    # plug-in-hybrids, because only those are important for the correlation with the charging infrastructure
    df = df.iloc[:, [1, 6, 8]]
    df.dropna(inplace=True)
    
    # Rename the columns (NR = New Registrations)
    df.columns = ['NR Overall', 'NR Electric', 'NR Plug-in-Hybrid']
    
    # Just take the rows for the summation over the year
    idx = int(np.where(df.index.map(lambda i: i.startswith('Januar-')))[0])
    if month != 1:
        df = df.iloc[idx:]
    else:
        df = df.iloc[:idx]

    # Rename the first index value
    df.index.values[0] = 'Germany'
    
    # Remove the 'Sonstige' Row
    df.drop(index='Sonstige', inplace=True)

    # Assign index name
    df.index.name = 'State'
    
    return df
    

def get_datasource_3() -> pd.DataFrame:
    df = pd.read_excel(io=URL_DS_3,
                       sheet_name='Bundesländer_mit_Hauptstädten',
                       usecols=[0,2],
                       header=None,
                       index_col=None)

    # Drop unimportant rows
    df = df.iloc[7:-16]

    # Rename the columns
    df.columns = ['State', 'Area (km^2)']

    # Remove the number from each state name
    df['State'] = df['State'].apply(lambda x: x[4:] if type(x) is str else x)

    # Set 'Germany' as the state for the last row
    df['State'].iloc[-1] = 'Germany'

    # Drop the rows which contain NaN (= rows for the states capitals)
    df.dropna(inplace=True)

    # Set the State column as the index
    df.set_index('State', inplace=True)

    return df
    


# ------------------------------------------------------------------- #
#                        Relationship over time                       #
# ------------------------------------------------------------------- #

# -------------- Get Datasource 2.1 -------------------

ds2_1 = get_datasource_2_1()

# -------------- Get Datasource 1 -------------------

ds1 = get_datasource_1()

# --------------   Prep Datasource 1 for 'over time' -------------------

# Take the data for whole Germany
ds1_time = ds1.loc['Summe'].unstack()
# Just select the dates which are the fist day of a year
ds1_time = ds1_time[ds1_time.index.map(lambda d: d.day == 1 and d.month == 1)]
# Adapt the index
ds1_time.index = ds1_time.index.map(lambda d: d.year)
ds1_time.index.name = 'Year'
ds1_time.columns.name = None
# Create new dataframe with increase of chargingpoints in one year
ds1_time_increase = ds1_time.diff(periods=-1) * -1
# Rename the columns of both dataframes
# CP = Charging Points (overall), SCP = Standard Charging Points, FCP = Fast Charging Points
# Increase = Increase of chargning points over the year
# Amount = Amount at the beginning of the year
ds1_time_increase.columns = ['Increase SCP', 'Increase FCP', 'Increase CP']
ds1_time.columns = ['Amount SCP', 'Amount FCP', 'Amount CP']
# Add the dataframe for the increase to the original dataframe
ds1_time = pd.concat([ds1_time, ds1_time_increase], axis=1)

# --------------------------  Combine data --------------------------

data_years = pd.concat([ds2_1, ds1_time], axis=1).dropna().astype(int)



# ------------------------------------------------------------------- #
#                        Relationship by states                       #
# ------------------------------------------------------------------- #

# use the last year (to get the data for a whole year)
year = dt.date.today().year - 1

# --------------   Prep Datasource 1 for 'by states' -------------------

# Take the amount of charging points at the start of the year
ds1_states = ds1[dt.datetime(year=year, month=1, day=1)]

# Rename the columns
ds1_states.columns = ['Amount SCP', 'Amount FCP', 'Amount CP']

# Rename the index for the sum over all states to 'Germany'
ds1_states.index.values[-1] = 'Germany'

# Cast the values to integer
ds1_states = ds1_states.astype(int)

# -------------- Get Datasource 2.2 -------------------

ds2_2 = get_datasource_2_2(year=year)

# -------------- Get Datasource 3 ---------------------

ds3 = get_datasource_3()

# ----------- Get Abbreviations Dataframe -------------

abbreviations = get_abbreviations_dict()
df_abbreviations = pd.DataFrame(abbreviations.values(), abbreviations.keys(), columns=['Abbreviation'])
df_abbreviations.index.name = 'State'

# ---------------  Combine data ------------------------

data_states = pd.concat([df_abbreviations, ds3, ds2_2, ds1_states], axis=1)



# ------------------------------------------------------------------- #
#                       Store data to database                        #
# ------------------------------------------------------------------- #

data_years.to_sql('over_time', f'sqlite:////{DATA_DIR}/data.sqlite', if_exists='replace')
data_states.to_sql('by_states', f'sqlite:////{DATA_DIR}/data.sqlite', if_exists='replace')
