import pandas as pd


df = pd.read_csv("https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv", sep=";")

df.to_sql("airports", "sqlite:///airports.sqlite", if_exists="replace", index=False)
