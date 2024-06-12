import sqlite3
import logging

import kaggle
import requests, zipfile, io
import pandas as pd
import os, glob


class ETL_Cpi:
    def __init__(self):
        self.url = 'https://api.worldbank.org/v2/en/indicator/FP.CPI.TOTL?downloadformat=csv'
        self.base_dir = '../data/'
        self.urls = [
            'https://query.data.world/s/3ibkgfh656yrydhmsg4uboxxm7hysr?dws=00000',
            'https://query.data.world/s/2x6uq5jmauvfnmfhc5ud4jv5amq4p6?dws=00000',
            'https://query.data.world/s/nc25wfakg22iva2tmkx4icgfnufggx?dws=00000',
            'https://query.data.world/s/fglgedqxdxc2giqvqgvbjxsqic2tuw?dws=00000',
            'https://query.data.world/s/wva7g5yxspu3bninh4ucn7xrp4h6sc?dws=00000'
        ]
        self.col_to_str = ['Area', 'Item', 'Element', 'Unit']
        self.col_to_str1 = ['Country Name', 'Change ', 'Unit']
        self.col_to_drop = ['Area Code', 'Item Code', 'Element Code'] + [f'Y{i}F' for i in range(1961, 2020)] + [f'Y{i}'
                                                                                                                 for i
                                                                                                                 in
                                                                                                                 range(
                                                                                                                     1961,
                                                                                                                     1970)]
        self.col_to_drop1 = ['ObjectId', '2020', '2021']
        self.dataset_kaggle = "mdazizulkabirlovlu/all-countries-temperature-statistics-1970-2021"
        self.csv_file_name = "all countries global temperature.csv"

    # DATA SOURCE 1 ;return: cpi_data_df #
    def extract_data(self):
        try:

            r = requests.get(self.url)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall(self.base_dir)
            files_to_be_deleted_pattern = "Metadata_*.csv"

            for f in glob.glob(self.base_dir + files_to_be_deleted_pattern):
                os.remove(f)

            files_to_be_stored_pattern = 'API_FP.CPI.TOTL_DS2_en_csv*.csv'
            logging.info(f"Successfully extracted 'CPI' data")
            for f in glob.glob(self.base_dir + files_to_be_stored_pattern):
                cpi_data_df = pd.read_csv(f, skiprows=[0, 1, 2, 3])  # on_bad_lines='skip'
                os.remove(f)
                return cpi_data_df
        except Exception as e:
            logging.error(f"An error occurred during extraction: {e}")
            raise

    # DATA SOURCE 2 ;returns: crop_df #
    def extract_data_crop_prd(self):
        try:
            crop_df_list = []
            for n, url in enumerate(self.urls):
                try:
                    df = pd.read_csv(url, encoding='latin-1')
                    # append 5 dataframes in total for crop production dataset
                    crop_df_list.append(df)
                    logging.info(f"Successfully extracted 'Crop Production' data {n + 1} from {url}")
                    return crop_df_list
                except Exception as e:
                    logging.error(f"Failed to extract data from {url}: {e}")
        except Exception as e:
            logging.error(f"An error occurred during extraction: {e}")
            raise

    # DATA SOURCE 3 ;returns: temperature_df####################
    def extract_data_temp(self):
        try:
            # Download the dataset from Kaggle
            kaggle.api.dataset_download_files(self.dataset_kaggle, path='.', unzip=True)

            # Check if the file was downloaded and extracted correctly
            if os.path.exists(self.csv_file_name):
                temperature_df = pd.read_csv(self.csv_file_name)
                # Remove the csv file
                os.remove(self.csv_file_name)
                logging.info(f"Successfully extracted 'Temperature Data' from {self.csv_file_name}")
            else:
                raise FileNotFoundError(f"File {self.csv_file_name} not found.")
            return temperature_df
        except Exception as e:
            logging.error(f"An error occurred during extraction: {e}")
            raise

    # Transformation --> DataSource-1: Consumer Price Inflation
    def transfrom_data(self, cpi_data_df):
        # print(cpi_data_df)
        columns_to_drop = ['Country Code', 'Indicator Name', 'Indicator Code', '2023', '2010', 'Unnamed: 68']
        cpi_data_df.drop(columns_to_drop, axis=1, inplace=True)
        cpi_data_df = self.remove_rows_with_all_null(cpi_data_df)
        cpi_data_df = cpi_data_df.interpolate(method='linear')
        cpi_data_df = self.remove_uniterpolated_countries_data(cpi_data_df)
        cpi_data_df = self.impute_values_for_UAE(cpi_data_df)
        return cpi_data_df

    #  Transformation --> DataSource-2: Crop Production

    def transform_data_crop(self, crop_df):
        try:
            Y_years = ["Y" + str(i) for i in range(1970, 2020)]
            crop_dataframes = []

            for df in crop_df:
                try:
                    # Convert specified columns to string type
                    df[self.col_to_str] = df[self.col_to_str].astype('string')
                    # Drop unnecessary columns
                    df.drop(columns=self.col_to_drop, inplace=True)
                    # linear interpolate columns with numeric missing values
                    df[Y_years] = df[Y_years].interpolate(method='linear')
                    crop_dataframes.append(df)
                except Exception as e:
                    logging.error(f"Failed to transform 'Crop Production' data: {e}")

            concatenated_df = pd.concat(crop_dataframes, axis=0, ignore_index=True)
            crop_concatenated_df = concatenated_df.rename(columns={'Area': 'Country Name'})

            # Forward filling with remaining missing values
            transformed_crop_df = crop_concatenated_df.interpolate(method='ffill')
            # Filtered crops of interest
            transformed_crop_df = transformed_crop_df[(transformed_crop_df['Item'].isin(
                ['Maize', 'Wheat', 'Rice, paddy', 'Sugar cane', 'Potatoes', 'Coconuts', 'Grapes',
                 'Dates']))].reset_index()

            return transformed_crop_df

        except Exception as e:
            logging.error(f"An error occurred during transformation: {e}")
            raise

    #  Transformation --> DataSource-3: All Countries Temperature Statistics 1970-2021
    def transform_data_temp(self, temperature_df):
        try:
            # list of years
            years = [str(i) for i in range(1970, 2020)]
            # Drop unnecessary columns from temperature_df
            temperature_df.drop(columns=self.col_to_drop1, inplace=True)
            # Convert specified columns to string type
            temperature_df[self.col_to_str1] = temperature_df[self.col_to_str1].astype('string')
            # linear interpolate columns with numeric missing values
            temperature_df[years] = temperature_df[years].interpolate(method='linear')
            return temperature_df

        except Exception as e:
            logging.error(f"An error occurred during transformation: {e}")
            raise

    def load_data(self, df, db_name, table_name):
        try:
            # Connect to SQLite database
            conn = sqlite3.connect(db_name)
            # Store the dataframe in the specified table
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            logging.info(f"Loading completed, data saved to database '{db_name}' in table '{table_name}'.")
        except Exception as e:
            logging.error(f"An error occurred during loading: {e}")
            raise
        finally:
            # Close the connection
            conn.close()
        # return db_name, table_name

    def remove_rows_with_all_null(self, df):
        list_of_all_null_countries = []
        country_null_value_count = {}

        for i in range(len(df)):
            country_null_value_count[df.iloc[i]['Country Name']] = df.iloc[i].isna().sum()
            if df.iloc[i].isna().sum() == 62:
                list_of_all_null_countries.append(i)
        df_refined = df.drop(list_of_all_null_countries)
        return df_refined

    def remove_uniterpolated_countries_data(self, df):
        list_of_uniterpolated_countries = ['Antigua and Barbuda', 'Armenia', 'Albania', 'Angola', 'Afghanistan',
                                           'Aruba']
        for i in list_of_uniterpolated_countries:
            df = df.drop(df[df['Country Name'] == i].index)
        return df

    def impute_values_for_UAE(self, df):
        mean_for_UAE = []
        for i in range(1984, 2023):
            if i == 2010:
                pass
            else:
                mean_for_UAE.append(df[str(i)].mean())
        mean_for_UAE.append(df['1980'].mean())

        cpi_values_of_UAE = df.iloc[0][25:].tolist()  # only available from 1984(1980 also)
        cpi_values_of_UAE.append(29.374970967037186)  # value for 1980

        perc_share_of_UAE_in_world_cpi_for_avail_data = []
        for i in range(len(cpi_values_of_UAE)):
            perc_share_of_UAE_in_world_cpi_for_avail_data.append(cpi_values_of_UAE[i] / mean_for_UAE[i])

        # interpolation for UAE for the yaers where data is not available
        # for the years where data is unavailable for UAE we can impute the data by
        # mean(all available countries CPI for that year)*0.9581559454843503
        imputation_value_constant_for_UAE = sum(perc_share_of_UAE_in_world_cpi_for_avail_data) / (
            len(perc_share_of_UAE_in_world_cpi_for_avail_data))

        for i in range(1960, 1985):
            if i == 1980:
                continue
            else:
                df.iloc[0, i - 1960 + 1] = imputation_value_constant_for_UAE * df[str(i)].mean()

        return df

    def extraction(self):
        cpi_data_df = self.extract_data()
        temp_data_df = self.extract_data_temp()
        crop_data_df = self.extract_data_crop_prd()
        return cpi_data_df, temp_data_df, crop_data_df

    def transformation(self):
        cpi_data_df_e, temp_data_df_e, crop_data_df_e = self.extraction()
        cpi_data_df_t = cpi.transfrom_data(cpi_data_df_e)
        temp_data_df_t = cpi.transform_data_temp(temp_data_df_e)
        crop_data_df_t = cpi.transform_data_crop(crop_data_df_e)
        return cpi_data_df_t, temp_data_df_t, crop_data_df_t

    def load(self):
        cpi_data_df_t, temp_data_df_t, crop_data_df_t = self.transformation()
        self.load_data(cpi_data_df_t, '../data/made_db.db', 'cpi_data')
        self.load_data(temp_data_df_t, '../data/made_db.db', 'temp_data')
        self.load_data(crop_data_df_t, '../data/made_db.db', 'crop_data')
        return


cpi = ETL_Cpi()
print('Extracting...')
cpi.load()
print('COMPLETED!!!')
