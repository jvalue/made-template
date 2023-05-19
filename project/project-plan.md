# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This project analyzes or trying to find correlation between public transportation time plan and weather.

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
The analysis helps to predict future delays and cancellation. To adjust people's time for the modified schedule. 

## Datasources
### Datasource1: Mobilithek
* Metadata URL: https://www.dwd.de/EN/ourservices/cdc/cdc_ueberblick-klimadaten_en.html
* Data URL: https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/10_minutes/air_temperature/recent/
* Data Type: CSV

### Datasource2: DB-API
* Metadata URL: https://developers.deutschebahn.com/db-api-marketplace/apis/product/timetables/api/26494#/Timetables_10213/overview
* Data URL: https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1
* Data Type: API

## Work Packages

1. DB-API-handling [#5][i1]
2. Weather data processing [#6][i2]
3. Automating the API calling [#7][i3]
4. Automating weather data processing [#8][i4]
5. Analyzing/Comparing the data [#9][i5]
6. Automated tests [#10][i6]
7. CI/CD Pipeline [#11][i7]
8. Deploying [#12][i8]



[i1]: https://github.com/HassanRady/2023-amse-template/issues/5
[i2]: https://github.com/HassanRady/2023-amse-template/issues/6
[i3]: https://github.com/HassanRady/2023-amse-template/issues/7
[i4]: https://github.com/HassanRady/2023-amse-template/issues/8
[i5]: https://github.com/HassanRady/2023-amse-template/issues/9
[i6]: https://github.com/HassanRady/2023-amse-template/issues/10
[i7]: https://github.com/HassanRady/2023-amse-template/issues/11
[i8]: https://github.com/HassanRady/2023-amse-template/issues/12






