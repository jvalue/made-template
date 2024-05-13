#!/bin/bash

# Define the repository
REPO="muhammadalyy14/FAU-Data-Engineering-Project"

# Create Milestones and store their IDs in an array
declare -A MILESTONES
MILESTONES["Project Setup and Data Identification"]=$(gh api -X POST /repos/$REPO/milestones --field title="Project Setup and Data Identification" --jq '.number')
MILESTONES["Data Collection and Pipeline"]=$(gh api -X POST /repos/$REPO/milestones --field title="Data Collection and Pipeline" --jq '.number')
MILESTONES["Data Analysis and Reporting"]=$(gh api -X POST /repos/$REPO/milestones --field title="Data Analysis and Reporting" --jq '.number')
MILESTONES["Tests"]=$(gh api -X POST /repos/$REPO/milestones --field title="Tests" --jq '.number')
MILESTONES["Integration and Workflow Automations"]=$(gh api -X POST /repos/$REPO/milestones --field title="Integration and Workflow Automations" --jq '.number')
MILESTONES["Final Documentation and Presentation"]=$(gh api -X POST /repos/$REPO/milestones --field title="Final Documentation and Presentation" --jq '.number')

# Optionally, print milestone IDs to verify creation
for key in "${!MILESTONES[@]}"; do
    echo "$key: ${MILESTONES[$key]}"
done