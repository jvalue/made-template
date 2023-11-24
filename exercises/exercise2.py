import pandas as pd
from sqlalchemy import create_engine, FLOAT, BIGINT, NVARCHAR

# Define the source CSV URL
csv_url = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"

# Function to load data from CSV and perform required transformations
def load_and_transform_data(csv_url: str) -> pd.DataFrame:
    # Load data from CSV
    df = pd.read_csv(csv_url, sep=';', decimal=',')
 
    # Drop the "Status" column
    df = df.drop(columns=["Status"], errors="ignore")
    
    # Drop rows with invalid values
    df = df.dropna()
    
    # Filter rows with valid "Verkehr" values
    valid_verkehr_values = ['FV', 'RV', 'nur DPN']
    df = df[df["Verkehr"].isin(valid_verkehr_values)]
    
    # Filter rows with valid "Laenge" and "Breite" values
    valid_coordinate_range = (-90, 90)
    df = df[(df["Laenge"] >= valid_coordinate_range[0]) & (df["Laenge"] <= valid_coordinate_range[1])]
    df = df[(df["Breite"] >= valid_coordinate_range[0]) & (df["Breite"] <= valid_coordinate_range[1])]

    # Filter rows with valid "IFOPT" values
    df = df[df["IFOPT"].str.match(r'^..:[0-9]+:[0-9]+(:[0-9]+)?$')]

    return df

# Function to write data to SQLite database
def write_to_sqlite(df: pd.DataFrame, database_name: str, table_name: str) -> None:
    engine = create_engine(f"sqlite:///{database_name}")
    types = {
        'EVA_NR': BIGINT,
        'DS100': NVARCHAR(length=128),
        'IFOPT': NVARCHAR(length=128),
        'NAME': NVARCHAR(length=128),
        'Verkehr': NVARCHAR(length=128),
        'Laenge': FLOAT(asdecimal=True),
        'Breite': FLOAT(asdecimal=True),
        'Betreiber_Name': NVARCHAR(length=128),
        'Betreiber_Nr': BIGINT
    }
    df.to_sql("trainstops", con=engine, index=False, if_exists='replace', dtype=types)
# Execute the pipeline
if __name__ == "__main__":
    data = load_and_transform_data(csv_url)
    write_to_sqlite(data, "trainstops.sqlite", "trainstops")
