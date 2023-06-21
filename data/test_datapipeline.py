""" 
Module for testing the module datapipeline.py
"""
import datetime as dt
import os
import numpy as np
import pandas as pd
import pytest
from sqlalchemy import create_engine, inspect
import datapipeline as pipe


@pytest.mark.dependency()
def test_get_datasources():
    """ Tests the methods to load the datasources """
    ds1 = pipe.get_datasource_1()
    assert isinstance(ds1, pd.DataFrame)

    ds2_1 = pipe.get_datasource_2_1()
    assert isinstance(ds2_1, pd.DataFrame)

    with pytest.raises(FileNotFoundError):
        ds2_2 = pipe.get_datasource_2_2(year=dt.date.today().year + 1)

    ds2_2 = pipe.get_datasource_2_2(year=dt.date.today().year - 1)
    assert isinstance(ds2_2, pd.DataFrame)

    ds3 = pipe.get_datasource_3()
    assert isinstance(ds3, pd.DataFrame)


@pytest.mark.dependency()
def test_store_dataframe():
    """ Tests the method to store a dataframe in a sqlite database """
    org_path = pipe.DATABASE_PATH
    temp_path = os.path.join(pipe.DATA_DIR, "data_test.sqlite")
    pipe.DATABASE_PATH = temp_path
    df = pd.DataFrame(np.arange(12).reshape(3, 4), columns=["A", "B", "C", "D"])

    pipe.store_dataframe(df, "test")

    assert os.path.exists(temp_path)

    engine = create_engine(f"sqlite:////{pipe.DATABASE_PATH}")
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    assert len(tables) == 1
    assert "test" in tables

    os.remove(temp_path)
    pipe.DATABASE_PATH = org_path


# Only execute test for the complete datapipeline if the previous tests passed
@pytest.mark.dependency(depends=["test_get_datasources", "test_store_dataframe"])
def test_datapipeline():
    """ 
    Tests the complete pipeline if all previous tests were successfull
    
    For this run the main function and check if it creates the sqlite database with #
    the expected amount of tables
    """
    if os.path.exists(pipe.DATABASE_PATH):
        os.remove(pipe.DATABASE_PATH)
    pipe.main()

    assert os.path.exists(pipe.DATABASE_PATH)

    engine = create_engine(f"sqlite:////{pipe.DATABASE_PATH}")
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    assert len(tables) == 2
    assert "over_time" in tables
    assert "by_states" in tables
