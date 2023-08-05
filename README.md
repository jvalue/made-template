<div style="text-align: center;">

# Electromobility and Charging Infrastructure in Germany

[![Licence](https://img.shields.io/badge/Licence-MIT-orange)](https://opensource.org/license/mit/)
[![Continuous Integration](https://github.com/nmarkert/amse/actions/workflows/ci-pipeline.yml/badge.svg)](https://github.com/nmarkert/amse/actions/workflows/ci-pipeline.yml)
[![python](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

</div>

## Overview
The aim of this project is to investigate if there is a relationship betwenn the charging point infrastructure and electromobility in Germany. Therefore it uses open available datasources provided by different institutions to analyze the relationship over time and by states ("Bundesländer"). <br>
In the `data` folder you can find the [datapipeline](https://github.com/nmarkert/amse/blob/main/data/datapipeline.py) which is used to load the data from the internet, proccesses it and stores it to a database. <br>
In the `project` folder you find all additional informations about the project, like what datasources where used. The final report about the findings from the processed data you can see in the [report.ipynb](https://github.com/nmarkert/amse/blob/main/project/report.ipynb).
## Context
This repository is the result of my participation in the course [Advanced Methods of Software Engineering](https://oss.cs.fau.de/teaching/specific/amse/) provided by the [Professorship of Open-Source Software](https://oss.cs.fau.de) from FAU. <br>
The task was to build a Data Engineering Project, which takes at least two public available datasources and processes them with an automated datapipeline, in order to report some findings from the result.


