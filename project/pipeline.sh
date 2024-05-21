#!/bin/bash
touch ./data/data.sqlite
python3 -m pip install -r ./project/requirements.txt
python3 ./project/pipeline.py