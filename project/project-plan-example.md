# Project Plan

## A visual inspection of Regional Economic Trends: North America & Latin America Analysis
<!-- Give your project a short title. -->
This analysis utilizes the International Renewable Energy Agency (IRENA) dataset to carry out a comprehensive visual inspection of the energy deployment across the Americas. Some of the key aspects that will be covered are: Costs, Energy Transition, Capacity and Generation and Investment trends.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
* How have economic indicators (such as GDP, poverty rate, or education level) evolved over time across different countries in North America and Latin America & the Caribbean, and what trends or patterns can be identified in their development?



## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
For this project, I am working on integrating and analyzing global economic and development indicators from the World Bank for different regions. The goal is to clean, merge, and store these indicators in an SQLite database to facilitate future analysis. The project begins by downloading raw CSV files containing economic data as well as many indicators for North America and Latin America & the Caribbean. These files are then extracted from compressed archives, cleaned by removing unnecessary columns, and merged with metadata that provides descriptions for each indicator. The data is then transformed to match a predefined schema with columns for country names, indicator codes, and values for each year from 1960 to 2023 and stored in two tables 'LCN' and 'NAC' of the world_data.sqlite database.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

#### Datasource 1: North America Economic Data [World Bank](https://data.worldbank.org/region/north-america?view=chart)
This dataset contains various economic and development indicators for countries in North America, including the United States, Canada, and Mexico. It includes data on GDP, poverty rates, education, healthcare, and other socio-economic indicators over time (from 1960 to 2023). The data is provided by the World Bank in CSV format and will be used to examine the economic development and trends in the North American region. The source is available for download through a World Bank API, which delivers the data in a zip file.

#### Datasource 2: Latin America & Caribbean Economic Data [World Bank]( https://data.worldbank.org/region/latin-america-and-caribbean?view=chart)
Similar to the North American dataset, this dataset provides economic and development indicators for countries in Latin America and the Caribbean. It includes a wide range of data on economic growth, social development, and health metrics. The dataset spans the years 1960 to 2023 and will be used to analyze trends in economic and social development for the Latin American and Caribbean region. The data is also provided in CSV format and can be accessed through the World Bank API in a compressed zip file. [World bank Website](https://data.worldbank.org/)

### Datasource: World Bank Dataset
* Metadata URL: https://data.worldbank.org/country
* Data source 1: https://data.worldbank.org/region/north-america?view=chart
* Data source 2: https://data.worldbank.org/region/latin-america-and-caribbean?view=chart
* Data Type: csv

### License
[Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets)



## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

- [x] Data Collection and Cleaning [#1][i1]
- [] Exploratory Data Analysis [#2][i1]
- [] Visualization Development [#3][i1]
- [] Comparision of Investment Trends [#4][i1]
- [] Final Report and Presentation [#5][i1]

[i1]: https://github.com/jvalue/made-template/issues/1
