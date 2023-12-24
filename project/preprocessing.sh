#!/bin/bash -x

echo "**** Executing pipeline ****"

# execute pipeline python project/pipeline.py
python pipeline.py

echo "**** Extracting Latitude and Langitude of addressand storing it to database ****"

# execute data-preprocessing.py file
python data-preprocessing.py

read -p "Press any key to continue... " -n1 -s
exit 0