import pandas as pd
from sqlalchemy import create_engine

####################################################
# 1st dataset: Healthy life years at birth
df1 = pd.read_csv( \
    'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/tps00150/?format=SDMX-CSV&lang=en&label=label_only', \
    sep=','
)

#look at the data to see what is in the dataframe
print(df1)

# exclude geneder data, as I do not use it in my analysis
df1 = df1[~df1['sex'].isin(['Females', 'Males'])]

# drop unnesessary columns
df1.drop(columns=['DATAFLOW','LAST UPDATE', 'freq', 'unit', 'indic_he', 'OBS_FLAG', 'sex'], inplace=True)

# turn years into columns
df1_new = df1.pivot(index='geo', columns='TIME_PERIOD')['OBS_VALUE']
df1 = df1_new
df1.reset_index(inplace=True)

# specify the directory where to load the dataset
engine1 = create_engine('sqlite:///../data/dataset_hly.sqlite')

# load the table into a sink (sqlite file)
df1.to_sql('dataset_hly', engine1, if_exists='replace', index=False)



####################################################
# 2nd dataset: net greenhouse gas emissions per capita
df2 = pd.read_csv( \
    'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/sdg_13_10/?format=SDMX-CSV&lang=en&label=label_only', \
    sep=','
)

#look at the data to see what is in the dataframe
print(df1)

# exclude index and other Total data, as I do not use it in my analysis (i use only tonnes per capita)
df2 = df2[~df2['unit'].isin(['Index, 1990=100'])]
df2 = df2[~df2['src_crf'].isin(['Total (excluding LULUCF and memo items, including international aviation)'])]

# drop unnesessary columns
df2.drop(columns=['DATAFLOW','LAST UPDATE', 'freq', 'airpol', 'unit', 'src_crf', 'OBS_FLAG'], inplace=True)

# turn years into columns
df2_new = df2.pivot(index='geo', columns='TIME_PERIOD')['OBS_VALUE']
df2 = df2_new
df2.reset_index(inplace=True)

# specify the directory where to load the dataset
engine2 = create_engine('sqlite:///../data/dataset_gasem.sqlite')

# load the table into a sink (sqlite file)
df1.to_sql('dataset_gasem', engine2, if_exists='replace', index=False)
