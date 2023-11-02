# Project Plan

## Title
<!-- Give your project a short title. -->
Comparative Analysis of Unemployment Trends in East and West Germany (2018-2023)

## Main Question
<!-- Think about one main question you want to answer based on the data. -->
1- How do unemployment trends and demographics compare between East and West Germany from 2018 to 2023, 
And what insights can be drawn from their differences and similarities?

## Description
<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
The project aims to conduct an in-depth comparative analysis of unemployment data from East and West Germany over a span of six years (2018-2023). By analyzing various metrics like total unemployment, gender-specific unemployment, youth unemployment, and long-term unemployment, we will be able to identify patterns, disparities, and trends across these two regions. This will not only give us a clearer understanding of the economic conditions in both parts of Germany but might also pave the way for more informed policy decisions.

The project will use data from two distinct datasets, which will be cleaned, preprocessed, and then visualized to draw meaningful conclusions.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->
### Datasource1: UnEmployment East Germany
* Metadata URL: https://www.destatis.de/EN/Themes/Economy/Short-Term-Indicators/Labour-Market/arb130.html#241598
* Data URL: https://drive.google.com/file/d/1TU0W0fzBEB-dbv_wp_k6Ro6Y6IRj-ysZ/view?usp=sharing
* Data Type: CSV
<!-- Short description of the DataSource. -->
The dataset provides Unemployment statistics specific to various cities in East Germany. It covers metrics such as total unemployment, gender-specific rates, youth unemployment, and long-term unemployment.


### Datasource2: UnEmployment West Germany
* Metadata URL: https://www.destatis.de/EN/Themes/Economy/Short-Term-Indicators/Labour-Market/arb120.html#241586
* Data URL: https://drive.google.com/file/d/10wZiHedngMfpn8gSvHfj1o2nizJaHISl/view?usp=sharing
* Data Type: CSV
<!-- Short description of the DataSource. -->
The dataset offers a comprehensive view of Unemployment figures for various cities in West Germany. It covers metrics such as total unemployment, gender-specific rates, youth unemployment, and long-term unemployment.


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->
1. Data Acquisition
    - Download datasets from the provided URLs.
    - Initial exploration to understand the structure and content.

2. Data Cleaning and Pre-processing
    - Handle missing values.
    - Standardize data formats across both datasets.
    - Filter out irrelevant data and keep only the data from 2018 to 2023.

3. Exploratory Data Analysis (EDA)
    - Descriptive statistics for each dataset.
    - Identify patterns and anomalies.

4. Data Visualization
    - Plot year-wise trends for both East and West Germany.
    - Compare gender-specific unemployment rates.
    - Visualize youth and long-term unemployment rates.

5. Insight Generation and Reporting
    - Interpret the visualizations.
    - Draft conclusions and insights from the analysis.
    - Present findings in a comprehensive report.
