# Project Plan

## Title
<!-- Give your project a short title. -->
MADE 23/24 - Correlation between demographic classes and the quality of life in a urban area

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
To what extent does a demographic subdivision of an urban area correlate with the general quality of life?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Health has always been a fairly extensive discussed topic and with thematically more diverse treatment of its components, sub-areas such as mental health steadily gained general awareness over the last years. With this progress in thinking about personal health, the question about the term 'quality of life' has also arisen rather frequently. Being very situation-dependent and mostly subjective, it is yet a hard to define aspect of every person's life. This project therefore aims to investigate whether there are conclusions that can be drawn out of a possible correlation between demographic strata and their respective quality of life. Therefore, different demographic aspects such as age, income, housing situation, etc. shall be examined using sample data of the city of London in the years 2012 - 2016. The results of this project can provide information about a possible dependancy of the private situation on the quality of live on individual demographic groups.


## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefix "DatasourceX" where X is the id of the datasource. -->

### Datasource1: London Borough Demographics
* Metadata URL: https://www.kaggle.com/datasets/marshald/london-boroughs/
* Data URL: https://www.kaggle.com/datasets/marshald/london-boroughs/?select=london-borough-profiles-2016+Data+set.csv
* Data Type: CSV

The datasource profiles demographic data, such as labour market, economy and so on regarding the boroughs of London in the year of 2016.

### Datasource2: Smart meters in London
* Metadata URL: https://www.kaggle.com/datasets/jeanmidev/smart-meters-in-london/
* Data URL: https://www.kaggle.com/datasets/jeanmidev/smart-meters-in-london
* Data Type: CSV

The datasource contains the energy consumption readings for a sample of about 5500 London households and information about the allocated acorn (a geodemographic segmentation of the UK's population) from between November 2011 and February 2014.

### Datasource3: London Crime Data
* Metadata URL: https://www.kaggle.com/datasets/jboysen/london-crime
* Data URL: https://www.kaggle.com/datasets/jboysen/london-crime?select=london_crime_by_lsoa.csv
* Data Type: CSV

Crime in major metropolitan areas, such as London, occurs in distinct patterns. This data covers the number of criminal reports by month, LSOA borough, and major/minor category from Jan 2008-Dec 2016.

### Datasource4: Housing in London
* Metadata URL: https://www.kaggle.com/datasets/justinas/housing-in-london
* Data URL: https://www.kaggle.com/datasets/justinas/housing-in-london?select=housing_in_london_yearly_variables.csv
* Data Type: CSV

This data contains information about the housing market of London from the years 1999 until 2019.
> The data has been extracted from London Datastore. It is released under UK Open Government License v2 and v3. The underlining datasets can be found here:
> * https://data.london.gov.uk/dataset/uk-house-price-index
> * https://data.london.gov.uk/dataset/number-and-density-of-dwellings-by-borough
> * https://data.london.gov.uk/dataset/subjective-personal-well-being-borough
> * https://data.london.gov.uk/dataset/household-waste-recycling-rates-borough
> * https://data.london.gov.uk/dataset/earnings-place-residence-borough
> * https://data.london.gov.uk/dataset/recorded_crime_summary
> * https://data.london.gov.uk/dataset/jobs-and-job-density-borough
> * https://data.london.gov.uk/dataset/ons-mid-year-population-estimates-custom-age-tables

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Retrieve data sets and set up data pipeline [#6][i6]
2. Find suitable demographic classifiers [#1][i1]
3. Define parameters to measure quality of life [#2][i2]
4. Map demographic classifiers towards the quality of life parameters [#3][i3]
5. Analyze the mappings [#4][i4]
 

[i1]: https://github.com/julian-m10/made-2324/issues/1
[i2]: https://github.com/julian-m10/made-2324/issues/2
[i3]: https://github.com/julian-m10/made-2324/issues/3
[i4]: https://github.com/julian-m10/made-2324/issues/4
[i6]: https://github.com/julian-m10/made-2324/issues/6