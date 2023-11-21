import urllib.request
import os.path
import pandas as pd
import zipfile
from datetime import datetime, date
import sqlalchemy as sqla


# This file is intentionally "overcomplex" (f.e. union()) to allow for easy addition
# of equally shaped data, for example different years of weather data

# Map storage locations to download links
datasets = {
    "data/bicycletheft.csv": "https://www.polizei-berlin.eu/Fahrraddiebstahl/Fahrraddiebstahl.csv",
    "data/airtemp_berlin_brandenburg.zip": "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/historical/stundenwerte_TU_00427_19730101_20221231_hist.zip",
    "data/precipitation_berlin_brandenburg.zip": "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/precipitation/historical/stundenwerte_RR_00427_19950901_20221231_hist.zip"
}

# All DWD percipitation dataset paths
datasets_dwd_precipitation = []

# All DWD air temperature dataset paths
datasets_dwd_air_temperature = []
datasets_bt = ["data/bicycletheft.csv"]

# Main entry point
def pipeline():
    download_datasets()
    unzip_dwd_data()
    dwd_data = read_dwd_data()
    bicycle_theft_data = read_bicycle_theft_data()
    print(dwd_data.dtypes)
    print(dwd_data.dtypes)
    write_sql(dwd_data, "dwd")
    write_sql(bicycle_theft_data, "bicycle_theft")

# Download the datasets
def download_datasets():
    for filename, url in datasets.items():
        if(not os.path.exists(filename)):
            print("Downloading {} from {}".format(filename, url))
            urllib.request.urlretrieve(filename=filename,url=url)
        else:
            print("File {} already present, skipping...".format(filename))

# Unzip the downloaded datasets
def unzip_dwd_data():
    zipfiles = [filename for filename,url in datasets.items() if url.startswith("https://opendata.dwd.de") and filename.endswith("zip")]
    for file in zipfiles:
        archive = zipfile.ZipFile(file)
        relevant_files = [zipinfo.filename for zipinfo in archive.filelist if zipinfo.filename.startswith("produkt")]
        for relevant_file in relevant_files:
            res_path = zipfile.ZipFile(file).extract(member=relevant_file,path="data/")
            if("precipitation" in file):
                datasets_dwd_precipitation.append(res_path)
            elif("airtemp" in file):
                datasets_dwd_air_temperature.append(res_path)

# Read, transform and clean DWD data (DWD data is static)
def read_dwd_data():
    precipitation_sets = [read_csv_dwd(path) for path in datasets_dwd_precipitation]
    air_temp_sets = [read_csv_dwd(path) for path in datasets_dwd_air_temperature]
    precipation_data = union(precipitation_sets)
    air_temp_data = union(air_temp_sets)

    # Merge percipitation and air temperture data
    joined_data = pd.merge(precipation_data,air_temp_data,on=["MESS_DATUM","STATIONS_ID"])
    joined_data["date_hour"] = pd.to_datetime(joined_data["MESS_DATUM"],format="%Y%m%d%H")

    # Filter invalid measurements
    joined_data = joined_data.loc[joined_data["RS_IND"]!=-999]

    # Convert to boolean
    joined_data["RS_IND"] = joined_data["RS_IND"].map(lambda x: x==1)

    # Drop unused columns
    joined_data.drop(columns=["eor_x","eor_y","MESS_DATUM", "QN_9","QN_8"],errors="ignore",inplace=True)

    # Translate and shorten
    joined_data["WRTR"] = joined_data["WRTR"].map(
        {
        0:"none",
        9:"mv",
        8:"liquid and solid",
        7:"solid",
        6:"liquid",
        4:"unassertable",
        1:"deprecated",
        -999:"na"
        }
    )

    # Rename columns for better readability
    joined_data = joined_data.rename(
        columns={
            "STATIONS_ID": "weatherstation_id",
            "  R1": "precipitation",
            "RS_IND": "has_precipitation",
            "WRTR": "precipitation_type",
            "TT_TU": "air_temperature",
            "RF_TU": "humidity"
        })
    return joined_data

# Read, transform and clean the bicycle theft data
def read_bicycle_theft_data():
    bicycle_theft_sets = [read_csv_bt(path) for path in datasets_bt]
    bt_data = union(bicycle_theft_sets)

    # Convert time formats
    bt_data = parse_bt_times(bt_data)

    # Translate
    bt_data["only_attempted"] = bt_data["VERSUCH"].map(translate_yes_no)

    bt_data = bt_data.rename(columns={
        "LOR": "region_identifier",
        "SCHADENSHOEHE": "damages_amount_euro",
        "ART_DES_FAHRRADS": "type_of_bike",
        "DELIKT": "type_of_crime",
        "ERFASSUNGSGRUND":"type_of_theft"
    })

    # Old columns
    bt_data = bt_data.drop(columns=[
        "TATZEIT_ANFANG_DATUM"
        ,"TATZEIT_ANFANG_STUNDE"
        ,"TATZEIT_ENDE_DATUM"
        ,"TATZEIT_ENDE_STUNDE"
        ,"ANGELEGT_AM"
        ,"VERSUCH"])

    # The Berlin bicycle dataset is updated daily with new theft data. It currently seems that data will only be appended,
    # however, if old data is removed, a archived version must be used and the link in datasets must be added.
    # The relevant data is currently the year 2022.    
    if(dataset_too_new(bt_data)):
        raise Exception("""Bicycle theft dataset does not contain the relevant information anymore (it is too new).
         "Please change the link""")

    return bt_data


def dataset_too_new(bt_data):
     return bt_data[(bt_data["created_time"] > datetime(year=2022,month=1,day=1)) & (bt_data["created_time"] < datetime(year=2022,month=12,day=30))].size==0

# Translate german ja/nein/unbekannt to their english equivalents
def translate_yes_no(x):
    x = x.lower()
    mapping = {
        "ja":"yes",
        "nein":"no"}
    if(x in mapping.keys()):
        return mapping[x]
    else:
        return "unknown"

# Convert time string to datetime
def parse_bt_times(bt_data):
    DATE_FORMAT = "%d.%m.%Y"
    bt_data["theft_begin_time"] = bt_data.apply(lambda row: datetime.strptime(row["TATZEIT_ANFANG_DATUM"],DATE_FORMAT).replace(hour=row["TATZEIT_ANFANG_STUNDE"]),axis=1)
    bt_data["theft_end_time"] = bt_data.apply(lambda row: datetime.strptime(row["TATZEIT_ENDE_DATUM"],DATE_FORMAT).replace(hour=row["TATZEIT_ENDE_STUNDE"]),axis=1)
    bt_data["created_time"] = pd.to_datetime(bt_data["ANGELEGT_AM"],format=DATE_FORMAT)
    return bt_data
    
# Write a dataframe
def write_sql(df, table_name):
    engine = sqla.create_engine("sqlite:///data/bt_and_weather.sqlite")
    df.to_sql(table_name, engine, if_exists="replace", index=True)
    engine.dispose()

# Read csv with settings specific to DWD data
def read_csv_dwd(file):
    return pd.read_csv(filepath_or_buffer=file,sep=";",quotechar='"')

# Read csv with settings specific to BT data
def read_csv_bt(file):
    return pd.read_csv(filepath_or_buffer=file,sep=",",encoding_errors="ignore")

# Build the union of equally formatted datasets, f.e. for different years
def union(sets):
    superset = sets.pop()
    for set in sets:
        superset.append(set)
    return superset

# main function
if __name__=="__main__":
    pipeline()