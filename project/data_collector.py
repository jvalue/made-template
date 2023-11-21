import gdown
import pandas as pd
import os
from sqlalchemy import create_engine, FLOAT, BIGINT, NVARCHAR

os.environ["KAGGLE_CONFIG_DIR"] = os.path.dirname('./project/kaggle.json')

from kaggle.api.kaggle_api_extended import KaggleApi

# Instantiate the Kaggle API
api = KaggleApi()
api.authenticate() 

# Download the bitcoin dataset
api.dataset_download_files('varpit94/bitcoin-data-updated-till-26jun2021', path='.', unzip=True) 

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('BTC-USD.csv',sep=',')

# created a SQLAlchemy engine to connect a bitcoin db
data_path = './data/bitcoin.sqlite'
engine = create_engine(f'sqlite:///{data_path}')

types = {
    'Date': NVARCHAR(length=128),
    'Open': FLOAT(asdecimal=True),
    'High': FLOAT(asdecimal=True),
    'Low': FLOAT(asdecimal=True),
    'Close': FLOAT(asdecimal=True),
    'Adj': FLOAT(asdecimal=True),
    'Close': FLOAT(asdecimal=True),
    'Volume': BIGINT,
}

df.to_sql("bitcoin", con=engine, index=False, if_exists='replace', dtype=types)

# Download the gold-price dataset
api.dataset_download_files('odins0n/monthly-gold-prices', path='.', unzip=True) 

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('1990-2021.csv',sep=',')

# created a SQLAlchemy engine to connect a gold-price db
data_path = './data/gold-price.sqlite'
engine = create_engine(f'sqlite:///{data_path}')

types = {
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

df.to_sql("gold-price", con=engine, index=False, if_exists='replace', dtype=types)

# os.remove('data.csv')
