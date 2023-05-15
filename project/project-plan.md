# Project Plan

## Summary
This project aims to analyze the correlation between the proximity of public transport stops and the rental prices of apartments in Nuremberg.

## Rationale
By understanding the relationship between public transport stops and rental prices, this analysis can provide valuable insights for renters, landlords, and city planners in optimizing public transportation networks and improving the accessibility of housing in Nuremberg.

## Datasources
### Datasource1: Nuremberg Stops: IDs and geodata
Metadata URL: https://mobilithek.info/offers/-6228947429763481687 <br />
Data URL: https://opendata.vag.de/dataset/08eb49f9-0f6c-4b76-96fd-5f8e3a0ac593/resource/c66d5b67-6a01-4190-a9cf-1de6359d07ae/download/20170601_haltestellen_id_geo.xlsx <br />
Data Type: xlsx 

This dataset provides information on all subway, tram, and bus stops in the VAG area of Nuremberg, including their IDs and geolocation data.

### Datasource2: Immoscout24 dataset
Metadata URL: https://www.kaggle.com/datasets/corrieaar/apartment-rental-offers-in-germany <br />
Data URL: https://www.kaggle.com/datasets/corrieaar/apartment-rental-offers-in-germany/download?datasetVersionNumber=6 <br />
Data Type: xlsx

This dataset contains rental property listings on Immoscout24, the largest real estate platform in Germany, including information on rental prices, property attributes, and location.

## Work Packages
- [x] : Find usable open data sources
- [x] : Build data pipelines
- [x] : Data cleaning and preprocessing
- [ ] : Exploratory data analysis
- [ ] : Spatial analysis
- [ ] : Visualization and reporting
- [ ] : Implement automated testing
- [ ] : Add continous integration
- [ ] : Deploy project