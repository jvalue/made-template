"""
This module contains funcitons for loading, massaging and storing the data from the datasources
and also a main funciton which combines all processes into one pipeline
"""
import datetime as dt
import os
import time
import urllib
import numpy as np
import pandas as pd


DATA_DIR = os.path.dirname(__file__)
DATABASE_PATH = os.path.join(DATA_DIR, "data.sqlite")

URL_DS_1 = "https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Energie/" + \
 "Unternehmen_Institutionen/E_Mobilitaet/Ladesaeuleninfrastruktur.xlsx?__blob=publicationFile"

URL_DS_2_BASE = "https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ28/" + \
 "fz28_{year:04}_{month:02}.xlsx?__blob=publicationFile"

URL_DS_3 = "https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/" + \
 "Administrativ/02-bundeslaender.xlsx?__blob=publicationFile"


def get_abbreviations_dict() -> dict[str, str]:
    """
    Returns a dictionary with the abbrevations for every german state 
    based on https://www.destatis.de/DE/Methoden/abkuerzung-bundeslaender-DE-EN.html
    """
    return {
        "Baden-Württemberg": "BW",
        "Bayern": "BY",
        "Berlin": "BE",
        "Brandenburg": "BB",
        "Bremen": "HB",
        "Hamburg": "HH",
        "Hessen": "HE",
        "Mecklenburg-Vorpommern": "MV",
        "Niedersachsen": "NI",
        "Nordrhein-Westfalen": "NW",
        "Rheinland-Pfalz": "RP",
        "Saarland": "SL",
        "Sachsen": "SN",
        "Sachsen-Anhalt": "ST",
        "Schleswig-Holstein": "SH",
        "Thüringen": "TH",
        "Germany": "DE",
    }


def get_abbrevations_dataframe() -> pd.DataFrame:
    """ Returns a Dataframe build from the Abrbrevations Dict"""
    abbreviations = get_abbreviations_dict()
    df = pd.DataFrame(
        abbreviations.values(), abbreviations.keys(), columns=["Abbreviation"]
    )
    df.index.name = "State"
    return df


def load_excel_from_url(url: str, sheet: str, params: dict[str, any] = None, retries: int = 0,
                        sec_wait: float = 5) -> pd.DataFrame | None:
    """ 
    Loads an excel sheet from the given url and returns it as a dataframe
     - params is a dictionary for the parameters given to the pandas read_excel funciton
     - retries specifies the amount of retries if loading doesn't work
     - sec_wait specifies the seconds to wait after each retry
    Returns None if the excel sheet couldn't be loaded
    """
    df = None
    if params is None:
        params = {}

    for _ in range(retries+1):
        try:
            df = pd.read_excel(io=url, sheet_name=sheet, **params)
            break
        except (urllib.error.HTTPError, urllib.error.URLError):
            time.sleep(sec_wait)

    return df


def get_datasource_1() -> pd.DataFrame:
    """ Loads Datasource 1 from the url and returns the cleaned dataframe """
    print(" - Loading Datasource 1")

    df = load_excel_from_url(url=URL_DS_1,
                             sheet="4.1 Ladepunkte je BL",
                             params={"header": [6, 7], "index_col": 4},
                             retries=5)
    if df is None:
        raise FileNotFoundError("Couldn't load Datasource 1")

    # Drop unimportant rows and columns
    df = df.iloc[:-1, 4:]

    # Assign index and column names
    df.columns.names = ["Date", "Type"]
    df.index.name = "State"

    # Cast the values to integer
    df = df.astype(int)

    return df


def get_datasource_2_1() -> pd.DataFrame:
    """ Loads Datasource 2.1 from the url and returns the cleaned dataframe """
    print(" - Loading Datasource 2.1")

    # Get the latest available version
    today = dt.date.today()
    month, year = today.month, today.year
    df = None
    for _ in range(6):
        month -= 1
        if month == 0:
            month = 12
            year -= 1
        url = URL_DS_2_BASE.format(year=year, month=month)
        df = load_excel_from_url(url=url,
                                 sheet="FZ 28.2",
                                 params={"index_col": 1},
                                 retries=2, sec_wait=3)
        if df is not None:
            break

    if df is None:
        raise FileNotFoundError("Couldn't load Datasource 2.1")

    # Drop unimportant rows and columns
    # Note: Besides the amount of all new registrations, we only need the colums for clectric cars
    # and plug-in-hybrids, because only those are important for the correlation with the charging
    # infrastructure
    df = df.iloc[:, [1, 6, 8]]
    df.dropna(inplace=True)

    # Rename the columns (NR = New Registrations)
    df.columns = ["NR Overall", "NR Electric", "NR Plug-in-Hybrid"]

    # Just take the rows for the annual amounts
    df = df.loc[list(filter(lambda i: "Jahr" in i, df.index))]

    # Rename the index values
    df.index = df.index.map(lambda i: int(i.split(" ")[1]))
    df.index.name = "Year"

    # Drop current year, if it isn't complete
    # (we just want data for complete years in the dataframe)
    if month != 12 and year in df.index:
        df = df.drop(year)

    return df


