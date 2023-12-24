import sqlite3
import pandas as pd
from geopy.geocoders import Nominatim

# connect with database
conn = sqlite3.connect('datasets.sqlite')


# read dataset and create decoder instance
df_immoscout = pd.read_sql_query(f'SELECT * FROM immoscout', conn)  
geolocator = Nominatim(user_agent="user")

# Initialize lists to store latitude and longitude values
latitudes = []
longitudes = []

#create address and then generate longitude and latitude using gep[y library
for index, row in df_immoscout.iterrows():
    address = f"{row['houseNumber']} {row['street']}, {row['cityTown']}, {row['district']}, {row['zipCode']} , {row['federalState']}"

  
    location = geolocator.geocode(address)

    # Check if location exit
    if location is not None:
        latitudes.append(location.latitude)
        longitudes.append(location.longitude)
        print("Address: ", address, "Latitude: ", location.latitude, "Latitude: ", location.longitude)
    else:
        latitudes.append(None)
        longitudes.append(None)

# Adding columns to db
df_immoscout['latitude'] = latitudes
df_immoscout['longitude'] = longitudes
df_immoscout.to_sql('immoscout', conn, if_exists='replace', index=False)

conn.close()