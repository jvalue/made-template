# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This projects analyzes the amount of cyclist in münster and the weather in münster.

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
The analysis helps determine how much the weather effects the willingness of people to use their bycicle in münster

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Verkehrszählung Fahrradverkehr: Tagesaktuelle Daten 
* Metadata URL: https://www.govdata.de/web/guest/suchen/-/details/verkehrszahlung-fahrradverkehr-daten-der-zahlstellen-munster-josefsviertel11f62
* Data URL: https://github.com/od-ms/radverkehr-zaehlstellen
* Data Type: CSV

Im Stadtgebiet Münster gibt es einige Fahrrad-Zählstellen. Das Amt für Mobilität und Tiefbau stellt die Anzahl der täglich gezählten RadfahrerInnen an den Fahrradzählstationen in dem hier verlinkten GIT-Repository tagesaktuell zur Verfügung.



Die Daten werden jede Nacht aktualisiert und liegen in 15-Minuten-Abständen vor. Die aktuellsten Daten befinden sich immer im Unterverzeichnis der entsprechenden Zählstelle in der Datei, die nach dem aktuellen Monat benannt ist. Beispiel ist “04-2021.csv” für April 2021.

### Datasource1: Historische stündliche Stationsmessungen der Lufttemperatur und Luftfeuchte für Deutschland 
* Metadata URL: https://mobilithek.info/offers/-4920664365588601619
* Data URL: https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/moisture/historical/stundenwerte_TF_01766_19891001_20221231_hist.zip
* Data Type: txt

Diese historischen Daten sind qualitätsgeprüfte Messwerte und Beobachtungen. Sie stammen aus Stationen des DWD und rechtlich und qualitativ gleichgestellten Partnernetzstationen. Umfangreiche Stationsmetadaten (Stationsverlegungen,  Instrumentenwechsel, Wechsel der Bezugszeit, Änderungen in den Algorithmen) werden mitgeliefert.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Example Issue [#1][i1]
2. ...

[i1]: https://github.com/jvalue/2023-amse-template/issues/1
