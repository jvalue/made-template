import requests
import pandas as pd
from zipfile import ZipFile
import os
from colorama import init, Fore
from utils import data_directory

# Initialize colorama
init(autoreset=True)


def download_and_extract_zip(url, target_file, extract_to='.'):
    """
    Downloads a ZIP file from a URL and extracts its contents to a specified directory.

    Args:
    - url (str): The URL to the ZIP file.
    - extract_to (str): The directory to extract the contents to.

    Returns:
    - str: The path to the specific extracted CSV file.
    """
    try:
        # Ensure the extract_to directory exists
        if not os.path.exists(extract_to):
            os.makedirs(extract_to)

        # Download the file
        local_zip_path = os.path.join(extract_to, 'temp_data.zip')
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_zip_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        # Extract the file
        with ZipFile(local_zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

        # Clean up the zip file
        os.remove(local_zip_path)

        # Check if the specific CSV file exists in the extracted contents
        target_file_path = os.path.join(extract_to, target_file)
        if os.path.exists(target_file_path):
            print(Fore.GREEN + f"Specific CSV file found: {target_file}")
            return target_file_path

        print(Fore.RED + f"{target_file} not found in the ZIP archive.")
        return None

    except Exception as e:
        print(Fore.RED + f"Error downloading or extracting ZIP file: {e}")
        return None


def extract_fao_temperature_data(zip_url):
    """
    Extracts temperature change data from FAO.

    Args:
    - zip_url (str): The URL to the FAO temperature change dataset ZIP file.

    Returns:
    - pd.DataFrame: DataFrame containing the extracted data.
    """

    target_ = 'Environment_Temperature_change_E_All_Data.csv'
    csv_path = download_and_extract_zip(
        zip_url, target_file=target_, extract_to=data_directory)
    if csv_path:
        try:
            temperature_data = pd.read_csv(csv_path, encoding='utf-8')
            print(
                Fore.GREEN + "Successfully extracted FAO temperature data with UTF-8 encoding.")
            return temperature_data
        except UnicodeDecodeError as e_utf8:
            print(Fore.YELLOW + f"UTF-8 encoding failed: {e_utf8}")
            print(Fore.YELLOW + "Trying latin1 encoding...")
            try:
                temperature_data = pd.read_csv(csv_path, encoding='latin1')
                print(
                    Fore.GREEN + "Successfully extracted FAO temperature data with latin1 encoding.")
                return temperature_data
            except UnicodeDecodeError as e_latin1:
                print(Fore.RED + f"latin1 encoding failed: {e_latin1}")
        except Exception as e:
            print(Fore.RED + f"Error reading CSV file: {e}")
            return None
    return None


def extract_world_bank_co2_data(zip_url):
    """
    Extracts CO2 emissions data from the World Bank.

    Args:
    - zip_url (str): The URL to the World Bank CO2 emissions dataset ZIP file.

    Returns:
    - pd.DataFrame: DataFrame containing the extracted data.
    """
    target_ = 'API_EN.ATM.CO2E.KT_DS2_en_csv_v2_360757.csv'

    csv_path = download_and_extract_zip(
        zip_url, target_file=target_,  extract_to=data_directory)
    if csv_path:
        try:
            co2_data = pd.read_csv(csv_path, skiprows=3, encoding='utf-8')
            print(
                Fore.GREEN + "Successfully extracted World Bank CO2 data with UTF-8 encoding.")
            return co2_data
        except UnicodeDecodeError as e_utf8:
            print(Fore.YELLOW + f"UTF-8 encoding failed: {e_utf8}")
            print(Fore.YELLOW + "Trying latin1 encoding...")
            try:
                co2_data = pd.read_csv(csv_path, skiprows=3, encoding='latin1')
                print(
                    Fore.GREEN + "Successfully extracted World Bank CO2 data with latin1 encoding.")
                return co2_data
            except UnicodeDecodeError as e_latin1:
                print(Fore.RED + f"latin1 encoding failed: {e_latin1}")
        except Exception as e:
            print(Fore.RED + f"Error reading CSV file: {e}")
            return None
    return None
