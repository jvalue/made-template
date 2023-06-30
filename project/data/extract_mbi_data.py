import pandas as pd
import pandas as pd
from geopy.geocoders import Nominatim

class ChargerData:
    def __init__(self, url):
        self.url = url
        self.df = pd.read_csv(url, delimiter=";")
    
    def get_state_by_coord(self, coord):
        geolocator = Nominatim(user_agent="geoapi")
        location = geolocator.reverse(coord, exactly_one=True)
        address = location.raw['address']
        state = address.get('state', '')
        return state
    
    def preprocess_data(self):
        selected_columns = ["betreiber", "art_der_ladeeinrichung", "anzahl_ladepunkte", "anschlussleistung", "koordinaten"]
        self.df = self.df[selected_columns].rename(columns={"betreiber": "Operator", "art_der_ladeeinrichung": "Types_of_Charger", "anzahl_ladepunkte": "Number_of_charging_point", "anschlussleistung": "connected_load", "koordinaten": "Coordinates"})
        value_map = {
            'Normalladeeinrichtung': 'Normal',
            'Schnellladeeinrichtung': 'Fast'
        }
        self.df['Types_of_Charger'] = self.df['Types_of_Charger'].replace(value_map)
    
    def process_data(self):
        self.preprocess_data()
        self.df_new = self.df
        self.df_new["Coordinates"] = self.df_new["Coordinates"].map(self.get_state_by_coord, na_action='ignore')
        self.df_new.rename(columns={"Coordinates": "State"}, inplace=True)
    
    def save_data(self, filename):
        self.df_new.to_csv(filename, index=False)


url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-ladesaulen-in-deutschland/exports/csv"
charger_data = ChargerData(url)
charger_data.process_data()
csv_file_path = "./project/data/mobi_data.csv"
if charger_data:
    charger_data.save_data(csv_file_path)
    
    print(f"CSV file '{csv_file_path}' created successfully.")
else:
    print(f"Error: Failed to create the file.")
