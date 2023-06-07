#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[14]:


#Data Extraction
trainstops= pd.read_csv('https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV',delimiter=';', on_bad_lines='skip')


# In[15]:


#Data transformation

#dropping Status column
trainstopsNew = trainstops.drop("Status", axis=1)


# In[16]:


#Dropping invalid rows in Verkehr
trainstopsNew =  trainstopsNew[trainstopsNew['Verkehr'].isin(['FV', 'RV', 'nur DPN'])]


# In[33]:


#Dropping invalid values in "Laenge" and "Breite"
# trainstopsNew.Laenge = trainstopsNew['Laenge'].str.replace(',', '.').astype(float)
# trainstopsNew.Breite = trainstopsNew['Breite'].str.replace(',', '.').astype(float)

trainstopsNew = trainstopsNew[(trainstopsNew['Laenge'] >= -90) & (trainstopsNew['Laenge'] <= 90)]
trainstopsNew = trainstopsNew[(trainstopsNew['Breite'] >= -90) & (trainstopsNew['Breite'] <= 90)]


# In[35]:


#Setting up valid value filter
trainstopsNew= trainstopsNew[trainstopsNew['IFOPT'].str.match(r'^[a-zA-Z]{2}:\d+:?\d*:?(\d+)?$', na=False)]


# In[37]:


#Dropping empty cells 
trainstopsNew= trainstopsNew.dropna()


# In[40]:


#Transforming datatypes
datatypes = {
            "EVA_NR": int,
            "DS100": str,
            "IFOPT": str,
            "NAME": str,
            "Verkehr": str,
            "Laenge": float,
            "Breite": float,
            "Betreiber_Name": str,
            "Betreiber_Nr": int
        }
trainstopsNew = trainstopsNew.astype(datatypes)


# In[43]:


#Writing data into SQLite database
trainstopsNew.to_sql('TrainstopsData', 'sqlite:///trainstops.sqlite', if_exists='replace')

