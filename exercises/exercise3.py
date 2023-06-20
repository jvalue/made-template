import pandas as pd
import sqlite3

class CarDataPipeline:
    def __init__(self, url, database, table_name):
        self.url = url
        self.database = database
        self.table_name = table_name

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
        
        self.data['CIN'] = self.data['CIN'].astype(str)
        self.data = self.data[self.data['CIN'].str.len() == 5]
        numeric_columns = ['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']
        self.data[numeric_columns] = self.data[numeric_columns].apply(pd.to_numeric, errors='coerce')
        self.data = self.data.dropna(subset=numeric_columns)
        self.data = self.data[(self.data[numeric_columns] > 0).all(axis=1)]

    def create_database(self):
        
        conn = sqlite3.connect(self.database)
        self.data.to_sql(self.table_name, conn, if_exists='replace', index=False)
        conn.close()

    def run_pipeline(self):
        self.load_data()
        self.transform_data()
        self.validate_data()
        self.create_database()

# Initialize the data pipeline with the necessary parameters
url = 'https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv'
database = "cars.sqlite"
table_name = "cars"
pipeline = CarDataPipeline(url, database, table_name)

# Run the data pipeline
pipeline.run_pipeline()
