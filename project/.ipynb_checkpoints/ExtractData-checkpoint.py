# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:49:00 2024

@author: Akash
"""

import os
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


class ExtractData:
    #Kaggle API initialization
    def __init__(self):
        self.kaggle_api = KaggleApi()
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(self.script_dir,'..','data')
        self.download_dir = os.path.abspath(self.data_dir)
        os.environ['KAGGLE_CONFIG_DIR'] = os.path.join(self.script_dir,".kaggle")

        
    # This will call kaggle api, perform authentication and download data in Data directory
    def download_dataset(self,dataset_name):
        self.kaggle_api.authenticate()
        self.kaggle_api.dataset_download_files(dataset_name, path=self.download_dir, unzip=True)
        
     
    
    def load_and_clean_data(self,dataset_name):
        print("Data Transformation")
        dataset = pd.read_csv(os.path.join(self.download_dir,dataset_name))
        numeric_mean = dataset.select_dtypes(include=[np.number]).mean()
        df_numeric_imputed =dataset.select_dtypes(include=[np.number]).fillna(numeric_mean)
        dataset_imputed = pd.concat([dataset.select_dtypes(exclude=[np.number]),df_numeric_imputed],axis=1)
        return dataset_imputed
    
    def save_data(self,database_name,dataset,table_name):
        print("Load into Sqlite\n")
        engine = create_engine(f'sqlite:///{self.download_dir}/{database_name}.sqlite')
        dataset.to_sql(table_name,con=engine,if_exists='replace',index=False)
        engine.dispose()
    
    def remove_unnecessary_files(self):
        print("Removing Unnecessary Files")
        for filename in os.listdir(self.download_dir):
            if not filename.endswith(".sqlite"):
              file_path = os.path.join(self.download_dir, filename)
              
              if os.path.isfile(file_path):
                  os.remove(file_path)
                  print(f"file removed: {filename}")
    
        
        
        
        
        
        
#pipeline
if __name__ == '__main__':    
    extract = ExtractData()
    
    try:    
        extract.download_dataset('alessandrolobello/agri-food-co2-emission-dataset-forecasting-ml')        
        dataset = extract.load_and_clean_data('Agrofood_co2_emission.csv')   
        extract.save_data('ClimateDB', dataset,"emission")   

        print("Loading new data\n")             
        extract.download_dataset("rajkumarpandey02/2023-world-population-by-country")
        dataset = extract.load_and_clean_data("countries-table.csv")
        extract.save_data('ClimateDB', dataset,"population")  
    finally:
        extract.remove_unnecessary_files()
            
        
        
        
        
        
        
        
        
        
        
        