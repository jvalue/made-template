#!/bin/bash -x

echo "=== Executing pipeline ==="

# Execute your pipeline python project/pipeline.py
python pipeline.py


read -p "Press any key to continue... " -n1 -s
exit 0