import os
import pandas as pd
import numpy as np

from etl_pipeline_runner.services import (
    ETLPipeline,
    DataExtractor,
    CSVHandler,
    SQLiteLoader,
    ETLQueue,
)

DATA_DIRECTORY = os.path.join(os.getcwd(), "data")

# yangon_city


def transform_yangon(data_frame: pd.DataFrame):
    data_frame.drop(
        labels=["Prcp", "Snow", "Wdir", "Wspd", "Wpgt", "Pres", "Tsun"],
        axis=1,
        inplace=True,
    )
    data_frame.insert(
        loc=4,
        column="City",
        value="Yangon",
        allow_duplicates=True,
    )
    # dataframe.dropna(axis= 0, inplace= True)
    return data_frame


yangon_loader = SQLiteLoader(
    db_name="analysis.sqlite",
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
    data_name="Yangon weather",
    url="https://bulk.meteostat.net/v2/daily/48097.csv.gz",
    type=DataExtractor.CSV,
    file_handlers=(yangon_csv_handler,),
)

# mandalay_city


def transform_mandalay(data_frame: pd.DataFrame):
    data_frame.drop(
        labels=["Prcp", "Snow", "Wdir", "Wspd", "Wpgt", "Pres", "Tsun"],
        axis=1,
        inplace=True,
    )
    data_frame.insert(loc=4, column="City", value="mandalay", allow_duplicates=True)
    # dataframe.dropna(axis= 0, inplace= True)
    return data_frame


mandalay_loader = SQLiteLoader(
    db_name="analysis.sqlite",
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

# naypyitaw_city


def transform_naypyitaw(data_frame: pd.DataFrame):
    data_frame.drop(
        labels=["Prcp", "Snow", "Wdir", "Wspd", "Wpgt", "Pres", "Tsun"],
        axis=1,
        inplace=True,
    )
    data_frame.insert(loc=4, column="City", value="naypyitaw", allow_duplicates=True)
    # dataframe.dropna(axis= 0, inplace= True)
    return data_frame


naypyitaw_loader = SQLiteLoader(
    db_name="analysis.sqlite",
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

# supermarket_sales


def transform_supermarket_sales_datasource(data_frame: pd.DataFrame):
    data_frame = data_frame.drop(
        labels=[
            "Invoice ID",
            "Branch",
            "Customer type",
            "Gender",
            "Unit price",
            "Tax 5%",
            "Time",
            "cogs",
            "gross margin percentage",
            "gross income",
            "Rating",
        ],
        axis=1,
    )
    return data_frame


supermarket_sales_datasource_loader = SQLiteLoader(
    db_name="analysis.sqlite",
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


if __name__ == "__main__":
    yangon_pipeline = ETLPipeline(
        extractor=yangon_extractor,
    )
    mandalay_pipeline = ETLPipeline(
        extractor=mandalay_extractor,
    )
    naypyitaw_pipeline = ETLPipeline(
        extractor=naypyitaw_extractor,
    )
    supermarket_pipeline = ETLPipeline(
        extractor=supermarket_sales_datasource_extractor,
    )
    ETLQueue(
        etl_pipelines=(
            yangon_pipeline,
            mandalay_pipeline,
            naypyitaw_pipeline,
            supermarket_pipeline,
        )
    ).run()
