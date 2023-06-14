#!/bin/sh
echo "Pipeline Execution"
python pipeline.py

# Pipeline testing
echo "Pipeline testing"
python tests.py
echo "Successfully Executed"