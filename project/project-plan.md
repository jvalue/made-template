# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This projects analyzes the relationship between the type and quantity of vehicles and the population and population composition in Münster.

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
The analysis can provide valuable insights into the current state of transportation infrastructure in the city, which can help local authorities make informed decisions on how to improve it. 

Additionally, understanding the relationship between the type and quantity of vehicles and the population and population composition can help identify potential areas of concern. For example, analyzing the types of vehicles preferred by Münster residents of different ages and genders can inform sales plans aimed at these groups. 

Lastly, this type of analysis can provide a better understanding of the transportation needs of different groups within the population, such as the elderly or young, which can inform policies aimed at improving their access to transportation services..

## Datasources
Datasource1: Mobilithek
* Metadata URL: https://mobilithek.info/offers/-1738218276875079533
* Data URL: https://opendata.stadt-muenster.de/sites/default/files/Fahrzeugbestand-Regierungsbezirk-Muenster-2018-2022.xlsx
* Data Type: xlsx
Datasource1: opendata.stadt-muenster
* Metadata URL: https://opendata.stadt-muenster.de/dataset/statistik-bev%C3%B6lkerungsentwicklung
* Data URL:https://www.stadt-muenster.de/fileadmin/user_upload/stadt-muenster/61_stadtentwicklung/pdf/sms/05515000_csv_bevoelkerungsentwicklung_geschlecht.csv
*          https://www.stadt-muenster.de/fileadmin/user_upload/stadt-muenster/61_stadtentwicklung/pdf/sms/05515000_csv_bevoelkerungsentwicklung_altersgruppen.csv
*          https://www.stadt-muenster.de/fileadmin/user_upload/stadt-
           muenster/61_stadtentwicklung/pdf/sms/05515000_csv_bevoelkerungsentwicklung_staatsangehoerigkeit.csv
* Data Type: CSV
<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

get DATA:"Fahrzeugbestand Regierungsbezirk Münster 2018-2022"from Datasourse 1

get DATA:"Bevölkerungsentwicklung nach Geschlecht"from Datasource 2
         "Bevölkerungsentwicklung nach Altersgruppen"from Datasource 2
         "Bevölkerungsentwicklung nach 1. Staatsangehörigkeit"from Datasource 2
   
## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1.Data Collection and Cleaning: This work package involves collecting data on the type and quantity of vehicles in Münster as well as population and population composition data. The collected data needs to be cleaned and formatted for analysis. (Issue: Data Collection and Cleaning)

2.Exploratory Data Analysis: This work package involves exploring the relationships between the type and quantity of vehicles and the population and population composition using descriptive statistics and visualizations. (Issue: Exploratory Data Analysis)
3.Statistical Analysis: This work package involves conducting statistical analysis to quantify the relationships between the variables of interest, such as correlation and regression analysis. (Issue: Statistical Analysis)
4.Interpretation of Results: This work package involves interpreting the results of the statistical analysis and drawing meaningful conclusions about the relationships between the type and quantity of vehicles and the population and population composition. (Issue: Interpretation of Results)
4.Documentation and Reporting: This work package involves documenting the methodology, results, and recommendations of the analysis in a report that is clear, concise, and accessible to stakeholders. (Issue: Documentation and Reporting)

[i1]: 