def get_datasource_2_2(year: int, month: int = 12) -> pd.DataFrame:
    """ Loads Datasource 2.2 from the url and returns the cleaned dataframe """
    print(" - Loading Datasource 2.2")

    url = URL_DS_2_BASE.format(year=year, month=month)
    df = load_excel_from_url(url=url,
                             sheet="FZ 28.9",
                             params={"index_col": 1},
                             retries=5)
    if df is None:
        raise FileNotFoundError(f"Couldn't load Datasource 2.2 for Year {year} and Month {month}")

    # Drop unimportant rows and columns
    # Note: Besides the amount of all new registrations, we only need the colums for clectric cars
    # and plug-in-hybrids, because only those are important for the correlation with the charging
    # infrastructure
    df = df.iloc[:, [1, 6, 8]]
    df.dropna(inplace=True)

    # Rename the columns (NR = New Registrations)
    df.columns = ["NR Overall", "NR Electric", "NR Plug-in-Hybrid"]

    # Just take the rows for the summation over the year
    idx = int(np.where(df.index.map(lambda i: i.startswith("Januar-")))[0][0])
    if month != 1:
        df = df.iloc[idx:]
    else:
        df = df.iloc[:idx]

    # Rename the first index value
    df.index.values[0] = "Germany"

    # Remove the 'Sonstige' Row
    df.drop(index="Sonstige", inplace=True)

    # Assign index name
    df.index.name = "State"

    return df


def get_datasource_3() -> pd.DataFrame:
    """ Loads Datasource 3 from the url and returns the cleaned dataframe """
    print(" - Loading Datasource 3")

    df = load_excel_from_url(url=URL_DS_3,
                             sheet="Bundesländer_mit_Hauptstädten",
                             params={"usecols": [0, 2], "header": None, "index_col": None},
                             retries=5)
    if df is None:
        raise FileNotFoundError("Couldn't load Datasource 3")

    # Drop unimportant rows
    df = df.iloc[7:-16]

    # Rename the columns
    df.columns = ["State", "Area (km^2)"]

    # Remove the number from each state name
    df["State"] = df["State"].apply(lambda x: x[4:] if isinstance(x, str) else x)

    # Set 'Germany' as the state for the last row
    df["State"].iloc[-1] = "Germany"

    # Drop the rows which contain NaN (= rows for the states capitals)
    df.dropna(inplace=True)

    # Set the State column as the index
    df.set_index("State", inplace=True)

    return df


def prep_datasource_1_over_time(df: pd.DataFrame) -> pd.DataFrame:
    """ Prepares Datasource 1 for further use for data over time """
    # Take the data for whole Germany
    df = df.loc["Summe"].unstack()

    # Just select the dates which are the fist day of a year
    df = df[df.index.map(lambda d: d.day == 1 and d.month == 1)]

    # Adapt the index
    df.index = df.index.map(lambda d: d.year)
    df.index.name = "Year"
    df.columns.name = None

    # Create new dataframe with increase of chargingpoints in one year
    df_increase = df.diff(periods=-1) * -1

    # Rename the columns of both dataframes
    # CP = Charging Points (overall), SCP = Standard Charging Points, FCP = Fast Charging Points
    # Increase = Increase of chargning points over the year
    # Amount = Amount at the beginning of the year
    df_increase.columns = ["Increase SCP", "Increase FCP", "Increase CP"]
    df.columns = ["Amount SCP", "Amount FCP", "Amount CP"]

    # Add the dataframe for the increase to the original dataframe
    df = pd.concat([df, df_increase], axis=1)

    # Drop NaN entries and cast the values to integer
    df = df.dropna().astype(int)

    return df


def prep_datasource_1_by_states(df: pd.DataFrame, year: int) -> pd.DataFrame:
    """ Prepares Datasource 1 for further use for data by states """
    # Take the amount of charging points at the start of the year
    df = df[dt.datetime(year=year, month=1, day=1)]

    # Rename the columns
    df.columns = ["Amount SCP", "Amount FCP", "Amount CP"]

    # Rename the index for the sum over all states to 'Germany'
    df.index.values[-1] = "Germany"

    return df


def combine_dataframes(data: list[pd.DataFrame]) -> pd.DataFrame:
    """ Combines a list of dataframes and drops unmergable rows """
    return pd.concat(data, axis=1).dropna()


def store_dataframe(df: pd.DataFrame, table: str):
    """ Stores a dataframe as a table in an sqlite database """
    print(f" - Storing Data into table '{table}' of database '{os.path.basename(DATABASE_PATH)}'")
    df.to_sql(table, f"sqlite:////{DATABASE_PATH}", if_exists="replace")


def main():
    """ 
    Main function of module: 
    Loads in datasources, massages data and stores it to the database 
    """
    print("----------- Starting Datapipeline -----------")

    # use the last year (to get the data for a whole year)
    year = dt.date.today().year - 1

    # ---------------- Loading data ----------------
    print("Loading the Data")
    ds1 = get_datasource_1()
    ds2_1 = get_datasource_2_1()
    ds2_2 = get_datasource_2_2(year=year)
    ds3 = get_datasource_3()

    # ------------- Transforming data --------------
    print("Transforming the Data")
    # Data over time
    ds1_time = prep_datasource_1_over_time(ds1)
    data_time = combine_dataframes([ds2_1, ds1_time]).astype(int)
    # Data by states
    ds1_states = prep_datasource_1_by_states(ds1, year)
    df_abbreviations = get_abbrevations_dataframe()
    data_states = combine_dataframes([df_abbreviations, ds3, ds2_2, ds1_states])

    # ----------------- Storing data ----------------
    print("Storing the Data")
    store_dataframe(data_time, "over_time")
    store_dataframe(data_states, "by_states")

    print("----------- Finished Datapipeline -----------")


if __name__ == "__main__":
    main()
