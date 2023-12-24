#!/bin/bash -x

echo "**** Executing pipeline ****"

# Execute pipeline python project/pipeline.py
python pipeline.py

read -p "Press any key to exit" -n1 -s

exit 0