#!/bin/bash


echo "=== Executing pipeline ==="



# Check dataset is avilable
if [ -f "./datasets.sqlite" ]; then
  echo "Dataset exist."
  

else
  echo "Dataset not exist executing pipeline to fetchand create database."
  
  # Execute pipeline
  python ./pipeline.py
  
fi

echo "=== Running Tests ==="
python test.py

read -p "Press any key to continue... " -n1 -s