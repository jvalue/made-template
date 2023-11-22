import os.path
from kaggle.api.kaggle_api_extended import KaggleApi


def download_datasets(k_api):
    """
    Checks file system if data is already existent to avoid unnecessary download traffic.
    If not, the specified files will be downloaded using the Kaggle API object.
    """
    # files_to_download = ['smart_meters/acorn_details.csv', 'smart_meters/informations_households.csv',
    #                      'crime/london_crime_by_lsoa.csv', 'housing/housing_in_london_yearly_variables.csv',
    #                      'borough_demo/london-borough-profiles-2016 Data set.csv']
    if not os.path.isfile('smart_meters/acorn_details.csv'):
        k_api.dataset_download_file(dataset='jeanmidev/smart-meters-in-london', file_name='acorn_details.csv',
                                    path='../data/smart_meters')
    if not os.path.isfile('smart_meters/informations_households.csv'):
        k_api.dataset_download_file(dataset='jeanmidev/smart-meters-in-london', file_name='informations_households.csv',
                                    path='../data/smart_meters')
    if not os.path.isfile('crime/london_crime_by_lsoa.csv'):
        k_api.dataset_download_file(dataset='jboysen/london-crime', file_name='london_crime_by_lsoa.csv',
                                    path='../data/crime')  # Huge file (approx. 1GB) --> can take a while
    if not os.path.isfile('housing/housing_in_london_yearly_variables.csv'):
        k_api.dataset_download_file(dataset='justinas/housing-in-london',
                                    file_name='housing_in_london_yearly_variables.csv',
                                    path='../data/housing')
    if not os.path.isfile('borough_demo/london-borough-profiles-2016 Data set.csv'):
        k_api.dataset_download_file(dataset='marshald/london-boroughs',
                                    file_name='london-borough-profiles-2016 Data set.csv',
                                    path='../data/borough_demo')


# API object is used to communicate with the remote datasources
api = KaggleApi()
api.authenticate()

download_datasets(api)
