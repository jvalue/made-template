import pytest
import pandas as pd
from etl_pipeline.transform import (
    delete_columns,
    drop_null_rows,
    fill_missing_values,
    rename_columns,
    filter_rows,
    add_new_column,
    change_column_type,
    standardize_date_column,
    rename_year_columns,
)


@pytest.fixture
def sample_dataframe() -> pd.DataFrame:
    """
    Fixture for a sample DataFrame.

    :return: Sample DataFrame.
    :rtype: pd.DataFrame
    """
    data = {
        "Column1": [1, 2, 3, None],
        "Column2": ["A", "B", None, "D"],
        "Column3": [4.5, None, 6.5, 7.5],
    }
    return pd.DataFrame(data)


@pytest.fixture
def sample_ym_date_dataframe() -> pd.DataFrame:
    """
    Fixture for a sample DataFrame with YYYYMM date columns.

    :return: Sample DataFrame.
    :rtype: pd.DataFrame
    """
    data = {
        "Date": ["1958M01", "1958M02", "1958M03", "1958M04"],
        "Value": [1.1, 2.2, 3.3, 4.4],
    }
    return pd.DataFrame(data)


@pytest.fixture
def sample_md_date_dataframe() -> pd.DataFrame:
    """
    Fixture for a sample DataFrame with DMM/DD/YYYY date columns.

    :return: Sample DataFrame.
    :rtype: pd.DataFrame
    """
    data = {
        "Date": ["D12/17/1992", "D01/01/1993", "D02/28/1993", "D03/15/1993"],
        "Value": [1.1, 2.2, 3.3, 4.4],
    }
    return pd.DataFrame(data)


@pytest.fixture
def sample_fyear_dataframe() -> pd.DataFrame:
    """
    Fixture for a sample DataFrame with FYYYY columns.

    :return: Sample DataFrame.
    :rtype: pd.DataFrame
    """
    data = {
        "F1992": [0.1, 0.2, 0.3],
        "F1993": [0.4, 0.5, 0.6],
        "F1994": [0.7, 0.8, 0.9],
        "OtherColumn": ["A", "B", "C"],
    }
    return pd.DataFrame(data)


def test_delete_columns(sample_dataframe: pd.DataFrame) -> None:
    """
    Test the delete_columns function for deleting specified columns from a DataFrame.

    :param sample_dataframe: Sample DataFrame for testing.
    :type sample_dataframe: pd.DataFrame
    :return: None
    """
    columns_to_delete = [
        "Column2",
        "Column4",
    ]  # Column4 does not exist, should be ignored
    df_transformed = delete_columns(sample_dataframe, columns_to_delete)
    expected_df = sample_dataframe.drop(columns=["Column2"], errors="ignore")
    pd.testing.assert_frame_equal(df_transformed, expected_df)


def test_drop_null_rows(sample_dataframe: pd.DataFrame) -> None:
    """
    Test the drop_null_rows function for dropping rows with any null values.

    :param sample_dataframe: Sample DataFrame for testing.
    :type sample_dataframe: pd.DataFrame
    :return: None
    """
    df_transformed = drop_null_rows(sample_dataframe)
    expected_df = sample_dataframe.dropna()
    pd.testing.assert_frame_equal(df_transformed, expected_df)


def test_fill_missing_values(sample_dataframe: pd.DataFrame) -> None:
    """
    Test the fill_missing_values function
    for filling missing values with a specified value.

    :param sample_dataframe: Sample DataFrame for testing.
    :type sample_dataframe: pd.DataFrame
    :return: None
    """
    fill_value = 0
    df_transformed = fill_missing_values(sample_dataframe, fill_value=fill_value)
    expected_df = sample_dataframe.fillna(fill_value)
    pd.testing.assert_frame_equal(df_transformed, expected_df)


def test_rename_columns(sample_dataframe: pd.DataFrame) -> None:
    """
    Test the rename_columns function for renaming columns based on a provided mapping.

    :param sample_dataframe: Sample DataFrame for testing.
    :type sample_dataframe: pd.DataFrame
    :return: None
    """
    columns_mapping = {"Column1": "NewColumn1", "Column2": "NewColumn2"}
    df_transformed = rename_columns(sample_dataframe, columns_mapping)
    expected_df = sample_dataframe.rename(columns=columns_mapping)
    pd.testing.assert_frame_equal(df_transformed, expected_df)


