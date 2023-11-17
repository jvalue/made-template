from urllib.request import urlretrieve
import os
import pandas
import sqlite3


class DataSource:  
    def __init__(self, url: str, sep: str, type: str, headers: list[str], output_filename: str, comp_type: str) -> None:
        self.url = url
        self.sep = sep
        self.type = type
        self.headers = headers
        self.output_filename = output_filename
        self.comp_type = comp_type
        
class DataBase: 
    def __init__(self, database_name: str, table_name: str) -> None:
        self.database_name = database_name
        self.table_name = table_name
        


class DataPipeline:
    def __init__(self, data_source: DataSource, output_DB: DataBase) -> None:
        self.data_source = data_source
        self.output_DB = output_DB
    
    def extract_data(self):
        file_path=os.path.join(os.getcwd(),"data",f"{self.data_source.output_filename}.{self.data_source.type}")
        urlretrieve(url=self.data_source.url, filename=file_path)
        return file_path
    
    def transform_data(self,file_path):
        #read the file from a location 
        dataframe = pandas.read_csv(
            filepath_or_buffer=file_path, 
            compression=self.data_source.comp_type, 
            sep= self.data_source.sep,
            names= self.data_source.headers,
            )
        return dataframe
        
    
    def load_data(self, dataframe):
        #save dataframe in the database
        connection = sqlite3.connect(
            database = os.path.join(os.getcwd(),"data", self.output_DB.database_name)
        )
        dataframe.to_sql(name = self.output_DB.table_name, con = connection, if_exists= "replace",index = False)
        connection.close()        
    
    def run_pipeline(self): 
        # extract the data
        file_path = self.extract_data()
        # transform the data:cleaning 
        dataframe = self.transform_data(file_path = file_path)
        # load the data 
        self.load_data(dataframe = dataframe)
        # os.remove(path=file_path)
             
        

if __name__ == "__main__": 
    yagon_source = DataSource(
        url = "https://bulk.meteostat.net/v2/daily/48097.csv.gz", 
        sep= "," ,
        type= "gz" , 
        headers= ["Date","Tavg","Tmin","Tmax", "Prcp", "Snow", "Wdir", "Wspd","Wpgt", "Pres", "Tsun"],
        output_filename= "yagon_weatherdata.csv",
        comp_type= "gzip"
    )  
    yagon_DB = DataBase(database_name= "analysis.sqlite", table_name= "weather") 
    yagon_pipeline = DataPipeline(data_source = yagon_source, output_DB=yagon_DB)
    yagon_pipeline.run_pipeline()    
   