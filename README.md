# EDA - Customer Loans in Finance
EDA project with AiCore's data analytics course
## Table of contents 
- [Introduction](#subheading-1)
- [Getting started](#subheading-2)
- [Learnings](#subheading-3)

## Introduction
Making informed lending decisions starts with understanding the data. In this project, I dive into the world of finance to uncover patterns, risks, and insights in customer loans. Through **data cleaning, visualisation, and statistical analysis**, I explore trends in loan approvals and risks, and identify anomalies in the data. The goal? To transform raw data into valuable insights that help manage risk and improve financial decision-making. 🚀

## Getting started
I structured the project to keep the code organised and easy to manage. The db_utils.py file handles the database connection using an RDSDatabaseConnector class, which connects to the AWS RDS database and extracts the customer loans dataset. The connection details are stored securely in a credentials.yaml file, which is ignored by Git to protect sensitive information. There’s also a function that saves the extracted data as a CSV file locally for easier access during analysis and a create_df function which creates a dataframe from the csv file. 

For working with the data, I created a transformations.py file, which includes three main classes:
- DataTransform - applies transformations to clean and prepare the data.
- DataFrameInfo – helps me quickly check important information about the dataset.
- Plotter – handles visualisations to help spot trends and patterns.
  
All of this comes together in my EDA.ipynb notebook, where I show my full workflow, from loading the data to exploring it through cleaning, analysing, and visualizing.

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

## Learnings

#### Data Cleaning
I learned how to handle messy data by dealing with missing values and using appropriate imputation methods to keep the dataset reliable.

#### Handling Skewness
I gained experience managing skewed data, especially when caused by lots of zeros, and learned when transformations are needed.

#### Outliers and Correlated Data
I understood why outliers and highly correlated features shouldn't always be removed, as they can hold important insights and can represent real data.

#### Workflow and Structure
This project helped me structure my code with reusable classes, making my analysis clear and easy to manage.

