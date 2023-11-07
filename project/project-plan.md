# Project Plan

## Title
<!-- Give your project a short title. -->
BRFC - Behavior risk factors & cancer project.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
How do behavioral risks influence cancer (or even mutations). 

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Cancer is one of the leading number of deaths, bronchus and lung cancer deaths are now ranked 6th among the leading causes of deaths (https://www.who.int/news-room/fact-sheets/detail/the-top-10-causes-of-death). 

This projects aims to uncover relations of behavioral risk factors and cancer.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

#### Datasource1a: GDC - NCI Genomic Data Commons
Cancer and genomic data GraphQL API
* Metadata URL: https://docs.gdc.cancer.gov/API/Users_Guide/GraphQL_Examples/
* Data URL: https://api.gdc.cancer.gov/v0/graphql
* Query: ToBeSpecified with project
* Data Type: json

#### Datasource1b: GDC - NCI Genomic Data Commons
Cancer and genomic data direct download
* Metadata URL: https://docs.gdc.cancer.gov/API/Users_Guide
* Data URL: https://portal.gdc.cancer.gov/exploration?filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22bronchus%20and%20lung%22%5D%7D%7D%5D%7D
* Data Type: json

#### Datasource2: Behavioral Risk Factor Surveillance
Nutrition, Physical Activity, and Obesity - Behavioral Risk Factor Surveillance System
* Metadata URL: https://catalog.data.gov/harvest/object/721fe106-9250-45d7-9093-1edacb565cd4
* Data URL: https://catalog.data.gov/dataset/nutrition-physical-activity-and-obesity-behavioral-risk-factor-surveillance-system
* Data Type: json/xml/rdf/csv


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

### Milestone 1: Data inspection, Goal: Data available, conclusion if data is sufficient, side effects of data
1. Download data packages [#1]
2. Inspect data packages
3. Elaborate on side effects of data

### Milestone 2: Work on question 1 'Correlation of behavioral risk factors and cancer (primary site 'bronchus and lung')'
1. Data preprocessing
2. Data evaluation
3. Report

### Milestone 3: Work on question 2: 'Find mutations in genomic data related to behavioral risk factors for cancer primary site 'bronchus and lung''
1. Data preprocessing
2. Implementation of CNN
3. Data evaluation
4. Report

### Milestone 4: Summarizing
1. Revise reports
2. Conclude
3. Poster