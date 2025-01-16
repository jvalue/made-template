#!/bin/bash

# Set paths for input and output data
OUTPUT_FILE1="data/los_angeles_data_portal.sqlite"
OUTPUT_FILE2="data/meteostat.sqlite"

# Run the pipeline using the virtual environment's Python binary
echo "Executing pipeline.py..."
python3 project/pipeline.py

# Validate the pipeline execution
if [ $? -ne 0 ]; then
    echo "Pipeline execution failed!"
    exit 1
fi

# Validate that the output files were created
echo "Checking if output files exist..."
if [ -f "$OUTPUT_FILE1" ]; then
    echo "Output file $OUTPUT_FILE1 exists."
else
    echo "Test failed: Output file $OUTPUT_FILE1 is missing."
    exit 1
fi

if [ -f "$OUTPUT_FILE2" ]; then
    echo "Output file $OUTPUT_FILE2 exists."
else
    echo "Test failed: Output file $OUTPUT_FILE2 is missing."
    exit 1
fi

# Validate database tables in los_angeles_data_portal.sqlite
echo "Checking database tables in $OUTPUT_FILE1..."
TABLES1=$(sqlite3 "$OUTPUT_FILE1" ".tables")
EXPECTED_TABLE1="los_angeles_data_portal"
echo "$TABLES1" | grep -qi "$EXPECTED_TABLE1"
if [ $? -eq 0 ]; then
    echo "Test passed: '$EXPECTED_TABLE1' table exists in $OUTPUT_FILE1."
else
    echo "Test failed: '$EXPECTED_TABLE1' table is missing in $OUTPUT_FILE1."
    exit 1
fi

# Validate database tables in meteostat.sqlite
echo "Checking database tables in $OUTPUT_FILE2..."
TABLES2=$(sqlite3 "$OUTPUT_FILE2" ".tables")
EXPECTED_TABLE2="meteostat"
echo "$TABLES2" | grep -qi "$EXPECTED_TABLE2"
if [ $? -eq 0 ]; then
    echo "Test passed: '$EXPECTED_TABLE2' table exists in $OUTPUT_FILE2."
else
    echo "Test failed: '$EXPECTED_TABLE2' table is missing in $OUTPUT_FILE2."
    exit 1
fi

echo "All tests passed successfully."