# Exercises
During the course there were also five exercises given to work on. All of them required to build a datapipeline based on a given task and a given dataset. 
The exercises should be solved alternately [Python](https://www.python.org/) and [Jayvee](https://github.com/jvalue/jayvee). <br>
Automated Feedback to the exercises was provided using a GitHub action, which is defined in `.github/workflows/exercise-feedback.yml`

So this directory contains my solutions to the exercises. The given task descriptions are listed below together with links to the respective file.

## Exercise 1
[Link to Solution](https://github.com/nmarkert/amse/blob/main/exercises/exercise1.jv)
* Build an automated data pipeline for the following source:
    * https://mobilithek.info/offers/-8691940611911586805
    * direct link to CSV:<br>
    https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv
* Goal:
    * Write data into a SQLite database called “airports.sqlite”, in the table “airports”
    * Assign fitting built-in SQLite types (e.g., BIGINT, TEXT or FLOAT) to all columns
    * No further data validation is required, do not drop any rows or change any data points

## Exercise 2
[Link to Solution](https://github.com/nmarkert/amse/blob/main/exercises/exercise2.py)
* Build an automated data pipeline for the following source:
    * https://mobilithek.info/offers/-8739430008147831066
    * direct link to CSV:<br>
    https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV
* Goal:
    * Write data into a SQLite database called “trainstops.sqlite”, in the table “trainstops”
    * First, drop the "Status" column
    * Then, drop all rows with invalid values:
        * Valid "Verkehr" values are "FV", "RV", "nur DPN"
        * Valid "Laenge", "Breite" values are geographic coordinate system values between -90 and 90
        * Valid "IFOPT" values follow this pattern:<br>
        `<exactly two characters>:<any amount of numbers>:<any amount of numbers><optionally another colon followed by any amount of numbers>`
        * Empty cells are considered invalid
    * Use fitting SQLite types (e.g., BIGINT, TEXT or FLOAT) for all columns

## Exercise 3
[Link to Solution](https://github.com/nmarkert/amse/blob/main/exercises/exercise3.jv)
* Build an automated data pipeline for the following source:
    * Link to data offer:<br>https://mobilithek.info/offers/-655945265921899037
    * Direct download link:<br>https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv
* Goal:
    * Write data into a SQLite database called “cars.sqlite”, in the table “cars”
    * Pick suitable encoding:
        * Make sure to preserve the german special letters like “ü” or “ä”
    * Reshape data structure
        * Ignore the first 6 lines and last 4 lines as metadata
        * Keep only the following columns, rename them to the new name given here (M-BU contain summary data)
            * Column A: date
            * Column B: CIN
            * Column C: name
            * Column M: petrol
            * Column W: diesel
            * Column AG: gas
            * Column AQ: electro
            * Column BA: hybrid
            * Column BK: plugInHybrid
            * Column BU: others
        * Drop all other columns
    * Validate data
        * date/name are strings, no need to validate date
        * CINs are Community Identification Numbers, must be strings with 5 characters and can have a leading 0
        * all other columns should be positive integers > 0
        * drop all rows that contain invalid values
    * Use fitting SQLite types (e.g., BIGINT, TEXT or FLOAT) for all columns

## Exercise 4
[Link to Solution](https://github.com/nmarkert/amse/blob/main/exercises/exercise4.py)
* Build an automated data pipeline for the following source:
    * Link to data offer: <br>https://mobilithek.info/offers/526718847762190336
    * Direct download link:<br>https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip
* Goal
    * Download and unzip data
        * Use the “data.csv” in the zip file
    * Reshape data
        * Only use the columns "Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"
        * Rename "Temperatur in °C (DWD)" to "Temperatur"
        * Rename "Batterietemperatur in °C" to "Batterietemperatur"
            * There can be multiple temperature measurements per row
                * discard all columns to the right of “​​Geraet aktiv”
   * Transform data
        * Transform temperatures in Celsius to Fahrenheit (formula is (TemperatureInCelsius * 9/5) + 32) in place (keep the same column names)
            * Columns Temperatur and Batterietemperatur
    * Validate data
        * Use validations as you see fit, e.g., for Geraet to be an id over 0
    * Use fitting SQLite types (e.g., BIGINT, TEXT or FLOAT) for all columns
    * Write data into a SQLite database called “temperatures.sqlite”, in the table “temperatures”

## Exercise 5
[Link to Solution](https://github.com/nmarkert/amse/blob/main/exercises/exercise5.jv)
* Build an automated data pipeline for the following source:
    * Link to data offer:<br>https://mobilithek.info/offers/110000000002933000
    * Direct download link:<br>https://gtfs.rhoenenergie-bus.de/GTFS.zip
* Goal
    * Work with GTFS data
    * Pick out only stops (from stops.txt)
        * Only stop_id, stop_name, stop_lat, stop_lon, zone_id with fitting data types
    * Filter data
        * Only keep stops from zone 2001
    * Validate data
        * stop_name must be a text and maintain german umlauts
        * stop_lat/stop_lon must be a geographic coordinates between -90 and 90 including upper/lower bounds
        * Drop rows containing invalid data
    * Use fitting SQLite types (e.g., BIGINT, TEXT or FLOAT) for all columns
    * Write data into a SQLite database called “gtfs.sqlite”, in the table “stops”



