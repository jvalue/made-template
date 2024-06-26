import numpy as np
from script import transform_hly, load_hly, transform_gasem, load_gasem

import pandas as pd
import sqlite3
from pandas.testing import assert_frame_equal
from sqlalchemy import create_engine


##############################################
# tests for the 1st dataset
def test_transform_hly():
    data = pd.DataFrame({
        'geo': ['Place1', 'Place1', 'Place1', 'Place2', 'Place2', 'Place2'],
        'TIME_PERIOD': [2011, 2012, 2013, 2011, 2012, 2013],
        'OBS_VALUE': [1.0, 2, np.NaN, 4.0, np.NaN, 6],
        'sex': ['male', 'female', 'total', 'male', 'female', 'total'],
        'DATAFLOW': ['a', 'b', 'c', 'd', 'e', 'f'],
        'LAST UPDATE': ['2024', '2024', '2024', '2024', '2024', '2024'],
        'freq': ['y', 'y', 'y', 'y', 'y', 'y'],
        'unit': ['hly', 'hly', 'hly', 'hly', 'hly', 'hly'],
        'indic_he': ['a', 'b', 'c', 'd', 'e', 'f'],
        'OBS_FLAG': ['a', 'b', 'c', 'd', 'e', 'f']
    })
    # data.shape = (6, 10)
    # data.isnull().any()
    
    transformed_data = transform_hly(data)
    
    # expected transformed_data.shape = (2, 4)
    # expected transformed_data.isnull().any().any() = False
    assert transformed_data.shape == (2, 4)
    assert transformed_data.isnull().any().any() == False
    print('passed test_transform_hly')

   
def test_load_hly():
    data = pd.DataFrame({
        'geo': ['x', 'y', 'z'],
        '2012': [5, np.NaN, 6],
        '2013': [3, 4, 5]
    })
    
    test_path = './project/test_load_hly.sqlite'
    load_hly(data, test_path)
    
    conn = sqlite3.connect(test_path)
    result = pd.read_sql_query("SELECT * FROM dataset_hly", conn)
    conn.close()
    
    assert_frame_equal(result, data)
    print('passed test_load_hly')
    

##############################################
# tests for the 2nd dataset
def test_transform_gasem():
    data = pd.DataFrame({
        'geo': ['Place1', 'Place1', 'Place1', 'Place2', 'Place2', 'Place2'],
        'TIME_PERIOD': [2011, 2012, 2013, 2011, 2012, 2013],
        'OBS_VALUE': [1.0, 2, np.NaN, 4.0, np.NaN, 6],
        'DATAFLOW': ['a', 'b', 'c', 'd', 'e', 'f'],
        'LAST UPDATE': ['2024', '2024', '2024', '2024', '2024', '2024'],
        'freq': ['y', 'y', 'y', 'y', 'y', 'y'],
        'airpol': ['a', 'b', 'c', 'd', 'e', 'f'],
        'src_crf': ['a', 'b', 'c', 'd', 'e', 'f'],
        'unit': ['tonnes', 'tonnes', 'tonnes', 'tonnes', 'tonnes', 'tonnes'],
        'OBS_FLAG': ['a', 'b', 'c', 'd', 'e', 'f']
    })
    # data.shape = (6, 10)
      
    transformed_data = transform_gasem(data)
    
    # expected transformed_data.shape = (2, 4)    
    assert transformed_data.shape == (2, 4)
    print('passed test_transform_gasem')

   
def test_load_gasem():
    data = pd.DataFrame({
        'geo': ['a', 'b', 'c'],
        '2012': [8, np.NaN, 9],
        '2013': [2, 4.0, 7]
    })
    
    test_path = './project/test_load_gasem.sqlite'
    load_gasem(data, test_path)
    
    conn = sqlite3.connect(test_path)
    result = pd.read_sql_query("SELECT * FROM dataset_gasem", conn)
    conn.close()
    
    assert_frame_equal(result, data)
    print('passed test_load_gasem')


if __name__ == '__main__':
    test_transform_hly()
    test_load_hly()
    test_transform_gasem()
    test_load_gasem()
