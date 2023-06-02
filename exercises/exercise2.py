import os
print(os.path.abspath(''))

import pandas as pd
import sqlalchemy

df = pd.read_csv("exercises/D_Bahnhof_2020_alle.csv", sep=";")
df = df.drop(columns=["Status"])

df = df.dropna()

verkehr_valids = ["FV", "RV", "nur DPN"]
df = df[df["Verkehr"].isin(verkehr_valids)]

df["Laenge"] = df["Laenge"].replace(to_replace=r",", value=".",regex=True)
df["Breite"] = df["Breite"].replace(to_replace=r",", value=".",regex=True)
df["Laenge"] = df["Laenge"].astype(float)
df["Breite"] = df["Breite"].astype(float)
df = df[df["Laenge"] >= -90]
df = df[df["Laenge"] <= 90]
df = df[df["Breite"] >= -90]
df = df[df["Breite"] <= 90]

df["IFOPT"] = df["IFOPT"].str.extract('(^[a-zA-Z]{2}:[0-9]*:[0-9]*[:[0-9]*]*)')

df.to_sql("trainstops", con="sqlite:///trainstops.sqlite")