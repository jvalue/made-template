import pandas as pd
from sqlalchemy import create_engine, engine


class DataPipeline:
    def __init__(self) -> None:
        #Giving the URL for the date Source
        self.data_url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
        self.database_url = "sqlite:///airports.sqlite"
    
    def extract(self):
        #Extracting CSV data from the URL
        
            self.data = pd.read_csv(self.data_url, sep=';')
            print(self.data.head)
           
        
    def transform(self):
        #Get information about the dataframe
        print("Trasforming data:")
        print(self.data.info())
    
    def load(self):
        #Loadt data into the SQLlite database
        engine = create_engine(self.database_url)
        self.data.to_sql("airports", con=engine, index=False, if_exists="replace")
        
    
    def run_pipeline(self):
        self.extract()
        self.transform()
        self.load()
    

pipeline = DataPipeline()
pipeline.run_pipeline()