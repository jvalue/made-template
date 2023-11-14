import pandas as pd
import sqlite3

def download_from_url(url):
    data = pd.read_csv(url, low_memory=False, sep=';')
    return data

def save_to_sql(data):
    print(data.shape)
    conn = sqlite3.connect("airports.sqlite")
    cursor = conn.cursor()
    create_table_query = f"CREATE TABLE IF NOT EXISTS airports ({', '.join([f'{col} {data[col].dtype}' for col in data.columns])});"
    cursor.execute(create_table_query)
    data.to_sql("airports.sqlite", conn, if_exists="replace", index=False)
    conn.close()

if __name__=="__main__":
    url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
    data = download_from_url(url)
    save_to_sql(data)