# Project Plan

## Title
<!-- Give your project a short title. -->
BRFC - Behavior risk factors & cancer project.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
How do behavioral risks influence cancer (or even mutations). 

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Cancer is one of the leading number of deaths, bronchus and lung cancer deaths are now ranked 6th among the leading causes of deaths (https://www.who.int/news-room/fact-sheets/detail/the-top-10-causes-of-death). Also obesity is a world wide health issue and influences diseases. Rising numbers in cancer and obesity are alerting and therefore it is of high interest to reveal any relations of obesity/behavioral risk factors and cancer in order to apply countermeasures.

This project aims to uncover relations of behavioral risk factors and cancer.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1 GDC - NCI Genomic Data Commons
License: Data usage agreement: https://gdc.cancer.gov/about-data/data-analysis-policies

Several apis/ways to retrieve data from GDS: https://docs.gdc.cancer.gov/Data/Data_Model/GDC_Data_Model/#data-users
Data Model: https://gdc.cancer.gov/developers/gdc-data-model

#### Datasource1a GraphQL API: GDC - NCI Genomic Data Commons
Cancer and genomic data GraphQL API
* Metadata URL: https://docs.gdc.cancer.gov/API/Users_Guide/GraphQL_Examples/
* Data URL: https://api.gdc.cancer.gov/v0/graphql
* Query: ToBeSpecified with project
* Data Type: json

#### Datasource1b REST API: GDC - NCI Genomic Data Commons
Cancer and genomic data direct download
* Metadata URL: https://docs.gdc.cancer.gov/API/Users_Guide
* Data URL: https://portal.gdc.cancer.gov/exploration?filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22bronchus%20and%20lung%22%5D%7D%7D%5D%7D
* Data Type: json

### Datasource2 Behavioral Risk Factor Surveillance
License: https://opendefinition.org/licenses/odc-odbl/
#### Datasource2: Behavioral Risk Factor Surveillance
Nutrition, Physical Activity, and Obesity - Behavioral Risk Factor Surveillance System
* Metadata URL: https://catalog.data.gov/harvest/object/721fe106-9250-45d7-9093-1edacb565cd4
* Data URL: https://catalog.data.gov/dataset/nutrition-physical-activity-and-obesity-behavioral-risk-factor-surveillance-system
* Data Type: json/xml/rdf/csv


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

### Milestone 1: Data inspection, Goal: Data available, conclusion if data is sufficient, side effects of data
1. Download data packages [#1][i1]
2. Inspect data packages [#2][i2]
3. Elaborate on side effects of data [#3][i3]

### Milestone 2: Work on question 1 'Correlation of behavioral risk factors and cancer (primary site 'bronchus and lung')'
1. Data preprocessing [#4][i4]
2. Data evaluation [#5][i5]
3. Report [#6][i6]

### Milestone 3: Work on question 2: 'Find mutations in genomic data related to behavioral risk factors for cancer primary site 'bronchus and lung''
1. Data preprocessing [#7][i7]
2. Implementation of CNN [#8][i8]
3. Data evaluation [#9][i9]
4. Report [#10][i10]

### Milestone 4: Summarizing
1. Revise reports [#11][i11]
2. Conclude [#12][i12]
3. Poster [#13][i13]

---

[i1]: https://github.com/nilapalin/made-template/issues/1
[i2]: https://github.com/nilapalin/made-template/issues/2
[i3]: https://github.com/nilapalin/made-template/issues/3
[i4]: https://github.com/nilapalin/made-template/issues/4
[i5]: https://github.com/nilapalin/made-template/issues/5
[i6]: https://github.com/nilapalin/made-template/issues/6
[i7]: https://github.com/nilapalin/made-template/issues/7
[i8]: https://github.com/nilapalin/made-template/issues/8
[i9]: https://github.com/nilapalin/made-template/issues/9
[i10]: https://github.com/nilapalin/made-template/issues/10
[i11]: https://github.com/nilapalin/made-template/issues/11
[i12]: https://github.com/nilapalin/made-template/issues/12
[i13]: https://github.com/nilapalin/made-template/issues/13

<!--
Comments and Hints:
Demo showing cases with pancreatic cancer with and without mutations in the gene KRAS
https://portal.gdc.cancer.gov/analysis?analysisId=demo-comparison&analysisTableTab=result

Inspect:
Survival Analysis
Survival plot 1: with gene mutation 2: without gene mutation
Age at Diagnosis

Evaluation:
- Differentiate race/ethnicity for cancer and BRFSS
- Differentiate gender for cancer and BRFSS
- Differentiate age for cancer and BRFSS
- search for data with specific genes regarding BRFSS
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6226269/ MC4R and LEPR
    MC4R (melanocortin 4 receptor): https://portal.gdc.cancer.gov/genes/ENSG00000166603
    https://de.wikipedia.org/wiki/Melanocortin-4-Rezeptor 'Ferner unterdrückt er das Hungergefühl'
        

-->