import pandas as pd
import os
from sqlalchemy import create_engine, FLOAT, BIGINT, NVARCHAR

os.environ["KAGGLE_CONFIG_DIR"] = os.path.dirname('./project/kaggle.json')

from kaggle.api.kaggle_api_extended import KaggleApi

DATASET_DICT = {
    "bitcoin": {
        "dataset_path": "varpit94/bitcoin-data-updated-till-26jun2021",
        "file_name": "BTC-USD.csv",
        "database_name": "bitcoin",
        "sqlalchemy_datatype": {
            'Date': NVARCHAR(length=128),
            'Open': FLOAT(asdecimal=True),
            'High': FLOAT(asdecimal=True),
            'Low': FLOAT(asdecimal=True),
            'Close': FLOAT(asdecimal=True),
            'Adj': FLOAT(asdecimal=True),
            'Close': FLOAT(asdecimal=True),
            'Volume': BIGINT,
        }
    },
    "gold-price": {
        "dataset_path": "odins0n/monthly-gold-prices",
        "file_name": "1990-2021.csv",
        "database_name": "gold-price",
        "sqlalchemy_datatype": {
            'Date': NVARCHAR(length=128),
            'United States(USD)': FLOAT(asdecimal=True),
            'Europe(EUR)': FLOAT(asdecimal=True),
            'Japan(JPY)': FLOAT(asdecimal=True),
            'United Kingdom(GBP)': FLOAT(asdecimal=True),
            'Canada(CAD)': FLOAT(asdecimal=True),
            'Switzerland(CHF)': FLOAT(asdecimal=True),
            'India(INR)': FLOAT(asdecimal=True),
            'China(CNY)' : FLOAT(asdecimal=True),
            'Turkey(TRY)' : FLOAT(asdecimal=True),
            'Saudi Arabia(SAR)' : FLOAT(asdecimal=True),
            'Indonesia(IDR)' : FLOAT(asdecimal=True),
            'United Arab Emirates(AED)' : FLOAT(asdecimal=True),
            'Thailand(THB)' : FLOAT(asdecimal=True),
            'Vietnam(VND)' : FLOAT(asdecimal=True),
            'Egypt(EGP)' : FLOAT(asdecimal=True),
            'South Korean(KRW)' : FLOAT(asdecimal=True),
            'Australia(AUD)' : FLOAT(asdecimal=True),
            'South Africa(ZAR)' : FLOAT(asdecimal=True),
        }
    },
}

def authenticate_kaggle():
    api = KaggleApi()
    api.authenticate() 

    return api

def download_dataset(kaggle_api):
    
    for key, val in DATASET_DICT.items():
        kaggle_api.dataset_download_files(val['dataset_path'], path='./', unzip=True)

    return

def get_bitcoin_dataframe():
    # kaggle_api = authenticate_kaggle()
    # # Download the bitcoin dataset
    # kaggle_api.dataset_download_files('varpit94/bitcoin-data-updated-till-26jun2021', path='.', unzip=True) 

    # # Read the CSV file into a Pandas DataFrame
    # df = pd.read_csv('BTC-USD.csv',sep=',')

    # # created a SQLAlchemy engine to connect a bitcoin db
    # data_path = './data/bitcoin.sqlite'
    # engine = create_engine(f'sqlite:///{data_path}')

    # types = {
    #     'Date': NVARCHAR(length=128),
    #     'Open': FLOAT(asdecimal=True),
    #     'High': FLOAT(asdecimal=True),
    #     'Low': FLOAT(asdecimal=True),
    #     'Close': FLOAT(asdecimal=True),
    #     'Adj': FLOAT(asdecimal=True),
    #     'Close': FLOAT(asdecimal=True),
    #     'Volume': BIGINT,
    # }

    # df.to_sql("bitcoin", con=engine, index=False, if_exists='replace', dtype=types)
    bitcoin_df = pd.read_csv(DATASET_DICT["bitcoin"]["file_name"])

    return bitcoin_df

def get_gold_price_dataframe():
    # kaggle_api = authenticate_kaggle()
    # # Download the gold-price dataset
    # kaggle_api.dataset_download_files('odins0n/monthly-gold-prices', path='.', unzip=True) 

    # # Read the CSV file into a Pandas DataFrame
    # df = pd.read_csv('1990-2021.csv',sep=',')

    # # created a SQLAlchemy engine to connect a gold-price db
    # data_path = './data/gold-price.sqlite'
    # engine = create_engine(f'sqlite:///{data_path}')

    # types = {
    #     'Date': NVARCHAR(length=128),
    #     'United States(USD)': FLOAT(asdecimal=True),
    #     'Europe(EUR)': FLOAT(asdecimal=True),
    #     'Japan(JPY)': FLOAT(asdecimal=True),
    #     'United Kingdom(GBP)': FLOAT(asdecimal=True),
    #     'Canada(CAD)': FLOAT(asdecimal=True),
    #     'Switzerland(CHF)': FLOAT(asdecimal=True),
    #     'India(INR)': FLOAT(asdecimal=True),
    #     'China(CNY)' : FLOAT(asdecimal=True),
    #     'Turkey(TRY)' : FLOAT(asdecimal=True),
    #     'Saudi Arabia(SAR)' : FLOAT(asdecimal=True),
    #     'Indonesia(IDR)' : FLOAT(asdecimal=True),
    #     'United Arab Emirates(AED)' : FLOAT(asdecimal=True),
    #     'Thailand(THB)' : FLOAT(asdecimal=True),
    #     'Vietnam(VND)' : FLOAT(asdecimal=True),
    #     'Egypt(EGP)' : FLOAT(asdecimal=True),
    #     'South Korean(KRW)' : FLOAT(asdecimal=True),
    #     'Australia(AUD)' : FLOAT(asdecimal=True),
    #     'South Africa(ZAR)' : FLOAT(asdecimal=True),
    # }

    # df.to_sql("gold-price", con=engine, index=False, if_exists='replace', dtype=types)

    gold_price_df = pd.read_csv(DATASET_DICT["gold-price"]["file_name"])

    return gold_price_df

def dump_dataset_to_db(dataframe, db_name, datatype):

    db_engine = create_engine(f"sqlite:///data/{db_name}.sqlite")
    dataframe.to_sql(db_name, db_engine, index=False, if_exists='replace', dtype=datatype)
    return

def data_collector():

    kaggle_api = authenticate_kaggle()

    download_dataset(kaggle_api)

    bitcoin_df = get_bitcoin_dataframe()

    gold_price_df = get_gold_price_dataframe()

    dump_dataset_to_db(dataframe=bitcoin_df, db_name=DATASET_DICT['bitcoin']['database_name'],
                       datatype=DATASET_DICT['bitcoin']['sqlalchemy_datatype'])

    dump_dataset_to_db(dataframe=gold_price_df, db_name=DATASET_DICT['gold-price']['database_name'],
                       datatype=DATASET_DICT['gold-price']['sqlalchemy_datatype'])

    return

if __name__ == "__main__":
    data_collector()
