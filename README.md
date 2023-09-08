
## Pandas Descriptive Statistics Script

IDS 706 Mini-Project 2

Pandas Descriptive Statistics Script

###Goal

The goal of this project is to establish a CodeSpaces environment that automates the process of loading an email dataset using `Pandas` and executing a `readfile` function to generate descriptive statistics on the dataset, utilizing GitHub Actions.

The workflow includes running a Makefile to perform tasks such as installation (`make install`), testing (`make test`), code formatting (`make format`), linting (`make lint`), and an all-inclusive task (`make all`). This automation streamlines the data analysis process and enhances code quality.

###Preperation

I used the IDS-706-Python-GitHub-template for this project. 

This template includes a `Makefile`, `requirements.txt`, `.devcontainer`, `.gitignore`, `GitHubActions`, and `Readme`.

###Overview

In this project:


1). I added pandas 2.1.0 in the requirements.txt.

 

2). I wrote a `readfile` function in the main.py, which reads a CSV file and returns the summary statistics.

 

3). I wrote a test function `test_readfile` in the test_main.py, which checks the summary statistics of `emails.csv`.

+ check the mean value of the first column in emails.csv
+ check the minimum value of the first column in emails.csv
+ check the maximum value of the first column in emails.csv

###Check Format and Test Approval Image


