import sqlite3

import pandas
import pytest
import os
import requests
# from pytest_mock import MockerFixture

from ETL_Pipeline import ETL_Cpi


@pytest.fixture
def create_dbCursor():
    conn = sqlite3.connect("../data/made_db.db")
    cursor = conn.cursor()
    yield cursor
    conn.close()


@pytest.fixture
def create_dbConnection():
    file_path = "../data/made_db.db"
    if not os.path.isfile(file_path):
        pytest.fail(f"Error: The given file path '{file_path}' does not exist.")
    try:
        conn = sqlite3.connect(file_path)
        yield conn
    finally:
        conn.close()


# test case for kaggle dataset availability
def test_is_kaggle_link_available():
    print("Checking if kaggle link is available")
    response = requests.get(
        "https://www.kaggle.com/datasets/mdazizulkabirlovlu/all-countries-temperature-statistics-1970-2021/data?select=all+countries+global+temperature.csv")
    assert response.status_code == 200


# checks for extractions
def test_data_extraction():
    print("Checking if extraction functionality is available")
    pipeline = ETL_Cpi()
    result = pipeline.extraction()
    assert isinstance(result, tuple)
    assert len(result) == 3
    assert isinstance(result[0], pandas.DataFrame)
    assert isinstance(result[1], pandas.DataFrame)
    assert isinstance(result[2], list)


# check for crop data extraction
def test_crop_data_extraction():
    print("Checking crop data extraction from FAO")
    pipeline = ETL_Cpi()
    result = pipeline.extract_data_crop_prd()
    assert isinstance(result, list)
    assert len(result) == 5


# checks for transformations
def test_data_transformation():
    print("Checking data transformation")
    pipeline = ETL_Cpi()
    result = pipeline.transformation()
    assert isinstance(result, tuple)
    assert len(result) == 3
    assert isinstance(result[0], pandas.DataFrame)
    assert isinstance(result[1], pandas.DataFrame)
    assert isinstance(result[2], pandas.DataFrame)


# test for number of items in crop database should be 23
def test_num_of_crop_categories(create_dbCursor):
    print("Performing Data Validation")
    create_dbCursor.execute("SELECT DISTINCT Item from crop_data")


# check for columns in all data frames
def test_column_names_in_data():
    print("Performing data consistency - Step1")
    pipeline = ETL_Cpi()
    result = pipeline.transformation()
    actual_columns_cpi_data = ['country_name', '1960', '1961', '1962', '1963', '1964', '1965', '1966',
                               '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975',
                               '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984',
                               '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993',
                               '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002',
                               '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2011', '2012',
                               '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021',
                               '2022']
    actual_columns_in_crop_data = ['country_name', 'Unit', 'Change ', '1970', '1971', '1972', '1973',
                                   '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982',
                                   '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991',
                                   '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000',
                                   '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                                   '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018',
                                   '2019']
    actual_columns_in_temp_data = ['index', 'country_name', 'Item', 'Element', 'Unit', 'Y1970', 'Y1971',
                                   'Y1972', 'Y1973', 'Y1974', 'Y1975', 'Y1976', 'Y1977', 'Y1978', 'Y1979',
                                   'Y1980', 'Y1981', 'Y1982', 'Y1983', 'Y1984', 'Y1985', 'Y1986', 'Y1987',
                                   'Y1988', 'Y1989', 'Y1990', 'Y1991', 'Y1992', 'Y1993', 'Y1994', 'Y1995',
                                   'Y1996', 'Y1997', 'Y1998', 'Y1999', 'Y2000', 'Y2001', 'Y2002', 'Y2003',
                                   'Y2004', 'Y2005', 'Y2006', 'Y2007', 'Y2008', 'Y2009', 'Y2010', 'Y2011',
                                   'Y2012', 'Y2013', 'Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018', 'Y2019']

    actual_column_list = [actual_columns_cpi_data, actual_columns_in_crop_data, actual_columns_in_temp_data]
    i = 0
    for df in result:
        expected_columns = result[i].columns.tolist()
        assert expected_columns == actual_column_list[i]
        i += 1


# check for data types of columns
def test_data_types_of_cpi_data():
    print("Performing data consistency - Step2")

    pipeline = ETL_Cpi()
    
    actual_data_type_cpi_data = ['string', 'float64', 'float64', 'float64', 'float64', 'float64',
     'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
     'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
     'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
     'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
     'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
     'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
     'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
     'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
     'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
     'float64', 'float64', 'float64']
    actual_data_type_crop_data = [ 'string', 'string', 'string', 'float64', 'float64', 'float64',
       'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
       'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
       'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
       'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
       'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
       'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
       'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
       'float64', 'float64', 'float64', 'float64', 'float64']
    actual_data_type_temp_data = [ 'int64', 'string', 'string', 'string', 'string', 'float64',
     'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
     'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
     'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
     'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
     'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
     'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
     'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
     'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
     'float64']

    actual_data_type = [actual_data_type_cpi_data, actual_data_type_crop_data, actual_data_type_temp_data]

    result = pipeline.transformation()
    i = 0
    for df in result:
        expected_columns\
            = list(df.dtypes)
        expected_columns = [str(i) for i in expected_columns]
        assert expected_columns == actual_data_type[i]
        i += 1


def test_is_table_cpi_present(create_dbCursor):
    print("Validating DB Availability")
    create_dbCursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    all_table_list = create_dbCursor.fetchall()
    assert ('cpi_data',) in all_table_list


def test_is_table_temp_present(create_dbCursor):
    create_dbCursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    all_table_list = create_dbCursor.fetchall()
    assert ("temp_data",) in all_table_list


def test_is_table_crop_present(create_dbCursor):
    create_dbCursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    all_table_list = create_dbCursor.fetchall()
    assert ('crop_data',) in all_table_list


def test_is_pipeline_running(create_dbConnection):
    print("Validating Pipeline Performance")
    pipeline = ETL_Cpi()
    pipeline.load()
    cursor = create_dbConnection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    db_tables_count = cursor.fetchall()
    assert len(db_tables_count) > 0, ("The database does not contain any tables, hence it is not a valid SQLite "
                                      "database.")
