import pandas as pd
from sqlalchemy import create_engine


def extract_data_csv(file_path):
    """Extracts data from a CSV file."""
    try:
        df = pd.read_csv(file_path, sep=';', low_memory=False)
        print("Data successfully extracted from CSV.")
        return df
    except Exception as e:
        print(f"Failed to read CSV file: {e}")
        return None


def validate_and_transform_data(df):
    """Validates and transforms train data."""
    if df is None:
        return None

    try:
        # Dropping 'Status' column and replacing comma with dot in 'Laenge' and 'Breite'
        df.drop(columns=['Status'], inplace=True)
        df['Laenge'] = df['Laenge'].str.replace(',', '.').astype(float)
        df['Breite'] = df['Breite'].str.replace(',', '.').astype(float)

        # Filtering data based on given conditions
        valid_conditions = (
            df["Verkehr"].isin(["FV", "RV", "nur DPN"]) &
            df["Laenge"].between(-90, 90) &
            df["Breite"].between(-90, 90) &
            df["IFOPT"].str.match(r"^[A-Za-z]{2}:\d+:\d+(?::\d+)?$")
        )
        df = df[valid_conditions].dropna()

        # Changing data types
        data_types = {
            "EVA_NR": int, "DS100": str, "IFOPT": str,
            "NAME": str, "Verkehr": str, "Laenge": float,
            "Breite": float, "Betreiber_Name": str, "Betreiber_Nr": int
        }
        df = df.astype(data_types)

        print("Data transformation successful.")
        return df

    except Exception as e:
        print(f"Data transformation failed: {e}")
        return None


def load_data_to_db(df, table_name, db_name="trainstops.sqlite"):
    """Loads data into an SQLite database."""
    if df is None:
        return

    try:
        engine = create_engine(f"sqlite:///{db_name}")
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print("Data successfully loaded into the database.")
    except Exception as e:
        print(f"Failed to load data into the database: {e}")


def main():
    csv_url = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
    data = extract_data_csv(csv_url)
    transformed_data = validate_and_transform_data(data)

    if transformed_data is not None:
        load_data_to_db(transformed_data, "trainstops")
    else:
        print("Process halted due to previous errors.")


if __name__ == "__main__":
    main()
