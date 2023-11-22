import os.path
import pandas as pd
import sqlalchemy as db
from kaggle.api.kaggle_api_extended import KaggleApi
from sqlalchemy_utils import database_exists, create_database


def main():
    api = KaggleApi()
    api.authenticate()
    download_datasets(api)
    alter_datasets()


def download_datasets(k_api):
    """
    Checks file system if data is already existent to avoid unnecessary download traffic.
    If not, the specified files will be downloaded using the Kaggle API object.
    """
    # files_to_download = ['smart_meters/acorn_details.csv', 'smart_meters/informations_households.csv',
    #                      'crime/london_crime_by_lsoa.csv', 'housing/housing_in_london_yearly_variables.csv',
    #                      'borough_demo/london-borough-profiles-2016 Data set.csv']
    if not os.path.isfile('../data/smart_meters/acorn_details.csv'):
        k_api.dataset_download_file(dataset='jeanmidev/smart-meters-in-london', file_name='acorn_details.csv',
                                    path='../data/smart_meters')
    if not os.path.isfile('../data/smart_meters/informations_households.csv'):
        k_api.dataset_download_file(dataset='jeanmidev/smart-meters-in-london', file_name='informations_households.csv',
                                    path='../data/smart_meters')
    if not os.path.isfile('../data/crime/london_crime_by_lsoa.csv.zip'):
        k_api.dataset_download_file(dataset='jboysen/london-crime', file_name='london_crime_by_lsoa.csv',
                                    path='../data/crime')  # Huge file (approx. 1GB) --> can take a while
    if not os.path.isfile('../data/housing/housing_in_london_yearly_variables.csv'):
        k_api.dataset_download_file(dataset='justinas/housing-in-london',
                                    file_name='housing_in_london_yearly_variables.csv',
                                    path='../data/housing')
    if not os.path.isfile('../data/borough_demo/london-borough-profiles-2016 Data set.csv'):
        k_api.dataset_download_file(dataset='marshald/london-boroughs',
                                    file_name='london-borough-profiles-2016 Data set.csv',
                                    path='../data/borough_demo')


def alter_datasets():
    borough_demo = pd.read_csv('../data/borough_demo/london-borough-profiles-2016%20Data%20set.csv')
    crime = pd.read_csv('../data/crime/london_crime_by_lsoa.csv.zip')
    housing = pd.read_csv('../data/housing/housing_in_london_yearly_variables.csv')
    smart_meters_acorn = pd.read_csv('../data/smart_meters/acorn_details.csv')
    smart_meters_households = pd.read_csv('../data/smart_meters/informations_households.csv')

    save_to_database(borough_demo=borough_demo)


def save_to_database(**dfs):
    # There is unfortunately still an error with the connection of SQLALchemy to the local sqlite database
    pass
    # engine = db.create_engine('sqlite:///data/database.sqlite', echo=True)
    # if not database_exists(engine.url):
    #     create_database(engine.url)
    # con = engine.connect()
    #
    # for df in dfs:
    #     metadata = db.MetaData()
    #     table = db.Table('test', metadata, db.Column('test', db.String, primary_key=True))
    #     metadata.create_all(engine)


if __name__ == "__main__":
    main()
