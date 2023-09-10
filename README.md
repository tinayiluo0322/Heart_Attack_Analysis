[![CI](https://github.com/nogibjj/tinayi_week2_mini_project/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/tinayi_week2_mini_project/actions/workflows/cicd.yml)

## Pandas Descriptive Statistics Script

IDS 706 Mini-Project 2

Pandas Descriptive Statistics Script

### Goal

The goal of this project is to establish a CodeSpaces environment that automates the process of loading an email dataset using `Pandas` and executing a `readfile` function to generate descriptive statistics on the dataset, utilizing GitHub Actions.

The workflow includes running a Makefile to perform tasks such as installation (`make install`), testing (`make test`), code formatting (`make format`), linting (`make lint`), and an all-inclusive task (`make all`). This automation streamlines the data analysis process and enhances code quality.

### Preperation

I used the IDS-706-Python-GitHub-template for this project. 

This template includes a `Makefile`, `requirements.txt`, `.devcontainer`, `.gitignore`, `GitHubActions`, and `Readme`.

### Overview

In this project:


1). I added pandas 2.1.0 in the requirements.txt.

 

2). I wrote a `readfile` function in the main.py, which reads a CSV file and returns the summary statistics.

 

3). I wrote a test function `test_readfile` in the test_main.py, which checks the summary statistics of `emails.csv`.

+ check the mean value of the first column in emails.csv
+ check the minimum value of the first column in emails.csv
+ check the maximum value of the first column in emails.csv

### Check Format and Test Approval Image

+ install code `make install`
  
<img width="1067" alt="Screen Shot 2023-09-08 at 4 53 59 PM" src="https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/84203fec-f516-4f85-8cd2-0b0e2eaced38">

+ lint code `make lint`
+ format code `make format`
+ test code `make test`

<img width="1124" alt="Screen Shot 2023-09-08 at 4 54 29 PM" src="https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/defbc82f-82cc-4b36-b05b-0170b1014acd">

+ code `make all` executes install, lint, format, and test targets

<img width="1120" alt="Screen Shot 2023-09-08 at 4 55 01 PM" src="https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/349a11eb-7f99-44ba-afd3-e456ba80f167">

