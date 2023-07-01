import pandas as pd
import sqlite3
from geopy.geocoders import Nominatim
from sqlalchemy import create_engine

# Define a function to get the state based on coordinates
def get_state_by_coord(coord):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.reverse(coord, exactly_one=True)
    if location is None:
        return "Unknown"
    address = location.raw.get('address', {})
    state = address.get('state', 'Unknown')
    return state


# Read the CSV files
df_new = pd.read_csv("./project/data/mobi_data.csv")
df_map = pd.read_csv("./project//data/EV_Charging_Points_Germany.csv")

# Create a new DataFrame with modified columns
map_df_new = df_map.copy()
map_df_new['coordinates'] = df_map['Latitude'].astype(str) + ", " + df_map['Longitude'].astype(str)
map_df_new["State"] = map_df_new["coordinates"].map(get_state_by_coord, na_action='ignore')
map_df_new = map_df_new.drop(columns=['Latitude', 'Longitude','Title','Town','Postcode','Status'])

# Merge the DataFrames based on the 'State' column
merged = pd.merge(df_new, map_df_new, on='State', how='inner')


db_file = "./data.sqlite"
table_name = "CSP"
# Create the SQLite engine and connect to the database
engine = create_engine(f"sqlite:///{db_file}")
conn = engine.connect()

# Write the data from the DataFrame into the table
merged.to_sql(table_name, conn, if_exists="replace", index=False)

# Close the database connection
conn.close()
engine.dispose()




