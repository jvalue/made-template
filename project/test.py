import sqlite3
import pytest
import os

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

def test_is_table_present(create_dbCursor):
    create_dbCursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    all_table_list = create_dbCursor.fetchall()
    assert ('cpi_data',) in all_table_list
    assert ("temp_data",) in all_table_list
    assert ('crop_data',) in all_table_list


def test_is_pipeline_running(create_dbConnection):
    pipeline = ETL_Cpi()
    pipeline.load()
    cursor = create_dbConnection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    db_tables_count = cursor.fetchall()
    assert len(db_tables_count) > 0, ("The database does not contain any tables, hence it is not a valid SQLite "
                                      "database.")

# def extract_column_info(columns):
#     return [(name, type_) for _, name, type_, _, _, _ in columns]
#
#
# @pytest.mark.parametrize("table_name, expected_columns", [
#     # ("food_price_inflation", [
#     #     ("Open", "FLOAT"),
#     #     ("High", "FLOAT"),
#     #     ("Low", "FLOAT"),
#     #     ("Close", "FLOAT"),
#     #     ("Inflation", "FLOAT"),
#     #     ("country", "TEXT"),
#     #     ("ISO3", "TEXT"),
#     #     ("date", "TEXT"),
#     # ]),
#     ("temperature", [
#         ("Area Code", "BIGINT"),
#         ("Area Code (M49)", "TEXT"),
#         ("Area", "TEXT"),
#         ("Months Code", "BIGINT"),
#         ("Months", "TEXT"),
#         ("Element", "TEXT"),
#         ("Unit", "TEXT"),
#     ])
# ])
# def test_table_columns(create_dbCursor, table_name, expected_columns):
#     create_dbCursor.execute(f"PRAGMA table_info({table_name});")
#     columns = create_dbCursor.fetchall()
#     extracted_columns = extract_column_info(columns)
#     for column, data_type in expected_columns:
#         assert (column, data_type) in extracted_columns
#
#
# @pytest.mark.parametrize("table_name", ["temperature"  # , "food_price_inflation"
#                                         ])
# def test_table_data(create_dbCursor, table_name):
#     create_dbCursor.execute(f"SELECT COUNT(*) FROM {table_name};")
#     count = create_dbCursor.fetchone()[0]
#     assert count > 0
#
#
# @pytest.mark.parametrize("table_name, column_name, min_value, max_value", [
#     ("temperature", "Y1961", -50, 50),
#     # ("food_price_inflation", "Inflation", -100, 1000)
# ])
# def test_data_validity(create_dbCursor, table_name, column_name, min_value, max_value):
#     query = f"SELECT {column_name} FROM {table_name} WHERE {column_name} NOT BETWEEN ? AND ?;"
#     create_dbCursor.execute(query, (min_value, max_value))
#     invalid_values = create_dbCursor.fetchall()
#     assert len(invalid_values) == 0, f"Found invalid values in column {column_name} of table {table_name}"
#
#
# @pytest.mark.parametrize("table_name, year_column_prefix, start_year, end_year", [
#     ("temperature", "Y", 1961, 2020),
#     # ("food_price_inflation", "Y", 2000, 2020)
# ])
# def test_time_series_consistency(create_dbCursor, table_name, year_column_prefix, start_year, end_year):
#     for year in range(start_year, end_year + 1):
#         column_name = f"{year_column_prefix}{year}"
#         create_dbCursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} IS NULL;")
#         null_count = create_dbCursor.fetchone()[0]
#         assert null_count == 0, f"Found NULL values in column {column_name} of table {table_name}"
