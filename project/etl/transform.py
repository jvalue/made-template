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

    return df