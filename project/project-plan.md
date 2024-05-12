# Project Plan

## Title
<!-- Give your project a short title. -->
Effects of the EU Emissions Trading System (EU ETS) on emissions in Europe and worldwide.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
How significant is the impact of the EU Emissions Trading System (EU ETS) in the sectors it sanctions and to what degree does that make an impact on global emissions.

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Reducing emissions is a critical step towards slowing down the effects of climate change. To tackle this issue, many countries are planning and have already enforced emissions trading systems. Such trading systems set a price on the emission of CO2e to motivate producers and consumers of CO2e emitting products to reduce their carbon footprint. As these trading systems market themselves by claiming to reduce emissions, this trend should be visible when analyzing the data they present. One system that makes sense to analyze is the EU Emissions Trading System (EU ETS) as it exists the longest (since 2005) and also offers detailed information on emissions in the EU. The goal of this project is thus to assess the significance of the EU ETS in reducing emissions inside of the EU by processing its European Union Transaction Log. Additionally the question of how much and how efficiently it impacts emissions on a global scale should be answered. Finally, answering these questions should help motivate having more and stricter emissions trading systems worldwide to help slow down climate change.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: European Union Transaction Log
* Metadata URL: https://climate.ec.europa.eu/eu-action/eu-emissions-trading-system-eu-ets/union-registry_en
* Data URL: https://climate.ec.europa.eu/document/download/ebb2c20e-8737-4a73-b6ba-a4b7e78ecc01_en?filename=verified_emissions_2023_en_1.xlsx
* Data Type: CSV/XLSX

Datasource1 contains data on the allocated emission allowances and actual verified emissions from 2008 to 2022 of operators that are part of the EU ETS. 

### Datasource2: Operators in the EU ETS
* Metadata URL: https://climate.ec.europa.eu/eu-action/eu-emissions-trading-system-eu-ets/union-registry_en
* Data URL: https://climate.ec.europa.eu/document/download/ab2c1214-decb-40bc-bb0d-d37f080bdebd_en?filename=policy_ets_registry_operators_ets_en.xlsx
* Data Type: CSV/XLSX

Datasource2 contains detailed information about the EU ETS operators listed in the European Union Transaction Log.

### Datasource3: CO2e Price Development in the EU ETS
* Metadata URL: https://www.umweltbundesamt.de/daten/klima/der-europaeische-emissionshandel#teilnehmer-prinzip-und-umsetzung-des-europaischen-emissionshandels
* Data URL: https://www.umweltbundesamt.de/sites/default/files/medien/384/bilder/dateien/2_abb_preisentwick-emissionsber-eua_2023-11-23.xlsx
* Data Type: CSV/XLSX

Datasource3 contains data on the development of the price on CO2e in the EU ETS since 2008.

### Datasource4: Global GHG Emissions
* Metadata URL: https://edgar.jrc.ec.europa.eu/report_2023
* Data URL: https://edgar.jrc.ec.europa.eu/booklet/EDGARv8.0_FT2022_GHG_booklet_2023.xlsx
* Data Type: CSV/XLSX

Datasource4 contains data on the greenhouse gas emissions of all world countries from 1970 up until 2022.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Write data pipelines to clean and store all datasets [#1][i1]
2. Combine datasets 1 and 2 (EU ETS) [#2][i2]
3. Write a data report to document the improvements on the datasets [#3][i3]
4. Analyze the EU ETS datasets in conjunction with the CO2e price development dataset [#4][i4]
5. Put emission reducing efforts of the EU into relation with global emissions [#5][i5]
6. Write a project report on the results of the data analysis [#6][i6]

[i1]: https://github.com/stefanpfahler/made-template/issues/3
[i2]: https://github.com/stefanpfahler/made-template/issues/4
[i3]: https://github.com/stefanpfahler/made-template/issues/5
[i4]: https://github.com/stefanpfahler/made-template/issues/6
[i5]: https://github.com/stefanpfahler/made-template/issues/7
[i6]: https://github.com/stefanpfahler/made-template/issues/8