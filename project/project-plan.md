# Project Plan

## Title
<!-- Give your project a short title. -->
Awesome MADE project.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->


1. Does cancer on primary site 'bronchus and lung' appear more often in areas with high air polution?
optional (AI part):
2. Are there specific mutations on genes for cancer on primary site 'bronchus and lung' in areas with high polution

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
XY is an important problem, because... This projects analyzes XY, using method A. The results can give insights into...

Air polution has many effects on the environment. One effect is that there are more diseases related to it, e.g. cancer. 
This projects aims to uncover relations of air polution and cancer in the primary site 'bronchus and lung' and optionally reveals information of mutations in genomic data of patients with cancer on the primary site 'bronchus and lung' regarding the living habitat and its air polution.

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

#### Datasource2: Air Quality
Ambient outdoor air pollution database Version 2022
* Metadata URL: https://www.who.int/data/gho/data/themes/air-pollution/who-air-quality-database/2022
* Data URL: https://cdn.who.int/media/docs/default-source/air-pollution-documents/air-quality-and-health/who_aap_2021_v9_11august2022.xlsx?sfvrsn=9035996c_3
* Data Type: xlsx


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

### Milestone 1: Data inspection, Goal: Data available, conclusion if data is sufficient, side effects of data
1. Download data packages [#1][i1]
2. Inspect data packages
3. Elaborate on side effects of data

[i1]: h

### Milestone 2: Work on question 1 'Correlation of air polution and cancer primary site 'bronchus and lung''
1. Data preprocessing
2. Data evaluation
3. Report

### Milestone 3: Work on question 2: 'Find mutations in genomic data related to air polution for cancer primary site 'bronchus and lung''
1. Data preprocessing
2. Implementation of CNN
3. Data evaluation
4. Report

### Milestone 4: Summarizing
1. Revise reports
2. Conclude
3. Poster

## TODO
-[] investigate exposures: cigarettes per day