import sqlite3
import pandas as pd

def filter_df(df_name):
    df_name.rename(columns = { 'MONATSZAHL':'Info','AUSPRAEGUNG':'Detail','JAHR':'Year','MONAT':'Month','WERT':'Value'}, inplace = True)
    df_name.dropna(subset=['Value'], inplace = True)
    return df_name

def create_table(table_name,df_name,conn):
    
    c = conn.cursor()
    c.execute("""
              CREATE TABLE IF NOT EXISTS {}(
                  Info TEXT,
                  Detail TEXT,
                  Year INTEGER,
                  Month INTEGER,
                  Value Float)
                  """.format(table_name))
    conn.commit()
    df_name.to_sql(table_name, conn, if_exists='replace')
    conn.commit()

if __name__ == '__main__':
    
    accidents_df = pd.read_csv(' https://opendata.muenchen.de/dataset/5e73a82b-7cfb-40cc-9b30-45fe5a3fa24e/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7/download/monatszahlen2307_verkehrsunfaelle_10_07_23_nosum.csv', 
                               usecols=['MONATSZAHL','AUSPRAEGUNG','JAHR','MONAT','WERT'], on_bad_lines='skip')
    weather_df = pd.read_csv(' https://opendata.muenchen.de/dataset/d7e42935-8884-40d3-9284-096d9cafecdd/resource/64c8c183-7fd0-4b29-9958-4169d22ee883/download/monatszahlen2307_witterung_10_07_23_nosum.csv', 
                               usecols=['MONATSZAHL','AUSPRAEGUNG','JAHR','MONAT','WERT'], on_bad_lines='skip')
    
    accidents_df = filter_df(accidents_df)
    weather_df = filter_df(weather_df)
    
    #print(accidents_df)
    #print(weather_df)
    
    conn = sqlite3.connect(r'C:\Users\Impana\OneDrive\Desktop\MAde_project\project\data\my_database_db')
    create_table('Accidents',accidents_df,conn)
    create_table('Weather',weather_df,conn)
    df_out = pd.read_sql_query("""SELECT * FROM Accidents where Info = 'Alkoholunfälle'""", conn)
    print(df_out)
    exit(0)
