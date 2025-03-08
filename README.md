# EDA - Customer Loans in Finance
EDA project with AiCore's data analytics course
## Table of contents 
- [Introduction](#introduction)
- [Short Summary of Findings](#short-summary-of-findings)
- [Getting Started](#getting-started)
- [Installation Instructions](#installation_instructions)
- [Usage Instructions](#usage_instructions)
- [Learnings](#learnings)

## Introduction
Making informed lending decisions starts with understanding the data. In this project, I dive into the world of finance to uncover patterns, risks, and insights in customer loans. Through **data cleaning, visualisation, and statistical analysis**, I explore trends in loan approvals and risks, and identify anomalies in the data. The goal? To transform raw data into valuable insights that help manage risk and improve financial decision-making. 🚀

## Short Summary of Findings
- Approximately 70.68% of the total loan amounts has been repaid so far
- 1 in 10 loans are 'Charged Off'
- An additional $130 million is projected to be collected over the next six months, as visualized in the bar charts
- **Risk Indicators**: Analysis suggests that certain factors are correlated with default risk, offering insight into which loans are more likely to go unpaid
  - Loans grades F and G show the highest risk, whereas grade A loans appear to be the safest
  - Customers who don't own a home are more at risk
  - A higher DTI is associated with an increased risk of loss
  - Loans with larger amounts, higher interest rates, and higher installment payments have a higher default risk
  
![Analysis visualisation](https://github.com/user-attachments/assets/d9c441be-1ee5-4c72-95f0-4fe0d8a52430)
![Analysis visualisation 2](https://github.com/user-attachments/assets/23fecb3a-1823-4eb1-b751-d20fd4d18f94)
![Analysis visualisation 3](https://github.com/user-attachments/assets/94bcecac-6dac-4d75-804b-b8f4f3fb3f24)

## Getting started
I structured the project to keep the code organised and easy to manage. The db_utils.py file handles the database connection using an RDSDatabaseConnector class, which connects to the AWS RDS database and extracts the customer loans dataset. The connection details are stored securely in a credentials.yaml file, which is ignored by Git to protect sensitive information. There’s also a function that saves the extracted data as a CSV file locally for easier access during analysis and a create_df function which creates a dataframe from the csv file. 

For working with the data, I created a transformations.py file, which includes three main classes:
- DataTransform - applies transformations to clean and prepare the data
- DataFrameInfo – helps me quickly check important information about the dataset
- Plotter – handles visualisations to help spot trends and patterns
- Analysis - performs revenue and repayment analysis
  
All of this comes together in two notebooks:
- EDA.ipynb: This notebook focuses on exploratory data analysis, including data loading, cleaning, and initial visualisations to understand the overall structure and distribution of the data.
- analysis.ipynb: This notebook dives deeper into statistical analyses, examines risk factors, and visualizes key insights such as recovery rates and projected losses.

### Built with
- Python verison 3

### Prerequisites
db_uilts.py file 
- <img height="20" alt="Screenshot import pandas" src="https://github.com/hosna22/EDA-Customer-Loans/blob/main/images/importpd.png" />
- <img height="20" alt="Screenshot import psycopg2" src="https://github.com/hosna22/EDA-Customer-Loans/blob/main/images/importpsy.png" />
- <img height="20" alt="Screenshot import sqlalchemy" src="https://github.com/hosna22/EDA-Customer-Loans/blob/main/images/importeng.png" />
- <img height="20" alt="Screenshot import yaml" src="https://github.com/hosna22/EDA-Customer-Loans/blob/main/images/importyaml.png" />

transformations.py file
- <img height="20" alt="Screenshot import pandas" src="https://github.com/hosna22/EDA-Customer-Loans/blob/main/images/importpandas.png" />
- <img height="20" alt="Screenshot import missingno" src="https://github.com/hosna22/EDA-Customer-Loans/blob/main/images/importmsn.png" />
- <img height="20" alt="Screenshot import matplotlib" src="https://github.com/hosna22/EDA-Customer-Loans/blob/main/images/importplt.png" />
- <img height="20" alt="Screenshot import seaborn" src="https://github.com/hosna22/EDA-Customer-Loans/blob/main/images/importsns.png" />
- <img height="20" alt="Screenshot import numpy" src="https://github.com/hosna22/EDA-Customer-Loans/blob/main/images/importnp.png" />

EDA.ipynb file 
- <img height="20" alt="Screenshot 2025-03-03 at 11 13 07" src="https://github.com/user-attachments/assets/579871da-e49e-4f76-a4dc-5a231e251c6d" />
- <img height="20" alt="Screenshot import pandas" src="https://github.com/hosna22/EDA-Customer-Loans/blob/main/images/importpandas.png" />
- <img height="20" alt="Screenshot import statsmodels" src="https://github.com/user-attachments/assets/6419fde7-78d6-4d6a-ac23-abb3551bb5e0" />

## Installation Instructions
**Clone git repository**
1. Copy the 'HTTPS' URL by clicking '<> Code' above the list of files
2. In your CLI, type 'git clone' then paste the URL. Ensure you're in the location you want to save the files.
3. Press enter

## Usage Instructions
1. The csv file containing the dataset from the AWS database is saved in the repository as 'loan_payments.csv'
  - **SKIP** Normally, you would run the 'db_utils.py' to extract the dataset from the AWS database and save it locally as a csv file. However, you need access to the credentials.yaml file which is confidential. 
2. Open and run the 'EDA.ipynb' notebook. This contains exploratory data analysis where the data is cleaned and transformed.
  - This involved removing and imputing nulls, optimising skewness, checking outliers and identify correlation.
  - The process is explained in the notebook.
3. Open and run the 'analysis.ipynb' notebook. This contains statistical analysis which provides insights, conclusions and visualisations from the dataset. 

## Learnings

#### Data Cleaning
I learned how to handle messy data by dealing with missing values and using appropriate imputation methods to keep the dataset reliable.

#### Handling Skewness
I gained experience managing skewed data, especially when caused by lots of zeros, and learned when transformations are needed.

#### Outliers and Correlated Data
I understood why outliers and highly correlated features shouldn't always be removed, as they can hold important insights and can represent real data.

#### Workflow and Structure
This project helped me structure my code with reusable classes, making my analysis clear and easy to manage.
