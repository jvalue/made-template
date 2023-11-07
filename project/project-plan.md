# Project Plan

## Summary
This data science project aims to analyze the Paphos International Airport of Cyprus daily Air traffic and weather data to determine the differences between air traffic of the airport. As Paphos is one of the main International and busiest airport of the Cyprus, its really important to know the analysis of air traffics dependency on weather so that commercial airlines as well as passengers can plan the trips accordingly. This project draws a connection between weather and air traffic to help the countries economy.

## Rationale
The analysis helps to do correlate frequency of air traffic in Paphos International Airport based on weather forcasts. 


## Datasources
### Datasource 1: European Data Portal - Daily Air Traffic at Paphos Airport
#### Metadata URL: https://data.europa.eu/en
#### Sample Data URL: https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fwww.data.gov.cy%2Fsites%2Fdefault%2Ffiles%2FPAFOS%2520AIRPORT%2520DAILY%2520AIR%2520TRAFFIC%25202019.xlsx&wdOrigin=BROWSELINK
#### Data Type: CSV
#### Data Descriptions:
In this data source contains daily air traffic data of Paphos International Airport divided by monthly basis. Data includes tanding and take-off count of both the international and national flights. This dataset also takes into account the transit flights and helicopters landing and take-off information. 

### Datasource 2: Meteostat Developers - Dail weather data of Paphos International Airport of Cyprus
#### Metadata URL: https://dev.meteostat.net/bulk/daily.html#endpoints
Sample Data URL: https://bulk.meteostat.net/v2/daily/{station}.csv.gz Station-id of Paphos Airport = '17600'
#### Data Type: CSV
#### Data Descriptions:
This data source will provide daily weather and climate data of Paphos Airport that includes average air temperature, daily minimum and maximum air temperature, monthly precipitation total, maximum snow depth, average wind direction and speed, peak wind gust, average sea-level air pressure, and monthly sunshine total.

## Work Packages:
1. Extract data from multiple sources.
2. Implement data transformation step in ETL Data Pipeline.
3. Implement data loading step in ETL Data Pipeline.
4. Creating Graphs for the analysis.
5. Calculating the frequency of air traffic dependency on weather.
6. Final Analysis Report and Presentation.