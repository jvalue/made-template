#!/bin/bash

# Define the repository
REPO="Hassan8725/advance_data_engineering"

# Create Issues and assign them to the milestones
create_issue() {
  local title="$1"
  local body="$2"
  local milestone="$3"
  echo "Creating issue '$title' under milestone ID ${MILESTONES[$milestone]}"
  gh issue create --repo $REPO --title "$title" --body "$body" --milestone "$milestone"
}

# Issues for Objective Definition and Data Source Selection
create_issue "Define the research question" "Details of the issue..." "Objective Definition and Data Source Selection"
create_issue "Locate potential data sources" "Details of the issue..." "Objective Definition and Data Source Selection"
create_issue "Evaluate the identified data sources" "Details of the issue..." "Objective Definition and Data Source Selection"

# Issues for Data Acquisition and Pipeline
create_issue "Determine the best data storage format" "Details of the issue..." "Data Acquisition and Pipeline"
create_issue "Convert data into the chosen format" "Details of the issue..." "Data Acquisition and Pipeline"
create_issue "Data Pipeline" "Details of the issue..." "Data Acquisition and Pipeline"

# Issues for Data Exploration, Analytics and Report
create_issue "Conduct exploratory data analysis and preliminary visualization" "Details of the issue..." "Data Exploration, Analytics and Report"
create_issue "Create Modules: DataLoader, Pipeline, Visualizations, Models, etc" "Details of the issue..." "Data Exploration, Analytics and Report"
create_issue "Perform data analysis and modeling (where necessary)" "Details of the issue..." "Data Exploration, Analytics and Report"
create_issue "Address all the research questions" "Details of the issue..." "Data Exploration, Analytics and Report"
create_issue "Draw conclusions from the analysis" "Details of the issue..." "Data Exploration, Analytics and Report"

# Issues for Tests
create_issue "Create Tests for each module" "Details of the issue..." "Tests"

# Issues for Continuous integration
create_issue "Develop CI for Tests" "Details of the issue..." "Continuous integration"
create_issue "Develop CI for Pre-Commit" "Details of the issue..." "Continuous integration"

# Issues for Reporting Results
create_issue "Develop visual representations" "Details of the issue..." "Reporting Results"
create_issue "Enhance the repository's presentation" "Details of the issue..." "Reporting Results"
create_issue "Prepare the final presentation" "Details of the issue..." "Reporting Results"
