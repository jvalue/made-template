#!/bin/bash

echo "Running ETL Pipeline..."
bash ./pipeline.sh

echo "Running System Level Test..."
python ./test.py

echo "Running unit-test/pytest..."
pytest ./test.py
