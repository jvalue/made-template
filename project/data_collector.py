import gdown
import pandas as pd
import os
from sqlalchemy import create_engine, FLOAT, BIGINT, NVARCHAR

data_path = '../data/bitcoin.sqlite'
engine = create_engine(f'sqlite:///{data_path}')

file_id = '17WbP39sBzav1L_ir78Ec9qbb3HfOjjiC'
url = 'https://drive.google.com/uc?export=download&id='+file_id
gdown.download(url, 'data.csv')

df = pd.read_csv('data.csv',sep=',')

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

df.to_sql("bitcoin", engine, index=False, if_exists='replace', dtype=types)


data_path = '../data/gold-price.sqlite'
engine = create_engine(f'sqlite:///{data_path}')

file_id = '1i_WTJItXDqQ9Fha6sCEeEBlCfB5qMTnk'
url = 'https://drive.google.com/uc?export=download&id='+file_id
gdown.download(url, 'data.csv')

df = pd.read_csv('data.csv',sep=',')

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

df.to_sql("gold-price", engine, index=False, if_exists='replace', dtype=types)

os.remove('data.csv')
