# Project Plan

## Title
<!-- Give your project a short title. -->
Climate Resilience and Financial Commitments: Analysis of Disaster Trends and Environment Spending.

## Questions

<!-- Think about one main question you want to answer based on the data. -->
1. How have climate-related disasters evolved globally over the past decade?
2. Which regions or countries are most frequently affected by specific types of climate-related disasters?
3. What is the relationship between disaster frequency and the INFORM risk indices?
4. How do financial investments in environmental protection influence the effectiveness of disaster management?

## Description

<!-- Describe your  project in max. 200 words. Consider writing about why and how you attempt it. -->
This project aims to conduct a detailed analysis of climate-related disasters, focusing on how frequently specific disasters occur within various countries, and the corresponding financial investments made in mitigation and prevention. The study will leverage three datasets to explore the incidence of disasters like storms, floods, and landslides, compare these occurrences with the INFORM risk indices, and examine the financial efforts countries devote to disaster prevention.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasoruce # 1: Climate-related Disasters Frequency
* Data URL: https://opendata.arcgis.com/datasets/b13b69ee0dde43a99c811f592af4e821_0.csv
* Metadata URL: https://climatedata.imf.org/datasets/b13b69ee0dde43a99c811f592af4e821_0/about
* Data Type: .csv

This dataset, sourced from EM-DAT by the Université catholique de Louvain, tracks the frequency of various climate-related disasters globally from 1980 to 2022. It includes detailed records for different types of disasters such as droughts, floods, extreme temperatures, landslides, storms, and wildfires. Each entry specifies the country affected, the type of disaster, and the annual occurrence data. This dataset enables an analysis of trends over decades to understand how the frequency of these disasters has changed in response to global climate change.

### Datasource 2: Climate-driven INFORM Risk
* Data URL: https://opendata.arcgis.com/datasets/7cae02f84ed547fbbd6210d90da19879_0.csv
* Metadata URL: https://climatedata.imf.org/datasets/7cae02f84ed547fbbd6210d90da19879_0/about
* Data Type: .csv

The Climate-driven INFORM Risk Indicator, adjusted annually by IMF staff, provides a comprehensive assessment of the risk associated with climate-driven hazards. It focuses on three dimensions: hazard & exposure, vulnerability, and lack of coping capacity. Each country's data from 2013 to 2022 reflects the aggregated risk posed by potential climate-related events such as floods, tropical cyclones, and droughts. This dataset aids in evaluating the preparedness and vulnerability of different nations to handle climate-induced disasters.

### Datasource 3: Government Expenditure on Environmental Protection
* Data URL: https://opendata.arcgis.com/datasets/d22a6decd9b147fd9040f793082b219b_0.csv
* Metadata URL: https://climatedata.imf.org/datasets/d22a6decd9b147fd9040f793082b219b_0/about
* Data Type: .csv

This dataset measures the financial commitment of various governments towards environmental protection as a percentage of GDP, spanning from 1995 to 2022. Compiled within the framework of the Classification of Functions of Government (COFOG), it covers expenditures on pollution abatement, biodiversity and landscape protection, waste management, and other environmental activities. This dataset is crucial for analyzing how investment in environmental protection correlates with national economic priorities and the management of climate risk.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

This project is structured into six work packages, represented as [milestones in the GitHub repository](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/milestones).


1. *Project Setup and Data Identification* [[WP1](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/milestone/1)]
    1. Formulate the central research questions [[issue](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/issues/6)]
    2. Identify suitable data sources [[issue](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/issues/7)]
    3. Assess and select the appropriate data sources [[issue](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/issues/8)]
2. *Data Collection and Pipeline* [[WP2](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/milestone/2)]
    1. Decide on the optimal data storage solution [[issue](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/issues/9)]
    2. Convert data into the chosen format [[issue](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/issues/10)]
    3. Data Pipeline [[issue](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/issues/11)]
3. *Data Analysis and Reporting* [[WP3](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/milestone/3)]
    1. Execute initial data exploration and basic visualizations [[issue](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/issues/12)]
    2. Develop Functional Modules: Data Handling, Analysis Workflow, Visualization Tools, Analytical Models[[issue](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/issues/13)]
    3. Conduct comprehensive data analysis and apply modeling techniques as needed  [[issue](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/issues/14)]
    4. Address all the research questions [[issue](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/issues/15)]
    5. Show conclusions form the analysis [[issue](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/issues/16)]
4. *Tests* [[WP4](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/milestone/4)]
    1. Design and implement module tests [[issue](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/issues/17)]
5. *Integration and Workflow Automation * [[WP5](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/milestone/5)]
    1. Implement Continuous Integration (CI) for module testing [[issue](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/issues/18)]
6. *Final Documentation and Presentation* [[WP6](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/milestone/6)]
    1. Create visual representations [[issue](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/issues/19)]
    2. Improve the project documentation [[issue](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/issues/20)]
    3. Prepare the final presentation [[issue](https://github.com/muhammadalyy14/FAU-Data-Engineering-Project/issues/21)]


Issues are subject to change