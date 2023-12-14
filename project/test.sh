#!/bin/bash


echo "=== Executing pipeline ==="

# Execute pipeline
python project/pipeline.py
  
# Check dataset is avilable
if [ -f "./datasets.sqlite" ]; then
  echo "Dataset exist."
else
  echo "Dataset not exist executing pipeline to fetchand create database."
fi

echo "=== Running Tests ==="

#Execute testcase
python project/test.py

read -p "Press any key to continue... " -n1 -s