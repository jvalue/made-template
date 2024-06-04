import pytest
import pandas as pd
import sqlite3
from etl.load import store_data
import os

def test_store_data_successful(tmp_path):
    """Test storing data successfully into an SQLite database."""
    db_path = tmp_path / "test.db"
    table_name = "test_table"
    data = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data)

    # Store data
    result = store_data(df, str(db_path), table_name)
    
    # Check that there were no errors
    assert result is None, "Expected no errors when storing data successfully."

    # Connect to the database to verify contents
    conn = sqlite3.connect(str(db_path))
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()

    # Check if data is correctly inserted
    assert len(rows) == 2
    assert rows[0] == (1, 3)
    assert rows[1] == (2, 4)

    conn.close()

def test_store_data_with_database_error(tmp_path):
    """Test the function's error handling when an invalid path is used."""
    # Create a nested invalid file path
    db_path = tmp_path / "nonexistent_directory" / "invalid.db"
    table_name = "test_table"
    data = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data)

    # Expect failure due to invalid file path (non-existent directory)
    result = store_data(df, str(db_path), table_name)

    # Check that an OperationalError was raised
    assert isinstance(result, sqlite3.OperationalError), "Expected sqlite3.OperationalError due to invalid file path."

# Optional: Additional tests for different edge cases
