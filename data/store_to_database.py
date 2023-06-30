import pandas as pd
import sqlite3
from geopy.geocoders import Nominatim


# Define a function to get the state based on coordinates
def get_state_by_coord(coord):
        geolocator = Nominatim(user_agent="geoapi")
        location = geolocator.reverse(coord, exactly_one=True)
        address = location.raw['address']
        state = address.get('state', '')
        return state


# Read the CSV files
df_new = pd.read_csv("./data/mobi_data.csv")
df_map = pd.read_csv("./data/EV_Charging_Points_Germany.csv")

# Create a new DataFrame with modified columns
map_df_new = df_map.copy()
map_df_new['coordinates'] = df_map['Latitude'].astype(str) + ", " + df_map['Longitude'].astype(str)
map_df_new["State"] = map_df_new["coordinates"].map(get_state_by_coord, na_action='ignore')
map_df_new = map_df_new.drop(columns=['Latitude', 'Longitude'])

# Merge the DataFrames based on the 'State' column
merged = pd.merge(df_new, map_df_new, on='State', how='inner')

# Save the merged DataFrame to an SQLite database
conn = sqlite3.connect('./data/data.db')  # Connect to the database file
merged.to_sql('charging_station_data', conn, if_exists='replace', index=False)  # Save DataFrame to a table in the database
conn.close()  # Close the database connection




