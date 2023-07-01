## Project Title: Electrifying Germany: Visualizing the Spatial Distribution of EV Charging Stations 

# Project Plan

## Summary

The main purpose of this project is to combine the charging station registration information with geospatial data to provide a thorough visualisation of the distribution of electric vehicle (EV) charging stations across different areas in Germany. The study's goal is to give insights on the existing EV charging infrastructure and its spatial distribution, allowing for a better understanding of the present level of EV adoption as well as prospective areas for development in terms of carbon emissions reduction.

## Rationale

Adoption of electric vehicles is viewed as a critical approach to reducing carbon emissions and combating climate change. The accessibility and availability of EV charging infrastructure is critical in increasing EV adoption. This study can provide significant information to policymakers and industry stakeholders by visualising the spatial distribution of charging stations in Germany. It can assist in identifying locations with inadequate charging infrastructure and informing strategic decisions to enhance sustainable transportation and successfully cut carbon emissions.

## Datasources


### Datasource 1: E-charging station register
* Metadata URL: https://mobilithek.info/offers/-2413665570381145802
* Data URL: https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebieten/Energie/Unternahmen_Institutionen/E_Mobilitaet/Ladesaeulenregister.xlsx%3f__blob%3dpublicationFile%26v%3d21
* Data Type: XLSX

Description : It provides data on publicly accessible charging infrastructure in Germany reported under the Charging Station Ordinance .

### Datasource 2 : Geographic distribution of charging stations
* Data URL: https://openchargemap.org/site
* Data Access Method: Through API
* Data Type: CSV

Description : OpenChargeMap is an open-source platform that provides information about electric vehicle charging stations worldwide. It allows users to access data on the location, availability, and types of charging stations.


## Work Packages

1. Set up data ingestion pipeline [i1]
2. Implement data transformation logic[i2]
3. Build data modeling and storage infrastructure. [i3]
4. Implement data quality checks and monitoring . [i4]
5. Exploratory Data Analysis. [i5]
6. Visualization and Reporting. [i6] 

[i1]: https://github.com/diganto-deb/2023-AMSE/issues/1
[i2]: https://github.com/diganto-deb/2023-AMSE/issues/2
[i3]: https://github.com/diganto-deb/2023-AMSE/issues/3
[i4]: https://github.com/diganto-deb/2023-AMSE/issues/4
[i5]: https://github.com/diganto-deb/2023-AMSE/issues/5
[i6]: https://github.com/diganto-deb/2023-AMSE/issues/6
