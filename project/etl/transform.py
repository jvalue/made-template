import pandas as pd

def rename_year_columns(df):
    """
    Rename columns by removing 'F' from the beginning of year columns.
    Args:
        df (pd.DataFrame): DataFrame with year columns prefixed with 'F'.
    Returns:
        pd.DataFrame: DataFrame with renamed year columns, ensuring a copy is returned.
    """
    rename_dict = {col: col[1:] if col.startswith('F') else col for col in df.columns}
    return df.rename(columns=rename_dict).copy()

def simplify_indicator(df):
    """
    Simplify the 'Indicator' column by keeping only the last word of each entry.
    Args:
        df (pd.DataFrame): DataFrame with the 'Indicator' column to be simplified.
    Returns:
        pd.DataFrame: DataFrame with the simplified 'Indicator' column.
    """
    df['Indicator'] = df['Indicator'].apply(lambda x: x.split(':')[-1].strip())
    return df

def standardize_country_names(df):
    """
    Standardize country names based on a predefined mapping.
    Args:
        df (pd.DataFrame): DataFrame with the 'Country' column to be standardized.
    Returns:
        pd.DataFrame: DataFrame with standardized country names.
    """
    country_mapping = {
        "Afghanistan, Islamic Rep. of": "Afghanistan",
        "Armenia, Rep. of": "Armenia",
        "Azerbaijan, Rep. of": "Azerbaijan",
        "Bahamas, The": "Bahamas",
        "Belarus, Rep. of": "Belarus",
        "Bosnia and Herzegovina": "Bosnia & Herzegovina",
        "Cabo Verde": "Cape Verde",
        "Central African Rep.": "Central African Republic",
        "China, P.R.: Hong Kong": "Hong Kong",
        "China, P.R.: Macao": "Macao",
        "China, P.R.: Mainland": "China",
        "Congo, Dem. Rep. of the": "Democratic Republic of the Congo",
        "Congo, Rep. of": "Republic of the Congo",
        "Côte d'Ivoire": "Ivory Coast",
        "Czech Rep.": "Czech Republic",
        "Dominican Rep.": "Dominican Republic",
        "Egypt, Arab Rep. of": "Egypt",
        "Eswatini, Kingdom of": "Eswatini",
        "Ethiopia, The Federal Dem. Rep. of": "Ethiopia",
        "Fiji, Rep. of": "Fiji",
        "Gambia, The": "Gambia",
        "Iran, Islamic Rep. of": "Iran",
        "Kazakhstan, Rep. of": "Kazakhstan",
        "Korea, Dem. People's Rep. of": "North Korea",
        "Korea, Rep. of": "South Korea",
        "Kyrgyz Rep.": "Kyrgyzstan",
        "Lao People's Dem. Rep.": "Laos",
        "Macedonia, Republic of": "North Macedonia",
        "Madagascar, Rep. of": "Madagascar",
        "Micronesia, Federated States of": "Micronesia",
        "Moldova, Rep. of": "Moldova",
        "Myanmar": "Myanmar (Burma)",
        "Russian Federation": "Russia",
        "São Tomé and Príncipe, Dem. Rep. of": "São Tomé and Príncipe",
        "Serbia, Rep. of": "Serbia",
        "Slovak Rep.": "Slovakia",
        "Tanzania, United Rep. of": "Tanzania",
        "United Arab Emirates": "UAE",
        "United Kingdom": "UK",
        "United States": "USA",
        "Yemen, Rep. of": "Yemen"
    }
    
    non_existent_countries = [
        "Germany Dem Rep (former)", "Germany Fed Rep (former)",
        "Netherlands Antilles", "Soviet Union (former)"
        
    ]
    df['Country'] = df['Country'].replace(country_mapping)
    df = df[~df['Country'].isin(non_existent_countries)]
    return df

def apply_transformations(df, table_name):
    """
    Apply transformations to the DataFrame based on the table name.
    Args:
        df (pd.DataFrame): DataFrame to be transformed.
    Returns:
        pd.DataFrame: Transformed DataFrame.
    """
    column_mappings = {
        'climate_disaster_freq': ['ObjectId','Country','ISO3','Indicator','Unit','F2013','F2014','F2015','F2016','F2017','F2018','F2019','F2020','F2021'],
        'climate_inform_risk': ['ObjectId','Country','ISO3','Indicator','Unit','F2013','F2014','F2015','F2016','F2017','F2018','F2019','F2020','F2021']        
    }

    if table_name == 'climate_disaster_freq':
        df = simplify_indicator(df)
        
    if table_name in column_mappings:
        # Ensure only required columns are in the DataFrame before proceeding
        relevant_columns = [col for col in column_mappings[table_name] if col in df.columns]
        df = df[relevant_columns]
        df = rename_year_columns(df)
        df = standardize_country_names(df)

    return df
