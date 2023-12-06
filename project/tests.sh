#!/bin/bash
echo RUNNING
# Execute the data pipeline
python -m script.py

data_file="C:\Users\Impana\OneDrive\Desktop\MAde_project\project\data\my_database_db"


# Check if the output file exists
if [ -f "$data_file" ]; then
    echo "Yes! Output file $data_file is available."
else
    echo "No! Output file $data_file is not available."
fi
