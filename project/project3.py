"""
The author of the dataset fatal-police-shootings-in-the-us
is KAROLINA WULLUM: https://www.kaggle.com/datasets/kwullum/fatal-police-shootings-in-the-us
Its license is CC BY-NC-SA 4.0. Website of the license: https://creativecommons.org/licenses/by-nc-sa/4.0/
This project makes some changes to the original data.

The license of the dataset california-crime is us-pd,
which is not protected by copyright,
and the public is free to copy, distribute, modify, or use the work as they wish.
"""

import os
import pandas as pd
import kagglehub
import sqlite3
import logging
import requests
from tenacity import retry, stop_after_attempt, wait_fixed

# record program running information using log
logging.basicConfig(filename='data/project3.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


# download dataset from kaggle
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def download_dataset(dataset_name):
    try:
        path = kagglehub.dataset_download(dataset_name)
        logging.info(f"Successfully download Dataset {dataset_name} to {path}")
        return path
    except Exception as e:
        logging.error(f"Failed to download dataset {dataset_name}: {e}")
        return None


# Read csv file from the directory
def read_csv(file_path, encoding):
    try:
        data = pd.read_csv(file_path, encoding=encoding)
        logging.info(f"Successfully read CSV file from {file_path}")
        return data
    except Exception as e:
        logging.error(f"Failed to read CSV file from {file_path}: {e}")
        return None


def transform_crime_enforcement_data(c_data, e_data):
    c_data = c_data.drop(columns=['Rape (legacy definition)', 'Population'])
    c_data['City'] = c_data['City'].str.rstrip('3')
    e_data.columns = e_data.columns.str.replace('\r', ' ', regex=False)  # some column names \r
    e_data.columns = e_data.columns.str.replace(r'\s+', ' ', regex=True)  # replace multiple spaces with one space
    merged_data = pd.merge(c_data, e_data, on='City', how='inner')
    merged_data = merged_data.replace(r',(?=\d)', '', regex=True)  # some numbers have comma, need to be deleted

    merged_data = merged_data.astype({
        'City': 'string',
        'Violent crime': 'int32',
        'Murder and nonnegligent manslaughter': 'int32',
        'Rape (revised definition)': 'int32',
        'Robbery': 'int32',
        'Aggravated assault': 'int32',
        'Property crime': 'int32',
        'Burglary': 'int32',
        'Larceny-theft': 'int32',
        'Motor vehicle theft': 'int32',
        'Arson': 'int32',
        'Population': 'int32',
        'Total law enforcement employees': 'int32',
        'Total officers': 'int32',
        'Total civilians': 'int32'
    })

    logging.info(f"Successfully transform crime&enforcement data")
    return merged_data


def transform_factors_data(i_data, p_data, h_data):
    i_data = i_data[i_data['Geographic Area'] == 'CA']  # only reserve data related to California
    p_data = p_data[p_data['Geographic Area'] == 'CA']
    h_data = h_data[h_data['Geographic Area'] == 'CA']
    i_data = i_data.drop(columns='Geographic Area')  # only care about cities in California, not states
    p_data = p_data.drop(columns='Geographic Area')
    h_data = h_data.drop(columns='Geographic Area')
    merged_data2 = pd.merge(i_data, p_data, on='City', how='inner')
    merged_data2 = pd.merge(merged_data2, h_data, on='City', how='inner')  # merge 3 Dataframe
    merged_data2 = merged_data2[~merged_data2['City'].str.contains('CDP', na=False)]  # delete CDP regions (not cities)
    # replace all string data with NaN, 250,000+
    merged_data2['Median Income'] = pd.to_numeric(merged_data2['Median Income'], errors='coerce')
    # replace NaN with 250000
    merged_data2['Median Income'].fillna(250000, inplace=True)

    merged_data2 = merged_data2.astype({
        'City': 'string',
        'Median Income': 'int32',
        'poverty_rate': 'float64',
        'percent_completed_hs': 'float64'
    })

    logging.info(f"Successfully transform factors data")
    return merged_data2


def load_to_db(conn, dataframe, table_name):
    try:
        dataframe.to_sql(table_name, conn, if_exists='replace', index=False)  # load dataframe to a database
        logging.info(f"Successfully loaded data to table: {table_name}")
    except Exception as e:
        logging.error(f"Failed to load data to table: {table_name}: {e}")


def main(conn=None):
    # download two different datasets from kaggle (Extract)
    crime_enforcement_path = download_dataset("fbi-us/california-crime")
    print(crime_enforcement_path)
    if not crime_enforcement_path:
        return
    factors_path = download_dataset("kwullum/fatal-police-shootings-in-the-us")
    print(factors_path)
    if not factors_path:
        return

    # Read and transform crime data (Transform)
    crime_path = os.path.join(crime_enforcement_path, 'ca_offenses_by_city.csv')
    enforcement_path = os.path.join(crime_enforcement_path, 'ca_law_enforcement_by_city.csv')
    c_data = read_csv(crime_path, 'UTF-8')
    e_data = read_csv(enforcement_path, 'UTF-8')
    if c_data is None or e_data is None:
        return
    merged_data = transform_crime_enforcement_data(c_data, e_data)

    # Read and transform social factors data
    income_path = os.path.join(factors_path, 'MedianHouseholdIncome2015.csv')
    poverty_path = os.path.join(factors_path, 'PercentagePeopleBelowPovertyLevel.csv')
    education_path = os.path.join(factors_path, 'PercentOver25CompletedHighSchool.csv')
    i_data = read_csv(income_path, 'ISO-8859-1')
    p_data = read_csv(poverty_path, 'ISO-8859-1')
    h_data = read_csv(education_path, 'ISO-8859-1')
    if i_data is None or p_data is None or h_data is None:
        return
    merged_data2 = transform_factors_data(i_data, p_data, h_data)

    # load data to the database with two different table names
    conn_by_main = False
    if conn is None:  # make sure the test program can run
        conn = sqlite3.connect('data/project3.db')
        conn_by_main = True

    try:
        load_to_db(conn, merged_data, 'crime_enforcement')
        load_to_db(conn, merged_data2, 'factors')
        conn.commit()
        logging.info("Successfully created two datasets.")
    except Exception as e:
        logging.error(f"Failed to connect to database or load changes: {e}")
    finally:
        if conn_by_main is True:
            # make sure that the system test can run successfully
            conn.close()
            logging.info("connection to database is closed.\n")
        else:
            logging.info("connection to database is not closed yet due to system test.")


if __name__ == "__main__":
    main()
