import pandas as pd
import sqlalchemy as sql
import numpy as np  

class DataPipeline:
    def __init__(self, url, db_name, table_name):
        #save url link
        self._url = url
        self._db_name = db_name
        self._table_name = table_name
        self._df = None

    def read_csv(self, lines_to_skip, lines_to_read):
        # Read the specified lines from the CSV file into a DataFrame
        #lines_to_skip: I want to start reading lines from 8 row.
        #lines_to_read: Number of lines to read
        self._df = pd.read_csv(self._url, skiprows=lines_to_skip, nrows=lines_to_read, delimiter=';', encoding='latin1')
        self._df.reset_index(inplace=True)

    def read_excel(self, sheet, limits):
        #Get the range of cells where the data is.
        init_row,final_row,init_col,final_col = limits
        #Get the excel file on python
        xls = pd.ExcelFile(self._url)
        #Read an specific sheet
        self._df = pd.read_excel(xls, 'EU-Jahreskenngrößen 2022')
        #Capture the part of the dataframe that is relevant for the analysis
        self._df = self._df.iloc[init_row:final_row,init_col:final_col].copy()
        #Reset index beacuse all indexes are correlated with df2
        self._df.reset_index(inplace=True, drop =True)

    def rename_cols(self, cols_name):
        #Rename columns
        self._df.columns = cols_name

    def del_missing_info(self, col_name, character):
        #Delete row with missing information
        self._df = self._df[self._df[col_name] != character]

    def replace_str(self, strings_to_be_replaced, target):
        for string in strings_to_be_replaced:
            self._df = self._df.replace({string:target})

    def create_sqldb(self, dtype_mapping):
        engine = sql.create_engine(f"sqlite:///data/{self._db_name}.sqlite", echo=False)
        self._df.to_sql(self._table_name, con=engine, if_exists="replace", 
                        index=False, dtype = dtype_mapping)



if __name__ == '__main__':
    #Datasourse 1: Vehicles
    db_url_1 = "https://www.landesdatenbank.nrw.de/ldbnrwws/downloader/00/tables/46251-02iz_00.csv"
    db_name_1 = 'vehicles'
    table_name_1 = 'vehicles'
    dp_1 = DataPipeline(db_url_1, db_name_1, table_name_1)
    dp_1.read_csv(list(range(1, 8)), 61)
    cols_name = ['PC','Province','Vehicles', 'Cars', 'Trucks', 'Tractors', 'Motorcycles']
    dp_1.rename_cols(cols_name)
    dp_1.del_missing_info('Vehicles', "-")
    dtype_mapping_sql = {
        'PC': sql.types.String, 
        'Province': sql.types.String,  
        'Vehicles': sql.types.Integer,
        'Cars': sql.types.Integer,
        'Trucks': sql.types.Integer,
        'Tractors': sql.types.Integer,
        'Motorcycles': sql.types.Integer}
    dp_1.create_sqldb(dtype_mapping_sql)

    #Datasourse 2: AirPollution
    db_url_2 = "https://www.opengeodata.nrw.de/produkte/umwelt_klima/luftqualitaet/luqs/eu_jahreskenngroessen/LUQS-EU-Kenngroessen-2022.xlsx"
    db_name_2 = 'airpollution'
    table_name_2 = 'airpollution'
    dp_2 = DataPipeline(db_url_2, db_name_2, table_name_2)
    dp_2.read_excel('EU-Jahreskenngrößen 2022', (5,158,0,17))
    cols_name2 = ['Name','ID', 'Area name', 'Classification', 'EU-Code',
        'NO2 time coverage %', 'NO2 anual average µg/m³', 
        'NO2 Max. 1h value', 'NO2 # 1h values > 200 µg/m³', 
        'NO2 measuring method', 'PM10 time coverage %',
        'PM10 anual average µg/m³', 'PM10 daily average > 50 µg/m³', 'PM10 measuring method',
        'PM2,5 time coverage %', 'PM2,5 anual average µg/m³', 'PM2,5 measuring method']
    dp_2.rename_cols(cols_name2)
    #Need to erase '---' and '--' from all the cells
    dp_2.replace_str(['---','--','nan'], np.nan)

    dtype_mapping2_sql = {
        'Name': sql.types.String, 
        'ID': sql.types.String, 
        'Area name': sql.types.String, 
        'Classification': sql.types.String, 
        'EU-Code': sql.types.String,
        'NO2 time coverage %': sql.types.Float, 
        'NO2 anual average µg/m³': sql.types.Float, 
        'NO2 Max. 1h value': sql.types.Integer,
        'NO2 # 1h values > 200 µg/m³': sql.types.Integer, 
        'NO2 measuring method': sql.types.String, 
        'PM10 time coverage %': sql.types.Float,
        'PM10 anual average µg/m³': sql.types.Float, 
        'PM10 daily average > 50 µg/m³': sql.types.Float, 
        'PM10 measuring method': sql.types.String,
        'PM2,5 time coverage %': sql.types.Float, 
        'PM2,5 anual average µg/m³': sql.types.Float, 
        'PM2,5 measuring method': sql.types.String}
    dp_2.create_sqldb(dtype_mapping2_sql)