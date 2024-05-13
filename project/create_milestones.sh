#!/bin/bash

# Define the repository
REPO="Hassan8725/advance_data_engineering"

# Create Milestones and store their IDs in an array
declare -A MILESTONES
MILESTONES["Objective Definition and Data Source Selection"]=$(gh api -X POST /repos/$REPO/milestones --field title="Objective Definition and Data Source Selection" --jq '.number')
MILESTONES["Data Acquisition and Pipeline"]=$(gh api -X POST /repos/$REPO/milestones --field title="Data Acquisition and Pipeline" --jq '.number')
MILESTONES["Data Exploration, Analytics and Report"]=$(gh api -X POST /repos/$REPO/milestones --field title="Data Exploration, Analytics and Report" --jq '.number')
MILESTONES["Tests"]=$(gh api -X POST /repos/$REPO/milestones --field title="Tests" --jq '.number')
MILESTONES["Continuous integration"]=$(gh api -X POST /repos/$REPO/milestones --field title="Continuous integration" --jq '.number')
MILESTONES["Reporting Results"]=$(gh api -X POST /repos/$REPO/milestones --field title="Reporting Results" --jq '.number')
