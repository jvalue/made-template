# Project Plan

## Title

The Influence of Bicycle Paths on the Use of Rental Bikes in Munich

## Main Question

Does Munich's regional bicycle infrastructure influence the use of the MVG rental bike?

## Description

The use of rental bikes or bikes in general is an important topic as the car-heavy urban transport of the past, with its high CO2 emissions, must be transformed into the climate-neutral, low-energy transportation of the future. Thus, the bicycle represents the best solution for the reduction of climate damage in the mobility sector.

This project analyzes two data sets, one about the use of rental bikes from the "Münchner Verkehrsgesellschaft mbH" (MVG, Munich Transport Company) and the other about bicycle paths in Munich from the "Baureferat der Landeshauptstadt München" (Building Department of the City of Munich).

The existing data sets should first be stored in a database and then enriched with additional geographical data, i.e. the potential paths from start to end point. Finally, the enriched data will be analyzed, explained and visualized in the report. Some potential measures used for the analytical part could be:
- The use frequency of existing bicycle lanes and/or bicycle paths by MVG bikes
- The share of bicycle lanes/bikeways in the distance traveled per use and/or in total (Den Anteil der Fahrradstraßen/Fahrradwege an der zurückgelegten Strecke pro Nutzung und/oder insgesamt)

The results of this project work could provide insights into the interplay between urban bicycle infrastructure and the use of rental bike services in large cities as Munich, using "MVG Rad" (MVG bike) as an example.

## Datasources

### Datasource1: Fahrten mit dem MVG-Rad
* Metadata URL: https://opendata.muenchen.de/dataset/fahrten-mit-dem-mvg-rad and https://www.mvg.de/services/mvg-rad.html
* Data URL: https://www.mvg.de/dam/mvg/services/mobile-services/mvg-rad/fahrten-csv/MVG_Rad_Fahrten_2022.zip
* Data Type: ZIP/CSV (unzipped)

This dataset contains 709145 entries about trips with the MVG bike in 2022 described by id, start-time, end-time, start-latitude & -longitude, end-latitude & -longitude, rental-is-station (bool), rental-station-name (optional), return-is-station (bool), and return-station-name (optional).

### Datasource2: Radverkehrsanlagen im Straßenunterhalt der Landeshauptstadt München
* Metadata URL: https://opendata.muenchen.de/dataset/radverkehrsanlagen-im-strassenunterhalt-der-landeshauptstadt-muenchen
* Data URL: https://opendata.muenchen.de/dataset/7ad3bc6c-4c1a-4a63-9cb2-0d613f5b69fa/resource/14977232-94f3-4cdb-94fc-1e709698ba3f/download/radwege_t2.csv
* Data Type: CSV

This dataset contains 21173 entries about cycling facilities in Munich described by id, name, shape-length, type, start-x-y-coordinates, and end-x-y-coordinates. Additionally, there is a shape dataset which could provide further information about the exact path shapes.

## Work Packages

1. [Milestone WP1](https://github.com/M-HRL/made/milestone/1): Data acquisition and preprocessing
	- Load the data into a database [i1](https://github.com/M-HRL/made/issues/1)
	- Clean the data [i2](https://github.com/M-HRL/made/issues/2)
	- Perform some exploratory data analysis [i3](https://github.com/M-HRL/made/issues/3)
2. [Milestone WP2](https://github.com/M-HRL/made/milestone/2): Data enrichment and feature engineering
	- Obtain the potential paths from start to end point of each trip [i4](https://github.com/M-HRL/made/issues/4)
	- Combine the two datasets [i5](https://github.com/M-HRL/made/issues/5)
	- Calculate some additional features [i6](https://github.com/M-HRL/made/issues/6)
3. [Milestone WP3](https://github.com/M-HRL/made/milestone/3): Data analysis and visualization
	- Formulate some hypotheses based on the main question [i7](https://github.com/M-HRL/made/issues/7)
	- Test the hypotheses using appropriate statistical methods [i8](https://github.com/M-HRL/made/issues/8)
	- Visualize the results using plots and charts [i9](https://github.com/M-HRL/made/issues/9)
	- Interpret the results and answer the main question [i10](https://github.com/M-HRL/made/issues/10)
4. [Milestone WP4](https://github.com/M-HRL/made/milestone/4): Report writing (and presentation)
	- Write the report [i11](https://github.com/M-HRL/made/issues/11)
	- Present the report [i12](https://github.com/M-HRL/made/issues/12)