def test_filter_rows(sample_dataframe: pd.DataFrame) -> None:
    """
    Test the filter_rows function for filtering rows based on a condition.

    :param sample_dataframe: Sample DataFrame for testing.
    :type sample_dataframe: pd.DataFrame
    :return: None
    """
    condition = "Column1 > 1"
    df_transformed = filter_rows(sample_dataframe, condition)
    expected_df = sample_dataframe.query(condition)
    pd.testing.assert_frame_equal(df_transformed, expected_df)


def test_add_new_column(sample_dataframe: pd.DataFrame) -> None:
    """
    Test the add_new_column function for adding a new column with specified values.

    :param sample_dataframe: Sample DataFrame for testing.
    :type sample_dataframe: pd.DataFrame
    :return: None
    """
    new_column_name = "NewColumn"
    values = [10, 20, 30, 40]
    df_transformed = add_new_column(sample_dataframe, new_column_name, values)
    expected_df = sample_dataframe.copy()
    expected_df[new_column_name] = values
    pd.testing.assert_frame_equal(df_transformed, expected_df)


def test_change_column_type(sample_dataframe: pd.DataFrame) -> None:
    """
    Test the change_column_type function
    for changing the data type of a specified column.

    :param sample_dataframe: Sample DataFrame for testing.
    :type sample_dataframe: pd.DataFrame
    :return: None
    """
    column_name = "Column1"
    new_type = "str"
    df_transformed = change_column_type(sample_dataframe, column_name, new_type)
    expected_df = sample_dataframe.copy()
    expected_df[column_name] = expected_df[column_name].astype(new_type)
    pd.testing.assert_frame_equal(df_transformed, expected_df)


def test_standardize_ym_date_column(sample_ym_date_dataframe: pd.DataFrame) -> None:
    """
    Test the standardize_date_column
    function for handling YYYYMM date format.

    :param sample_ym_date_dataframe: Sample DataFrame with
        YYYYMM date columns for testing.
    :type sample_ym_date_dataframe: pd.DataFrame
    :return: None
    """
    # Expected DataFrame after date standardization
    expected_data = {
        "Date": pd.to_datetime(
            ["1958-01-01", "1958-02-01", "1958-03-01", "1958-04-01"]
        ),
        "Value": [1.1, 2.2, 3.3, 4.4],
    }
    expected_df = pd.DataFrame(expected_data)

    # Standardize date column
    df_transformed = standardize_date_column(sample_ym_date_dataframe, "Date")

    # Check if the DataFrame matches the expected result
    pd.testing.assert_frame_equal(df_transformed, expected_df)


def test_standardize_md_date_column(sample_md_date_dataframe: pd.DataFrame) -> None:
    """
    Test the standardize_date_column
    function for handling DMM/DD/YYYY date format.

    :param sample_md_date_dataframe: Sample DataFrame
        with DMM/DD/YYYY date columns for testing.
    :type sample_md_date_dataframe: pd.DataFrame
    :return: None
    """
    # Expected DataFrame after date standardization
    expected_data = {
        "Date": pd.to_datetime(
            ["1992-12-17", "1993-01-01", "1993-02-28", "1993-03-15"]
        ),
        "Value": [1.1, 2.2, 3.3, 4.4],
    }
    expected_df = pd.DataFrame(expected_data)

    # Standardize date column
    df_transformed = standardize_date_column(sample_md_date_dataframe, "Date")

    # Check if the DataFrame matches the expected result
    pd.testing.assert_frame_equal(df_transformed, expected_df)


def test_rename_year_columns(sample_fyear_dataframe: pd.DataFrame) -> None:
    """
    Test the rename_year_columns function for renaming FYYYY columns.

    :param sample_fyear_dataframe: Sample DataFrame with FYYYY columns for testing.
    :type sample_fyear_dataframe: pd.DataFrame
    :return: None
    """
    # Expected DataFrame after renaming year columns
    expected_data = {
        "1992": [0.1, 0.2, 0.3],
        "1993": [0.4, 0.5, 0.6],
        "1994": [0.7, 0.8, 0.9],
        "OtherColumn": ["A", "B", "C"],
    }
    expected_df = pd.DataFrame(expected_data)

    # Rename year columns
    df_transformed = rename_year_columns(sample_fyear_dataframe)

    # Check if the DataFrame matches the expected result
    pd.testing.assert_frame_equal(df_transformed, expected_df)
