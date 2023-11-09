import pandas as pd
from sqlalchemy import create_engine

# URL of the data source
data_source_url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"

# SQLite database file and table name
database_name = "airports.sqlite"
table_name = "airports"

# Download and Read the CSV data into a Pandas DataFrame 
try:
    data_frame = pd.read_csv(data_source_url, low_memory=False , sep=';')

    # Create SQLite engine and write the DataFrame to the database
    engine = create_engine(f"sqlite:///{database_name}")
    data_frame.to_sql(table_name, engine, if_exists="replace", index=False)

    # Close database connection
    engine.dispose()

    print(f"Data has been successfully written to {database_name} in the table {table_name}")
except Exception as e:
    print(f"Failed to read CSV data: {str(e)}")




# import pandas as pd
# from sqlalchemy import create_engine

# # URL in Variable speichern
# url = 'https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv'

# # Den lokalen Dateipfad und Name für die Datenbank definieren (hier im selben Verzeichnis)
# db_path = 'airports.sqlite'

# # Die Daten von der URL abrufen und mit Pandas Funktion lesen. WICHTIG: Anmerken dass es mit Semikolon getrent wird! (https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas-read-csv)
# data = pd.read_csv(url, sep=';')

# # Eine Verbindung mit einer lokalen SQLite-Datenbank herstellen. (https://docs.sqlalchemy.org/en/20/core/engines.html)
# engine = create_engine('sqlite:///' + db_path)

# # Die Daten in die Datenbank einfügen (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)
# data.to_sql('airports', engine, if_exists='replace', index=False)

# # Datenbankverbindung beenden
# engine.dispose()