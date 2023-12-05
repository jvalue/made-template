#!/bin/bash

# Navigate to the project directory
cd C:/.../made-template-ws2324 # I used windows 

# Activate the virtual environment (replace "made" with the name of your virtual environment)
# Uncomment the line below if you are using a virtual environment
# ./made/Scripts/activate

# Install the required dependencies for testing (if not installed)
# Replace "test_requirements.txt" with the actual name of your test requirements file
# Uncomment the line below if you have a test requirements file
# pip install -r project/requirements.txt

# Run the Python tests
 
python -m unittest discover -s /project -p "tests.py"

# Deactivate the virtual environment (replace "made" with the name of your virtual environment)
# Uncomment the line below if you are using a virtual environment
# deactivate
