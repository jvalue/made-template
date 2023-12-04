import pandas as pd
import pytest
from sqlalchemy import create_engine, inspect
import data_collector as dc


@pytest.mark.dependency()
def test_get_datasets():
    ds1 = dc.get_bitcoin_dataframe()
    assert isinstance(ds1, pd.DataFrame)

    ds2 = dc.get_gold_price_dataframe()
    assert isinstance(ds2, pd.DataFrame)


# Only execute test for the complete datapipeline if the previous tests passed
@pytest.mark.dependency()
def test_data_collector_pipeline():
    """
    test data collector pipeline number of created tables and names
    """
    data_dict = dc.DATASET_DICT
    dc.data_collector()

    co_db_engine = create_engine(f"sqlite:///data/{data_dict['bitcoin']['database_name']}.sqlite")
    inspector = inspect(co_db_engine)
    tables = inspector.get_table_names()

    assert len(tables) == 1
    assert data_dict['bitcoin']['database_name'] in tables

    gp_db_engine = create_engine(f"sqlite:///data/{data_dict['gold-price']['database_name']}.sqlite")
    inspector = inspect(gp_db_engine)
    tables = inspector.get_table_names()

    assert len(tables) == 1
    assert data_dict['gold-price']['database_name'] in tables