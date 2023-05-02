# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This projects analyzes the relationship between the amount of electirc charging stations available and the new registrations of electirc cars in Germany.
For this, we take a look at the development over time and the situations at different german states.

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
The analysis can help to decide if building more electirc charging stations would lead to a higher new registartion rate of electric cars.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Charging Infrastructure
* Metadata URL: https://www.bundesnetzagentur.de/DE/Sachgebiete/ElektrizitaetundGas/Unternehmen_Institutionen/E-Mobilitaet/Ladesaeulenkarte/start.html
* Data URL: https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Energie/Unternehmen_Institutionen/E_Mobilitaet/Ladesaeuleninfrastruktur.xlsx?__blob=publicationFile
* Data Format: xlsx

Excel Sheet provided by the Bundesnetzagentur, which shows the Charging Infrastructure for Electronic Cars in Germany in numbers. 
It includes normal charging points (Normalladepunkte, NLP) and fast charging points (Schnellladepunkte, SLP).
Important for this project will be especially the sheet "4.1 Ladepunkte je BL", which shows for every german state the amount of NLPs and SLPs at a specific point in time.

### Datasource2: New registrations of motor vehicles with alternative drive systems
* Metadata URL: https://mobilithek.info/offers/573358160767496192
* Data URL: https://www.kba.de/DE/Statistik/Fahrzeuge/Neuzulassungen/Umwelt/n_umwelt_node.html
    * e.g. for January 2022: https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ28/fz28_2022_01.xlsx?__blob=publicationFile
* Data Format: xlsx

Excel Sheets provided for every Month by the Kraftfahrt-Bundesamt, which shows the new registrations of motor vehicles with alternative drive systems. 
Important for this project will be especially the sheets "FZ 28.2", which shows the new registration numbers for each month since 2016 and "FZ 28.9", which shows the new registrations for a specific month categorized by the corresponding state

### Datasource3: German states with capitals by area, population and population density
* Metadata URL: https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/02-bundeslaender.html
* Data URL: https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/02-bundeslaender.xlsx?__blob=publicationFile
* Data Format: xlsx

Excel Sheet provided by the Statistisches Bundesamt, which shows the area and population for each german state and their capital city.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Explore Datasources [#1](https://github.com/nmarkert/amse/issues/1)
2. Build an Automated Data Pipeline [#2](https://github.com/nmarkert/amse/issues/2)
3. Explore and Analyze resulting Data [#3](https://github.com/nmarkert/amse/issues/3)
4. Report Findings [#4](https://github.com/nmarkert/amse/issues/4)
5. Add Automated Tests [#5](https://github.com/nmarkert/amse/issues/5)
6. Add Continuous Integration [#6](https://github.com/nmarkert/amse/issues/6)
7. Deploy using GitHub Pages [#7](https://github.com/nmarkert/amse/issues/7)
