import pandas as pd
from pathlib import Path
from etl_pipeline.extractor import extract_csv
from etl_pipeline.transform import delete_columns, standardize_date_column, rename_year_columns
from etl_pipeline.loader import load_df_to_sqlite

def main():
    db_name = Path("./data/climate_data_final.db")

    datasources = {
        "Annual_Surface_Temperature_Change": {
            "url": "https://opendata.arcgis.com/datasets/4063314923d74187be9596f10d034914_0.csv",
            "columns_to_delete": [
                'ObjectId', 'ISO2', 'ISO3', 'Indicator', 'Unit', 'Source', 'CTS_Code', 'CTS_Name', 'CTS_Full_Descriptor',
                'F1961', 'F1962', 'F1963', 'F1964', 'F1965', 'F1966', 'F1967', 'F1968', 'F1969', 'F1970',
                'F1971', 'F1972', 'F1973', 'F1974', 'F1975', 'F1976', 'F1977', 'F1978', 'F1979', 'F1980',
                'F1981', 'F1982', 'F1983', 'F1984', 'F1985', 'F1986', 'F1987', 'F1988', 'F1989', 'F1990',
                'F1991', 'F2021', 'F2022'
            ],
            "rename_year_columns": True  
        },
        "World_Monthly_CO2_Concentrations": {
            "url": "https://opendata.arcgis.com/datasets/9c3764c0efcc4c71934ab3988f219e0e_0.csv",
            "columns_to_delete": ['ObjectId', 'ISO2', 'ISO3', 'Indicator', 'Source', 'CTS_Code', 'CTS_Name', 'CTS_Full_Descriptor'],
            "date_column": "Date"
        },
        "Change_in_Mean_Sea_Levels": {
            "url": "https://opendata.arcgis.com/datasets/b84a7e25159b4c65ba62d3f82c605855_0.csv",
            "columns_to_delete": ['ObjectId', 'ISO2', 'ISO3', 'Indicator', 'Unit', 'Source', 'CTS_Code', 'CTS_Name', 'CTS_Full_Descriptor'],
            "date_column": "Date"
        },
        "Land_Cover_Alteration": {
            "url": "https://opendata.arcgis.com/datasets/b1e6c0ea281f47b285addae0cbb28f4b_0.csv",
            "columns_to_delete": ['ObjectId', 'ISO2', 'ISO3', 'Source', 'CTS_Code', 'CTS_Name', 'CTS_Full_Descriptor'],
            "rename_year_columns": True  
        }
    }

    for table_name, config in datasources.items():
        # Step 1: Extract
        df = extract_csv(config["url"])

        # Step 2: Transform - Delete columns
        df_transformed = delete_columns(df, config["columns_to_delete"])

        # Step 3: Transform - Standardize date column if specified
        if "date_column" in config:
            df_transformed = standardize_date_column(df_transformed, config["date_column"])

        # Step 4: Transform - Rename year columns if specified
        if "rename_year_columns" in config and config["rename_year_columns"]:
            df_transformed = rename_year_columns(df_transformed)

        # Step 5: Load
        load_df_to_sqlite(db_name, table_name, df_transformed)

    print("Data processing completed and loaded into the database.")

if __name__ == "__main__":
    main()
