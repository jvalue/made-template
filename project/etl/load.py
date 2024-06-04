import sqlite3
from sqlite3 import DatabaseError

def store_data(df, db_path, table_name):
    """
    Store data into a SQLite table in the specified database.
    Args:
        df (pd.DataFrame): DataFrame to store in the database.
        db_path (str): Path to the SQLite database file.
        table_name (str): Name of the table to store data in.
    """
    try:
        with sqlite3.connect(db_path) as conn:
            df.to_sql(table_name, conn, if_exists='replace', index=False)
    except DatabaseError as e:
        return e
        