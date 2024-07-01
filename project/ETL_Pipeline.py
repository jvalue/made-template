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
        self.col_to_drop_in_crop_data = ['Area Code', 'Item Code', 'Element Code'] + [f'Y{i}F' for i in
                                                                                      range(1961, 2020)] + [f'Y{i}'
                                                                                                            for i
                                                                                                            in
                                                                                                            range(
                                                                                                                1961,
                                                                                                                1970)]
        self.col_to_drop_in_temp_data = ['ObjectId', '2020', '2021','Unit','Change ']
        self.dataset_kaggle_URI = "mdazizulkabirlovlu/all-countries-temperature-statistics-1970-2021"
        self.kaggle_csv_file = "all countries global temperature.csv"

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
            crop_data_urls = {
                'urls': [
                    'https://query.data.world/s/3ibkgfh656yrydhmsg4uboxxm7hysr?dws=00000',
                    'https://query.data.world/s/2x6uq5jmauvfnmfhc5ud4jv5amq4p6?dws=00000',
                    'https://query.data.world/s/nc25wfakg22iva2tmkx4icgfnufggx?dws=00000',
                    'https://query.data.world/s/fglgedqxdxc2giqvqgvbjxsqic2tuw?dws=00000',
                    'https://query.data.world/s/wva7g5yxspu3bninh4ucn7xrp4h6sc?dws=00000'
                ]
            }
            # getting required urls
            urls = crop_data_urls['urls']
            for n, url in enumerate(urls):
                try:
                    df = pd.read_csv(url, encoding='latin-1')
                    # Combine a total of 5 dataframes for the crop production dataset
                    crop_df_list.append(df)
                    logging.info(f"Successfully extracted 'Crop Production' data {n + 1} from {url}")
                except Exception as e:
                    logging.error(f"Failed to extract data from {url}: {e}")
            return crop_df_list
        except Exception as e:
            logging.error(f"An error occurred during extraction: {e}")
            raise

    # DATA SOURCE 3 ;returns: temperature_df #
    def extract_data_temp(self):
        try:
            # Obtain the dataset from Kaggle
            kaggle.api.dataset_download_files(self.dataset_kaggle_URI, path='.', unzip=True)
            csv_file_from_kaggle_name = self.kaggle_csv_file
            # Verify that the file was successfully downloaded and extracted.
            if os.path.exists(csv_file_from_kaggle_name):
                temperature_df = pd.read_csv(csv_file_from_kaggle_name)
                # Remove the csv file
                os.remove(csv_file_from_kaggle_name)
                logging.info(f"Successfully extracted 'Temperature Data' from {csv_file_from_kaggle_name}")
            else:
                raise FileNotFoundError(f"File {csv_file_from_kaggle_name} not found.")
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
        cpi_data_df = cpi_data_df.rename(columns={'Country Name': 'country_name'})
        col_to_str = ['country_name']
        cpi_data_df[col_to_str] = cpi_data_df[col_to_str].astype('string')
        columns = cpi_data_df.columns.tolist()[1:]
        cpi_data_df = pd.melt(cpi_data_df, id_vars=['country_name'], value_vars=columns, var_name='year',
                              value_name='cpi')
        return cpi_data_df

    #  Transformation --> DataSource-2: Crop Production
    def transform_data_crop(self, crop_df):
        try:
            Y_years = []
            for i in range(1970, 2020):
                Y_years.append("Y" + str(i))
            crop_dataframes = []

            for df in crop_df:
                try:
                    col_to_str = ['Area', 'Item', 'Element', 'Unit']
                    df[col_to_str] = df[col_to_str].astype('string')
                    df.drop(columns=self.col_to_drop_in_crop_data, inplace=True)
                    df[Y_years] = df[Y_years].interpolate(method='linear')
                    crop_dataframes.append(df)
                except Exception as e:
                    logging.error(f"Failed to transform 'Crop Production' data: {e}")
            concatenated_df = pd.concat(crop_dataframes, axis=0, ignore_index=True)
            crop_concatenated_df = concatenated_df.rename(columns={'Area': 'country_name'})

            # Filled missing values using forward fill
            transformed_crop_df = crop_concatenated_df.interpolate(method='ffill')

            # Staple food crops of various countries based on global continents
            transformed_crop_df = transformed_crop_df[(transformed_crop_df['Item'].isin(
                ['Yams', 'Bananas', 'Sweet potatoes', 'Maize', 'Beans, green', 'Beans, dry',
                 'Soybeans', 'Potatoes', 'Tomatoes', 'Onions, dry', 'Onions, shallots, green', 'Rice, paddy',
                 'Rice, paddy (rice milled equivalent)', 'Wheat', 'Groundnuts, with shell', 'Blueberries',
                 'Cranberries', 'Gooseberries', 'Raspberries', 'Strawberries', 'Dates', 'Plums and sloes',
                 'Millet', 'Coconuts']))].reset_index()
            # rename name of the crops
            transformed_crop_df = transformed_crop_df.replace(
                {'Beans, green': 'Green beans',
                 'Beans, dry': 'Dry beans',
                 'Onions, dry': 'Dry Onion',
                 'Onions, shallots, green': 'Green Onion',
                 'Rice, paddy': 'Rice',
                 'Rice, paddy (rice milled equivalent)': 'Rice',
                 'Groundnuts, with shell': 'Peanuts',
                 'Plums and sloes': 'Plums',
                 }
            )
            area_harvested_df = pd.DataFrame()
            yield_df = pd.DataFrame()
            production_df = pd.DataFrame()

            for i in range(len(transformed_crop_df)):
                if transformed_crop_df.iloc[i]['Element']== "Area harvested":
                    area_harvested_df = area_harvested_df._append(transformed_crop_df.iloc[i], ignore_index=True)
                elif transformed_crop_df.iloc[i]['Element']== "Yield":
                    yield_df = yield_df._append(transformed_crop_df.iloc[i], ignore_index=True)
                else:
                    production_df = production_df._append(transformed_crop_df.iloc[i], ignore_index=True)

            columns = area_harvested_df.columns.tolist()
            vars = columns[1:3]
            vals = columns[5:]
            area_harvested_df = pd.melt(area_harvested_df,id_vars=vars,value_vars=vals,var_name='Year',
                                     value_name='Area in Hectare')

            columns = yield_df.columns.tolist()
            vars = columns[1:3]
            vals = columns[5:]
            yield_df = pd.melt(yield_df,id_vars=vars,value_vars=vals,var_name='Year',
                                     value_name='Yield (hg/ha)')

            columns = production_df.columns.tolist()
            vars = columns[1:3]
            vals = columns[5:]
            production_df = pd.melt(production_df,id_vars=vars,value_vars=vals,var_name='Year',
                                     value_name='Item production in Tonnes')
            data_frame_list = [area_harvested_df, yield_df, production_df]
            return data_frame_list
        except Exception as e:
            logging.error(f"An error occurred during transformation: {e}")
            raise

    #  Transformation --> DataSource-3: All Countries Temperature Statistics 1970-2021
    def transform_data_temp(self, temperature_df):
        try:
            years = []
            for i in range(1970, 2020):
                years.append(str(i))
            # cols = temperature_df.columns.tolist()
            # print(cols)
            temperature_df.drop(columns=self.col_to_drop_in_temp_data, inplace=True)
            col_to_str1 = ['Country Name']
            temperature_df[col_to_str1] = temperature_df[col_to_str1].astype('string')
            temperature_df[years] = temperature_df[years].interpolate(method='linear')
            temperature_df = temperature_df.rename(columns={'Country Name': 'country_name'})
            columns = temperature_df.columns.tolist()[1:]
            temperature_df = pd.melt(temperature_df, id_vars=['country_name'], value_vars=columns, var_name='year',
                                     value_name='Surface Temperature Change in °C')
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
        # print(len(crop_data_df))
        # print(crop_data_df[0].shape,crop_data_df[1].shape,crop_data_df[2].shape,crop_data_df[3].shape,crop_data_df[4].shape)
        return cpi_data_df, temp_data_df, crop_data_df

    def transformation(self):
        cpi_data_df_e, temp_data_df_e, crop_data_df_e = self.extraction()
        cpi_data_df_t = cpi.transfrom_data(cpi_data_df_e)
        temp_data_df_t = cpi.transform_data_temp(temp_data_df_e)
        crop_data_df_t_list = cpi.transform_data_crop(crop_data_df_e)
        return cpi_data_df_t, temp_data_df_t, crop_data_df_t_list

    def load(self):
        cpi_data_df_t, temp_data_df_t, crop_data_df_t_list = self.transformation()
        # print(list(cpi_data_df_t.dtypes),list(temp_data_df_t.dtypes), list(crop_data_df_t.dtypes))
        self.load_data(cpi_data_df_t, '../data/made_db.db', 'cpi_data')
        self.load_data(temp_data_df_t, '../data/made_db.db', 'temp_data')
        self.load_data(crop_data_df_t_list[0], '../data/made_db.db', 'area_harvested_data')
        self.load_data(crop_data_df_t_list[1], '../data/made_db.db', 'yield_data')
        self.load_data(crop_data_df_t_list[2], '../data/made_db.db', 'production_data')
        return


cpi = ETL_Cpi()
print('Extracting...')
cpi.load()
print('COMPLETED!!!')
