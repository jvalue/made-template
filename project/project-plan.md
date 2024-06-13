# Project Plan

## Title
<!-- Give your project a short title. -->
Urban Tree Management for Climate Resilience in Würzburg.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
How can urban tree data be leveraged to enhance climate resilience and improve living conditions in Würzburg?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Urban areas around the globe are facing increased environmental challenges exacerbated by climate change, including rising temperatures and deteriorating air quality. This project aims to analyze the role of urban trees in mitigating these effects in the city of Würzburg. Utilizing detailed data on tree species, sizes, and locations along with soil moisture data, the project will assess how strategic urban forestry can contribute to sustainable city planning and climate adaptation strategies. The findings will help to optimize green space planning and management in urban environments.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Baumkataster der Stadt Würzburg
* Metadata URL: [Baumkataster der Stadt Würzburg Details](https://www.govdata.de/web/guest/suchen/-/details/baumkataster-der-stadt-wurzburg)
* Data URL: [Baumkataster der Stadt Würzburg Data](https://opendata.wuerzburg.de/api/v2/catalog/datasets/baumkataster_stadt_wuerzburg/exports/csv)
* Data Type: CSV

This dataset contains information on over 40,000 public trees in Würzburg, including species, trunk circumference, height, and crown width, along with geographical coordinates.


### Datasource2: Würzburger Klimabäume - Bodenfeuchte
* Metadata URL: [Würzburger Klimabäume - Bodenfeuchte Details](https://www.govdata.de/web/guest/suchen/-/details/wurzburger-klimabaeume-bodenfeuchte)
* Data URL: [Würzburger Klimabäume - Bodenfeuchte Data](https://opendata.wuerzburg.de/api/v2/catalog/datasets/sls-klimabaeume/exports/csv)
* Data Type: CSV

Sensor data from selected trees planted in different soil types across Würzburg, tracking soil moisture to help in the creation of watering schedules and study tree health under varying urban conditions.


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Data Discovery and Preparation [#1][i1]
2. Development of an Automated Data Pipeline [#2][i2]
3. Data Report [#3][i3]
4. Implementation of Automated Tests [#4][i4]


[i1]: https://github.com/iremhalac/made-template/issues/1
[i2]: https://github.com/iremhalac/made-template/issues/2
[i3]: https://github.com/iremhalac/made-template/issues/3
[i4]: https://github.com/iremhalac/made-template/issues/4
