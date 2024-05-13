#!/bin/bash

# Define the repository
REPO="muhammadalyy14/FAU-Data-Engineering-Project"

# Create Issues and assign them to the milestones
create_issue() {
  local title="$1"
  local body="$2"
  local milestone="$3"
  echo "Creating issue '$title' under milestone ID '$milestone'"
  gh issue create --repo $REPO --title "$title" --body "$body" --milestone "$milestone"
}


# Issues for Project Setup and Data Identification
create_issue "Formulate the central research questions" "Define the main questions that will guide the research." "Project Setup and Data Identification"
create_issue "Identify suitable data sources" "Identify and list potential data sources for the project." "Project Setup and Data Identification"
create_issue "Assess and select the appropriate data sources" "Evaluate the identified data sources and select the most suitable for the project." "Project Setup and Data Identification"

# Issues for Data Collection and Pipeline
create_issue "Decide on the optimal data storage solution" "Select the best data storage format based on the data types and analysis requirements." "Data Collection and Pipeline"
create_issue "Convert data into the chosen format" "Convert and prepare the data into the selected format for easier processing." "Data Collection and Pipeline"
create_issue "Data Pipeline" "Set up a data pipeline for continuous data collection and processing." "Data Collection and Pipeline"

# Issues for Data Analysis and Reporting
create_issue "Execute initial data exploration and basic visualizations" "Perform preliminary data checks and create initial visualizations to understand data trends." "Data Analysis and Reporting"
create_issue "Develop Functional Modules: Data Handling, Analysis Workflow, Visualization Tools, Analytical Models" "Build modular components for data processing, analysis, visualization, and modeling." "Data Analysis and Reporting"
create_issue "Conduct comprehensive data analysis and apply modeling techniques as needed" "Perform detailed data analysis and use statistical or machine learning models." "Data Analysis and Reporting"
create_issue "Address all the research questions" "Ensure that all the formulated research questions are thoroughly investigated and answered." "Data Analysis and Reporting"
create_issue "Show conclusions from the analysis" "Summarize the findings and conclusions derived from the data analysis." "Data Analysis and Reporting"

# Issues for Tests
create_issue "Design and implement module tests" "Create tests for each developed module to ensure reliability and correctness." "Tests"

# Issues for Integration and Workflow Automation
create_issue "Implement Continuous Integration (CI) for module testing" "Develop and set up CI processes for automated testing of modules." "Integration and Workflow Automations"

# Issues for Final Documentation and Presentation
create_issue "Create visual representations" "Develop comprehensive and informative visual representations of the data and findings." "Final Documentation and Presentation"
create_issue "Improve the project documentation" "Enhance the overall project documentation to ensure clarity and comprehensiveness." "Final Documentation and Presentation"
create_issue "Prepare the final presentation" "Compile and prepare the final presentation to summarize the project and its outcomes." "Final Documentation and Presentation"
