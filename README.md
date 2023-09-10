[![CI](https://github.com/nogibjj/tinayi_week2_mini_project/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/tinayi_week2_mini_project/actions/workflows/cicd.yml)

## Pandas Descriptive Statistics Script

IDS 706 Mini-Project 2

Pandas Descriptive Statistics Script

### Goal

The goal of this project is to 

+ establish a CodeSpaces environment that automates the process of loading a dataset using `Pandas` and executing a `readfile` function to generate descriptive statistics on the dataset, utilizing GitHub Actions. 
  
+ create data visualizations of the dataset using Jupyter Notebook

The workflow includes running a Makefile to perform tasks such as installation (`make install`), testing (`make test`), code formatting (`make format`), linting (`make lint`), and an all-inclusive task (`make all`). This automation streamlines the data analysis process and enhances code quality.

### Preperation

+ I used the IDS-706-Python-GitHub-template for this project. This template includes a `Makefile`, `requirements.txt`, `.devcontainer`, `.gitignore`, `GitHubActions`, and `Readme`.

+ I downloaded the `Email Spam Classification Dataset CSV` from Kaggle.

### Dataset Background 

`Email Spam Classification Dataset CSV` is a csv file containing related information of 5172 randomly picked email files and their respective labels for spam or not-spam classification.

The csv file contains 5172 rows, each row for each email. There are 3002 columns. The first column indicates Email name. The name has been set with numbers and not recipients' name to protect privacy. The last column has the labels for prediction : 1 for spam, 0 for not spam. The remaining 3000 columns are the 3000 most common words in all the emails, after excluding the non-alphabetical characters/words. For each row, the count of each word(column) in that email(row) is stored in the respective cells. Thus, information regarding all 5172 emails are stored in a compact dataframe rather than as separate text files.

#### [Resources](https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv) 

### Overview

This project creates a Python script using Pandas for descriptive statistics. The specific steps involve: 

+ Create a Phython script

  + Read a dataset (CSV)

  + Generate summary statistics (mean, median, standard deviation)

  + Create one data visualization

+ Generate summary report (PDF or markdown)
  
### Description

Step1: In the requirements.txt, adding pandas 2.1.0. 

Step2: In the main.py, I created a Python Script. It includes 
       + a `readfile` function, which reads a CSV file and returns the summary statistics.
       + a 'graph' function which provides visual context on the CSV data.

Step3: In the test_main.py, I wrote a test function `test_readfile` , which checks the summary statistics of `emails.csv`.
       + check the mean value of the second column (letter "the") in emails.csv
       + check the median value of the second column (letter "the") in emails.csv
       + check the standard deviation value of the second column (letter "the") in emails.csv

Step4: I generate summary report (PDF or markdown) from Jupyter Notebook

### Check Format and Test Approval Image

+ install code `make install`
  
<img width="1067" alt="Screen Shot 2023-09-08 at 4 53 59 PM" src="https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/84203fec-f516-4f85-8cd2-0b0e2eaced38">

+ lint code `make lint`
+ format code `make format`
+ test code `make test`

<img width="1124" alt="Screen Shot 2023-09-08 at 4 54 29 PM" src="https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/defbc82f-82cc-4b36-b05b-0170b1014acd">

+ code `make all` executes install, lint, format, and test targets

<img width="1120" alt="Screen Shot 2023-09-08 at 4 55 01 PM" src="https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/349a11eb-7f99-44ba-afd3-e456ba80f167">

