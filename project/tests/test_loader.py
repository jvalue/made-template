import pytest
import sqlite3
import pandas as pd
from pathlib import Path
from etl_pipeline.loader import load_df_to_sqlite

@pytest.fixture
def sample_dataframe() -> pd.DataFrame:
    """
    Fixture for a sample DataFrame.

    :return: Sample DataFrame.
    :rtype: pd.DataFrame
    """
    data = {
        'Column1': [1, 2, 3],
        'Column2': ['A', 'B', 'C']
    }
    return pd.DataFrame(data)

@pytest.fixture
def temp_db_path(tmp_path) -> Path:
    """
    Fixture for a temporary SQLite database path.

    :param tmp_path: Temporary path fixture from pytest.
    :type tmp_path: Path
    :return: Path to the temporary SQLite database file.
    :rtype: Path
    """
    return tmp_path / "temp_test.db"

def test_load_df_to_sqlite(temp_db_path: Path, sample_dataframe: pd.DataFrame) -> None:
    """
    Test the load_df_to_sqlite function for loading a DataFrame into a SQLite database.

    :param temp_db_path: Path to the temporary SQLite database file.
    :type temp_db_path: Path
    :param sample_dataframe: Sample DataFrame to be loaded.
    :type sample_dataframe: pd.DataFrame
    :return: None
    """
    table_name = 'test_table'
    
    # Call the function
    load_df_to_sqlite(str(temp_db_path), table_name, sample_dataframe)
    
    # Verify the table is created and data is loaded correctly
    conn = sqlite3.connect(temp_db_path)
    df_from_db = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()

    # Check if the DataFrame loaded into the database matches the sample DataFrame
    pd.testing.assert_frame_equal(df_from_db, sample_dataframe)

    # Explicitly delete the temporary database file
    temp_db_path.unlink()

if __name__ == "__main__":
    pytest.main()
