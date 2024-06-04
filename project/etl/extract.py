import pandas as pd

def fetch_data(url):
    """
    Fetch data from a given URL and return as a DataFrame.
    Args:
        url (str): URL to fetch the CSV data from.
    Returns:
        pd.DataFrame: Data fetched from the URL or an empty DataFrame if an error occurs.
    """
    try:
        return pd.read_csv(url)
    except pd.errors.EmptyDataError as e:
        print(f"Error fetching data from {url}: {e}")
        return pd.DataFrame()  # Return empty DataFrame if there's an error