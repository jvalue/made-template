

import pandas as pd
import sqlite3
import os


def read_csv(file_path):
    return pd.read_csv(file_path,delimiter=';', error_bad_lines=False)
 

def create_sqlite_connection(database_name):
    conn = sqlite3.connect(database_name)
    return conn, conn.cursor()

def close_sqlite_connection(conn):
    conn.commit()
    conn.close()

def create_table(cursor, table_name, column_types):
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        {', '.join([f'{col} {col_type}' for col, col_type in column_types.items()])}
    );
    """
    cursor.execute(create_table_query)

def write_to_sqlite(df, conn, table_name):
    df.to_sql(table_name, conn, if_exists='replace', index=False)

def main(csv_file_path, database_name, table_name, column_types):
    # Read CSV file
    df = read_csv(csv_file_path)

    # Create SQLite connection and cursor
    conn, cursor = create_sqlite_connection(database_name)

    # Create a table with the specified column types
    create_table(cursor, table_name, column_types)

    # Write data from the DataFrame to the SQLite table
    write_to_sqlite(df, conn, table_name)

    # Close the connection
    close_sqlite_connection(conn)

    print(f"Data has been successfully written to {database_name}.{table_name}")

if __name__ == "__main__":
    # Customize these parameters based on your dataset and preferences
    #REAL , TEXT, text, text, text, text, real, real, real, real,text, text, real

    csv_file_path = 'https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv'
    database_name = 'airports.sqlite'
    #
    table_name = 'airports'
    column_types = {
        'column_1': 'REAL',
        'column_2': 'TEXT',
        'column_3': 'TEXT',
        'column_4': 'TEXT',
        'ccolumn_5': 'TEXT',
        'column_6': 'TEXT',
        'column_7': 'REAL',
        'column_8': 'REAL',
        'column_9': 'REAL',
        'column_10': 'REAL',
        'column_11': 'TEXT',
        'column_12': 'TEXT',
         'geo_punkt': 'TEXT',
        # Add more columns as needed
    }
    current_directory = os.getcwd()
    database_path = os.path.join(current_directory, 'airports.sqlite')

    print(f"The SQLite database is located at: {database_path}")

    main(csv_file_path, database_name, table_name, column_types)

