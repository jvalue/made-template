import sqlite3
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Connect to the database
conn = sqlite3.connect('dataset.sqlite')

# Query the database and load all data into a DataFrame
immoscout_table = "SELECT * FROM immoscout"
immoscout_table = pd.read_sql_query(immoscout_table, conn)

# Create a geocoder instance
geolocator = Nominatim(user_agent="my_app")

# Initialize lists to store latitude and longitude values
latitudes = []
longitudes = []

# Iterate over each row in the DataFrame
for index, row in immoscout_table.iterrows():
    # Check if the city is Munich or Nuremberg
    if row['City'] in ['München', 'Nürnberg']:
        address = f"{row['houseNumber']} {row['street']}, {row['Town']}, {row['City']}, {row['zipCode']} , {row['federalState']}"
        try:
            location = geolocator.geocode(address, timeout=10)
            if location is not None:
                latitudes.append(location.latitude)
                longitudes.append(location.longitude)
                print(address, ":", location.latitude, location.longitude)
            else:
                latitudes.append(None)
                longitudes.append(None)
        except GeocoderTimedOut:
            print(f"Geocoding timed out for address: {address}")
    else:
        # For other cities, use the existing latitude and longitude values
        latitudes.append(None)
        longitudes.append(None)

# Add latitude and longitude columns to the DataFrame
immoscout_table['latitude'] = latitudes
immoscout_table['longitude'] = longitudes

# Save the updated DataFrame back to the database
immoscout_table.to_sql('immoscout', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()
