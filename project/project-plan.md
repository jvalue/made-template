# Project Plan

## Visual Analysis of the Number of Law Enforcement Officers and the Number of Crimes in California, the U.S. 
<!-- Give your project a short title. -->
The project uses data from the FBI's Uniform Crime Reporting program to visualize and analyze the number of law enforcement officers and the number of crimes in various cities in California.


## Main Question
<!-- Think about one main question you want to answer based on the data. -->

1. Do all California cities have the same ratio of the number of law enforcement officers to the number of crimes in that city? Or is the number of law enforcement officers greater in some cities?
2. What are the most common types of crimes in California? Are there certain crimes that are more common in a city compared to the rest of the state? If there are, what's the most common crime in each city?

## Description
<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->

This project visualizes and analyzes the number of law enforcement officers, the number of crimes, the types of crimes, and the rates of crimes in various cities in California using data provided by the FBI. The safety of a city has an important impact on the quality of life of its inhabitants, economic development and social stability. The number of law enforcement officers and the crime rate of a city are important factors in considering the security of a city. Exploring the above issues through tableau, python, or jayvee on data released by the FBI will not only reveal differences in public safety resource allocation and crime types across cities, but also provide recommendations for policy development, law enforcement efficiency improvement, public safety awareness, and the feasibility of people moving to California cities.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: ca_law_enforcement_by_city, 2015
* Metadata URL: https://ucr.fbi.gov/crime-in-the-u.s/2015/crime-in-the-u.s.-2015/resource-pages/downloads/download-printable-files
* Data URL: https://www.kaggle.com/datasets/fbi-us/california-crime?select=ca_law_enforcement_by_city.csv
* License: us-pd
* Data Type: CSV

This dataset is published by the Federal Bureau of Investigation's (FBI) Uniform Crime Reporting (UCR) program. This dataset shows the data of Law Enforcement Officers in California Cities.

### Datasource2: ca_offenses_by_city, 2015
* Metadata URL: https://ucr.fbi.gov/crime-in-the-u.s/2015/crime-in-the-u.s.-2015/resource-pages/downloads/download-printable-files
* Data URL: https://www.kaggle.com/datasets/fbi-us/california-crime?select=ca_offenses_by_city.csv
* License: us-pd
* Data Type: CSV

This dataset is published by the Federal Bureau of Investigation's (FBI) Uniform Crime Reporting (UCR) program. This dataset shows the reported Crime in California Cities. Categories of crimes reported include violent crime, murder and nonnegligent manslaughter, rape, robbery, aggravated assault, property crime, burglary, larceny-theft, motor vehicle damage, and arson. 

## Work Packages
<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Data Conversion & Cleaning [#1][i1]
2. Solutions & Data Analysis [#2][i2]
3. Data Visualization [#3][i3]
4. Final Report & Presentation [#4][i3]

[i1]: https://github.com/jvalue/made-template/issues/123
[i2]: https://github.com/jvalue/made-template/issues/128
[i3]: https://github.com/jvalue/made-template/issues/129
