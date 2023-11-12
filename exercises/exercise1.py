import pandas as pd
from sqlalchemy import create_engine

class DataPipeline:
    def __init__(self) -> None:
        self.data_url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
        self.database_url = "sqlite:///airports.sqlite"

    def extract(self):
        # Extract data from the source URL
        try:
            self.data = pd.read_csv(self.data_url, sep=';')
            print('Here is the printing')
            print(self.data.head)
        except pd.errors.ParserError as e:
            print(f"Error parsing CSV file: {e}")

    def transform(self):
        # Print information about the DataFrame (example transformation)
        print("Transforming data:")
        print(self.data.info())

    def load(self):
        # Load data into SQLite database using SQLAlchemy
        engine = create_engine(self.database_url)
        self.data.to_sql("airports", con=engine, index=False, if_exists="replace")

    def run_pipeline(self):
        self.extract()
        self.transform()
        self.load()

# Instantiate and run the pipeline
pipeline = DataPipeline()
pipeline.run_pipeline()
