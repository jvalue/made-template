# Project Plan

## Title
<!-- Give your project a short title. -->
CO2 emissions and heath status across countries in the EU.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. How do CO2 emission impact the heath condition of the EU nations?
2. Which EU countries experience 
3. How do the CO2 emission values of the EU countries change over time?
4. How does heath status of the EU population change over time?
5. What are the main deseaes that are present in the high CO2 emission EU countries?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Heath condition of the population is one of the most important determinats of the economy, pruductivity and prosperity of a population. Among other factors influencing the heath status are nutrition, individual genetics and teh environment. This project focuses on the air quality in particular CO2 emission values as the main proxy of the environmental status of a country. In this project the CO2 emission values and heath condition values (healthy life years, causes of death, cases of the respiratory system deseases) are being analyzed using an ETL pipeline in Jayvee. The results can give insights into the CO2 emission and health-related issues and respective policy making. 

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Heath Dataset EU
* Metadata URL: https://ec.europa.eu/eurostat/cache/metadata/en/hlth_hlye_esms.htm#data_rev1715803061964
* Data URL: https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/hlth_hlye$defaultview/?format=SDMX-CSV&compressed=true
* Data Type: CSV

The indicator of healthy life years (HLY) measures the number of remaining years that a person of specific age is expected to live without any severe or moderate health problems. The notion of health problem for Eurostat's HLY is reflecting a disability dimension and is based on a self-perceived question which aims to measure the extent of any limitations, for at least six months, because of a health problem that may have affected respondents as regards activities they usually do (the so-called GALI - Global Activity Limitation Instrument foreseen in the annual EU-SILC survey). The indicator is therefor also called disability-free life expectancy (DFLE). So, HLY is a composite indicator that combines mortality data with health status data.

### Datasource2: ExampleSource
* Metadata URL: https://ec.europa.eu/eurostat/cache/metadata/en/sdg_13_10_esmsip2.htm
* Data URL: https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/sdg_13_10/?format=SDMX-CSV&compressed=true
* Data Type: CSV

The indicator measures total national emissions (from both ESD and ETS sectors) including international aviation of the so called ‘Kyoto basket’ of greenhouse gases, including carbon dioxide (CO2), methane (CH4), nitrous oxide (N2O), and the so-called F-gases (hydrofluorocarbons, perfluorocarbons, nitrogen triflouride (NF3) and sulphur hexafluoride (SF6)) from all sectors of the GHG emission inventories (including international aviation and indirect CO2). The indicator is presented in two forms: as net emissions including land use, land use change and forestry (LULUCF) as well as excluding LULUCF. Using each gas’ individual global warming potential (GWP), they are being integrated into a single indicator expressed in units of CO2 equivalents. The GHG emission inventories are submitted annually by the EU Member States to the United Nations Framework Convention on Climate Change (UNFCCC).

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Research on the topic and investigate available data [#1][i1]
2. Download data and set up a pipeline on Jayvee [#2][i2]
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
