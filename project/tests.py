import sqlite3
import pandas as pd

def check_table_columns(conn, table_name, expected_columns):
    query = f"PRAGMA table_info({table_name});"
    table_info = pd.read_sql_query(query, conn)
    
    actual_columns = set(table_info['name'])
    expected_columns_set = set(expected_columns)
    
    unexpected_columns = actual_columns - expected_columns_set
    missing_columns = expected_columns_set - actual_columns

    error_message = ""
    if unexpected_columns or missing_columns:
        error_message += f"Columns mismatch in '{table_name}':\n"
        if unexpected_columns:
            error_message += f"Unexpected columns: {', '.join(unexpected_columns)}.\n"
        if missing_columns:
            error_message += f"Missing columns: {', '.join(missing_columns)}.\n"

    if error_message:
        raise AssertionError(error_message)

def test_table_data(conn, table_name, primary_key_column):
    query = f"SELECT * FROM {table_name} LIMIT 5;"
    table_data = pd.read_sql_query(query, conn)

    assert not table_data.empty, f"{table_name} data is empty."
    assert primary_key_column in table_data.columns, f"{primary_key_column} column not found in {table_name} data."

def main():
    db_path = "../data/data.db"
    conn = sqlite3.connect(db_path)

    try:
        # Baumkataster Table
        baumkataster_expected_columns = [
            'species', 'species_latin', 'crown_width', 'height', 'trunk_circumference', 'tree_type'
        ]
        check_table_columns(conn, 'baumkataster', baumkataster_expected_columns)
        test_table_data(conn, 'baumkataster', 'species')  # assuming 'species' is the primary key

        # Klimabaeume Table
        klimabaeume_expected_columns = [
            'tree_number', 'species_latin', 'species_german', 'latitude', 'longitude', 
            'soil_composition', 'vol_water_content_30', 'vol_water_content_100', 
            'permittivity_30', 'permittivity_100', 'conductivity_30', 'conductivity_100', 
            'usable_field_capacity_30', 'usable_field_capacity_100', 'temperature_30', 
            'temperature_100', 'battery_percentage'
        ]
        check_table_columns(conn, 'klimabaeume', klimabaeume_expected_columns)
        test_table_data(conn, 'klimabaeume', 'tree_number')  # assuming 'tree_number' is the primary key

        print("All tests passed successfully.")
    except AssertionError as e:
        print(f"Test failed: {e}")
        raise IOError("Test failed.") from e
    finally:
        conn.close()

if __name__ == "__main__":
    main()
