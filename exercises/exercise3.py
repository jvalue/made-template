import pandas as pd
import sqlalchemy

class CarDataPipeline:
    
    def __init__(self):
        self.url = 'https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv'
        self.engine = sqlalchemy.create_engine("sqlite:///cars.sqlite")
        self.table_name = "cars"

    def load_data(self):
        self.data = pd.read_csv(self.url, sep=';', encoding='iso-8859-1', skiprows=6, skipfooter=4, engine='python')

    def transform_data(self):
        self.data = self.data.iloc[:, [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]]
        self.data = self.data.rename(columns={
            self.data.columns[0]: 'date',
            self.data.columns[1]: 'CIN',
            self.data.columns[2]: 'name',
            self.data.columns[3]: 'petrol',
            self.data.columns[4]: 'diesel',
            self.data.columns[5]: 'gas',
            self.data.columns[6]: 'electro',
            self.data.columns[7]: 'hybrid',
            self.data.columns[8]: 'plugInHybrid',
            self.data.columns[9]: 'others'
        })
        
    def validate_data(self):
        
        self.data['CIN'] = self.data['CIN'].astype(str).str.zfill(5)
        numeric_columns = ['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']
        for col in numeric_columns:
            self.data[col] = pd.to_numeric(self.data[col], errors='coerce')
            self.data = self.data[self.data[col] > 0]
        
    def store_to_database(self):
        
        column_types = {
                    'date': sqlalchemy.String(20),
                    'CIN': sqlalchemy.String(255),
                    'name': sqlalchemy.String(255),
                    'petrol': sqlalchemy.Integer,
                    'diesel': sqlalchemy.Integer,
                    'gas': sqlalchemy.Integer,
                    'electro': sqlalchemy.Integer,
                    'hybrid': sqlalchemy.Integer,
                    'plugInHybrid': sqlalchemy.Integer,
                    'others': sqlalchemy.Integer
                }
        
        self.data.to_sql(name=self.table_name, con=self.engine, if_exists="replace", index=False, dtype=column_types)


    def run_pipeline(self):
        self.load_data()
        self.transform_data()
        self.validate_data()
        self.store_to_database()


pipeline = CarDataPipeline()

# Run the data pipeline
pipeline.run_pipeline()
