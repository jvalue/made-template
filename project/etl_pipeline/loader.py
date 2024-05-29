import sqlite3
import pandas as pd


def load_df_to_sqlite(db_name: str, table_name: str, df: pd.DataFrame) -> None:
    """
    Loads a DataFrame into a SQLite database table.

    If the table already exists in the database, it will be replaced.

    :param db_name: Name of the SQLite database file.
    :type db_name: str
    :param table_name: Name of the table to be created/updated in the database.
    :type table_name: str
    :param df: DataFrame to be loaded into the database.
    :type df: pd.DataFrame
    :return: None
    """
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
