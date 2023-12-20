#! /bin/bash
#PYTHON=python3.8
# Run system tests
echo "----------------------------------- System Level Testing Started -----------------------------------"
python -m unittest tests/pipelinetest.py
echo "----------------------------------- System Level Testing Ended -----------------------------------"
