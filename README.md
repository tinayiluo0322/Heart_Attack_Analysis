[![CI](https://github.com/nogibjj/tinayi_week2_mini_project/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/tinayi_week2_mini_project/actions/workflows/cicd.yml)

## Pandas Descriptive Statistics Script

IDS 706 Mini-Project 2

Pandas Descriptive Statistics Script

### Goal

The goal of this project is to:

+ establish a CodeSpaces environment that automates the process of loading a dataset using `Pandas` and executing a `readfile` function to generate descriptive statistics on the dataset, utilizing GitHub Actions. 
  
+ create data visualizations of the dataset using `matplotlib`

+ create summary report using `Jupyter Notebook`

The workflow includes running a Makefile to perform tasks such as installation (`make install`), testing (`make test`), code formatting (`make format`), linting (`make lint`), and an all-inclusive task (`make all`). This automation streamlines the data analysis process and enhances code quality.

### Preperation

+ I used the IDS-706-Python-GitHub-template for this project. This template includes a `Makefile`, `requirements.txt`, `.devcontainer`, `.gitignore`, `GitHubActions`, and `Readme`.

+ I downloaded the `Heart Attack Analysis & Prediction Dataset` from Kaggle.

### Dataset Description

`Heart Attack Analysis & Prediction Dataset` (simplify as `heart.csv`) is a csv file containing related information of 302 randomly picked people and their respective information including age, sex, exercise induced angina, number of major vessels, chest pain type, resting blood pressure, cholestoral, fasting blood sugar, resting electrocardiographic results, and chances of heart attack.

+ Age : Age of the patient

+ Sex : Sex of the patient

+ exang: exercise induced angina (1 = yes; 0 = no)

+ ca: number of major vessels (0-3)

+ cp : Chest Pain type chest pain type

  + Value 1: typical angina

  + Value 2: atypical angina

  + Value 3: non-anginal pain

  + Value 4: asymptomatic

+ trtbps : resting blood pressure (in mm Hg)

+ chol : cholestoral in mg/dl fetched via BMI sensor

+ fbs : (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)

+ rest_ecg : resting electrocardiographic results

  + Value 0: normal

  + Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)

  + Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria

  + thalach : maximum heart rate achieved

+ target : 0= less chance of heart attack 1= more chance of heart attack


#### [Resources](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset) 

### Overview

This project creates a Python script using Pandas for descriptive statistics. The specific steps involve: 

+ Create a Phython script

  + Read a dataset (CSV)

  + Generate summary statistics (mean, median, standard deviation)

  + Create data visualizations

+ Generate summary report (PDF)
  
### Description

Step 1: In the requirements.txt, I added pandas 2.1.0 and matplotlib==3.7.2. 

<img width="914" alt="Screen Shot 2023-09-11 at 12 56 29 AM" src="https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/29707693-8415-4eeb-b754-53140f1bbf54">


Step 2: In the main.py, I created a Python Script. It includes 

       + a `readfile` function, which reads a CSV file.
       
       + a 'summary' function which generates summary statistics for the numeric columns in the DataFrame heart.csv.

       + a 'median' function which calculate the median value for each column in heart.csv

       + a 'histogram' function which generate histogram for each column in heart.csv

       + a 'scatter_age_blood_pressure' function which generate scatter plot with fitted line for the 4th column (resting blood pressure) and the 1st column (age) in heart.csv

<img width="905" alt="Screen Shot 2023-09-11 at 12 57 11 AM" src="https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/0bc88d4b-3872-4527-a362-ce270f592a33">

<img width="798" alt="Screen Shot 2023-09-11 at 12 57 40 AM" src="https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/17b904d4-5058-406a-8cff-925a905facff">

<img width="892" alt="Screen Shot 2023-09-11 at 9 30 08 AM" src="https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/3edff112-b69d-4238-a769-cf5b36039231">


Step 3: In the `test_main.py`, I wrote two test functions `test_readfile` and `test_median`, which checks the summary statistics of `heart.csv`.

       + check the mean value of the fourth column (resting blood pressure)
       
       + check the median value of the fourth column (resting blood pressure)
       
       + check the standard deviation value of the fourth column (resting blood pressure)

<img width="750" alt="Screen Shot 2023-09-11 at 12 58 25 AM" src="https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/5ee5aa36-4d13-4387-a849-7fe3e6d2c239">


Step 4: I generated [Data Visualizations](Data_Visualization.html)

+ summary statistics

<img width="1013" alt="Screen Shot 2023-09-11 at 1 12 52 AM" src="https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/c0027011-01fa-4641-b1db-2bc16fc0b837">

+ median values

<img width="916" alt="Screen Shot 2023-09-11 at 1 13 15 AM" src="https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/50e1b86f-4158-4333-984a-4d32e5b2fb42">

+ histogram of each column

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/698dc927-6391-4266-8dcc-fa475a9df65a)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/658fd114-57b4-4d5d-a65a-a4f397e38248)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/aded97be-f769-47a9-81b1-4f5efe5118a5)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/46f27fd7-f0ab-45af-9ecd-33a0403cc631)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/bbe3d598-306d-4ed3-b3dc-61c8a37438a5)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/0ad57724-7e35-4d8a-8f8f-a50541f7a050)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/212788dc-c385-4953-a8d8-c8fc8cceac6f)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/861c299c-d037-45b4-9d0f-de29e1ca4de7)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/f4d65bca-c483-4866-a734-0576b5076cdb)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/c8c2ae73-95c9-410f-849b-4880bbcdcb66)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/e786fbf7-f238-48ef-9f26-705967b8843a)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/4f775859-6b73-4cfa-af1b-0e8bdd34b7b3)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/46be7348-fd3c-41c9-a608-bd1c8921c1f7)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/2c5310b6-e218-4727-8c7f-59072ff97f8d)

+ scatter plot for resting blood pressure and age in heart.csv

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/31a73193-129e-47dd-ac9b-d7a87e974f84)


Step 5: I generated the summary report (PDF) from Jupyter Notebook

#### [Summary Report PDF](Summary-Report.pdf)

### Check Format and Test Approval Image

+ install code `make install`
  
<img width="1067" alt="Screen Shot 2023-09-08 at 4 53 59 PM" src="https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/84203fec-f516-4f85-8cd2-0b0e2eaced38">

+ lint code `make lint`
+ format code `make format`
+ test code `make test`

<img width="1001" alt="Screen Shot 2023-09-10 at 11 58 29 PM" src="https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/96b1d4cf-7e38-435c-aafb-0c8de8a2de97">

+ code `make all` executes install, lint, format, and test targets

<img width="992" alt="Screen Shot 2023-09-10 at 11 59 16 PM" src="https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/00408673-e649-49f7-a4c5-e8e2f3777a5f">

