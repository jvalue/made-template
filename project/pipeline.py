import pandas as pd
import sqlite3 as db
df = pd.read_csv(
    "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/env_air_gge?format=SDMX-CSV&compressed=false",
    sep= ",", header=0, na_filter=True)

df.drop_duplicates(inplace = True)

conn = db.connect("../data/dataset.db")

df.to_sql("dataset", conn, if_exists="replace", index=False)

conn.close()