# Project Plan

## Title
<!-- Give your project a short title. -->
Casualty severity in the UK vehicle accidents

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. Does the type of vehicle correlate with casualty severity?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Road safety is a global concern, demanding an understanding of factors contributing to accidents. Our focus lies on unraveling insights from road traffic accidents spanning 2009, 2015, and 2018, specifically examining how the "Type of vehicle" correlates with "Casualty severity".
This exploration seeks to inform interventions, shaping policies for enhanced road safety.


## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Road traffic accidents in the UK (2009)
* Metadata URL: https://data.europa.eu/data/datasets/road-traffic-accidents?locale=en
* Data URL: https://datamillnorth.org/download/road-traffic-accidents/288d2de3-0227-4ff0-b537-2546b712cf00/2009.csv
* Data Type: CSV

Short description of the DataSource.
The dataset contains information about road accidents in the UK in the year 2009. This dataset will be analyzed to understand how does "type of vehicles" correlate to "casualty severity".

### Datasource2: Road traffic accidents in the UK (2015)
* Metadata URL: https://data.europa.eu/data/datasets/road-traffic-accidents?locale=en
* Data URL: https://datamillnorth.org/download/road-traffic-accidents/df98a6dd-704e-46a9-9d6d-39d608987cdf/2015.csv
* Data Type: CSV

Short description of the DataSource.
The dataset contains information about road accidents in the UK in the year 2015. This dataset will be analyzed to find a correlation between the year 2009 and 2015 in terms of casualty severity.

### Datasource3: Road traffic accidents in the UK (2018)
* Metadata URL: https://data.europa.eu/data/datasets/road-traffic-accidents?locale=en
* Data URL: https://datamillnorth.org/download/road-traffic-accidents/8c100249-09c5-4aac-91c1-9c7c3656892b/RTC%25202018_Leeds.csv
* Data Type: CSV

Short description of the DataSource.
The dataset contains information about road accidents in the UK in the year 2018. This dataset will be analyzed to find a correlation between the year 2009 and 2015 in terms of casualty severity in the year 2018 and compare it to the those past years.


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Exploration: Data Cleaning: Address any missing or inconsistent values in the "type of vehicle" and "casualty severity" columns.
   Ensure consistency in vehicle type categories and casualty severity levels across the three datasets. 
2. Integration: Develop a data integration plan to combine motor type of 2009, 2015 and 2018 datasets into a unified dataset.
   Perform descriptive statistics on the "type of vehicle" and "casualty severity" variables to understand their distributions.
3. Analysis: Generate visualizations to visually represent the correlation.
   Explore how the correlation between vehicle Type of vehicle and Casualty severity has changed over the years (2009, 2015, 2018) to find any specific trends in the correlation.
4. Reporting: Summarize the key findings and insights gained from the analysis.
Reinforce the relevance of understanding the correlation between vehicle types and casualty severity for road safety.

[i1]: https://github.com/jvalue/made-template/issues/1
