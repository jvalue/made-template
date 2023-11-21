# Project Plan

## Title
Correlation between air pollution and number of vehicles with combustion motors in Nordrhein-Westfalen.

## Main Question

1. Is the number of combustion motor vehicles the main factor in air pollution in Nordrhein-Westfalen?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. "XY is an important problem, because... This projects analyzes XY, using method A. The results can give insights into..."-->

In analysis it helps to get a clear view of the amount of cars in the air pollution in the state of Nordrhein-Westfalen. This analysis also helps identify areas with a greater number of vehicles, which could potentially indicate a greater demand for services related to mechanical workshops and gasoline consumption. The resulting information may be relevant in a study that evaluates the number of vehicles a city can afford to have because high pollution can lead to a high rate of respiratory diseases.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Stock of motor vehicles by vehicle type in Nordrhein-Westfalen
* Metadata URL: https://mobilithek.info/offers/-4132669826481765343
* Data URL: https://www.landesdatenbank.nrw.de/ldbnrwws/downloader/00/tables/46251-02iz_00.csv
* Data Type: CSV

Stock of motor vehicles by motor vehicle type of cities:   Köln,   Münster, Detmold, Arnsberg, Düsseldorf

### Datasource2: Annual parameters of air pollutants in Nordrhein-Westfalen
* Metadata URL: https://www.opengeodata.nrw.de/produkte/umwelt_klima/luftqualitaet/luqs/eu_jahreskenngroessen/
* Data URL: https://www.opengeodata.nrw.de/produkte/umwelt_klima/luftqualitaet/luqs/eu_jahreskenngroessen/LUQS-EU-Kenngroessen-2022.xlsx
* Data Type: xlsx

Annual parameters of air pollutants in Nordrhein-Westfalen for 2022: Nitrogen dioxide, fine dust (PM10), fine dust (PM2.5), sulfur dioxide, benzene, lead, arsenic, cadmium, nickel, benzopyrene

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Explore Datasources [#1][i1]
2. Clean & Transform data [#2][i2]
3. Build an Automated Data Pipeline #3[i3]
4. Deploy the Tests #4
5. Explore and Analyze Resulting Data #5
6. Improve Data Pipeline #6
7. Report Findings #7
8. Write Final Report and submit #8
9. Submit the project #9

[i1]: https://github.com/JoaquinAyzanoa/made-template_ws2324/issues/6
[i2]: https://github.com/JoaquinAyzanoa/made-template_ws2324/issues/8
[i2]: https://github.com/JoaquinAyzanoa/made-template_ws2324/issues/9
