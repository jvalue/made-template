import pytest
import copy

from project.pipeline import (
    yangon_loader, mandalay_loader, naypyitaw_loader,transform_yangon,transform_mandalay,transform_naypyitaw,transform_supermarket_sales_datasource, yangon_csv_handler,mandalay_csv_handler,
    naypyitaw_csv_handler, yangon_extractor,mandalay_extractor,naypyitaw_extractor,DATA_DIRECTORY,
)
from etl_pipeline_runner.services import (
    ETLPipeline,
    DataExtractor,
    CSVHandler,
    SQLiteLoader,
    ETLQueue,
)

@pytest.fixture
def sales_pipeline():
    supermarket_sales_datasource_loader = SQLiteLoader(
    db_name="test.sqlite",
    table_name="supermarket_sales",
    if_exists=SQLiteLoader.REPLACE,
    index=False,
    method=None,
    output_directory=DATA_DIRECTORY,
    )
    
    
    supermarket_sales_datasource_csv_handler = CSVHandler(
        file_name="supermarket_sales - Sheet1.csv",
        sep=",",
        names=None,
        transformer=transform_supermarket_sales_datasource,
        loader=supermarket_sales_datasource_loader,
    )

    supermarket_sales_datasource_extractor = DataExtractor(
        data_name="supermarket_sales_datasource weather",
        url="https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales/download?datasetVersionNumber=3",
        type=DataExtractor.KAGGLE_ARCHIVE,
        file_handlers=(supermarket_sales_datasource_csv_handler,),
    )
    sales_pipeline=ETLPipeline(extractor=supermarket_sales_datasource_extractor)
    yield sales_pipeline

        



@pytest.fixture
def yangon_pipeline():
    yangon_loader = SQLiteLoader(
    db_name="test.sqlite",
    table_name="weather",
    if_exists=SQLiteLoader.REPLACE,
    index=False,
    method=None,
    output_directory=DATA_DIRECTORY,
    )
    
    yangon_csv_handler = CSVHandler(
        file_name="48097.csv.gz",
        sep=",",
        names=[
            "Date",
            "Tavg",
            "Tmin",
            "Tmax",
            "Prcp",
            "Snow",
            "Wdir",
            "Wspd",
            "Wpgt",
            "Pres",
            "Tsun",
        ],
        transformer=transform_yangon,
        loader=yangon_loader,
        compression=CSVHandler.GZIP_COMPRESSION,
    )

    yangon_extractor = DataExtractor(
        data_name="yangon weather",
        url="https://bulk.meteostat.net/v2/daily/48097.csv.gz",
        type=DataExtractor.CSV,
        file_handlers=(yangon_csv_handler,),
    )
    yangon_pipeline=ETLPipeline(extractor=yangon_extractor)
    yield yangon_pipeline

@pytest.fixture
def mandalay_pipeline():
    mandalay_loader = SQLiteLoader(
    db_name="test.sqlite",
    table_name="weather",
    if_exists=SQLiteLoader.APPEND,
    index=False,
    method=None,
    output_directory=DATA_DIRECTORY,
    )
    
    mandalay_csv_handler = CSVHandler(
        file_name="48042.csv.gz",
        sep=",",
        names=[
            "Date",
            "Tavg",
            "Tmin",
            "Tmax",
            "Prcp",
            "Snow",
            "Wdir",
            "Wspd",
            "Wpgt",
            "Pres",
            "Tsun",
        ],
        transformer=transform_mandalay,
        loader=mandalay_loader,
        compression=CSVHandler.GZIP_COMPRESSION,
    )

    mandalay_extractor = DataExtractor(
        data_name="mandalay weather",
        url="https://bulk.meteostat.net/v2/daily/48042.csv.gz",
        type=DataExtractor.CSV,
        file_handlers=(mandalay_csv_handler,),
    )
    mandalay_pipeline=ETLPipeline(extractor=mandalay_extractor)
    yield mandalay_pipeline


       
@pytest.fixture
def naypyitaw_pipeline():
    naypyitaw_loader = SQLiteLoader(
    db_name="test.sqlite",
    table_name="weather",
    if_exists=SQLiteLoader.APPEND,
    index=False,
    method=None,
    output_directory=DATA_DIRECTORY,
    )
    
    naypyitaw_csv_handler = CSVHandler(
        file_name="VYNT0.csv.gz",
        sep=",",
        names=[
            "Date",
            "Tavg",
            "Tmin",
            "Tmax",
            "Prcp",
            "Snow",
            "Wdir",
            "Wspd",
            "Wpgt",
            "Pres",
            "Tsun",
        ],
        transformer=transform_naypyitaw,
        loader=naypyitaw_loader,
        compression=CSVHandler.GZIP_COMPRESSION,
    )

    naypyitaw_extractor = DataExtractor(
        data_name="naypyitaw weather",
        url="https://bulk.meteostat.net/v2/daily/VYNT0.csv.gz",
        type=DataExtractor.CSV,
        file_handlers=(naypyitaw_csv_handler,),
    )
    naypyitaw_pipeline=ETLPipeline(extractor=naypyitaw_extractor)
    yield naypyitaw_pipeline       
        
