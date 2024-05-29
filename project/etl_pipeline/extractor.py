import requests
import pandas as pd
from io import StringIO

def extract_csv(csv_url: str) -> pd.DataFrame:
    """
    Downloads a CSV file from a given URL and returns it as a DataFrame.
    
    :param csv_url: URL of the CSV file to be downloaded.
    :type csv_url: str
    :return: DataFrame containing the CSV data.
    :rtype: pd.DataFrame
    """
    response = requests.get(csv_url)
    response.raise_for_status()  
    
    csv_data = StringIO(response.text)
    df = pd.read_csv(csv_data)
    
    return df

