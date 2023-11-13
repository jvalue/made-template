from urllib.request import urlretrieve
import os
import pandas
import sqlite3


class DataPipeline:
    def __init__(self) -> None:
        pass
    
    def extract_data(self, url , file_name ):
        file_path=os.path.join(os.getcwd(),"exercises",file_name)
        urlretrieve(url=url, filename=file_path)
        return file_path
    
    def transform_data(self,file_path):
        #read the file from a location 
        dataframe = pandas.read_csv(filepath_or_buffer=file_path, sep= ";", header=0, encoding="utf-8")
        return dataframe
    
    def load_data(self, dataframe):
        #save dataframe in the database
        connection = sqlite3.connect(database = "airports.sqlite")  
        dataframe.to_sql(name = "airports", con = connection, if_exists= "replace",index = False)
        connection.close()        
    
    def run_pipeline(self,data_url,file_name ): 
        # extract the data
        file_path = self.extract_data(url=data_url, file_name = file_name )
        # transform the data:cleaning 
        dataframe = self.transform_data(file_path = file_path)
        # load the data 
        self.load_data(dataframe = dataframe)
        os.remove(path=file_path)
        

if __name__ == "__main__":       
    pipeline = DataPipeline()
    pipeline.run_pipeline(
        data_url= "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv" ,
        file_name="Airport.csv"
    )


    
    