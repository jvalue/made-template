
# Build an automated data pipeline for the following source:
# https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv

# Goal:
#   - Write data into a SQLite database called “airports.sqlite”, in the table “airports”
#   - Assign fitting built-in SQLite types (e.g., BIGINT, TEXT or FLOAT) to all columns
#   - Do not rename column names!
#   - No further data validation is required, do not drop any rows or change any data points

import sqlalchemy as sa
from sqlalchemy.types import BIGINT, TEXT, FLOAT
import pandas as pd

def automated_pipeline():

    # files
    source_url = 'https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv'
    db_file = 'airports.sqlite'

    # extract data from source (delimiter = ';')
    data = pd.read_csv(source_url, ';')

    # sqlite engine (three slashes for relative path)
    engine = sa.create_engine(f'sqlite:///{db_file}', echo=False)

    dtype={
        'column_1': BIGINT,
        'column_2': TEXT,
        'column_3': TEXT,
        'column_4': TEXT,
        'column_5': TEXT,
        'column_6': TEXT,
        'column_7': FLOAT,
        'column_8': FLOAT,
        'column_9': BIGINT,
        'column_10': FLOAT,
        'column_11': TEXT,
        'column_12': TEXT,
        'geo_punkt': TEXT,
    }

    # load to file (replaces file content if already exists; no index; uses declared dtype)
    data.to_sql("airports", con=engine, if_exists='replace', index=False, dtype=dtype)
   

if __name__ == '__main__':
    automated_pipeline()