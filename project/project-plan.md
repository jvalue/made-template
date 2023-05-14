# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This project analyzes the frequency of cyclists in the Weselstraße in Münster in 2018 and 2022. The main objective would be to perform an analytical comparision between these two years to conclude about the evolution of this frequency.

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
This analysis could help the cities of münster to analyze in more detail certain neighborhoods and streets in which the number of cyclists is low or became lower. The objective would be to, for example, review the infrastructure for cyclists in these areas and possibly propose changes that could encourage the inhabitants of these streets to use their bicycles more often.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: 
* Metadata URL: https://mobilithek.info/offers/-8377471639463689219
* Data URL: 
* Data Type: CSV

### Datasource2: 
* Metadata URL: https://www.stadt-muenster.de/verkehrsplanung/verkehr-in-zahlen/radverkehrszaehlungen/weseler-strasse
* Data: 
* Data Type: CSV

There are a number of bicycle counting points in the city of Münster. The Office for Mobility and Civil Engineering provides the number of cyclists counted daily at the bicycle counting stations in the GIT repository linked here on a daily basis.

Data is updated nightly and is available at 15 minute intervals.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Extract multiple streets data into one csv files (merge) [#1][i1]
2. ...

[i1]: https://github.com/OmarFourati/2023-amse-template/issues/1
