import pandas as pd
from db_utils import create_df

class DataTransform:
    def __init__(self):
        pass
    
    def date_format(self, dataframe, *args):
        for col in args:
            dataframe[col] = pd.to_datetime(dataframe[col], format='%b-%Y', errors='coerce')
        return(dataframe)
    
    def employment_number_system(self, dataframe, col):
        map_dict = {'<1 year':'1', '1 year':'2', '2 years':'3', '3 years':'4', '4 years':'5', '5 years':'6', '6 years':'7', '7 years':'8', '8 years':'9', '9 years':'10', '10+ years':'11'}
        dataframe[col] = dataframe[col].map(map_dict)
        dataframe[col] = pd.to_numeric(dataframe[col], downcast='signed', errors='coerce')
        return(dataframe)
    
    def numeric_format(self, dataframe, col, phrase):
        dataframe[col] = dataframe[col].str.replace(f'{phrase}', '')
        dataframe[col] = pd.to_numeric(dataframe[col], downcast='signed', errors='coerce')
        return(dataframe)
    
    def impute_data_median(self, dataframe, *args):
        for col in args:
            dataframe[col] = dataframe[col].fillna(dataframe[col].median())
        return(dataframe)
    
    def impute_data_mean(self, dataframe, *args):
        for col in args:
            dataframe[col] = dataframe[col].fillna(dataframe[col].mean())
        return(dataframe)

class DataFrameInfo:
    def __init__(self):
        pass
    
    def df_data_types(self, dataframe):
        print('DataFrame data types:\n', dataframe.dtypes)
    
    def df_statistical_values(self, dataframe):
        print('DataFrame statistical values:\n', dataframe.describe())

    def column_basic_statistics(self, dataframe, *args):
        for col in args:
            mean_value = round(dataframe[col].mean(), 2)
            median_value = round(dataframe[col].median(), 2)
            mode_value = (dataframe[col].mode()[0])
            std_value = round(dataframe[col].std(), 2)
            print(f'{col}: Mean={mean_value}, Median={median_value}, Mode={mode_value}, Standard deviation={std_value}')
    
    def categorical_distinct_values(self, dataframe):
        col_list=['term', 'grade', 'sub_grade', 'employment_length', 'home_ownership', 'verification_status', 'loan_status', 'payment_plan', 'purpose', 'policy_code', 'application_type']
        print('DataFrame count distinct values of categorical data:\n', dataframe[col_list].nunique())
    
    def df_shape(self, dataframe):
        print('DataFrame shape:\n', dataframe.shape)
    
    def df_null_percent(self, dataframe):
        print('DataFrame percentage of null values:\n', round(dataframe.isnull().sum()/len(dataframe)*100, 2))
        
