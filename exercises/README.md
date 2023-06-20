# Exercises

## Exercise 1
* Build an automated data pipeline for the following source:
    * https://mobilithek.info/offers/-8691940611911586805
    * direct link to CSV:<br>
    https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv
* Goal:
    * Write data into a SQLite database called “airports.sqlite”, in the table “airports”
    * Assign fitting built-in SQLite types (e.g., BIGINT, TEXT or FLOAT) to all columns
    * No further data validation is required, do not drop any rows or change any data points

## Exercise 2
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

