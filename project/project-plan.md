# Project Plan

## Title
<!-- Give your project a short title. -->
Energy consumption as driver of greenhouse gas emissions and the influence of renewables.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. How does the amount of energy consumed influence the net greenhouse gas emissions of European countries?
2. And how is this influenced by the share of renewables in total energy?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
-

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Net greenhouse gas emissions
* Metadata URL: https://ec.europa.eu/eurostat/databrowser/view/sdg_13_10/default/table
* Data URL: https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/sdg_13_10/?format=SDMX-CSV&i
* Data Type: SDMX-CSV 1.0
* Source of Data: [Eurostat](https://ec.europa.eu/eurostat/databrowser/view/sdg_13_10/default/table)
* License: [Open Data License](https://ec.europa.eu/eurostat/about-us/policies/copyright)

Net greenhouse gas emissions for all countries in the european union either relative to 1990 or as tonnes per capita.

### Datasource2: Primary energy consumption
* Metadata URL: https://ec.europa.eu/eurostat/databrowser/view/sdg_07_10/default/table
* Data URL: https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/sdg_07_10/?format=SDMX-CSV&i
* Data Type: SDMX-CSV 1.0
* Source of Data: [Eurostat](https://ec.europa.eu/eurostat/databrowser/view/sdg_07_10/default/table)
* License: [Open Data License](https://ec.europa.eu/eurostat/about-us/policies/copyright)

Energy consumption of end users like households or industry and the energy consumption of the energy sector itself, accounting for energy transformation costs.
The data is available for all countries of the european union.
Data is measured either as million tonnes of oil equivalent, relative to 2005 or as tonnes of oil equivalent per capita.

### Datasource3: Share of energy from renewable sources
* Metadata URL: https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table
* Data URL: https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/nrg_ind_ren/?format=SDMX-CSV&i
* Data Type: SDMX-CSV 1.0
* Source of Data: [Eurostat](https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table)
* License: [Open Data License](https://ec.europa.eu/eurostat/about-us/policies/copyright)

The share of energy generated from renewable sources as declared by the european union. The data is available for all countries of the european union and is measured in percentages.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Write Automated Data Pipeline [#1][i1]
2. Analyze Data Sources [#2][i2]
3. Clean Data [#3][i3]
4. Analyze Cleaned Data [#4][i4]
5. Write Data Report [#5][i5]
6. Add Automated Test Cases [#6][i6]
7. Add Continous Integration [#7][i7]
8. Write Final Report [#8][i8]
9. Make Repository Presentable [#9][i9]
10. Project Presentation [#10][i10]

[i1]: -
