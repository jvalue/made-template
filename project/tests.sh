#!/bin/bash

# # Export kaggle.json to os env for Kaggle authentication
# KAGGLE_JSON_PATH="./project/kaggle.json"
# KAGGLE_CONFIG_DIR=$(dirname "$KAGGLE_JSON_PATH")
# export KAGGLE_CONFIG_DIR

# Install required packages from requirements.txt
pip install --upgrade pip
pip install -r ./project/requirements.txt

# Run your Python file
pytest ./project/test_pipeline.py