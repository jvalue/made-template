#!/bin/bash
pytest project/tests/tests_system.py


# To run the tests you need kaggle credentials to pull data from kaggle.
# To do so: 
#   1. please find and copy the kaggle credentials from the link (https://docs.google.com/document/d/1J3Y7zVdyiKP4VPlxbpZy8Y1xYMefgAKLtVGs-BqZxzQ/edit?usp=sharing)
#   2. create kaggle.json in root directory with the credentials from step 1 .
#   3. run chmod +x ./project/tests.sh
#   4. run ./project/tests.sh

# I have used etl-pipeline-runner python package to build the pipeline. 
# The unit test cases of the pipeline components are written here: https://github.com/prantoamt/etl-pipeline-runner/tree/main/tests