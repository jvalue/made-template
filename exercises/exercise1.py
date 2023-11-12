import pandas as pd
import sqlalchemy as sqla


url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
airports = pd.read_csv(url, sep=";")
airports.set_index("column_1", inplace=True)
engine = sqla.create_engine("sqlite:///airports.sqlite")
airports.to_sql("airports", engine, if_exists="replace", index=True)
engine.dispose()