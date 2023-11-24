import requests
import pandas as pd
from io import StringIO
import sqlite3
import os


parking_garages = 'https://opendata.muenchen.de/dataset/addaa7d4-40be-4621-846e-c5358cbe3f26/resource/e0e0e4e1-1b25-4c04-a0ea-cf9cc8335c57/download/230907places.csv'
disabled_parking_space= 'https://opendata.muenchen.de/dataset/80a2d76a-ebc9-40b5-b54c-b5c8af9df65f/resource/c1166a5a-5764-47e1-92bb-2d63dab785eb/download/220624_behindertenparkplaetze_muenchen.csv'

parking_response = requests.get(parking_garages)
disabled_response= requests.get(disabled_parking_space)

parking_data = parking_response.text
disabled_data = disabled_response.text

parking_df = pd.read_csv(StringIO(parking_data))
parking_df = parking_df.fillna(0) 


disabled_df = pd.read_csv(StringIO(disabled_data))
disabled_df = disabled_df.fillna(0) 



root_dir = os.path.abspath('.')
print(root_dir)


data_dir = os.path.join(root_dir, 'data')
db_path = os.path.join(data_dir, 'my_database.db')



conn = sqlite3.connect(db_path)
parking_df.to_sql('parking_table', conn, if_exists='replace', index=False)
disabled_df.to_sql('disabled_table', conn, if_exists='replace', index=False)
conn.close()

conn = sqlite3.connect(db_path)
cursor = conn.cursor()


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = cursor.fetchall()
table_names = [name[0] for name in table_names]


print("Tables (datasets) in the database:")
for table_name in table_names:
    print(table_name)


conn.close()

print("Data pipeline complete! and datasets are succesfully stored in the database")
print(db_path)
#print(parking_df)
#print(disabled_df)
