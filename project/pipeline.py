import os
import requests
import pandas as pd
import sqlite3

def download_file(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {url}")
    else:
        print(f"Failed to download file from {url}")

def process_baumkataster(sql_doc):
    url = "https://opendata.wuerzburg.de/api/v2/catalog/datasets/baumkataster_stadt_wuerzburg/exports/csv"
    save_path = "../data/baumkataster.csv"
    download_file(url, save_path)
    
    # Load the dataset
    df = pd.read_csv(save_path, sep=';')
    
    # Print original columns
    print("\nOriginal Baumkataster Columns:", df.columns.tolist())
    
    # Strip whitespace from headers
    df.columns = [col.strip() for col in df.columns]
    
    # Rename columns to more readable names
    df.rename(columns={
        'json_featuretype': 'feature_type',
        'baumart': 'species',
        'baumart_la': 'species_latin',
        'kronenbrei': 'crown_width',
        'baumhoehe': 'height',
        'stammumfan': 'trunk_circumference',
        'baumtyp': 'tree_type',
        'source_id': 'source_id',
        'category': 'category',
        'city': 'city',
        'geo_punkt': 'geo_point'
    }, inplace=True)

    # Print renamed columns
    print("\nRenamed Baumkataster Columns:", df.columns.tolist())
    
    # Data transformation and error handling
    df.dropna(subset=['species', 'species_latin'], inplace=True)  # Drop rows with essential columns missing

    # Impute missing values with more robust methods
    for col in ['crown_width', 'trunk_circumference', 'height']:
        # Use median for numerical columns (less sensitive to outliers)
        df[col] = df[col].fillna(df[col].median())

    # Drop specified columns
    df.drop(['feature_type', 'source_id', 'category', 'city', 'geo_point'], axis=1, inplace=True)

    # Save the cleaned dataset
    df.to_csv(save_path, index=False)
    print("Baumkataster Columns:", df.columns.tolist())
    print(f"\nProcessed and saved Baumkataster data to {save_path}")

    # Save to SQLite
    conn = sqlite3.connect(sql_doc)
    df.to_sql('baumkataster', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()
    
    print("Baumkataster data saved to SQLite database.")




def process_klimabaeume(sql_doc):
    url = "https://opendata.wuerzburg.de/api/v2/catalog/datasets/sls-klimabaeume/exports/csv"
    save_path = "../data/klimabaeume.csv"
    download_file(url, save_path)
    
    # Load the dataset
    df = pd.read_csv(save_path, sep=';')
    
    # Print original columns
    print("\nOriginal Klimabaeume Columns:", df.columns.tolist())
    
    # Strip whitespace from headers
    df.columns = [col.strip() for col in df.columns]
    
    # Rename columns to more readable names
    df.rename(columns={
        'tree_number': 'tree_number',
        'species_latin': 'species_latin',
        'species_german': 'species_german',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'soil_composition': 'soil_composition',
        'vol_water_content_30': 'vol_water_content_30',
        'vol_water_content_100': 'vol_water_content_100',
        'permittivity_30': 'permittivity_30',
        'permittivity_100': 'permittivity_100',
        'conductivity_30': 'conductivity_30',
        'conductivity_100': 'conductivity_100',
        'usable_field_capacity_30': 'usable_field_capacity_30',
        'usable_field_capacity_100': 'usable_field_capacity_100',
        'temperature_30': 'temperature_30',
        'temperature_100': 'temperature_100',
        'battery_percentage': 'battery_percentage',
        'timestamp': 'timestamp',
        'koordinaten': 'coordinates'
    }, inplace=True)

    # Print renamed columns
    print("\nRenamed Klimabaeume Columns:", df.columns.tolist())

    # Data transformation and error handling
    numeric_columns = [
        'vol_water_content_30', 'vol_water_content_100', 'permittivity_30', 
        'permittivity_100', 'conductivity_30', 'conductivity_100', 
        'usable_field_capacity_30', 'usable_field_capacity_100', 
        'temperature_30', 'temperature_100', 'battery_percentage'
    ]
    
    # Convert columns to numeric, coerce errors
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Identify and handle different types of columns
    categorical_columns = [col for col in df.columns if col not in numeric_columns]
    
    # Drop rows with missing essential data (numeric columns)
    df.dropna(subset=numeric_columns, inplace=True)
    
    # Impute missing values with more robust methods
    # Use median for numerical columns (less sensitive to outliers)
    for col in numeric_columns:
        df[col] = df[col].fillna(df[col].median())
    
    # Use mode for categorical columns (most frequent value)
    for col in categorical_columns:
        df[col] = df[col].fillna(df[col].mode()[0])  # Assuming one mode

    # Drop specified columns
    df.drop(['timestamp', 'coordinates'], axis=1, inplace=True)

    # Save the cleaned dataset
    df.to_csv(save_path, index=False)
    print("Klimabaeume Columns:", df.columns.tolist())
    print(f"\nProcessed and saved Klimabaeume data to {save_path}")

    # Save to SQLite
    conn = sqlite3.connect(sql_doc)
    df.to_sql('klimabaeume', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()
    print("Klimabaeume data saved to SQLite database.")

if __name__ == "__main__":
    if not os.path.exists("../data"):
        os.makedirs("../data")
    
    sql_doc = "../data/data.db"
    
    process_baumkataster(sql_doc)
    process_klimabaeume(sql_doc)
