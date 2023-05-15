import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from time import time


localPath_Immoscout24 = r"D:\Education\MS-AI\Sem-2\Data Engineering [OSS-AMSE]\2023-amse-template/project\datasets\Immoscout24.csv"
localPath_nuremberg = r"D:\Education\MS-AI\Sem-2\Data Engineering [OSS-AMSE]\2023-amse-template\project\datasets\Nuremberg_Stops_IDs_and_geodata.xlsx"

#url_Immoscout24= "https://drive.google.com/file/d/1-MQG7iSzORQpCtsULyddBFQSWwbLWBA8/view?usp=share_link";
#url_nuremberg= "https://opendata.vag.de/dataset/08eb49f9-0f6c-4b76-96fd-5f8e3a0ac593/resource/c66d5b67-6a01-4190-a9cf-1de6359d07ae/download/20170601_haltestellen_id_geo.xlsx";

############################################
############### Data Extraction ############
############################################
t1 = time()
print("Data Extraction in progress...")
df_nuremberg = pd.read_excel(localPath_nuremberg)
df_Immoscout24 = pd.read_csv(localPath_Immoscout24)
t2 = time()

print("Finish: Data Extraction {} s ".format(t2 - t1))

############################################
############ Data Transformation ###########
############################################
t1 = time()
print("Data Transformation in progress...")

print("Renaming the columns to english titles...")
# Renaming the columns to english titles
df_nuremberg.rename(
    columns={
        "VGNKennung": "VAGIdentifier",
        "VAGKennung": "VAGIdentifierChar",
        "Haltepunkt": "breakpoint",
        "GlobalID": "GlobalID",
        "Haltestellenname": "stopName",
        "latitude": "latitude",
        "longitude": "longitude",
        "Betriebszweig": "branchOfService",
        "Dataprovider": "dataprovider",
    },
    inplace=True,
)

print("Removing Unwanted Columns...")
### Remove Unwanted Columns
df_nuremberg.drop(columns=["breakpoint", "GlobalID", "branchOfService", "dataprovider"])
df_Immoscout24.drop(columns=["picturecount", "scoutId"])

print("Replacing Nan Values...")
# Replace Nan values with 0
df_nuremberg.replace(np.nan, 0)
df_Immoscout24.replace(np.nan, 0)
t2 = time()
print("Finish: Data Transformation {} s ".format(t2 - t1))


############################################
################# Load Data ################
############################################
t1 = time()
print("SQLite DB Creation....")

engine = create_engine("sqlite:///nuremberg_stops_immoscout.db")
df_nuremberg.to_sql("nuremberg_stops", engine, if_exists="replace")
df_Immoscout24.to_sql("immoscout", engine, if_exists="replace")
t2 = time()
print("Finish: Data Loading  {} s ".format(t2 - t1))
