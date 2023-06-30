import requests
import json
import csv

class OpenChargeMapAPI:
    def __init__(self, api_key):
        self.api_url = "https://api.openchargemap.io/v3/poi"
        self.params = {
            "output": "json",
            "countrycode": "DE",
            "maxresults": 40000,
            "key": api_key
        }
    
    def fetch_data(self):
        response = requests.get(self.api_url, params=self.params)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return None
    
    def extract_information(self, data):
        extracted_data = []
        for result in data:
            address_info = result['AddressInfo']
            usage_type = result['UsageType']['Title'] if result['UsageType'] else 'N/A'
            status = result['StatusType']['Title']
            extracted_data.append({
                'Title': address_info['Title'],
                'Town': address_info['Town'],
                'State': address_info['StateOrProvince'],
                'Postcode': address_info['Postcode'],
                'Latitude': address_info['Latitude'],
                'Longitude': address_info['Longitude'],
                'Usage_Type': usage_type,
                'Status': status
            })
        return extracted_data
    
    def save_to_csv(self, data, csv_file_path):
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Town', 'State', 'Postcode', 'Latitude', 'Longitude', 'Usage_Type', 'Status'])
            for row in data:
                writer.writerow(list(row.values()))

# Set up the API endpoint and parameters
api_key = "2777768f-8252-49e0-be9e-297268caa42c"  # Replace with your Open Charge Map API key
open_charge_map_api = OpenChargeMapAPI(api_key)

# Fetch data from the API
data = open_charge_map_api.fetch_data()

if data:
    # Specify the CSV file path
    csv_file_path = "./data/EV_Charging_Points_Germany.csv"
    
    # Extract relevant information from the response
    extracted_data = open_charge_map_api.extract_information(data)
    
    # Save extracted data to CSV
    open_charge_map_api.save_to_csv(extracted_data, csv_file_path)
    
    print(f"CSV file '{csv_file_path}' created successfully.")
else:
    print(f"Error: Failed to fetch data from the API.")







