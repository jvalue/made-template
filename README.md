# Analyzing the Correlation between Supershop Sales and Weather Patterns in Myanmar (Yangon, Mandalay, Naypyitaw): A Data-Driven Investigation

## Project Overview

Welcome to the *"Analyzing the Correlation between Supershop Sales and Weather Patterns in Myanmar"* project repository. In the retail landscape, particularly within supermarkets, external factors like weather conditions play a pivotal role. This project delves into the intricate relationship between temperature patterns and Supershop sales. The investigation specifically focuses on the impact of temperature on Supershop sales in three major cities in Myanmar: Yangon, Mandalay, and Naypyitaw. Understanding this correlation holds the potential to revolutionize conventional strategies, providing businesses with insights to enhance decision-making through predictive analytics.

## Project Goals

The primary objectives of this project include answering the following questions:

1. **Temperature Variation (Jan-Mar 2019):** Explore the temperature variances in Yangon, Mandalay, and Naypyitaw cities during the period from January to March 2019.

2. **Supermarket Sales Trends:** Analyze and compare Supershop sales data in these three cities within the same timeframe, identifying patterns or fluctuations.

3. **Temperature-Sales Correlation:** Investigate whether and to what extent temperature influences supermarket sales, shedding light on consumer behavior dynamics.

You can find the project report [here](/project/report.ipynb). To run the report on your local machine, ensure that you have the necessary libraries installed. Follow the steps outlined in the [Project setup](#project-setup) section for the installation process.

Feel free to navigate through the report to gain a comprehensive understanding of the project's objectives, methods, results, and potential implications. We encourage collaboration, contributions, and adaptations of these findings for further exploration. Let's dive into the intriguing intersection of Supershop sales and weather patterns in Myanmar!

## Project Setup

1. Clone the repository:

``git clone git@github.com:islam15-8789/made-template.git``

2. Create virtual environment:

``python3.11 -m venv venv``

3. Activate the virtual environment:

``source .venv/bin/activate`` 

4. Install requirements:

``pip install -r requirements.txt``

## etl-pipeline-runner
An ETL (Extract Transform Load) pipeline has been employed a to gather the required data for this project. Throughout the project, a collaborative effort has been made to initiate an [open-source Python package](https://github.com/prantoamt/etl-pipeline-runner) for executing ETL pipelines. Take a moment to review our contributions and share your feedback. Your input is highly appreciated.

## Exercises
During the semester you will need to complete exercises, sometimes using [Python](https://www.python.org/), sometimes using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.<jv or py>`.

In regular intervalls, exercises will be given as homework to complete during the semester. We will divide you into two groups, one completing an exercise in Jayvee, the other in Python, switching each exercise. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv` or `./exercises/exercise1.py`
2. `./exercises/exercise2.jv` or `./exercises/exercise2.py`
3. `./exercises/exercise3.jv` or `./exercises/exercise3.py`
4. `./exercises/exercise4.jv` or `./exercises/exercise4.py`
5. `./exercises/exercise5.jv` or `./exercises/exercise5.py`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
