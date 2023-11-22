import pandas as pd
from sqlalchemy import create_engine
import os.path
from os import path

dataset1 = pd.read_csv('/Users/akshatkhara/Desktop/Study Material/Semester 3/Methods of Advance Data Engineering/made-template-WS2324/India_Injury_Road_Accident_Fatality_2017-2020.csv')
dataset2 = pd.read_csv('/Users/akshatkhara/Desktop/Study Material/Semester 3/Methods of Advance Data Engineering/made-template-WS2324/Road Accident Data 2020 India.csv')

data1 = pd.DataFrame(dataset1)
data2 = pd.DataFrame(dataset2)




