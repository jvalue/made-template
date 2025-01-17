# Methods of Advanced Data Engineering Template Project

This template project provides some structure for your open data project in the MADE module at FAU.
This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.

To get started, please follow these steps:
1. Create your own fork of this repository. Feel free to rename the repository right after creation, before you let the teaching instructors know your repository URL. **Do not rename the repository during the semester**.

## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones, so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to HTML: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervals, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/).

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions → Exercise Feedback in your repository.

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
  ## A visual analysis of the security situation and potential crime influencing factors in California‘s cities
  California is not only the most economically developed state in the U.S., but also the most populous state in the U.S. Its stunning scenery, booming economy, advanced technology and excellent educational resources combine to attract visitors from all over the world. While the security situation in California is an important consideration for people before traveling, California's security situation presents complexity. In this regard, this project puts forward the following questions to study the security situation in California cities and tries to answer them through data engineering methods:
   1. What types of crimes are most common in all California cities? Is there a type of crime that is
 predominant in most cities?
   2. Which cities in California have the highest crime rate (per 100000 residents)?
   3. Do all California cities have similar ratios of the number of law enforcement officers to the number
 of crimes? Or are the ratios of the number of law enforcement to the population similar?
   4. Do California cities with higher median household incomes or high school graduation rates have
 lower crime rates?
   5. Do cities with high poverty rates have higher crime rates?
      
The answers to these questions can provide a safety index for people who want to travel or settle in California, and can also help policymakers and government officials develop personalized crime prevention measures in specific cities. See [analysis-report.pdf](https://github.com/Jackie-Soo/made-template/blob/Jackie-Soo-patch-1/project/analysis-report.pdf) for details.

  ## License
  This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0).
  See the [LICENSE](https://github.com/Jackie-Soo/made-template/blob/Jackie-Soo-patch-1/LICENSE) file for details.
