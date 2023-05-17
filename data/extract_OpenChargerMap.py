import requests
import json
import csv

# Set up the API endpoint and parameters
api_url = "https://api.openchargemap.io/v3/poi"
params = {
    "output": "json",
    "countrycode": "DE",
    "maxresults": 43000,  # Number of results to fetch
    "key": "2777768f-8252-49e0-be9e-297268caa42c"  # Replace with your Open Charge Map API key
}

# Send a GET request to the API endpoint
response = requests.get(api_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response data as JSON
    data = json.loads(response.text)
    
    # Specify the CSV file path
    csv_file_path = "/Users/diganto/Data_Engineering/2023-AMSE/data/EV_Charging_Points_Germany.csv"
    
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Town', 'State','Postcode', 'Latitude', 'Longitude','Usage_Type','Status']) 

        # Extract relevant information from the response
        for result in data:
            title = result['AddressInfo']['Title']
            town = result['AddressInfo']['Town']
            State = result['AddressInfo']['StateOrProvince']
            Postcode = result['AddressInfo']['Postcode']
            latitude = result['AddressInfo']['Latitude']
            longitude = result['AddressInfo']['Longitude']
            Usage_type= result['UsageType']['Title'] if result['UsageType'] else 'N/A'
            Status = result['StatusType']['Title']
                     
            
            writer.writerow([title,town,State, Postcode, latitude, longitude, Usage_type, Status])
            
       # print(f"CSV file '{csv_file_path}' created successfully.")

            
else:
    print(f"Error: {response.status_code} - {response.text}")







