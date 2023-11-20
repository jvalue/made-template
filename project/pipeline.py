import pandas as pd
from sqlalchemy import create_engine


# preprocess the data after fetching via url
def process_and_load_data(url, table, column_map, col_to_drop):
    try:
        # Extract and Transform in one step
        df = pd.read_html(url)[0][:-1]
        df.rename(columns=column_map, inplace=True)
        df.drop(columns=col_to_drop, inplace=True)
        # Database Engine
        engine = create_engine("sqlite:///../data/unemployed.sqlite")
        # Load to SQLite
        df.to_sql(table, engine, if_exists="replace")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    # Common Column Map and Columns to Drop
    column_map = {'Year, month': 'year', 'Year, month.1': 'month',
                  'Total': 'total', 'Male': 'male', 'Female': 'female',
                  'Juveniles of under 20 years of age': 'under_20_year_age',
                  'Long-term unemployed': 'long_term'}
    col_to_drop = ["total", "under_20_year_age", "long_term"]

    # URLs
    west_unemployed = "https://www.destatis.de/EN/Themes/Economy/Short-Term-Indicators/Labour-Market/arb120.html#241586"
    east_unemployed = "https://www.destatis.de/EN/Themes/Economy/Short-Term-Indicators/Labour-Market/arb130.html#241598"

    # Process and Load Data
    process_and_load_data(
        west_unemployed, "unemployed_west", column_map, col_to_drop)
    process_and_load_data(
        east_unemployed, "unemployed_east", column_map, col_to_drop)


if __name__ == "__main__":
    main()
