# Project Plan

## Title
<!-- Give your project a short title. -->
The impact of weather on bicycle theft in Berlin

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
Does sunny or rainy weather have an impact on bicycle theft in Berlin? Is there a correlation between temperature or percipitation and bicycle theft (or a seasonality)? 

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Bicycle theft is a huge problem in Berlin, as it has one of [the highest rates of bike theft per inhabitant in Germany](https://www.wsm.eu/en/knowledge/bicycle-theft-in-germany/). This poses the question: How can i keep my bicycle safe in Berlin? Apart from a strong lock, there might be other influences on the probability of getting your bike stolen, such as place or time of the day. A rather uncommon factor to think of is the weather, though it plays a huge part in mobility and transportation, especially for bicycles. Thus, in this project, i will analyze correlations between bicycle theft and weather data by combining two datasets from Berlin. 

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource 1: Bicycle theft data in Berlin 
* Metadata URL: https://www.berlin.de/polizei/_assets/dienststellen/lka/datensatzbeschreibung.pdf 
* Data URL: https://www.polizei-berlin.eu/Fahrraddiebstahl/Fahrraddiebstahl.csv 
* Data Type: CSV
* Description: Bicycle theft data from Berlin, each entry containing the timeframe in which the bike was stolen, the value of the stolen good and the location


### Datasource 2: Air Temperature in Berlin
* Metadata URL: https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/historical/stundenwerte_TU_00399_19691201_20110801_hist.zip
* Data URL: https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/historical/stundenwerte_TU_00399_19691201_20110801_hist.zip
* Data Type: TXT (csv)
* Description: Air temperature data for Berlin-Alexanderplatz, from 1970 - 2022

### Datasource 3: Precipitation in Berlin
* Metadata URL: https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/precipitation/historical/stundenwerte_RR_00399_19950901_20110801_hist.zipstundenwerte_TU_00399_19691201_20110801_hist.zip
* Data URL: https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/precipitation/historical/stundenwerte_RR_00399_19950901_20110801_hist.zip
* Data Type: TXT (csv)
* Description: Percipitation data for Berlin-Alexanderplatz, from 1970 - 2022

### (Datasource 4: Location codes for Berlin)
* to be decided if used


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Find suitable datasource and add basic project-plan.md [#1](https://github.com/luca-dot-sh/made-project/issues/1)
2. Explore datasets [#3](https://github.com/luca-dot-sh/made-project/issues/3)
3. Create data pipeline [#4](https://github.com/luca-dot-sh/made-project/issues/4)
4. Add tests for data pipeline [#5](https://github.com/luca-dot-sh/made-project/issues/5)
5. Create CI with test cases [#6](https://github.com/luca-dot-sh/made-project/issues/6)
6. Add license [#7](https://github.com/luca-dot-sh/made-project/issues/7)
7. Add report [#8](https://github.com/luca-dot-sh/made-project/issues/8)
8. Polish README.md [#9](https://github.com/luca-dot-sh/made-project/issues/9)