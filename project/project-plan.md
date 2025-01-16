## Title

Crime Data Analysis in Los Angeles

## Main Question

1. What are the patterns in crime types and locations across different neighborhoods in Los Angeles?
2. How do crime rates vary by time of day, day of the week, or season in Los Angeles?
3. Are crime rates in Los Angeles related to its weather trend?

## Description

The objective of this project is to analyze and model crime data in Los Angeles to identify spatial and temporal patterns. By examining historical crime incidents, we aim to uncover insights into when and where various types of crimes are most likely to occur. Leveraging a dataset that includes information on crime type, location, and date, this project will employ data analysis and machine learning techniques to predict potential crime hotspots.
The analysis will provide a deeper understanding of crime patterns in Los Angeles, potentially aiding in proactive law enforcement and community awareness. This project will involve data cleaning, exploration, feature engineering, model development, and visualization to provide actionable insights.

## Datasources

### Datasource1: Crime in Los Angeles Dataset
* Metadata URL: https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8/about_data 
* Data URL: https://www.kaggle.com/code/fadymamdouh01/crime-in-los-angeles-data/input
* Data Type: CSV

This dataset contains records of crime incidents in Los Angeles, with details on crime type, location, date, time, etc. It offers a comprehensive view of crime in the city, allowing for spatial and temporal analysis. Key attributes in the dataset include:

- **Date Rptd**: Date the crime was reported
- **AREA NAME**: Specific neighborhood and approximate location of the incident
- **Crm Cd Desc**: Classification of the crime (e.g., assault, theft)
- **DATE OCC**: Date when the crime occurred, useful for time-based pattern analysis
- **TIME OCC**: Time when the crime occured.
- etc

### Datasource2: Weather in Los Angeles Dataset
* Data URL: https://bulk.meteostat.net/v2/monthly/72295.csv.gz 
* Data Type: CSV

This dataset provides monthly weather data for Los Angeles, including temperature, precipitation, and other climatic variables. It is ideal for correlating crime patterns with weather conditions to uncover potential relationships. Key attributes in the dataset include:

- **Date**: The specific month and year of the weather record
- **TAVG**: Average temperature for the month (in °C)
- **TMIN**: Minimum temperature recorded during the month (in °C)
- **TMAX**: Maximum temperature recorded during the month (in °C)
- **PRCP**: Total precipitation for the month (in mm)
- **WSPD**: Average wind speed during the month (in km/h)
- etc

## Work Packages

1. Extract the data from multiple sources
2. Implement the data transformation step in ETL Pipeline
3. Implement the data loading step in ETL Data Pipeline
4. Perform automated tests for the project
5. Continuous integration pipeline for the project
6. Final report and presentation submission
