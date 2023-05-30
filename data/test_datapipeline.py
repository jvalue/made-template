import subprocess
import pandas as pd
import numpy as np
import datapipeline as pipe
import os
import datetime as dt
import pytest
from sqlalchemy import create_engine, inspect


@pytest.mark.dependency()
def test_get_datasources():
    ds1 = pipe.get_datasource_1()
    assert type(ds1) == pd.DataFrame
    
    ds2_1 = pipe.get_datasource_2_1()
    assert type(ds2_1) == pd.DataFrame
    
    with pytest.raises(Exception):
         ds2_2 = pipe.get_datasource_2_2(year=dt.date.today().year + 1)
    
    ds2_2 = pipe.get_datasource_2_2(year=dt.date.today().year - 1)
    assert type(ds2_2) == pd.DataFrame
    
    ds2_3 = pipe.get_datasource_3()
    assert type(ds2_3) == pd.DataFrame

    
@pytest.mark.dependency()
def test_store_dataframe():
    org_path = pipe.DATABASE_PATH
    temp_path = os.path.join(pipe.DATA_DIR, 'data_test.sqlite')
    pipe.DATABASE_PATH = temp_path
    df = pd.DataFrame(np.arange(12).reshape(3, 4), columns=['A', 'B', 'C', 'D'])
    
    pipe.store_dataframe(df, 'test')
    
    assert os.path.exists(temp_path) == True
    
    engine = create_engine(f'sqlite:////{pipe.DATABASE_PATH}')
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    
    assert len(tables) == 1
    assert 'test' in tables
    
    os.remove(temp_path)
    pipe.DATABASE_PATH = org_path


# Only execute test for the complete datapipeline if the previous tests passed
@pytest.mark.dependency(depends=['test_get_datasources', 'test_store_dataframe'])  
def test_datapipeline():
    if os.path.exists(pipe.DATABASE_PATH):
        os.remove(pipe.DATABASE_PATH)    
    subprocess.run(['python', os.path.join(pipe.DATA_DIR, 'datapipeline.py')])
    
    assert os.path.exists(pipe.DATABASE_PATH) == True
    
    engine = create_engine(f'sqlite:////{pipe.DATABASE_PATH}')
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    
    assert len(tables) == 2
    assert 'over_time' in tables
    assert 'by_states' in tables