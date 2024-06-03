# Project Plan

## Title
<!-- Give your project a short title. -->
The link between health status and net greenhouse gas emissions in the EU: a cross-country analysis.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. How do net greenhouse gas emissions influence the health status of EU countries?
2. Which EU countries exhibit the highest levels of greenhouse gas emissions?
3. How do net greenhouse gas emission values of the EU countries change over time?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Health condition of the population is one of the most important determinants of the economy, productivity, and prosperity of a population. Among other factors influencing health status are nutrition, individual genetics, and the environment. This project focuses on air quality, specifically net greenhouse gas emission values, as the main proxy for the environmental status of a country. In this project, greenhouse gas emission values and health condition values (measured as healthy life years) are analyzed using an ETL pipeline in Python. The results can provide insights into the relationship between greenhouse gas emissions and the health state of the different countries of the EU, contributing to the future policy making and public health strategies.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Heathy life years
* Metadata URL: https://ec.europa.eu/eurostat/cache/metadata/en/hlth_hlye_esms.htm#data_rev1715803061964
* Data URL: https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/hlth_hlye$defaultview/?format=SDMX-CSV&compressed=true
* Data Type: CSV

The healthy life years (HLY) is an expectancy indicator that measures how many years a person of a certain age is expected to live without severe or moderate health problems. Health expectancies use the Sullivan method, which combines mortality and health status data. Mortality data includes age-specific death rates, probabilities of dying and surviving, the number left alive at a given age, person-years lived, and life expectancy. Health status is measured using the PH030 variable from the EU-SILC Survey, which asks about limitations in daily activities due to health problems for at least the last six months. Responses are categorized as severely limited, limited but not severely, or not limited at all. Proportions of healthy and unhealthy individuals are then calculated by sex and age.

### Datasource2: Net greenhouse gas emissions
* Metadata URL: https://ec.europa.eu/eurostat/cache/metadata/en/sdg_13_10_esmsip2.htm
* Data URL: https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/sdg_13_10/?format=SDMX-CSV&compressed=true
* Data Type: CSV

The indicator measures national greenhouse gas emissions, including international aviation, covering CO2, CH4, N2O, and F-gases (hydrofluorocarbons, perfluorocarbons, NF3, and SF6) from all sectors. It is presented as net emissions including land use, land use change, and forestry (LULUCF). Each gas's emissions are converted to CO2 equivalents using their global warming potential (GWP). 

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Research on the topic and investigate available data [#1][i1]
2. Download data and set up a pipeline in Python [#2][i2]

3. Explore data [#3][i3]
4. Clean and modify data [#4][i4]
5. Evaluate data on the research questions [#5][i5]
6. Write final report [#6][i6]

[i1]: https://github.com/segalanastasiia/made-template/issues/1
[i2]: https://github.com/segalanastasiia/made-template/issues/2
[i3]: https://github.com/segalanastasiia/made-template/issues/3
[i4]: https://github.com/segalanastasiia/made-template/issues/4
[i5]: https://github.com/segalanastasiia/made-template/issues/5
[i6]: https://github.com/segalanastasiia/made-template/issues/6
