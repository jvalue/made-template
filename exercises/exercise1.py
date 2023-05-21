import pandas as pd
from sqlalchemy import String, Float, BIGINT, TEXT, INTEGER


df = pd.read_csv("https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv", sep=";")

df.to_sql("airports", "sqlite:///./exercises/airports.sqlite", if_exists="replace",index=False)