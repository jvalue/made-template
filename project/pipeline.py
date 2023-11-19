from urllib.request import urlretrieve
import os
import pandas
import sqlite3
import opendatasets as od


class DataSource:  
    def __init__(self, url: str, sep: str, type: str, headers: list[str], output_filename: str, comp_type: str, sourcename: str, d_name: str ) -> None:
        self.url = url
        self.sep = sep
        self.type = type
        self.headers = headers
        self.output_filename = output_filename
        self.comp_type = comp_type
        self.sourcename = sourcename
        self.d_name = d_name
        
class DataBase: 
    def __init__(self, database_name: str, table_name: str) -> None:
        self.database_name = database_name
        self.table_name = table_name
        


class DataPipeline:
    def __init__(self, data_source: DataSource, output_DB: DataBase) -> None:
        self.data_source = data_source
        self.output_DB = output_DB
    
    def _extract_meteostat_data(self):
        file_path=os.path.join(os.getcwd(),"data",f"{self.data_source.output_filename}.{self.data_source.type}")
        urlretrieve(url=self.data_source.url, filename=file_path)
        return file_path   
    
    def _extract_kaggle_data(self):
        data_dir = "data"
        od.download(
            dataset_id_or_url=self.data_source.url,
            data_dir=data_dir,
            force=False,
            dry_run=False,
        )
        dataset_id = od.utils.kaggle_direct.get_kaggle_dataset_id(
            dataset_id_or_url=self.data_source.url
        )
        id = dataset_id.split("/")[1]
        file_path = os.path.join(data_dir, id, self.data_source.output_filename)
        return file_path      
    
    def extract_data(self):
        if (self.data_source.sourcename == "meteostat"): 
            file_path = self._extract_meteostat_data()
        elif (self.data_source.sourcename == "kaggle"):
            file_path = self._extract_kaggle_data()     
        return file_path
            
 
    
    def _transform_meteostat_data(self, file_path: str):
        dataframe = pandas.read_csv(
                filepath_or_buffer=file_path, 
                compression=self.data_source.comp_type, 
                sep= self.data_source.sep,
                names= self.data_source.headers,
                )
        dataframe.drop(labels = ["Prcp", "Snow", "Wdir", "Wspd","Wpgt", "Pres", "Tsun"], axis=1, inplace= True)
        dataframe.insert(loc=4, column= "City", value= self.data_source.d_name, allow_duplicates = True)
        # dataframe.dropna(axis= 0, inplace= True)
        return dataframe
    
    def _transform_kaggle_data(self, file_path: str):
        dataframe = pandas.read_csv(
                filepath_or_buffer=file_path, 
                compression=self.data_source.comp_type, 
                sep= self.data_source.sep,
                header = self.data_source.headers,
                )
        dataframe.drop(labels = ["Invoice ID", "Branch", "Customer type", "Gender","Unit price", "Tax 5%", "Time","cogs", "gross margin percentage", "gross income", "Rating"], axis=1, inplace= True)
        return dataframe

    def transform_data(self,file_path):
        #read the file from a location
        if (self.data_source.sourcename == "meteostat"): 
            dataframe = self._transform_meteostat_data(file_path=file_path)
        elif (self.data_source.sourcename == "kaggle"): 
            dataframe = self._transform_kaggle_data(file_path=file_path)
        return dataframe
        
    def _load_meteostat_data(self,dataframe):
        connection = sqlite3.connect(
            database = os.path.join(os.getcwd(),"data", self.output_DB.database_name)
        )
        dataframe.to_sql(name = self.output_DB.table_name, con = connection, if_exists= "append",index = False)
    
        connection.close() 
        
    def _load_kaggle_data(self,dataframe):
        connection = sqlite3.connect(
            database = os.path.join(os.getcwd(),"data", self.output_DB.database_name)
        )
        dataframe.to_sql(name = self.output_DB.table_name, con = connection, if_exists= "replace",index = False)
    
        connection.close() 
            
    def load_data(self, dataframe):
        if (self.data_source.sourcename == "meteostat"): 
            self._load_meteostat_data(dataframe = dataframe)
        elif (self.data_source.sourcename == "kaggle"):
            self._load_kaggle_data(dataframe = dataframe)
            
               
    
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
        comp_type= "gzip",
        sourcename= "meteostat",
        d_name= "yagon", 
    )  
    weather_DB = DataBase(database_name= "analysis.sqlite", table_name= "weather") 
    yagon_pipeline = DataPipeline(data_source = yagon_source, output_DB=weather_DB)
    yagon_pipeline.run_pipeline()    
    
    mandalay_source = DataSource(
        url = "https://bulk.meteostat.net/v2/daily/48042.csv.gz", 
        sep= "," ,
        type= "gz" , 
        headers= ["Date","Tavg","Tmin","Tmax", "Prcp", "Snow", "Wdir", "Wspd","Wpgt", "Pres", "Tsun"],
        output_filename= "mandalay_weatherdata.csv",
        comp_type= "gzip",
        sourcename= "meteostat",
        d_name= "mandalay", 
    )  
    mandalay_pipeline = DataPipeline(data_source = mandalay_source, output_DB = weather_DB)
    mandalay_pipeline.run_pipeline()
    
    naypyitaw_source = DataSource(
        url = "https://bulk.meteostat.net/v2/daily/VYNT0.csv.gz", 
        sep= "," ,
        type= "gz" , 
        headers= ["Date","Tavg","Tmin","Tmax", "Prcp", "Snow", "Wdir", "Wspd","Wpgt", "Pres", "Tsun"],
        output_filename= "naypyitaw_weatherdata.csv",
        comp_type= "gzip",
        sourcename= "meteostat",
        d_name= "naypyitaw", 
    )  
    naypyitaw_pipeline = DataPipeline(data_source = naypyitaw_source, output_DB = weather_DB)
    naypyitaw_pipeline.run_pipeline()
   
    supermarket_sales_datasource = DataSource(
        url = "https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales/download?datasetVersionNumber=3", 
        sep= "," ,
        type= "zip", 
        output_filename= "supermarket_sales - Sheet1.csv",
        comp_type= None,
        headers= 0,
        sourcename= "kaggle",
        d_name= None, 
    ) 
    sales_DB = DataBase(database_name= "analysis.sqlite", table_name= "sales") 
    supermarket_sales_pipeline = DataPipeline(data_source = supermarket_sales_datasource, output_DB = sales_DB)
    supermarket_sales_pipeline.run_pipeline()