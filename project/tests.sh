#!/bin/bash

cd ../data/
# Test 1: System-level test
echo "Running system-level test..."
python extract_mbi_data.py
python extract-OpenChargerMap.py
##python store_to_database.py

# Validate output files
if [ -f "./data/mobi_data.csv" ]; then
    echo "CSV file 'mobi_data.csv' created successfully."
else
    echo "Error: Failed to create CSV file 'mobi_data.csv'."
fi

if [ -f "./data/EV_Charging_Points_Germany.csv" ]; then
    echo "CSV file 'EV_Charging_Points_Germany.csv' created successfully."
else
    echo "Error: Failed to create CSV file 'EV_Charging_Points_Germany.csv'."
fi

#if [ -f "./data/data.db" ]; then
 #   echo "SQLite database 'data.db' created successfully."
#else
 #   echo "Error: Failed to create SQLite database 'data.db'."
#fi

python -m unittest discover -s project.tests -p "*_UnitTest.py"
