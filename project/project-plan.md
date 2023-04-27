# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->

This projects analyzes the national passenger transport demand in Germany.
After the analysis, the following questions should have an answer.

- How old are the passengers using public transport.
- Where do they go?
- why do they go?

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->

- Understanding the travel patterns of different age groups can help identify the transportation needs of different demographics, which can inform transportation policy and planning. For example, if a certain age group is found to be traveling more frequently, it may indicate a need for better transit options or increased mobility services for that group.
- Understanding traffic flow patterns can help identify congested regions and routes, which can inform transportation planning and infrastructure investments. This can lead to reduced travel times, less congestion and frustration for commuters, and potentially reduced carbon emissions from vehicles stuck in traffic.
- Understanding traffic flow patterns can help identify congested regions and routes, which can inform transportation planning and infrastructure investments. This can lead to reduced travel times, less congestion and frustration for commuters, and potentially reduced carbon emissions from vehicles stuck in traffic.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Vorläufige bundesweite Verkehrsströme (National passenger transport demand)

- Metadata URL: https://mobilithek.info/mdp-api/files/aux/573360269906817024/metadata.csv
- Data URL: https://mobilithek.info/mdp-api/files/aux/573360269906817024/trip_count_matrix_county_by_age_activity_2022.csv
- Data Type: CSV

This dataset contains preliminary results of the national passenger transport demand model DEMO in the form of traffic flow matrices between the 400 urban and rural districts in Germany. It is published by the German Aerospace Center (DLR).
The results depict Germany-wide traffic flows for an average working day. The traffic flows are broken down by trip purpose and age group per origin/destination relation.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Find datasource [#2](https://github.com/iheziqi/amse-project/issues/2)
2. Finish project plan (for now week2) [#3](https://github.com/iheziqi/amse-project/issues/3)
