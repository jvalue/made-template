import pandas as pd
from sqlalchemy import create_engine, Table, Column, MetaData
from sqlalchemy.types import BIGINT, TEXT, FLOAT


source_url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
db_file = "airports.sqlite"
table_name = "airports"
column_names = ["id", "airport_name", "city", "country", "iata_code", "icao_code", "latitude", "longitude", "altitude", "timezone"]
column_types = [BIGINT, TEXT, TEXT, TEXT, TEXT, TEXT, FLOAT, FLOAT, FLOAT, TEXT]


def build_data_pipeline(source_url, db_file, table_name, column_names, column_types):
    # Fetch the data from the source URL into a pandas DataFrame
    df = pd.read_csv(source_url, delimiter = ';')
    
    # Create the SQLite engine and connect to the database
    engine = create_engine(f"sqlite:///{db_file}")
    conn = engine.connect()
    
    # Create the metadata and table object
    metadata = MetaData()
    table = Table(table_name, metadata, *[Column(name, column_type) for name, column_type in zip(column_names, column_types)])
    
    # Create the table in the database
    metadata.create_all(engine)
    
    # Write the data from the DataFrame into the table
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    
    # Close the database connection
    conn.close()
    engine.dispose()

# Call the data pipeline function
build_data_pipeline(source_url, db_file, table_name, column_names, column_types)


