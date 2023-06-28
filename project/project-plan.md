# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
The goal of this project is to analyze the relationship between the amount of electric charging stations available and the new registrations of electric cars in Germany.
For this we take a look at the amount of charging points overall, combining standard charging points (SCP) and fast charging points (FCP), and how they effect the new registrations of electric cars and plug-in-hybrids.
We will analyze the relationship between these two factors over time for whole germany and at a specific point in time for the different states of germany.

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
This analysis should show the relationship between electric charging stations and the new registration rate of electric cars, in order to help deciding if building more charging stations for cars would lead to a higher rate of electirc powered cars.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Charging Infrastructure
* Metadata URL: https://www.bundesnetzagentur.de/DE/Sachgebiete/ElektrizitaetundGas/Unternehmen_Institutionen/E-Mobilitaet/Ladesaeulenkarte/start.html
* Data URL: https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Energie/Unternehmen_Institutionen/E_Mobilitaet/Ladesaeuleninfrastruktur.xlsx?__blob=publicationFile
* Data Format: xlsx

Excel Sheet provided by the Bundesnetzagentur, which shows the Charging Infrastructure for Electronic Cars in Germany in numbers. 
It includes normal charging points (Normalladepunkte, NLP) and fast charging points (Schnellladepunkte, SLP).
Important for this project will be especially the sheet "4.1 Ladepunkte je BL", which shows for every german state the amount of NLPs and SLPs at a specific point in time.

### Datasource2: New Registrations of Motor Vehicles with Alternative Drive Systems
* Metadata URL: 
    * 2021: https://mobilithek.info/offers/573358207202664448
    * 2022: https://mobilithek.info/offers/573358160767496192
    * 2023: https://mobilithek.info/offers/573357313572614144
* Data Format: xlsx

**Datasource2.1: New Registrations over Time**
* Data URL: https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ28/fz28_2023_03.xlsx?__blob=publicationFile _(or newer version if available)_
    * Sheet: FZ 28.2

Excel Sheet shows the new registrations of motor vehicles with alternative drive systems for each month since January 2016.

**Datasource2.2: New Registrations by German States**
* Data URL:
    * 2021: https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ28/fz28_2021_12.xlsx?__blob=publicationFile
    * 2022: https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ28/fz28_2022_12.xlsx?__blob=publicationFile
    * Sheet: FZ 28.9

Excel Sheets show the new registrations of motor vehicles with alternative drive systems for each german state summed up over the full year for 2021 and 2022.



### Datasource3: German States with Capitals by Area, Population and Population Density
* Metadata URL: https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/02-bundeslaender.html
* Data URL: https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/02-bundeslaender.xlsx?__blob=publicationFile
* Data Format: xlsx

Excel Sheet provided by the Statistisches Bundesamt, which shows the area and population for each german state and their capital city.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Explore Datasources [#1](https://github.com/nmarkert/amse/issues/1)
2. Build an Automated Data Pipeline [#2](https://github.com/nmarkert/amse/issues/2)
3. Explore and Analyze Resulting Data [#3](https://github.com/nmarkert/amse/issues/3)
4. Add Automated Tests [#5](https://github.com/nmarkert/amse/issues/5)
5. Add Continuous Integration [#6](https://github.com/nmarkert/amse/issues/6)
6. Improve Data Pipeline [#11](https://github.com/nmarkert/amse/issues/11)
7. Report Findings [#4](https://github.com/nmarkert/amse/issues/4)
8. Refine Datasources Notebook [#9](https://github.com/nmarkert/amse/issues/9)
9. Make Repository Submission-Ready [#12](https://github.com/nmarkert/amse/issues/12) 
