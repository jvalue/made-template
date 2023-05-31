#!/bin/bash

echo "=== Executing pipeline ==="
# Execute your pipeline
python ./data/pipeline.py

# Validate the output file(s)
if [ -f "./nuremberg_stops_immoscout.db" ]; then
  echo "Output file(s) exist."
else
  echo "Output file(s) not found."
fi

echo "=== Running Tests ==="
python test.py

read -p "Press any key to continue... " -n1 -s
