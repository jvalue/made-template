import os
import io
import pandas as pd
import requests
import shutil
import zipfile
from sqlalchemy import create_engine, Table, Column, String, Integer, Float, MetaData



def create_temp_directory(path="project/temp_dir"):
    """Creates a temporary directory for storing extracted files."""
    os.makedirs(path, mode=0o777, exist_ok=True)
    return path


def create_database_engine(db_path="data/world_data.sqlite"):
    """Creates and returns an SQLAlchemy engine."""
    return create_engine(f"sqlite:///{db_path}")


def create_tables(metadata, year_columns):
    """Defines and returns the table structures."""
    tables = {
        "LCN": Table(
            "LCN",
            metadata,
            Column("CountryName", String),
            Column("CountryCode", String),
            Column("IndicatorName", String),
            Column("IndicatorCode", String),
            Column("SourceNote", String),
            Column("SourceOrganization", String),
            *[Column(year, Float) for year in year_columns],
        ),
        "NAC": Table(
            "NAC",
            metadata,
            Column("CountryName", String),
            Column("CountryCode", String),
            Column("IndicatorName", String),
            Column("IndicatorCode", String),
            Column("SourceNote", String),
            Column("SourceOrganization", String),
            *[Column(year, Float) for year in year_columns],
        ),
    }
    return tables


def download_and_extract_data(urls, temp_dir):
    """Downloads and extracts CSV files from the given URLs."""
    for region, url in urls.items():
        response = requests.get(url)
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            zip_ref.extractall(temp_dir)
        print(f"Downloaded and extracted data for {region}")


def load_main_and_metadata_files(temp_dir):
    """Loads main and metadata files from the temporary directory."""
    main_files = [
        f for f in os.listdir(temp_dir) if f.startswith("API") and f.endswith(".csv")
    ]
    metadata_files = [
        f
        for f in os.listdir(temp_dir)
        if f.startswith("Metadata_Indicator") and f.endswith(".csv")
    ]
    metadata_files = list(reversed(metadata_files))
    return main_files, metadata_files


def clean_and_merge_data(main_file, metadata_file, temp_dir, year_columns):
    """Cleans and merges the main data with metadata."""
    # Load main data
    main_df = pd.read_csv(
        os.path.join(temp_dir, main_file), encoding="utf-8-sig", skiprows=4
    )
    main_df.fillna(0, inplace=True)
    main_df = main_df.loc[:, ~main_df.columns.str.contains("^Unnamed")]

    # Load metadata
    metadata_df = pd.read_csv(
        os.path.join(temp_dir, metadata_file), encoding="utf-8-sig"
    )
    metadata_df = metadata_df.loc[:, ~metadata_df.columns.str.contains("^Unnamed")]
    metadata_df.rename(columns={"INDICATOR_CODE": "Indicator Code"}, inplace=True)
    metadata_df = metadata_df.drop(columns=["INDICATOR_NAME"])

    # Merge data and metadata on 'Indicator Code'
    merged_df = main_df.merge(metadata_df, on="Indicator Code", how="outer")

    # Rename columns to match the database table schema
    merged_df.rename(
        columns={
            "Country Name": "CountryName",
            "Country Code": "CountryCode",
            "Indicator Name": "IndicatorName",
            "Indicator Code": "IndicatorCode",
            "SOURCE_NOTE": "SourceNote",
            "SOURCE_ORGANIZATION": "SourceOrganization",
        },
        inplace=True,
    )

    # Rearrange columns
    merged_df = merged_df[
        [
            "CountryName",
            "CountryCode",
            "IndicatorName",
            "IndicatorCode",
            "SourceNote",
            "SourceOrganization",
            *year_columns,
        ]
    ]

    return merged_df


def save_to_database(merged_df, table_name, tables, engine):
    """Saves the merged data to the appropriate SQLite table."""
    if table_name in tables:
        merged_df.to_sql(table_name, engine, if_exists="append", index=False)
        print(f"Merged data and metadata stored in SQLite table '{table_name}'")
    else:
        print(f"Table '{table_name}' not found in the database")


def clean_up(temp_dir):
    """Removes the temporary directory."""
    shutil.rmtree(temp_dir)
    print("Cleaned up temporary directory.")


def main():
    """Main function that orchestrates the entire process."""
    urls = {
        "north_america": "https://api.worldbank.org/v2/en/country/NAC?downloadformat=csv",
        "latin_america_caribbean": "https://api.worldbank.org/v2/en/country/LCN?downloadformat=csv",
    }

    # Create the temp directory and database engine
    temp_dir = create_temp_directory()
    engine = create_database_engine()
    print("Created temporary directory and database engine.")

    # Define year columns (1960 to 2023)
    year_columns = [str(year) for year in range(1960, 2024)]

    # Create tables if they don't exist
    metadata = MetaData()
    tables = create_tables(metadata, year_columns)
    metadata.create_all(engine)

    # Download and extract data
    download_and_extract_data(urls, temp_dir)

    # Load main and metadata files
    main_files, metadata_files = load_main_and_metadata_files(temp_dir)

    # Process each file pair
    for main_file, metadata_file in zip(main_files, metadata_files):
        merged_df = clean_and_merge_data(
            main_file, metadata_file, temp_dir, year_columns
        )

        # Determine the table name based on the region
        # table_name = main_file.split("_")[1].split(".")[0].title().replace(" ", "_")
        # table_name = region.replace("_", " ").title().replace(" ", "_")
        # Determine the region and map to table name
        region = main_file.split("_")[1].split(".")[0]

        # Save the merged data to the database
        save_to_database(merged_df, region, tables, engine)

    # Clean up the temporary directory
    clean_up(temp_dir)


if __name__ == "__main__":
    main()
