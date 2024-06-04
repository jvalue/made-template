from etl.extract import fetch_data
from etl.load import store_data
from etl.transform import apply_transformations

def main():
    db_path = './data/climate.db'
    sources = {
        "https://opendata.arcgis.com/datasets/b13b69ee0dde43a99c811f592af4e821_0.csv": "climate_disaster_freq",
        "https://opendata.arcgis.com/datasets/7cae02f84ed547fbbd6210d90da19879_0.csv": "climate_inform_risk"
    }

    for url, table_name in sources.items():
        df = fetch_data(url)
        if not df.empty:  # Proceed only if DataFrame is not emspty
            df_transformed = apply_transformations(df,table_name)
            store_data(df_transformed, db_path, table_name)

if __name__ == "__main__":
    main()