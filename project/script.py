import pandas as pd
import numpy as np
from sqlalchemy import create_engine

####################################################
# 1st dataset: Healthy life years at birth
def extract_hly():
    url = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/tps00150/?format=SDMX-CSV&lang=en&label=label_only'
    df1 = pd.read_csv(url, sep=',')
    
    return df1


def transform_hly(df1):
    # exclude gender data, as I do not use it in my analysis
    df1 = df1[~df1['sex'].isin(['Females', 'Males'])].copy()

    # drop unnecessary columns
    df1.drop(columns=['DATAFLOW','LAST UPDATE', 'freq', 'unit', 'indic_he', 'OBS_FLAG', 'sex'], inplace=True)
  
    # add new empty entries for Iceland, as there are missing values for 2019-2022
    if not df1[(df1['geo'] == 'Iceland') & (df1['TIME_PERIOD'] >= 2019)].any().any():
        missing_rows = pd.DataFrame({
            'geo': ['Iceland']*4,
            'TIME_PERIOD': [2019, 2020, 2021, 2022],
            'OBS_VALUE': [None]*4
        })
        df1 = pd.concat([df1, missing_rows])
        
    # interpolate missing values in the dataset
    df1['TIME_PERIOD'] = pd.to_numeric(df1['TIME_PERIOD'])
    df1.sort_values(by=['geo', 'TIME_PERIOD'], inplace=True)
    df1['OBS_VALUE'] = df1.groupby('geo')['OBS_VALUE'].apply(lambda x: x.interpolate())
    df1['OBS_VALUE'] = df1.groupby('geo')['OBS_VALUE'].ffill().bfill()
           
    return df1


def load_hly(df1, path):
    # specify the directory where to load the dataset
    engine_hly = create_engine(f'sqlite:///{path}')

    # load the table into a sink (sqlite file)
    df1.to_sql('dataset_hly', engine_hly, if_exists='replace', index=False)




####################################################
# 2nd dataset: net greenhouse gas emissions per capita
def extract_gasem():
    url = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/sdg_13_10/?format=SDMX-CSV&lang=en&label=label_only'
    df2 = pd.read_csv(url, sep=',')
    
    return df2


def transform_gasem(df2):
    # exclude index and other Total data, as I do not use it in my analysis (I use only tonnes per capita)
    df2 = df2[~df2['unit'].isin(['Index, 1990=100'])].copy()
    df2 = df2[~df2['src_crf'].isin(['Total (excluding LULUCF and memo items, including international aviation)'])].copy()
    # drop rows with years 1990-2010, as there is no data for these years in the hly dataset
    df2 = df2[~df2['TIME_PERIOD'].isin(range(1990, 2011))]
    
    # drop unnecessary columns
    df2.drop(columns=['DATAFLOW','LAST UPDATE', 'freq', 'airpol', 'unit', 'src_crf', 'OBS_FLAG'], inplace=True)
   
    return df2


def load_gasem(df2, path):
    # specify the directory where to load the dataset
    engine_gasem = create_engine(f'sqlite:///{path}')

    # load the table into a sink (sqlite file)
    df2.to_sql('dataset_gasem', engine_gasem, if_exists='replace', index=False)


def merge_datasets(df1, df2):
    merged_df = pd.merge(df1, df2, on=['geo', 'TIME_PERIOD'], suffixes=('_hly', '_gasem'))
    return merged_df


def pipeline():
    df1 = extract_hly()
    df1 = transform_hly(df1)  
    load_hly(df1, '../data/dataset_hly.sqlite')

    df2 = extract_gasem()
    df2 = transform_gasem(df2)
    load_gasem(df2, '../data/dataset_gasem.sqlite')

    merged_df = merge_datasets(df1, df2)
    
    load_hly(merged_df, '../data/merged_dataset.sqlite')


if __name__ == '__main__':
    pipeline()
    