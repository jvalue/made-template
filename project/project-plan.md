# Project Plan

## Title
<!-- Give your project a short title. -->
Correlation analysis between newly registered cars and Greenhouse gas emissions in the European Union.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
Is the type of car engine a significant factor contributing to climate change? What other vehicle features play a crucial role in influencing it?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
*Greenhouse gas emissions from transport account for 25% of the total EU greenhouse gas emissions. In order to achieve climate neutrality by 2050, as specified in the European Green Deal, there is a target to reduce greenhouse gas emissions from the transport sector by 90%.*[^r1]

The goal is to explore the latest Passenger cars[^r2], with a particular focus on engine-related features. We can further refine our research by focusing on specific regions to determine if the same pattern emerges. Depending on the results, we can then consider exploring more databases to enhance our analysis if we find the correlation we are seeking.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasourcet1:  Europa(Average CO2 emissions per km from new passenger cars)
* Metadata URL: https://ec.europa.eu/eurostat/cache/metadata/en/sdg_12_30_esmsip2.htm
* Data URL: https://ec.europa.eu/eurostat/databrowser/view/sdg_12_30__custom_8320511/default/table?lang=en
* Data Type: CSV

The indicator is defined as the average carbon dioxide (CO2) emissions per km by new passenger cars in a given year. The reported emissions are based on type-approval and can deviate from the actual CO2 emissions of new cars. Since 2021, the emissions are measured with a new test procedure (Worldwide harmonized Light vehicles Test Procedure WLTP), compared to the New European Driving Cycle (NEDC) procedure used until 2020. The WLTP aims to reflect better real driving conditions and WLTP values are systematically higher than NEDC values. This change leads to a break in time series between 2020 and 2021.

### Datasourcet2:  Europa(Stock of vehicles by category and NUTS 2 regions)
* Metadata URL: https://ec.europa.eu/eurostat/cache/metadata/en/tran_r_esms.htm
* Data URL: https://ec.europa.eu/eurostat/databrowser/view/tran_r_vehst__custom_8319538/default/table?lang=en
* Data Type: CSV

Due to the nature of transport, a spatial reference is built into most legal acts dealing with transport statistics. In a few cases, these sources can be directly used for the derivation of regional transport indicators, while other indicators are collected on a voluntary basis. This is the case of the regional transport data collection in which both data types are used.

Three types of regional data can be distinguished depending on their source: two are based on data collections performed on the basis of legal acts (the Maritime and Aviation data) and one is a voluntary data collection (infrastructures, vehicles and road accidents).

### Datasourcet3:  Europa(New passenger cars by type of motor energy)
* Metadata URL: https://ec.europa.eu/eurostat/cache/metadata/en/rail_if_esms.htm
* Data URL: https://ec.europa.eu/eurostat/databrowser/view/road_eqr_carpda__custom_8320321/default/table?lang=en
* Data Type: CSV

The data in this dataset comes from the Common Questionnaire for Transport Statistics, developed and surveyed by Eurostat in cooperation between the United Nations Economic Commission for Europe (UNECE) and the International Transport Forum (ITF) at OECD.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

- Week 02
- 1. - [x] [Project needs at least two open data source][i2]
- 2. - [x] [Project can cover next exercises][i3]

[i2]: https://github.com/jvalue/made-template/issues/2
[i3]: https://github.com/jvalue/made-template/issues/3

## References and footnotes

[^r3]: EC, 2021, Communication from the Commission to the European Parliament, the Council, the European Economic and Social Committee and the Committee of the Regions ‘Fit for 55’: delivering the EU’s 2030 Climate Target on the way to climate neutrality, COM(2021) 550 final

[^r2]: [Glossary:Passenger_car](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Passenger_car)
