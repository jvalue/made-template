import pandas as pd
#import sqlalchemy as sq
from sqlalchemy import create_engine, Float, Text, Integer

#Fetch and load data into a dataframe
url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
df = pd.read_csv(url, delimiter=';', index_col='column_1')
#print(df.head())

columns_dataTypes = {
    "column_1": Integer(),
    "column_2": Text(),
    "column_3": Text(),
    "column_4": Text(),
    "column_5": Text(),
    "column_6": Text(),
    "column_7": Float(),
    "column_8": Float(),
    "column_9": Integer(),
    "column_10": Float(),
    "column_11": Text(),
    "column_12": Text(),
    "geo_punkt": Text()
}

#created a SQLALchemy engine to connect a database
engine = create_engine('sqlite:///airports.sqlite')

df.to_sql("airports", engine, index=False, if_exists='replace', dtype=columns_dataTypes)
