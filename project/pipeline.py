import pandas as pd
import sqlite3

class ETLPipeline:
    def _init_(self):
        self.urls = [
            'https://query.data.world/s/3ibkgfh656yrydhmsg4uboxxm7hysr?dws=00000',
            'https://query.data.world/s/2x6uq5jmauvfnmfhc5ud4jv5amq4p6?dws=00000',
            'https://query.data.world/s/nc25wfakg22iva2tmkx4icgfnufggx?dws=00000',
            'https://query.data.world/s/fglgedqxdxc2giqvqgvbjxsqic2tuw?dws=00000',
            'https://query.data.world/s/wva7g5yxspu3bninh4ucn7xrp4h6sc?dws=00000'
        ]
        self.columns_to_string = ['Area', 'Item', 'Element', 'Unit']
        self.columns_to_drop = ['Area Code', 'Item Code', 'Element Code']
        self.years_to_drop = [f'Y{i}F' for i in range(1961, 2020)]
        self.years_to_drop2 = [f'Y{i}' for i in range(1961, 1970)]
    
    def extract(self):
        dataframes = []
        for url in self.urls:
            df = pd.read_csv(url, encoding='latin-1')
            dataframes.append(df)
        return dataframes
    
    def transform(self, dataframes):
        transformed_dataframes = []
        for df in dataframes:
            # Convert specified columns to string type
            df[self.columns_to_string] = df[self.columns_to_string].astype('string')
            # Drop unnecessary columns
            df.drop(columns=self.columns_to_drop + self.years_to_drop + self.years_to_drop2, inplace=True)
            # Forward fill missing values
            df.ffill(inplace=True)
            transformed_dataframes.append(df)
        
        # Concatenate all DataFrames
        concatenated_df = pd.concat(transformed_dataframes, axis=0, ignore_index=True)
        return concatenated_df
    
    def load(self, dataframe, db_name, table_name):
        # Ensure the dataframe has data
        if dataframe.empty:
            print("Dataframe is empty. Nothing to load into the database.")
            return db_name, table_name
        
        print("Dataframe to be loaded:")
        print(dataframe.head())
        
        # Connect to SQLite database
        conn = sqlite3.connect(db_name)
        try:
            # Store the dataframe in the specified table
            dataframe.to_sql(table_name, conn, if_exists='replace', index=False)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Close the connection
            conn.close()
        return db_name, table_name
    
    def run(self, db_name, table_name):
        extracted_data = self.extract()
        print("Extraction completed.")
        
        transformed_data = self.transform(extracted_data)
        print("Transformation completed.")
        
        db_name, table_name = self.load(transformed_data, db_name, table_name)
        print(f"Loading completed. Data saved to database '{db_name}' in table '{table_name}'.")
        
        return extracted_data, transformed_data, db_name, table_name

# Running the ETL pipeline
etl = ETLPipeline()
extracted, transformed, db_name, table_name = etl.run('etl_data.db', 'etl_table')

# for calling
# from etl_pipeline import ETLPipeline

# # Running the ETL pipeline
# etl = ETLPipeline()
# extracted_data, transformed_data, saved_file = etl.run('demo11.csv')