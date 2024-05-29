import pandas as pd
from typing import List, Dict, Any

def delete_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Deletes specified columns from the DataFrame.
    
    :param df: DataFrame from which columns will be deleted.
    :type df: pd.DataFrame
    :param columns: List of columns to delete.
    :type columns: List[str]
    :return: DataFrame with specified columns deleted.
    :rtype: pd.DataFrame
    """
    return df.drop(columns=columns, errors='ignore')

def drop_null_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop rows with any null values.

    :param df: DataFrame from which rows will be dropped.
    :type df: pd.DataFrame
    :return: DataFrame with rows containing null values dropped.
    :rtype: pd.DataFrame
    """
    return df.dropna()

def fill_missing_values(df: pd.DataFrame, fill_value: Any = None, method: str = "None") -> pd.DataFrame:
    """
    Fill missing values with a specified value or method.

    :param df: DataFrame in which missing values will be filled.
    :type df: pd.DataFrame
    :param fill_value: Value to fill missing values with. Default is None.
    :type fill_value: Any, optional
    :param method: Method to use for filling missing values ('ffill', 'bfill', etc.). Default is None.
    :type method: str, optional
    :return: DataFrame with missing values filled.
    :rtype: pd.DataFrame
    """
    if fill_value is not None:
        return df.fillna(fill_value)
    if method is not None:
        return df.fillna(method=method)
    return df

def rename_columns(df: pd.DataFrame, columns_mapping: Dict[str, str]) -> pd.DataFrame:
    """
    Rename columns based on a provided mapping.

    :param df: DataFrame in which columns will be renamed.
    :type df: pd.DataFrame
    :param columns_mapping: Dictionary mapping old column names to new column names.
    :type columns_mapping: Dict[str, str]
    :return: DataFrame with renamed columns.
    :rtype: pd.DataFrame
    """
    return df.rename(columns=columns_mapping)

def filter_rows(df: pd.DataFrame, condition: Any) -> pd.DataFrame:
    """
    Filter rows based on a condition.

    :param df: DataFrame from which rows will be filtered.
    :type df: pd.DataFrame
    :param condition: Condition to filter rows by.
    :type condition: Any
    :return: DataFrame with filtered rows.
    :rtype: pd.DataFrame
    """
    return df.query(condition)

def add_new_column(df: pd.DataFrame, column_name: str, values: Any) -> pd.DataFrame:
    """
    Add a new column with specified values.

    :param df: DataFrame to which the new column will be added.
    :type df: pd.DataFrame
    :param column_name: Name of the new column.
    :type column_name: str
    :param values: Values for the new column.
    :type values: Any
    :return: DataFrame with the new column added.
    :rtype: pd.DataFrame
    """
    df[column_name] = values
    return df

def change_column_type(df: pd.DataFrame, column_name: str, new_type: Any) -> pd.DataFrame:
    """
    Change the data type of a specified column.

    :param df: DataFrame in which the column type will be changed.
    :type df: pd.DataFrame
    :param column_name: Name of the column to change the type of.
    :type column_name: str
    :param new_type: New data type for the column.
    :type new_type: Any
    :return: DataFrame with the column type changed.
    :rtype: pd.DataFrame
    """
    df[column_name] = df[column_name].astype(new_type)
    return df


def standardize_date_column(df: pd.DataFrame, date_column: str) -> pd.DataFrame:
    """
    Standardize the date column to a uniform date format.

    :param df: DataFrame containing the date column.
    :type df: pd.DataFrame
    :param date_column: Name of the date column to standardize.
    :type date_column: str
    :return: DataFrame with the standardized date column.
    :rtype: pd.DataFrame
    """
    # Handle specific known date formats
    if df[date_column].str.contains('M').any():
        df[date_column] = pd.to_datetime(df[date_column], format='%YM%m', errors='coerce')
    elif df[date_column].str.contains(r'\d{1,2}/\d{1,2}/\d{4}').any():
        # Handle date format like D12/17/1992
        df[date_column] = pd.to_datetime(df[date_column].str.extract(r'(\d{1,2}/\d{1,2}/\d{4})')[0], format='%m/%d/%Y', errors='coerce')
    else:
        df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
    return df

def rename_year_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename columns with the prefix 'F' followed by a four-digit year (FYYYY) to just the year (YYYY).

    :param df: DataFrame with columns to be renamed.
    :type df: pd.DataFrame
    :return: DataFrame with renamed columns.
    :rtype: pd.DataFrame
    """
    new_columns = {col: col[1:] for col in df.columns if col.startswith('F') and col[1:].isdigit() and len(col) == 5}
    df.rename(columns=new_columns, inplace=True)
    return df

